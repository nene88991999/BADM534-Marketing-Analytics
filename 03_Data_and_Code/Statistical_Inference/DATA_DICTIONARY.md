# Data Dictionary

## mHealth Input and Sample

Input: `../mHealth/data/food_entries.csv.gz`, verified against `../mHealth/manifest.json`. Only `Userid` and `Fancydate` are read. The cohort includes pseudonyms whose first four hexadecimal characters after the initial prefix represent an integer below 4096. Membership additionally requires an observed day before May 1, 2016. The retained dates are normalized to calendar days and duplicates are collapsed. No nutrient or weight values are used.

`mhealth_monthly.csv` has one row per month. `users` is the fixed roster; `logged_days` counts distinct user-days; `calendar_days` is users times days in that month; `users_without_logs` retains roster members without that month's entries. `logging_percent` is 100 times logged days divided by calendar days.

`mhealth_uncertainty.csv` has one row per uncertainty method. `estimate_pp`, `se_pp`, `ci_low_pp`, and `ci_high_pp` use percentage points. `p_value` is two-sided for zero mean change. `reference_df` is 339 for the approximate paired Student test and absent for the normal independent-day comparison. The latter intentionally omits dependence. `mhealth.json` records the source hash, roster rule, target, and interpretation.

## Synthetic Store Outcomes

`synthetic_store_customers.csv` retains repetition 0 at correlation 0.3. There are 40 stores, each with 20 customer rows. `store` identifies the assignment and shared-shock unit; `customer` is a within-store index. `assigned_promotion` is 0 or 1 and constant within store. `contribution_dollars` is synthetic net contribution for a customer, with Gaussian support allowing losses. Every potential treatment effect is zero.

`simulation.json` records seed 20261125, 4,000 experiments per correlation, 20 treated stores, mean contribution 100 dollars, marginal variance 800 dollars squared, correlations 0, 0.1, 0.3, and 0.5, and alpha 0.05. New stores and customers are drawn in each experiment; common underlying draws and assignments are retained across correlations. Equal store sizes make store- and customer-average point estimates identical.

## Simulation Results

`null_calibration.csv` has one row per correlation and method. `rejections` counts p-values below 0.05; `rejection_rate` divides by `repetitions`. `mc_ci_low` and `mc_ci_high` are 95% Wilson intervals for that fraction. Effect estimates, empirical effect standard deviations, mean reported standard errors, and theoretical effect standard deviations use dollars. `design_effect` is the theoretical variance ratio to the independent-customer benchmark, `1 + (customers_per_store - 1) * rho`.

`first_experiment.csv` retains repetition 0 at every correlation and method. It includes the effect, standard error, Welch reference degrees of freedom, p-value, and effect confidence interval. Those intervals concern one experiment; the Wilson intervals in `null_calibration.csv` concern the Monte Carlo rejection fraction. Neither is a prediction interval for an individual customer.
