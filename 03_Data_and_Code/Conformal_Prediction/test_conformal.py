"""Independent rank enumeration and constructed-case checks."""
import math
import unittest
from fractions import Fraction as F
from conformal import label_set, threshold
from demand_intervals import make_inputs, evaluate, assess
from complaint_sets import make_calibration


class ConformalChecks(unittest.TestCase):
    def test_exchangeable_rank_enumeration(self):
        # Conditional on 20 distinct scores, each position is equally likely
        # to be the test score. Enumerate every possible held-out position.
        augmented = list(range(1, 21))
        covered = sum(test <= threshold(augmented[:i] + augmented[i+1:])
                      for i, test in enumerate(augmented))
        self.assertEqual(covered, 18)

    def test_small_sample_boundary_and_ties(self):
        self.assertTrue(math.isinf(threshold(range(8))))
        self.assertEqual(threshold(range(1, 10)), 9)
        self.assertEqual(threshold([2] * 19), 2)
        self.assertIn("a", label_set({"a": "0.35", "b": "0.65"}, .65))

    def test_invalid_inputs(self):
        for scores, alpha in [([], .1), ([1], 0), ([1], 1), ([math.nan], .1)]:
            with self.assertRaises(ValueError):
                threshold(scores, alpha)
        for p in [{}, {"a": .2, "b": .2}, {"a": -1, "b": 2}]:
            with self.assertRaises(ValueError):
                label_set(p, .65)

    def test_demand_counts_and_group_comparison(self):
        cal, test = make_inputs()
        self.assertEqual((len(cal), len(test)), (99, 100))
        residuals = [abs(r["demand"] - r["prediction"]) for r in cal]
        # Histogram implies positions 1..80 <= 8, 81..90 = 10, 91..99 = 20.
        self.assertEqual(sum(x <= 8 for x in residuals), 80)
        self.assertEqual(sum(x == 10 for x in residuals), 10)
        self.assertEqual(sum(x == 20 for x in residuals), 9)
        self.assertEqual(threshold(residuals), 10)
        for g, expected in [("regular", 8), ("volatile", 20)]:
            values = [abs(r["demand"] - r["prediction"])
                      for r in cal if r["segment"] == g]
            self.assertEqual(threshold(values), expected)
        detail, pooled = evaluate(test, dict(regular=10, volatile=10), "p", "r")
        self.assertEqual([r["covered"] for r in pooled], [90, 80, 10])
        detail, grouped = evaluate(test, dict(regular=8, volatile=20), "g", "r")
        self.assertEqual([r["covered"] for r in grouped], [98, 80, 18])
        self.assertEqual(sum(F(str(r["width"])) for r in detail) / 100, F(104, 5))

    def test_changed_outcomes_keep_same_denominator(self):
        _, rows = make_inputs()
        detail, result = evaluate(rows, dict(regular=10, volatile=10), "p", "s", 25)
        self.assertEqual([r["covered"] for r in result], [5, 0, 5])
        self.assertEqual({r["store_id"] for r in detail}, {r["store_id"] for r in rows})
        with self.assertRaises(ValueError):
            assess(rows + rows[:1])

    def test_prediction_sets_and_infinite_cutoff(self):
        cal = make_calibration()
        scores = [1 - F(r["probabilities"][r["true_label"]]) for r in cal]
        self.assertEqual(threshold(scores), .65)
        p = [{"billing": ".70", "delivery": ".20", "product": ".10"},
             {"billing": ".45", "delivery": ".40", "product": ".15"},
             {"billing": ".34", "delivery": ".33", "product": ".33"}]
        self.assertEqual([label_set(row, .65) for row in p],
                         [["billing"], ["billing", "delivery"], []])
        self.assertEqual(label_set(p[2], math.inf), list(p[2]))


if __name__ == "__main__":
    unittest.main()
