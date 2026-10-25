"""Audit supplied McBroken tables and build aggregate, offline teaching inputs."""
import argparse
import hashlib
import json
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent
DEFAULT_SOURCE = (ROOT.parents[1] / "01_Resources" /
                  "02_M2_Customer_Data_and_Visualization/mcbroken_api_lab/data")
PREFIX = "mcbroken_daily_2025-10_2026-10_"


def validate_panel(panel, dimension):
    if panel.duplicated(["date", "store_key"]).any():
        raise ValueError("Duplicate store-date records")
    if dimension.store_key.duplicated().any():
        raise ValueError("Duplicate dimension keys")
    if not panel.is_broken.isin([0, 1]).all():
        raise ValueError("Missing or nonbinary status")
    if not panel.store_key.isin(dimension.store_key).all():
        raise ValueError("Unmatched store key")
    if not panel.last_checked_min.between(0, 60).all():
        raise ValueError("Check age outside the supplied archive's range")


def make_transitions(panel, daily):
    """Match exact next calendar dates; retain the count of unlabeled origins."""
    good = daily.n_checked.ge(2000) & daily.offset_hours.abs().le(3)
    origin = panel[panel.date.isin(daily.loc[good, "date"])].copy()
    origin["date"] += pd.Timedelta(days=1)
    origin = origin[origin.date.le(daily.date.max())]
    origin = origin.rename(columns={"is_broken": "previous_unavailable"})
    target = panel[panel.date.isin(daily.loc[good, "date"])][
        ["date", "store_key", "is_broken"]]
    pairs = origin.merge(target, on=["date", "store_key"], how="left",
                         validate="one_to_one")
    return (pairs.groupby(["date", "previous_unavailable"]).is_broken
            .agg(n_origins="size", n_labeled="count", n_unavailable="sum")
            .reset_index())


def main(source):
    source = Path(source)
    used = []
    def read(name, **kwargs):
        path = source / name
        used.append(path)
        return pd.read_csv(path, **kwargs)

    panel = read(PREFIX + "stores_us_panel.csv.gz", parse_dates=["date"])
    dim = read(PREFIX + "stores_us_dim.csv")
    country = read(PREFIX + "country.csv", parse_dates=["date"])
    snaps = read(PREFIX + "snapshots_used.csv")
    weekly = read("mcbroken_weekly_2020_2026_country.csv", parse_dates=["date"])
    weekly_snaps = read("mcbroken_weekly_2020_2026_snapshots_used.csv")
    validate_panel(panel, dim)
    us = country[country.country.eq("USA")].copy()
    if us.date.duplicated().any():
        raise ValueError("Duplicate US snapshot dates")
    actual = panel.groupby("date").is_broken.agg(n_checked="size", n_broken="sum")
    pd.testing.assert_frame_equal(actual.sort_index(),
        us.set_index("date")[["n_checked", "n_broken"]].sort_index(),
        check_dtype=False, check_freq=False)
    days = panel.groupby("store_key").date.nunique()
    pd.testing.assert_series_equal(days.sort_index(),
        dim.set_index("store_key").n_days.sort_index(), check_names=False)
    snaps["snapshot_utc"] = pd.to_datetime(snaps.ts, utc=True)
    snaps["date"] = snaps.snapshot_utc.dt.tz_localize(None).dt.normalize()
    if snaps.date.duplicated().any():
        raise ValueError("Multiple selected snapshots per calendar date")
    daily = pd.DataFrame({"date": pd.date_range(snaps.date.min(), snaps.date.max())})
    daily = daily.merge(snaps[["date", "snapshot_utc", "sha"]], on="date",
                        how="left", validate="one_to_one")
    daily = daily.merge(us[["date", "n_checked", "n_broken"]], on="date",
                        how="left", validate="one_to_one")
    daily["share_unavailable"] = daily.n_broken / daily.n_checked
    target = daily.date.dt.tz_localize("UTC") + pd.Timedelta(hours=18)
    daily["offset_hours"] = (daily.snapshot_utc - target).dt.total_seconds() / 3600
    transitions = make_transitions(panel, daily)
    for col in ["n_origins", "n_labeled", "n_unavailable"]:
        transitions[col] = transitions[col].astype(int)
    assert (transitions.n_unavailable <= transitions.n_labeled).all()
    assert (transitions.n_labeled <= transitions.n_origins).all()

    ordered = panel.sort_values(["store_key", "date"])
    gaps = ordered.groupby("store_key").date.diff().dt.days
    event = pd.Timestamp("2024-10-28")
    weekly["event_week"] = (weekly.date - event).dt.days // 7
    event_data = weekly[weekly.event_week.between(-12, 12)
                        & weekly.country.isin(["USA", "UK", "CA"])].copy()
    event_data = event_data.merge(weekly_snaps[["period", "sha"]], on="period",
                                  validate="many_to_one")
    assert event_data.commit.eq(event_data.sha.str[:12]).all()
    event_data["share_unavailable"] = event_data.n_broken / event_data.n_checked
    out = ROOT / "data"
    out.mkdir(exist_ok=True)
    daily.to_csv(out / "daily_us.csv", index=False)
    transitions.to_csv(out / "transitions.csv", index=False)
    event_data.drop(columns="share_broken").to_csv(out / "policy_window.csv", index=False)
    audit = {
        "source_rows": len(panel), "address_keys": len(dim),
        "exact_coordinate_pairs": len(dim[["lat", "lon"]].drop_duplicates()),
        "calendar_days": len(daily), "us_observed_days": len(us),
        "missing_us_days": int(daily.n_checked.isna().sum()),
        "low_coverage_days": int(daily.n_checked.lt(2000).sum()),
        "successive_key_records": int(gaps.notna().sum()),
        "consecutive_day_pairs": int(gaps.eq(1).sum()),
        "long_gap_pairs": int(gaps.gt(1).sum()),
        "median_days_per_key": float(dim.n_days.median()),
        "snapshot_abs_offset_hours_max": float(daily.offset_hours.abs().max()),
        "duplicate_store_dates": 0, "unmatched_keys": 0,
        "country_counts_reconciled": True, "dimension_days_reconciled": True,
        "matching": "Original address keys; coordinates are an audit, not a merge rule.",
        "transition_screen": "Both dates: >=2000 US records and within 3 hours of 18:00 UTC.",
        "status_scope": "The supplied binary field was validated; raw API missingness cannot be recovered from these CSVs.",
    }
    (out / "audit.json").write_text(json.dumps(audit, indent=2) + "\n")
    manifest = {
        "source": "Rashiq Zahid, McBroken; snapshots via MrFlynn/mcbroken-archive",
        "urls": ["https://mcbroken.com", "https://github.com/MrFlynn/mcbroken-archive"],
        "files": {p.name: {"sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
                            "bytes": p.stat().st_size} for p in used},
        "rights": "Upstream archive software uses Unlicense; no separate McBroken data license was established. Public teaching outputs are attributed aggregate calculations.",
    }
    (ROOT / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps(audit, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    main(parser.parse_args().source)
