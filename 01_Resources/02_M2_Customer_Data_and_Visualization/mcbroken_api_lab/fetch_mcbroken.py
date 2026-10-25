#!/usr/bin/env python3
"""Collect McDonald's ice-cream-machine status from McBroken (https://mcbroken.com).

BADM 534 lab: calling a public JSON endpoint, handling the response, and turning
nested JSON into a tidy table.

Usage
-----
    python fetch_mcbroken.py                      # live call, saves raw JSON + CSV to ./data
    python fetch_mcbroken.py --source archive     # same file, but from the public-domain GitHub archive
    python fetch_mcbroken.py --from-file mcbroken.json
    python fetch_mcbroken.py --out ../data --quiet

What the script does
--------------------
1. Sends an HTTP GET request for ``markers.json`` (one record per restaurant) and
   ``stats.json`` (city league table) with a User-Agent header that says who we are.
2. Checks the status code, decodes gzip if the server sends compressed bytes, and
   parses the JSON.
3. Flattens the GeoJSON ``FeatureCollection`` into a pandas DataFrame, one row per store.
4. Saves a timestamped raw copy (so the analysis can be re-run later) and a CSV.

Notes for students
------------------
* McBroken has no documented API and no terms-of-use page. ``markers.json`` is the
  file the website itself loads, so one request per session is the same load as
  opening the site. Do not loop over it in a tight loop; one call per class is plenty.
* The underlying facts come from McDonald's own ordering API, observed by the
  McBroken author (Rashiq Zahid). Treat the data as "publicly viewable, no licence":
  fine to analyse and cite, not something to re-publish as your own dataset.
* The GitHub archive (MrFlynn/mcbroken-archive) re-publishes hourly snapshots under
  the Unlicense. It is reachable from most campus and corporate networks even when
  mcbroken.com is not, so it is the fallback here.
"""
from __future__ import annotations

import argparse
import datetime as dt
import gzip
import json
import re
import sys
from pathlib import Path

import pandas as pd
import requests

LIVE_MARKERS = "https://mcbroken.com/markers.json"
LIVE_STATS = "https://mcbroken.com/stats.json"
ARCHIVE_MARKERS = "https://raw.githubusercontent.com/MrFlynn/mcbroken-archive/main/mcbroken.json"
USER_AGENT = "BADM534-marketing-analytics-lab/1.0 (University of Illinois; course use; contact instructor)"
TIMEOUT = 30  # seconds; never leave a request without a timeout


# --------------------------------------------------------------------------- HTTP

def get_json(url: str, session: requests.Session | None = None) -> tuple[object, dict]:
    """GET ``url`` and return (parsed_json, metadata).

    Handles two things beginners usually miss:
    * non-200 status codes (``raise_for_status`` turns them into exceptions), and
    * gzip bytes served without a ``Content-Encoding`` header (McBroken does this;
      the archive's workflow pipes the download through ``gunzip`` for the same reason).
    """
    s = session or requests.Session()
    headers = {"User-Agent": USER_AGENT, "Accept": "application/json", "Accept-Encoding": "gzip"}
    t0 = dt.datetime.now(dt.timezone.utc)
    r = s.get(url, headers=headers, timeout=TIMEOUT)
    r.raise_for_status()                      # 4xx / 5xx -> requests.HTTPError
    raw = r.content
    if raw[:2] == b"\x1f\x8b":                # gzip magic number
        raw = gzip.decompress(raw)
    data = json.loads(raw)
    meta = {
        "url": url,
        "status_code": r.status_code,
        "fetched_at_utc": t0.isoformat(timespec="seconds"),
        "bytes": len(raw),
        "content_type": r.headers.get("Content-Type"),
        "content_encoding": r.headers.get("Content-Encoding"),
        "elapsed_s": round(r.elapsed.total_seconds(), 2),
    }
    return data, meta


def load_markers(source: str = "auto", path: str | None = None) -> tuple[list, dict]:
    """Return (features, meta). ``source`` is 'live', 'archive', 'file' or 'auto'.

    'auto' tries the live endpoint, then the GitHub archive. Each step is reported so
    you can see which one actually produced the data.
    """
    if source == "file" or path:
        p = Path(path or "mcbroken.json")
        data = json.loads(p.read_text())
        meta = {"url": str(p), "fetched_at_utc": dt.datetime.fromtimestamp(p.stat().st_mtime, dt.timezone.utc).isoformat(timespec="seconds"), "source": "file"}
        return _features(data), meta
    order = {"live": [LIVE_MARKERS], "archive": [ARCHIVE_MARKERS], "auto": [LIVE_MARKERS, ARCHIVE_MARKERS]}[source]
    errors = []
    for url in order:
        try:
            data, meta = get_json(url)
            meta["source"] = "live" if url == LIVE_MARKERS else "archive"
            return _features(data), meta
        except Exception as e:  # noqa: BLE001 - we want to report and move on
            errors.append(f"{url}: {type(e).__name__}: {e}")
            print(f"[warn] {errors[-1]}", file=sys.stderr)
    raise RuntimeError("Could not load markers from any source:\n  " + "\n  ".join(errors))


def _features(data) -> list:
    """Live file is a GeoJSON FeatureCollection; the archive stores the bare feature list."""
    if isinstance(data, dict) and "features" in data:
        return data["features"]
    if isinstance(data, list):
        return data
    raise ValueError("Unexpected JSON shape: expected FeatureCollection or list of features")


# --------------------------------------------------------------------------- tidy

_MINUTES = re.compile(r"(\d+)")


def flatten(features: list, fetched_at_utc: str | None = None) -> pd.DataFrame:
    """One row per store. Keeps every property, adds coordinates and a parsed check time."""
    rows = []
    for f in features:
        p = f.get("properties", {})
        lon, lat = (f.get("geometry", {}).get("coordinates") or [None, None])[:2]
        m = _MINUTES.search(p.get("last_checked", "") or "")
        rows.append({
            # Early snapshots (2020-21) have no country field: McBroken then covered the US only.
            "country": p.get("country") or "USA",
            "state": p.get("state"),
            "city": p.get("city"),
            "street": p.get("street"),
            "lat": lat,
            "lon": lon,
            "is_broken": bool(p.get("is_broken")),
            "is_active": bool(p.get("is_active")),
            "dot": p.get("dot"),
            "last_checked_min": int(m.group(1)) if m else None,
        })
    base_cols = ["country", "state", "city", "street", "lat", "lon", "is_broken", "is_active", "dot", "last_checked_min"]
    df = pd.DataFrame(rows, columns=base_cols)              # explicit columns so an empty snapshot still has a schema
    df["lat"] = pd.to_numeric(df["lat"], errors="coerce")   # old snapshots store coordinates as strings
    df["lon"] = pd.to_numeric(df["lon"], errors="coerce")
    # A stable key for a store: McBroken publishes no ID, so use the address + rounded location.
    df["store_id"] = (
        df["country"].fillna("") + "|" + df["state"].fillna("") + "|" + df["city"].fillna("")
        + "|" + df["street"].fillna("") + "|" + df["lat"].round(4).astype(str) + "," + df["lon"].round(4).astype(str)
    )
    if fetched_at_utc:
        t = pd.Timestamp(fetched_at_utc)
        df["checked_at_utc"] = t - pd.to_timedelta(df["last_checked_min"].fillna(0), unit="min")
    cols = ["store_id", "country", "state", "city", "street", "lat", "lon", "is_broken", "is_active", "dot", "last_checked_min"]
    if fetched_at_utc:
        cols.append("checked_at_utc")
    return df[cols]


def summarise(df: pd.DataFrame, top: int = 10) -> pd.DataFrame:
    """Share of checked stores reporting a broken machine, by country/state."""
    g = (df.groupby(["country", "state"], dropna=False)
           .agg(n_checked=("is_broken", "size"), n_broken=("is_broken", "sum"))
           .reset_index())
    g["share_broken"] = (g["n_broken"] / g["n_checked"]).round(4)
    return g.sort_values("n_checked", ascending=False).head(top) if top else g


# --------------------------------------------------------------------------- main

def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--source", choices=["auto", "live", "archive"], default="auto")
    ap.add_argument("--from-file", dest="path", help="read a saved markers.json / mcbroken.json instead of downloading")
    ap.add_argument("--out", default="data", help="output folder (default ./data)")
    ap.add_argument("--no-stats", action="store_true", help="skip stats.json")
    ap.add_argument("--no-raw", action="store_true", help="do not keep the raw JSON (about 10 MB per snapshot)")
    ap.add_argument("--gzip", action="store_true", help="write the CSV gzip-compressed (for scheduled daily snapshots)")
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()

    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)

    features, meta = load_markers("file" if a.path else a.source, a.path)
    stamp = meta["fetched_at_utc"].replace(":", "").replace("-", "")[:15]
    df = flatten(features, meta["fetched_at_utc"])

    raw_path = out / f"markers_raw_{stamp}.json"
    if not a.no_raw:
        raw_path.write_text(json.dumps(features))
    csv_path = out / (f"mcbroken_snapshot_{stamp}.csv" + (".gz" if a.gzip else ""))
    df.to_csv(csv_path, index=False)
    (out / f"markers_meta_{stamp}.json").write_text(json.dumps(meta, indent=1))

    if not a.no_stats and not a.path:
        try:
            stats, smeta = get_json(LIVE_STATS)
            (out / f"stats_{stamp}.json").write_text(json.dumps(stats, indent=1))
            if not a.quiet:
                print(f"stats.json: overall broken share {stats.get('broken')}% across {len(stats.get('cities', []))} listed cities")
        except Exception as e:  # noqa: BLE001
            print(f"[warn] stats.json not available: {type(e).__name__}: {e}", file=sys.stderr)

    if not a.quiet:
        print(f"source: {meta['source']}  ({meta['url']})  fetched {meta['fetched_at_utc']}")
        print(f"stores: {len(df):,}   broken: {df['is_broken'].mean():.1%}   countries: {df['country'].nunique()}")
        us = df[df["country"] == "USA"]
        if len(us):
            print(f"USA: {len(us):,} stores checked in the last hour, {us['is_broken'].mean():.1%} broken")
            print(summarise(us, top=10).to_string(index=False))
        print(f"saved: {csv_path}" + ("" if a.no_raw else f"  and  {raw_path}"))


if __name__ == "__main__":
    main()
