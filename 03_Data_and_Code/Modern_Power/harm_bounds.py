"""Reported-table sensitivity, scalar equivalence, and bounded-bias inference.

Rounded estimates and clustered SEs are treated as a fixed Gaussian approximation.
Targets are illustrative, not validated tolerances or original prespecified margins.
No utility panel, synthetic-control refit, or event-study covariance is available here.
"""
import json
from pathlib import Path

from scipy.optimize import brentq
from scipy.stats import norm

ALPHA = 0.05
REFERENCE_PP = 100 * 456 / 6804  # Ratio of reported means, not mean utility ratio.
CASES = (
    ("residential_reference", "Table 2 column 4, p. 23",
     .261 * REFERENCE_PP, .158 * REFERENCE_PP,
     "USD/MWh at reference exposure", (1., 2., 3.)),
    ("four_owner_slope", "Table 4 column 4, p. 26",
     .158, .160, "USD/MWh per exposure percentage point", (.1, .2, .3)),
)


def zero_null_power(effect, se):
    """Rejection probability at a specified alternative; no observed-power input."""
    z = norm.ppf(1 - ALPHA / 2)
    return float(norm.cdf(-z - effect / se) + norm.sf(z - effect / se))


def folded_cdf(cutoff, boundary, se):
    """Probability that |Normal(boundary,se**2)| is at most cutoff."""
    return float(norm.cdf((cutoff - boundary) / se)
                 - norm.cdf((-cutoff - boundary) / se))


def assess(estimate, se, margin):
    if se <= 0 or margin <= 0:
        raise ValueError("Positive SE and margin required")
    z = norm.ppf(1 - ALPHA)
    upper = estimate + z * se
    # H0: theta >= margin against theta < margin.
    upper_p = float(norm.cdf((estimate - margin) / se))
    # H0: |theta| >= margin; intersection of two one-sided tests.
    tost_p = max(upper_p, float(norm.sf((estimate + margin) / se)))
    # Scalar folded-normal equivalence test: size ALPHA at +/- margin.
    critical = brentq(lambda c: folded_cdf(c, margin, se) - ALPHA,
                     0, margin + 10 * se)
    folded_p = folded_cdf(abs(estimate), margin, se)
    return dict(
        margin=margin, zero_null_power_at_margin=zero_null_power(margin, se),
        upper95=float(upper), one_sided_margin_p=upper_p,
        excludes_positive_margin=bool(upper < margin),
        tost_p=float(tost_p), tost_equivalent=bool(tost_p < ALPHA),
        folded_p=folded_p, folded_equivalent=bool(folded_p < ALPHA),
        folded_critical=critical,
    )


def build():
    cases = []
    for name, source, estimate, se, units, margins in CASES:
        cases.append(dict(case=name, source=source, estimate=estimate, se=se,
                          units=units,
                          p_zero=float(2 * norm.sf(abs(estimate / se))),
                          upper95=float(estimate + norm.ppf(.95) * se),
                          comparisons=[assess(estimate, se, d) for d in margins]))
    # A scalar sensitivity calculation with an imposed bound |bias| <= B.
    # This is not the full HonestDiD estimator or an estimated bias correction.
    b, se = CASES[0][2:4]
    bias = [dict(assumed_bias_bound=B, units="USD/MWh", upper95=float(
                b + norm.ppf(.95) * se + B)) for B in (0., .5, 1.)]
    return dict(alpha=ALPHA, reference_exposure_pp=REFERENCE_PP,
                setup="Fixed-SE Gaussian approximations to rounded published tables",
                margins="Teaching alternatives; no validated policy tolerance",
                cases=cases, bounded_bias=bias)


def main():
    result = build()
    Path(__file__).with_name("results.json").write_text(
        json.dumps(result, indent=2) + "\n")
    for case in result["cases"]:
        print(case["case"], case["units"], f'upper95={case["upper95"]:.4f}')
        for r in case["comparisons"]:
            print(f'  margin={r["margin"]:g}, power={r["zero_null_power_at_margin"]:.3f}, '
                  f'upper-test p={r["one_sided_margin_p"]:.3f}, '
                  f'TOST p={r["tost_p"]:.3f}, folded p={r["folded_p"]:.3f}')


if __name__ == "__main__":
    main()
