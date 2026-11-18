"""Imposed discount, margin, and complaint curves; no estimated customer harm."""
from pathlib import Path
import argparse
import json
import numpy as np


def outcomes(a):
    a = np.asarray(a)
    price = 20 * (1 - a/100)
    profit = 10 + .4*a - .01*a*a
    units = profit / (price - 4)  # Fixed $4 unit cost; expected units per eligible customer.
    return profit, price*units, units, .01 + .0001*a*a


def run(output):
    output.mkdir(parents=True, exist_ok=True)
    a = np.linspace(0, 40, 401)
    profit, revenue, units, complaints = outcomes(a)
    eligible = complaints <= .03
    indexes = {"revenue": int(np.argmax(revenue)), "profit": int(np.argmax(profit)),
               "profit_with_complaint_cap": int(np.argmax(np.where(eligible, profit, -np.inf)))}
    result = {key: {"discount_pp": float(a[i]), "profit_usd": float(profit[i]),
                    "revenue_usd": float(revenue[i]), "complaint_fraction": float(complaints[i])}
              for key, i in indexes.items()}
    np.savetxt(output / "objectives.csv", np.c_[a, profit, revenue, units, complaints], delimiter=",",
               header="discount_pp,profit_usd,revenue_usd,units_per_customer,complaint_fraction", comments="", fmt="%.10g")
    (output / "objectives_summary.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parent / "results")
    run(parser.parse_args().output)
