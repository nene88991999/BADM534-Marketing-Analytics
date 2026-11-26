# Logging Tasks and Measurement

## Population and Timing

The source is the transformed mHealth teaching release dated October 23, 2026. Select public pseudonyms whose first four hexadecimal digits represent an integer below 4096, matching the recurring course cohort. Eligibility then requires at least one food record from January 1 through June 30, 2016. Both later tasks retain this same roster. Its membership reflects prior recorded activity, not an account-enrollment registry or a representative consumer sample.

July is the development task and August is the evaluation task. A task's start date is included and its end date is excluded. The input also contains the preceding date and the end date when observed, so filtering has an observable consequence. Local calendar dates are preserved from the source; no timestamp or time-zone interpretation is added.

## Files and Variables

| File or Field | Definition |
| --- | --- |
| `roster.csv`, `user_id` | One row for each eligible user. Aliases U0001 onward follow sorted public pseudonyms; the same alias identifies the same user in both tasks. |
| `observed_days.csv` | One row per observed user-date in the task window and its two boundary dates, restricted to the fixed roster. |
| `date` | ISO calendar date, YYYY-MM-DD. |
| `entries` | Number of source food rows on that date. Several entries still represent one logged day. This is not calorie intake. |
| `task.json` | Task ID, included start, excluded end, and earlier eligibility cutoff. |
| `logged_days` | Distinct dates with at least one record in the specified window for this user. |
| `window_days` | Number of calendar days from included start to excluded end. |
| `logging_rate` | `logged_days / window_days`, on a 0–1 scale. |

Users without records during the task window remain in the output with zero logged days. That zero describes the released file's logging indicator. It does not establish zero food intake, account closure, or observation of every actual logging event. No nutrition screen is applied because the target is record presence rather than dietary intake.

## Controlled Errors

The independent tests use invented users A, B, C, and Z. They introduce a repeated date, a duplicate roster key, boundary dates, an out-of-roster record, an ambiguous non-ISO date, missing output users, and nonfinite values. These records remain separate from the actual mHealth task inputs. The reference calculation rejects duplicate roster keys and invalid dates; repeated event dates are collapsed to a distinct-day indicator.

## Published Benchmark Aggregates

The three CSVs under `01_Resources/40_Econometric_Coding_Workflows/data` retain the authors' schema. `appendix_silent_vs_loud.csv` contains three workflow rows. `n` counts assigned runs; `failures = loud + silent`. Fields ending in `per100` divide by assigned runs, whereas `silent_share_of_failures_pct` divides by failures. The `_lo` and `_hi` fields are supplied 95% percentile intervals from 4,000 bootstrap draws over 40 tasks.

`prompt_agency.csv` contains six prompt rows and nine platform rows, distinguished by `panel`. The stored `few_shot` label means one related code example in this manuscript. Each prompt cell has 7,200 assigned runs; each language cell has 4,800. `successes` is an integer count, and `success_pct` uses a 0–100 scale. The course contrast program selects the prompt panel explicitly.

`summary_by_model.csv` contains six model rows. Success fields ending in `_pct` use a 0–100 scale; cost fields ending in `_usd` are dollars. The incremental-cost calculation divides the difference in mean token cost per run by the difference in success probabilities on a 0–1 scale. It excludes analyst effort and downstream losses. Model names and effort levels remain the authors' labels.

## Constructed Error Assessments and Hypothetical Costs

`semantic_checks.csv` has one row per constructed program and period. `executed` records whether the program returned; `complete` requires every roster user and a finite value for each requested numeric field. `total_days_matches` checks only the sum of logged days. `valid` also checks every user's values against the reference. `mean_returned_rate` averages the rows returned by that program and can change its denominator or units in an incorrect case. Empty values are unavailable outcomes.

`decision_costs.csv` reports expected dollars for the stated number of assigned analyses. The probability of an undetected error is per assigned analysis; the loss is conditional on such an error reaching a decision. Review minutes include correction effort. All operating inputs are hypothetical and are recorded in `decision_cost_summary.json`.
