"""Check constructed structured claims against computed mHealth evidence."""

import json
import math
from copy import deepcopy
from common import load_food, save_result
from reporting import monthly_review


def check_claim(claim, evidence):
    required = {"metric", "period", "value", "unit", "denominator", "interpretation"}
    if not isinstance(claim, dict) or set(claim) != required:
        return ["schema"]
    rows = [row for row in evidence["periods"] if row["period"] == claim["period"]]
    if len(rows) != 1 or claim["metric"] != evidence["metric"]:
        return ["unknown metric or period"]
    row = rows[0]
    errors = []
    if type(claim["value"]) not in (int, float) or not math.isfinite(claim["value"]):
        errors.append("numeric value")
    elif not math.isclose(
        claim["value"], row["logging_fraction"], rel_tol=0, abs_tol=1e-10
    ):
        errors.append("value disagrees with evidence")
    if (
        type(claim["denominator"]) is not int
        or claim["denominator"] != row["calendar_user_days"]
    ):
        errors.append("denominator")
    if claim["unit"] != evidence["unit"]:
        errors.append("unit")
    if claim["interpretation"] != evidence["interpretation"]:
        errors.append("unsupported interpretation")
    return errors


if __name__ == "__main__":
    evidence = monthly_review(load_food())
    june = evidence["periods"][1]
    valid = {
        "metric": "logging_fraction",
        "period": "2016-06",
        "value": june["logging_fraction"],
        "unit": evidence["unit"],
        "denominator": june["calendar_user_days"],
        "interpretation": "descriptive",
    }
    candidates = {"supported": valid}
    changes = {
        "wrong_number": ("value", valid["value"] + 0.1),
        "wrong_denominator": ("denominator", june["users_with_logs"]),
        "causal_claim": ("interpretation", "causal health benefit"),
    }
    for name, (field, value) in changes.items():
        candidates[name] = deepcopy(valid)
        candidates[name][field] = value
    result = {
        "candidate_origin": "constructed teaching examples; no LLM request",
        "checks": {
            name: check_claim(claim, evidence) for name, claim in candidates.items()
        },
    }
    assert result["checks"]["supported"] == []
    assert all(result["checks"][name] for name in changes)
    save_result("claim_checks", result)
    print(json.dumps(result, indent=2))
