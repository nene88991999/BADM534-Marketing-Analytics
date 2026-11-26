"""Two synthetic demand completions match every tested purchase probability.

Unit demand, quasilinear money utility, stable demand, prices in dollars.
Run: python3 03_Data_and_Code/AI_Experimentation_and_Pricing/compare_demand_completions.py
"""
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parent
WEIGHTS = {"L": F(3, 5), "H": F(2, 5)}
OBSERVED = {"L": {5: F(9, 10), 10: F(1, 2), 20: F(1, 10)},
            "H": {5: F(19, 20), 10: F(4, 5), 20: F(1, 2)}}


def curves(world):
    if world not in ("negative_change", "positive_change"):
        raise ValueError("Unknown synthetic completion.")
    low_knot = (F(51, 10), F(1, 2)) if world == "negative_change" else (F(99, 10), F(9, 10))
    high_knot = (F(199, 10), F(4, 5)) if world == "negative_change" else (F(101, 10), F(1, 2))
    return {"L": [(F(0), F(1)), (F(5), F(9, 10)), low_knot,
                  (F(10), F(1, 2)), (F(20), F(1, 10)), (F(30), F(0))],
            "H": [(F(0), F(1)), (F(5), F(19, 20)), (F(10), F(4, 5)),
                  high_knot, (F(20), F(1, 2)), (F(30), F(0))]}


def integral(points, left, right):
    """Exact trapezoid integral on a piecewise-linear demand curve."""
    total = F(0)
    for (x0, y0), (x1, y1) in zip(points, points[1:]):
        a, b = max(left, x0), min(right, x1)
        if a < b:
            ya = y0 + (y1-y0) * (a-x0)/(x1-x0)
            yb = y0 + (y1-y0) * (b-x0)/(x1-x0)
            total += (b-a) * (ya+yb)/2
    return total


def calculate():
    results = {}
    for world in ("negative_change", "positive_change"):
        points = curves(world)
        gain = integral(points["L"], F(5), F(10))
        loss = integral(points["H"], F(10), F(20))
        results[world] = {"demand_points": points, "L_surplus_gain": gain,
                          "H_surplus_loss": loss,
                          "population_surplus_change": WEIGHTS["L"]*gain-WEIGHTS["H"]*loss}
    return {"data_type": "Synthetic population probabilities; no sample estimates",
            "observed_probabilities": OBSERVED, "worlds": results,
            "uniform_revenue": F(31, 5), "targeted_revenue": F(67, 10),
            "monotonic_surplus_change_bounds": [F(-17, 10), F(7, 10)]}


if __name__ == "__main__":
    out = ROOT / "scanlon_results"
    out.mkdir(exist_ok=True)
    (out / "demand_completions.json").write_text(json.dumps(calculate(), indent=2,
        default=lambda x: {"exact": str(x), "decimal": float(x)}) + "\n")
