"""An explicitly hypothetical comparison over 100 assigned analysis tasks."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def calculate():
    wage_per_minute = 60 / 60  # An assumed analyst cost of $60 per hour.
    cases = [
        {"workflow": "Basic", "assigned": 100, "valid": 80, "api_dollars": 10,
         "review_minutes": 240, "correction_minutes": 100},
        {"workflow": "Checked", "assigned": 100, "valid": 95, "api_dollars": 20,
         "review_minutes": 150, "correction_minutes": 30},
    ]
    for row in cases:
        row["total_dollars"] = row["api_dollars"] + wage_per_minute * (
            row["review_minutes"] + row["correction_minutes"])
        row["valid_rate"] = row["valid"] / row["assigned"]
        row["dollars_per_valid_task"] = row["total_dollars"] / row["valid"]
    return {"scope": "Hypothetical inputs; no observed model performance or labor savings",
            "analyst_dollars_per_hour": 60, "cases": cases}


if __name__ == "__main__":
    output = HERE / "results"
    output.mkdir(exist_ok=True)
    result = calculate()
    (output / "hypothetical_costs.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
