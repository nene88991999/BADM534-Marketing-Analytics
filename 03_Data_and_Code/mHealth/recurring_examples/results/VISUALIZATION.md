# mHealth Visualization Examples

The examples compare recording behavior in May and June 2016 for the 340 teaching-cohort users with a food entry before May 1. Membership is fixed before the comparison. The source checksum is recorded in [visualization.json](visualization.json); cohort preparation and source definitions are in the [example guide](../README.md) and [data dictionary](../../DATA_DICTIONARY.md).

## Reproduce

Use the pinned [requirements](../requirements.txt). From the repository root:

```sh
python 03_Data_and_Code/mHealth/recurring_examples/visualization.py
python 03_Data_and_Code/mHealth/recurring_examples/visualization_charts.py
python 03_Data_and_Code/mHealth/recurring_examples/chart_audit.py
python 03_Data_and_Code/mHealth/recurring_examples/test_visualization.py
```

The first command loads the existing public teaching-data release and cohort cache. Download instructions are in the parent guide. The next command creates three editable TikZ figures in `06_Lecture_Notes/figures` and the browser chart. `06_Lecture_Notes/build_notes.py --figures` compiles the notes and updates figure PNG previews when Pandoc, Tectonic, Poppler, and Pillow are available. Complete program text is printed in M2, Sections 2.14–2.15, and M8, Section 8.12. M3, Section 3.6.1, interprets the paired interval.

## Files and Variables

| File | Contents |
| --- | --- |
| [visualization.json](visualization.json) | Membership, source checksum, monthly aggregates, bootstrap seed/draws, paired change, intervals, and individual-change quantiles. |
| [visualization_monthly.csv](visualization_monthly.csv) | Two rows, one per month. Counts, calendar denominators, logging percentages, and entries per recorded day. |
| [visualization_ecdf.csv](visualization_ecdf.csv) | Aggregate frequency at each distinct logging fraction, with the exact cumulative percentage and eligible-user count. |
| [visualization_interactive.html](visualization_interactive.html) | Month selector, denominator comparison, distribution plot, and visible aggregate table. Download and open locally, or serve as a static HTML file. GitHub's repository file view displays source. |
| [visualization_interactive.vl.json](visualization_interactive.vl.json) | Machine-readable Vega-Lite specification and embedded aggregate data. |
| [chart_audit.json](chart_audit.json) | Outcomes for the correct specification and four constructed chart mistakes. |

`observed_user_days` counts distinct user/date pairs with at least one food entry. `calendar_user_days` equals the fixed eligible-user count times the month's calendar length. `logger_calendar_days` instead uses only users with at least one log that month. `logging_percent` and `conditional_logging_percent` use those respective denominators. `entries_per_observed_day` divides all recorded food rows by observed user-days.

The distribution's `logging_percent` is an individual user's fraction of calendar days with logs, expressed as a percentage. `users_at_value` is the aggregate count at that value; `cumulative_percent` is the percentage of eligible users at or below it. Ties and zeros remain in the table. No user identifiers or individual histories are exported by these programs.

## Interpretation

May and June logging coverage is 67.19% and 62.07% for the fixed population, compared with 72.07% and 67.42% when conditioning on a user logging that month. Mean entries per observed day are 11.80 and 11.69. The difference between conditional intensity and population coverage matters for a retention decision.

The paired change is -5.12 percentage points, with a 95% percentile-bootstrap interval of [-7.93, -2.43], using 5,000 resamples and seed 534. The bootstrap resamples whole users with both monthly outcomes together. It assumes independent users under an empirical user-history sampling model with the months fixed. Shared calendar shocks and population representativeness are outside that model. The separately labeled independent-day interval is deliberately incorrect for the observed dependence structure.

The distribution plot describes customer heterogeneity; the interval plot describes uncertainty about the average change. Neither comparison estimates the effect of a product intervention. A day with no food entry is zero for observed logging, while consumption on that day remains unobserved.

## Figure Descriptions

- **Denominators:** grouped May/June bars start at zero. Illinois Blue uses all eligible calendar user-days; Illini Orange conditions on users with logs in each month. Identical numerators produce different percentages.
- **Distribution:** solid blue May and dashed orange June step curves show the percentage of eligible users at or below each logging fraction. Endpoint masses at zero and daily recording remain visible.
- **Uncertainty:** both horizontal intervals center on the same mean change. The paired-user interval is wider than the incorrect independent-day interval; a dashed vertical line marks zero change.

The browser chart preserves 0–100% scales for both month selections, reports counts in tooltips, and supplies a static table. Its JavaScript libraries load from a CDN, so chart rendering requires internet access; the table remains available offline. No Python server or external AI service is used by the exported page.

## Verification

The three programs were executed locally with Python 3.13, pandas 2.2.3, numpy 2.1.3, and Altair 5.5.0. Five independent tests cover calendar lengths, duplicate dates, empty months, tied CDF values, preserved pairs, and constructed unit/denominator/baseline errors. The chart audit accepts the correct specification and rejects each constructed mistake; this is not a measured error rate for an LLM.

The PDF and all three TikZ previews were compiled and visually reviewed. Browser interaction testing was unavailable because the desktop was locked; both month parameter states were independently compiled and rendered with Vega-Lite 5.20, with rendered labels checked against the numerical evidence. The validation record is [visualization_validation.json](visualization_validation.json). Downloaded reference notebooks were inspected as sources and were not executed.

## Sources

Chart choice draws on the [Financial Times Visual Vocabulary](https://github.com/Financial-Times/chart-doctor/blob/main/visual-vocabulary/README.md). Distribution and uncertainty distinctions are supported by the [seaborn tutorials](https://seaborn.pydata.org/tutorial.html). The [Altair tutorial](https://github.com/altair-viz/altair-tutorial) supplies the declarative-interaction approach; the course programs use their own mHealth transformations and current pinned syntax. [VisEval](https://github.com/microsoft/VisEval) motivates the distinction among executable code, fidelity to a request, and readability. Original references and license terms are recorded in the [resource review](../../../../01_Resources/00_Index/dataviz_resource_review_2026-10-23.json).
