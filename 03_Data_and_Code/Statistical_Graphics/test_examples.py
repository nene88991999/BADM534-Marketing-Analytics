"""Small independent checks for pairing, ranking, and probability arithmetic."""
import csv
import math
import unittest
from pathlib import Path
from fractions import Fraction
from paired_changes import evaluate as paired
from ranking_calibration import evaluate as calibrated

HERE = Path(__file__).resolve().parent


def load(name):
    with (HERE / "inputs" / name).open(newline="") as stream:
        return list(csv.DictReader(stream))


class Examples(unittest.TestCase):
    def test_paired_exact_difference_variance(self):
        result = paired(load("paired_spending.csv"))
        self.assertEqual(result["mean_change"], 5)
        self.assertAlmostEqual(result["paired_standard_error"], math.sqrt(1 / 14))

    def test_pairing_and_row_order(self):
        rows = load("paired_spending.csv")
        first = paired(rows)
        self.assertEqual(first, paired(rows[::-1]))
        mismatched = [dict(a, after_dollars=b["after_dollars"])
                      for a, b in zip(rows, rows[::-1])]
        second = paired(mismatched)
        self.assertEqual(first["mean_change"], second["mean_change"])
        self.assertGreater(second["paired_standard_error"], 10)

    def test_incomplete_and_duplicate_pairs(self):
        rows = load("paired_spending.csv")
        for invalid in [rows + rows[:1], [dict(rows[0], after_dollars="nan")] + rows[1:],
                        [dict(rows[0], before_dollars="")] + rows[1:]]:
            with self.assertRaises(ValueError):
                paired(invalid)

    def test_auc_from_group_counts(self):
        rows = load("purchase_predictions.csv")
        # Positive counts 2,6,12,16; negative counts 18,14,8,4.
        # Wins plus half ties: 18 + 150 + 432 + 672 = 1272.
        for model in ("model_a", "model_b"):
            metrics, _ = calibrated(rows, model)
            self.assertEqual(Fraction(metrics["auc_exact"]), Fraction(1272, 36 * 44))

    def test_probability_losses_and_totals(self):
        rows = load("purchase_predictions.csv")
        a, bins = calibrated(rows, "model_a")
        b, _ = calibrated(rows, "model_b")
        self.assertAlmostEqual(a["brier"], .175)
        self.assertAlmostEqual(b["brier"], .21855)
        self.assertEqual((a["predicted_purchases"], b["predicted_purchases"]), (36, 40))
        self.assertEqual(sum(r["customers"] for r in bins), 80)
        self.assertEqual(sum(r["purchases"] for r in bins), 36)

    def test_invalid_predictions_and_outcomes(self):
        rows = load("purchase_predictions.csv")
        for invalid in [rows + rows[:1], [dict(rows[0], model_a="1.2")] + rows[1:],
                        [dict(rows[0], purchase="2")] + rows[1:]]:
            with self.assertRaises(ValueError):
                calibrated(invalid, "model_a")


if __name__ == "__main__":
    unittest.main()
