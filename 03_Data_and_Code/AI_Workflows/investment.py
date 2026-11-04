"""Conditional reuse costs and buyer/seller price bounds; all inputs are imposed."""
import csv
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent / "results"


def reuse_hours(uses, setup, old_per_use, new_per_use, upkeep_per_use):
    if uses < 0 or min(setup, old_per_use, new_per_use, upkeep_per_use) < 0:
        raise ValueError("Uses and hours must be nonnegative")
    old = uses * old_per_use
    new = setup + uses * (new_per_use + upkeep_per_use)
    return old, new, old - new


def price_bounds(value, outside_utility, buyer_burden, unit_cost, fixed_cost, volume):
    if volume <= 0:
        raise ValueError("Conditional volume must be positive")
    # Quasilinear buyer utility: value - price - burden >= outside utility.
    ceiling = value - outside_utility - buyer_burden
    # Zero seller profit: volume * (price - unit_cost) >= fixed_cost.
    floor = unit_cost + fixed_cost / volume
    return floor, ceiling


def write_csv(name, rows):
    with (OUT / name).open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main():
    OUT.mkdir(exist_ok=True)
    reuse = []
    for n in range(25):
        old, new, saved = reuse_hours(n, 6, 2, 1.25, 0.25)
        reuse.append({"uses": n, "old_hours": old,
                      "reusable_hours": new, "net_hours_saved": saved})
    assert reuse[12]["net_hours_saved"] == 0
    assert next(r["uses"] for r in reuse if r["net_hours_saved"] > 0) == 13
    assert reuse[24]["net_hours_saved"] == 6
    pricing = []
    for scenario, unit_cost, outside in [
        ("Initial", 20, 80), ("Seller automation", 10, 80), ("Shared adoption", 10, 140)
    ]:
        floor, ceiling = price_bounds(200, outside, 40, unit_cost, 1000, 50)
        # Direct monetary balances verify both boundary calculations.
        assert 50 * (floor - unit_cost) - 1000 == 0
        assert 200 - ceiling - 40 == outside
        pricing.append({"scenario": scenario, "unit_cost_dollars": unit_cost,
                        "fixed_cost_dollars": 1000, "conditional_volume": 50,
                        "value_dollars": 200, "buyer_burden_dollars": 40,
                        "outside_utility_dollars": outside,
                        "price_floor_dollars": floor, "price_ceiling_dollars": ceiling,
                        "feasible": floor <= ceiling})
    assert [r["feasible"] for r in pricing] == [True, True, False]
    write_csv("reuse_costs.csv", reuse)
    write_csv("price_bounds.csv", pricing)
    summary = {"scope": "Hypothetical equal-quality costs and monetary valuations.",
               "reuse_break_even_uses": 12, "first_positive_saving_uses": 13,
               "pricing": "Conditional on 50 sales; no demand or equilibrium is estimated.",
               "price_bounds": pricing}
    (OUT / "investment_results.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
