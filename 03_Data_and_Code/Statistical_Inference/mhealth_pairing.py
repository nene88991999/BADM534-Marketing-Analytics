"""Compare paired-user and independent-day uncertainty in observed logging."""
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

ROOT = Path(__file__).resolve().parent
MHEALTH = ROOT.parent / "mHealth"
OUTPUT = ROOT / "results"
MONTHS = ("2016-05", "2016-06")


def load_days():
    """Verify the release and retain distinct days in the established cohort."""
    path = MHEALTH / "data/food_entries.csv.gz"
    manifest = json.loads((MHEALTH / "manifest.json").read_text())
    expected = manifest["files"][path.name]["sha256"]
    with path.open("rb") as handle:
        digest = hashlib.file_digest(handle, "sha256").hexdigest()
    if digest != expected:
        raise ValueError("Food-entry file differs from the released input")
    parts = []
    for chunk in pd.read_csv(path, usecols=["Userid", "Fancydate"],
                             chunksize=250000):
        code = chunk.Userid.str.slice(1, 5).map(lambda x: int(x, 16))
        part = chunk.loc[code < 4096].copy()
        part["date"] = pd.to_datetime(part.pop("Fancydate")).dt.normalize()
        parts.append(part.drop_duplicates())
    days = pd.concat(parts, ignore_index=True).drop_duplicates()
    return days, digest


def monthly_rates(days):
    """Fix membership before May; retain zero-log users in both months."""
    days = days[["Userid", "date"]].drop_duplicates()
    members = sorted(days.loc[days.date < "2016-05-01", "Userid"].unique())
    if len(members) < 2:
        raise ValueError("At least two users observed before May are required")
    rates = pd.DataFrame(index=members)
    rows = []
    for month in MONTHS:
        period = pd.Period(month, freq="M")
        mask = days.Userid.isin(members) & days.date.dt.to_period("M").eq(period)
        count = days.loc[mask].groupby("Userid").size().reindex(members, fill_value=0)
        if not count.between(0, period.days_in_month).all():
            raise ValueError("Logged days exceed the calendar denominator")
        rates[month] = count / period.days_in_month
        rows.append({"month": month, "users": len(members),
                     "logged_days": int(count.sum()),
                     "calendar_days": len(members) * period.days_in_month,
                     "users_without_logs": int(count.eq(0).sum()),
                     "logging_percent": float(100 * rates[month].mean())})
    return rates, rows


def compare_uncertainty(rates):
    """Two-sided tests of zero mean change; all effect units are percentage points."""
    x = rates[list(MONTHS)].to_numpy(dtype=float)
    if len(x) < 2 or not np.isfinite(x).all() or ((x < 0) | (x > 1)).any():
        raise ValueError("Complete user pairs with rates in [0, 1] are required")
    change = 100 * (x[:, 1] - x[:, 0])
    estimate = float(change.mean())
    se = float(change.std(ddof=1) / np.sqrt(len(x)))
    if se == 0:
        raise ValueError("A positive sample variance of changes is required")
    critical = stats.t.ppf(.975, len(x) - 1)
    paired_p = float(2 * stats.t.sf(abs(estimate / se), len(x) - 1))
    p = x.mean(axis=0)
    n_days = len(x) * np.array([31, 30])
    naive_se = float(100 * np.sqrt(np.sum(p * (1 - p) / n_days)))
    naive_p = float(2 * stats.norm.sf(abs(estimate / naive_se)))
    covariance = np.cov(100 * x.T, ddof=1)
    paired_variance = (covariance[0, 0] + covariance[1, 1]
                       - 2 * covariance[0, 1]) / len(x)
    if not np.isclose(paired_variance, se ** 2):
        raise AssertionError("Paired variance identity failed")
    return [
        {"method": "paired_users", "estimate_pp": estimate, "se_pp": se,
         "p_value": paired_p, "ci_low_pp": float(estimate - critical * se),
         "ci_high_pp": float(estimate + critical * se), "reference_df": len(x)-1,
         "independence_unit": "user", "interpretation": "descriptive change"},
        {"method": "independent_days_contrast", "estimate_pp": estimate,
         "se_pp": naive_se, "p_value": naive_p,
         "ci_low_pp": float(estimate - stats.norm.ppf(.975) * naive_se),
         "ci_high_pp": float(estimate + stats.norm.ppf(.975) * naive_se),
         "reference_df": None, "independence_unit": "user-day",
         "interpretation": "deliberately incorrect independence comparison"},
    ]


def main():
    days, digest = load_days()
    rates, monthly = monthly_rates(days)
    comparisons = compare_uncertainty(rates)
    OUTPUT.mkdir(exist_ok=True)
    pd.DataFrame(monthly).to_csv(OUTPUT / "mhealth_monthly.csv", index=False)
    pd.DataFrame(comparisons).to_csv(OUTPUT / "mhealth_uncertainty.csv", index=False)
    result = {"source_sha256": digest, "cohort_prefix_threshold": 4096,
              "membership": "observed before 2016-05-01", "users": len(rates),
              "outcome": "fraction of calendar days with a recorded food entry",
              "estimand": "mean within-user June minus May change",
              "causal_effect": False, "comparisons": comparisons}
    (OUTPUT / "mhealth.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
