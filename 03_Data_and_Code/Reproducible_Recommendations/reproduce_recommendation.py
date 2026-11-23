"""Recompute a synthetic recommendation and retain its numerical evidence.

Python 3.10+, standard library. No network, model, or editor calls.
The two input constructions are separate; all personas and panels are invented.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parent / "Synthetic_Consumers"
sys.path.insert(0, str(SOURCE))
from anchor_measurement import score_responses, summarize
from concept_screening import evaluate


def load(path):
    return json.loads(path.read_text())


def calculate(source=SOURCE):
    records = score_responses(load(source / "data/anchor_responses.json"))
    concepts = summarize(records)
    screening, details = evaluate(load(source / "data/concept_panels.json"))
    computed = dict(response_ratings=records, concept_ratings=concepts,
                    screening_summary=screening, screening_details=details)
    for name, value in computed.items():
        if load(source / f"results/{name}.json") != value:
            raise ValueError(f"Saved {name} disagrees with a fresh calculation.")
    refill = next(r for r in concepts
                  if r["concept"] == "refill" and r["anchor_set"] == "set_1")
    first = next(r for r in records if r["concept"] == "refill"
                 and r["persona"] == "p01" and r["repeat"] == 1
                 and r["anchor_set"] == "set_1")
    second = next(r for r in records if r["concept"] == "refill"
                  and r["persona"] == "p02" and r["anchor_set"] == "set_1")
    # Hold each persona's rating fixed and vary p01's identical repeat count.
    sensitivity = [dict(p01_repeats=n, p02_repeats=1,
        equal_persona_mean=(first["mean_rating"] + second["mean_rating"]) / 2,
        equal_row_mean=(n * first["mean_rating"] + second["mean_rating"]) / (n + 1))
        for n in range(1, 6)]
    tracked = [source / "data/anchor_responses.json",
               source / "data/concept_panels.json",
               SOURCE / "anchor_measurement.py", SOURCE / "concept_screening.py",
               ROOT / "reproduce_recommendation.py"]
    return dict(scope="Entirely synthetic; no model or customer observations",
        response_mean=first["mean_rating"], response_distribution=first["distribution"],
        equal_persona_mean=refill["mean_rating"],
        equal_row_mean=refill["row_weighted_mean"],
        response_rows=refill["response_rows"], personas=refill["personas"],
        repeat_sensitivity=sensitivity, screening=screening,
        sha256={p.parent.name + "/" + p.name:
                hashlib.sha256(p.read_bytes()).hexdigest() for p in tracked})


def write_report(result, output):
    output.mkdir(parents=True, exist_ok=True)
    (output / "evidence.json").write_text(
        json.dumps(result, indent=2, allow_nan=False) + "\n")
    link = lambda path: Path(os.path.relpath(path, output)).as_posix()
    rows = {r["candidate"]: r for r in result["screening"]}
    selected = lambda row: ("unresolved" if row["selected"] is None
                            else ", ".join(row["selected"]))
    pooled, reversed_row = rows["pooled"], rows["reversed"]
    correlation = ("undefined" if pooled["pearson"] is None
                   else f"{pooled['pearson']:.3f}")
    recall = ("undefined" if reversed_row["top_two_recall"] is None
              else f"{reversed_row['top_two_recall']:.0%}")
    lines = ["# Product-Screening Recommendation", "", "By Nathan Yang", "",
        "A product manager must decide which concepts warrant human research. "
        "All inputs below are invented. No model calls or customer study took place.", "",
        "## Response Weights", "",
        f"The refill example has {result['response_rows']} response rows from "
        f"{result['personas']} personas. Equal persona weights give "
        f"{result['equal_persona_mean']:.3f}; equal row weights give "
        f"{result['equal_row_mean']:.6f} on a five-category rating scale.", "",
        "Persona p01's first response has the following imposed category weights.", "",
        "| Rating | Weight |", "| --- | --- |"]
    lines += [f"| {k} | {p:.2f} |"
              for k, p in enumerate(result["response_distribution"], 1)]
    lines += ["", rf"The expected rating is $\sum_{{k=1}}^{{5}}k p_k={result['response_mean']:.2f}$.", "",
        "![Identical repeats raise the row mean while the persona mean stays fixed]("
        + link(ROOT.parents[1] / "06_Lecture_Notes/figures/M01_repeat_weights.png") + ")", "",
        "## Concept Selection", "",
        f"A separate construction compares {pooled['concepts']} invented concepts "
        "with an invented reference panel. The pooled pattern's shortlist is "
        f"{selected(pooled)} and its correlation is {correlation}. "
        f"The reversed pattern selects {selected(reversed_row)}. Its recall of "
        f"the reference top two ({', '.join(reversed_row['reference_top_two'])}) "
        f"is {recall}.", "",
        "These patterns use reference outcomes in their construction. Their results "
        "justify checking ranking errors before funding a human study. They supply "
        "no evidence of actual purchase demand or out-of-sample performance.", "",
        "An assumed research budget of \\$500 and an assumed incentive of \\$25 "
        "per participant allow 20 incentives before recruitment and operating costs. "
        "This arithmetic does not determine an adequate study size.", "",
        "## Reproduction", "",
        "[Numerical evidence](evidence.json) | [Full Python]("
        + link(ROOT / "reproduce_recommendation.py") + ") | [Data dictionary]("
        + link(SOURCE / "DATA_DICTIONARY.md") + ")", "",
        "[Response inputs](" + link(SOURCE / "data/anchor_responses.json")
        + ") | [Concept inputs](" + link(SOURCE / "data/concept_panels.json") + ")", "",
        "From the course root: `python3 "
        "03_Data_and_Code/Reproducible_Recommendations/reproduce_recommendation.py`.", ""]
    (output / "recommendation.md").write_text("\n".join(lines))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "results")
    args = parser.parse_args()
    write_report(calculate(), args.output.resolve())
    print("Recomputed four saved tables and wrote evidence.json and recommendation.md.")
