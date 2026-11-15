"""Exact arithmetic for centroid weighting and stale assignments."""
from fractions import Fraction as F
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


def examples():
    # Earlier assignments: ten observations with mean 2.
    # Current batch: two observations with mean 7. Alpha is one-half.
    alpha = F(1, 2)
    total = (1 - alpha) * 20 + alpha * 14
    mass = (1 - alpha) * 10 + alpha * 2
    center = total / mass
    naive = (1 - alpha) * 2 + alpha * 7
    points = [F(0), F(4), F(5), F(10)]
    centers = [F(2), F(15, 2)]
    saved = [0, 0, 0, 1]
    final = [min(range(2), key=lambda j: (x - centers[j])**2)
             for x in points]
    saved_loss = sum((x - centers[j])**2
                     for x, j in zip(points, saved)) / len(points)
    final_loss = sum((x - centers[j])**2
                     for x, j in zip(points, final)) / len(points)
    return {
        "scope": "Constructed scalar examples; no observed customer outcomes",
        "ema_sum": str(total), "ema_mass": str(mass),
        "ema_centroid": str(center), "mean_of_centroids": str(naive),
        "points": [str(x) for x in points],
        "centers": [str(x) for x in centers],
        "saved_labels": saved, "final_labels": final,
        "boundary": str(sum(centers) / 2),
        "changed": sum(a != b for a, b in zip(saved, final)),
        "denominator": len(points),
        "saved_assignment_mse": str(saved_loss),
        "final_assignment_mse": str(final_loss),
    }


if __name__ == "__main__":
    result = examples()
    (HERE / "results").mkdir(exist_ok=True)
    (HERE / "results/centroid_checks.json").write_text(
        json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
