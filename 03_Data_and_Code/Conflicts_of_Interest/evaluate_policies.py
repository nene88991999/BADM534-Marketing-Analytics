"""Compare synthetic feed policies, incentive weights, and refusal rights."""
import csv
import json
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
INTEGER_FIELDS = (
    "n", "contribution_cents", "goals_completed", "regret_reports",
    "excess_minutes", "respects_stop", "discloses_incentive",
)


def load_rows(path):
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    seen = set()
    for row in rows:
        for name in INTEGER_FIELDS:
            row[name] = int(row[name])
        key = (row["policy"], row["group"])
        assert key not in seen, key
        seen.add(key)
        assert row["n"] > 0
        for name in ("goals_completed", "regret_reports"):
            assert 0 <= row[name] <= row["n"]
        assert row["contribution_cents"] >= 0
        assert row["excess_minutes"] >= 0
        for name in ("respects_stop", "discloses_incentive"):
            assert row[name] in (0, 1)
    return rows


def summarize(rows):
    by_policy = defaultdict(list)
    for row in rows:
        by_policy[row["policy"]].append(row)
    composition = None
    result = {}
    for policy, group_rows in by_policy.items():
        current = {r["group"]: r["n"] for r in group_rows}
        if composition is None:
            composition = current
        assert current == composition, "Policy populations differ"
        n = sum(r["n"] for r in group_rows)
        totals = {
            k: sum(r[k] for r in group_rows)
            for k in ("contribution_cents", "goals_completed",
                      "regret_reports", "excess_minutes")
        }
        result[policy] = {
            "n": n, **totals,
            "contribution_usd_per_user_day": totals["contribution_cents"] / (100 * n),
            "goal_completion_rate": totals["goals_completed"] / n,
            "regret_rate": totals["regret_reports"] / n,
            "excess_minutes_per_user_day": totals["excess_minutes"] / n,
            "respects_stop": all(r["respects_stop"] for r in group_rows),
            "discloses_incentive": all(r["discloses_incentive"] for r in group_rows),
            "groups": {
                r["group"]: {
                    "n": r["n"],
                    "goal_completion_rate": r["goals_completed"] / r["n"],
                    "regret_rate": r["regret_reports"] / r["n"],
                } for r in group_rows
            },
        }
    return result


def best(policies, penalty, require_stop=False):
    """Penalty units: hypothetical USD per additional regret report."""
    scores = {
        name: p["contribution_usd_per_user_day"] - penalty * p["regret_rate"]
        for name, p in policies.items()
        if not require_stop or p["respects_stop"]
    }
    assert scores, "No policy meets the stated condition"
    maximum = max(scores.values())
    return sorted(name for name, score in scores.items()
                  if abs(score - maximum) < 1e-12)


def main():
    policies = summarize(load_rows(HERE / "policy_inputs.csv"))
    weights = [0, 0.5, 2]
    decisions = [
        {"regret_penalty_usd": weight, "require_stop": stop,
         "maximizers": best(policies, weight, stop)}
        for stop in (False, True) for weight in weights
    ]
    output = {"status": "synthetic exact scenario; no estimated effects",
              "policies": policies, "decisions": decisions}
    destination = HERE / "results"
    destination.mkdir(exist_ok=True)
    (destination / "policy_comparison.json").write_text(
        json.dumps(output, indent=2) + "\n", encoding="utf-8")
    for policy, values in policies.items():
        print(policy, f"USD {values['contribution_usd_per_user_day']:.3f}",
              f"goals {values['goal_completion_rate']:.1%}",
              f"regret {values['regret_rate']:.1%}")
    for decision in decisions:
        print(decision)


if __name__ == "__main__":
    main()
