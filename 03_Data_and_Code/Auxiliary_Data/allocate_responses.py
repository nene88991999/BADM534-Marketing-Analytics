"""Four invented product profiles and a cost comparison at a common MSE target.

Adaptation of Jasin, Lin, and Zhang (2026), Section 5.3. All parameters are
imposed. Independent Gaussian errors and the specified bias features define
the model; this program calculates analytic moments without collecting data.
"""
import argparse
import csv
import json
from math import ceil, isfinite, sqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load_parameters(path=ROOT / "data/parameters.json"):
    parameters = json.loads(Path(path).read_text())
    for key in ("primary_variance", "auxiliary_variance", "primary_cost",
                "auxiliary_cost", "mse_target"):
        if not isfinite(parameters[key]) or parameters[key] <= 0:
            raise ValueError(f"{key} must be finite and positive.")
    if len(parameters["primary_coefficients"]) != 3:
        raise ValueError("Primary coefficients must follow intercept, feature, price.")
    if len(parameters["auxiliary_bias_coefficients"]) != 2:
        raise ValueError("Bias coefficients must follow intercept, price.")
    return parameters


def optimal_precision(lam):
    if not isfinite(lam) or lam <= 0:
        raise ValueError("The information-cost ratio must be finite and positive.")
    if lam >= 1 / 3:
        return 3.0, 0.0
    primary = 2 + sqrt(2 * lam / (1 - lam))
    auxiliary = sqrt(2 * (1 - lam) / lam) - 1 - sqrt(2 * lam / (1 - lam))
    return primary, auxiliary


def calculate(parameters):
    b0, bf, bp = parameters["primary_coefficients"]
    g0, gp = parameters["auxiliary_bias_coefficients"]
    profiles = []
    for price in (-1, 1):
        for feature in (-1, 1):
            primary = b0 + bf * feature + bp * price
            profiles.append(dict(price=price, feature=feature,
                primary_mean=round(primary, 12),
                auxiliary_mean=round(primary + g0 + gp * price, 12)))
    vp, va = parameters["primary_variance"], parameters["auxiliary_variance"]
    cp, ca = parameters["primary_cost"], parameters["auxiliary_cost"]
    target = parameters["mse_target"]
    lam = ca * va / (cp * vp)
    t, s = optimal_precision(lam)
    primary_n = 4 * ceil(t * vp / (4 * target))
    auxiliary_n = 4 * ceil(s * va / (4 * target))
    reference_n = 4 * ceil(3 * vp / (4 * target))
    tp, ta = primary_n / vp, auxiliary_n / va
    cost = cp * primary_n + ca * auxiliary_n
    summary = dict(information_cost_ratio=lam, mse_target=target,
        primary_n=primary_n, auxiliary_n=auxiliary_n,
        primary_per_profile=primary_n // 4, auxiliary_per_profile=auxiliary_n // 4,
        primary_only_n=reference_n, primary_only_cost=cp * reference_n,
        primary_only_mse=3 * vp / reference_n, mixed_cost=cost,
        rounded_saving_fraction=1 - cost / (cp * reference_n),
        asymptotic_saving_fraction=1 - (t + lam * s) / 3,
        primary_precision=tp, auxiliary_precision=ta,
        intercept_variance=1 / tp, price_variance=1 / tp,
        feature_variance=1 / (tp + ta),
        correct_model_mse=2 / tp + 1 / (tp + ta))
    curve = [dict(information_cost_ratio=0.0, saving_fraction=1 / 3,
                  fully_confounded_saving=0.0, limiting_value=True)]
    ratios = [0.000001, 0.00001, 0.0001, 0.0002, 0.0005]
    ratios += [i / 1000 for i in range(1, 401)]
    for ratio in ratios:
        t, s = optimal_precision(ratio)
        curve.append(dict(information_cost_ratio=ratio,
            saving_fraction=1 - (t + ratio * s) / 3,
            fully_confounded_saving=0.0, limiting_value=False))
    return profiles, summary, curve


def write_csv(path, rows):
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def run(output):
    profiles, summary, curve = calculate(load_parameters())
    output.mkdir(parents=True, exist_ok=True)
    write_csv(output / "profile_means.csv", profiles)
    write_csv(output / "value_curve.csv", curve)
    (output / "allocation.json").write_text(json.dumps(summary, indent=2, allow_nan=False) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "results")
    run(parser.parse_args().output)
