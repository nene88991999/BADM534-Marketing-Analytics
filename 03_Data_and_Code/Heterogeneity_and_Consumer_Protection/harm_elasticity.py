"""Synthetic partial pooling: greater precision, fewer detected harms.

Normal working-prior posterior intervals; repeated-sample risk is evaluated
under an explicit two-point population. No consumer harms are estimated
from the released retail data.
"""
from pathlib import Path
import json
import numpy as np
import pandas as pd
from scipy.integrate import quad
from scipy.stats import norm

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "results"
HARM_SHARE = 0.1
HARM = 2.0             # Standardized harm: one unit is $10 per person-month.
SIGMA = 1.0
ALPHA = 0.05
POPULATION = 10_000
MONTHS = 12
DOLLARS_PER_UNIT = 10


def conditional_update(xtx, xty, error_variance, prior_mean, prior_covariance):
    """Normal coefficient update used inside hierarchical regression, no RNG."""
    prior_precision = np.linalg.inv(prior_covariance)
    precision = xtx/error_variance+prior_precision
    covariance = np.linalg.inv(precision)
    mean = np.linalg.solve(precision, xty/error_variance+prior_precision@prior_mean)
    return mean, covariance


def evaluate(weight):
    """weight is the fraction of the unpooled estimate retained, 0 < w <= 1."""
    if not 0 < weight <= 1:
        raise ValueError("Use 0 < weight <= 1.")
    z = norm.isf(ALPHA)
    posterior_sd = SIGMA*np.sqrt(weight)
    # Flag when posterior mean minus z times posterior SD exceeds zero.
    threshold = z*SIGMA/np.sqrt(weight)
    u = threshold/SIGMA-HARM/SIGMA
    missed = norm.cdf(u)
    false_flag = norm.sf(threshold/SIGMA)
    mean_mse = weight**2*SIGMA**2+(1-weight)**2*HARM_SHARE*HARM**2
    harmed_mse = weight**2*SIGMA**2+(1-weight)**2*HARM**2
    dollars = POPULATION*HARM_SHARE*HARM*DOLLARS_PER_UNIT*MONTHS*missed
    # Precision P=1/(w*sigma^2); d log H / d log P.
    elasticity = z/(2*np.sqrt(weight))*norm.pdf(u)/missed
    # Recalibrating to the same actual 5% false-positive rate changes the rule.
    matched_threshold = weight*z*SIGMA
    matched_detection = norm.sf(matched_threshold/(weight*SIGMA)-HARM/SIGMA)
    return dict(data_weight=weight, posterior_precision=1/posterior_sd**2,
                posterior_sd=posterior_sd, average_mse=mean_mse,
                harmed_group_mse=harmed_mse, detection_probability=1-missed,
                false_flag_probability=false_flag,
                missed_harm_probability=missed, consumer_loss_usd=dollars,
                harm_precision_elasticity=elasticity,
                matched_false_positive_detection=matched_detection)


def verify():
    """Numerical integration, derivative, denominator, and calibration checks."""
    # Scalar special case of the matrix update in bayesm's runiregG.
    mean, covariance = conditional_update(np.array([[1.0]]), np.array([2.0]),
                                         1.0, np.array([0.0]), np.array([[0.4]]))
    assert np.isclose(mean[0], 4/7)
    assert np.isclose(covariance[0, 0], 2/7)
    for w in (1.0, .75, .5, 2/7):
        row = evaluate(w)
        conditional = []
        for theta in (0.0, HARM):
            risk = quad(lambda y: (w*y-theta)**2*norm.pdf(y,theta,SIGMA),
                        -np.inf, np.inf)[0]
            conditional.append(risk)
        assert np.isclose((1-HARM_SHARE)*conditional[0]+HARM_SHARE*conditional[1],
                          row["average_mse"])
        assert np.isclose(conditional[1], row["harmed_group_mse"])
        threshold = norm.isf(ALPHA)*SIGMA/np.sqrt(w)
        detection = quad(lambda y: norm.pdf(y,HARM,SIGMA), threshold, np.inf)[0]
        assert np.isclose(detection, row["detection_probability"])
        if w < 1:
            step = 1e-5
            derivative = (np.log(evaluate(w+step)["consumer_loss_usd"])
                          -np.log(evaluate(w-step)["consumer_loss_usd"]))/(2*step)
            assert np.isclose(-w*derivative, row["harm_precision_elasticity"], rtol=1e-7)
        assert np.isclose(row["matched_false_positive_detection"], evaluate(1)["detection_probability"])
    pooled, raw = evaluate(2/7), evaluate(1)
    assert pooled["average_mse"] < raw["average_mse"]
    assert pooled["posterior_sd"] < raw["posterior_sd"]
    assert pooled["detection_probability"] < raw["detection_probability"]
    assert pooled["harmed_group_mse"] > raw["harmed_group_mse"]


def main():
    OUT.mkdir(exist_ok=True)
    verify()
    rows = [evaluate(w) for w in (1.0, .75, .5, 2/7)]
    pd.DataFrame(rows).to_csv(OUT / "precision_detection_scenarios.csv", index=False)
    curve = [evaluate(float(w)) for w in np.linspace(1, 2/7, 101)]
    pd.DataFrame(curve).to_csv(OUT / "precision_detection_curve.csv", index=False)
    setup = dict(harm_share=HARM_SHARE, harm_standard_units=HARM, sampling_sd=SIGMA,
                 population=POPULATION, months=MONTHS, dollars_per_unit=DOLLARS_PER_UNIT,
                 signal="Y conditional on theta is Normal(theta,1); theta is 0 with probability .9 and 2 with probability .1.",
                 working_prior="Normal(0,tau^2), where w=tau^2/(tau^2+1); w=1 is the unpooled limit.",
                 decision="One-sided 95% posterior lower bound exceeds zero. Actual false-positive rates differ.",
                 interpretation="Synthetic loss from missed harm; no real-data consumer effect, no bias reduction claim, no universal claim about heterogeneity adjustment.")
    (OUT / "precision_detection_setup.json").write_text(json.dumps(setup, indent=2)+"\n")
    print(pd.DataFrame(rows).to_string(index=False))
    print("Quadrature, finite differences, group risks, and matched-calibration checks passed.")


if __name__ == "__main__":
    main()
