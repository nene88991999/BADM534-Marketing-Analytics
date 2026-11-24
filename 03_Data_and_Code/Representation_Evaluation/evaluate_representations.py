"""Compare reconstruction and routing on four invented text representations."""
from pathlib import Path
import json
import math

ROOT = Path(__file__).resolve().parent


def score(points, reconstructed):
    if len(points) != len(reconstructed) or not points:
        raise ValueError("Supply matching nonempty inputs")
    n = len(points)
    means = [sum(p[j] for p in points) / n for j in (0, 1)]
    variation = [sum((p[j] - means[j]) ** 2 for p in points) for j in (0, 1)]
    if min(variation) <= 0:
        raise ValueError("Both component variances must be positive")
    errors = [sum((p[j] - q[j]) ** 2 for p, q in zip(points, reconstructed))
              for j in (0, 1)]
    expected = [p[1] > 0 for p in points]
    routed = [q[1] > 0 for q in reconstructed]
    positives = sum(expected)
    if positives == 0:
        raise ValueError("Recall needs at least one review-required case")
    total_fvu = sum(errors) / sum(variation)
    component_fvu = [e / v for e, v in zip(errors, variation)]
    weights = [v / sum(variation) for v in variation]
    weighted = sum(w * e for w, e in zip(weights, component_fvu))
    if not math.isclose(weighted, total_fvu, rel_tol=1e-12, abs_tol=1e-12):
        raise AssertionError("Component errors must reproduce total error")
    return {"records": n, "variation": variation, "squared_errors": errors,
            "variance_weights": weights, "component_fvu": component_fvu,
            "total_fvu": total_fvu, "variance_explained_pct": 100 * (1 - total_fvu),
            "review_required": positives, "routed": sum(routed),
            "true_positives": sum(a and b for a, b in zip(expected, routed)),
            "recall": sum(a and b for a, b in zip(expected, routed)) / positives,
            "accuracy": sum(a == b for a, b in zip(expected, routed)) / n}


def calculate(data):
    identifiers = [r["case_id"] for r in data["cases"]]
    if len(set(identifiers)) != len(identifiers):
        raise ValueError("Case identifiers must be unique")
    results = []
    for scale in data["style_scales"]:
        points = [(scale * r["style_sign"], r["review_signal"]) for r in data["cases"]]
        representations = {
            "A": [(p[0], 0) for p in points],
            "B": [(data["representation_B_style_multiplier"] * p[0], p[1]) for p in points],
        }
        for name, values in representations.items():
            results.append({"style_scale": scale, "representation": name,
                            "case_ids": identifiers, "inputs": points,
                            "reconstructed": values, **score(points, values)})
    return {"synthetic": True, "weights": "Equal weight per case",
            "routing_rule": "Review when reconstructed second coordinate is strictly positive",
            "results": results}


if __name__ == "__main__":
    data = json.loads((ROOT / "data/cases.json").read_text())
    result = calculate(data)
    output = ROOT / "results"
    output.mkdir(exist_ok=True)
    (output / "representations.json").write_text(json.dumps(result, indent=2) + "\n")
    for row in result["results"]:
        print(f"Scale {row['style_scale']}: {row['representation']}, "
              f"variance explained {row['variance_explained_pct']:.6f}%, recall {row['recall']:.0%}")
