# Data Dictionary

## Published Research Inputs

The source files are in `../../01_Resources/14_LLM_Evidence_and_Revalidation/source_tables/`, accompanied by their original MIT license and README.

- `claims.csv`: one row for each of 50 selected claims. `blog_id` is C1-C50; `key` is the upstream internal identifier. `verdict` records the source classification. `dead` is displayed as expired. `paper_date` is the first public paper date. `paper_anchor` and `null_value` are claim-specific metric values; their units depend on `metric`. A relative effect of one matches the reference and zero matches the claim-specific null. Model-specific nulls require the detailed post data.
- `panel_values.csv`: one row for each claim-model pair. `model` is a stable panel identifier; `model_name` is the reported model; `release` is its release date. `value`, `lo`, and `hi` retain the claim's metric units. `n` is the source's claim-specific scoring count, not a uniform independent sample size. `e` is the relative effect. `reliable=False` marks an unscorable comparison and remains missing from model-level counts. `source` and `note` identify run provenance and qualifications.
- `post_results.json`: the released fitted curves, classification, dates, and uncertainty. `death` is the authors' estimated expiration date; `death_kind` distinguishes fitted, interval-based, and recent-model-count dates. `generated` dates the export, rather than the models or their publication.

## Derived Research Outputs

- `verdicts.csv`: claim counts and fractions, denominator 50.
- `lifetimes.csv`: one row per claim; `months` is elapsed days divided by 365.25/12. `event=1` uses an estimated expiration date; `event=0` uses the September 30, 2026 censoring date. Censored rows do not establish that a claim lasts forever.
- `horizons.csv`: Kaplan-Meier point estimates at six, twelve, and twenty-four months. `followup_curve.csv` preserves every displayed step through twenty-four months.
- `model_counts.csv`: reliable and unreliable pair counts and the number of reliable point estimates at or below 0.2. This simple point-estimate count does not reproduce the full fitted category rule.
- `citation_fabrication.csv`: C11 observations for all twenty models. `fabricated_fraction` measures nonexistent cited works; it does not measure erroneous details about real works or whether a real source supports the assertion.

## Constructed Upgrade Outputs

- `synthetic_cases.csv`: `case_id` identifies one of 100 paired tasks; `segment` is routine or consequential; `old_pass` and `new_pass` are binary outcomes under a fixed rubric; `failure_cost` is stipulated dollars per failed task. All cases are constructed, complete, and equally weighted in the pooled accuracy.
- `upgrade_summary.json`: pass counts, recoveries, regressions, percentage-point changes, and aggregate dollar losses. The cost ratio is dimensionless. The zero-failure bound is a probability under an independent common-probability binomial model.
- `judge_comparison.json`: four imposed mean scores from a common 0-100 rubric, followed by within-judge, within-generator, and diagonal differences in score points.
