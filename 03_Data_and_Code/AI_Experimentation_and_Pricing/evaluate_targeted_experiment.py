"""Synthetic expected cells for a stratified pricing experiment; no sampling.

Assignment probabilities are invented, not the published experiment's design.
Run: python3 03_Data_and_Code/AI_Experimentation_and_Pricing/evaluate_targeted_experiment.py
"""
import json
from fractions import Fraction as F
from pathlib import Path
from evaluate_pricing import GROUPS, best_uniform, demand, surplus

ROOT = Path(__file__).resolve().parent


def calculate(propensities):
    if set(propensities) != set(GROUPS) or any(
            not 0 < e < 1 for e in propensities.values()):
        raise ValueError("Each group requires a known assignment probability in (0,1).")
    base = best_uniform(list(GROUPS.values()))
    rows = []
    treated = control = treated_mass = control_mass = ipw = F(0)
    for g, (w, lo, hi) in GROUPS.items():
        e = propensities[g]
        p1 = best_uniform([GROUPS[g]])
        y0, y1 = base * demand(base, lo, hi), p1 * demand(p1, lo, hi)
        cs0, cs1 = surplus(base, lo, hi), surplus(p1, lo, hi)
        treated += w * e * y1
        control += w * (1-e) * y0
        treated_mass += w * e
        control_mass += w * (1-e)
        ipw += w * e * y1 / e - w * (1-e) * y0 / (1-e)
        rows.append({"group": g, "population_share": w, "assignment_probability": e,
                     "expected_revenue_control": y0, "expected_revenue_treatment": y1,
                     "expected_surplus_loss_per_group_member": e * max(F(0), cs0-cs1),
                     "population_expected_lost_purchase_share":
                         w * e * max(F(0), demand(base, lo, hi)-demand(p1, lo, hi))})
    return {"rows": rows, "naive_difference": treated/treated_mass-control/control_mass,
            "ipw_policy_effect": ipw, "experiment_revenue_per_eligible": treated+control,
            "expected_lost_purchase_share": sum(r["population_expected_lost_purchase_share"]
                                                for r in rows)}


if __name__ == "__main__":
    results = {"data_type": "Exact synthetic expected cells, no empirical standard errors",
               "targeted": calculate({"L": F(1, 4), "H": F(3, 4)}),
               "balanced": calculate({"L": F(1, 2), "H": F(1, 2)})}
    out = ROOT / "scanlon_results"
    out.mkdir(exist_ok=True)
    (out / "experiment.json").write_text(json.dumps(results, indent=2,
        default=lambda x: {"exact": str(x), "decimal": float(x)}) + "\n")
