"""Evaluate false-positive rates with a store-randomized zero-effect promotion."""
import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "results"
SEED = 20261125
REPETITIONS = 4000
STORES = 40
CUSTOMERS = 20
VARIANCE = 800.0
CORRELATIONS = (0.0, 0.1, 0.3, 0.5)
ALPHA = .05


def welch(a, b):
    """Treat rows as experiments and columns as independent observations."""
    a, b = np.atleast_2d(a), np.atleast_2d(b)
    if min(a.shape[1], b.shape[1]) < 2:
        raise ValueError("Each arm needs at least two independent observations")
    v0, v1 = a.var(axis=1, ddof=1) / a.shape[1], b.var(axis=1, ddof=1) / b.shape[1]
    se = np.sqrt(v0 + v1)
    if np.any(se == 0):
        raise ValueError("A positive contrast variance is required")
    df = (v0 + v1) ** 2 / (v0 ** 2 / (a.shape[1]-1) + v1 ** 2 / (b.shape[1]-1))
    effect = b.mean(axis=1) - a.mean(axis=1)
    p = 2 * stats.t.sf(np.abs(effect / se), df)
    return effect, se, df, p


def compare_methods(outcomes, treated):
    """Equal store sizes make both point estimates identical."""
    r, g, m = outcomes.shape
    if treated.shape != (r, g) or g % 2 or not np.all(treated.sum(axis=1) == g//2):
        raise ValueError("Exactly half the stores must receive the promotion")
    customer0 = outcomes[~treated].reshape(r, g//2*m)
    customer1 = outcomes[treated].reshape(r, g//2*m)
    store_means = outcomes.mean(axis=2)
    store0 = store_means[~treated].reshape(r, g//2)
    store1 = store_means[treated].reshape(r, g//2)
    return {"customer_rows": welch(customer0, customer1),
            "store_means": welch(store0, store1)}


def wilson(successes, total):
    """Monte Carlo uncertainty for a rejection fraction, not an effect interval."""
    z = stats.norm.ppf(.975)
    p = successes / total
    center = (p + z*z/(2*total)) / (1 + z*z/total)
    half = z * np.sqrt(p*(1-p)/total + z*z/(4*total*total)) / (1 + z*z/total)
    return float(center-half), float(center+half)


def simulate(repetitions=REPETITIONS, stores=STORES, customers=CUSTOMERS, seed=SEED):
    if repetitions < 2 or stores < 4 or stores % 2 or customers < 2:
        raise ValueError("Use two repetitions, an even store count >=4, and >=2 customers")
    rng = np.random.default_rng(seed)
    # Shared Gaussian draws and assignments make the rho comparisons paired.
    store_shock = rng.normal(size=(repetitions, stores, 1))
    customer_shock = rng.normal(size=(repetitions, stores, customers))
    order = np.argsort(rng.random((repetitions, stores)), axis=1)
    treated = np.zeros((repetitions, stores), dtype=bool)
    treated[np.arange(repetitions)[:, None], order[:, :stores//2]] = True
    summaries, examples, first_data = [], [], None
    for rho in CORRELATIONS:
        # Potential outcomes are identical under promotion and control.
        y = (100 + np.sqrt(VARIANCE*rho)*store_shock
             + np.sqrt(VARIANCE*(1-rho))*customer_shock)
        results = compare_methods(y, treated)
        if not np.allclose(results["customer_rows"][0], results["store_means"][0]):
            raise AssertionError("Equal-size point estimates differ")
        for method, (effect, se, df, p) in results.items():
            rejected = int((p < ALPHA).sum())
            low, high = wilson(rejected, repetitions)
            summaries.append({"rho": rho, "method": method, "repetitions": repetitions,
                "rejections": rejected, "rejection_rate": rejected/repetitions,
                "mc_ci_low": low, "mc_ci_high": high, "mean_effect_dollars": effect.mean(),
                "empirical_effect_sd": effect.std(ddof=1), "mean_reported_se": se.mean(),
                "theoretical_effect_sd": np.sqrt(4*VARIANCE/stores*(rho+(1-rho)/customers)),
                "design_effect": 1+(customers-1)*rho})
            critical = stats.t.ppf(.975, df[0])
            examples.append({"rho": rho, "method": method, "repetition": 0,
                "effect_dollars": effect[0], "se_dollars": se[0], "df": df[0],
                "p_value": p[0], "ci_low": effect[0]-critical*se[0],
                "ci_high": effect[0]+critical*se[0]})
        if rho == .3:
            first_data = pd.DataFrame({"store": np.repeat(np.arange(stores), customers),
                "customer": np.tile(np.arange(customers), stores),
                "assigned_promotion": np.repeat(treated[0].astype(int), customers),
                "contribution_dollars": y[0].ravel()})
    return pd.DataFrame(summaries), pd.DataFrame(examples), first_data


def main():
    summary, examples, data = simulate()
    OUTPUT.mkdir(exist_ok=True)
    summary.to_csv(OUTPUT / "null_calibration.csv", index=False)
    examples.to_csv(OUTPUT / "first_experiment.csv", index=False)
    data.to_csv(OUTPUT / "synthetic_store_customers.csv", index=False)
    setup = {"seed": SEED, "repetitions_per_rho": REPETITIONS, "stores": STORES,
             "customers_per_store": CUSTOMERS, "treated_stores": STORES//2,
             "outcome_variance": VARIANCE, "mean_contribution_dollars": 100,
             "true_effect_dollars": 0, "within_store_correlations": CORRELATIONS,
             "alpha": ALPHA, "hypotheses_per_experiment": 1,
             "outcome": "synthetic net contribution per customer in dollars",
             "model_api_calls": 0}
    (OUTPUT / "simulation.json").write_text(json.dumps(setup, indent=2) + "\n")
    print(summary[["rho", "method", "rejections", "rejection_rate", "mean_reported_se"]]
          .to_string(index=False))


if __name__ == "__main__":
    main()
