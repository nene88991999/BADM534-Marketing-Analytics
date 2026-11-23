"""Original arithmetic for Jasin, Lin, and Zhang (2026), Sections 5.3 and 6.

Uses only the standard library. No author code, microdata, or model inference.
All four-profile means and sensitivity inputs are invented course examples.
Run from any working directory; results are written next to this script.
"""

from fractions import Fraction
from math import ceil, isclose, sqrt
from pathlib import Path
import json


def rank(rows):
    """Exact Gaussian elimination for the small integer design matrices."""
    matrix = [[Fraction(x) for x in row] for row in rows]
    pivot_row = 0
    for column in range(len(matrix[0])):
        pivot = next((i for i in range(pivot_row, len(matrix))
                      if matrix[i][column]), None)
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        divisor = matrix[pivot_row][column]
        matrix[pivot_row] = [x / divisor for x in matrix[pivot_row]]
        for i in range(len(matrix)):
            if i != pivot_row:
                factor = matrix[i][column]
                matrix[i] = [x - factor * y
                             for x, y in zip(matrix[i], matrix[pivot_row])]
        pivot_row += 1
        if pivot_row == len(matrix):
            break
    return pivot_row


def allocation(information_cost_ratio):
    """Theorem 3 with unit variances and unit primary sampling cost."""
    lam = information_cost_ratio
    if lam <= 0:
        raise ValueError("Use a positive cost ratio; zero is a limiting case.")
    if lam >= 1 / 3:
        primary, auxiliary = 3.0, 0.0
    else:
        primary = 2 + sqrt(2 * lam / (1 - lam))
        auxiliary = sqrt(2 * (1 - lam) / lam) - 1 - sqrt(2 * lam / (1 - lam))
    cost = primary + lam * auxiliary
    return {
        "information_cost_ratio": lam,
        "primary_precision": primary,
        "auxiliary_precision": auxiliary,
        "normalized_mse": 2 / primary + 1 / (primary + auxiliary),
        "cost_constant": cost,
        "asymptotic_saving_fraction": 1 - cost / 3,
    }


def numerical_cost(lam):
    """Search the feasible boundary without using Theorem 3's optimum."""
    best = 3.0
    for i in range(1, 20001):
        primary = 2 + i / 20000
        auxiliary = max(0.0, 1 / (1 - 2 / primary) - primary)
        best = min(best, primary + lam * auxiliary)
    return best


def calculate():
    cases = []
    for name, primary, mixed, var_p, var_a in [
        ("tea", 210.6, 54.8, 8.873, 0.187),
        ("digital_twins", 20.63, 13.97, 0.881, 0.096),
    ]:
        cases.append({
            "case": name, "published_primary_cost_constant": primary,
            "published_mixed_cost_constant": mixed,
            "saving_from_rounded_constants": 1 - mixed / primary,
            "assumed_auxiliary_to_primary_cost": 0.01,
            "information_cost_ratio": 0.01 * var_a / var_p,
        })

    profiles = [(f, p) for p in (-1, 1) for f in (-1, 1)]
    means = []
    for f, p in profiles:
        primary = 3 + 0.4 * f - 0.5 * p
        means.append({"feature": f, "price": p, "primary_mean": primary,
                      "auxiliary_mean": primary + 0.8 + 0.6 * p})
    for low, high in [(0, 1), (2, 3)]:
        for source in ("primary_mean", "auxiliary_mean"):
            assert isclose(means[high][source] - means[low][source], 0.8)
    for low, high in [(0, 2), (1, 3)]:
        assert isclose(means[high]["primary_mean"] - means[low]["primary_mean"], -1)
        assert isclose(means[high]["auxiliary_mean"] - means[low]["auxiliary_mean"], 0.2)

    response = [[1, f, p] for f, p in profiles]
    geometry = []
    for name, bias in [
        ("interaction_only", [[f * p] for f, p in profiles]),
        ("intercept_and_price", [[1, p] for f, p in profiles]),
        ("intercept_feature_and_price", response),
    ]:
        joint = [x + z for x, z in zip(response, bias)]
        overlap = rank(response) + rank(bias) - rank(joint)
        geometry.append({"bias_dictionary": name, "response_rank": rank(response),
                         "bias_rank": rank(bias), "intersection_dimension": overlap})
    assert [x["intersection_dimension"] for x in geometry] == [0, 2, 3]

    curve = []
    for lam in (0.0001, 0.001, 0.01, 0.1, 1 / 3, 0.5):
        result = allocation(lam)
        benchmark = numerical_cost(lam)
        assert isclose(result["normalized_mse"], 1.0, abs_tol=1e-12)
        assert -1e-10 <= benchmark - result["cost_constant"] < 1e-6
        result["independent_grid_cost"] = benchmark
        curve.append(result)

    optimum = allocation(0.01)
    epsilon_squared = 0.01
    primary_n = 4 * ceil(optimum["primary_precision"] / (4 * epsilon_squared))
    auxiliary_n = 4 * ceil(optimum["auxiliary_precision"] / (4 * epsilon_squared))
    primary_only_n = 4 * ceil(3 / (4 * epsilon_squared))
    cost = primary_n + 0.01 * auxiliary_n
    mse = 2 / primary_n + 1 / (primary_n + auxiliary_n)
    assert (primary_n, auxiliary_n, primary_only_n) == (216, 1296, 300)
    assert mse <= epsilon_squared
    omitted_feature_bias = 0.3
    coefficient_bias = omitted_feature_bias * auxiliary_n / (primary_n + auxiliary_n)

    return {
        "scope": "Published-ratio arithmetic and original analytic examples; no empirical replication.",
        "source_sections": ["Theorem 3, pp. 20-22", "Section 6, pp. 22-26"],
        "reported_case_arithmetic": cases,
        "invented_profile_means": means,
        "exact_geometry_checks": geometry,
        "allocation_curve": curve,
        "rounded_example": {
            "mse_target": epsilon_squared, "primary_n": primary_n,
            "auxiliary_n": auxiliary_n, "primary_only_n": primary_only_n,
            "cost": cost, "saving_fraction": 1 - cost / primary_only_n,
            "correct_model_mse": mse,
            "omitted_auxiliary_feature_bias": omitted_feature_bias,
            "expected_feature_coefficient_error": coefficient_bias,
            "squared_bias": coefficient_bias ** 2,
            "misspecified_model_mse": mse + coefficient_bias ** 2,
        },
        "model_calls": 0,
        "microdata_used": False,
        "author_code_executed": False,
    }


if __name__ == "__main__":
    output = Path(__file__).resolve().with_name("source_checks.json")
    output.write_text(json.dumps(calculate(), indent=2) + "\n")
    print(f"Verified source arithmetic and analytic examples: {output.name}")
