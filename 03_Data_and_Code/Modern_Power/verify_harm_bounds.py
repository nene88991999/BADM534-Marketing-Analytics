"""Independent numerical checks for the teaching calculations."""
import json
from pathlib import Path

import numpy as np
from scipy.integrate import quad
from scipy.stats import foldnorm, norm

from harm_bounds import ALPHA, CASES, assess, build, folded_cdf, zero_null_power


def main():
    result = build()
    for _, _, b, se, _, margins in CASES:
        for d in margins:
            r = assess(b, se, d)
            expected = foldnorm.ppf(ALPHA, d / se, scale=se)
            assert np.isclose(r["folded_critical"], expected)
            assert np.isclose(r["folded_p"], foldnorm.cdf(abs(b), d / se, scale=se))
            c = r["folded_critical"]
            boundary_size = quad(lambda x: norm.pdf(x, d, se), -c, c)[0]
            assert np.isclose(boundary_size, ALPHA)
            assert folded_cdf(c, 1.5 * d, se) <= ALPHA
            assert np.isclose(folded_cdf(c, -d, se), ALPHA)
            z = norm.ppf(1 - ALPHA / 2)
            tails = quad(lambda x: norm.pdf(x, d, se), -np.inf, -z * se)[0]
            tails += quad(lambda x: norm.pdf(x, d, se), z * se, np.inf)[0]
            assert np.isclose(zero_null_power(d, se), tails, atol=1e-9)
            assert r["excludes_positive_margin"] == (r["one_sided_margin_p"] < ALPHA)
            # Changing the unit rescales the region and preserves decisions.
            scaled = assess(b / 10, se / 10, d / 10)
            assert np.isclose(r["folded_p"], scaled["folded_p"])
    # A valid method must also recognize equivalence in an informative setup.
    # This mathematical check is synthetic, not a result for the paper.
    narrow = assess(0, .01, 1)
    assert narrow["excludes_positive_margin"] and narrow["tost_equivalent"]
    assert narrow["folded_equivalent"]
    b, se = CASES[0][2:4]
    for r in result["bounded_bias"]:
        B = r["assumed_bias_bound"]
        assert np.isclose(r["upper95"], b + norm.ppf(.95) * se + B)
        # Worst-case understatement: estimator mean is theta-B.
        assert np.isclose(norm.sf(-norm.ppf(.95)), .95)
    assert json.loads(Path(__file__).with_name("results.json").read_text()) == result
    print("Verified quadrature, folded-normal quantiles, boundary size, unit invariance, "
          "test/interval duality, power, an informative synthetic case, and saved results.")


if __name__ == "__main__":
    main()
