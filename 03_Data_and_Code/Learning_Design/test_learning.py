"""Independent numerical checks of the teaching constructions."""
import unittest
from fractions import Fraction
from learning_comparisons import percentage_comparison, factorial_effects


class LearningChecks(unittest.TestCase):
    def test_published_rounding(self):
        self.assertEqual(percentage_comparison(78, 67),
                         (Fraction(11), Fraction(1100, 67)))

    def test_relative_denominator(self):
        self.assertEqual(percentage_comparison(40, 50), (Fraction(-10), Fraction(-20)))
        self.assertEqual(percentage_comparison(0, 0), (Fraction(0), None))

    def test_invalid_percentages(self):
        for a, b in [(-1, 50), (40, 101)]:
            with self.assertRaises(ValueError):
                percentage_comparison(a, b)

    def test_factorial_arithmetic(self):
        r = factorial_effects({(0, 0): 60, (1, 0): 66, (0, 1): 68, (1, 1): 77})
        self.assertEqual(tuple(r.values()), (6, 9, 8, 11, Fraction(15, 2),
                                             Fraction(19, 2), 3, 17))

    def test_same_bundle_different_components(self):
        a = factorial_effects({(0, 0): 60, (1, 0): 66, (0, 1): 68, (1, 1): 77})
        b = factorial_effects({(0, 0): 60, (1, 0): 77, (0, 1): 60, (1, 1): 77})
        self.assertEqual(a['whole_package_pp'], b['whole_package_pp'])
        self.assertNotEqual(a['formats_equal_weight_effect_pp'], b['formats_equal_weight_effect_pp'])

    def test_missing_cell(self):
        with self.assertRaises(ValueError):
            factorial_effects({(0, 0): 60, (1, 1): 77})


if __name__ == "__main__":
    unittest.main()
