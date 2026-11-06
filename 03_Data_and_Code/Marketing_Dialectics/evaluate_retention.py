"""Compare two constructed customer populations with identical billed renewal.

Python 3.10+; standard library only. No network calls or real customer records.
Run: python3 03_Data_and_Code/Marketing_Dialectics/evaluate_retention.py
"""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def construct_customers():
    # Each tuple is (billed this month, wanted renewal before billing, count).
    # Counts are imposed teaching inputs, not estimated responses to a policy.
    cells = {
        "A": [(True, True, 880), (True, False, 20),
              (False, True, 20), (False, False, 80)],
        "B": [(True, True, 600), (True, False, 300),
              (False, True, 20), (False, False, 80)],
    }
    rows = []
    for population, groups in cells.items():
        number = 0
        for billed, wanted, count in groups:
            for _ in range(count):
                number += 1
                rows.append({"population": population,
                             "customer_id": f"{population}{number:04d}",
                             "billed": billed, "wanted_renewal": wanted})
    return rows


def summarize(rows):
    if not rows:
        raise ValueError("The population must contain customers.")
    keys = [(r["population"], r["customer_id"]) for r in rows]
    if len(set(keys)) != len(keys):
        raise ValueError("Duplicate customer within population.")
    if len({r["population"] for r in rows}) != 1:
        raise ValueError("Summarize one population at a time.")
    for r in rows:
        if type(r["billed"]) is not bool:
            raise ValueError("Billing must be observed as True or False.")
        if r["wanted_renewal"] is not None and type(r["wanted_renewal"]) is not bool:
            raise ValueError("Intent must be True, False, or None.")
    n = len(rows)
    billed = sum(r["billed"] for r in rows)
    wanted_billed = sum(r["billed"] and r["wanted_renewal"] is True for r in rows)
    unwanted_billed = sum(r["billed"] and r["wanted_renewal"] is False for r in rows)
    unknown_billed = sum(r["billed"] and r["wanted_renewal"] is None for r in rows)
    missed_wanted = sum(not r["billed"] and r["wanted_renewal"] is True for r in rows)
    assert wanted_billed + unwanted_billed + unknown_billed == billed
    return {
        "customers": n, "billed": billed, "billed_rate": billed / n,
        "wanted_billed": wanted_billed, "unwanted_billed": unwanted_billed,
        "unknown_intent_billed": unknown_billed,
        "wanted_but_not_billed": missed_wanted,
        "unwanted_billed_lower_share_all": unwanted_billed / n,
        "unwanted_billed_upper_share_all": (unwanted_billed + unknown_billed) / n,
        "unwanted_share_among_billed_lower": unwanted_billed / billed if billed else None,
    }


def main():
    rows = construct_customers()
    with (ROOT / "synthetic_customer_months.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    results = {p: summarize([r for r in rows if r["population"] == p])
               for p in sorted({r["population"] for r in rows})}
    output = {
        "data_type": "Entirely synthetic; two constructed populations",
        "unit": "One customer over one renewal month",
        "intent_timing": "Before billing; stipulated independently of billing",
        "comparison": "Descriptive identification example, not a policy effect",
        "results": results,
    }
    (ROOT / "results.json").write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
