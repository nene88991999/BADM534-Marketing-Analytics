"""Solve a synthetic two-restaurant market using exact rational arithmetic."""
import argparse
import csv
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load_parameters(path):
    raw = json.loads(path.read_text())
    if raw["data_type"] != "synthetic":
        raise ValueError("This example requires explicitly synthetic inputs")
    values = {key: F(str(raw[key])) for key in
              ("a_low", "a_high", "cost", "substitution")}
    values["accuracies"] = [F(str(x)) for x in raw["accuracies"]]
    if not 0 <= values["substitution"] < 1:
        raise ValueError("Substitution must be in [0, 1)")
    if not 0 <= values["cost"] < values["a_low"] < values["a_high"]:
        raise ValueError("Require 0 <= cost < a_low < a_high")
    if not values["accuracies"] or len(set(values["accuracies"])) != len(values["accuracies"]):
        raise ValueError("Provide distinct signal accuracies")
    if any(not F(1, 2) <= r <= 1 for r in values["accuracies"]):
        raise ValueError("Signal accuracy must be in [0.5, 1]")
    return values


def choose_price(expected_a, cost, substitution, objective):
    if objective == "independent":
        return ((1 - substitution) * expected_a + cost) / (2 - substitution)
    if objective == "joint":
        return (expected_a + cost) / 2
    raise ValueError("Unknown pricing objective")


def calculate(parameters):
    low, high = parameters["a_low"], parameters["a_high"]
    cost, d = parameters["cost"], parameters["substitution"]
    states = {"low": low, "high": high}
    outcomes, policies = [], []
    for r in parameters["accuracies"]:
        for objective in ("independent", "joint"):
            cells = []
            for state, actual_a in states.items():
                for signal, signal_a in states.items():
                    probability = (r if state == signal else 1 - r) / 2
                    if probability == 0:
                        continue
                    expected_a = r * signal_a + (1 - r) * (low + high - signal_a)
                    price = choose_price(expected_a, cost, d, objective)
                    q = (actual_a - price) / (1 + d)
                    if q <= 0 or price < cost:
                        raise ValueError("Reported prices require positive interior quantities and margins")
                    profit = 2 * (price - cost) * q
                    consumer_surplus = (1 + d) * q * q
                    gross_benefit = 2 * actual_a * q - (1 + d) * q * q
                    welfare = gross_benefit - 2 * cost * q
                    if welfare != profit + consumer_surplus:
                        raise ArithmeticError("Surplus accounting failed")
                    cells.append(dict(objective=objective, accuracy=r,
                        state=state, signal=signal, probability=probability,
                        actual_a=actual_a, expected_a=expected_a, price=price,
                        quantity=2 * q, profit=profit,
                        consumer_surplus=consumer_surplus, total_welfare=welfare,
                        expenditure=2 * price * q,
                        forecast_mse=(actual_a - expected_a) ** 2))
            if sum(x["probability"] for x in cells) != 1:
                raise ArithmeticError("Each policy must retain probability one")
            summary = dict(objective=objective, accuracy=r)
            for key in ("price", "quantity", "profit", "consumer_surplus",
                        "total_welfare", "expenditure", "forecast_mse"):
                summary[key] = sum(x["probability"] * x[key] for x in cells)
            summary["paid_price"] = summary["expenditure"] / summary["quantity"]
            outcomes.extend(cells)
            policies.append(summary)
    return outcomes, policies


def write_csv(path, rows):
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({key: format(float(value), ".10f") if isinstance(value, F)
                             else value for key, value in row.items()})


def run(parameters_path, output):
    outcomes, policies = calculate(load_parameters(parameters_path))
    output.mkdir(parents=True, exist_ok=True)
    write_csv(output / "state_outcomes.csv", outcomes)
    write_csv(output / "policies.csv", policies)
    exact = [{k: str(v) if isinstance(v, F) else v for k, v in row.items()}
             for row in policies]
    (output / "exact_results.json").write_text(json.dumps(exact, indent=2) + "\n")
    for row in policies:
        print(row["objective"], float(row["accuracy"]),
              "profit", round(float(row["profit"]), 4),
              "consumer surplus", round(float(row["consumer_surplus"]), 4))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--parameters", type=Path, default=ROOT / "parameters.json")
    parser.add_argument("--output", type=Path, default=ROOT / "results")
    args = parser.parse_args()
    run(args.parameters, args.output)
