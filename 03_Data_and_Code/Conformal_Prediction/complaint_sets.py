"""Constructed complaint probabilities and sets for a review-routing decision."""
from pathlib import Path
from fractions import Fraction as F
import json
from conformal import label_set, threshold

HERE = Path(__file__).resolve().parent
LABELS = ("billing", "delivery", "product")

def make_calibration():
    scores = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50,
              52, 54, 56, 58, 60, 62, 64, 65, 80]
    rows = []
    for i, score in enumerate(scores):
        true_label = LABELS[i % len(LABELS)]
        probabilities = {label: str(1 - F(score, 100)) if label == true_label
                         else str(F(score, 200)) for label in LABELS}
        label_set(probabilities, 1)  # Validate the probability vector.
        rows.append(dict(case_id=f"cal_{i:02d}", true_label=true_label,
                         probabilities=probabilities))
    return rows

def main():
    calibration = make_calibration()
    scores = [1 - F(r["probabilities"][r["true_label"]]) for r in calibration]
    q = threshold(scores, "0.10")
    queries = [dict(zip(LABELS, p)) for p in
               [("0.70", "0.20", "0.10"),
                ("0.45", "0.40", "0.15"),
                ("0.34", "0.33", "0.33")]]
    decisions = []
    for i, probabilities in enumerate(queries):
        selected = label_set(probabilities, q)
        action = "routing_candidate" if len(selected) == 1 else "human_review"
        decisions.append(dict(case_id=f"query_{i+1}", probabilities=probabilities,
                              labels=selected, set_size=len(selected), action=action))
    output = HERE / "results"
    output.mkdir(exist_ok=True)
    result = dict(alpha=0.10, calibration_cases=len(calibration), cutoff=q,
        minimum_probability=float(1 - F(str(q))), calibration=calibration,
        queries=decisions, scope="Synthetic scores and three unlabeled queries. "
        "No test accuracy or empirical coverage is measured. "
        "Set coverage alone does not control singleton-routing error.")
    (output / "complaint_sets.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "calibration"}, indent=2))

if __name__ == "__main__":
    main()
