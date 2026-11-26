# Source Review

## Article and Public Data

Mayana Pereira, Shane Greenstein, Raffaella Sadun, Prasanna Tambe, Lucia Ronchi Darre, Tammy Glazer, Allen Kim, Rahul Dodhia, and Juan Lavista Ferres, [Evidence and measures of the digital usage divide from 40 million Windows devices](https://www.nature.com/articles/s41467-026-78689-1), Nature Communications, November 9, 2026, DOI 10.1038/s41467-026-78689-1. The saved eight-page PDF is marked Article in Press. All eight pages and the thirteen-page supplement were reviewed on November 25, 2026.

The [Microsoft repository](https://github.com/microsoft/Consumption-of-Digital-Applications-Data-Set) contains the released indices, README, license, and standard repository documents. Commit `4024bc0938c4242f2429af94c5fec1e5a42113dc` and release tag `version` point to the inspected CSV. The release is also archived at [Zenodo](https://zenodo.org/records/22084797), DOI 10.5281/zenodo.22084797. No original analysis code is included. Private telemetry, category-level observations, and the internal privacy computation are unavailable.

## Observation and Index Construction

The telemetry concerns consenting consumer Windows devices from October 2022 through March 2023. Virtual, test, and business devices are excluded. The device-month is the activity unit; each device receives a dominant postal code. Engagement uses recent interaction or an active-display keep-alive condition. Monthly category activity is capped at 9,000 minutes. No within-month task sequence is supplied. Browser use can include web-based email, documents, and other activities that a category label cannot distinguish.

MCI combines media and information categories; CCI combines content creation and computational categories. The supplement uses squared first-principal-component loadings for category weights, transformed minutes for device scores, and total category-group minutes for geographic aggregation. The public values are neither percent adoption nor probabilities. Recomputing PCA from the two public indices cannot recover the original category weights.

The OpenDP procedure uses private PCA and Laplace noise in aggregation; the supplement reports total epsilon 4.1 under device-level neighboring records. This privacy statement concerns incremental disclosure under a specified mechanism and does not establish representativeness or an absence of all inferential risk. Zero-device geographic entries are assigned zero activity/counts before noise in the described procedure; the released CSV has no device counts to identify those entries. Treating a very small score as evidence of observed inability would extend the measure beyond its support.

## Reproducibility Checks

| Object | Checked Result | Interpretation |
| --- | --- | --- |
| Public CSV | 28,561 unique identifiers; no missing entries; 50 states and DC | Denominator for the course's release analysis |
| Main Figure 3 | 30,776 postal areas | A reported analytic sample whose relationship to the release is unresolved |
| Supplement prose | 28,199 in the information-sources discussion | A further reported count |
| Supplement Table 3 | 28,987 | Does not equal the release count |
| Supplement flow diagram | 35,177 initially; 31,299 after no-Census-match exclusion; 30,776 after missing predictors; 29,987 after household threshold | These steps do not reconcile all other counts |
| Equation S1 and Table 2 | Stated log2(1+minutes) fails to reproduce the three displayed MCI scores; natural log of positive minutes does reproduce two-decimal rounding | Alternative convention consistent with a toy table; original private transformation unresolved |

The supplement's flow uses a fewer-than-50-households exclusion, while another footnote describes a greater-than-30-households threshold. Preserve source locations and the actual release roster rather than inventing one reconciled screen. These documentation differences do not establish that every empirical finding is wrong.

The course's complete formula check uses the source's rounded weights, which sum to 0.996, and preserves the three displayed minute vectors. It compares conventions explicitly and leaves the upstream source unchanged. No source-provided notebook or private pipeline was executed.

## Census Context and Original Analyses

The course adds public 2017–2021 ACS income, education, and broadband estimates and 2021 Gazetteer internal points. [Census ZCTA guidance](https://www.census.gov/programs-surveys/geography/guidance/geo-areas/zctas.html) distinguishes generalized area representations from USPS postal codes. Exact identifier matches support a transparent contextual comparison; they do not establish identical populations.

The [table-based Summary File](https://www.census.gov/programs-surveys/acs/data/summary-file.2021.html) supplies B19013, B15003, and B28002. Official API metadata supplies variable definitions; direct summary-table downloads avoid an API-key requirement. [Census documentation of income boundary codes](https://www2.census.gov/adrm/PDB/2024/2024_PDB_Documentation.pdf) identifies 2,499 and 250,001 as open-ended intervals. The course excludes those 50 values from its income regression while preserving the records for usage-only comparisons.

The original examples assess the release, map Illinois internal points with fixed scales, estimate descriptive income projections, compare raw and standardized clusters, and check the supplement's numerical illustration. They reproduce their own computations. They do not reproduce the paper's full private analysis or observe customers' skills, willingness, welfare, AI adoption, or service outcomes.
