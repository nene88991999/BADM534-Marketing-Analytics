"""Repeated store experiments with known zero and nonzero dollar effects."""
import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

OUTPUT = Path(__file__).resolve().parent / "results"
SEED, REPETITIONS, ALPHA = 20261126, 20000, 0.05
STORES, EFFECTS = (40, 160), (0.0, 8.0)
CUSTOMERS, CUSTOMER_VARIANCE, RHO = 20, 800.0, 0.3
STORE_VARIANCE = CUSTOMER_VARIANCE * (RHO + (1 - RHO) / CUSTOMERS)


def pooled_test(control, treatment):
    """Rows are experiments; columns are independent equal-variance stores."""
    a, b = np.asarray(control), np.asarray(treatment)
    if a.ndim != 2 or b.shape != a.shape or a.shape[1] < 2:
        raise ValueError("Require equally sized two-dimensional groups")
    n = a.shape[1]
    effect = b.mean(axis=1) - a.mean(axis=1)
    se = np.sqrt((a.var(axis=1, ddof=1) + b.var(axis=1, ddof=1)) / n)
    df = 2 * n - 2
    p = 2 * stats.t.sf(np.abs(effect / se), df)
    return effect, se, p


def run(repetitions=REPETITIONS, seed=SEED):
    rng = np.random.default_rng(seed)
    summaries, bins, examples = [], [], []
    edges = np.linspace(0, 1, 21)
    for stores in STORES:
        n, df = stores // 2, stores - 2
        # Integrating the Gaussian customer shocks gives independent store means.
        groups = rng.normal(100, np.sqrt(STORE_VARIANCE),
                            size=(2, 2, repetitions, n))
        for truth in EFFECTS:
            estimates = []
            for repeat in range(2):
                estimates.append(pooled_test(groups[repeat, 0],
                                             groups[repeat, 1] + truth))
            effect, se, p = estimates[0]
            p_repeat = estimates[1][2]
            rejects = p < ALPHA
            critical = stats.t.ppf(1 - ALPHA / 2, df)
            true_se = np.sqrt(4 * STORE_VARIANCE / stores)
            ncp = truth / true_se
            power = stats.nct.cdf(-critical, df, ncp)
            power += stats.nct.sf(critical, df, ncp)
            summaries.append({"stores": stores, "true_effect_dollars": truth,
                "experiments": repetitions, "rejections": int(rejects.sum()),
                "rejection_rate": rejects.mean(), "analytical_power": power,
                "mc_standard_error": np.sqrt(power * (1 - power) / repetitions),
                "mean_estimate_dollars": effect.mean(),
                "estimate_sd_dollars": effect.std(ddof=1),
                "analytical_se_dollars": true_se,
                "estimate_q025": np.quantile(effect, .025),
                "estimate_q975": np.quantile(effect, .975),
                "ci95_coverage": (np.abs(effect - truth) <= critical * se).mean(),
                "repeat_rejections_after_rejection": int((rejects & (p_repeat < ALPHA)).sum()),
                "repeat_rate_after_rejection": (p_repeat[rejects] < ALPHA).mean()})
            counts, _ = np.histogram(p, bins=edges)
            for lo, hi, count in zip(edges[:-1], edges[1:], counts):
                bins.append({"stores": stores, "true_effect_dollars": truth,
                    "bin_left": lo, "bin_right": hi, "count": int(count),
                    "fraction": count / repetitions})
            # Retain the first draw, with no selection on significance.
            examples.append({"stores": stores, "true_effect_dollars": truth,
                "estimate_dollars": effect[0], "se_dollars": se[0],
                "p_value": p[0], "replication_p_value": p_repeat[0]})
    return pd.DataFrame(summaries), pd.DataFrame(bins), pd.DataFrame(examples)


def main():
    OUTPUT.mkdir(exist_ok=True)
    frames = run()
    for name, frame in zip(("pvalue_summary", "pvalue_bins", "pvalue_first"), frames):
        frame.to_csv(OUTPUT / (name + ".csv"), index=False, float_format="%.12g")
    setup = {"seed": SEED, "experiments_per_scenario": REPETITIONS,
        "independent_draws_per_pair": 2, "stores": STORES, "effects_dollars": EFFECTS,
        "customers_per_store": CUSTOMERS, "within_store_correlation": RHO,
        "customer_variance": CUSTOMER_VARIANCE, "store_mean_variance": STORE_VARIANCE,
        "alpha": ALPHA, "test": "two-sided equal-variance pooled Student t on store means",
        "scope": "Gaussian independent stores, balanced groups, one fixed-horizon test"}
    (OUTPUT / "pvalue_setup.json").write_text(json.dumps(setup, indent=2) + "\n")
    print(frames[0].to_string(index=False))


if __name__ == "__main__":
    main()
