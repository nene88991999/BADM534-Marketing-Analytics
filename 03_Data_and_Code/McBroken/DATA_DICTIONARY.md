# McBroken Teaching Data Dictionary

The underlying field `is_broken` records the source's availability status. In the course calculations, one means **recorded order unavailability** and zero means recorded availability. A missing record has unknown status. Mechanical failure, cleaning, inventory, closure, and ordering-system problems can produce different mechanisms behind the same recorded outcome.

## Daily US Calendar

`data/daily_us.csv` has one row per UTC calendar date from October 25, 2025, through October 24, 2026.

| Variable | Definition |
| --- | --- |
| `date` | Selected snapshot's calendar date in UTC. |
| `snapshot_utc` | Time the selected archive commit was recorded, not a technician inspection or necessarily the collection time. |
| `sha` | Full archive commit identifier; the source is `https://github.com/MrFlynn/mcbroken-archive/blob/SHA/mcbroken.json`. |
| `n_checked` | Number of US records in the supplied extracted snapshot; blank if there is no US observation. |
| `n_broken` | Number of those records with `is_broken = 1`. |
| `share_unavailable` | `n_broken / n_checked`, a fraction from zero to one. |
| `offset_hours` | Commit time minus 18:00 UTC on the same date, measured in hours. |

The daily coverage program reports equal-day means and pooled record fractions. The thresholds 1,000, 2,000, and 5,000 are imposed sensitivity choices. They do not establish representativeness or identify the reason for a sparse snapshot. The nine missing US dates remain blank, including when another country was observed.

## Next-Day Transitions

`data/transitions.csv` has one row per target date and previous-status group with eligible origins. The origin is the preceding calendar date. Both origin and scored target snapshots require at least 2,000 US records and an absolute offset of no more than three hours from 18:00 UTC. Same-key matches use exact next calendar dates. They retain the original address keys; no full-year coordinate merging occurs.

| Variable | Definition |
| --- | --- |
| `date` | Target UTC calendar date. |
| `previous_unavailable` | Origin status, zero or one. |
| `n_origins` | Eligible origin records in this previous-status group, including those with missing targets. Origins after the source's final evaluation horizon are excluded. |
| `n_labeled` | Origins matched to the same key in a usable next-day target snapshot. |
| `n_unavailable` | Matched targets with unavailability status one. |

`n_unavailable <= n_labeled <= n_origins`. A zero unavailable count with zero labels does not imply availability. `n_unavailable / n_labeled` is undefined in that case. Forecast scoring weights by `n_labeled` and ignores the unavailable target status of unmatched origins while reporting their count. The model is estimated on target dates before August 1, 2026; later target dates form the test set. Full-year `n_days` and `last_seen` are excluded from features.

## Policy Window

`data/policy_window.csv` retains the selected weekly snapshots for USA, Canada (`CA`), and UK in event weeks -12 through +12 around October 28, 2024. It includes source commit timestamps, UTC dates, ISO week labels, short `commit` and full `sha`, country, counts, exact `share_unavailable`, and `event_week`. Values are fractions before the program converts them to percentages. Week zero is visible in the figure and excluded from pre/post means. The mean weights each common week equally, after requiring at least 2,000 records for USA and 500 for each comparison country.

## Audit and Provenance

`data/audit.json` records source row counts, duplicate and unmatched-key checks, reconciliation results, coverage, address/coordinate diagnostics, gap counts, and the scope of the status audit. `manifest.json` identifies the six supplied source files by SHA-256 and byte size. The imported snapshot manifest contains selected commits even when their source extraction yields no usable US rows; this is why a manifest count and a panel date count can differ.

The original extractor uses Boolean conversion and a permissive number parser. The course's `api_checks.py` demonstrates stricter handling on constructed inputs. Two pinned raw snapshots were independently checked for nonboolean/missing US statuses and for agreement with supplied US totals. This spot check does not validate every historical JSON field or the underlying order-attempt mechanism.
