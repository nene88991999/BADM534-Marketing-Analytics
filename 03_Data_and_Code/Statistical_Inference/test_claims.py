"""Independent numerical and inferential checks for claims and decisions."""
import unittest

import numpy as np
import pandas as pd
from scipy import stats

from campaign_decisions import campaign, portfolio
from equivalence_claims import CASES, assess
from pvalue_distributions import pooled_test, run


class ClaimChecks(unittest.TestCase):
    def test_pooled_statistic_against_scipy(self):
        a, b = np.array([[1., 4., 8., 3.]]), np.array([[2., 7., 5., 10.]])
        effect, se, p = pooled_test(a, b)
        ref = stats.ttest_ind(b, a, axis=1, equal_var=True)
        np.testing.assert_allclose(effect / se, ref.statistic)
        np.testing.assert_allclose(p, ref.pvalue)

    def test_repeated_draws_and_bin_counts(self):
        a = run(repetitions=300, seed=7)
        b = run(repetitions=300, seed=7)
        for x, y in zip(a, b):
            pd.testing.assert_frame_equal(x, y)
        for (stores, truth), bins in a[1].groupby(["stores", "true_effect_dollars"]):
            row = a[0].query("stores == @stores and true_effect_dollars == @truth").iloc[0]
            self.assertEqual(bins["count"].sum(), 300)
            self.assertEqual(bins.iloc[0]["count"], row.rejections)
            self.assertAlmostEqual(bins.fraction.sum(), 1)

    def test_power_and_estimate_variance(self):
        summary, _, _ = run(repetitions=20000)
        for row in summary.itertuples():
            self.assertLess(abs(row.rejection_rate - row.analytical_power),
                            4 * row.mc_standard_error)
            self.assertLess(abs(row.estimate_sd_dollars / row.analytical_se_dollars - 1), .03)
            self.assertAlmostEqual(row.analytical_se_dollars**2, 1072 / row.stores)
        np.testing.assert_allclose(summary.loc[summary.true_effect_dollars.eq(0), "analytical_power"], .05)

    def test_portfolio_denominators(self):
        rows, ratio = portfolio()
        np.testing.assert_allclose(rows.expected_reject, [40, 160])
        self.assertAlmostEqual(rows.tests.sum(), 1000)
        self.assertAlmostEqual(ratio, .2)
        self.assertAlmostEqual(portfolio(null_fraction=1)[1], 1)
        self.assertTrue(np.isnan(portfolio(null_fraction=0, power=0)[1]))

    def test_campaign_against_chi_square(self):
        row = campaign()
        counts = [[101000, 899000], [100000, 900000]]
        ref = stats.chi2_contingency(counts, correction=False)
        self.assertAlmostEqual(row["p_value"], ref.pvalue)
        self.assertAlmostEqual(row["z"]**2, ref.statistic)

    def test_campaign_economic_units(self):
        row = campaign()
        self.assertAlmostEqual(row["lift"] * 100, .1)
        self.assertAlmostEqual(row["break_even_lift"] * 100, .25)
        self.assertAlmostEqual(row["net_dollars_per_treated_customer"], -.06)
        self.assertLess(row["net_ci95_high"], 0)
        self.assertGreater(row["ci95_low"], 0)

    def test_equivalence_against_shifted_library_tests(self):
        for case in CASES:
            row = assess(*case)
            _, n, a, b, sd = case
            lower = stats.ttest_ind_from_stats(b + 5, sd, n, a, sd, n,
                                              equal_var=True, alternative="greater")
            upper = stats.ttest_ind_from_stats(b - 5, sd, n, a, sd, n,
                                              equal_var=True, alternative="less")
            self.assertAlmostEqual(row["tost_lower_p"], lower.pvalue)
            self.assertAlmostEqual(row["tost_upper_p"], upper.pvalue)
            self.assertEqual(row["equivalent"], row["ci90_low"] > -5 and row["ci90_high"] < 5)

    def test_conclusions_follow_the_hypothesis(self):
        a, b, c, d = [assess(*case) for case in CASES]
        self.assertGreater(a["p_zero"], .05)
        self.assertFalse(a["equivalent"])
        self.assertGreater(b["p_zero"], .05)
        self.assertTrue(b["equivalent"])
        self.assertLess(c["p_zero"], .05)
        self.assertTrue(c["equivalent"])
        self.assertFalse(d["equivalent"])
        self.assertTrue(d["noninferior_below_upper_bound"])

    def test_boundary_not_selected_after_result(self):
        self.assertFalse(assess("boundary", 1000, 60, 65, 1)["equivalent"])
        row = assess(*CASES[2], bound=2)
        self.assertFalse(row["equivalent"])

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            campaign(n=100, treatment=101)
        with self.assertRaises(ValueError):
            portfolio(null_fraction=1.1)
        with self.assertRaises(ValueError):
            assess("invalid", 1, 60, 63, 20)


if __name__ == "__main__":
    unittest.main()
