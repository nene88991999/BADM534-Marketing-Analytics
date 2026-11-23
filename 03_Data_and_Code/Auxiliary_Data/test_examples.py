"""Independent checks of contrasts, joint regression, allocation, and scope."""
import copy
import unittest
from math import isclose
from allocate_responses import calculate, load_parameters, optimal_precision
from bias_sensitivity import evaluate


def solve(matrix, rhs):
    rows = [list(a) + [b] for a, b in zip(matrix, rhs)]
    for column in range(len(rows)):
        pivot = max(range(column, len(rows)), key=lambda i: abs(rows[i][column]))
        rows[column], rows[pivot] = rows[pivot], rows[column]
        divisor = rows[column][column]
        if abs(divisor) < 1e-12:
            raise ValueError("Singular matrix")
        rows[column] = [x / divisor for x in rows[column]]
        for i in range(len(rows)):
            if i != column:
                multiple = rows[i][column]
                rows[i] = [x - multiple * y for x, y in zip(rows[i], rows[column])]
    return [row[-1] for row in rows]


def joint_regression(primary_n, auxiliary_n, delta=0.0, full_bias=False):
    """Construct normal equations independently of the precision formulas."""
    size = 6 if full_bias else 5
    info = [[0.0] * size for _ in range(size)]
    rhs = [0.0] * size
    for source, count in [("primary", primary_n), ("auxiliary", auxiliary_n)]:
        for f, p in [(-1, -1), (1, -1), (-1, 1), (1, 1)]:
            x = [1, f, p]
            z = ([1, f, p] if full_bias else [1, p]) if source == "auxiliary" else [0] * (size - 3)
            design = x + z
            mean = 3 + 0.4 * f - 0.5 * p
            if source == "auxiliary":
                mean += 0.8 + 0.6 * p + delta * f
            for i in range(size):
                rhs[i] += count / 4 * design[i] * mean
                for j in range(size):
                    info[i][j] += count / 4 * design[i] * design[j]
    fitted = solve(info, rhs)
    variances = [solve(info, [int(i == j) for i in range(size)])[j] for j in range(3)]
    return fitted[:3], sum(variances)


class Examples(unittest.TestCase):
    def setUp(self):
        self.parameters = load_parameters()

    def test_profile_contrasts(self):
        rows, _, _ = calculate(self.parameters)
        means = {(r["feature"], r["price"]): r for r in rows}
        for price in (-1, 1):
            for name in ("primary_mean", "auxiliary_mean"):
                self.assertAlmostEqual(means[1, price][name] - means[-1, price][name], 0.8)
        for feature in (-1, 1):
            self.assertAlmostEqual(means[feature, 1]["primary_mean"] - means[feature, -1]["primary_mean"], -1)
            self.assertAlmostEqual(means[feature, 1]["auxiliary_mean"] - means[feature, -1]["auxiliary_mean"], 0.2)

    def test_continuous_allocation_against_feasible_search(self):
        for ratio in (0.001, 0.01, 0.1, 1 / 3, 0.8):
            t, s = optimal_precision(ratio)
            candidates = []
            for i in range(1, 20001):
                p = 2 + i / 20000
                a = max(0.0, 1 / (1 - 2 / p) - p)
                candidates.append(p + ratio * a)
            self.assertTrue(isclose(2 / t + 1 / (t + s), 1.0))
            self.assertAlmostEqual(t + ratio * s, min(candidates), places=6)
        self.assertEqual(optimal_precision(1 / 3), (3.0, 0.0))

    def test_rounded_counts_and_joint_regression_variance(self):
        _, result, _ = calculate(self.parameters)
        self.assertEqual((result["primary_per_profile"], result["auxiliary_per_profile"]), (54, 324))
        fitted, variance = joint_regression(216, 1296)
        for actual, expected in zip(fitted, [3, 0.4, -0.5]):
            self.assertAlmostEqual(actual, expected)
        self.assertAlmostEqual(result["correct_model_mse"], variance)
        self.assertLessEqual(variance, 0.01)
        self.assertAlmostEqual(result["mixed_cost"], 228.96)

    def test_omitted_bias_from_normal_equations(self):
        row = evaluate(self.parameters)[0]
        fitted, variance = joint_regression(216, 1296, delta=0.3)
        squared_error = sum((x - y) ** 2 for x, y in zip(fitted, [3, 0.4, -0.5]))
        self.assertAlmostEqual(row["omitted_bias_mse"], variance + squared_error)
        self.assertAlmostEqual(fitted[1], 23 / 35)
        self.assertGreater(row["omitted_bias_mse"], self.parameters["mse_target"])

    def test_more_responses_and_expanded_bias_dictionary(self):
        rows = evaluate(self.parameters)
        self.assertAlmostEqual(rows[0]["squared_bias"], rows[-1]["squared_bias"])
        self.assertAlmostEqual(rows[0]["total_coefficient_variance"] / 32, rows[-1]["total_coefficient_variance"])
        fitted, variance = joint_regression(216, 1296, delta=0.3, full_bias=True)
        self.assertAlmostEqual(variance, 3 / 216)
        for actual, expected in zip(fitted, [3, 0.4, -0.5]):
            self.assertAlmostEqual(actual, expected)

    def test_variance_units_and_no_auxiliary_boundary(self):
        revised = copy.deepcopy(self.parameters)
        revised["auxiliary_variance"] = 100
        _, result, _ = calculate(revised)
        self.assertEqual(result["information_cost_ratio"], 1)
        self.assertEqual(result["auxiliary_n"], 0)
        self.assertEqual(result["rounded_saving_fraction"], 0)
        with self.assertRaises(ValueError):
            optimal_precision(0)


if __name__ == "__main__":
    unittest.main()
