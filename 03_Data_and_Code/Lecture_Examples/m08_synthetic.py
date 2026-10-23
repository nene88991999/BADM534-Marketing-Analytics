"""Synthetic numerical examples for M8; run from any working directory."""

import itertools
import json
import math
from example_helpers import write_csv, ols_slope, shares

r = {}
items = {
    "A": ("Coffee", 0.90),
    "B": ("Coffee", 0.85),
    "C": ("Tea", 0.75),
    "D": ("Fruit", 0.65),
}
list_values = {}
for weight in [0, 0.2, 0.3]:
    list_values[str(weight)] = {
        "".join(choice): sum(items[j][1] for j in choice)
        + weight * len({items[j][0] for j in choice})
        for choice in itertools.combinations(items, 3)
    }
ra = lambda s: 100 * (-math.expm1(-s / 20))
rb = lambda s: 80 * (-math.expm1(-s / 40))
sa = (40 * math.log(2.5) + 60) / 3
sb = 60 - sa
r["M08"] = {
    "recommendation_objectives": list_values,
    "carryover": [100 * 0.5**t for t in range(4)],
    "average_A": ra(40) / 40,
    "average_B": rb(20) / 20,
    "marginal_A": 5 * math.exp(-40 / 20),
    "marginal_B": 2 * math.exp(-20 / 40),
    "current_total_contribution": ra(40) + rb(20),
    "optimal_spend_A": sa,
    "optimal_spend_B": sb,
    "optimal_total_contribution": ra(sa) + rb(sb),
    "contribution_gain": ra(sa) + rb(sb) - ra(40) - rb(20),
    "one_unit_transfer_gain": ra(39) + rb(21) - ra(40) - rb(20),
    "manual_total_minutes": 110,
    "assisted_total_minutes": 85,
    "time_reduction_fraction": 25 / 110,
}
assert math.isclose(5 * math.exp(-sa / 20), 2 * math.exp(-sb / 40))
# Independent grid check of the constrained optimum, to the grid's precision.
grid_best = max((ra(i / 100) + rb(60 - i / 100), i / 100) for i in range(6001))
assert abs(grid_best[1] - sa) < 0.01
write_csv(
    "M08_recommendation_synthetic.csv",
    ["item", "category", "relevance_score"],
    [(key, *value) for key, value in items.items()],
)
print(json.dumps(r, indent=2))
