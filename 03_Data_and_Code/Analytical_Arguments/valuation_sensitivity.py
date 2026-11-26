"""Synthetic welfare comparisons holding purchases and ordinal values fixed.

Each customer purchases one of four products. Values are imposed monetary
consumption values in USD per customer. Prices, other burdens, and procedural
cost differences are zero or common across procedures and cancel.
"""
import csv
from fractions import Fraction as F
from itertools import accumulate
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASELINE = (F(4, 10), F(3, 10), F(2, 10), F(1, 10))
ALTERNATIVE = (F(45, 100), F(2, 10), F(2, 10), F(15, 100))
VALUES = {"large_gap_at_top": (100, 2, 1, 0),
          "large_gap_at_bottom": (100, 99, 98, 0)}


def compare(baseline, alternative, values, incremental_cost=F(0)):
    """Return the consumption and net gain for the same customer population."""
    if not (len(baseline) == len(alternative) == len(values)):
        raise ValueError("Products must match across probabilities and values.")
    if any(p < 0 for p in baseline + alternative):
        raise ValueError("Probabilities must be nonnegative.")
    if sum(baseline) != 1 or sum(alternative) != 1:
        raise ValueError("Each purchase law must sum to one.")
    base = sum(p * v for p, v in zip(baseline, values))
    alt = sum(p * v for p, v in zip(alternative, values))
    cumulative = tuple(accumulate(q - p for p, q in zip(baseline, alternative)))
    gap_sum = sum((values[k] - values[k + 1]) * cumulative[k]
                  for k in range(len(values) - 1))
    assert alt - base == gap_sum
    return base, alt, alt - base, alt - base - incremental_cost


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
    cumulative = tuple(accumulate(q - p for p, q in zip(BASELINE, ALTERNATIVE)))
    rows = [{"product_rank": k + 1, "baseline_probability": BASELINE[k],
             "alternative_probability": ALTERNATIVE[k],
             "cumulative_change_pp": 100 * cumulative[k],
             "value_top_gap_usd": VALUES["large_gap_at_top"][k],
             "value_bottom_gap_usd": VALUES["large_gap_at_bottom"][k]}
            for k in range(4)]
    write_csv("purchase_and_value_inputs.csv", rows)
    results = []
    for name, values in VALUES.items():
        assert all(a > b for a, b in zip(values, values[1:]))
        base, alt, gain, net = compare(BASELINE, ALTERNATIVE, values)
        results.append({"valuation": name, "baseline_value_usd": base,
                        "alternative_value_usd": alt, "consumption_gain_usd": gain,
                        "incremental_cost_usd": 0, "net_gain_usd": net})
    write_csv("valuation_comparisons.csv", results)
    print("Same ranking and purchases; gains are +$4.80 and -$4.90 per customer.")


if __name__ == "__main__":
    main()
