# Inputs, Units, and Outputs

All values in `data/cases.json` are original synthetic teaching inputs. Node indices are zero-based. Each case is separate; their populations and training splits must not be combined.

## Four-Zone Retail Network

| Field | Meaning and Units |
|---|---|
| `zones` | Four zones A-D in fixed order. |
| `population` | People at each original origin; initially 100 per zone, total 400. |
| `weekly_zone_revenue_dollars` | Invented weekly total revenue for each zone, in dollars: 10, 10, 10, 40. |
| `group` | Contiguous group IDs 0 and 1; A-C enter group 0, D enters group 1. |
| `edges_minutes` | Undirected simple edges `[origin, destination, minutes]`; positive travel time. |
| `store_node` | Node 3, zone D, contains the one available outlet. |
| `access_threshold_minutes` | Inclusive five-minute threshold, with zero travel at the store's own origin. |

No nodes or people are excluded. Feature means weight original zones equally; access shares weight origins by people. Mean zone revenue differs from individual spending. Affinity is defined as the reciprocal of edge minutes. Binary membership, its averaging pseudoinverse, and combinatorial energy are used explicitly. Internal coarse self-loops are removed. Population changes affect access weights and do not automatically change the zone-revenue feature definition.

`results/zones.csv` retains one row per original zone: people, group, original and reconstructed revenue, original travel minutes, naive coarse minutes, and the two binary access indicators. `results/network.json` records group sizes, means, totals, reconstruction squared error, coarse affinities (per minute), reduction `1 - groups / original_zones`, and the two access shares. Energy has units dollars squared per minute for the weekly revenue feature.

## Label Cases

| Field | Meaning |
|---|---|
| `outcomes` | Three node labels 0, 0, 1 within one group. |
| `train_indices`, `test_indices` | Training node 2; test nodes 0 and 1. The training-only constant uses only node 2's outcome. |
| `alternative_test_indices` | A separate scoring subset containing node 2, used to compare a global majority with that subset's own ceiling. It is a separate split illustration. |
| `minority_groups` | Two groups, each with three routine-service labels 0 and one specialist-service label 1. Eight synthetic customers; two positive cases. |
| `parameter_edges` | Separate three-node path with two undirected edges, each counted once. |
| `parameter_training_indices`, `parameter_heldout_indices` | Permitted nodes 0 and 1; held-out node 2, separate from the purity example. |
| `parameter_labels_before`, `parameter_labels_after` | Only node 2 changes from 0 to 1. Training labels remain 0, 0. |

`results/labels.json` gives label choices, scoring counts, oracle purity, test scores, class-1 recall, and edge disagreement using all edges or only training-training edges. Majority ties choose the smaller numeric class. A training group with no labeled observations raises an error; an applied classifier would need a separately justified fallback. The all-label majority is an oracle diagnostic. The only fitted predictor in this example is a constant chosen from training labels.

## Background Sources

The review pins GraCo commit `19da8a6031dcf1803faa5723148b5975a5462af6` and Joly's paper version `2611.01200v1`. The published Cora metrics and the separate 800-person retail calculation remain in the [source review](../../01_Resources/32_Graph_Coarsening/SOURCE_REVIEW.md); they are not observations in this input file. Original licenses for source material remain in the resource collection. These course inputs and programs contain no copied publisher data or executable upstream code.
