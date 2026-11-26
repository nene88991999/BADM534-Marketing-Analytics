"""Evaluate original deliberate coding errors on the existing mHealth tasks."""
import csv
import json
import math
from collections import Counter
from datetime import date
from pathlib import Path

from evaluate_submission import grade
from logging_reference import calculate, read_csv

HERE = Path(__file__).resolve().parent
CASES = ["correct", "entry_counts", "inclusive_end", "denominator_30",
         "shifted_users", "omit_zero", "missing_value", "execution_failure"]


def candidate(case, roster, records, start, end):
    if case == "execution_failure":
        raise RuntimeError("Deliberately constructed execution failure")
    if case not in CASES:
        raise ValueError("Unknown constructed case.")
    users = [row["user_id"] for row in roster]
    days = (end - start).days
    seen, counts = {u: set() for u in users}, Counter()
    for row in records:
        d, u = date.fromisoformat(row["date"]), row["user_id"]
        keep = start <= d <= end if case == "inclusive_end" else start <= d < end
        if u in seen and keep:
            seen[u].add(d)
            counts[u] += int(row["entries"])
    values = [counts[u] if case == "entry_counts" else len(seen[u]) for u in users]
    if case == "shifted_users":
        values = values[1:] + values[:1]
    denominator = 30 if case == "denominator_30" else days
    rows = [{"user_id": u, "logged_days": n, "window_days": denominator,
             "logging_rate": n / denominator} for u, n in zip(users, values)]
    if case == "omit_zero":
        rows = [row for row in rows if row["logged_days"] > 0]
    if case == "missing_value":
        del rows[0]["logging_rate"]
    return rows


def complete(rows, expected_ids):
    ids = [r.get("user_id") for r in rows]
    if len(ids) != len(expected_ids) or set(ids) != set(expected_ids):
        return False
    try:
        return all(math.isfinite(float(r[k])) for r in rows
                   for k in ["logged_days", "window_days", "logging_rate"])
    except (KeyError, ValueError, TypeError):
        return False


def assess(case, roster, records, start, end):
    reference, summary = calculate(roster, records, start, end)
    try:
        rows = candidate(case, roster, records, start, end)
    except RuntimeError:
        return {"case": case, "executed": False, "complete": False,
                "total_days_matches": False, "valid": False,
                "classification": "loud_failure", "returned_users": 0,
                "correct_users": 0, "returned_days": None, "mean_returned_rate": None}
    structural = complete(rows, [r["user_id"] for r in reference])
    evaluated = grade(rows, reference)
    total = sum(row["logged_days"] for row in rows)
    rates = [row.get("logging_rate") for row in rows]
    mean = sum(rates) / len(rates) if rates and all(x is not None for x in rates) else None
    return {"case": case, "executed": True, "complete": structural,
            "total_days_matches": total == summary["observed_user_days"],
            "valid": evaluated["valid_output"],
            "classification": "success" if evaluated["valid_output"] else
            ("silent_failure" if structural else "loud_failure"),
            "returned_users": len(rows), "correct_users": evaluated["correct_users"],
            "returned_days": total, "mean_returned_rate": mean}


def main():
    output = HERE / "results"
    output.mkdir(exist_ok=True)
    results = []
    for role in ["development", "evaluation"]:
        folder = HERE / "tasks" / role
        spec = json.loads((folder / "task.json").read_text())
        roster, records = read_csv(folder / "roster.csv"), read_csv(folder / "observed_days.csv")
        for case in CASES:
            result = assess(case, roster, records, date.fromisoformat(spec["start"]),
                            date.fromisoformat(spec["end_exclusive"]))
            results.append({"task": role, **result})
    with (output / "semantic_checks.csv").open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(results[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(results)
    summary = {"scope": "Original deliberate errors on observed mHealth inputs; no LLM performance",
               "cases_per_task": len(CASES), "tasks": 2,
               "incorrect_cases_accepted_by_total_only": sum(
                   r["total_days_matches"] and not r["valid"] for r in results),
               "incomplete_outputs": sum(not r["complete"] for r in results)}
    (output / "semantic_summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps({"summary": summary, "results": results}, indent=2))


if __name__ == "__main__":
    main()
