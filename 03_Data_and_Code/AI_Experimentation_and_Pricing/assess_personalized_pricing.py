"""Exact synthetic incidence: one purchase opportunity, dollars, zero cost.

Python 3.10+, standard library; imports the adjacent pricing example.
Run: python3 03_Data_and_Code/AI_Experimentation_and_Pricing/assess_personalized_pricing.py
"""
import json
from fractions import Fraction as F
from pathlib import Path
from evaluate_pricing import GROUPS, best_uniform, demand, evaluate, surplus

ROOT = Path(__file__).resolve().parent


def calculate():
    base = best_uniform(list(GROUPS.values()))
    segmented = {g: best_uniform([cell]) for g, cell in GROUPS.items()}
    policies = {"uniform": {g: base for g in GROUPS},
                "segmented": segmented,
                "discount_only": {g: min(p, base) for g, p in segmented.items()}}
    totals, incidence = {}, []
    for policy, prices in policies.items():
        totals[policy] = {"prices": prices, **evaluate(prices, base)}
        for g, (weight, lo, hi) in GROUPS.items():
            q0, q1 = demand(base, lo, hi), demand(prices[g], lo, hi)
            delta = surplus(prices[g], lo, hi) - surplus(base, lo, hi)
            incidence.append({"policy": policy, "group": g,
                              "population_share": weight, "price": prices[g],
                              "surplus_change_per_group_member": delta,
                              "population_surplus_contribution": weight * delta,
                              "lost_purchase_share_within_group": max(F(0), q0-q1),
                              "population_lost_purchase_share": weight * max(F(0), q0-q1)})
    return {"data_type": "Synthetic uniform valuations; all eligible people included",
            "benchmark_price": base, "policies": totals, "incidence": incidence,
            "foregone_profit_from_cap_per_eligible":
                totals["segmented"]["profit_per_eligible_customer"] -
                totals["discount_only"]["profit_per_eligible_customer"],
            "moral_scope": "Amounts inform reasons; no numerical moral verdict"}


if __name__ == "__main__":
    out = ROOT / "scanlon_results"
    out.mkdir(exist_ok=True)
    (out / "incidence.json").write_text(json.dumps(calculate(), indent=2,
        default=lambda x: {"exact": str(x), "decimal": float(x)}) + "\n")
