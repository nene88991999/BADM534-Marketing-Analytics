"""Construct two views of six synthetic subscription accounts.

Run from any directory with Python 3.10 or later. Standard library only.
Outputs are written beside this script in artifact_results/.
"""
import csv
import hashlib
import io
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent / "artifact_results"
OUT.mkdir(exist_ok=True)
AS_OF = "2027-02-01T00:00:00Z"
ACCOUNTS = tuple("ABCDEF")
# All six accounts were subscribed at the start of January.
# These are explicit submitted requests, not inferred dissatisfaction.
REQUESTS = [
    {"account": "B", "requested": "2027-01-05T09:00:00Z",
     "completed": "2027-01-05T09:01:00Z"},
    {"account": "C", "requested": "2027-01-06T09:00:00Z",
     "completed": ""},
    {"account": "D", "requested": "2027-01-07T09:00:00Z",
     "completed": ""},
    {"account": "E", "requested": "2027-01-08T09:00:00Z",
     "completed": ""},
]
assert len(set(ACCOUNTS)) == len(ACCOUNTS) == 6
assert len({r["account"] for r in REQUESTS}) == len(REQUESTS)
assert all(r["account"] in ACCOUNTS for r in REQUESTS)
assert all(r["requested"] < AS_OF for r in REQUESTS)
assert all(not r["completed"] or
           r["requested"] <= r["completed"] < AS_OF for r in REQUESTS)

by_account = {r["account"]: r for r in REQUESTS}
retention_rows = []
assessment_rows = []
for account in ACCOUNTS:
    request = by_account.get(account)
    completed = bool(request and request["completed"])
    retained = int(not completed)
    retention_rows.append({"account": account, "retained": retained})
    assessment_rows.append({
        "account": account,
        "retained": retained,
        "request_submitted": int(request is not None),
        "request_completed": int(completed),
    })

def csv_text(rows, fields):
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue()

def write_text(name, value):
    path = OUT / name
    path.write_text(value, encoding="utf-8", newline="")
    return hashlib.sha256(path.read_bytes()).hexdigest()

# V1 and V2 are different releases: V2 adds request information.
v1 = csv_text(retention_rows, ["account", "retained"])
v2 = csv_text(assessment_rows, list(assessment_rows[0]))
# Same V2 records and schema, with only row order changed.
v2_reordered = csv_text(list(reversed(assessment_rows)),
                        list(assessment_rows[0]))
hashes = {
    "retention_v1.csv": write_text("retention_v1.csv", v1),
    "assessment_v2.csv": write_text("assessment_v2.csv", v2),
    "assessment_v2_reordered.csv": write_text(
        "assessment_v2_reordered.csv", v2_reordered),
}

def keyed_records(text):
    rows = list(csv.DictReader(io.StringIO(text)))
    assert len({r["account"] for r in rows}) == len(rows)
    return {r["account"]: r for r in rows}

assert hashes["assessment_v2.csv"] != hashes["assessment_v2_reordered.csv"]
assert keyed_records(v2) == keyed_records(v2_reordered)
assert [{"account": r["account"], "retained": r["retained"]}
        for r in assessment_rows] == retention_rows

retained_count = sum(r["retained"] for r in retention_rows)
request_count = sum(r["request_submitted"] for r in assessment_rows)
completion_count = sum(r["request_completed"] for r in assessment_rows)
pending_count = request_count - completion_count
summary = {
    "synthetic": True, "as_of_utc": AS_OF,
    "initial_accounts": len(ACCOUNTS), "retained_accounts": retained_count,
    "submitted_requests": request_count, "completed_requests": completion_count,
    "pending_requests": pending_count,
    "retention_fraction": retained_count / len(ACCOUNTS),
    "pending_fraction_among_requests": pending_count / request_count,
    "pending_fraction_among_retained": pending_count / retained_count,
}
assert (retained_count, request_count, completion_count, pending_count) == (5, 4, 1, 3)
manifest = {
    "dataset": "Synthetic Subscription Records",
    "synthetic": True, "as_of_utc": AS_OF,
    "population": "Six accounts subscribed at the start of January 2027",
    "unit": "Account at the cutoff; one request at most per account",
    "v1_purpose": "Describe subscription status at the cutoff",
    "v2_purpose": "Also assess completion of submitted cancellation requests",
    "retained_definition": "No completed cancellation before the cutoff",
    "identity_rule": "Same schema and values by unique account; ignore row order",
    "v2_parent": "V1 plus the synthetic request history defined in the program",
    "files_sha256": hashes,
    "interpretation": "Counts describe status and request completion. They do not measure consent, satisfaction, or causal effects.",
}
write_text("summary.json", json.dumps(summary, indent=2) + "\n")
write_text("manifest.json", json.dumps(manifest, indent=2) + "\n")
print(json.dumps(summary, indent=2))
