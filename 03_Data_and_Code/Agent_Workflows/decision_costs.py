"""Hypothetical review spending and loss from undetected analysis errors."""
import csv
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
WORKFLOWS = [
    {"workflow": "Basic", "api_per_task": 0.02, "review_minutes": 0.25, "undetected_error_probability": 0.05},
    {"workflow": "Checked", "api_per_task": 0.05, "review_minutes": 0.50, "undetected_error_probability": 0.01},
]


def expected_cost(row, loss, assigned=1000, wage_per_hour=60):
    p = row["undetected_error_probability"]
    if not 0 <= p <= 1 or min(loss, assigned, wage_per_hour, row["api_per_task"], row["review_minutes"]) < 0:
        raise ValueError("Probabilities must be in [0,1] and costs and counts nonnegative.")
    operating = row["api_per_task"] + row["review_minutes"] * wage_per_hour / 60
    return {"workflow": row["workflow"], "loss_per_undetected_error": loss,
            "assigned": assigned, "operating_dollars": assigned * operating,
            "expected_undetected_errors": assigned * p,
            "expected_error_loss_dollars": assigned * p * loss,
            "expected_total_dollars": assigned * (operating + p * loss)}


def break_even(basic, checked, wage_per_hour=60):
    cost0 = expected_cost(basic, 0, 1, wage_per_hour)["operating_dollars"]
    cost1 = expected_cost(checked, 0, 1, wage_per_hour)["operating_dollars"]
    improvement = basic["undetected_error_probability"] - checked["undetected_error_probability"]
    return (cost1 - cost0) / improvement if improvement else None


def main():
    output = HERE / "results"
    output.mkdir(exist_ok=True)
    threshold = break_even(*WORKFLOWS)
    rows = [expected_cost(row, loss) for loss in [0, 5, 7, 10, 20] for row in WORKFLOWS]
    with (output / "decision_costs.csv").open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    summary = {"scope": "Hypothetical inputs; no estimated labor savings or customer harm",
               "assigned_tasks": 1000, "analyst_dollars_per_hour": 60,
               "review_scope": "All review and correction time per assigned task",
               "workflows": WORKFLOWS, "break_even_loss_dollars": threshold,
               "loss_scope": "Manager-specified monetary consequence of an undetected wrong analysis"}
    (output / "decision_cost_summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps({"summary": summary, "costs": rows}, indent=2))


if __name__ == "__main__":
    main()
