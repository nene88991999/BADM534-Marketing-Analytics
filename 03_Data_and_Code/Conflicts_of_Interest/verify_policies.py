"""Independent hand calculations for the synthetic comparison."""
import json
from pathlib import Path
from evaluate_policies import best

result = json.loads((Path(__file__).parent / "results/policy_comparison.json").read_text())
p = result["policies"]
expected = {
    "finite_feed": (20000, 880, 40, 2400),
    "endless_feed": (31400, 856, 122, 6400),
    "disclosed_endless": (31400, 856, 122, 6400),
    "user_controls": (23600, 918, 34, 1200),
}
for name, totals in expected.items():
    row = p[name]
    assert row["n"] == 1000
    assert tuple(row[k] for k in (
        "contribution_cents", "goals_completed", "regret_reports", "excess_minutes"
    )) == totals
    assert abs(row["contribution_usd_per_user_day"] - totals[0] / 100000) < 1e-12
    assert abs(row["goal_completion_rate"] - totals[1] / 1000) < 1e-12
    assert abs(row["regret_rate"] - totals[2] / 1000) < 1e-12
    assert abs(row["excess_minutes_per_user_day"] - totals[3] / 1000) < 1e-12
assert p["endless_feed"]["groups"]["time_limited"]["regret_rate"] == 0.45
assert p["user_controls"]["groups"]["time_limited"]["regret_rate"] == 0.05
assert p["endless_feed"]["groups"]["leisure"]["goal_completion_rate"] == 0.92
assert p["endless_feed"]["groups"]["time_limited"]["goal_completion_rate"] == 0.60
assert not p["endless_feed"]["discloses_incentive"]
assert p["disclosed_endless"]["discloses_incentive"]
for weight in (0, 0.5):
    assert best(p, weight) == ["disclosed_endless", "endless_feed"]
assert best(p, 2) == ["user_controls"]
for weight in (0, 0.5, 2):
    assert best(p, weight, True) == ["user_controls"]
print("Verified exact totals, denominators, group burdens, ties, weights, and stopping condition.")
