"""Independent distribution identities and counterexample checks."""
import unittest
from fractions import Fraction

import numpy as np
from scipy.stats import chi2, ncx2

from andrews_inverse_power import inverse_radius, required_noncentrality
from data_center_claims import power, REFERENCE_PP, summarize
from logical_counterexamples import price_responses


class InversePowerChecks(unittest.TestCase):
    def test_scalar_inversion_matches_normal_tails(self):
        for se in [.160, .158*REFERENCE_PP, 493.0]:
            for target in [.5, .8, .9, .95]:
                d = inverse_radius([[se**2]], [1], target)
                self.assertAlmostEqual(power(d, se), target, places=11)

    def test_units_and_direction(self):
        v = np.diag([.25, 4.0])
        a = inverse_radius(v, [1, 0], .8)
        b = inverse_radius(v, [0, 1], .8)
        self.assertAlmostEqual(b/a, 4)
        self.assertAlmostEqual(inverse_radius(100*v, [1, 0], .8), 10*a)

    def test_covariance_rotation_preserves_power(self):
        v = np.array([[1., .3], [.3, 4.]])
        eta = np.array([1., 0.])
        rotation = np.array([[.6, -.8], [.8, .6]])
        self.assertAlmostEqual(inverse_radius(v, eta, .8),
            inverse_radius(rotation@v@rotation.T, rotation@eta, .8))

    def test_joint_monte_carlo_independently_checks_distribution(self):
        rng = np.random.default_rng(20261126)
        lam = required_noncentrality(.8, 2)
        z = rng.standard_normal((100000, 2))
        z[:, 0] += np.sqrt(lam)
        rejected = (z*z).sum(axis=1) > chi2.ppf(.95, 2)
        self.assertLess(abs(rejected.mean()-.8), .005)

    def test_radius_does_not_use_realized_estimate(self):
        a, b = summarize(0, 1), summarize(5, 1)
        self.assertEqual(a['mde80'], b['mde80'])
        self.assertEqual(b['upper95']-a['upper95'], 5)

    def test_invalid_inputs(self):
        for p in [.04, .05, 1]:
            with self.assertRaises(ValueError): required_noncentrality(p)
        with self.assertRaises(ValueError): inverse_radius([[1]], [2], .8)
        with self.assertRaises(np.linalg.LinAlgError):
            inverse_radius([[1, 1], [1, 1]], [1, 0], .8)


class CounterexampleChecks(unittest.TestCase):
    def test_agreement_on_support_does_not_imply_extrapolation(self):
        for i in range(101):
            a, b = price_responses(Fraction(i, 100))
            self.assertEqual(a, b)
        self.assertEqual(price_responses(Fraction(2)), (4, 14))

    def test_ratio_does_not_identify_numerator(self):
        self.assertEqual(Fraction(1000, 10), Fraction(1100, 11))
        self.assertNotEqual(1000, 1100)
        self.assertGreater(Fraction(1000, 8), Fraction(1000, 10))


if __name__ == '__main__':
    unittest.main()
