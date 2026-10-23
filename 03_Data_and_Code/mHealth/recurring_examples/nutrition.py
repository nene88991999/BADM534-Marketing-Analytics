"""Domain-informed sample definitions and explicitly hypothetical energy screens."""

import json
import math
import numpy as np
from common import load_inputs, save_result


def goldberg_bounds(days, pal, cv_intake=23, cv_bmr=8.5, cv_pal=15):
    """Individual EI:BMR bounds with Black (2000) coefficients, z=2, n=1."""
    if days < 1 or pal <= 0:
        raise ValueError("Positive assessment duration and PAL are required")
    variation = math.sqrt(cv_intake**2 / days + cv_bmr**2 + cv_pal**2) / 100
    return pal * math.exp(-2 * variation), pal * math.exp(2 * variation)


def run_analysis():
    food, daily, baskets = load_inputs()
    age_counts = food.groupby("Userid").Age_at_2016_01_01.nunique(dropna=False)
    assert age_counts.eq(1).all()
    ages = food.groupby("Userid").Age_at_2016_01_01.first()
    daily["age"] = daily.Userid.map(ages)
    # Nonnegative category calories and a positive denominator define valid shares.
    base = daily.loc[
        daily.variety.notna()
        & daily.food_calories.gt(0)
        & np.isfinite(daily.food_calories)
        & daily.age.ge(18)
    ].copy()
    training = base.loc[base.date.lt("2016-07-01")]
    lower, upper = training.food_calories.quantile([0.01, 0.99])
    masks = {
        "adult_positive_base": base.food_calories.gt(0),
        "fixed_100_to_5000_sensitivity": base.food_calories.between(100, 5000),
        "prior_period_1st_to_99th_percentile": base.food_calories.between(lower, upper),
        "daily_item_agreement_within_one": (base.food_calories - base.item_calories)
        .abs()
        .le(1),
    }
    summaries = []
    for name, mask in masks.items():
        selected = base.loc[mask]
        summaries.append(
            {
                "rule": name,
                "days": len(selected),
                "users": int(selected.Userid.nunique()),
                "removed_from_base": len(base) - len(selected),
                "mean_recorded_calories": float(selected.food_calories.mean()),
                "mean_variety": float(selected.variety.mean()),
            }
        )
    # Hypothetical complete records, stable energy balance, and predicted BMR.
    # These BMR/PAL inputs are imposed; no mHealth participant is classified.
    scenario = []
    for days in [1, 7]:
        for pal in [1.55, 1.80]:
            lo, hi = goldberg_bounds(days, pal)
            scenario.append(
                {
                    "days": days,
                    "assumed_pal": pal,
                    "bmr_kcal": 1500,
                    "lower_ratio": lo,
                    "upper_ratio": hi,
                    "lower_kcal": 1500 * lo,
                    "upper_kcal": 1500 * hi,
                    "illustrative_1600_kcal_flag": 1600 / 1500 < lo,
                }
            )
    result = {
        "source_observed_days": len(daily),
        "base_days": len(base),
        "base_removed_days": len(daily) - len(base),
        "age_min": float(ages.min()),
        "age_max": float(ages.max()),
        "training_days": len(training),
        "quantile_lower": float(lower),
        "quantile_upper": float(upper),
        "sensitivity": summaries,
        "hypothetical_goldberg": scenario,
    }
    save_result("nutrition", result)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    run_analysis()
