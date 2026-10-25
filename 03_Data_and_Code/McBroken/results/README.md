# McBroken Results and Verification

The programs ran successfully on October 24, 2026. The source data cover October 25, 2025, through October 24, 2026, for the daily audit and forecast case. The policy case uses 25 weekly snapshots around October 28, 2024, displaying week zero and excluding it from the pre/post means.

| Output | Content |
| --- | --- |
| `coverage_sensitivity.csv`, `coverage.json` | Coverage thresholds, equal-day means, pooled fractions, and missing/sparse dates. |
| `policy_means.csv`, `policy.json` | Country pre/post means and descriptive contrasts in percentage points. |
| `prediction_scores.csv`, `prediction.json` | Fixed time split, sample counts, label coverage, Brier scores, and accuracy. |
| `prediction_calibration.csv` | Training probabilities, later observed rates, and label coverage by previous status. |
| `source_spot_checks.json` | Checks of the first and last daily snapshots against their full upstream commit IDs. |
| `verification.json` | Python and package versions, executed programs, test counts, source checks, and PDF/figure counts. |

## Figure Descriptions

- **M02_mcbroken_coverage:** Two vertically aligned time-series panels share the same calendar. The upper panel reports observed US record counts and a dashed 2,000-record threshold; the lower panel reports the observed unavailable percentage from 0 to 100. Missing dates remain gaps. Counts change substantially while the percentage describes a changing observed population.
- **M06_mcbroken_policy:** Weekly unavailable percentages for USA, Canada, and UK share a 0–100 scale. A large UK pre-policy spike changes the comparative before/after calculation. The vertical line is the US policy effective week. The displayed comparison is descriptive.
- **M07_mcbroken_prediction:** Paired bars compare training probabilities with later observed rates within two previous-status groups. A previously unavailable record has a much higher later rate. Both later rates exceed the corresponding training forecast, indicating calibration drift in this test period.

Each figure uses the Illinois palette with redundant labels or line styles. TikZ sources and PNG companions are in `06_Lecture_Notes/figures/`; the full source programs are embedded in the Markdown and PDF notes.

## Checks Performed

The source preparation checks unique store-date and dimension keys, binary status, matched keys, reported check ages, national count reconciliation, and observed-date totals by key. Five counterexample tests verify missing-field handling, duplicate/unmatched keys, exact calendar matching, grouped versus individual Brier scores, and exclusion of later labels from training. The lecture-code checker verifies exact agreement between all embedded code and source files.

The first and last daily archive snapshots were independently retrieved by full commit ID and reconciled with the supplied national counts. Their US status fields were Boolean and nonmissing. The full historical network collection was not rerun. The supplied upstream notebook's saved outputs are reference material, not evidence that its collection code was executed during this verification.

The row counts do not establish physical restaurant counts, representative sampling, causal effects, or independent observations. The interpretation of each result follows the explicit sample and measurement definition in the data dictionary and notes.
