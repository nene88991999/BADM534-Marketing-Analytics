"""Exact synthetic error probabilities and decision losses; standard library only."""

from csv import DictWriter
from math import isclose, log
from pathlib import Path
from statistics import NormalDist
import json


NORMAL = NormalDist()
PREVALENCE = 0.10
SIGNAL_SHIFT = 2.0
OUTPUT = Path(__file__).resolve().parent / "results"


def error_rates(cutoff, shift=SIGNAL_SHIFT):
    """Flag harm when Z > cutoff; Z is N(0,1) or N(shift,1)."""
    false_positive = NORMAL.cdf(-cutoff)
    false_negative = NORMAL.cdf(cutoff - shift)
    return false_positive, false_negative


def expected_loss(cutoff, false_positive_cost, false_negative_cost,
                  prevalence=PREVALENCE, shift=SIGNAL_SHIFT):
    alpha, beta = error_rates(cutoff, shift)
    return ((1 - prevalence) * alpha * false_positive_cost
            + prevalence * beta * false_negative_cost)


def optimal_cutoff(false_positive_cost, false_negative_cost,
                   prevalence=PREVALENCE, shift=SIGNAL_SHIFT):
    """Minimize loss for two normal states with equal variance and positive shift."""
    if not 0 < prevalence < 1 or shift <= 0:
        raise ValueError("Use a prevalence in (0,1) and a positive signal shift.")
    if min(false_positive_cost, false_negative_cost) <= 0:
        raise ValueError("Error costs must be positive.")
    odds = ((1 - prevalence) * false_positive_cost
            / (prevalence * false_negative_cost))
    return shift / 2 + log(odds) / shift


def write_csv(path, records):
    with path.open("w", newline="") as handle:
        writer = DictWriter(handle, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)


def verify_calculations():
    # Symmetry gives an independent benchmark at the midpoint of the signals.
    alpha, beta = error_rates(SIGNAL_SHIFT / 2)
    assert isclose(alpha, beta, abs_tol=1e-12)
    assert isclose(error_rates(0)[0], 0.5, abs_tol=1e-12)
    assert isclose(optimal_cutoff(1, 1, prevalence=0.5), 1.0)
    # Check the analytical optimum against a separately enumerated dense grid.
    grid = [i / 1000 for i in range(-1000, 6001)]
    for fp, fn in [(1, 20), (20, 1)]:
        optimum = optimal_cutoff(fp, fn)
        grid_optimum = min(grid, key=lambda c: expected_loss(c, fp, fn))
        assert abs(optimum - grid_optimum) <= 0.00051
        assert expected_loss(optimum, fp, fn) <= expected_loss(grid_optimum, fp, fn) + 1e-12
    # Posterior odds at the optimum equal the specified loss ratio.
    cutoff = optimal_cutoff(1, 20)
    posterior_odds = (PREVALENCE / (1 - PREVALENCE)
                      * NORMAL.pdf(cutoff - SIGNAL_SHIFT) / NORMAL.pdf(cutoff))
    assert isclose(posterior_odds, 1 / 20, rel_tol=1e-12)
    return "Passed: symmetry, probability boundary, equal-cost benchmark, grid optima, posterior odds."


def main():
    verification = verify_calculations()
    OUTPUT.mkdir(exist_ok=True)
    scenarios = [("Missed harm costs 20", 1.0, 20.0),
                 ("Mistaken intervention costs 20", 20.0, 1.0)]
    rows = []
    for scenario, fp, fn in scenarios:
        rules = [("One-percent test", NORMAL.inv_cdf(0.99)),
                 ("Five-percent test", NORMAL.inv_cdf(0.95)),
                 ("Minimum expected loss", optimal_cutoff(fp, fn))]
        for rule, cutoff in rules:
            alpha, beta = error_rates(cutoff)
            rows.append({
                "scenario": scenario, "rule": rule, "cutoff": cutoff,
                "prevalence": PREVALENCE, "signal_shift": SIGNAL_SHIFT,
                "false_positive_cost": fp, "false_negative_cost": fn,
                "false_positive_rate": alpha, "false_negative_rate": beta,
                "power": 1 - beta,
                "expected_loss": expected_loss(cutoff, fp, fn),
            })
    write_csv(OUTPUT / "decision_rules.csv", rows)
    write_csv(OUTPUT / "figure_points.csv", rows[:3])
    commands = {"PrevalencePercent": 100 * PREVALENCE, "SignalShift": SIGNAL_SHIFT}
    for prefix, row in zip(["One", "Five", "Optimal"], rows[:3]):
        commands[prefix + "Cutoff"] = row["cutoff"]
        commands[prefix + "Loss"] = row["expected_loss"]
    (OUTPUT / "figure_values.tex").write_text("\n".join(
        "\\newcommand{\\" + name + "}{" + f"{value:.12f}" + "}"
        for name, value in commands.items()) + "\n")
    curve = []
    for index in range(161):
        cutoff = index / 40
        alpha, beta = error_rates(cutoff)
        curve.append({
            "cutoff": cutoff, "false_positive_rate": alpha,
            "false_negative_rate": beta,
            "missed_harm_cost_20": expected_loss(cutoff, 1, 20),
            "mistaken_intervention_cost_20": expected_loss(cutoff, 20, 1),
        })
    write_csv(OUTPUT / "risk_curve.csv", curve)
    summary = {
        "data_status": "Synthetic known distributions; no estimated market effects.",
        "unit": "One hypothetical case before observing its signal.",
        "null": "No specified harm; Z ~ N(0,1).",
        "alternative": "Specified harm; Z ~ N(2,1).",
        "prevalence": PREVALENCE,
        "loss_units": "Illustrative comparable loss units per case.",
        "correct_decision_loss": 0,
        "verification": verification,
        "rules": rows,
    }
    (OUTPUT / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(verification)
    for row in rows:
        print(f"{row['scenario']} | {row['rule']}: "
              f"alpha={row['false_positive_rate']:.4f}, "
              f"beta={row['false_negative_rate']:.4f}, "
              f"loss={row['expected_loss']:.4f}")


if __name__ == "__main__":
    main()
