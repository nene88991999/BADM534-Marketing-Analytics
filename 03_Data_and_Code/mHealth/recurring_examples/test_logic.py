"""Small counterexamples check the meaning of the transformations."""

import unittest
import numpy as np
import pandas as pd
from common import make_daily
from audit import require_unique
from ranking import evaluation_cases, personal_frequency, ranking_metrics
from nutrition import goldberg_bounds


class MeasurementChecks(unittest.TestCase):
    def test_goldberg_published_table(self):
        # Black (2000), Table 8, n=1, d=7, PAL=1.55: rounded limits 1.05 and 2.28.
        low, high = goldberg_bounds(7, 1.55)
        self.assertEqual((round(low, 2), round(high, 2)), (1.05, 2.28))

    def test_repeated_total_and_invalid_share(self):
        frame = pd.DataFrame(
            {
                "Userid": ["a"] * 4,
                "date": pd.to_datetime(
                    ["2016-01-01", "2016-01-01", "2016-01-03", "2016-01-03"]
                ),
                "category": ["x", "y", "x", "y"],
                "Calories": [90, 10, -1, 10],
                "Foodcalories": [100, 100, 9, 9],
                "Budgetcalories": [200] * 4,
            }
        )
        result = make_daily(frame)
        self.assertEqual(len(result), 2)  # No invented January 2 observation.
        self.assertEqual(result.food_calories.iloc[0], 100)
        self.assertAlmostEqual(result.variety.iloc[0], 0.18)
        self.assertTrue(np.isnan(result.variety.iloc[1]))

    def test_join_guard_rejects_multiplication(self):
        with self.assertRaises(ValueError):
            require_unique(pd.DataFrame({"user": ["a", "a"]}), ["user"])

    def test_target_never_enters_history(self):
        dates = pd.date_range("2016-05-01", periods=31).tolist() + [
            pd.Timestamp("2016-07-02")
        ]
        baskets = pd.DataFrame(
            {
                "Userid": ["a"] * len(dates),
                "date": dates,
                "basket": [("past",)] * 31 + [("future",)],
            }
        )
        cases, _, _ = evaluation_cases(baskets, "2016-07-01", ["past", "future"])
        history, target = cases[0]
        self.assertEqual(target, {"future"})
        np.testing.assert_array_equal(
            personal_frequency(history, "2016-07-01", ["past", "future"], None), [1, 0]
        )
        self.assertEqual(ranking_metrics(["past"], target), (0, 0))


if __name__ == "__main__":
    unittest.main()
