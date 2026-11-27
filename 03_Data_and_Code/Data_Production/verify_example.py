"""Check identification, selection, and arithmetic against hand totals."""
from fractions import Fraction
from data_availability import construct, population, release, weighted_mean

files = construct()
assert files["released_H_restricted.csv"] == files["released_L_restricted.csv"]
summaries = {(r["world"], r["policy"]): r
             for r in files["selection_comparisons.csv"]}
assert sum(r["effect_usd_oracle"] for r in population("H")) == 4000
assert sum(r["effect_usd_oracle"] for r in population("L")) == -4000
assert summaries["H", "restricted"]["target_mean_effect_usd_oracle"] == 10
assert summaries["L", "restricted"]["target_mean_effect_usd_oracle"] == -10
assert summaries["H", "broader"]["released_mean_change_usd"] == Fraction(10, 3)
assert summaries["H", "balanced"]["released_mean_change_usd"] == 10
for world in "HL":
    for policy in ("broader", "balanced"):
        row = summaries[world, policy]
        assert row["weighted_mean_change_usd"] == row["target_mean_effect_usd_oracle"]
for policy in ("restricted", "broader", "balanced"):
    assert release(population("H"), policy) == release(population("H")[::-1], policy)
try:
    weighted_mean(files["released_H_restricted.csv"], "restricted")
except ValueError:
    pass
else:
    raise AssertionError("Zero inclusion must fail explicitly")
try:
    release(population("H") + [population("H")[0]], "restricted")
except ValueError:
    pass
else:
    raise AssertionError("Duplicate household must fail explicitly")
bounds = files["bounds.csv"][0]
assert (bounds["population_lower_usd"], bounds["population_upper_usd"]) == (-15, 15)
# Replacing all unreleased effects by zero falsely returns -5 in world H.
assert Fraction(-2000, 400) == -5 != summaries["H", "restricted"]["target_mean_effect_usd_oracle"]
print("Verified exact totals, equivalent public records, selection, weights, bounds, and input checks.")
