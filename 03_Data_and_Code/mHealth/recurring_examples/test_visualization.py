"""Independent examples for cohort denominators, ties, pairing, and chart errors."""

from copy import deepcopy
import unittest
import numpy as np
import pandas as pd
from chart_audit import check_chart
from visualization import MONTHS, ecdf, paired_summary, prepare


class VisualizationLogic(unittest.TestCase):
    def test_cohort_duplicate_dates_and_month_length(self):
        food = pd.DataFrame({
            "Userid": ["A", "B", "A", "A", "A", "NEW"],
            "date": pd.to_datetime(["2016-04-01", "2016-04-02", "2016-05-03",
                                    "2016-05-03", "2016-06-01", "2016-06-02"]),
        })
        rates, report = prepare(food)
        self.assertEqual(list(rates.index), ["A", "B"])
        self.assertEqual(report.calendar_user_days.tolist(), [62, 60])
        self.assertEqual(report.observed_user_days.tolist(), [1, 1])
        self.assertEqual(rates.loc["B"].tolist(), [0, 0])
        self.assertAlmostEqual(rates.loc["A", MONTHS[0]], 1 / 31)
        self.assertAlmostEqual(report.iloc[0].conditional_logging_percent, 100 / 31)

    def test_empty_month_is_zero_logging_with_undefined_conditional_rate(self):
        food = pd.DataFrame({"Userid": ["A"], "date": pd.to_datetime(["2016-04-01"])})
        rates, report = prepare(food)
        self.assertTrue(rates.eq(0).all().all())
        self.assertTrue(report.conditional_logging_percent.isna().all())
        self.assertTrue(report.entries_per_observed_day.isna().all())

    def test_ecdf_keeps_zero_and_tied_values(self):
        curve = ecdf([0, 0, 0.5, 1])
        self.assertEqual(curve.logging_percent.tolist(), [0, 50, 100])
        self.assertEqual(curve.users_at_value.tolist(), [2, 1, 1])
        self.assertEqual(curve.cumulative_percent.tolist(), [50, 75, 100])

    def test_pairing_preserves_identical_changes(self):
        rates = pd.DataFrame({MONTHS[0]: [0, 0.2, 0.4, 0.6],
                              MONTHS[1]: [0.1, 0.3, 0.5, 0.7]})
        result = paired_summary(rates, draws=100)
        for key in ["change_pp", "ci_low_pp", "ci_high_pp"]:
            self.assertAlmostEqual(result[key], 10)

    def test_chart_audit_rejects_units_population_and_clipping(self):
        evidence = {"months": [{"period": "May", "observed_user_days": 1,
                                 "calendar_user_days": 62}]}
        chart = {"unit": "percent of eligible user-days", "interpretation": "descriptive",
                 "mark": "bar", "y_domain": [0, 100],
                 "rows": [{"period": "May", "value": 100 / 62, "denominator": 62}]}
        self.assertEqual(check_chart(chart, evidence), [])
        wrong = deepcopy(chart)
        wrong["rows"][0].update(value=100 / 31, denominator=31)
        self.assertEqual(check_chart(wrong, evidence), ["denominator", "plotted value"])
        wrong = deepcopy(chart)
        wrong["y_domain"] = [1, 2]
        wrong["unit"] = "fraction"
        self.assertEqual(check_chart(wrong, evidence), ["axis unit", "bar baseline"])
        wrong = deepcopy(chart)
        wrong["rows"][0]["value"] = np.nan
        self.assertEqual(check_chart(wrong, evidence), ["plotted value"])
        wrong = deepcopy(chart)
        wrong["rows"] *= 2
        self.assertEqual(check_chart(wrong, evidence), ["period coverage"])


if __name__ == "__main__":
    unittest.main()
