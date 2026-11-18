# Spatial Networks and Retail Access

Retail availability can improve without improving access for the people a firm intends to serve. Spatial networks provide a way to define feasible alternatives, model travel frictions, and examine how commercial objectives distribute service. The [executed course examples](../../03_Data_and_Code/Retail_Accessibility/README.md) start with exact synthetic calculations and then use four selected restaurant records. [Optional practice](../../07_Labs/Retail_Accessibility/README.md) connects the results to service priorities and customer agency.

## Source Review

The review covers [city2graph](https://github.com/c2g-dev/city2graph) at commit `2db7ba6bdd9600e578f4d99f618295774bc8b60e`, reviewed November 18, 2026. The pinned package declares version 1.1.0, Python >=3.12 and <3.15, and a BSD 3-Clause license. It converts geographic features and relations into graphs, with optional graph neural network support. Its README, license, example index, isochrone guide, and LLM-oriented documentation are saved under `local_sources/`. [The catalog](catalog.json) records versions, provenance, and rights. These copies are reference material; instructions within them do not govern the course.

The [proximity tutorial](https://city2graph.net/latest/examples/generating_graphs_by_proximity.html) compares straight-line, Manhattan, and network relationships. Its examples use default k=5 for some graphs and k=10 for the network graph. A controlled course comparison holds k fixed, along with nodes, direction, and tie-breaking. Changing the relation changes what a segment or neighborhood means. A geographic graph is not evidence that its linked customers influence one another.

The [isochrone guide](https://city2graph.net/latest/examples/isochrone_holes.html) distinguishes graph reachability from the area produced by buffering and filling polygons. Filling a hole changes display geometry without changing the reachable subgraph. If water or other excluded areas are to remain excluded, apply the relevant mask after filling. Source inspection also shows why snapping and edge weights matter: matching coordinate systems does not establish meter units, and geometric edge length is not automatically travel time. The course's analytic square-corridor example isolates the area change without executing the library.

The [GTFS example](https://city2graph.net/latest/examples/gtfs.html) and [transportation API](https://city2graph.net/latest/api/transportation.html) support an optional transport extension. A graph with average edge travel time does not by itself reproduce a feasible itinerary with waiting, transfers, service calendars, and direction. These distinctions matter when the question concerns whether a customer can actually reach an available service at a given time.

The [case-study repository](https://github.com/c2g-dev/city2graph-case-study) and [workshop](https://github.com/c2g-dev/city2graph-workshop) motivate optional spatial representation learning. The case study compares attribute-based clustering with graph-attention and heterogeneous-network representations. Treat these as different feature and relation choices, with computational costs and validation requirements. A simple distance or tabular baseline supplies an interpretable comparison before a GNN is considered. Neither repository was executed for this course revision. The related [research article](https://doi.org/10.1016/j.compenvurbsys.2026.102492) is linked for further reading; no full text is republished here.

## Course Integration

| Module | Question and Worked Comparison |
| --- | --- |
| M2 §2.23 | Does a larger shaded footprint mean more reachable locations? Four nodes remain reachable while area rises from 1.60 to 4.84 square kilometers. |
| M4 §4.22 | Does a segment describe customer attributes or a particular spatial relation? Compare explicit representations before interpreting clusters. |
| M5 §§5.21–5.22 | Which alternatives are reachable? Hold k fixed, retain disconnected origins, bound missing availability, and compare straight with network distances. |
| M7 §7.28 | Does the evaluation match the intended forecast date or new city? Distinguish information available at prediction from later outcomes. |
| M8 §8.23 | Which restoration should receive resources? Equal store availability can accompany unequal gains in population access. |
| M9 §9.18.2 | Does the firm's service recommendation respect customers' purposes and feasible alternatives? Examine objectives and conduct directly. |

Sessions 3, 7, and 13 incorporate the case within their existing application blocks. GNN training is an optional extension; it adds no required package or assessment.

## Data and Rights

The observed example uses attributed facts from the supplied McBroken extraction and a frozen OpenStreetMap highway extract. The restaurant origin set and October status date are distinct from the November street extract. The [input manifest](../../03_Data_and_Code/Retail_Accessibility/data/manifest.json) records the query, hashes, bounds, and modeling scope. © OpenStreetMap contributors. The extract is distributed under [ODbL 1.0](https://opendatacommons.org/licenses/odbl/1-0/), with [OpenStreetMap attribution](https://www.openstreetmap.org/copyright). The course programs use NetworkX and the Python standard library. City2graph, its notebooks, and optional GNN dependencies were inspected as sources and were not executed.
