"""Synthetic project histories, comparison windows, and donor sensitivity.

Prices are dollars/MWh. Each project belongs to a distinct utility. No source
observations or estimates from the electricity paper enter these calculations.
"""
import csv
from pathlib import Path

OUT = Path(__file__).resolve().parent / "results"


def construct():
    paths = {
        "completed": ([100, 106, 110], ["no_request", "committed", "operating"]),
        "cancelled": ([100, 106, 106], ["no_request", "committed", "cancelled"]),
        "unexposed": ([100, 100, 100], ["no_request"] * 3),
        "pending": ([100, 100, 106], ["no_request", "requested", "committed"]),
    }
    dates = ["2023Q1", "2024Q1", "2025Q4"]
    panel = [dict(utility=unit, quarter=date, period=t, state=states[t],
                  operating=int(states[t] == "operating"), price_usd_mwh=prices[t])
             for unit, (prices, states) in paths.items()
             for t, date in enumerate(dates)]
    price = {(r["utility"], r["period"]): r["price_usd_mwh"] for r in panel}
    def change(unit, baseline):
        return price[unit, 2] - price[unit, baseline]
    comparisons = []
    for label, baseline, cancelled_weight in [
        ("before_commitment_unexposed_donor", 0, 0),
        ("before_commitment_mixed_donors", 0, .5),
        ("before_opening_mixed_donors", 1, .5),
    ]:
        donor_change = (cancelled_weight * change("cancelled", baseline)
                        + (1 - cancelled_weight) * change("unexposed", baseline))
        comparisons.append(dict(comparison=label, baseline=dates[baseline],
                                treated_change=change("completed", baseline),
                                weighted_donor_change=donor_change,
                                change_difference=change("completed", baseline)
                                - donor_change))
    assert [r["change_difference"] for r in comparisons] == [10, 7, 4]
    sensitivity = [dict(cancelled_donor_increment=cost,
                        cancelled_donor_weight=weight,
                        gap=10 - weight * cost)
                   for cost in [0, 6, 12, 24] for weight in [0, .5, 1]]
    populations = []
    # Fixed status composition; change the net effect for the completed project.
    # These are means of imposed potential effects, not observational estimates.
    for scenario, completed in [("all_positive", 10), ("operating_savings", -2)]:
        populations.append(dict(scenario=scenario, proposal_units=3,
                                operating_units=1, completed_effect=completed,
                                cancelled_effect=6, pending_effect=6,
                                proposal_mean=(completed + 6 + 6) / 3,
                                operating_mean=completed))
    assert populations[0]["proposal_mean"] == 22 / 3
    assert populations[1]["proposal_mean"] == 10 / 3
    return {"project_panel.csv": panel, "window_comparisons.csv": comparisons,
            "donor_sensitivity.csv": sensitivity,
            "selected_populations.csv": populations}


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    for name, rows in construct().items():
        with (OUT / name).open("w", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
        print(name, len(rows), "rows")
