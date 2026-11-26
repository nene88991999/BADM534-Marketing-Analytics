"""Construct synthetic counterexamples to extrapolation and ratio interpretations.

No observation from the data-center study is used in these constructions.
"""
import csv
from fractions import Fraction
from pathlib import Path

OUTPUT = Path(__file__).resolve().parent / "results"


def price_responses(load):
    """Load is a normalized index; responses have hypothetical USD/MWh units."""
    linear = 2*load
    capacity_threshold = linear + 10*max(load-1, 0)**2
    return linear, capacity_threshold


def write_rows(name, rows):
    with (OUTPUT/name).open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=rows[0])
        writer.writeheader()
        writer.writerows(rows)


def main():
    OUTPUT.mkdir(exist_ok=True)
    rows = []
    for load in [Fraction(i, 4) for i in range(5)]+[Fraction(2)]:
        a, b = price_responses(load)
        rows.append(dict(load=float(load), linear=float(a), threshold=float(b),
                         within_assumed_historical_support=load <= 1))
    write_rows("logic_extrapolation.csv", rows)
    # Hypothetical one-period totals in dollars and MWh.
    rows = []
    for label, cost, sales in [("baseline", 1000, 10),
                               ("cost_and_sales_rise", 1100, 11),
                               ("sales_fall", 1000, 8)]:
        rows.append(dict(case=label, total_cost_usd=cost, sales_mwh=sales,
                         cost_per_mwh=float(Fraction(cost, sales))))
    write_rows("logic_cost_ratios.csv", rows)


if __name__ == "__main__":
    main()
