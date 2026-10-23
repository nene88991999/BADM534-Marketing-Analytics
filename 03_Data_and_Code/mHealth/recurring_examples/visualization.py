"""Prepare aggregate chart data and paired uncertainty for May and June."""

import json
import numpy as np
import pandas as pd
from common import OUTPUT, ROOT, SEED, load_food, save_result

MONTHS = ["2016-05", "2016-06"]


def prepare(food):
    # Membership is fixed before May; an absent log is zero logging only.
    members = sorted(food.loc[food.date < "2016-05-01", "Userid"].unique())
    if not members:
        raise ValueError("No users observed before May")
    rates = pd.DataFrame(index=members)
    rows = []
    for month in MONTHS:
        period = pd.Period(month, freq="M")
        part = food.loc[
            food.Userid.isin(members) & food.date.dt.to_period("M").eq(period)
        ]
        counts = (
            part[["Userid", "date"]].drop_duplicates().groupby("Userid").size()
            .reindex(members, fill_value=0)
        )
        rates[month] = counts / period.days_in_month
        observed = int(counts.sum())
        active = int(counts.gt(0).sum())
        assert counts.between(0, period.days_in_month).all()
        rows.append({
            "period": month, "eligible_users": len(members),
            "users_with_logs": active, "observed_user_days": observed,
            "calendar_user_days": len(members) * period.days_in_month,
            "logger_calendar_days": active * period.days_in_month,
            "food_entries": len(part),
            "logging_percent": 100 * rates[month].mean(),
            "conditional_logging_percent": (
                100 * observed / (active * period.days_in_month) if active else None
            ),
            "entries_per_observed_day": len(part) / observed if observed else None,
        })
    return rates, pd.DataFrame(rows)


def ecdf(values):
    """Exact right-continuous CDF; tied values contribute their full mass."""
    values = np.asarray(values, dtype=float)
    if len(values) == 0 or not np.isfinite(values).all():
        raise ValueError("A nonempty finite sample is required")
    x, count = np.unique(values, return_counts=True)
    return pd.DataFrame({
        "logging_percent": 100 * x, "users_at_value": count,
        "cumulative_percent": 100 * count.cumsum() / len(values),
        "eligible_users": len(values),
    })


def paired_summary(rates, draws=5000):
    # Each sampled index carries both months for the same user.
    difference = rates[MONTHS[1]].to_numpy() - rates[MONTHS[0]].to_numpy()
    if len(difference) < 2 or not np.isfinite(difference).all():
        raise ValueError("At least two complete user pairs are required")
    rng = np.random.default_rng(SEED)
    indices = rng.integers(0, len(difference), size=(draws, len(difference)))
    bootstrap = difference[indices].mean(axis=1)
    low, high = np.quantile(bootstrap, [0.025, 0.975])
    return {
        "users": len(difference), "bootstrap_draws": draws, "seed": SEED,
        "change_pp": float(100 * difference.mean()),
        "ci_low_pp": float(100 * low), "ci_high_pp": float(100 * high),
        "paired_se_pp": float(100 * difference.std(ddof=1) / np.sqrt(len(difference))),
        "individual_change_q25_pp": float(100 * np.quantile(difference, 0.25)),
        "individual_change_median_pp": float(100 * np.median(difference)),
        "individual_change_q75_pp": float(100 * np.quantile(difference, 0.75)),
    }


def main():
    rates, monthly = prepare(load_food())
    comparison = paired_summary(rates)
    # Deliberately wrong independence assumption, retained as a teaching contrast.
    p = monthly.logging_percent.to_numpy() / 100
    n = monthly.calendar_user_days.to_numpy()
    naive_se = float(100 * np.sqrt(np.sum(p * (1 - p) / n)))
    comparison.update({
        "naive_independent_days_se_pp": naive_se,
        "naive_ci_low_pp": comparison["change_pp"] - 1.96 * naive_se,
        "naive_ci_high_pp": comparison["change_pp"] + 1.96 * naive_se,
    })
    cdf = pd.concat([ecdf(rates[m]).assign(period=m) for m in MONTHS], ignore_index=True)
    assert np.allclose(monthly.logging_percent,
                       100 * monthly.observed_user_days / monthly.calendar_user_days)
    assert cdf.groupby("period").users_at_value.sum().eq(len(rates)).all()
    OUTPUT.mkdir(exist_ok=True)
    monthly.to_csv(OUTPUT / "visualization_monthly.csv", index=False)
    cdf.to_csv(OUTPUT / "visualization_ecdf.csv", index=False)
    manifest = json.loads((ROOT.parent / "manifest.json").read_text())
    result = {
        "source_sha256": manifest["files"]["food_entries.csv.gz"]["sha256"],
        "membership": "At least one observed day before 2016-05-01",
        "observation": "user-month; fraction of calendar days with a food entry",
        "interpretation": "descriptive within the selected cohort",
        "months": monthly.to_dict(orient="records"), "paired_change": comparison,
    }
    save_result("visualization", result)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
