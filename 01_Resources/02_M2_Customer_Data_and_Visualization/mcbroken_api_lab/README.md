# McBroken API lab: collecting public data with Python

The [verified course adaptation](../../../03_Data_and_Code/McBroken/README.md) supplies the executed examples used in the lecture notes. Read the [adaptation review](COURSE_ADAPTATION.md) for the policy-date correction, parser checks, measurement distinctions, and verification scope. The files below are the supplied source collection.

A worked example of pulling public data from a JSON endpoint, tidying it, and turning a live feed into a time series. The subject is McDonald's ice-cream machines, as tracked by [McBroken](https://mcbroken.com), which makes the mechanics memorable without being trivial: the data are real, messy, geographic, and change by the hour.

Module fit: **M2 (Customer Data and Visualization)** for the API and tidying work; **M6 (Causal Models and Experiments)** for the right-to-repair event study in the exercises; the AI-coding thread throughout (exercise 1 has students audit assistant-written request code).

## Files

| File | What it is |
|---|---|
| `mcbroken_api_lab.ipynb` | The lab, executed, with outputs. Start here. |
| `fetch_mcbroken.py` | Script and importable module. Calls the live endpoint (falls back to the GitHub archive), flattens GeoJSON to a DataFrame, saves a timestamped raw copy and CSV. |
| `build_panel.py` | Walks the git history of [MrFlynn/mcbroken-archive](https://github.com/MrFlynn/mcbroken-archive) and writes country, state and store panels. |
| `snapshot_mcbroken.yml` | GitHub Actions template: one snapshot a day committed to a repository ("git scraping"). |
| `data/mcbroken_snapshot_*.csv` | One flattened snapshot (one row per store checked in the previous hour). |
| `data/mcbroken_daily_2025-10_2026-10_country.csv` | Daily, one snapshot per day near 18:00 UTC, share broken by country. |
| `data/mcbroken_daily_2025-10_2026-10_us_state.csv` | Same, by US state. |
| `data/mcbroken_daily_2025-10_2026-10_stores_us_dim.csv` | Store dimension table: one row per US store seen during the year (`store_key`, address, lat/lon, days observed). |
| `data/mcbroken_daily_2025-10_2026-10_stores_us_panel.csv.gz` | Store-day panel: `date`, `store_key`, `is_broken` (0/1), `last_checked_min`. About 3 million rows; join to the dimension table on `store_key`. |
| `data/mcbroken_weekly_2020_2026_country.csv`, `..._us_state.csv` | Weekly (Monday nearest 18:00 UTC) from the archive's first commit, October 2020. |
| `data/*_snapshots_used.csv` | Which archive commit (and exact UTC time) each daily or weekly row came from. |

## Quick start

```bash
pip install requests pandas matplotlib
python fetch_mcbroken.py                     # live call; prints a summary, writes ./data
python fetch_mcbroken.py --source archive    # same file from GitHub, for locked-down networks
python build_panel.py --since 2026-08-01 --freq daily --tag demo --store-states IL
jupyter lab mcbroken_api_lab.ipynb
```

`build_panel.py` makes a blob-less clone of the archive (about 17 MB) in `~/.cache/mcbroken-archive` the first time, then fetches one ~1 MB snapshot per selected commit. A year of daily snapshots takes roughly ten minutes.

## Where the numbers come from

```
McDonald's ordering API  --(every few minutes: try to add a sundae to the cart)-->  McBroken
      McBroken  --> https://mcbroken.com/markers.json   (one GeoJSON feature per store, gzip)
                --> https://mcbroken.com/stats.json     (city league table)
      markers.json --(hourly GitHub Actions job, since 2020-10-24)--> MrFlynn/mcbroken-archive (git history)
      fetch_mcbroken.py  <-- markers.json or the archive's current file
      build_panel.py     <-- the archive's commits
```

McBroken was built in October 2020 by software engineer Rashiq Zahid. It marks a machine **broken when the McDonald's app refuses to add an ice-cream item to the cart** for that store. That is the operational definition behind every number here. It also fires when a store is closed, when the item is out of stock, or when the app itself has problems, so read `is_broken` as "ice cream could not be ordered", not as a service record.

The archive keeps, in each commit, only the stores McBroken re-checked in the previous 60 minutes (its own `jq` filter). A typical commit holds 15,000 to 25,000 of the roughly 30,000 tracked stores, so **the denominator of every share is "stores checked in that hour"**, and store-day panels have gaps. The archive's cadence has also changed: about 40 commits a day in late 2020, about 20 a day through 2025, and 4 to 7 a day in 2026, so the "nearest 18:00 UTC" snapshot can be some hours off in recent months. The exact commit time is in `*_snapshots_used.csv`.

## Data dictionary

**Snapshot and store panel** (`mcbroken_snapshot_*.csv`, `*_stores_*.csv`)

| Column | Meaning |
|---|---|
| `store_id` | `country|state|city|street|lat,lon` (4 dp). McBroken publishes no ID; this key is stable as long as the address text does not change. |
| `country` | McBroken's own codes: `USA`, `UK`, `CA`, `AU`, `JP`, `DE`, ... Some are not ISO (`SAR` and `SAJ` appear to be Saudi regions; `IN-SW` is unexplained). Check before merging with other data. |
| `state` | US state or province/region abbreviation as given by McBroken. |
| `city`, `street` | Address as given. |
| `lat`, `lon` | WGS84 coordinates from the GeoJSON geometry. |
| `is_broken` | True if the ice-cream item could not be added to the cart at the last check. |
| `is_active` | True if the store is in McBroken's active list (always True in the archive). |
| `dot` | Map colour: `working` or `broken`. |
| `last_checked_min` | Minutes between the check and the snapshot, parsed from text such as "Checked 12 minutes ago". |
| `checked_at_utc` | Snapshot time minus `last_checked_min`. |
| `date` | (store panel) calendar date (UTC) of the archive commit used; the exact time is in `*_snapshots_used.csv`. |
| `store_key` | (store panel) integer key joining `*_stores_us_panel.csv.gz` to `*_stores_us_dim.csv`. |
| `n_days`, `first_seen`, `last_seen` | (store dimension) how many daily snapshots the store appeared in, and the first and last date. |

**Aggregate panels** (`*_country.csv`, `*_us_state.csv`)

| Column | Meaning |
|---|---|
| `snapshot_utc`, `date`, `period`, `commit` | Commit time, UTC date, day or ISO week label, short commit hash. |
| `country`, `state` | Group. |
| `n_checked` | Stores in the snapshot for that group (the denominator). |
| `n_broken` | Of those, how many were broken. |
| `share_broken` | `n_broken / n_checked`, rounded to 4 dp. |

## Known issues to raise in class

- **Measurement, not mechanics.** `is_broken` is an app response. Store closures, stock-outs and app outages all look like a broken machine. Night-time shares are therefore higher.
- **Changing denominator.** Shares are over stores checked in that hour, and the checking cadence has changed several times. Level shifts in the six-year series are partly measurement changes. Compare within periods, or model the denominator explicitly.
- **No store ID.** The `store_id` key breaks when McBroken edits an address string ("1166 N Muldoon Rd" became "1166 North Muldoon Road" in July 2026, so that Anchorage store has two keys). Expect churn: about 29,000 distinct US keys over a year against roughly 13,500 US McDonald's. Matching on rounded lat/lon alone would merge most of them.
- **Gaps in the store panel.** Because each snapshot holds only the stores checked in the previous hour, a typical store appears in about 110 of the 365 daily snapshots. Treat the store panel as irregularly sampled.
- **Bad snapshots.** A few archive commits contain almost nothing (a failed download that still got committed). Drop days with `n_checked` far below the norm (for the US, under about 2,000) before computing shares.
- **Schema drift.** 2020-21 snapshots have no `country` or `dot` field (McBroken covered the US only; `flatten()` fills `country = "USA"`) and store coordinates as strings. Any script that reads old snapshots directly has to cope with this; `flatten()` does.
- **Time zones.** Everything is UTC. 18:00 UTC is 1 pm Central in summer and noon in winter.
- **Coverage changes.** Countries were added over the years, and in September 2024 Wendy's ran a promotion with McBroken that put Wendy's locations on the map; whether those ever entered `markers.json` is unverified. Watch `n_checked` for jumps before interpreting a change in `share_broken`.

## Terms, etiquette and attribution

- McBroken publishes no terms of use and no data licence. `markers.json` is the file the website itself loads, so one request is the same load as one visit. Treat the raw data as **publicly viewable, not openly licensed**: analyse it, cite it, show it in class, but do not re-publish the raw file as your own dataset. This folder therefore contains derived aggregates and one snapshot, not a mirror.
- The archive repository is released under the Unlicense (public domain) by its author; that covers the repository's code and packaging, not McDonald's underlying facts, whose status does not change by being archived.
- Identify yourself (the `User-Agent` string in `fetch_mcbroken.py`), set a timeout, and do not loop. One call per person per session is plenty; a scheduled job once a day is plenty.
- Cite as: Rashiq Zahid, *McBroken*, https://mcbroken.com (accessed DATE); snapshots via MrFlynn/mcbroken-archive, https://github.com/MrFlynn/mcbroken-archive.

## Suggested 75-minute session

1. (10 min) What an API is; open `stats.json` in a browser; read the response headers in the notebook.
2. (15 min) `markers.json`: nested JSON to a DataFrame; `json_normalize` vs a hand-written `flatten`.
3. (15 min) Share broken by state; the map; what `is_broken` measures and what it does not.
4. (15 min) Git scraping: the archive, `build_panel.py`, the daily and weekly series; the denominator problem.
5. (10 min) Exercise 1 live: students prompt their AI assistant for the fetch function, then audit it against the checklist (timeout, User-Agent, status code, gzip, raw copy).
6. (10 min) Set up exercise 5 (right-to-repair event study) as the bridge to Module 6.

## Background reading

- Simon Willison, *Git scraping: track changes over time by scraping to a Git repository* (2020): https://simonwillison.net/2020/Oct/9/git-scraping/
- NPR, *McDonald's ice cream machines seem to always be broken. Here's why* (2021): https://www.npr.org/transcripts/1059600306
- Nation's Restaurant News, *McDonald's franchisees will now have an easier time repairing ice cream machines* (28 Oct 2024), on the US Copyright Office exemption for commercial food-preparation equipment: https://www.nrn.com/quick-service/mcdonald-s-franchisees-will-now-have-an-easier-time-repairing-ice-cream-machines
- Public Knowledge / iFixit on the same exemption: https://rla.org/media/article/news-and-views/public-knowledge-ifixit-free-mcflurry
- Andy Greenberg, *They Hacked McDonald's Ice Cream Machines, and Started a Cold War* (Wired, 2021), on Kytch and Taylor. Search by title; the site blocks automated access.
- Kaggle has an older community time series of McBroken data (search "McDonald's ice cream machines broken timeseries"); licence varies by uploader, so check before using.

*Built 2026-10-24 for BADM 534 course preparation. Data in `data/` reflect the archive as of that date.*
