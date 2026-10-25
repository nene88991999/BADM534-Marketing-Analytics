# Verified Course Adaptation

The [McBroken teaching examples](../../../03_Data_and_Code/McBroken/README.md) integrate this supplied collection into Marketing Analytics, with full source in the lecture notes:

- M2 §2.16: order availability, coverage, missing dates, identifier diagnostics, parser checks, and exact calendar joins.
- M6 §6.16: descriptive policy contrasts and comparison-country sensitivity.
- M7 §7.18: fixed-date forecast evaluation, grouped probability scores, and missing future labels.

The source audit reconciles all 3,053,307 US panel records with the supplied daily country counts and the dimension table's observed-date counts. It finds nine dates without US observations, three sparse observed US dates under the imposed 2,000-record threshold, and substantial address-key turnover. The first and last daily snapshots were independently checked against their exact upstream commit IDs.

## Corrections and Interpretation

The [Copyright Office final rule](https://www.govinfo.gov/content/pkg/FR-2024-10-28/pdf/2024-24563.pdf) became effective October 28, 2024. The source notebook's October 25 reference concerns announcement timing. The course calculation uses the effective week and excludes it from the pre/post means. Comparisons with Canada and the UK produce materially different descriptive contrasts; neither is presented as an identified causal effect.

The original extractor's use of `bool(value)` can coerce a missing status to false and a string `"false"` to true. Substituting zero for missing check age can also manufacture a check timestamp. The course parser demonstrates explicit handling on constructed examples. Binary-value checks of the supplied CSVs cannot recover information already lost upstream. No historical status is imputed or silently changed.

The inspected archive workflow retains records whose reported check age is below 61 minutes, while its older README describes 31 minutes. Preserve the extraction version and commit IDs. Constant country counts or repeated percentages motivate a freshness check; they do not by themselves establish stale data.

The original notebook and network retrieval scripts remain source references. Their saved outputs were not regenerated during this course adaptation. The verified examples run from the local aggregate tables, with the full supplied bundle used for source reconstruction. No scheduling workflow was activated.
