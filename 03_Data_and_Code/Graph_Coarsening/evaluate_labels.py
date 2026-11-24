"""Synthetic label diagnostics: oracle purity, permitted fitting, and outcome use.

This computes small examples with the standard library; it does not call GraCo.
The parameter example uses a separate information split from the purity example.
"""
from collections import Counter
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


def majority(labels):
    counts = Counter(labels)
    if not counts:
        raise ValueError("A group needs labeled training observations or a fallback.")
    return min(counts, key=lambda label: (-counts[label], label))


def score(label, outcomes, indices):
    return sum(outcomes[i] == label for i in indices) / len(indices)


def disagreement(outcomes, edges):
    return sum(outcomes[i] != outcomes[j] for i, j in edges) / len(edges)


def calculate(case):
    y = case["outcomes"]
    train, test = case["train_indices"], case["test_indices"]
    assert not set(train) & set(test)
    oracle = majority(y)
    fitted = majority([y[i] for i in train])
    alternative = case["alternative_test_indices"]
    subset_best = majority([y[i] for i in alternative])
    groups = case["minority_groups"]
    outcomes = [label for group in groups for label in group]
    prediction = [majority(group) for group in groups for _ in group]
    positives = sum(label == 1 for label in outcomes)
    correct = sum(a == b for a, b in zip(outcomes, prediction))
    true_positive = sum(a == b == 1 for a, b in zip(outcomes, prediction))
    before, after = case["parameter_labels_before"], case["parameter_labels_after"]
    permitted = case["parameter_training_indices"]
    heldout = case["parameter_heldout_indices"]
    assert not set(permitted) & set(heldout)
    assert [before[i] for i in permitted] == [after[i] for i in permitted]
    assert all(before[i] == after[i] for i in range(len(before)) if i not in heldout)
    edges = case["parameter_edges"]
    training_edges = [(i, j) for i, j in edges if i in permitted and j in permitted]
    return dict(
        synthetic=True,
        purity=dict(outcomes=y, train_indices=train, test_indices=test,
                    full_group_majority=oracle, fitted_training_majority=fitted,
                    full_group_purity=score(oracle, y, list(range(len(y)))),
                    global_majority_test_score=score(oracle, y, test),
                    training_only_test_score=score(fitted, y, test),
                    test_count=len(test), alternative_subset_count=len(alternative),
                    alternative_global_score=score(oracle, y, alternative),
                    alternative_own_ceiling=score(subset_best, y, alternative)),
        minority=dict(people=len(outcomes), class_one_people=positives,
                      correct=correct, true_positive=true_positive,
                      accuracy=correct / len(outcomes), recall=true_positive / positives),
        parameter=dict(training_indices=permitted, heldout_indices=heldout,
                       all_edges_before=disagreement(before, edges),
                       all_edges_after=disagreement(after, edges),
                       training_edges_before=disagreement(before, training_edges),
                       training_edges_after=disagreement(after, training_edges)))


def main():
    case = json.loads((HERE / "data/cases.json").read_text())["labels"]
    result = calculate(case)
    output = HERE / "results"
    output.mkdir(exist_ok=True)
    (output / "labels.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
