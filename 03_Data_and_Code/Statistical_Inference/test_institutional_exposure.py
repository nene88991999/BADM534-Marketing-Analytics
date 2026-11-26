"""Independent accounting and counterfactual checks for synthetic examples."""
import unittest

import numpy as np

from institutional_exposure import (billing_examples, donor_examples,
                                    donor_comparisons, residual_recovery)


class InstitutionalExposureTests(unittest.TestCase):
    def test_billing_identity_and_changes(self):
        table = billing_examples().set_index("scenario")
        base = table.loc["baseline"]
        more = table.loc["more_use_same_average_price"]
        less = table.loc["higher_price_less_use"]
        self.assertEqual(more.average_price_usd_mwh, base.average_price_usd_mwh)
        self.assertEqual(more.bill_usd_per_customer_month, 110.)
        self.assertEqual(less.average_price_usd_mwh, 125.)
        self.assertEqual(less.bill_usd_per_customer_month,
                         base.bill_usd_per_customer_month)

    def test_aggregation_matches_individual_accounts(self):
        # Unequal usage with a common fixed charge. Reconstruct from accounts.
        use = np.array([.4, .6, 2.])
        bills = 20.+80.*use
        price = bills.sum()/use.sum()
        self.assertAlmostEqual(price*use.mean(), bills.mean())
        self.assertFalse(np.isclose(price, np.mean(bills/use)))

    def test_zero_operating_capacity_does_not_mean_zero_cost(self):
        t = donor_examples()
        donor = t.loc[t.utility == "cancelled"].iloc[0]
        self.assertEqual(donor.operating_addition_mw, 0.)
        self.assertEqual(donor.post_price-donor.prior_price, 8.)
        out = donor_comparisons(t).set_index("comparison")
        self.assertEqual(out.loc["weighted_operationally_untreated",
                                 "change_difference_usd_mwh"], 4.)
        self.assertEqual(out.loc["unexposed_comparison",
                                 "change_difference_usd_mwh"], 10.)

    def test_common_shock_cancels_from_change_difference(self):
        t = donor_examples()
        original = donor_comparisons(t).iloc[1].change_difference_usd_mwh
        t["post_price"] += 23.
        self.assertEqual(donor_comparisons(t).iloc[1].change_difference_usd_mwh,
                         original)

    def test_cost_recovery_depends_on_rules_and_guarantees(self):
        f = residual_recovery
        self.assertEqual(f(1e6, 0, 0, 1, .8, 1e5), 8.)
        self.assertEqual(f(1e6, 5e5, 0, 1, .8, 1e5), 4.)
        self.assertEqual(f(1e6, 1e6, 0, 1, .8, 1e5), 0.)
        self.assertEqual(f(1e6, 0, 0, 0, .8, 1e5), 0.)
        self.assertEqual(f(1e6, 0, 1e6, 1, .8, 1e5), 0.)
        self.assertEqual(f(1e6, 2e6, 0, 1, .8, 1e5), 0.)

    def test_invalid_units_and_fractions(self):
        for args in [(1, 0, 0, 1.1, .8, 1), (1, 0, 0, 1, -.1, 1),
                     (1, 0, 0, 1, .8, 0), (1, -1, 0, 1, .8, 1),
                     (np.nan, 0, 0, 1, .8, 1)]:
            with self.assertRaises(ValueError):
                residual_recovery(*args)


if __name__ == "__main__":
    unittest.main()
