"""Synthetic discount curves, cross-fitting, overlap, and interval evaluation.

Run: python dose_response.py --output results --repetitions 200
All doses are percentage points; profit is dollars per eligible customer.
The target population places equal weight on X=-1 and X=1.
"""
from pathlib import Path
import argparse
import json
import platform
import numpy as np

GRID = np.linspace(6, 34, 29)
SETTINGS = [(True, True), (True, False), (False, True), (False, False)]


def truth(a):
    return 10 + 0.4 * np.asarray(a) - 0.01 * np.asarray(a) ** 2


def generate(n=2400, seed=20261118, sigma=0.9):
    """Equal numbers of each observed type; no exclusions or missing rows."""
    if n % 2:
        raise ValueError("n must be even")
    rng = np.random.default_rng(seed)
    x = rng.permutation(np.repeat([-1.0, 1.0], n // 2))
    z = 0.9 * x + rng.normal(0, sigma, n)
    a = 40 / (1 + np.exp(-z))
    y = truth(a) + 2 * x + rng.normal(0, 1, n)
    return x, a, y


def outcome_features(x, a, correct=True):
    t = (np.asarray(a) - 20) / 10
    columns = [np.ones_like(t), t, t * t]
    if correct:
        columns.append(np.broadcast_to(x, t.shape))
    return np.column_stack(columns)


def treatment_features(x, correct=True):
    return np.column_stack([np.ones_like(x), x]) if correct else np.ones((len(x), 1))


def density(a, mean, sigma):
    """Logistic-normal density on (0,40), including its Jacobian."""
    a = np.asarray(a)
    z = np.log(a / (40 - a))
    return (np.exp(-0.5 * ((z - mean) / sigma) ** 2)
            / (np.sqrt(2 * np.pi) * sigma) * 40 / (a * (40 - a)))


def pseudo_outcome(x, a, y, outcome_correct=True, gps_correct=True, cap=None, seed=71):
    """Five folds; train each nuisance only on the other four folds.

    Standardization uses the stated equal-type target population. The wrong
    outcome model omits X; the wrong dose model omits X on the logit scale.
    cap is a fixed maximum weight, not an estimated quantile.
    """
    fold = np.random.default_rng(seed).permutation(np.arange(len(y)) % 5)
    xi, raw_weight = np.empty_like(y), np.empty_like(y)
    for k in range(5):
        tr, te = fold != k, fold == k
        b = np.linalg.lstsq(outcome_features(x[tr], a[tr], outcome_correct), y[tr], rcond=None)[0]
        mu = outcome_features(x[te], a[te], outcome_correct) @ b
        marginal_mu = sum(outcome_features(g, a[te], outcome_correct) @ b for g in [-1, 1]) / 2
        z = np.log(a[tr] / (40 - a[tr]))
        design = treatment_features(x[tr], gps_correct)
        c = np.linalg.lstsq(design, z, rcond=None)[0]
        sigma = np.sqrt(np.mean((z - design @ c) ** 2))
        observed_mean = treatment_features(x[te], gps_correct) @ c
        conditional = density(a[te], observed_mean, sigma)
        marginal = sum(density(a[te], treatment_features(np.full(te.sum(), g), gps_correct) @ c,
                               sigma) for g in [-1, 1]) / 2
        raw_weight[te] = marginal / conditional
        weight = raw_weight[te] if cap is None else np.minimum(raw_weight[te], cap)
        xi[te] = marginal_mu + weight * (y[te] - mu)
    return xi, raw_weight


def smooth(a, y, grid=GRID, bandwidth=2.0):
    """Local linear Gaussian smoother and conditional HC0 standard error.

    This standard error holds fitted pseudo-outcomes fixed. It omits nuisance
    estimation and smoothing bias; its coverage is evaluated, never presumed.
    """
    delta = np.asarray(a)[:, None] - np.asarray(grid)[None, :]
    w = np.exp(-0.5 * (delta / bandwidth) ** 2)
    s0, s1, s2 = w.sum(0), (w * delta).sum(0), (w * delta**2).sum(0)
    determinant = s0 * s2 - s1**2
    if np.any(determinant <= 1e-14):
        raise ValueError("Insufficient local variation at an evaluation dose")
    linear_weights = w * (s2 - delta * s1) / determinant
    slope_weights = w * (delta * s0 - s1) / determinant
    estimate = linear_weights.T @ y
    slope = slope_weights.T @ y
    residual = y[:, None] - estimate - delta * slope
    se = np.sqrt(((linear_weights * residual) ** 2).sum(0))
    return estimate, se


def plr_slope(x, a, y):
    """Cross-fitted Robinson partialling-out slope, with binary-X nuisances."""
    fold = np.random.default_rng(71).permutation(np.arange(len(y)) % 5)
    ra, ry = np.empty_like(a), np.empty_like(y)
    design = treatment_features(x)
    for k in range(5):
        tr, te = fold != k, fold == k
        ra[te] = a[te] - design[te] @ np.linalg.lstsq(design[tr], a[tr], rcond=None)[0]
        ry[te] = y[te] - design[te] @ np.linalg.lstsq(design[tr], y[tr], rcond=None)[0]
    return float(ra @ ry / (ra @ ra))


def hidden_confounding(grid=GRID):
    """Exact observable-data regression with an omitted independent U in {-1,1}.

    Z=.9X+.8U+Normal(0,.9), Y=truth(A)+2X+2U+noise. Bayes' rule gives
    E[U|Z,X]=tanh(.8*(Z-.9X)/.9**2). Both observable nuisance functions could
    be known exactly and adjustment for X would still miss the causal curve.
    """
    z = np.log(grid / (40 - grid))
    observed = truth(grid) + sum(2 * np.tanh(0.8 * (z - 0.9 * g) / 0.9**2)
                                for g in [-1, 1]) / 2
    return observed


def save_table(path, columns, rows):
    np.savetxt(path, np.asarray(rows), delimiter=",", header=",".join(columns), comments="", fmt="%.10g")


def run(output, repetitions=200):
    output.mkdir(parents=True, exist_ok=True)
    x, a, y = generate()
    save_table(output / "customers.csv", ["type", "discount_pp", "profit_usd"], np.c_[x, a, y])
    reference, curve_columns, curves = [], ["discount_pp", "truth_usd"], [GRID, truth(GRID)]
    for oc, gc in SETTINGS:
        name = f"outcome_{int(oc)}_density_{int(gc)}"
        xi, w = pseudo_outcome(x, a, y, oc, gc)
        est, se = smooth(a, xi)
        reference.append({"model": name, "rmse_usd": float(np.sqrt(np.mean((est-truth(GRID))**2))),
                          "weight_max": float(w.max()), "ess_rows": float(w.sum()**2/(w@w))})
        curve_columns.extend([name, name + "_conditional_se"])
        curves.extend([est, se])
    save_table(output / "curves.csv", curve_columns, np.column_stack(curves))
    evaluation, point_rows = [], []
    for oc, gc in SETTINGS:
        cover, whole, rmse, bias = [], [], [], []
        for r in range(repetitions):
            xr, ar, yr = generate(seed=10000+r)
            xi, _ = pseudo_outcome(xr, ar, yr, oc, gc)
            est, se = smooth(ar, xi)
            error = est - truth(GRID)
            hit = np.abs(error) <= 1.96 * se
            cover.append(hit); whole.append(hit.all())
            rmse.append(np.sqrt(np.mean(error**2))); bias.append(error)
        point_cover = np.mean(cover, axis=0)
        evaluation.append({"outcome_correct": oc, "density_correct": gc,
                           "mean_rmse_usd": float(np.mean(rmse)),
                           "mean_pointwise_coverage": float(point_cover.mean()),
                           "whole_grid_coverage_of_pointwise_intervals": float(np.mean(whole))})
        for dose, coverage, mean_bias in zip(GRID, point_cover, np.mean(bias, axis=0)):
            point_rows.append([int(oc), int(gc), dose, coverage,
                               np.sqrt(coverage*(1-coverage)/repetitions), mean_bias])
    save_table(output / "coverage.csv", ["outcome_correct", "density_correct", "discount_pp",
               "pointwise_coverage", "monte_carlo_se", "mean_bias_usd"], point_rows)
    overlap = []
    for sigma in [0.9, 0.22]:
        xx, aa, yy = generate(sigma=sigma)
        for cap in [None, 5.0]:
            xi, w = pseudo_outcome(xx, aa, yy, False, True, cap=cap)
            estimate, _ = smooth(aa, xi)
            used = w if cap is None else np.minimum(w, cap)
            overlap.append({"sigma": sigma, "cap": cap, "max_raw_weight": float(w.max()),
                            "ess_rows": float(used.sum()**2/(used@used)),
                            "rmse_usd": float(np.sqrt(np.mean((estimate-truth(GRID))**2)))})
    dose = np.linspace(1, 39, 153)
    save_table(output / "overlap.csv", ["discount_pp", "broad_minus", "broad_plus", "narrow_minus", "narrow_plus"],
               np.c_[dose, density(dose, -.9, .9), density(dose, .9, .9),
                     density(dose, -.9, .22), density(dose, .9, .22)])
    save_table(output / "hidden_confounding.csv", ["discount_pp", "causal_profit_usd", "adjusted_association_usd"],
               np.c_[GRID, truth(GRID), hidden_confounding()])
    report = {"seed": 20261118, "n": len(y), "repetitions": repetitions,
              "python": platform.python_version(), "numpy": np.__version__,
              "grid_pp": [6, 34, 1], "bandwidth_pp": 2.0,
              "reference": reference, "plr_slope_usd_per_pp": plr_slope(x, a, y),
              "simulation": evaluation, "overlap": overlap,
              "hidden_confounding_max_bias_usd": float(np.max(np.abs(hidden_confounding()-truth(GRID)))),
              "scope": "Synthetic fixed-design evaluations. Intervals are conditional HC0 pointwise approximations; no simultaneous-band guarantee."}
    (output / "summary.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parent / "results")
    parser.add_argument("--repetitions", type=int, default=200)
    args = parser.parse_args()
    if args.repetitions < 2:
        parser.error("Use at least two independent repetitions")
    run(args.output, args.repetitions)
