"""Published rounded percentages and an original synthetic factorial example.

Run from any directory. Standard library only; no student records or model calls.
"""
import csv
import json
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent


def percentage_comparison(treatment, comparison):
    """Inputs are percentages on a 0-100 scale; return points and relative %.

    Zero comparison values leave the relative percentage undefined.
    """
    a, b = Fraction(str(treatment)), Fraction(str(comparison))
    if not (0 <= a <= 100 and 0 <= b <= 100):
        raise ValueError("Scores must be percentages in [0, 100]")
    return a - b, (100 * (a - b) / b if b else None)


def factorial_effects(means):
    """Q: questions with feedback; F: alternative representations.

    Each key is (Q, F). Means are hypothetical percentage scores for the same
    population and common assessment. Equal allocation defines main effects.
    """
    if set(means) != {(0, 0), (1, 0), (0, 1), (1, 1)}:
        raise ValueError("All four factorial cells are required")
    m = {k: Fraction(str(v)) for k, v in means.items()}
    if any(not 0 <= x <= 100 for x in m.values()):
        raise ValueError("Scores must be percentages in [0, 100]")
    return {
        "questions_without_formats_pp": m[1, 0] - m[0, 0],
        "questions_with_formats_pp": m[1, 1] - m[0, 1],
        "formats_without_questions_pp": m[0, 1] - m[0, 0],
        "formats_with_questions_pp": m[1, 1] - m[1, 0],
        "questions_equal_weight_effect_pp":
            (m[1, 0] - m[0, 0] + m[1, 1] - m[0, 1]) / 2,
        "formats_equal_weight_effect_pp":
            (m[0, 1] - m[0, 0] + m[1, 1] - m[1, 0]) / 2,
        "interaction_pp": m[1, 1] - m[1, 0] - m[0, 1] + m[0, 0],
        "whole_package_pp": m[1, 1] - m[0, 0],
    }


def main():
    out = HERE / "results"
    out.mkdir(exist_ok=True)
    points, relative = percentage_comparison(78, 67)
    # Rounded figures reported in Google's September 16, 2025 announcement.
    with (out / "reported_percentage_comparison.csv").open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["treatment_percent", "comparison_percent",
                         "difference_percentage_points", "relative_change_percent"])
        writer.writerow([78, 67, float(points), float(relative)])
    means = {(0, 0): 60, (1, 0): 66, (0, 1): 68, (1, 1): 77}
    with (out / "synthetic_factorial_cells.csv").open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["questions", "formats", "mean_score_percent"])
        writer.writerows((q, v, means[q, v]) for q, v in sorted(means))
    effects = {k: float(v) for k, v in factorial_effects(means).items()}
    (out / "synthetic_factorial_effects.json").write_text(
        json.dumps(effects, indent=2) + "\n")
    print(f"Reported rounded scores: {float(points):g} points; {float(relative):.4f}% relative")
    print("Synthetic factorial:", effects)


if __name__ == "__main__":
    main()
