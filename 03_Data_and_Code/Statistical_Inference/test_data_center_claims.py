"""Independent identities and distribution checks for published-table arithmetic."""
import unittest

import numpy as np
from scipy.stats import chi2, ncx2, norm

from data_center_claims import REFERENCE_PP, power, summarize


class ReportedTableChecks(unittest.TestCase):
    def test_normal_power_matches_noncentral_chi_square(self):
        for d in [0, 1, 2, -2]:
            se = .158 * REFERENCE_PP
            expected = ncx2.sf(chi2.ppf(.95, 1), 1, (d/se)**2)
            self.assertAlmostEqual(power(d, se), expected, places=12)

    def test_scaling_preserves_test_and_interval(self):
        raw = summarize(.261, .158)
        scaled = summarize(.261*REFERENCE_PP, .158*REFERENCE_PP)
        self.assertAlmostEqual(raw['p_zero'], scaled['p_zero'])
        for key in ['estimate', 'se', 'ci95_low', 'ci95_high', 'upper95', 'mde80']:
            self.assertAlmostEqual(raw[key]*REFERENCE_PP, scaled[key])

    def test_bound_is_test_inversion(self):
        b, se = .261*REFERENCE_PP, .158*REFERENCE_PP
        upper = summarize(b, se)['upper95']
        self.assertAlmostEqual(norm.cdf((b-upper)/se), .05)
        self.assertGreater(norm.cdf((b-2)/se), .05)
        self.assertAlmostEqual(power(summarize(b, se)['mde80'], se), .8)

    def test_equal_aggregate_allows_unequal_incidence(self):
        uniform = np.full(1000, 2.0)
        concentrated = np.r_[np.full(100, 20.0), np.zeros(900)]
        self.assertEqual(uniform.sum(), concentrated.sum())
        self.assertEqual(uniform.mean(), concentrated.mean())
        self.assertGreater(concentrated.max(), uniform.max())

    def test_invalid_precision_rejected(self):
        with self.assertRaises(ValueError):
            power(1, 0)


if __name__ == '__main__':
    unittest.main()
