"""Measure recorded variety and separate observed days from calendar days."""

import json
import pandas as pd
from common import OUTPUT, load_inputs, save_result

food, daily, baskets = load_inputs()
eligible = daily.loc[daily.variety.notna()].copy()
eligible["breadth_group"] = pd.cut(
    eligible.category_count,
    [0, 5, 10, 20, 1000],
    labels=["1-5", "6-10", "11-20", "21+"],
)
table = eligible.groupby("breadth_group", observed=True).agg(
    days=("variety", "size"),
    mean_variety=("variety", "mean"),
    mean_recorded_calories=("food_calories", "mean"),
)
OUTPUT.mkdir(exist_ok=True)
table.to_csv(OUTPUT / "M02_breadth.csv")
assert int(table.days.sum()) == len(eligible)
calendar = pd.MultiIndex.from_product(
    [sorted(food.Userid.unique()), pd.date_range("2016-01-01", "2016-12-31")],
    names=["Userid", "date"],
)
panel = daily.set_index(["Userid", "date"]).reindex(calendar)
observed = panel.entries.notna()
result = {
    "eligible_days": len(eligible),
    "excluded_days": len(daily) - len(eligible),
    "calendar_user_days": len(panel),
    "observed_days": int(observed.sum()),
    "unobserved_days": int((~observed).sum()),
    "mean_variety_day_weighted": float(eligible.variety.mean()),
    "mean_variety_user_weighted": float(
        eligible.groupby("Userid").variety.mean().mean()
    ),
    "daily_total_equal_item_sum_within_one": int(
        (daily.food_calories - daily.item_calories).abs().le(1).sum()
    ),
    "daily_total_comparison_days": len(daily),
    "breadth": table.reset_index().to_dict(orient="records"),
}
save_result("M02", result)
print(json.dumps(result, indent=2))
