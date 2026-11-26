"""Hypothetical cancellation-time summaries with prespecified +/-5 second bounds."""
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

OUTPUT = Path(__file__).resolve().parent / "results"
BOUND, ALPHA = 5.0, .05
# Each scenario is a separate hypothetical parallel-group experiment.
CASES = [("imprecise", 50, 60.0, 64.0, 20.0),
         ("precise_small", 800, 60.0, 60.5, 20.0),
         ("detectable_small", 800, 60.0, 63.0, 20.0),
         ("faster", 800, 60.0, 54.0, 20.0)]


def assess(name, n, control_mean, treatment_mean, sample_sd, bound=BOUND):
    if n < 2 or sample_sd <= 0 or bound <= 0:
        raise ValueError("Require at least two customers per arm, positive SD and bound")
    delta = treatment_mean - control_mean
    df = 2 * n - 2
    se = sample_sd * np.sqrt(2 / n)
    p_zero = 2 * stats.t.sf(abs(delta / se), df)
    lower_p = stats.t.sf((delta + bound) / se, df)
    upper_p = stats.t.cdf((delta - bound) / se, df)
    half90 = stats.t.ppf(1 - ALPHA, df) * se
    half95 = stats.t.ppf(1 - ALPHA / 2, df) * se
    return {"case": name, "n_per_arm": n, "control_mean_seconds": control_mean,
        "treatment_mean_seconds": treatment_mean, "sd_each_arm_seconds": sample_sd,
        "estimate_seconds": delta, "se_seconds": se, "df": df,
        "p_zero": p_zero, "lower_bound_seconds": -bound, "upper_bound_seconds": bound,
        "tost_lower_p": lower_p, "tost_upper_p": upper_p,
        "tost_p": max(lower_p, upper_p), "equivalent": max(lower_p, upper_p) < ALPHA,
        "ci90_low": delta - half90, "ci90_high": delta + half90,
        "ci95_low": delta - half95, "ci95_high": delta + half95,
        "noninferior_below_upper_bound": upper_p < ALPHA}


def main():
    OUTPUT.mkdir(exist_ok=True)
    result = pd.DataFrame([assess(*case) for case in CASES])
    result.to_csv(OUTPUT / "equivalence_claims.csv", index=False, float_format="%.12g")
    print(result.to_string(index=False))


if __name__ == "__main__":
    main()
