"""Independent arithmetic, design, and input checks for the course examples."""
import unittest

import numpy as np
import pandas as pd
from scipy import stats

from mhealth_pairing import MONTHS, compare_uncertainty, monthly_rates
from store_randomization import compare_methods, simulate, welch, wilson


class InferenceChecks(unittest.TestCase):
    def test_fixed_roster_duplicate_days_and_late_entry(self):
        days = pd.DataFrame({"Userid": ["a", "b", "a", "a", "a", "c"],
            "date": pd.to_datetime(["2016-04-01", "2016-04-02", "2016-05-01",
                                    "2016-05-01", "2016-06-01", "2016-05-02"])})
        rates, monthly = monthly_rates(days)
        self.assertEqual(list(rates.index), ["a", "b"])
        np.testing.assert_allclose(rates.loc["a"], [1/31, 1/30])
        np.testing.assert_array_equal(rates.loc["b"], [0, 0])
        self.assertEqual([x["calendar_days"] for x in monthly], [62, 60])

    def test_paired_test_against_scipy(self):
        x = pd.DataFrame([[.1,.3],[.4,.2],[.5,.8],[.7,.9]], columns=MONTHS)
        result = compare_uncertainty(x)[0]
        reference = stats.ttest_rel(x.iloc[:,1], x.iloc[:,0])
        self.assertAlmostEqual(result["estimate_pp"], 12.5)
        self.assertAlmostEqual(result["p_value"], reference.pvalue)

    def test_user_permutation_keeps_pairs(self):
        x = pd.DataFrame([[.1,.3],[.4,.2],[.5,.8],[.7,.9]], columns=MONTHS)
        self.assertAlmostEqual(compare_uncertainty(x)[0]["se_pp"],
                               compare_uncertainty(x.iloc[[2,0,3,1]])[0]["se_pp"])

    def test_missing_pair_rejected(self):
        x = pd.DataFrame([[.1,.3],[.4,np.nan]], columns=MONTHS)
        with self.assertRaises(ValueError):
            compare_uncertainty(x)

    def test_welch_against_library(self):
        a, b = np.array([1,3,8,11]), np.array([2,6,7,9,17])
        effect, se, df, p = welch(a, b)
        ref = stats.ttest_ind(b, a, equal_var=False)
        self.assertAlmostEqual(effect[0]/se[0], ref.statistic)
        self.assertAlmostEqual(p[0], ref.pvalue)
        self.assertAlmostEqual(df[0], ref.df)

    def test_store_means_against_hand_calculation(self):
        y = np.array([[[0,2],[2,4],[4,6],[10,12]]], dtype=float)
        t = np.array([[False, False, True, True]])
        results = compare_methods(y, t)
        self.assertAlmostEqual(results["store_means"][0][0], 6)
        self.assertAlmostEqual(results["store_means"][1][0], np.sqrt(10))
        self.assertAlmostEqual(results["customer_rows"][0][0], 6)

    def test_copying_rows_does_not_add_stores(self):
        y = np.array([[[0,2],[2,4],[4,6],[10,12]]], dtype=float)
        t = np.array([[False, False, True, True]])
        a = compare_methods(y, t)
        b = compare_methods(np.repeat(y, 3, axis=2), t)
        for i in range(4):
            np.testing.assert_allclose(a["store_means"][i], b["store_means"][i])
        self.assertLess(b["customer_rows"][1][0], a["customer_rows"][1][0])

    def test_unbalanced_assignment_rejected(self):
        with self.assertRaises(ValueError):
            compare_methods(np.ones((1,4,3)), np.array([[True, False, False, False]]))

    def test_wilson_matches_exact_zero_boundary(self):
        low, high = wilson(0, 100)
        self.assertAlmostEqual(low, 0)
        z = stats.norm.ppf(.975)
        self.assertAlmostEqual(high, z*z/(100+z*z))

    def test_reproducibility_and_analytical_variance(self):
        a, _, data = simulate(repetitions=100, stores=8, customers=5, seed=19)
        b, _, _ = simulate(repetitions=100, stores=8, customers=5, seed=19)
        pd.testing.assert_frame_equal(a, b)
        row = a.loc[a.rho.eq(.3)].iloc[0]
        self.assertAlmostEqual(row.theoretical_effect_sd**2, 4*800/8*(.3+.7/5))
        self.assertEqual(data.groupby("store").assigned_promotion.nunique().max(), 1)


if __name__ == "__main__":
    unittest.main()
