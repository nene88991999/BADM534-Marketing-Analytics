"""Evaluate three imposed rating patterns on the same six synthetic concepts.

Reference counts are invented surveys, not human observations. Candidate PMFs are
fixed teaching inputs, not fitted predictions. No model calls or dependencies.
"""
import json
from math import isclose, isfinite, sqrt
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parent


def validate_pmf(pmf):
    if len(pmf) != 5 or any(not isfinite(x) or x < 0 for x in pmf):
        raise ValueError("A PMF needs five finite nonnegative values.")
    if not isclose(sum(pmf), 1, abs_tol=1e-12, rel_tol=0):
        raise ValueError("Category probabilities must sum to one.")
    return pmf


def mean_rating(pmf):
    return sum((k + 1) * x for k, x in enumerate(validate_pmf(pmf)))


def ks_similarity(left, right):
    validate_pmf(left)
    validate_pmf(right)
    x = y = distance = 0.0
    for a, b in zip(left, right):
        x, y = x + a, y + b
        distance = max(distance, abs(x - y))
    return 1 - distance


def correlation(left, right):
    if len(left) != len(right) or len(left) < 2:
        raise ValueError("Use paired concept scores with at least two concepts.")
    if any(not isfinite(x) for x in [*left, *right]):
        raise ValueError("Correlation requires finite scores.")
    x = [v - mean(left) for v in left]
    y = [v - mean(right) for v in right]
    xx, yy = sum(v * v for v in x), sum(v * v for v in y)
    return None if min(xx, yy) <= 1e-24 else sum(a * b for a, b in zip(x, y)) / sqrt(xx * yy)


def ranks(values):
    """Average ranks for exact ties; scores are ordered from smallest to largest."""
    order = sorted(range(len(values)), key=values.__getitem__)
    result = [None] * len(values)
    first = 0
    while first < len(order):
        last = first + 1
        while last < len(order) and values[order[last]] == values[order[first]]:
            last += 1
        for i in order[first:last]:
            result[i] = (first + 1 + last) / 2
        first = last
    return result


def shortlist(scores, count=2):
    if not 0 < count < len(scores) or any(not isfinite(x) for x in scores.values()):
        raise ValueError("Require finite scores and a shortlist smaller than the roster.")
    ordered = sorted(scores, key=lambda key: (-scores[key], key))
    if isclose(scores[ordered[count - 1]], scores[ordered[count]], abs_tol=1e-12, rel_tol=0):
        return None  # A boundary tie supplies no unique shortlist.
    return ordered[:count]


def evaluate(data):
    ids = [row["concept"] for row in data["reference"]]
    if len(set(ids)) != len(ids):
        raise ValueError("Reference concept identifiers must be unique.")
    observed = {}
    for row in data["reference"]:
        counts = row["counts"]
        if len(counts) != 5 or any(type(x) is not int or x < 0 for x in counts) or sum(counts) == 0:
            raise ValueError("Reference counts need five nonnegative integers and a positive total.")
        observed[row["concept"]] = [n / sum(counts) for n in counts]
    reference_means = {key: mean_rating(observed[key]) for key in ids}
    reference_top = shortlist(reference_means)
    if reference_top is None:
        raise ValueError("The reference needs a unique shortlist for this comparison.")
    summary, details = [], []
    for candidate, predictions in data["candidates"].items():
        if set(predictions) != set(ids):
            raise ValueError("Every candidate must cover exactly the same concept roster.")
        predicted_means = {key: mean_rating(predictions[key]) for key in ids}
        selected = shortlist(predicted_means)
        left, right = [reference_means[k] for k in ids], [predicted_means[k] for k in ids]
        similarities = [ks_similarity(observed[k], predictions[k]) for k in ids]
        summary.append(dict(candidate=candidate, concepts=len(ids),
            mean_ks_similarity=mean(similarities), mean_absolute_rating_error=mean(abs(x-y) for x,y in zip(left,right)),
            pearson=correlation(left, right), spearman=correlation(ranks(left), ranks(right)),
            reference_top_two=reference_top, selected=selected,
            selection_status="boundary_tie" if selected is None else "unique",
            top_two_recall=None if selected is None else len(set(selected) & set(reference_top))/2))
        for i, key in enumerate(ids):
            details.append(dict(candidate=candidate, concept=key, reference_mean=left[i],
                predicted_mean=right[i], ks_similarity=similarities[i],
                reference_distribution=observed[key], predicted_distribution=predictions[key]))
    return summary, details


def main():
    data = json.loads((ROOT / "data/concept_panels.json").read_text())
    summary, details = evaluate(data)
    out = ROOT / "results"
    out.mkdir(exist_ok=True)
    for name, value in [("screening_summary.json", summary), ("screening_details.json", details)]:
        (out / name).write_text(json.dumps(value, indent=2, allow_nan=False) + "\n")
    for row in summary:
        print(row["candidate"], row["mean_ks_similarity"], row["pearson"], row["selected"])


if __name__ == "__main__":
    main()
