"""Small counterexamples for missingness, keys, forecast timing, and scoring."""
import unittest

import numpy as np
import pandas as pd

from api_checks import check_time, status
from predict import brier_score, fit_probabilities
from prepare import make_transitions, validate_panel


class McBrokenTests(unittest.TestCase):
    def test_missing_flags_and_check_times(self):
        self.assertTrue(pd.isna(status(None)))
        self.assertEqual(status(False), 0)
        with self.assertRaises(ValueError):
            status("false")
        self.assertTrue(pd.isna(check_time("2026-01-01T18:00:00Z", "unknown")))
        self.assertEqual(check_time("2026-01-01T18:00:00Z", "Checked 12 minutes ago"),
                         pd.Timestamp("2026-01-01T17:48:00Z"))

    def test_duplicate_and_unmatched_keys(self):
        panel = pd.DataFrame({"date": [pd.Timestamp("2026-01-01")], "store_key": [1],
                              "is_broken": [0], "last_checked_min": [10]})
        dim = pd.DataFrame({"store_key": [1]})
        validate_panel(panel, dim)
        with self.assertRaises(ValueError):
            validate_panel(pd.concat([panel, panel]), dim)
        with self.assertRaises(ValueError):
            validate_panel(panel, pd.DataFrame({"store_key": [2]}))

    def test_calendar_matching_and_unobserved_target(self):
        # Key 1 is absent on day 2; shifting rows would falsely join days 1 and 3.
        panel = pd.DataFrame({"date": pd.to_datetime(["2026-01-01", "2026-01-03",
                                                       "2026-01-01", "2026-01-02"]),
                              "store_key": [1, 1, 2, 2], "is_broken": [1, 0, 0, 1]})
        daily = pd.DataFrame({"date": pd.date_range("2026-01-01", periods=3),
                              "n_checked": 3000, "offset_hours": 0})
        result = make_transitions(panel, daily)
        day2 = result[result.date.eq("2026-01-02")].set_index("previous_unavailable")
        self.assertEqual(day2.loc[1, "n_origins"], 1)
        self.assertEqual(day2.loc[1, "n_labeled"], 0)
        self.assertEqual(day2.loc[0, "n_unavailable"], 1)
        self.assertEqual(result.n_labeled.sum(), 1)

    def test_grouped_brier_matches_individual_rows(self):
        actual = np.array([1, 0, 0, 1, 1])
        probabilities = np.array([0.2, 0.2, 0.2, 0.8, 0.8])
        self.assertAlmostEqual(brier_score(np.array([3, 2]), np.array([1, 2]),
                                          np.array([0.2, 0.8])),
                               np.mean((actual - probabilities)**2))

    def test_future_labels_do_not_enter_training(self):
        data = pd.DataFrame({"date": pd.to_datetime(["2026-07-01", "2026-07-01", "2026-08-01"]),
                             "previous_unavailable": [0, 1, 1],
                             "n_labeled": [10, 10, 10], "n_unavailable": [1, 7, 9]})
        cutoff = pd.Timestamp("2026-08-01")
        before = fit_probabilities(data[data.date < cutoff])
        data.loc[data.date >= cutoff, "n_unavailable"] = 0
        after = fit_probabilities(data[data.date < cutoff])
        self.assertEqual(before[0], after[0])
        pd.testing.assert_series_equal(before[1], after[1])


if __name__ == "__main__":
    unittest.main()
