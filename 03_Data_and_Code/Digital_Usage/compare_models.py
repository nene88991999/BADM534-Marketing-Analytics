"""Compare descriptive income slopes on one complete-case geographic sample."""
import json
from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent


def fit(x, y, weights):
    # Weighted least squares by a square-root transformation; no inversion.
    scale = np.sqrt(weights / weights.mean())
    beta, _, rank, _ = np.linalg.lstsq(x * scale[:, None], y * scale, rcond=None)
    if rank != x.shape[1]:
        raise ValueError("The design matrix is rank deficient")
    return beta


def main():
    data = pd.read_csv(ROOT / "results/joined_areas.csv", dtype={"zip": "string"})
    fields = ["income_10k", "college_share", "broadband_share"]
    # Same rows for all models and both outcomes; equal geographic weights.
    sample = data.dropna(subset=fields).copy()
    assert len(sample) == int(data.regression_eligible.sum())
    ones = np.ones(len(sample))
    designs = {
        "Income": np.column_stack([ones, sample.income_10k]),
        "Income, Education, Broadband": np.column_stack([ones, sample[fields]]),
    }
    state = pd.get_dummies(sample.state, drop_first=True).to_numpy(dtype=float)
    designs["Controls and State Effects"] = np.column_stack([
        designs["Income, Education, Broadband"], state])
    result = []
    for outcome in ["mci", "cci"]:
        y = sample[outcome].to_numpy()
        for name, x in designs.items():
            beta = fit(x, y, ones)
            result.append({"index": outcome, "model": name,
                "areas": len(sample), "income_slope_per_10000_dollars": beta[1],
                "rmse_index_units": float(np.sqrt(np.mean((y - x @ beta) ** 2)))})
    pd.DataFrame(result).to_csv(ROOT / "results/regressions.csv", index=False)
    # Census household weights change the geographic estimand. They are not
    # Windows device counts or counts of individual people using applications.
    weighted = []
    for outcome in ["mci", "cci"]:
        y = sample[outcome].to_numpy()
        x = designs["Income, Education, Broadband"]
        beta = fit(x, y, sample.B28002_E001.to_numpy())
        weighted.append({"index": outcome, "areas": len(sample),
            "income_slope_per_10000_dollars": beta[1],
            "weight": "ACS household estimate"})
    pd.DataFrame(weighted).to_csv(ROOT / "results/household_weight_sensitivity.csv", index=False)
    (ROOT / "results/model_scope.json").write_text(json.dumps({
        "sample": len(sample), "unit": "released ZIP matched to 2021 ACS ZCTA",
        "income_units": "10000 inflation-adjusted 2021 dollars",
        "acs_period": "2017-2021", "usage_period": "October 2022-March 2023",
        "uncertainty": "No causal effect, population inference, or confidence interval estimated; ACS sampling error, privacy noise, and spatial dependence are not propagated."}, indent=2) + "\n")
    print(pd.DataFrame(result).to_string(index=False))


if __name__ == "__main__":
    main()
