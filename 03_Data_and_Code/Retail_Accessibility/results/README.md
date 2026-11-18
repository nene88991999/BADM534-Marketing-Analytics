# Retail Access Results

The reference calculations were executed on November 18, 2026 using Python 3.13.5 and NetworkX 3.4.2. [Input definitions and commands](../README.md), [field definitions](../DATA_DICTIONARY.md), and [verification hashes](../verification.json) accompany the results.

| Synthetic Policy | Known Access / 800 | Possible Access / 800 | Imposed Weekly Profit Gain |
| --- | --- | --- | --- |
| Baseline | 550 (68.75%) | 700 (87.50%) | $0 |
| Restore A | 650 (81.25%) | 800 (100%) | $20 |
| Restore D | 550 (68.75%) | 700 (87.50%) | $40 |

All graph times, population weights, thresholds, and profit gains are imposed. The unknown status at isolated X creates the bound width. A and D produce the same known-store availability fraction. D shortens some trips even though it adds no people under the five-minute threshold.

| Observed Restaurant Origin | Nearest by Straight Line | Distance (km) | Nearest on Modeled Network | Distance (km) |
| --- | --- | --- | --- | --- |
| South Neil | Mattis | 3.751 | Mattis | 5.021 |
| North Neil | Mattis | 3.478 | South Neil | 4.757 |
| Mattis | South Neil | 3.751 | South Neil | 5.021 |
| Cunningham | South Neil | 4.161 | South Neil | 5.499 |

The four observed origins are equally weighted. Targets are other recorded available restaurants of the same chain in the selected October 24 snapshot. The November 18 OpenStreetMap extract supplies an illustrative undirected network with straight snapping connectors. These results do not measure customer travel, all possible substitutes, or historical pedestrian routes. © OpenStreetMap contributors, [ODbL 1.0](https://opendatacommons.org/licenses/odbl/1-0/).

The map-footprint calculation increases shaded area from 1.60 to 4.84 square kilometers by filling a hole, with four reachable graph nodes before and after. The center retains no modeled route. Neighbor graphs use the same six connected nodes and the same k. At k=1 only two of six directed links coincide across distance definitions; at k=2 eight of twelve coincide.

The four TikZ figures describe, respectively, a bridge-induced distance difference, unchanged reachability under area filling, lower and upper access under restoration, and paired distances for observed restaurant origins. Exact tables support every plotted comparison. The course scripts ran; upstream city2graph and GNN programs did not.
