"""Synthetic price endogeneity and an exclusion-restriction sensitivity."""

from pathlib import Path
import json
import numpy as np


def fit_iv(y, x, z):
    # Instruments include the intercept. Avoid constructing an n-by-n matrix.
    xhat = z @ np.linalg.lstsq(z, x, rcond=None)[0]
    bread = np.linalg.inv(xhat.T @ x)
    beta = bread @ xhat.T @ y
    residual = y - x @ beta
    scores = xhat * residual[:, None]
    covariance = bread @ (scores.T @ scores) @ bread.T
    covariance *= len(y) / (len(y) - x.shape[1])  # HC1 correction
    se = np.sqrt(np.diag(covariance))
    return {
        "elasticity": float(beta[1]),
        "robust_se": float(se[1]),
        "ci95": [float(beta[1] - 1.96 * se[1]), float(beta[1] + 1.96 * se[1])],
    }


def calculate():
    rng = np.random.default_rng(534)
    n = 2000
    cost, demand, pricing_noise, sales_noise = rng.normal(size=(4, n))
    log_price = 2 + 0.4 * cost + 0.6 * demand + 0.2 * pricing_noise
    log_quantity = 5 - 1.5 * log_price + demand + 0.2 * sales_noise
    x = np.column_stack([np.ones(n), log_price])
    z = np.column_stack([np.ones(n), cost])
    first = z @ np.linalg.lstsq(z, log_price, rcond=None)[0]
    residual_ss = np.square(log_price - first).sum()
    total_ss = np.square(log_price - log_price.mean()).sum()
    first_stage_f = (total_ss - residual_ss) / (residual_ss / (n - 2))
    result = {
        "data": "synthetic independent markets",
        "markets": n,
        "seed": 534,
        "true_elasticity": -1.5,
        "ols": fit_iv(log_quantity, x, x),
        "valid_iv": fit_iv(log_quantity, x, z),
        "invalid_iv_direct_cost_effect_0_5": fit_iv(log_quantity + 0.5 * cost, x, z),
        "first_stage_f": float(first_stage_f),
    }
    return result


if __name__ == "__main__":
    result = calculate()
    output = Path(__file__).resolve().parent / "price_iv_results.json"
    output.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")
    print(json.dumps(result, indent=2))
