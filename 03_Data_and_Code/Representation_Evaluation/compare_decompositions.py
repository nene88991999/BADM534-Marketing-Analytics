"""Exact nonunique vector decompositions; no autoencoder training."""
from pathlib import Path
import json
import math

ROOT = Path(__file__).resolve().parent


def calculate():
    target = (2.0, 0.0)
    rows = []
    for slope in (1.0, 2.0):
        coefficient = math.sqrt(1 + slope ** 2)
        directions = [(1 / coefficient, slope / coefficient),
                      (1 / coefficient, -slope / coefficient)]
        contributions = [tuple(coefficient * x for x in direction)
                         for direction in directions]
        reconstructed = tuple(sum(c[j] for c in contributions) for j in (0, 1))
        for direction in directions:
            if not math.isclose(sum(x * x for x in direction), 1.0):
                raise AssertionError("Directions must have unit norm")
        if not all(math.isclose(x, y, abs_tol=1e-12)
                   for x, y in zip(reconstructed, target)):
            raise AssertionError("Both decompositions must match the target")
        removal_error = sum((x - y) ** 2 for x, y in zip(target, contributions[1]))
        rows.append({"slope": slope, "coefficient_per_direction": coefficient,
                     "unit_directions": directions, "contributions": contributions,
                     "reconstructed": reconstructed,
                     "squared_error_after_removing_first": removal_error})
    return {"synthetic": True, "target": target, "results": rows}


if __name__ == "__main__":
    result = calculate()
    output = ROOT / "results"
    output.mkdir(exist_ok=True)
    (output / "decompositions.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
