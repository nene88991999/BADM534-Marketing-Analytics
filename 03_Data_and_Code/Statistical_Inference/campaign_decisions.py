"""Hypothetical campaign summaries and expected counts in a test portfolio."""
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

OUTPUT = Path(__file__).resolve().parent / "results"


def campaign(n=1000000, control=100000, treatment=101000,
             margin=40.0, contact_cost=0.10):
    if n <= 0 or not (0 <= control <= n and 0 <= treatment <= n) or margin <= 0:
        raise ValueError("Require valid counts and a positive contribution margin")
    a, b = control / n, treatment / n
    lift = b - a
    pooled = (control + treatment) / (2 * n)
    null_se = np.sqrt(2 * pooled * (1 - pooled) / n)
    se = np.sqrt((a * (1 - a) + b * (1 - b)) / n)
    low, high = lift + np.array([-1, 1]) * stats.norm.ppf(.975) * se
    return {"customers_per_arm": n, "control_conversions": control,
        "treatment_conversions": treatment, "lift": lift,
        "null_se": null_se, "se": se, "z": lift / null_se,
        "p_value": 2 * stats.norm.sf(abs(lift / null_se)),
        "ci95_low": low, "ci95_high": high, "margin_dollars": margin,
        "contact_cost_dollars": contact_cost, "break_even_lift": contact_cost / margin,
        "net_dollars_per_treated_customer": margin * lift - contact_cost,
        "net_ci95_low": margin * low - contact_cost,
        "net_ci95_high": margin * high - contact_cost}


def portfolio(tests=1000, null_fraction=.8, alpha=.05, power=.8):
    if tests <= 0 or not all(0 <= x <= 1 for x in (null_fraction, alpha, power)):
        raise ValueError("Require positive count and probabilities in [0, 1]")
    nulls, effects = tests * null_fraction, tests * (1 - null_fraction)
    false, true = nulls * alpha, effects * power
    rows = [{"truth": "zero_effect", "tests": nulls,
             "expected_reject": false, "expected_nonreject": nulls - false},
            {"truth": "nonzero_effect", "tests": effects,
             "expected_reject": true, "expected_nonreject": effects - true}]
    ratio = false / (false + true) if false + true > 0 else float("nan")
    return pd.DataFrame(rows), ratio


def main():
    OUTPUT.mkdir(exist_ok=True)
    result = pd.DataFrame([campaign()])
    result.to_csv(OUTPUT / "campaign_decision.csv", index=False, float_format="%.12g")
    rows, ratio = portfolio()
    rows.to_csv(OUTPUT / "test_portfolio.csv", index=False, float_format="%.12g")
    sensitivity = []
    for null_fraction in [.2, .5, .8, .95]:
        for power in [.2, .8]:
            _, fraction = portfolio(null_fraction=null_fraction, power=power)
            sensitivity.append({"null_fraction": null_fraction, "alpha": .05,
                "power": power, "ratio_expected_false_to_all_rejections": fraction})
    pd.DataFrame(sensitivity).to_csv(OUTPUT / "portfolio_sensitivity.csv",
                                   index=False, float_format="%.12g")
    print(result.to_string(index=False))
    print(rows.to_string(index=False))
    print("Ratio of expected false to all rejections:", ratio)


if __name__ == "__main__":
    main()
