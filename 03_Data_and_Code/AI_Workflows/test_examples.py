"""Small exact counterexamples for the teaching calculations."""
import itertools
import unittest
from fractions import Fraction
from factorial import contrasts
from investment import price_bounds, reuse_hours
from repeated_selection import expected_selected_accuracy, select_candidate


class ExampleChecks(unittest.TestCase):
    def test_additive_changes_have_no_interaction(self):
        effects = contrasts({(0, 0): Fraction(1, 10), (0, 1): Fraction(3, 10),
                             (1, 0): Fraction(4, 10), (1, 1): Fraction(6, 10)})
        self.assertEqual(effects["interaction"], 0)
        self.assertEqual(effects["joint_change"], Fraction(1, 2))

    def test_binomial_maximum_against_exhaustive_binary_outcomes(self):
        outcomes = list(itertools.product((0, 1), repeat=6))
        expected = sum(max(sum(x[:3]), sum(x[3:])) / 3 for x in outcomes) / len(outcomes)
        self.assertAlmostEqual(expected_selected_accuracy(3, 2), expected)
        self.assertAlmostEqual(expected_selected_accuracy(80, 1), 0.5)

    def test_tie_rule_uses_first_candidate(self):
        self.assertEqual(select_candidate([1, 3, 3, 0]), 1)

    def test_upkeep_can_prevent_recovery_of_setup(self):
        self.assertLess(reuse_hours(1000, 6, 2, 1.25, 0.75)[2], 0)
        self.assertEqual(reuse_hours(0, 6, 2, 1.25, 0.25), (0, 6, -6))

    def test_equality_allows_zero_surplus_only(self):
        self.assertEqual(price_bounds(100, 60, 10, 20, 100, 10), (30, 30))
        with self.assertRaises(ValueError):
            price_bounds(100, 60, 10, 20, 100, 0)


if __name__ == "__main__":
    unittest.main()
