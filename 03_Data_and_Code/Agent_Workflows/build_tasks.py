"""Construct small, reproducible tasks from the released mHealth food file."""
import csv
import gzip
import hashlib
import json
from collections import Counter
from datetime import date, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / "mHealth"


def digest(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def write_csv(path, fields, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main():
    source = SOURCE / "data/food_entries.csv.gz"
    release = json.loads((SOURCE / "manifest.json").read_text())
    expected = release["files"][source.name]["sha256"]
    if digest(source) != expected:
        raise ValueError("The mHealth release checksum differs.")
    prior_users, counts = set(), Counter()
    with gzip.open(source, "rt", newline="") as stream:
        for row in csv.DictReader(stream):
            user = row["Userid"]
            if int(user[1:5], 16) >= 4096:
                continue
            day = date.fromisoformat(row["Fancydate"][:10])
            if date(2016, 1, 1) <= day < date(2016, 7, 1):
                prior_users.add(user)
            if date(2016, 6, 30) <= day <= date(2016, 9, 1):
                counts[user, day] += 1
    # Eligibility is fixed using January-June records for both later tasks.
    aliases = {u: f"U{i:04d}" for i, u in enumerate(sorted(prior_users), 1)}
    tasks = []
    for month, role in [(7, "development"), (8, "evaluation")]:
        start, end = date(2016, month, 1), date(2016, month + 1, 1)
        task = HERE / "tasks" / role
        spec = {"task_id": role, "start": str(start), "end_exclusive": str(end),
                "eligibility_cutoff_exclusive": "2016-07-01"}
        write_csv(task / "roster.csv", ["user_id"],
                  ({"user_id": u} for u in aliases.values()))
        records = [{"user_id": aliases[u], "date": str(d), "entries": n}
                   for (u, d), n in sorted(counts.items())
                   if u in aliases and start - timedelta(days=1) <= d <= end]
        write_csv(task / "observed_days.csv", ["user_id", "date", "entries"], records)
        (task / "task.json").write_text(json.dumps(spec, indent=2) + "\n")
        tasks.append({**spec, "roster_users": len(aliases), "input_rows": len(records)})
    inputs = sorted((HERE / "tasks").glob("*/*"))
    manifest = {"source": "mHealth teaching release 2026-10-23",
                "source_sha256": expected, "selection": "Pseudonym prefix below 4096; observed January-June 2016",
                "unit": "Observed user-day; entries counts source food rows",
                "tasks": tasks, "model_calls": 0,
                "files": {str(p.relative_to(HERE)): digest(p) for p in inputs}}
    (HERE / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps(tasks, indent=2))


if __name__ == "__main__":
    main()
