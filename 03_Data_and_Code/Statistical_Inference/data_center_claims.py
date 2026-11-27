"""Reconstruct reported-table implications; no utility-panel replication."""
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import brentq
from scipy.stats import norm

ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"
REFERENCE_PP = 100 * 456 / 6804  # Ratio of reported means, pp of peak MW.
ALPHA = 0.05


def power(effect, se, alpha=ALPHA):
    """Two-sided normal-test power at an externally specified true effect."""
    if se <= 0 or not 0 < alpha < 1:
        raise ValueError("Positive SE and alpha strictly between zero and one required")
    z = norm.ppf(1 - alpha / 2)
    shift = np.asarray(effect) / se
    return norm.cdf(-z - shift) + norm.sf(z - shift)


def summarize(estimate, se):
    z = norm.ppf(0.975)
    return dict(estimate=estimate, se=se,
                p_zero=2 * norm.sf(abs(estimate / se)),
                ci95_low=estimate - z * se, ci95_high=estimate + z * se,
                upper95=estimate + norm.ppf(0.95) * se,
                mde80=brentq(lambda d: power(d, se) - 0.8, 0, 10 * se))


def main():
    RESULTS.mkdir(exist_ok=True)
    # Rana, Kaps, Netessine, October 2026 version: Tables 2, 4, and 7.
    # Published SEs already cluster by utility; retain them without inflation.
    inputs = [
        ("residential_reference", "Table 2 col 4; pp. 23-24", .261, .158,
         REFERENCE_PP, "USD/MWh at reference exposure", 41, 627),
        ("cloud_slope", "Table 4 col 4; p. 26", .158, .160,
         1, "USD/MWh per exposure pp", 41, 627),
        ("other_owner_slope", "Table 4 col 4; p. 26", 1.042, .477,
         1, "USD/MWh per exposure pp", 41, 627),
        ("sales_slope", "Table 7 col 1; p. 31", 291, 493,
         1, "quarterly MWh per added MW", 42, 648),
    ]
    estimates = []
    for key, source, b, se, scale, units, clusters, n in inputs:
        estimates.append(dict(case=key, source=source, reported_coefficient=b,
                              reported_se=se, scale=scale, units=units,
                              treated_utilities=clusters, observations=n,
                              **summarize(b * scale, se * scale)))
    pd.DataFrame(estimates).to_csv(RESULTS / "data_center_estimates.csv", index=False)

    se = .158 * REFERENCE_PP
    targets = [1.0, 2.0, 3.0]
    pd.DataFrame([dict(target_usd_per_mwh=d, power=power(d, se),
                       nonrejection_probability=1-power(d, se),
                       upper95_below_target=(.261*REFERENCE_PP + norm.ppf(.95)*se < d))
                  for d in targets]).to_csv(RESULTS / "data_center_power.csv", index=False)
    grid = np.linspace(0, 5, 101)
    pd.DataFrame(dict(target_usd_per_mwh=grid, power=power(grid, se))).to_csv(
        RESULTS / "data_center_power_curve.csv", index=False)

    # A hypothetical full 2,190-hour quarter with no displacement of other sales.
    pd.DataFrame([dict(utilization=u, hours=2190, target_mwh_per_mw=2190*u,
                       power=power(2190*u, 493)) for u in [.25, .50]]).to_csv(
        RESULTS / "data_center_sales_targets.csv", index=False)

    # Tables 2 and A.4: descriptive denominator, not a causal decomposition.
    increase = 166.85 - 123.59
    share = .261 * REFERENCE_PP / increase
    pd.DataFrame([dict(reference_exposure_pp=REFERENCE_PP,
                       observed_price_increase=increase,
                       estimated_share=share, residual_share=1-share,
                       developer_equality_p_reported=.101)]).to_csv(
        RESULTS / "data_center_reporting_checks.csv", index=False)

    # Synthetic counterexample: equal use, fixed population, one monthly period.
    # Two cost allocations produce the same average; consent is unobserved.
    n, mwh = 1000, 1.0
    rows = []
    for label, affected, extra_bill in [("uniform", n, 2), ("concentrated", 100, 20)]:
        total = affected * extra_bill
        rows.append(dict(scenario=label, households=n, affected_households=affected,
                         mwh_per_household=mwh, extra_bill_if_affected=extra_bill,
                         aggregate_extra_revenue=total,
                         average_increase_usd_per_mwh=total/(n*mwh)))
    pd.DataFrame(rows).to_csv(RESULTS / "data_center_incidence_illustration.csv", index=False)


if __name__ == "__main__":
    main()
