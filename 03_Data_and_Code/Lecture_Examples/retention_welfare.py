"""Synthetic retention procedures with fixed, opposed monetary stakes.

Run with Python 3 from any directory. Uses only the standard library.
No customer data are loaded. All probabilities and values are imposed.
Outputs are dollars per eligible customer relative to direct choice.
"""
from pathlib import Path
import csv
import json
from math import isclose


def evaluate(probabilities, direct, firm_margin, customer_loss):
    if not 0 <= direct <= 1:
        raise ValueError("Direct-choice probability must be in [0, 1].")
    if firm_margin < 0 or customer_loss < 0:
        raise ValueError("This example requires opposed nonnegative stakes.")
    rows = []
    for procedure, probability in probabilities.items():
        if not 0 <= probability <= 1:
            raise ValueError("Each renewal probability must be in [0, 1].")
        change = probability - direct
        profit = firm_margin * change
        value = -customer_loss * change
        rows.append({
            "procedure": procedure,
            "renewal_probability": probability,
            "firm_profit_change": round(profit, 10),
            "customer_value_change": round(value, 10),
            "combined_surplus_change": round(profit + value, 10),
        })
    return rows


def main():
    probabilities = {"low_renewal": 0.10, "direct": 0.20,
                     "high_renewal": 0.60}
    margin, loss = 11.0, 10.0
    rows = evaluate(probabilities, 0.20, margin, loss)
    low, direct, high = rows
    assert direct["firm_profit_change"] == 0
    assert direct["customer_value_change"] == 0
    # Independent expected-level calculations use 100 eligible customers.
    n = 100
    baseline_profit = n * 0.20 * margin
    selected_profit = n * 0.60 * margin
    assert isclose(high["firm_profit_change"],
                   (selected_profit - baseline_profit) / n)
    assert isclose(high["customer_value_change"], -40 * loss / n)
    assert high["firm_profit_change"] == 4.4
    assert high["customer_value_change"] == -4.0
    assert high["combined_surplus_change"] == 0.4
    assert isclose(high["customer_value_change"] -
                   low["customer_value_change"], -5.0)
    folder = Path(__file__).resolve().parent
    with (folder / "retention_welfare.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    report = {"input_type": "synthetic imposed probabilities and stakes",
              "unit": "dollars per eligible customer",
              "benchmark": "direct choice, renewal probability 0.20",
              "firm_margin": margin, "customer_loss_per_renewal": loss,
              "procedures": rows}
    (folder / "retention_welfare_results.json").write_text(
        json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
