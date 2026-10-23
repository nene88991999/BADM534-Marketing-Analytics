"""Check a narrow chart specification against the monthly evidence table."""

from copy import deepcopy
import json
import math
from common import OUTPUT, save_result


def check_chart(chart, evidence):
    errors = []
    expected = {row["period"]: row for row in evidence["months"]}
    if chart.get("unit") != "percent of eligible user-days":
        errors.append("axis unit")
    if chart.get("interpretation") != "descriptive":
        errors.append("interpretation")
    if chart.get("mark") == "bar" and chart.get("y_domain", [None])[0] != 0:
        errors.append("bar baseline")
    rows = chart.get("rows", [])
    if sorted(row["period"] for row in rows) != sorted(expected):
        errors.append("period coverage")
    for row in rows:
        ref = expected.get(row["period"])
        if ref is None:
            continue
        value = row["value"]
        target = 100 * ref["observed_user_days"] / ref["calendar_user_days"]
        if not math.isfinite(value) or not math.isclose(value, target, abs_tol=1e-8):
            errors.append("plotted value")
        if row["denominator"] != ref["calendar_user_days"]:
            errors.append("denominator")
    return sorted(set(errors))


def main():
    evidence = json.loads((OUTPUT / "visualization.json").read_text())
    correct = {
        "unit": "percent of eligible user-days", "interpretation": "descriptive",
        "mark": "bar", "y_domain": [0, 100],
        "rows": [{"period": r["period"], "value": r["logging_percent"],
                  "denominator": r["calendar_user_days"]} for r in evidence["months"]],
    }
    cases = {"correct": correct}
    for name in ["fraction_as_percent", "conditional_denominator", "truncated_bar", "causal_title"]:
        cases[name] = deepcopy(correct)
    cases["fraction_as_percent"]["rows"][0]["value"] /= 100
    row = cases["conditional_denominator"]["rows"][0]
    row["denominator"] = evidence["months"][0]["logger_calendar_days"]
    row["value"] = evidence["months"][0]["conditional_logging_percent"]
    cases["truncated_bar"]["y_domain"] = [60, 75]
    cases["causal_title"]["interpretation"] = "causal"
    result = {name: check_chart(chart, evidence) for name, chart in cases.items()}
    assert result["correct"] == []
    assert all(result[name] for name in cases if name != "correct")
    save_result("chart_audit", {"constructed_cases": result})
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
