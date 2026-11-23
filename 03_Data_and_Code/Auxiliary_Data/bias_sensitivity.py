"""Expected coefficient error when auxiliary feature bias is omitted.

Both source counts increase together at a fixed allocation ratio. Errors
remain independent with the variances in parameters.json. Analytic variance
and squared bias refer to the three primary-model coefficients.
"""
import argparse
import json
from math import isfinite
from pathlib import Path
from allocate_responses import ROOT, calculate, load_parameters, write_csv


def evaluate(parameters):
    _, allocation, _ = calculate(parameters)
    delta = parameters["omitted_feature_bias"]
    if not isfinite(delta):
        raise ValueError("The omitted feature bias must be finite.")
    rows = []
    for scale in parameters["sample_multipliers"]:
        if not isinstance(scale, int) or scale <= 0:
            raise ValueError("Sample multipliers must be positive integers.")
        primary_n = scale * allocation["primary_n"]
        auxiliary_n = scale * allocation["auxiliary_n"]
        t = primary_n / parameters["primary_variance"]
        s = auxiliary_n / parameters["auxiliary_variance"]
        coefficient_error = delta * s / (t + s)
        variance = 2 / t + 1 / (t + s)
        rows.append(dict(sample_multiplier=scale, primary_n=primary_n,
            auxiliary_n=auxiliary_n,
            expected_feature_coefficient=parameters["primary_coefficients"][1] + coefficient_error,
            feature_coefficient_error=coefficient_error,
            total_coefficient_variance=variance, squared_bias=coefficient_error ** 2,
            correct_model_mse=variance, omitted_bias_mse=variance + coefficient_error ** 2,
            original_mse_target=parameters["mse_target"]))
    return rows


def run(output):
    rows = evaluate(load_parameters())
    output.mkdir(parents=True, exist_ok=True)
    write_csv(output / "bias_sensitivity.csv", rows)
    summary = {
        "scope": "Analytic moments in an invented balanced linear design.",
        "first_allocation": rows[0],
        "last_allocation": rows[-1],
        "bias_features_in_fitted_model": ["intercept", "price"],
        "additional_bias_feature_in_sensitivity": "premium feature",
        "expanded_dictionary": ["intercept", "premium feature", "price"],
        "expanded_dictionary_auxiliary_value": 0.0,
        "value_scope": "Unrestricted bias coefficients and worst-case MSE for the full primary coefficient vector.",
    }
    (output / "bias_summary.json").write_text(json.dumps(summary, indent=2, allow_nan=False) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "results")
    run(parser.parse_args().output)
