"""Best responses from published rounded Table 9, not microdata replication.

Python 3.10+, standard library. Units are RMB revenue per messaged consumer.
Run: python3 03_Data_and_Code/AI_Experimentation_and_Pricing/reconstruct_competitive_targeting.py
"""
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def calculate():
    source = json.loads((ROOT / "competitive_payoffs.json").read_text())
    names = source["strategies"]
    a = [[F(cell[0]) for cell in row] for row in source["payoffs"]]
    b = [[F(cell[1]) for cell in row] for row in source["payoffs"]]
    n = len(names)
    best_a = {names[j]: [names[i] for i in range(n)
                         if a[i][j] == max(a[k][j] for k in range(n))] for j in range(n)}
    best_b = {names[i]: [names[j] for j in range(n)
                         if b[i][j] == max(b[i])] for i in range(n)}
    equilibria = [(names[i], names[j]) for i in range(n) for j in range(n)
                 if names[i] in best_a[names[j]] and names[j] in best_b[names[i]]]
    return {"source": source["source"], "units": source["units"],
            "best_responses_A": best_a, "best_responses_B": best_b,
            "pure_equilibria_from_rounded_payoffs": equilibria,
            "behavioral_vs_uniform_revenue_gains":
                {"A": a[2][2]-a[0][0], "B": b[2][2]-b[0][0]},
            "relative_gains": {"A": a[2][2]/a[0][0]-1, "B": b[2][2]/b[0][0]-1},
            "A_behavioral_vs_geobehavioral_gap_when_B_behavioral": a[2][2]-a[3][2],
            "scope": "Static estimated game; no posterior draws, privacy values, or permission measure"}


if __name__ == "__main__":
    out = ROOT / "scanlon_results"
    out.mkdir(exist_ok=True)
    (out / "competitive_targeting.json").write_text(json.dumps(calculate(), indent=2,
        default=lambda x: {"exact": str(x), "decimal": float(x)}) + "\n")
