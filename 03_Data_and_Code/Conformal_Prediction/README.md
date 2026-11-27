# Conformal Prediction: Data and Code

An inventory manager needs demand intervals; a customer-service manager needs to recognize ambiguous complaint categories. These original constructed examples connect interval width and label-set size to those decisions. Full explanations and the three program files appear in [M7 §§7.24–7.25](../../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md), with changed-demand interpretation in [M8 §8.21](../../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md).

## Run

Use Python 3.10 or later with its standard library. From this directory:

```sh
python demand_intervals.py
python complaint_sets.py
python -m unittest -v test_conformal.py
```

No input download, package installation, credentials, or model account is required. Both programs construct their complete inputs and replace only their generated files in `results/`. `conformal.py` supplies the shared rank and label-set functions. There is no random seed because every record is deterministic. Decimal and rational inputs make the small examples hand-checkable; the probability helper expects exact vectors that sum to one.

## Demand Example

Each synthetic store contributes one weekly demand outcome, with its forecast fixed at `100 + 5 * volume_index`. Segment labels are defined before calibration, and disjoint store identifiers separate calibration from evaluation. Fixing these objects isolates how the calibration rule changes the intervals without introducing model fitting.

| Field | Definition and Units |
| --- | --- |
| `store_id` | Unique synthetic identifier within each calibration/evaluation population |
| `split` | `calibration` or `evaluation`; roles are assigned before interval construction |
| `segment` | Predefined `regular` or `volatile` group |
| `volume_index` | Imposed dimensionless predictor, integers 0–19 |
| `prediction`, `demand` | Fixed forecast and constructed weekly demand, in units |
| `scenario` | `reference` or a paired change adding 25 units to each outcome |
| `method` | Pooled calibration or calibration separately within segment |
| `evaluated_demand` | Demand after the specified scenario change, in units |
| `lower`, `upper`, `width` | Prediction-interval endpoints and width, in demand units |
| `covered` | One when the evaluated outcome lies within the inclusive endpoints |

Using all 99 calibration stores gives a 90% pooled threshold of 10 units, compared with segment thresholds of 8 and 20. Evaluation retains all 100 stores, including every interval miss, so the reported coverage uses the full evaluation population.

| Rule and Scenario | Overall Coverage | Regular Coverage | Volatile Coverage | Mean Width, Units |
| --- | --- | --- | --- | --- |
| Pooled, Reference | 90/100 | 80/80 | 10/20 | 20.0 |
| Within Segment, Reference | 98/100 | 80/80 | 18/20 | 20.8 |
| Pooled, Demand +25 | 5/100 | 0/80 | 5/20 | 20.0 |
| Within Segment, Demand +25 | 10/100 | 0/80 | 10/20 | 20.8 |

The change in outcomes holds store identities, forecasts, and calibration fixed. These are descriptive calculations on a constructed population, not estimated coverage in a retail dataset. The within-segment theorem requires exchangeability within predefined groups; ordinary pooled coverage also requires its stated exchangeability condition. A better segment result in this illustration does not establish customer benefit or fairness.

## Complaint Example

Nineteen synthetic calibration cases have known labels and imposed probability vectors over billing, delivery, and product. The 18th true-class error score is 0.65, so a label is included at probability 0.35 or higher. Three additional queries are unlabeled: their sets are billing alone, billing plus delivery, and the empty set. The first is a routing candidate and the other two are assigned human review. No empirical accuracy or coverage is claimed for the unlabeled queries. Singleton-selection error requires its own evaluation.

## Outputs and Figure Companions

- [calibration.csv](results/calibration.csv) and [evaluation.csv](results/evaluation.csv): complete demand inputs.
- [intervals.csv](results/intervals.csv): all 400 scenario-method-store calculations, preserving the paired stores across scenarios.
- [coverage.csv](results/coverage.csv): twelve aggregate rows, with counts, coverage, and widths; text/table companion to the segment figure.
- [demand_summary.json](results/demand_summary.json): thresholds, denominators, and scope.
- [complaint_sets.json](results/complaint_sets.json): all labeled calibration probabilities and the three query sets; companion to the routing figure.
- [verification.json](verification.json): execution environment, checks, and file hashes.

The full programs ran under Python 3.13.5. Six independent checks passed, including exhaustive held-out-rank enumeration rather than comparison of a function with a duplicate implementation. The [resource review](../../01_Resources/18_Conformal_Prediction/SOURCE_REVIEW.md) records inspected reference code separately from these executions. All course code and records in this folder were written for these examples; no upstream code or customer records were copied.
