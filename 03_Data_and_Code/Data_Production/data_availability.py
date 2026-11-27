"""Exact synthetic billing populations and institutionally selected evidence.

Run from any directory with Python 3.10+. No external data or dependencies.
Both potential outcomes are known only because this program constructs them.
"""
import csv
from fractions import Fraction
from pathlib import Path
from random import Random

HERE = Path(__file__).resolve().parent
OUT = HERE / "results"
GROUPS = "ABCD"
POLICIES = {"restricted": (100, 100, 0, 0),
            "broader": (100, 100, 50, 50),
            "balanced": (50, 50, 50, 50)}


def population(world):
    if world not in ("H", "L"):
        raise ValueError("Unknown synthetic world")
    rows = []
    for group in GROUPS:
        effect = 30 if world == "H" and group in "CD" else -10
        for i in range(100):
            previous = 120 + i % 5
            rows.append({"household_id": f"{group}{i:03d}", "group": group,
                         "previous_bill_usd": previous,
                         "current_bill_usd": previous + effect,
                         "no_project_bill_usd_oracle": previous,
                         "effect_usd_oracle": effect})
    return rows


def release(rows, policy):
    ids = [r["household_id"] for r in rows]
    if len(set(ids)) != len(ids):
        raise ValueError("Duplicate household")
    rng = Random(20261126)
    selected = []
    for group, count in zip(GROUPS, POLICIES[policy]):
        eligible = sorted((r for r in rows if r["group"] == group),
                          key=lambda r: r["household_id"])
        if len(eligible) != 100:
            raise ValueError("Expected 100 households in each stratum")
        inclusion = Fraction(count, len(eligible))
        for row in rng.sample(eligible, count):
            selected.append({k: row[k] for k in
                             ("household_id", "group", "previous_bill_usd",
                              "current_bill_usd")} | {"inclusion": inclusion})
    return sorted(selected, key=lambda r: r["household_id"])


def mean_change(rows):
    if not rows:
        raise ValueError("Empty observed sample")
    return Fraction(sum(r["current_bill_usd"] - r["previous_bill_usd"]
                        for r in rows), len(rows))


def weighted_mean(rows, policy):
    # The target is all 400 households, with equal population weights.
    if any(n == 0 for n in POLICIES[policy]):
        raise ValueError("Zero inclusion leaves target strata unsupported")
    return sum((Fraction(r["current_bill_usd"] - r["previous_bill_usd"])
                / r["inclusion"] for r in rows), Fraction(0)) / 400


def effect_bounds(observed_mean, coverage, lower, upper):
    if not (0 <= coverage <= 1 and lower <= upper):
        raise ValueError("Invalid coverage or support")
    return (coverage * observed_mean + (1 - coverage) * lower,
            coverage * observed_mean + (1 - coverage) * upper)


def construct():
    files = {}
    summaries = []
    for world in ("H", "L"):
        rows = population(world)
        files[f"synthetic_ledger_{world}.csv"] = rows
        target = Fraction(sum(r["effect_usd_oracle"] for r in rows), 400)
        for policy in POLICIES:
            observed = release(rows, policy)
            files[f"released_{world}_{policy}.csv"] = observed
            weighted = ("undefined" if policy == "restricted"
                        else weighted_mean(observed, policy))
            summaries.append({"world": world, "policy": policy,
                              "target_households": 400,
                              "released_households": len(observed),
                              "coverage": Fraction(len(observed), 400),
                              "released_mean_change_usd": mean_change(observed),
                              "target_mean_effect_usd_oracle": target,
                              "weighted_mean_change_usd": weighted})
    lower, upper = effect_bounds(Fraction(-10), Fraction(1, 2), -20, 40)
    files["bounds.csv"] = [{"observed_mean_usd": -10, "coverage": "1/2",
                            "missing_lower_usd_assumed": -20,
                            "missing_upper_usd_assumed": 40,
                            "population_lower_usd": lower,
                            "population_upper_usd": upper}]
    files["selection_comparisons.csv"] = summaries
    return files


def main():
    OUT.mkdir(exist_ok=True)
    for name, rows in construct().items():
        with (OUT / name).open("w", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
        print(name, len(rows), "synthetic rows")


if __name__ == "__main__":
    main()
