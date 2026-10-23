"""Estimate descriptive next-calendar-day associations with clustered uncertainty."""

import json
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from common import load_inputs, save_result

food, daily, baskets = load_inputs()
future = daily[["Userid", "date", "food_calories"]].copy()
future["date"] -= pd.Timedelta(days=1)
future = future.rename(columns={"food_calories": "next_calories"})
panel = daily.merge(future, on=["Userid", "date"], validate="one_to_one")
panel = panel.loc[panel.food_calories.gt(0) & panel.next_calories.gt(0)].copy()
counts = panel.groupby("Userid").size()
panel = panel.loc[panel.Userid.isin(counts[counts >= 2].index)].copy()
panel["log_next"] = np.log(panel.next_calories)
panel["month"] = panel.date.dt.month
panel["weekday"] = panel.date.dt.dayofweek
assert (panel.next_calories > 0).all()
restricted = panel.loc[
    panel.food_calories.between(100, 5000) & panel.next_calories.between(100, 5000)
].copy()
counts = restricted.groupby("Userid").size()
restricted = restricted.loc[restricted.Userid.isin(counts[counts >= 2].index)]
fits = {}
base = "log_next ~ category_count + C(month) + C(weekday)"
specifications = [
    ("pooled", base, panel),
    ("user_fixed_effects", base + " + C(Userid)", panel),
    ("restricted_fixed_effects", base + " + C(Userid)", restricted),
]
for name, formula, sample in specifications:
    fit = smf.ols(formula, data=sample).fit(
        cov_type="cluster", cov_kwds={"groups": sample.Userid}, use_t=True
    )
    coefficient = float(fit.params["category_count"])
    low, high = map(float, fit.conf_int().loc["category_count"])
    fits[name] = {
        "pairs": len(sample),
        "users": int(sample.Userid.nunique()),
        "coefficient": coefficient,
        "se": float(fit.bse["category_count"]),
        "ci_low": low,
        "ci_high": high,
        "geometric_mean_percent": 100 * float(np.expm1(coefficient)),
    }
result = {
    "pairs": len(panel),
    "users": int(panel.Userid.nunique()),
    "min_next_calories": float(panel.next_calories.min()),
    "max_next_calories": float(panel.next_calories.max()),
    "models": fits,
}
save_result("M03", result)
print(json.dumps(result, indent=2))
