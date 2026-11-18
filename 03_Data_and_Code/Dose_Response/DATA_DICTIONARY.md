# Data Dictionary

All records are synthetic. Seeds and generation equations are in [README.md](README.md) and the complete programs. No source customer data enter these examples.

| File | Observation Unit | Variables and Interpretation |
| --- | --- | --- |
| `results/customers.csv` | Eligible customer in one promotion week | `type`: observed demand characteristic, -1 or 1; `discount_pp`: assigned discount in percentage points; `profit_usd`: realized profit in dollars |
| `results/curves.csv` | Evaluation dose | `discount_pp`: 6–34 in steps of one; `truth_usd`: known population profit; `outcome_1_density_0`, etc.: estimated curves, where 1 identifies a correctly specified nuisance model; `_conditional_se`: local linear HC0 standard error holding fitted adjusted outcomes fixed |
| `results/coverage.csv` | Model specification and evaluation dose | `pointwise_coverage`: fraction of 200 independent samples whose approximate interval contains the known response; `monte_carlo_se`: binomial simulation standard error; `mean_bias_usd`: average signed curve error |
| `results/overlap.csv` | Dose on a 1–39 grid | Conditional densities per percentage point for types minus/plus one; `broad` uses transformed-dose noise SD 0.9; `narrow` uses 0.22 |
| `results/hidden_confounding.csv` | Evaluation dose | `causal_profit_usd`: equal-type causal mean; `adjusted_association_usd`: exact observed regression standardized over X while U is omitted |
| `results/stores.csv` | Customer within store | `store`: 0–19; `region`: 0–3; `discount_pp`: randomized discount; `profit_usd`: synthetic profit; `validation_fold`: 0–4, allocated within each store |
| `results/store_curves.csv` | Store and dose | `truth`, `complete`, `separate`, `partial`: known or fitted profit in dollars; every store uses the same 29-dose grid |
| `results/pooling_cv.csv` | Candidate penalty pair | `equal_store_validation_mse`: dollars squared, averaging each store's out-of-fold MSE equally; `region_penalty`, `store_penalty`: penalties applied to the stated standardized basis coefficients |
| `results/objectives.csv` | Candidate discount | `profit_usd`, `revenue_usd`: dollars per eligible customer; `units_per_customer`: expected units with $4 unit cost; `complaint_fraction`: imposed probability, not a measured rate |

`summary.json` records the reference estimates, 200-sample evaluation, effective sample sizes, and exact hidden-confounder bias. Curve RMSE averages squared error equally over the stated grid and then takes a square root; the repeated-sample summary averages those RMSEs. Pointwise mean coverage averages the 29 dose-specific rates. Whole-grid coverage records how often all 29 pointwise intervals contain their targets; it is distinct from pointwise coverage and has no 95% guarantee.

`pooling_summary.json` reports the square root of mean squared curve error with equal weight per store and grid point. Small stores have 12 or 25 customers (eight stores); large stores have 150 or 300 (eight stores); four stores with 60 customers enter the all-store comparison. `objectives_summary.json` reports each selected discount and its outcomes on the 0.1-percentage-point search grid.
