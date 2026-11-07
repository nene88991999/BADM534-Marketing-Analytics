"""Synthetic customer spending: preserve pairs when estimating mean change."""
from pathlib import Path
import csv
import json
import math
import statistics as st
from scipy.stats import t

HERE = Path(__file__).resolve().parent


def evaluate(rows):
    if len(rows) < 2:
        raise ValueError("At least two complete customer pairs are required")
    ids = [row["customer_id"] for row in rows]
    if any(not value for value in ids) or len(set(ids)) != len(ids):
        raise ValueError("Customer IDs must be nonempty and unique")
    before = [float(row["before_dollars"]) for row in rows]
    after = [float(row["after_dollars"]) for row in rows]
    if any(not math.isfinite(x) or x < 0 for x in before + after):
        raise ValueError("Spending must be finite and nonnegative")
    change = [b - a for a, b in zip(before, after)]
    n = len(rows)
    mean = st.mean(change)
    se = st.stdev(change) / math.sqrt(n)
    covariance = sum((a - st.mean(before)) * (b - st.mean(after))
                     for a, b in zip(before, after)) / (n - 1)
    independent_se = math.sqrt((st.variance(before) + st.variance(after)) / n)
    margin = float(t.ppf(0.975, df=n - 1)) * se
    return dict(customers=n, mean_before=st.mean(before),
                mean_after=st.mean(after), mean_change=mean,
                paired_standard_error=se, covariance=covariance,
                independent_standard_error=independent_se,
                ci_lower=mean - margin, ci_upper=mean + margin,
                ci_scope="Hypothetical iid normal customer differences; 95% t interval",
                data_scope="Eight imposed pairs; descriptive change, no causal effect")


def main():
    with (HERE / "inputs/paired_spending.csv").open(newline="") as stream:
        rows = list(csv.DictReader(stream))
    result = evaluate(rows)
    output = HERE / "results"
    output.mkdir(exist_ok=True)
    (output / "paired_changes.json").write_text(json.dumps(result, indent=2) + "\n")
    with (output / "customer_changes.csv").open("w", newline="") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(["customer_id", "change_dollars"])
        writer.writerows((r["customer_id"], float(r["after_dollars"])
                         - float(r["before_dollars"])) for r in rows)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
