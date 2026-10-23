"""Synthetic numerical examples for M2; run from any working directory."""

import itertools
import json
import math
from example_helpers import write_csv, ols_slope, shares

r = {}
campaigns = [
    ("A", "new", 100, 9),
    ("A", "returning", 100, 80),
    ("B", "new", 200, 20),
    ("B", "returning", 100, 81),
]
write_csv(
    "M02_campaigns_synthetic.csv",
    ["campaign", "customer_type", "assigned_customers", "conversions"],
    campaigns,
)
r["M02"] = {
    "observed_A": 89 / 200,
    "observed_B": 101 / 300,
    "common_mix_A": (0.09 + 0.80) / 2,
    "common_mix_B": (0.10 + 0.81) / 2,
    "basket_jaccard_high": 3 / 5,
    "basket_jaccard_low": 1 / 7,
}
assert r["M02"]["observed_A"] > r["M02"]["observed_B"]
assert r["M02"]["common_mix_B"] > r["M02"]["common_mix_A"]
variety_shares = {"equal": [0.5, 0.5], "concentrated": [0.9, 0.1]}
r["M02"]["variety"] = {
    name: 1 - sum(s * s for s in vals) for name, vals in variety_shares.items()
}
write_csv(
    "M02_variety_synthetic.csv",
    ["basket", "category", "spending_share"],
    [
        (name, f"C{i+1}", share)
        for name, vals in variety_shares.items()
        for i, share in enumerate(vals)
    ],
)
assert math.isclose(r["M02"]["variety"]["equal"], 0.5)
assert math.isclose(r["M02"]["variety"]["concentrated"], 0.18)
print(json.dumps(r, indent=2))
