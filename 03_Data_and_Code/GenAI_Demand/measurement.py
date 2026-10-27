"""Audit the supplied Wikipedia capture without making network requests."""
from pathlib import Path
import json

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parents[1] / "01_Resources/08_M8_Current_Topics_in_Marketing/genai_demand_lab/data"
OUTPUT = HERE / "results"
TITLES = ["Claude_(language_model)", "Claude_(AI)"]


def unique_views(frame):
    """Count each title-date once; reject conflicting repeated responses."""
    keys = ["date", "article"]
    if frame[keys + ["provider", "views"]].isna().any().any():
        raise ValueError("Missing title, date, provider, or view count")
    if not np.isfinite(frame.views).all() or (frame.views < 0).any():
        raise ValueError("View counts must be finite and nonnegative")
    if (frame.views % 1 != 0).any():
        raise ValueError("View counts must be integers")
    conflicts = frame.groupby(keys)[["provider", "views"]].nunique()
    if (conflicts > 1).any().any():
        raise ValueError("Conflicting repeated title-date responses")
    return frame.drop_duplicates(keys).copy()


def title_calendar(frame, titles, start, end):
    """A missing title-day remains unknown; zero must be explicitly recorded."""
    frame = unique_views(frame)
    dates = pd.date_range(start, end, freq="D")
    selected = frame.loc[frame.article.isin(titles)]
    wide = selected.pivot(index="date", columns="article", values="views")
    wide = wide.reindex(index=dates, columns=titles)
    wide["observed_titles"] = wide[titles].notna().sum(axis=1)
    wide["selected_title_views"] = wide[titles].sum(axis=1, min_count=len(titles))
    wide.index.name = "date"
    return wide


def main():
    raw = pd.read_csv(SOURCE / "wikipedia_pageviews_daily_2026-10-26.csv", parse_dates=["date"])
    clean = unique_views(raw)
    daily = title_calendar(clean, TITLES, "2026-06-01", "2026-09-30")
    rows = []
    for month, group in daily.groupby(daily.index.to_period("M")):
        row = {"month": str(month), "calendar_days": len(group),
               "complete_days": int(group.selected_title_views.notna().sum())}
        for column in TITLES + ["selected_title_views"]:
            # Full-month totals are missing if even one title-day is unknown.
            row[column] = group[column].sum(min_count=len(group))
        rows.append(row)
    monthly = pd.DataFrame(rows)
    assert monthly.complete_days.eq(monthly.calendar_days).all()
    june, september = monthly.iloc[0], monthly.iloc[-1]
    result = {
        "input_rows": len(raw), "unique_title_days": len(clean),
        "exact_duplicates_removed": len(raw) - len(clean),
        "selected_titles": TITLES, "complete_days": int(daily.selected_title_views.notna().sum()),
        "old_title_change_pct": 100 * (september[TITLES[0]] / june[TITLES[0]] - 1),
        "selected_titles_change_pct": 100 * (september.selected_title_views / june.selected_title_views - 1),
        "measurement": "Recorded pageview events for two selected English Wikipedia titles; not unique people or payments",
        "capture_status": "Supplied dated CSV, not a new retrieval; API responses and rename history were not re-collected",
    }
    # Independent aggregate check using the long input rather than the pivot.
    selected = clean.loc[clean.article.isin(TITLES) & clean.date.between(daily.index.min(), daily.index.max())]
    direct = selected.groupby(selected.date.dt.to_period("M")).views.sum().to_numpy()
    np.testing.assert_array_equal(monthly.selected_title_views, direct)
    OUTPUT.mkdir(exist_ok=True)
    daily.to_csv(OUTPUT / "wikipedia_title_days.csv", float_format="%.8f")
    monthly.to_csv(OUTPUT / "wikipedia_months.csv", index=False, float_format="%.8f")
    (OUTPUT / "measurement.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
