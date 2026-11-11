"""Evaluate saved synthetic grader decisions on a fixed public practice set."""
from pathlib import Path
import argparse
import csv
import json

HERE = Path(__file__).resolve().parent


def evaluate(cases, predictions):
    reference = {row["id"]: row["reference"] for row in cases}
    if len(reference) != len(cases) or set(reference.values()) != {"PASS", "FAIL"}:
        raise ValueError("Unique IDs and both reference classes are required")
    graders = {}
    for row in predictions:
        if row["case_id"] not in reference or not row["grader"]:
            raise ValueError("Unknown case or empty grader name")
        saved = graders.setdefault(row["grader"], {})
        if row["case_id"] in saved:
            raise ValueError("Duplicate grader/case pair")
        saved[row["case_id"]] = row["prediction"]
    if not graders:
        raise ValueError("No graders supplied")
    results = []
    for name, saved in sorted(graders.items()):
        counts = dict(tp=0, tn=0, fp=0, fn=0, abstained=0, missing=0, invalid=0)
        for case_id, truth in reference.items():
            pred = saved.get(case_id)
            if pred is None:
                counts["missing"] += 1
            elif pred == "ABSTAIN":
                counts["abstained"] += 1
            elif pred not in {"PASS", "FAIL"}:
                counts["invalid"] += 1
            else:
                key = {("PASS", "PASS"): "tp", ("FAIL", "FAIL"): "tn",
                       ("FAIL", "PASS"): "fp", ("PASS", "FAIL"): "fn"}[truth, pred]
                counts[key] += 1
        n_pass = sum(v == "PASS" for v in reference.values())
        n_fail = len(reference) - n_pass
        tp, tn, fp, fn = (counts[k] for k in ("tp", "tn", "fp", "fn"))
        answered = tp + tn + fp + fn
        reviewed = counts["abstained"] + counts["missing"] + counts["invalid"]
        # Unscored cases remain in their reference-class denominator.
        balanced = .5 * (tp / n_pass + tn / n_fail)
        results.append(dict(grader=name, cases=len(reference), reference_pass=n_pass,
            reference_fail=n_fail, **counts, answered=answered,
            coverage=answered / len(reference), accuracy_all=(tp + tn) / len(reference),
            balanced_accuracy_all=balanced, false_pass_rate=fp / n_fail,
            accuracy_answered=(tp + tn) / answered if answered else None,
            review_cases=reviewed,
            # Imposed loss units: false approval 10, false rejection 1,
            # referral .5 with perfect resolution by the human reviewer.
            loss_units=10 * fp + fn + .5 * reviewed))
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--predictions", type=Path, default=HERE / "data/grader_predictions.csv")
    parser.add_argument("--output", type=Path, default=HERE / "results")
    args = parser.parse_args()
    cases = json.loads((HERE / "data/grader_cases.json").read_text())["cases"]
    with args.predictions.open(newline="") as file:
        predictions = list(csv.DictReader(file))
    results = evaluate(cases, predictions)
    args.output.mkdir(parents=True, exist_ok=True)
    with (args.output / "grader_summary.csv").open("w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=list(results[0]))
        writer.writeheader()
        writer.writerows(results)
    (args.output / "grader_summary.json").write_text(json.dumps(results, indent=2) + "\n")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
