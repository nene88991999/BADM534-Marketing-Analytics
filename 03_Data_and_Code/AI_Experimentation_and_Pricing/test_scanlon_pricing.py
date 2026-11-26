"""Independent economic checks for the five pricing and justification examples."""
import unittest
from fractions import Fraction as F
from assess_personalized_pricing import calculate as incidence
from compare_demand_completions import OBSERVED, calculate as completions, curves, integral
from evaluate_targeted_experiment import calculate as experiment
from reconstruct_competitive_targeting import calculate as game
from compare_pricing_damages import calculate as damages


class PricingChecks(unittest.TestCase):
    def test_group_h_burden(self):
        rows = incidence()["incidence"]
        h = next(r for r in rows if r["policy"] == "segmented" and r["group"] == "H")
        self.assertEqual(h["surplus_change_per_group_member"], -F(193, 24))
        self.assertEqual(h["population_lost_purchase_share"], F(1, 10))

    def test_cap_is_feasible_and_profitable(self):
        d = incidence()["policies"]
        self.assertEqual(d["discount_only"]["profit_per_eligible_customer"], F(92, 15))
        self.assertGreater(d["discount_only"]["profit_per_eligible_customer"],
                           d["uniform"]["profit_per_eligible_customer"])
        self.assertEqual(d["discount_only"]["strictly_worse_share"], 0)

    def test_incidence_adds_to_total(self):
        result = incidence()
        for policy, total in result["policies"].items():
            delta = sum(r["population_surplus_contribution"] for r in result["incidence"]
                        if r["policy"] == policy)
            self.assertEqual(delta, total["surplus_per_eligible_customer"] - F(259, 40))

    def test_known_stratum_weighting(self):
        d = experiment({"L": F(1, 4), "H": F(3, 4)})
        self.assertEqual(d["ipw_policy_effect"], F(25, 12))
        self.assertEqual(d["naive_difference"], F(475, 132))
        self.assertEqual(d["expected_lost_purchase_share"], F(3, 40))

    def test_balanced_assignment(self):
        d = experiment({"L": F(1, 2), "H": F(1, 2)})
        self.assertEqual(d["naive_difference"], d["ipw_policy_effect"])
        self.assertEqual(d["expected_lost_purchase_share"], F(1, 20))

    def test_positivity_and_missing_group(self):
        for p in [{"L": F(1, 2), "H": F(1)}, {"L": F(1, 2)}]:
            with self.assertRaises(ValueError): experiment(p)

    def test_same_observed_likelihood(self):
        for world in ["negative_change", "positive_change"]:
            for g, pts in curves(world).items():
                self.assertTrue(all(x0 < x1 and y0 >= y1 for (x0,y0),(x1,y1)
                                    in zip(pts, pts[1:])))
                self.assertEqual({p:dict(pts)[F(p)] for p in OBSERVED[g]}, OBSERVED[g])

    def test_opposite_welfare_signs(self):
        worlds = completions()["worlds"]
        self.assertEqual(worlds["negative_change"]["population_surplus_change"], -F(841, 500))
        self.assertEqual(worlds["positive_change"]["population_surplus_change"], F(341, 500))
        self.assertTrue(all(d["H_surplus_loss"] > 0 for d in worlds.values()))

    def test_integral_clipping(self):
        self.assertEqual(integral([(F(0),F(1)),(F(10),F(0))],F(2),F(8)), F(3))

    def test_monotonic_bounds(self):
        low, high = completions()["monotonic_surplus_change_bounds"]
        self.assertEqual(low, F(3,5)*5*F(1,2)-F(2,5)*10*F(4,5))
        self.assertEqual(high, F(3,5)*5*F(9,10)-F(2,5)*10*F(1,2))
        for w in completions()["worlds"].values():
            self.assertLess(low, w["population_surplus_change"])
            self.assertLess(w["population_surplus_change"], high)

    def test_published_game(self):
        d=game()
        self.assertEqual(d["pure_equilibria_from_rounded_payoffs"], [("behavioral","behavioral")])
        self.assertEqual(d["behavioral_vs_uniform_revenue_gains"], {"A":F(19,1000),"B":F(35,1000)})
        self.assertEqual(d["A_behavioral_vs_geobehavioral_gap_when_B_behavioral"], F(1,1000))

    def test_invoice_identity(self):
        d=damages()
        self.assertEqual(d["signed_invoice_difference"], 1840)
        self.assertEqual(d["revenue_change"], 1040)
        self.assertEqual(d["revenue_change"], d["signed_invoice_difference"]+
                         d["quantity_component_at_but_for_price"])

    def test_benchmark_sensitivity(self):
        self.assertEqual(damages(F(110))["signed_invoice_difference"], 920)
        self.assertEqual(damages(F(120))["signed_invoice_difference"], 0)
        self.assertEqual(damages(F(130))["signed_invoice_difference"], -920)

    def test_bad_damages_input(self):
        with self.assertRaises(ValueError): damages(actual_units=-1)


if __name__ == "__main__":
    unittest.main()
