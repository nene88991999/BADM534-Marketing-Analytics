# Earnings-Call Data Dictionary

## Observation Levels

`firms.csv` has one row per ticker in the supplied 123-firm roster. `calls.csv` has one row per unique `call_id`. `mentions.csv` has one row per regex occurrence, keyed by `mention_id`; several occurrences can belong to the same call, turn, or sentence. Joining calls directly to mentions repeats call-level quantities. Aggregate matches to call first, then use a validated one-to-one join when constructing call-level rates.

## Inputs

| File | Fields and Meaning |
| --- | --- |
| `firms.csv` | `ticker`, company, supplied sector group; `inclusion` describes selection; `n_calls_in_window` includes empty-text records; provider list URL |
| `calls.csv` | Stable call ID, ticker, company, supplied group, call date, fiscal year/quarter, source URL; `n_turns`; `qa_start_turn` is a heuristic index, with -1 meaning undetected; total and role word counts; core, broad, and per-term regex counts |
| `mentions.csv` | Match ID, call ID, ticker/date; dictionary term/category/tier; heuristic role and section; turn index. No transcript text or speaker names |
| `dictionary.csv` | Term ID, category, core/broad tier, Python regex, case-sensitive flag (0/1). Tier describes retrieval specificity, not a verified business practice |
| `interpretation_cases.csv` | Seven selected source match IDs and URLs, original term IDs, course-authored paraphrases, evidence scope, and interpretation. Purposeful examples, not representative accuracy labels |

Fiscal quarters can differ from calendar quarters. The time-series output derives calendar quarters from `call_date`. The first and last calendar quarters have partial date support. Interior calendar coverage alone does not establish complete source capture.

## Derived Flags and Rates

`text_observed` means `words_total > 0`. The empty `DLTR_FY2026Q2` record remains in the coverage assessment, with unknown `has_core`. `has_core` is 1 if at least one core match occurs in an observed call and 0 otherwise; NaN denotes unobserved text. This binary indicator measures dictionary occurrence, not confirmed adoption. `qa_detected` means `qa_start_turn >= 0`; it is a parsing flag, not evidence that no Q&A occurred when false.

`core_call_rate` divides positive calls by observed calls. `per_10000_words` divides role-specific core matches by words attributed to that role in the same call sample and multiplies by 10,000. Management words include prepared remarks and Q&A; analyst words are attributed to Q&A. Unknown/operator words can appear in total words without entering either role denominator.

`firm_coverage.csv` retains Winmark (WINA), with zero supplied calls and an unknown rate. Firms with observed calls and no matches have rate zero. `event_windows.csv` uses calendar-day distance from February 27, 2024, excludes the event day, and includes the endpoints at ±60, ±90, or ±120 days. `firms_in_both_windows` retains firms with at least one observed call in each window. `share_percent` weights calls equally; `firm_equal_share_percent` averages within-firm rates equally.

## Interpretation Conditions

Disclosure is selected by the firm, analysts, transcript coverage, and the vocabulary. Roles and Q&A sections are heuristic. The source retains only truncated excerpts, so applying the dictionary to an excerpt cannot reconstruct whole-call recall. No direct prices, customer outcomes, policy-adoption labels, or independently validated legal outcomes are present. Repeated calls within firms also share business and communication conditions; a statistical generalization would require a defensible sampling target and dependence-aware uncertainty calculation.
