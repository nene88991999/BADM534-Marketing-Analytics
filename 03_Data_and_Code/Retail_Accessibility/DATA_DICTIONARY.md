# Retail Accessibility Data Dictionary

## Observed Inputs

`data/restaurants.csv` has one row for each of four restaurant keys observed on October 24, 2026 within latitudes 40.06 to 40.16 and longitudes -88.33 to -88.17. The status field is `available = 1 - is_broken` from the supplied extraction. Both limits are inclusive. Restaurant records outside the selected box and absent records are excluded before forming the four-origin denominator.

| Field | Meaning and Units |
| --- | --- |
| `store_key` | Preserved source identifier; not a row number or coordinate match |
| `date` | Snapshot date, YYYY-MM-DD |
| `lat`, `lon` | Restaurant latitude and longitude in decimal degrees |
| `available` | 1 for recorded order availability; 0 for recorded unavailability |
| `street`, `city` | Location labels from the supplied store table |
| `snapshot_utc` | Source snapshot timestamp in UTC |
| `archive_sha` | Source archive Git commit containing the snapshot |

`data/osm_highways.json.gz` is compressed JSON with `elements` containing 34,568 highway ways and 125,226 referenced nodes. Node coordinates are decimal degrees; ways list ordered node IDs and tags. This is the retained query response, before course graph filters. `data/manifest.json` records the source date, query, bounding boxes, source SHA-256, frozen input hashes, time-alignment scope, and rights.

The network bounding box spans latitudes 40.08 to 40.155 and longitudes -88.30 to -88.185. The calculation retains only segments with both endpoints in the box. It retains residential, living-street, pedestrian, footway, path, steps, service, unclassified, primary, secondary, and tertiary ways, including specified road links. Areas and ways marked unavailable to foot travel are excluded. `access=no/private` is excluded unless an explicit allowed foot tag overrides it. Unspecified foot access is accepted for the listed classes as a modeling assumption. Edges are undirected. The graph has 109,694 nodes, 129,310 edges, and 622 connected components. All four snapped origins lie in its 104,584-node largest component.

Distances use a spherical Earth radius of 6,371.0088 km. Each origin and target is snapped to the closest retained node; its straight connector enters total network distance. The maximum permitted snap is 200 m. Actual snaps range from 11.3 to 20.6 m. Graph boundaries, missing ways, access assumptions, and connector geometry affect the comparison. Paths outside the box and unobserved alternatives are absent.

## Synthetic Inputs

| Origin | Coordinates | People | Store and Baseline Availability |
| --- | --- | --- | --- |
| W0 | (0,0) | 100 | A: unavailable |
| W1 | (0,2) | 300 | No store |
| W2 | (0,4) | 100 | C: available |
| E0 | (1,0) | 50 | B: available |
| E1 | (1,2) | 50 | No store |
| E2 | (1,4) | 50 | D: unavailable |
| X | (4,0) | 150 | U: unknown |

The graph has edges W0-W1, W1-W2, E0-E1, and E1-E2 taking four minutes each, plus W2-E2 taking two minutes. X is isolated. Straight-line proxy minutes equal twice Euclidean coordinate distance. Schematic figure spacing is not a distance scale. Access means a minimum time of at most five minutes to an available store, including a store at the origin. All population rows enter the denominator, including X. Known-store unavailability uses four known-status stores as its separate denominator.

The map-footprint example has four corner nodes on a two-kilometer square, with two minutes per edge. Its square-corner corridor extends 0.1 km on each side of the graph perimeter. Outer area is 2.2 squared and inner area is 1.8 squared. The difference, 1.60 square kilometers, is the corridor footprint. Filling the center yields 4.84 square kilometers without adding a node or route.

## Outputs

| File | Observation Unit and Fields |
| --- | --- |
| `synthetic_origins.csv` | Origin-policy pair, 21 rows; people, nearest known/possible minutes, lower/upper reachability indicators |
| `policies.csv` | Baseline or one-store restoration, 3 rows; lower/upper counts and shares, imposed incremental weekly profit in dollars, known-store unavailable share |
| `neighbors.csv` | Directed origin-target pair selected under a metric and k; six connected origins, k in {1,2} |
| `neighbor_comparison.csv` | One row per k; directed and common edge counts, mean network travel along each selected graph |
| `synthetic_summary.json` | Synthetic input scope and population totals, policy comparisons, neighbor summaries |
| `observed_pairs.csv` | Ordered pair of distinct restaurants, 12 rows; great-circle and modeled-network distances in km, target availability |
| `observed_origins.csv` | Restaurant origin, 4 rows; snap distance in m, snapped node, eligible target count, nearest target and distance for each metric |
| `observed_summary.json` | Dates, graph size, origin denominator, threshold counts, and interpretation scope |
| `cartography.json` | Imposed graph and geometry results; reachable-node counts and square-kilometer areas |

Blank nearest distances in the synthetic CSV mean no eligible reachable store. They do not mean zero minutes. Unknown status remains distinct from known unavailability. Lower and upper shares describe completed-status scenarios; no sampling interval, causal effect, or measured customer substitution is estimated.
