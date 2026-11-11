"""Score hand-annotated synthetic answers; no model calls or automatic fact checking."""
from pathlib import Path
import csv
import json

HERE = Path(__file__).resolve().parent


def assess(data):
    sources = {row["id"] for row in data["sources"]}
    questions = {row["id"] for row in data["questions"]}
    if len(sources) != len(data["sources"]) or len(questions) != len(data["questions"]):
        raise ValueError("Source and question IDs must be unique")
    rows, summaries = [], []
    for condition, answers in data["answers"].items():
        if len(answers) != len(questions) or {a["question_id"] for a in answers} != questions:
            raise ValueError("Every condition must answer the same questions exactly once")
        available = set(data["conditions"][condition])
        if not available <= sources:
            raise ValueError("Unknown source in a condition")
        for answer in answers:
            cited = answer["citations"]
            if not set(cited) <= available:
                raise ValueError("Citation is absent from the supplied context")
            if type(answer["supported"]) is not bool:
                raise ValueError("Each claim needs an explicit reference annotation")
            rows.append(dict(condition=condition, question_id=answer["question_id"],
                cited=int(bool(cited)), supported=int(answer["supported"]),
                citations=";".join(cited), answer=answer["answer"], reason=answer["reason"]))
        sample = [r for r in rows if r["condition"] == condition]
        summaries.append(dict(condition=condition, answers=len(sample),
            cited=sum(r["cited"] for r in sample),
            supported=sum(r["supported"] for r in sample)))
    return rows, summaries


def main():
    data = json.loads((HERE / "data/source_cases.json").read_text())
    rows, summaries = assess(data)
    output = HERE / "results"
    output.mkdir(exist_ok=True)
    for name, records in [("source_claims.csv", rows), ("source_summary.csv", summaries)]:
        with (output / name).open("w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=list(records[0]))
            writer.writeheader()
            writer.writerows(records)
    print(json.dumps(dict(scope=data["scope"], summaries=summaries), indent=2))


if __name__ == "__main__":
    main()
