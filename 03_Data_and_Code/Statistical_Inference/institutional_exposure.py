"""Synthetic electricity examples: bills, cancelled projects, and cost allocation.

All values are imposed. This is a two-period comparison, not a replication of
the paper's synthetic-control/within-utility capacity regression. No downloads.
"""
from pathlib import Path

import numpy as np
import pandas as pd

OUTPUT = Path(__file__).resolve().parent / "results"


def billing_examples():
    """One month per row; the same 1,000 customer accounts in every scenario."""
    rows = []
    for name, revenue, sales in [
        ("baseline", 100000., 1000.),
        ("more_use_same_average_price", 110000., 1100.),
        ("higher_price_less_use", 100000., 800.),
    ]:
        customers = 1000
        price = revenue/sales
        mean_use = sales/customers
        rows.append(dict(scenario=name, revenue_usd=revenue,
                         sales_mwh=sales, customer_months=customers,
                         average_price_usd_mwh=price,
                         use_mwh_per_customer_month=mean_use,
                         bill_usd_per_customer_month=revenue/customers))
    result = pd.DataFrame(rows)
    assert np.allclose(result.average_price_usd_mwh *
                       result.use_mwh_per_customer_month,
                       result.bill_usd_per_customer_month)
    return result


def donor_examples():
    """Assume equal baseline prices and no other changes in three utilities."""
    return pd.DataFrame([
        dict(utility="completed", project_status="operating",
             operating_addition_mw=100., prior_price=100., post_price=110.,
             project_related_increase=10., donor_weight=0.),
        dict(utility="cancelled", project_status="cancelled_after_investment",
             operating_addition_mw=0., prior_price=100., post_price=108.,
             project_related_increase=8., donor_weight=.75),
        dict(utility="unexposed", project_status="no_project",
             operating_addition_mw=0., prior_price=100., post_price=100.,
             project_related_increase=0., donor_weight=.25),
    ])


def donor_comparisons(utilities):
    """Compare changes, holding donor weights fixed at their imposed values."""
    treated = utilities.loc[utilities.utility == "completed"].iloc[0]
    donors = utilities.loc[utilities.donor_weight > 0]
    weights = donors.donor_weight.to_numpy()
    assert np.isclose(weights.sum(), 1)
    assert donors.operating_addition_mw.eq(0).all()
    treated_change = treated.post_price-treated.prior_price
    rows = []
    for scenario, donor_change in [
        ("unexposed_comparison", 0.),
        ("weighted_operationally_untreated", float(weights @
         (donors.post_price-donors.prior_price).to_numpy())),
    ]:
        rows.append(dict(comparison=scenario,
                         treated_change_usd_mwh=treated_change,
                         donor_change_usd_mwh=donor_change,
                         change_difference_usd_mwh=treated_change-donor_change))
    return pd.DataFrame(rows)


def residual_recovery(annual_requirement, developer_payment, reusable_offset,
                      allowed_fraction, residential_share, sales_mwh):
    """Illustrative annual recovery of unmatched costs, in USD/MWh.

    Requirement, payments, and the reuse offset all use annual USD. Fractions
    represent imposed cost-recovery and class-allocation rules. They are not
    estimated legal entitlements. Upfront capital expenditure is not used.
    """
    values = [annual_requirement, developer_payment, reusable_offset,
              allowed_fraction, residential_share, sales_mwh]
    if not np.isfinite(values).all() or min(values[:3]) < 0:
        raise ValueError("Finite inputs and nonnegative annual amounts required")
    if not 0 <= allowed_fraction <= 1 or not 0 <= residential_share <= 1:
        raise ValueError("Recovery and allocation fractions must be in [0, 1]")
    if sales_mwh <= 0:
        raise ValueError("Positive annual residential sales required")
    residual = max(annual_requirement-developer_payment-reusable_offset, 0.)
    return allowed_fraction*residential_share*residual/sales_mwh


def recovery_examples():
    rows = []
    for name, payment, allowed in [
        ("no_developer_payment", 0., 1.),
        ("partial_developer_payment", 500000., 1.),
        ("full_developer_payment", 1000000., 1.),
        ("recovery_disallowed", 0., 0.),
    ]:
        value = residual_recovery(1000000., payment, 0., allowed, .8, 100000.)
        rows.append(dict(scenario=name, annual_requirement_usd=1000000.,
                         developer_annual_payment_usd=payment,
                         reusable_annual_offset_usd=0., allowed_fraction=allowed,
                         residential_share=.8, annual_residential_mwh=100000.,
                         residential_increase_usd_mwh=value))
    return pd.DataFrame(rows)


def main():
    OUTPUT.mkdir(exist_ok=True)
    utilities = donor_examples()
    tables = {"institutional_bills": billing_examples(),
              "institutional_donors": utilities,
              "institutional_comparisons": donor_comparisons(utilities),
              "institutional_recovery": recovery_examples()}
    for name, table in tables.items():
        table.to_csv(OUTPUT/f"{name}.csv", index=False)


if __name__ == "__main__":
    main()
