import unittest
from fractions import Fraction as F
from evaluate_pricing import demand, surplus, best_uniform, evaluate, GROUPS


class PricingChecks(unittest.TestCase):
    def test_uniform_optimum_and_independent_totals(self):
        p = best_uniform(list(GROUPS.values()))
        self.assertEqual(p, F(19, 3))
        r = evaluate({"L": p, "H": p}, p)
        self.assertEqual(r["profit_per_eligible_customer"], F(361, 60))
        self.assertEqual(r["surplus_per_eligible_customer"], F(259, 40))
        self.assertEqual(r["purchase_share"], F(19, 20))

    def test_segmented_distribution(self):
        r = evaluate({"L": F(6), "H": F(15)}, F(19, 3))
        self.assertEqual(r["profit_per_eligible_customer"], F(81, 10))
        self.assertEqual(r["surplus_per_eligible_customer"], F(69, 20))
        self.assertEqual(r["strictly_better_share"], F(3, 5))
        self.assertEqual(r["strictly_worse_share"], F(2, 5))

    def test_discount_policy_can_benefit_both_sides(self):
        r = evaluate({"L": F(6), "H": F(19, 3)}, F(19, 3))
        self.assertEqual(r["profit_per_eligible_customer"], F(92, 15))
        self.assertEqual(r["surplus_per_eligible_customer"], F(20, 3))
        self.assertEqual(r["strictly_worse_share"], 0)
        self.assertEqual(r["purchase_share"], 1)

    def test_support_boundaries(self):
        self.assertEqual(demand(F(4), F(6), F(10)), 1)
        self.assertEqual(surplus(F(4), F(6), F(10)), 4)
        self.assertEqual(demand(F(10), F(6), F(10)), 0)
        self.assertEqual(surplus(F(12), F(6), F(10)), 0)
        self.assertEqual(best_uniform([(F(1), F(10), F(30))]), 15)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError): demand(F(-1), F(6), F(10))
        with self.assertRaises(ValueError): demand(F(7), F(10), F(6))
        with self.assertRaises(ValueError): evaluate({"L": F(6)}, F(6))


if __name__ == "__main__":
    unittest.main()
