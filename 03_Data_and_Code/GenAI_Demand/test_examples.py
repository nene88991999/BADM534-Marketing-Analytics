"""Hand-checkable counterexamples for the GenAI demand teaching cases."""
import unittest

import numpy as np
import pandas as pd

from demand import price_projection
from measurement import title_calendar, unique_views
from retention import acquisition_type, cohort_outcomes


class TeachingChecks(unittest.TestCase):
    def test_alias_retrieval_is_not_a_second_observation(self):
        d = pd.DataFrame({"date": pd.to_datetime(["2026-01-01"] * 2),
                          "article": ["A", "A"], "provider": ["P", "P"], "views": [7, 7]})
        self.assertEqual(unique_views(d).views.sum(), 7)
        d.loc[1, "views"] = 8
        with self.assertRaisesRegex(ValueError, "Conflicting"):
            unique_views(d)

    def test_unknown_title_day_is_distinct_from_zero(self):
        d = pd.DataFrame({"date": pd.to_datetime(["2026-01-01"] * 2 + ["2026-01-02"]),
                          "article": ["A", "B", "A"], "provider": ["P"] * 3,
                          "views": [7, 0, 9]})
        c = title_calendar(d, ["A", "B"], "2026-01-01", "2026-01-02")
        self.assertEqual(c.selected_title_views.iloc[0], 7)
        self.assertTrue(pd.isna(c.selected_title_views.iloc[1]))

    def test_fixed_cohort_and_endpoint_return(self):
        d = pd.DataFrame([(1, "2025-01", "A"), (2, "2025-01", "A"),
                          (3, "2025-01", "B"), (1, "2025-02", "B"),
                          (1, "2025-03", "A"), (2, "2025-03", "B"),
                          (3, "2025-03", "B")], columns=["consumer_id", "month", "provider"])
        c = cohort_outcomes(d, "A", "2025-01", 2, ["2025-01", "2025-02", "2025-03"])
        last = c.iloc[-1]
        self.assertEqual(last.cohort_size, 2)
        self.assertEqual(last.same_provider, 1)
        self.assertEqual(last.other_provider_only, 1)
        self.assertEqual(last.continuous_same_provider, 0)

    def test_out_of_support_horizon_is_not_churn(self):
        d = pd.DataFrame([(1, "2025-01", "A")], columns=["consumer_id", "month", "provider"])
        with self.assertRaisesRegex(ValueError, "calendar"):
            cohort_outcomes(d, "A", "2025-01", 1, ["2025-01"])

    def test_acquisition_includes_four_distinct_events(self):
        self.assertEqual(acquisition_type(set(), {"B"}, False), "first_paid_entry")
        self.assertEqual(acquisition_type(set(), {"B"}, True), "category_return")
        self.assertEqual(acquisition_type({"A"}, {"B"}, True), "complete_provider_switch")
        self.assertEqual(acquisition_type({"A"}, {"A", "B"}, True), "provider_addition")

    def test_exact_binary_model_recovers_known_slope(self):
        d = pd.DataFrame({"provider": ["A", "A", "B", "B"],
                          "month": ["01", "02", "01", "02"], "basic_price": [10, 20, 20, 10]})
        utility = np.array([-2.0, -1.5, -1.0, -0.5]) - 0.2 * d.basic_price
        p = 1 / (1 + np.exp(-utility))
        self.assertAlmostEqual(price_projection(d, p)["price_coefficient"], -0.2)

    def test_no_price_variation_after_controls(self):
        d = pd.DataFrame({"provider": ["A", "A", "B", "B"],
                          "month": ["01", "02", "01", "02"], "basic_price": [10, 10, 20, 20]})
        with self.assertRaisesRegex(ValueError, "identified"):
            price_projection(d, [0.1, 0.2, 0.3, 0.4])

    def test_zero_share_does_not_get_an_arbitrary_pseudocount(self):
        d = pd.DataFrame({"provider": ["A", "A", "B", "B"],
                          "month": ["01", "02", "01", "02"], "basic_price": [10, 20, 20, 10]})
        with self.assertRaisesRegex(ValueError, "strictly"):
            price_projection(d, [0.0, 0.1, 0.2, 0.3])


if __name__ == "__main__":
    unittest.main()
