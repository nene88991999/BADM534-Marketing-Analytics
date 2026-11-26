"""Exact synthetic purchase laws with equal fit and different policy effects.

Each customer receives one offer and can buy one unit. Two equally common
groups historically receive different prices. All probabilities are imposed
population quantities; there is no sampled dataset or estimated coefficient.
"""
import csv
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
GROUPS = {"A": F(1, 2), "B": F(1, 2)}
HISTORICAL_PRICE = {"A": 10, "B": 20}
MODELS = ("price_response", "group_selection")


def purchase_probability(model, group, price):
    """Probability per offer at a USD price in the specified two-price menu."""
    if group not in GROUPS or price not in (10, 20):
        raise ValueError("The example covers groups A/B and prices 10/20 only.")
    if model == "price_response":
        return F(6, 5) - F(price, 25)
    if model == "group_selection":
        return {"A": F(4, 5), "B": F(2, 5)}[group]
    raise ValueError(model)


def observed_joint(model):
    """Joint probabilities of group, price, and purchase in historical offers."""
    rows = []
    for group, weight in GROUPS.items():
        price = HISTORICAL_PRICE[group]
        prob = purchase_probability(model, group, price)
        for purchase in (0, 1):
            mass = weight * (prob if purchase else 1 - prob)
            rows.append({"group": group, "price_usd": price,
                         "purchase": purchase, "population_mass": mass})
    return rows


def policy_purchase(model, price):
    """Assign the same price to all customers; preserve group weights and rules."""
    return sum(weight * purchase_probability(model, group, price)
               for group, weight in GROUPS.items())


def write_csv(name, rows):
    output = HERE / "results"
    output.mkdir(exist_ok=True)
    with (output / name).open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]),
                                lineterminator="\n")
        writer.writeheader()
        writer.writerows({k: float(v) if isinstance(v, F) else v
                          for k, v in row.items()} for row in rows)


def main():
    observed = observed_joint(MODELS[0])
    assert observed == observed_joint(MODELS[1])
    assert sum(row["population_mass"] for row in observed) == 1
    write_csv("observed_purchase_law.csv", observed)
    counterfactuals = []
    effects = []
    for model in MODELS:
        for group in GROUPS:
            for price in (10, 20):
                counterfactuals.append({"model": model, "group": group,
                    "price_usd": price,
                    "purchase_probability": purchase_probability(model, group, price),
                    "historically_observed": price == HISTORICAL_PRICE[group]})
        low, high = (policy_purchase(model, price) for price in (10, 20))
        effects.append({"model": model, "purchase_at_10": low,
                        "purchase_at_20": high, "effect_pp": 100 * (high - low)})
    write_csv("conditional_purchase_rules.csv", counterfactuals)
    write_csv("policy_effects.csv", effects)
    print("Identical historical joint laws; policy effects are -40 and 0 pp.")


if __name__ == "__main__":
    main()
