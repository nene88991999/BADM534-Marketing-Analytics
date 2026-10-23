# Synthetic Lecture Examples

These small datasets and calculations support the [eight lecture-note modules](../../06_Lecture_Notes/README.md). All observations, probabilities, and response curves in this folder are **synthetic teaching inputs**, constructed for these notes on October 23, 2026. They contain no student records or real customer data. They are not replications of the published studies discussed in the notes.

Run from the repository root:

```sh
python3 03_Data_and_Code/Lecture_Examples/verify_examples.py
```

The script requires Python 3 and uses only its standard library. It writes the CSV files below and [verified_calculations.json](verified_calculations.json) beside the script. It has been executed successfully. It reconciles order totals, checks the campaign reversal and regression slopes, verifies choice shares, enumerates recommendation lists, and compares the media-budget solution with an independent grid search. It also reports the remaining calculations, including confidence intervals, CLV, and classification metrics.

The script intentionally overwrites these generated example files. Edit the input definitions in the script to change an example, then reconcile the module text and figure. Floating-point output can include tiny numerical artifacts such as `-1.9999999999999991`; displayed values in the notes are rounded.

## Data Dictionary

No file uses a missing-value code. Counts are nonnegative integers; probabilities are fractions in [0,1]. No sample exclusions or transformations were applied to outside data. Currency is in illustrative dollars unless a field or module explicitly uses thousands of dollars. Periods and horizons are imposed by the accompanying case, not calendar dates.

| File | Observation Unit | Fields and Units | Notes |
| --- | --- | --- | --- |
| [M01_order_lines_synthetic.csv](M01_order_lines_synthetic.csv) | Product line within an order | `order_id`, `customer_id`: identifiers; `quantity`: items; `unit_price_dollars`: dollars per item | Two orders, three lines; revenue 37; average order value 18.50 |
| [M02_campaigns_synthetic.csv](M02_campaigns_synthetic.csv) | Campaign by customer type | `campaign`: A/B; `customer_type`: new/returning; `assigned_customers`, `conversions`: counts | Illustrates composition and standardization; does not establish a causal campaign effect |
| [M03_rivals_synthetic.csv](M03_rivals_synthetic.csv) | Illustrative store/market observation | `demand_group`: low/high; `rival_count`: competitors; `sales_illustrative_units`: outcome units | Three observations per demand group; pooled and within-group slopes differ |
| [M04_segmentation_synthetic.csv](M04_segmentation_synthetic.csv) | Customer | `customer`: identifier; `spending_dollars`: total spending; `visits`: count in a common hypothetical window | Compare raw distance with spending divided by 100 |
| [M05_annotation_synthetic.csv](M05_annotation_synthetic.csv) | Classification scenario with 1,000 documents | `prevalence`: true issue fraction; other columns: confusion-matrix counts | Sensitivity 0.80 and specificity 0.90 in both scenarios; counts are stored as whole-valued decimals |
| [M06_experiment_synthetic.csv](M06_experiment_synthetic.csv) | Assignment arm | `assignment`: email/control; `assigned_customers`, `purchasers`: counts | Purchase incidence over a hypothetical 30-day horizon; independent assignments assumed |
| [M06_did_synthetic.csv](M06_did_synthetic.csv) | Group | `group`: treated/comparison; `before`, `after`: mean outcome in illustrative units | Two periods; parallel untreated trends is an imposed interpretation condition |
| [M07_coupon_synthetic.csv](M07_coupon_synthetic.csv) | Hypothetical customer type | Purchase columns: potential purchase probabilities under each action; `margin_dollars`, `discount_dollars`, `contact_cost_dollars`: dollars | Both potential probabilities are known by construction; real data require a causal design |
| [M08_recommendation_synthetic.csv](M08_recommendation_synthetic.csv) | Candidate item | `item`: identifier; `category`: nominal label; `relevance_score`: unitless score | Scores are not probabilities; enumerate three-item lists and a category-variety bonus |

## Additional Calculations

The JSON report also contains renewal incremental contribution (M1), basket Jaccard similarity (M2), an OLS confidence interval (M3), logit shares and acquisition-adjusted CLV (M4), prevalence-dependent precision (M5), email-effect uncertainty and power (M6), a classification threshold and coupon value (M7), and recommendation objectives, carryover, media optimization, and total workflow time (M8).

Read the equations and assumptions in the relevant module before adapting a calculation. Confidence-interval and power formulas are approximations under the stated design. The known media curves are imposed, smooth, and concave; their optimum is not an estimated budget recommendation. Coding assistants should be asked to explain these conditions and verify a small case before extending the code.
