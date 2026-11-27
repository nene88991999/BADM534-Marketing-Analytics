"""Inverse power in a fixed Wald approximation (Andrews, 1989).

Published inputs are rounded coefficients/clustered SEs, not a panel replication.
The two-outcome covariance and precision multipliers are synthetic illustrations.
"""
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import brentq
from scipy.stats import chi2, ncx2

from data_center_claims import REFERENCE_PP

OUTPUT = Path(__file__).resolve().parent / "results"
ALPHA = .05


def required_noncentrality(target_power, restrictions=1, alpha=ALPHA):
    """Invert the noncentral chi-square power function at a fixed test size."""
    if restrictions < 1 or int(restrictions) != restrictions:
        raise ValueError("A positive integer number of restrictions is required")
    if not 0 < alpha < target_power < 1:
        raise ValueError("Require 0 < alpha < target power < 1")
    cutoff = chi2.ppf(1-alpha, restrictions)
    objective = lambda lam: ncx2.sf(cutoff, restrictions, lam)-target_power
    upper = 1.0
    while objective(upper) < 0:
        upper *= 2
    return brentq(objective, 0, upper)


def inverse_radius(covariance, direction, target_power, alpha=ALPHA):
    """Deviation d=r*direction needed for power; direction has Euclidean norm 1."""
    v, eta = np.asarray(covariance, float), np.asarray(direction, float)
    q = eta.size
    if v.shape != (q, q) or not np.all(np.isfinite(v)):
        raise ValueError("Finite square covariance matching the direction required")
    if not np.allclose(v, v.T) or not np.isclose(eta @ eta, 1):
        raise ValueError("Symmetric covariance and unit direction required")
    np.linalg.cholesky(v)  # Positive definiteness; no pseudoinverse substitution.
    information = eta @ np.linalg.solve(v, eta)
    return np.sqrt(required_noncentrality(target_power, q, alpha)/information)


def main():
    OUTPUT.mkdir(exist_ok=True)
    sources = [("residential_reference", .158*REFERENCE_PP, "USD/MWh"),
               ("four_owner_slope", .160, "USD/MWh per exposure pp"),
               ("sales_slope", 493.0, "quarterly MWh per added MW")]
    rows = []
    for name, se, unit in sources:
        for probability in [.5, .8, .9, .95]:
            radius = inverse_radius([[se**2]], [1], probability)
            rows.append(dict(case=name, se=se, units=unit, alpha=ALPHA,
                             target_power=probability, deviation=radius,
                             standardized_deviation=radius/se))
    pd.DataFrame(rows).to_csv(OUTPUT/"andrews_inverse_power.csv", index=False)

    # Assumed precision changes, not estimated corrections to the published SE.
    rows = []
    for multiplier in [.75, 1, 1.5]:
        se = .158*REFERENCE_PP*multiplier
        rows.append(dict(se_multiplier=multiplier, se=se,
                         mde80=inverse_radius([[se**2]], [1], .8)))
    pd.DataFrame(rows).to_csv(OUTPUT/"andrews_precision_scenarios.csv", index=False)

    # Synthetic independent outcomes A and B, each measured in USD/MWh.
    # V is the covariance of their estimators, not individual observations.
    v = np.diag([.5**2, 2.0**2])
    directions = {"A_only": [1., 0.], "B_only": [0., 1.],
                  "equal_increases": [1/np.sqrt(2), 1/np.sqrt(2)]}
    rows = []
    for name, direction in directions.items():
        radius = inverse_radius(v, direction, .8)
        delta = radius*np.asarray(direction)
        rows.append(dict(direction=name, restrictions=2, alpha=ALPHA,
                         target_power=.8, radius=radius,
                         effect_A=delta[0], effect_B=delta[1]))
    pd.DataFrame(rows).to_csv(OUTPUT/"andrews_directional_power.csv", index=False)


if __name__ == "__main__":
    main()
