"""Recompute published aggregates; no model calls or upstream code execution."""
import csv
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parents[1] / "01_Resources/40_Econometric_Coding_Workflows/data"
ORDER = ["chatbot", "self_repair", "agent"]


def read_csv(path):
    with path.open(newline="") as stream:
        return list(csv.DictReader(stream))


def failure_rates(rows):
    result = []
    for row in rows:
        n, failed, loud, silent = (int(row[k]) for k in ["n", "failures", "loud", "silent"])
        if n <= 0 or min(loud, silent) < 0 or failed != loud + silent or failed > n:
            raise ValueError("Failure counts must partition a positive assigned-run denominator.")
        result.append({"agency": row["agency"], "assigned": n, "successes": n - failed,
                       "failures": failed, "loud": loud, "silent": silent,
                       "success_pct": 100 * (n - failed) / n,
                       "loud_per100": 100 * loud / n, "silent_per100": 100 * silent / n,
                       "silent_share_of_failures_pct": 100 * silent / failed if failed else None})
    return sorted(result, key=lambda row: ORDER.index(row["agency"]))


def prompt_contrasts(rows):
    cells = {}
    for row in rows:
        if row["panel"] != "prompt":
            continue
        key = row["agency"], row["prompt"]
        if key in cells:
            raise ValueError("Duplicate prompt cell.")
        n, passed = int(row["n"]), int(row["successes"])
        if n <= 0 or not 0 <= passed <= n:
            raise ValueError("Invalid success count.")
        cells[key] = (n, passed)
    result = []
    for agency in ORDER:
        n0, s0 = cells[agency, "zero_shot"]
        n1, s1 = cells[agency, "few_shot"]
        p0, p1 = s0 / n0, s1 / n1
        result.append({"agency": agency, "zero_assigned": n0, "example_assigned": n1,
                       "zero_successes": s0, "example_successes": s1,
                       "zero_success_pct": 100 * p0, "example_success_pct": 100 * p1,
                       "gain_pp": 100 * (p1 - p0),
                       "fraction_of_zero_failures_removed": (p1 - p0) / (1 - p0) if p0 < 1 else None})
    return result


def save_csv(path, rows):
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main():
    output = HERE / "results"
    output.mkdir(exist_ok=True)
    raw = read_csv(SOURCE / "appendix_silent_vs_loud.csv")
    failures = failure_rates(raw)
    for row in failures:
        published = next(x for x in raw if x["agency"] == row["agency"])
        for field in ["loud_per100", "silent_per100", "silent_share_of_failures_pct"]:
            assert math.isclose(row[field], float(published[field]), abs_tol=1e-10)
    prompts = prompt_contrasts(read_csv(SOURCE / "prompt_agency.csv"))
    for row in failures:
        paired = next(x for x in prompts if x["agency"] == row["agency"])
        assert row["assigned"] == paired["zero_assigned"] + paired["example_assigned"]
        assert row["successes"] == paired["zero_successes"] + paired["example_successes"]
    cost_rows = []
    for row in read_csv(SOURCE / "summary_by_model.csv"):
        gain = (float(row["agent_pct"]) - float(row["chatbot_pct"])) / 100
        increase = float(row["cost_per_run_agent_usd"]) - float(row["cost_per_run_chatbot_usd"])
        cost_rows.append({"model": row["model"], "gain_pp": 100 * gain,
                          "additional_dollars_per_run": increase,
                          "dollars_per_additional_success": increase / gain if gain > 0 else None})
    save_csv(output / "benchmark_failure_rates.csv", failures)
    save_csv(output / "benchmark_prompt_contrasts.csv", prompts)
    save_csv(output / "benchmark_incremental_cost.csv", cost_rows)
    summary = {"source": "Galiani, Lopez, and Sosa; release v1.2, November manuscript",
               "assigned_runs": sum(r["assigned"] for r in failures), "tasks": 40,
               "models": 6, "source_datasets": 32,
               "self_repair_share_of_success_gain":
               (failures[1]["successes"] - failures[0]["successes"]) /
               (failures[2]["successes"] - failures[0]["successes"]),
               "prompt_interaction_pp": prompts[2]["gain_pp"] - prompts[0]["gain_pp"],
               "scope": "Published aggregate reconstruction; original runs and bootstrap not rerun"}
    (output / "benchmark_summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps({"summary": summary, "failures": failures, "prompts": prompts}, indent=2))


if __name__ == "__main__":
    main()
