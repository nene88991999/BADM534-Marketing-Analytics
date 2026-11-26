"""Recompute the supplement's three-device illustration under two transforms."""
import json
from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent
# Supplement Table 1's rounded MCI weights and Table 2's illustrative minutes.
WEIGHTS = np.array([.212, .263, .132, .098, .082, .142, .067])
MINUTES = np.array([[30, 200, 100, 25, 5, 600, 300],
                    [0, 15, 120, 0, 360, 1200, 45],
                    [10, 20, 45, 30, 20, 500, 30]], dtype=float)
PUBLISHED = np.array([4.46, 3.09, 3.47])


def compare():
    stated = np.log2(1 + MINUTES) @ WEIGHTS
    positive_log = np.zeros_like(MINUTES)
    np.log(MINUTES, out=positive_log, where=MINUTES > 0)
    alternative = positive_log @ WEIGHTS
    return stated, alternative


def main():
    stated, alternative = compare()
    totals = MINUTES.sum(axis=1)
    table = pd.DataFrame({"device": [1, 2, 3], "minutes": totals,
        "published_mci": PUBLISHED, "equation_s1": stated,
        "log_positive_minutes_zero_at_zero": alternative})
    table.to_csv(ROOT / "results/index_check.csv", index=False)
    summary = {"rounded_weights_sum": float(WEIGHTS.sum()),
        "equal_device_mean_of_displayed_values": float(PUBLISHED.mean()),
        "minute_weighted_mean_of_displayed_values": float(np.average(PUBLISHED, weights=totals)),
        "alternative_matches_displayed_rounding": bool(np.array_equal(np.round(alternative, 2), PUBLISHED)),
        "private_pipeline_transform": "unresolved"}
    (ROOT / "results/index_check.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(table.to_string(index=False))


if __name__ == "__main__":
    main()
