"""Compare record validation with support for eight constructed claims.

Uses a published-table reconstruction already included in the course.
The claims, human approval, decisions, and reference judgments are authored
teaching cases. No model calls or upstream repository code are used.
"""
from pathlib import Path
from statistics import NormalDist
import argparse
import csv
import hashlib
import json
import math
import re
import tempfile

HERE = Path(__file__).resolve().parent
INPUT = HERE.parent / "Statistical_Inference/results/data_center_estimates.csv"
TARGET = "utility_average_residential_price"
UNITS = "USD/MWh at reference exposure"


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def reconstruct(path=INPUT):
    with Path(path).open(newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream))
    selected = [row for row in rows if row["case"] == "residential_reference"]
    if len(selected) != 1:
        raise ValueError("Expected one residential-reference row")
    row = selected[0]
    b, se = float(row["reported_coefficient"]), float(row["reported_se"])
    scale = float(row["scale"])
    if not all(math.isfinite(x) for x in (b, se, scale)) or se <= 0 or scale <= 0:
        raise ValueError("Finite coefficient and positive SE and scale required")
    if row["units"] != UNITS:
        raise ValueError("Unexpected units")
    normal = NormalDist()
    estimate, uncertainty = b * scale, se * scale
    values = {
        "estimate": estimate,
        "se": uncertainty,
        "p_zero": 2 * normal.cdf(-abs(b / se)),
        "ci95_low": estimate - normal.inv_cdf(.975) * uncertainty,
        "ci95_high": estimate + normal.inv_cdf(.975) * uncertainty,
        "upper95": estimate + normal.inv_cdf(.95) * uncertainty,
    }
    for key, value in values.items():
        if not math.isclose(value, float(row[key]), rel_tol=1e-10, abs_tol=1e-12):
            raise ValueError("Reconstruction disagrees with saved " + key)
    return {"source": row["source"], "reported_coefficient": b,
            "reported_se": se, "scale": scale, "target": TARGET,
            "units": UNITS, "normal_approximation": True, **values}


def make_claims(values):
    # Reference judgments concern these complete records and their wording.
    # They are disclosed teaching labels, never inputs to either checker.
    specifications = [
        ("estimate", "estimate", values["estimate"], TARGET, ["table"], True,
         "The scaled estimate is about 1.75 USD/MWh at reference exposure."),
        ("nonrejection", "p_zero", values["p_zero"], TARGET, ["table"], True,
         "The two-sided normal test does not reject zero at five percent."),
        ("upper-bound", "upper95", values["upper95"], TARGET, ["table"], True,
         "The one-sided 95 percent normal upper bound is about 3.49 USD/MWh."),
        ("household-assurance", "no_harm", 0.0, "household_bill", ["table"], False,
         "The evidence demonstrates that data centers do not harm households."),
        ("approved-assurance", "no_harm", 0.0, "household_bill",
         ["table", "manager-approval"], False,
         "Manager approval establishes that households suffer no harm."),
        ("missing-source", "estimate", values["estimate"], TARGET,
         ["absent-table"], False,
         "The scaled estimate is about 1.75 USD/MWh at reference exposure."),
        ("wrong-number", "estimate", 0.0, TARGET, ["table"], False,
         "The estimated utility price effect equals zero."),
        ("mismatched-text", "p_zero", values["p_zero"], TARGET, ["table"], False,
         "The insignificant result proves that households suffer no harm."),
    ]
    return [{"id": key, "quantity": quantity, "value": value, "target": target,
             "sources": sources, "reference_acceptable": reference,
             "statement": statement, "units": "probability" if quantity == "p_zero"
             else UNITS if target == TARGET else "USD/household/month"}
            for key, quantity, value, target, sources, reference, statement in specifications]


def record_errors(record, sources):
    errors = []
    for key in ("id", "statement", "quantity", "target", "units", "sources", "value"):
        if key not in record:
            errors.append("missing field: " + key)
    if errors:
        return errors
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", record["id"]):
        errors.append("invalid identifier")
    if not isinstance(record["sources"], list) or not record["sources"]:
        errors.append("sources must be a nonempty list")
    else:
        errors.extend("unresolved source: " + source for source in record["sources"]
                      if source not in sources)
    if not isinstance(record["value"], (float, int)) or not math.isfinite(record["value"]):
        errors.append("nonfinite value")
    return errors


def contract_errors(record, sources, values):
    errors = record_errors(record, sources)
    if errors:
        return errors
    if "table" not in record["sources"]:
        errors.append("reported table required")
    if record["target"] != TARGET:
        errors.append("recorded outcome does not measure the claimed target")
    quantity = record["quantity"]
    if quantity not in ("estimate", "p_zero", "upper95"):
        errors.append("quantity requires additional premises and evidence")
    else:
        units = "probability" if quantity == "p_zero" else UNITS
        if record["units"] != units:
            errors.append("units disagree")
        if not math.isclose(record["value"], values[quantity], rel_tol=1e-10, abs_tol=1e-12):
            errors.append("number disagrees with the reconstruction")
    # No natural-language entailment check is performed here.
    return errors


def append_record(directory, record):
    """Exclusive creation preserves an existing record; it does not prove truth."""
    key = record["id"]
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", key):
        raise ValueError("Invalid record identifier")
    path = Path(directory) / (key + ".json")
    with path.open("x", encoding="utf-8") as stream:
        json.dump(record, stream, indent=2, sort_keys=True)
        stream.write("\n")
    return path


def revision_example():
    first = {"id": "decision-v1", "status": "accepted",
             "action": "publish an assurance", "claim": "household-assurance",
             "scenario": "fictional institutional decision"}
    revised = {"id": "decision-v2", "status": "accepted",
               "action": "withdraw the assurance and publish the bounded estimate",
               "claim": "estimate", "supersedes": "decision-v1",
               "reason": "Nonrejection and utility prices do not establish no household harm."}
    with tempfile.TemporaryDirectory() as name:
        original = append_record(name, first)
        before = digest(original)
        try:
            append_record(name, {**first, "action": "silently rewrite the old decision"})
        except FileExistsError:
            rejected = True
        else:
            rejected = False
        append_record(name, revised)
        checks = {"overwrite_rejected": rejected,
                  "original_preserved": digest(original) == before,
                  "revision_retained": len(list(Path(name).glob("*.json"))) == 2}
    return [first, revised], checks


def write_csv(path, rows):
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main(out):
    out.mkdir(parents=True, exist_ok=True)
    values = reconstruct()
    sources = {"table": {"kind": "reported_table", "sha256": digest(INPUT)},
               "manager-approval": {"kind": "human", "scenario": "fictional approval"}}
    claims = make_claims(values)
    rows = []
    for claim in claims:
        structural = record_errors(claim, sources)
        contract = contract_errors(claim, sources, values)
        rows.append({**claim, "sources": ";".join(claim["sources"]),
                     "record_valid": not structural, "contract_valid": not contract,
                     "record_errors": "; ".join(structural),
                     "contract_errors": "; ".join(contract)})
    comparisons = []
    for rule in ("record_valid", "contract_valid"):
        comparisons.append({"rule": rule, "records": len(rows),
                            "accepted": sum(row[rule] for row in rows),
                            "false_approvals": sum(row[rule] and not row["reference_acceptable"]
                                                   for row in rows),
                            "false_rejections": sum(not row[rule] and row["reference_acceptable"]
                                                    for row in rows)})
    history, checks = revision_example()
    if not all(checks.values()):
        raise AssertionError("Revision history was not preserved")
    write_csv(out / "claim_assessments.csv", rows)
    write_csv(out / "checker_comparison.csv", comparisons)
    for filename, value in (("table_reconstruction.json", values),
                            ("decision_history.json", history), ("preservation_checks.json", checks)):
        (out / filename).write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")
    outputs = ["claim_assessments.csv", "checker_comparison.csv", "table_reconstruction.json",
               "decision_history.json", "preservation_checks.json"]
    manifest = {"input": "../Statistical_Inference/results/data_center_estimates.csv",
                "input_sha256": digest(INPUT), "program_sha256": digest(__file__),
                "constructed_claims": len(claims), "live_model_calls": 0,
                "upstream_code_executed": False,
                "scope": "Normal approximation from rounded published summaries; authored claim cases.",
                "outputs": {name: digest(out / name) for name in outputs}}
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"checker_comparison": comparisons, "preservation": checks}, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=HERE / "results")
    main(parser.parse_args().out)
