"""Synthetic numerical examples for M3; run from any working directory."""

import itertools
import json
import math
from example_helpers import write_csv, ols_slope, shares

r = {}
low = [(1, 9), (2, 8), (3, 7)]
high = [(4, 16), (5, 15), (6, 14)]
write_csv(
    "M03_rivals_synthetic.csv",
    ["demand_group", "rival_count", "sales_illustrative_units"],
    [("low", x, y) for x, y in low] + [("high", x, y) for x, y in high],
)
r["M03"] = {
    "pooled": ols_slope(low + high),
    "low": ols_slope(low),
    "high": ols_slope(high),
    "simple_sales_fit": ols_slope([(1, 3), (2, 5), (3, 7)]),
    "coefficient_ci": [2 - 1.96 * 0.5, 2 + 1.96 * 0.5],
}
assert math.isclose(r["M03"]["pooled"]["slope"], 11 / 7)
assert r["M03"]["low"]["slope"] == r["M03"]["high"]["slope"] == -1
print(json.dumps(r, indent=2))
