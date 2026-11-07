"""Evaluate imposed purchase probabilities on the same synthetic customers."""
from pathlib import Path
from fractions import Fraction as F
import csv
import json

HERE = Path(__file__).resolve().parent


def evaluate(rows, column):
    ids = [r["customer_id"] for r in rows]
    if not rows or any(not x for x in ids) or len(set(ids)) != len(ids):
        raise ValueError("Nonempty rows with unique customer IDs are required")
    y = [F(r["purchase"]) for r in rows]
    p = [F(r[column]) for r in rows]
    if set(y) != {0, 1} or any(x < 0 or x > 1 for x in p):
        raise ValueError("Both binary outcomes and probabilities in [0,1] are required")
    positive = [x for x, outcome in zip(p, y) if outcome == 1]
    negative = [x for x, outcome in zip(p, y) if outcome == 0]
    concordance = sum(F(a > b) + F(a == b, 2)
                      for a in positive for b in negative)
    auc = concordance / (len(positive) * len(negative))
    brier = sum((a - b) ** 2 for a, b in zip(p, y)) / len(y)
    bins = []
    for score in sorted(set(p)):
        outcomes = [b for a, b in zip(p, y) if a == score]
        bins.append(dict(model=column, mean_prediction=float(score),
                         customers=len(outcomes), purchases=int(sum(outcomes)),
                         observed_share=float(sum(outcomes) / len(outcomes))))
    metrics = dict(customers=len(y), purchases=int(sum(y)),
                   predicted_purchases=float(sum(p)), auc=float(auc),
                   auc_exact=str(auc), brier=float(brier), brier_exact=str(brier))
    return metrics, bins


def main():
    with (HERE / "inputs/purchase_predictions.csv").open(newline="") as stream:
        rows = list(csv.DictReader(stream))
    results, bins = {}, []
    for model in ("model_a", "model_b"):
        results[model], table = evaluate(rows, model)
        bins.extend(table)
    results["scope"] = "Fixed synthetic customers and imposed predictions; no model fit"
    output = HERE / "results"
    output.mkdir(exist_ok=True)
    (output / "ranking_calibration.json").write_text(json.dumps(results, indent=2) + "\n")
    with (output / "calibration_bins.csv").open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(bins[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(bins)
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
