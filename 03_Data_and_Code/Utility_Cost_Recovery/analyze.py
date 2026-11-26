"""Reproduce coverage, a qualitative comparison matrix, and bill arithmetic."""
import csv
import json
from collections import Counter
from decimal import Decimal
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGES = {"forecast", "request", "proposal", "accounting_mechanism",
          "approved_price_illustration", "regulator_explanation"}
DIRECTIONS = {"increase", "offset", "mechanism", "mixed", "unclear"}


def load_inputs():
    sources = json.loads((HERE / "sources.json").read_text())
    claims = json.loads((HERE / "data/claims.json").read_text())
    retrieval = json.loads((HERE / "data/retrieval_snapshot.json").read_text())
    for rows, key in [(sources, "id"), (claims, "claim_id"), (retrieval, "source_id")]:
        if len({x[key] for x in rows}) != len(rows):
            raise ValueError("Duplicate key: " + key)
    index = {s["id"]: s for s in sources}
    if set(index) != {r["source_id"] for r in retrieval}:
        raise ValueError("Retrieval roster must retain all selected sources")
    for row in claims:
        if row["source_id"] not in index or row["stage"] not in STAGES:
            raise ValueError("Unknown source or evidence stage")
        if row["direction"] not in DIRECTIONS:
            raise ValueError("Unknown direction")
        if not all(row[k] for k in ["locator", "population", "counterevidence",
                                    "interpretation_limit", "annotation_status"]):
            raise ValueError("An interpretation requires context and qualifications")
    return index, claims, retrieval


def coverage(sources, retrieval):
    rows = []
    for record in retrieval:
        spec = sources[record["source_id"]]
        observed = record["status"] == "ok"
        rows.append({"source_id": spec["id"], "kind": spec["kind"],
                     "observed": observed,
                     "words": record.get("words") if observed else None,
                     "recovery_matches": record.get("recovery") if observed else None})
    return rows


def comparison_matrix(sources, claims):
    # A claim is the coding unit. Related documents remain within an issuer family.
    rows = []
    for row in claims:
        spec = sources[row["source_id"]]
        rows.append({"issuer_family": spec["issuer"], "date": spec["date"],
                     **row, "source_url": spec.get("primary_url", spec["url"])})
    return rows


def bill_calculations():
    before, after = Decimal("155.84"), Decimal("182.71")
    change = after - before
    return [
        {"case": "NJBPU_PSEG", "monthly_kwh": 650,
         "monthly_change_usd": str(change),
         "percent_change": str((100 * change / before).quantize(Decimal("0.01"))),
         "annualized_change_usd": str(12 * change),
         "status": "Fixed-use illustration of announced auction prices; excludes later adjustments"},
        {"case": "Evergy_Missouri_West", "monthly_kwh": 1005,
         "monthly_change_usd": "17.25", "percent_change": None,
         "annualized_change_usd": str(12 * Decimal("17.25")),
         "status": "Proposed bill change if approved and held for 12 equal-use months"},
    ]


def write_csv(path, rows):
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main():
    sources, claims, retrieval = load_inputs()
    out = HERE / "results"
    out.mkdir(exist_ok=True)
    write_csv(out / "coverage.csv", coverage(sources, retrieval))
    write_csv(out / "evidence_matrix.csv", comparison_matrix(sources, claims))
    write_csv(out / "bill_illustrations.csv", bill_calculations())
    observed = [r for r in retrieval if r["status"] == "ok"]
    result = {"selected_documents": len(sources),
              "downloaded_documents": len(observed),
              "selected_calls": sum(s["kind"] == "earnings_call" for s in sources.values()),
              "claims": len(claims),
              "issuer_families": len({s["issuer"] for s in sources.values()}),
              "coded_stages": dict(sorted(Counter(c["stage"] for c in claims).items())),
              "coded_directions": dict(sorted(Counter(c["direction"] for c in claims).items())),
              "interpretation": "Counts describe purposeful teaching selections, not population prevalence.",
              "independent_human_coders": 0, "causal_effect_estimates": 0}
    (out / "summary.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
