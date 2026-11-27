"""A finite synthetic DiD population with a treatment-affected covariate."""
import csv
from itertools import product
from pathlib import Path
import numpy as np

OUT = Path(__file__).resolve().parent / "results"


def fit(y, columns, weights):
    x = np.column_stack([np.ones(len(y)), *columns])
    root = np.sqrt(weights)
    assert np.linalg.matrix_rank(x * root[:, None]) == x.shape[1]
    return np.linalg.lstsq(x * root[:, None], y * root, rcond=None)[0]


def calculate():
    rows = []
    # W precedes treatment. X0 is constant and provides no extra information.
    for w, d, u, e in product([0, 1], [0, 1], [-1, 1], [-1, 1]):
        propensity = .25 + .5 * w
        weight = .5 * (propensity if d else 1 - propensity) * .25
        x_untreated = w + u
        rows.append(dict(w=w, d=d, u=u, e=e, weight=weight, x0=0,
                         x1_untreated=x_untreated,
                         x1_observed=x_untreated + 2 * d,
                         y0=100, y1=100 + 4 * d + 3 * x_untreated + e))
    values = {k: np.array([r[k] for r in rows]) for k in rows[0]}
    d, w, mass = values["d"], values["w"], values["weight"]
    dy = values["y1"] - values["y0"]
    x = values["x1_observed"]
    treated, untreated = d == 1, d == 0
    assert np.isclose(mass.sum(), 1) and np.isclose(mass[treated].sum(), .5)
    assert np.isclose(np.average(w[treated], weights=mass[treated]), .75)
    assert np.isclose(np.average(w[untreated], weights=mass[untreated]), .25)
    # Learn the untreated outcome trend only among untreated units.
    outcome_fit = fit(dy[untreated], [x[untreated]], mass[untreated])
    # Learn untreated X1 conditional on W, again only among untreated units.
    covariate_fit = fit(x[untreated], [w[untreated]], mass[untreated])
    expected_x0 = covariate_fit[0] + covariate_fit[1] * w[treated]
    expected_trend = outcome_fit[0] + outcome_fit[1] * expected_x0
    imputation = np.average(dy[treated] - expected_trend,
                            weights=mass[treated])
    estimates = {
        "omit_covariates_or_use_constant_baseline": fit(dy, [d], mass)[1],
        "adjust_for_observed_post_treatment_x": fit(dy, [d, x], mass)[1],
        "adjust_for_observed_pre_treatment_w": fit(dy, [d, w], mass)[1],
        "untreated_covariate_imputation": imputation,
    }
    analytical = [5.5, -2, 4, 4]
    result = []
    for (name, estimate), expected in zip(estimates.items(), analytical):
        assert np.isclose(estimate, expected)
        result.append(dict(method=name, estimate=float(estimate),
                           true_att=4, analytical=expected))
    return rows, result


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    for name, rows in zip(["panel_population.csv", "panel_estimates.csv"],
                          calculate()):
        with (OUT / name).open("w", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
    for row in calculate()[1]:
        print(row["method"], round(row["estimate"], 6))
