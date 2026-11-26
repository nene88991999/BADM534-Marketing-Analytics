"""Independent exact checks of the synthetic reasoning examples."""
import unittest
from fractions import Fraction as F
from price_models import observed_joint, policy_purchase, purchase_probability
from valuation_sensitivity import BASELINE, ALTERNATIVE, VALUES, compare


class PriceModelChecks(unittest.TestCase):
    def test_observed_cells(self):
        expected = [F(1, 10), F(2, 5), F(3, 10), F(1, 5)]
        for model in ("price_response", "group_selection"):
            self.assertEqual([r["population_mass"] for r in observed_joint(model)], expected)

    def test_counterfactual_effects(self):
        self.assertEqual(policy_purchase("price_response", 20) -
                         policy_purchase("price_response", 10), F(-2, 5))
        self.assertEqual(policy_purchase("group_selection", 20) -
                         policy_purchase("group_selection", 10), 0)

    def test_new_randomized_cells_distinguish_rules(self):
        self.assertEqual(purchase_probability("price_response", "A", 20), F(2, 5))
        self.assertEqual(purchase_probability("group_selection", "A", 20), F(4, 5))
        self.assertEqual(purchase_probability("price_response", "B", 10), F(4, 5))
        self.assertEqual(purchase_probability("group_selection", "B", 10), F(2, 5))

    def test_declared_support(self):
        with self.assertRaises(ValueError):
            purchase_probability("price_response", "A", 30)


class ValuationChecks(unittest.TestCase):
    def test_hand_calculated_levels(self):
        self.assertEqual(compare(BASELINE, ALTERNATIVE, VALUES["large_gap_at_top"]),
                         (F(204, 5), F(228, 5), F(24, 5), F(24, 5)))
        self.assertEqual(compare(BASELINE, ALTERNATIVE, VALUES["large_gap_at_bottom"]),
                         (F(893, 10), F(422, 5), F(-49, 10), F(-49, 10)))

    def test_equal_endpoints_and_strict_ranking(self):
        for values in VALUES.values():
            self.assertEqual((values[0], values[-1]), (100, 0))
            self.assertTrue(all(a > b for a, b in zip(values, values[1:])))

    def test_every_rank_cutoff(self):
        differences = [sum(ALTERNATIVE[:k]) - sum(BASELINE[:k]) for k in range(1, 5)]
        self.assertEqual(differences, [F(1, 20), F(-1, 20), F(-1, 20), F(0)])

    def test_dominance_under_every_nonempty_step_value(self):
        dominating = (F(1, 2), F(3, 10), F(1, 10), F(1, 10))
        for k in range(1, 4):
            step = tuple(int(j < k) for j in range(4))
            self.assertGreaterEqual(compare(BASELINE, dominating, step)[2], 0)

    def test_costs_and_translation(self):
        values = VALUES["large_gap_at_top"]
        gain = compare(BASELINE, ALTERNATIVE, values, F(1))[3]
        self.assertEqual(gain, F(19, 5))
        shifted = tuple(v + 50 for v in values)
        self.assertEqual(compare(BASELINE, ALTERNATIVE, shifted)[2], F(24, 5))

    def test_invalid_distribution(self):
        with self.assertRaises(ValueError):
            compare((F(1), F(1)), (F(1), F(0)), (1, 0))


if __name__ == "__main__":
    unittest.main()
