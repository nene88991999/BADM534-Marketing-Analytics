"""Calculate observed logging days for a fixed earlier-period roster."""
import csv
import json
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent


def read_csv(path):
    with path.open(newline="") as stream:
        return list(csv.DictReader(stream))


def calculate(roster, records, start, end):
    users = [row["user_id"] for row in roster]
    if not users or len(users) != len(set(users)):
        raise ValueError("The roster must be nonempty with one row per user.")
    days = (end - start).days
    if days <= 0:
        raise ValueError("The end must follow the start.")
    observed = {u: set() for u in users}
    excluded_rows = 0
    for row in records:
        d = date.fromisoformat(row["date"])
        if row["user_id"] not in observed or not start <= d < end:
            excluded_rows += 1
            continue
        # Multiple entries and repeated rows still represent one logged day.
        observed[row["user_id"]].add(d)
    rows = [{"user_id": u, "logged_days": len(observed[u]), "window_days": days,
             "logging_rate": len(observed[u]) / days} for u in users]
    total = sum(r["logged_days"] for r in rows)
    summary = {"roster_users": len(users), "window_days": days,
               "observed_user_days": total, "possible_user_days": len(users) * days,
               "zero_log_users": sum(r["logged_days"] == 0 for r in rows),
               "mean_logging_rate": total / (len(users) * days),
               "excluded_input_rows": excluded_rows}
    return rows, summary


def main():
    output = HERE / "results"
    output.mkdir(exist_ok=True)
    summaries = {}
    for role in ["development", "evaluation"]:
        task = HERE / "tasks" / role
        spec = json.loads((task / "task.json").read_text())
        rows, summary = calculate(read_csv(task / "roster.csv"),
                                  read_csv(task / "observed_days.csv"),
                                  date.fromisoformat(spec["start"]),
                                  date.fromisoformat(spec["end_exclusive"]))
        with (output / f"{role}_reference.csv").open("w", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)
        summaries[role] = summary
    (output / "logging_summary.json").write_text(json.dumps(summaries, indent=2) + "\n")
    print(json.dumps(summaries, indent=2))


if __name__ == "__main__":
    main()
