"""Grade a CSV without executing submitted code or making model calls."""
import argparse
import csv
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent


def grade(candidate, reference):
    expected = {r["user_id"]: r for r in reference}
    found, errors = {}, []
    for row in candidate:
        user = row.get("user_id", "")
        if user in found:
            errors.append(f"duplicate user: {user}")
        found[user] = row
    missing, extra = sorted(set(expected) - set(found)), sorted(set(found) - set(expected))
    correct = 0
    for user in sorted(set(expected) & set(found)):
        try:
            actual = [float(found[user][k]) for k in ["logged_days", "window_days", "logging_rate"]]
            target = [float(expected[user][k]) for k in ["logged_days", "window_days", "logging_rate"]]
            ok = all(math.isfinite(a) and math.isclose(a, b, rel_tol=0, abs_tol=1e-10)
                     for a, b in zip(actual, target))
            correct += ok
        except (KeyError, ValueError, TypeError):
            errors.append(f"invalid values: {user}")
    valid = not missing and not extra and not errors and correct == len(expected)
    return {"valid_output": valid, "correct_users": correct, "roster_users": len(expected),
            "missing_users": missing, "extra_users": extra, "format_errors": errors}


def read_rows(path):
    with path.open(newline="") as stream:
        return list(csv.DictReader(stream))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("candidate", type=Path)
    parser.add_argument("--task", choices=["development", "evaluation"], default="development")
    args = parser.parse_args()
    reference = read_rows(HERE / "results" / f"{args.task}_reference.csv")
    try:
        candidate = read_rows(args.candidate)
        result = grade(candidate, reference)
    except (OSError, UnicodeError, csv.Error) as exc:
        result = {"valid_output": False, "failure": type(exc).__name__, "roster_users": len(reference)}
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["valid_output"] else 1)


if __name__ == "__main__":
    main()
