"""Synthetic numerical examples for M7; run from any working directory."""

import itertools
import json
import math
from example_helpers import write_csv, ols_slope, shares

r = {}
r["M07"] = {
    "precision": 30 / 100,
    "recall": 30 / 50,
    "accuracy": (30 + 880) / 1000,
    "all_negative_accuracy": 950 / 1000,
    "cost_threshold": 1 / (1 + 9),
    "coupon_A": 40 * (0.8 - 0.78) - 5 * 0.8 - 2,
    "coupon_B": 40 * (0.3 - 0.15) - 5 * 0.3 - 2,
}
write_csv(
    "M07_coupon_synthetic.csv",
    [
        "customer",
        "purchase_with_coupon",
        "purchase_without_coupon",
        "margin_dollars",
        "discount_dollars",
        "contact_cost_dollars",
    ],
    [("A", 0.8, 0.78, 40, 5, 2), ("B", 0.3, 0.15, 40, 5, 2)],
)

rankings = {
    "ABC": [("A", 0), ("B", 1), ("C", 1)],
    "BCA": [("B", 1), ("C", 1), ("A", 0)],
}


def dcg(labels):
    return sum(
        (2**label - 1) / math.log2(rank + 1)
        for rank, label in enumerate(labels, start=1)
    )


ideal = dcg([1, 1, 0])
r["M07"]["rankings"] = {
    name: {
        "precision_at_3": sum(v for _, v in vals) / 3,
        "recall_at_3": sum(v for _, v in vals) / 2,
        "dcg_at_3": dcg([v for _, v in vals]),
        "ndcg_at_3": dcg([v for _, v in vals]) / ideal,
    }
    for name, vals in rankings.items()
}
write_csv(
    "M07_rankings_synthetic.csv",
    ["ranking", "position", "item", "binary_relevance"],
    [
        (name, pos, item, rel)
        for name, vals in rankings.items()
        for pos, (item, rel) in enumerate(vals, start=1)
    ],
)
assert math.isclose(r["M07"]["rankings"]["BCA"]["ndcg_at_3"], 1)
assert 0.693 < r["M07"]["rankings"]["ABC"]["ndcg_at_3"] < 0.694

goal_items = {"A": (0.9, 0.1), "B": (0.75, 0.6), "C": (0.6, 0.9)}
goal_score = (
    lambda item, alpha: (1 - alpha) * goal_items[item][0] + alpha * goal_items[item][1]
)
r["M07"]["goal_blend"] = {
    "scores": {
        str(alpha): {item: goal_score(item, alpha) for item in goal_items}
        for alpha in [0, 0.25, 0.5, 1]
    },
    "optimal_switches": [3 / 13, 1 / 3],
}
write_csv(
    "M07_goals_synthetic.csv",
    ["item", "preference_score", "goal_score"],
    [(item, *scores) for item, scores in goal_items.items()],
)
assert math.isclose(goal_score("A", 3 / 13), goal_score("B", 3 / 13))
assert math.isclose(goal_score("B", 1 / 3), goal_score("C", 1 / 3))
for i in range(1001):
    alpha = i / 1000
    expected = "A" if alpha < 3 / 13 else ("B" if alpha < 1 / 3 else "C")
    assert max(goal_items, key=lambda j: goal_score(j, alpha)) == expected
print(json.dumps(r, indent=2))
