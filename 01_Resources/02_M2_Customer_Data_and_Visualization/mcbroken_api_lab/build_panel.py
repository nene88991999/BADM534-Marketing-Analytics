#!/usr/bin/env python3
"""Build a time-series panel of McDonald's ice-cream-machine outages from the McBroken archive.

The live McBroken endpoint only tells you about *now*. For anything over time (trends,
seasonality, before/after an event) you need snapshots. MrFlynn/mcbroken-archive is a
"git scraping" repository: a GitHub Actions job downloads markers.json several times a
day and commits it, so the git history *is* the time series (60,000+ commits since
October 2020). This script walks that history and writes tidy CSVs.

Usage
-----
    python build_panel.py --since 2025-10-24 --until 2026-10-24 --freq daily  --tag daily_1y
    python build_panel.py --since 2020-10-24 --until 2026-10-24 --freq weekly --tag weekly_6y --no-store-panel

Options
-------
    --hour-utc 18        pick, for each day/week, the commit closest to this UTC hour (18 UTC = 1 pm Central)
    --store-states IL    which US states get a store-level panel (comma list, 'all', or 'none')
    --repo PATH          existing clone to reuse; by default a blob-less clone is made in ~/.cache

How the archive snapshot is defined
-----------------------------------
Each commit holds only the stores McBroken re-checked in the previous ~60 minutes
(the archive's own filter), so the number of stores per snapshot varies (roughly
15,000-25,000 of the ~30,000 tracked). Shares are therefore "share of stores checked
in that hour", and a store-day panel has gaps. Both are normal for scraped data and
worth discussing in class before anyone fits a model.

Requires git on PATH. Blobs are fetched lazily, one per snapshot (about 1 MB each).
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import subprocess
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fetch_mcbroken import flatten  # noqa: E402

ARCHIVE_URL = "https://github.com/MrFlynn/mcbroken-archive"


def git(repo: Path, *args: str, binary: bool = False) -> bytes | str:
    r = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, check=True)
    return r.stdout if binary else r.stdout.decode()


def ensure_repo(path: Path | None) -> Path:
    if path and (path / ".git").exists():
        return path
    cache = path or Path.home() / ".cache" / "mcbroken-archive"
    if not (cache / ".git").exists():
        print(f"cloning {ARCHIVE_URL} (commits only, no blobs) into {cache} ...", file=sys.stderr)
        cache.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["git", "clone", "--quiet", "--filter=blob:none", "--no-checkout", ARCHIVE_URL, str(cache)], check=True)
    else:
        subprocess.run(["git", "-C", str(cache), "fetch", "--quiet"], check=False)
    return cache


def pick_commits(repo: Path, since: str, until: str, freq: str, hour_utc: int) -> pd.DataFrame:
    """One commit per day (or ISO week): the one closest to ``hour_utc``."""
    log = git(repo, "log", "--format=%H %cI", f"--since={since}T00:00:00Z", f"--until={until}T23:59:59Z", "origin/main")
    rows = [line.split() for line in log.splitlines() if line.strip()]
    c = pd.DataFrame(rows, columns=["sha", "ts"])
    c["ts"] = pd.to_datetime(c["ts"], utc=True)
    c["period"] = c["ts"].dt.strftime("%G-W%V") if freq == "weekly" else c["ts"].dt.strftime("%Y-%m-%d")
    c["dist"] = (c["ts"].dt.hour * 60 + c["ts"].dt.minute - hour_utc * 60).abs()
    if freq == "weekly":                       # prefer Mondays, then nearest hour
        c["dist"] += c["ts"].dt.weekday * 1440
    return c.sort_values(["period", "dist"]).groupby("period").head(1).sort_values("ts").reset_index(drop=True)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--since", required=True)
    ap.add_argument("--until", default=dt.date.today().isoformat())
    ap.add_argument("--freq", choices=["daily", "weekly"], default="daily")
    ap.add_argument("--hour-utc", type=int, default=18)
    ap.add_argument("--tag", default=None, help="file-name prefix (default: <freq>_<since>_<until>)")
    ap.add_argument("--out", default="data")
    ap.add_argument("--repo", type=Path, default=None)
    ap.add_argument("--store-states", default="IL", help="US states for the store-level panel: comma list, 'all' or 'none'")
    ap.add_argument("--no-store-panel", action="store_true")
    a = ap.parse_args()

    repo = ensure_repo(a.repo)
    commits = pick_commits(repo, a.since, a.until, a.freq, a.hour_utc)
    tag = a.tag or f"{a.freq}_{a.since}_{a.until}"
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    print(f"{len(commits)} snapshots selected ({a.freq}, nearest {a.hour_utc:02d}:00 UTC) from {commits['ts'].min()} to {commits['ts'].max()}", file=sys.stderr)

    store_states = None if (a.no_store_panel or a.store_states.lower() == "none") else (
        None if a.store_states.lower() == "all" else {s.strip().upper() for s in a.store_states.split(",")})
    keep_store_rows = not (a.no_store_panel or a.store_states.lower() == "none")

    country_rows, state_rows, store_frames = [], [], []
    for i, c in commits.iterrows():
        try:
            raw = git(repo, "show", f"{c.sha}:mcbroken.json", binary=True)
            features = json.loads(raw)
        except subprocess.CalledProcessError:
            print(f"[skip] {c.sha[:8]} {c.ts}: no mcbroken.json in this commit", file=sys.stderr)
            continue
        except json.JSONDecodeError:
            print(f"[skip] {c.sha[:8]} {c.ts}: unreadable JSON", file=sys.stderr)
            continue
        if isinstance(features, dict):
            features = features.get("features", [])
        df = flatten(features, c.ts.isoformat())
        df = df[df["is_active"]]
        if df.empty:
            print(f"[skip] {c.sha[:8]} {c.ts}: empty snapshot", file=sys.stderr)
            continue
        snap = {"snapshot_utc": c.ts.isoformat(), "date": c.ts.strftime("%Y-%m-%d"), "period": c.period, "commit": c.sha[:12]}

        g = df.groupby("country", dropna=False)["is_broken"].agg(n_checked="size", n_broken="sum").reset_index()
        for r in g.itertuples(index=False):
            country_rows.append({**snap, "country": r.country, "n_checked": int(r.n_checked), "n_broken": int(r.n_broken)})
        us = df[df["country"] == "USA"]
        g = us.groupby("state", dropna=False)["is_broken"].agg(n_checked="size", n_broken="sum").reset_index()
        for r in g.itertuples(index=False):
            state_rows.append({**snap, "country": "USA", "state": r.state, "n_checked": int(r.n_checked), "n_broken": int(r.n_broken)})
        if keep_store_rows:
            sel = us if store_states is None else us[us["state"].isin(store_states)]
            s = sel[["store_id", "state", "city", "street", "lat", "lon", "is_broken", "last_checked_min"]].copy()
            s.insert(0, "date", snap["date"])
            store_frames.append(s)
        if (i + 1) % 25 == 0 or i + 1 == len(commits):
            print(f"  {i + 1}/{len(commits)}  {c.ts:%Y-%m-%d}  stores={len(df):,}  US broken={us['is_broken'].mean():.1%}", file=sys.stderr)

    country = pd.DataFrame(country_rows)
    country["share_broken"] = (country["n_broken"] / country["n_checked"]).round(4)
    country.to_csv(out / f"mcbroken_{tag}_country.csv", index=False)
    state = pd.DataFrame(state_rows)
    state["share_broken"] = (state["n_broken"] / state["n_checked"]).round(4)
    state.to_csv(out / f"mcbroken_{tag}_us_state.csv", index=False)
    print(f"wrote {out / f'mcbroken_{tag}_country.csv'} ({len(country):,} rows) and ..._us_state.csv ({len(state):,} rows)", file=sys.stderr)
    if store_frames:
        # Two tables, as in a database: a store dimension (one row per store) and a long panel keyed by a
        # short integer, which keeps the panel about ten times smaller than repeating the address on every row.
        stores = pd.concat(store_frames, ignore_index=True)
        dim = (stores.groupby("store_id", sort=True)
                     .agg(state=("state", "first"), city=("city", "first"), street=("street", "first"),
                          lat=("lat", "first"), lon=("lon", "first"), n_days=("date", "nunique"),
                          first_seen=("date", "min"), last_seen=("date", "max"))
                     .reset_index())
        dim.insert(0, "store_key", range(1, len(dim) + 1))
        panel = stores.merge(dim[["store_id", "store_key"]], on="store_id")[["date", "store_key", "is_broken", "last_checked_min"]]
        panel["is_broken"] = panel["is_broken"].astype(int)
        panel = panel.sort_values(["date", "store_key"])
        label = "us" if store_states is None else "_".join(sorted(store_states))
        dim.to_csv(out / f"mcbroken_{tag}_stores_{label}_dim.csv", index=False)
        p = out / (f"mcbroken_{tag}_stores_{label}_panel.csv" + (".gz" if len(panel) > 400_000 else ""))
        panel.to_csv(p, index=False)
        print(f"wrote {p} ({len(panel):,} store-day rows) and ..._dim.csv ({len(dim):,} stores)", file=sys.stderr)
    commits.drop(columns="dist").to_csv(out / f"mcbroken_{tag}_snapshots_used.csv", index=False)


if __name__ == "__main__":
    main()
