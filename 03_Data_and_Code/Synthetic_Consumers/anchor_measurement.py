"""Map imposed similarities to ratings while preserving response and persona units.

Inputs are instructor-authored text and synthetic similarities, not LLM measurements.
Python 3.10+; standard library only; no network or model calls.
"""
from collections import defaultdict
import json
from math import isfinite
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parent


def rating_distribution(similarities, tolerance=1e-12):
    """Study setting: subtract minimum, normalize, epsilon=0, temperature=1.

    Return None when the spread is at most tolerance. This explicit abstention
    rule is a course adaptation for an otherwise undefined normalization.
    """
    if len(similarities) != 5 or any(
        not isinstance(x, (int, float)) or not isfinite(x) or not -1 <= x <= 1
        for x in similarities
    ):
        raise ValueError("Five finite cosine similarities in [-1, 1] are required.")
    if not isfinite(tolerance) or tolerance < 0:
        raise ValueError("Tolerance must be finite and nonnegative.")
    smallest = min(similarities)
    if max(similarities) - smallest <= tolerance:
        return None
    weights = [x - smallest for x in similarities]
    return [x / sum(weights) for x in weights]


def average_distributions(distributions):
    """A missing mapping leaves the aggregate incomplete, with no silent exclusion."""
    if not distributions or any(row is None for row in distributions):
        return None
    return [mean(row[k] for row in distributions) for k in range(5)]


def mean_rating(distribution):
    return None if distribution is None else sum(
        (k + 1) * p for k, p in enumerate(distribution)
    )


def score_responses(data):
    concepts, personas = set(data["concepts"]), set(data["personas"])
    anchors = set(data["anchor_sets"])
    if len(anchors) != 2 or any(len(s) != 5 for s in data["anchor_sets"].values()):
        raise ValueError("This example has two complete five-category anchor sets.")
    records, seen, covered = [], set(), set()
    for row in data["responses"]:
        key = (row["concept"], row["persona"], row["repeat"])
        if key in seen or key[0] not in concepts or key[1] not in personas:
            raise ValueError("Duplicate response key or unknown concept/persona.")
        if set(row["similarities"]) != anchors or not row["text"].strip():
            raise ValueError("Each response needs text and both anchor comparisons.")
        seen.add(key)
        covered.add(key[:2])
        distributions = {a: rating_distribution(row["similarities"][a])
                         for a in sorted(anchors)}
        distributions["average_sets"] = average_distributions(list(distributions.values()))
        for anchor, distribution in distributions.items():
            records.append(dict(concept=key[0], persona=key[1], repeat=key[2],
                                anchor_set=anchor, distribution=distribution,
                                mean_rating=mean_rating(distribution),
                                status="scored" if distribution is not None else "uninformative"))
    if covered != {(c, p) for c in concepts for p in personas}:
        raise ValueError("Every declared concept/persona pair needs a response.")
    return records


def summarize(records):
    grouped = defaultdict(list)
    for row in records:
        grouped[row["concept"], row["anchor_set"]].append(row)
    summaries = []
    for (concept, anchor), group in sorted(grouped.items()):
        by_persona = defaultdict(list)
        for row in group:
            by_persona[row["persona"]].append(row["distribution"])
        # Average repeats within persona, then give each persona equal weight.
        persona_pmfs = [average_distributions(rows) for rows in by_persona.values()]
        balanced = average_distributions(persona_pmfs)
        row_weighted = average_distributions([row["distribution"] for row in group])
        summaries.append(dict(concept=concept, anchor_set=anchor,
            response_rows=len(group), scored_rows=sum(r["status"] == "scored" for r in group),
            personas=len(by_persona), distribution=balanced,
            mean_rating=mean_rating(balanced),
            top_two_share=None if balanced is None else sum(balanced[3:]),
            row_weighted_mean=mean_rating(row_weighted),
            status="complete" if balanced is not None else "incomplete"))
    return summaries


def main():
    data = json.loads((ROOT / "data/anchor_responses.json").read_text())
    records = score_responses(data)
    summaries = summarize(records)
    out = ROOT / "results"
    out.mkdir(exist_ok=True)
    for name, value in [("response_ratings.json", records), ("concept_ratings.json", summaries)]:
        (out / name).write_text(json.dumps(value, indent=2, allow_nan=False) + "\n")
    for row in summaries:
        print(row["concept"], row["anchor_set"], row["mean_rating"], row["status"])


if __name__ == "__main__":
    main()
