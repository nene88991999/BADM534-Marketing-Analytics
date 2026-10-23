"""Independent small-data checks for the added teaching methods."""

from pathlib import Path
import sys
import unittest
import numpy as np
import pandas as pd
from association_rules import metrics
from claim_checks import check_claim
from cuped import adjust
from logging_gaps import first_gap, kaplan_meier
from recency import snapshot
from reporting import monthly_review

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "Lecture_Examples"))
from price_iv import fit_iv


class ExtensionLogic(unittest.TestCase):
    def test_basket_metrics_and_repeated_servings(self):
        # Ten baskets: A in four, B in five, both in three.
        result = metrics(10, 4, 5, 3)
        self.assertAlmostEqual(result["confidence_a_to_b"], 0.75)
        self.assertAlmostEqual(result["lift"], 1.5)

    def test_censoring_risk_set_and_ties(self):
        records = pd.DataFrame(
            {"duration": [1, 2, 3, 3], "event": [True, False, True, False]}
        )
        curve = kaplan_meier(records)
        self.assertEqual(curve.at_risk.tolist(), [4, 3, 2])
        self.assertEqual(curve.gap_free.tolist(), [0.75, 0.75, 0.375])

    def test_gap_event_uses_confirmation_date(self):
        start, end = pd.Timestamp("2016-01-01"), pd.Timestamp("2016-01-06")
        dates = {start, pd.Timestamp("2016-01-04")}
        self.assertEqual(first_gap(dates, start, end, 2), (2, True))
        self.assertEqual(
            first_gap(dates, start, start + pd.Timedelta(days=1), 2), (1, False)
        )

    def test_snapshot_excludes_future_and_zero_fills_counts(self):
        days = pd.DataFrame(
            {
                "Userid": ["A", "B", "A"],
                "date": pd.to_datetime(["2016-06-30", "2016-05-01", "2016-07-15"]),
            }
        )
        base = snapshot(days, "2016-06-30")
        pd.testing.assert_frame_equal(base, snapshot(days.iloc[:2], "2016-06-30"))
        self.assertEqual(base.loc["A", "frequency_30d"], 1)
        self.assertEqual(base.loc["B", "frequency_30d"], 0)

    def test_fixed_cohort_report_and_structured_claim(self):
        food = pd.DataFrame(
            {
                "Userid": ["A", "B", "A", "A", "A", "NEW"],
                "date": pd.to_datetime(
                    [
                        "2016-04-01",
                        "2016-04-02",
                        "2016-05-03",
                        "2016-05-03",
                        "2016-06-01",
                        "2016-06-02",
                    ]
                ),
            }
        )
        evidence = monthly_review(food)
        self.assertEqual(evidence["periods"][0]["observed_user_days"], 1)
        self.assertEqual(evidence["periods"][0]["calendar_user_days"], 62)
        claim = {
            "metric": "logging_fraction",
            "period": "2016-06",
            "value": 1 / 60,
            "unit": evidence["unit"],
            "denominator": 60,
            "interpretation": "descriptive",
        }
        self.assertEqual(check_claim(claim, evidence), [])
        claim["value"] = float("nan")
        self.assertIn("numeric value", check_claim(claim, evidence))

    def test_adjustment_preserves_mean_but_can_increase_variance(self):
        y = np.array([0.0, 1.0, 2.0])
        centered = adjust(y, y, 1)
        self.assertTrue(np.allclose(centered, [1, 1, 1]))
        wrong = adjust(y, y, -1)
        self.assertEqual(wrong.mean(), y.mean())
        self.assertGreater(wrong.var(), y.var())

    def test_iv_recovers_noiseless_slope(self):
        price = np.array([1.0, 2.0, 4.0, 7.0])
        x = np.column_stack([np.ones(4), price])
        z = np.column_stack([np.ones(4), [1.0, 3.0, 2.0, 5.0]])
        result = fit_iv(1 - 2 * price, x, z)
        self.assertAlmostEqual(result["elasticity"], -2)


if __name__ == "__main__":
    unittest.main()
