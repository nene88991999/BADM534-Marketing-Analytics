# Retail Availability and Customer Access

A service manager choosing which location to restore needs to know whose alternatives improve. A restaurant count gives every location equal weight. Network access depends on origins, route costs, availability, and the population receiving weight. These examples connect [M2 §2.23](../../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md), [M4 §4.22](../../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md), [M5 §§5.21–5.22](../../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md), [M7 §7.28](../../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md), [M8 §8.23](../../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md), and [M9 §9.18.2](../../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md).

## Inputs and Comparisons

`accessibility.py` constructs an entirely synthetic seven-origin network with 800 people and five stores. The only bridge links the northern bank nodes. Four stores have known availability; store U at disconnected origin X has unknown availability. The five-minute threshold, population weights, route times, and profits are imposed. The lower access bound counts only known available stores; the upper bound treats U as available. Both retain all 800 people. The interval describes missing status, with fixed graph and population. It is not a confidence interval.

Known availability yields network access for 550 people, or 68.75%, versus 650 people using the straight-line proxy. Restoring A raises network access to 650; restoring D leaves it at 550. Both actions lower the known-store unavailable fraction from one-half to one-quarter. D still shortens travel for some origins. Equal restoration costs and imposed weekly profit gains of $20 at A and $40 at D create different rankings under profit and five-minute access. The calculation supplies no universal service standard.

The proximity comparison uses the same six connected origins, the same `k`, directed links, and alphabetical tie-breaking. X is excluded only from this neighbor comparison. With `k=1`, each graph has six links and two are shared. Straight-line-selected neighbors average ten minutes on the actual synthetic network; network-selected neighbors average 3.33 minutes. With `k=2`, the respective means are seven and 4.33 minutes. No clustering or graph neural network is fitted.

`snapshot_access.py` uses four observed McBroken restaurant records in Champaign-Urbana on October 24, 2026. Each restaurant is an origin; targets are other recorded available restaurants of the same chain in the selected box. Origins receive equal weight. The analysis uses a November 18 street extract from OpenStreetMap, filtered for a stated set of pedestrian-compatible highway tags and public-access rules. Edges are undirected, lengths use great-circle kilometers, and straight connectors join restaurant coordinates to the nearest retained node. Restaurant entrances, directional pedestrian restrictions, crossing barriers, and travel delays are unverified. The later network does not reconstruct historical street conditions.

North Neil's nearest alternative changes from Mattis by straight-line distance (3.478 km) to South Neil on the modeled network (4.757 km). Under an imposed four-kilometer threshold, three of four origins have a straight-line alternative and none have a modeled-network alternative. These are distances from restaurant origins within a selected set. The calculation does not estimate customers' residences, their alternatives across all chains, or actual substitution. Unavailability is a recorded ordering outcome and does not establish mechanical failure.

`cartography.py` uses an original synthetic four-node square. Each edge takes two minutes; all four nodes are reachable within five minutes. An imposed square-corner corridor covers 1.60 square kilometers. Filling its interior shades 4.84 square kilometers while the reachable graph remains unchanged. No modeled route leads to the center. This analytic geometry example does not call the upstream isochrone function.

## Run

The reference run used Python 3.13.5 and NetworkX 3.4.2. Inputs are committed; analysis requires no account, live download, or model API. From this directory:

```sh
python3.13 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m unittest -v test_examples.py
.venv/bin/python accessibility.py --output local_runs
.venv/bin/python cartography.py --output local_runs
.venv/bin/python snapshot_access.py --output local_runs
.venv/bin/python verify_results.py
```

Use an installed compatible interpreter if `python3.13` has another path. The three analysis programs accept `--output`; the default is `results/`. `verify_results.py` checks committed reference results. The main calculations are deterministic and need no random seed. Full source for all three appears directly in the lecture notes. [Optional ungraded practice](../../07_Labs/Retail_Accessibility/README.md) uses the same inputs and programs.

## Provenance and Rights

[The input manifest](data/manifest.json) records selection bounds, dates, the Overpass query, and input hashes. `restaurants.csv` contains attributed derived facts from the [supplied McBroken extraction](../McBroken/manifest.json). The extraction's store key is preserved. Missing records are not recoded as available, and no coordinate-based entity matching is performed. A separate upstream data license has not been established. The frozen restaurant subset permits reproducing the calculations without the larger supplied archive.

`osm_highways.json.gz` contains highway ways and referenced nodes from the saved query response. © OpenStreetMap contributors. The extract is available under the [Open Database License 1.0](https://opendatacommons.org/licenses/odbl/1-0/); see [OpenStreetMap's attribution and copyright information](https://www.openstreetmap.org/copyright). Attribute OpenStreetMap when redistributing the extract, derived databases, or visual products, and retain applicable ODbL obligations. A future live request will return a changed database; use the frozen input for the reference result.

The [source review](../../01_Resources/25_Spatial_Networks/README.md) records city2graph's pinned version and license. The course programs are original NetworkX calculations. No upstream notebooks, city2graph package, or graph neural network training were executed.

## Verification and Figures

Eight tests check enumerated shortest paths, both completions of unknown status, retention of isolated origins, the contrast between store counts and access, availability monotonicity, fixed neighbor counts, distance units, and access-tag and boundary rules. `verify_results.py` checks input hashes, population totals, all twelve observed distances against Bellman-Ford, straight-distance lower bounds, and all eight nearest-alternative selections. [The verification record](verification.json) preserves result hashes.

`build_figures.py` writes four editable TikZ sources from the declared inputs and saved outputs. The notes builder supplies PNG companions. Figure descriptions and exact results are available in [the output guide](results/README.md) and [data dictionary](DATA_DICTIONARY.md). Analytical diagrams use Illinois colors, labels, and distinct markers.
