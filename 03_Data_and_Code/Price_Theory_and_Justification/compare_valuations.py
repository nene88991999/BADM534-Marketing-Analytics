"""Synthetic budgets, willingness to pay, and actual compensation.

Run with Python 3; only the standard library is required.
All inputs are constructed teaching values, with no estimated parameters.
"""
import json
import math
from pathlib import Path


def willingness_to_pay(budget, service_increment):
    """Solve log(budget - payment) + increment = log(budget)."""
    if budget <= 0 or service_increment < 0:
        raise ValueError("Use a positive budget and nonnegative increment.")
    return budget * (-math.expm1(-service_increment))


def compare():
    increment = 0.2
    rows = []
    for scenario, budgets in (
        ("baseline", {"A": 100.0, "B": 1000.0}),
        ("budgets_exchanged", {"A": 1000.0, "B": 100.0}),
    ):
        for person, budget in budgets.items():
            payment = willingness_to_pay(budget, increment)
            rows.append(dict(scenario=scenario, person=person,
                             budget_dollars=budget, service_increment=increment,
                             willingness_to_pay_dollars=payment))

    # A separate one-period project: the firm gains $140 and 100 residents
    # each lose $1 relative to no project. Transfers have zero resource cost.
    firm_gain = 140.0
    residents = 100
    loss_per_resident = 1.0
    policies = []
    for policy, payment in (("no_compensation", 0.0),
                            ("actual_compensation", loss_per_resident)):
        transfer = residents * payment
        firm_change = firm_gain - transfer
        resident_change = payment - loss_per_resident
        policies.append(dict(
            policy=policy, residents=residents,
            transfer_per_resident_dollars=payment,
            firm_change_dollars=firm_change,
            each_resident_change_dollars=resident_change,
            aggregate_dollar_change=firm_change + residents * resident_change,
            people_with_dollar_losses=residents if resident_change < 0 else 0,
        ))
    return dict(setup="Synthetic one-period comparisons; dollars and dimensionless utility",
                willingness_to_pay=rows, compensation=policies)


def main():
    results = compare()
    output = Path(__file__).resolve().parent / "results.json"
    output.write_text(json.dumps(results, indent=2) + "\n")
    for row in results["willingness_to_pay"]:
        print(f"{row['scenario']}: {row['person']}, budget "
              f"${row['budget_dollars']:.0f}, reservation price "
              f"${row['willingness_to_pay_dollars']:.2f}")
    for row in results["compensation"]:
        print(f"{row['policy']}: firm ${row['firm_change_dollars']:.0f}, "
              f"each resident ${row['each_resident_change_dollars']:.0f}, "
              f"aggregate ${row['aggregate_dollar_change']:.0f}, "
              f"{row['people_with_dollar_losses']} residents lose")


if __name__ == "__main__":
    main()
