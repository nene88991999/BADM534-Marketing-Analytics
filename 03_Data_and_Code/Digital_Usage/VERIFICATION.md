# Verification Record

Executed November 25, 2026 with Python 3.12.14, NumPy 2.3.5, and pandas 2.2.3. No downloaded code, private telemetry, or AI-model endpoint was executed.

## Programs and Numerical Checks

- `prepare_census.py` extracted three official summary tables and Gazetteer internal points, recording full-source hashes. The compact inputs and raw digital-usage release have checksums in `manifest.json`.
- `assess_release.py`, `verify_index.py`, `compare_models.py`, and `cluster_usage.py` executed successfully from archived inputs.
- Eleven unittest checks passed. They verify identifier restoration and invalid keys, missing values and denominators, open-ended income codes, selected direct source matches, a hand-calculated OLS slope, weighted regression against repeated rows, partial regression, exhaustive two-cluster enumeration on five points, adjusted Rand arithmetic, scalar logarithmic calculations, and group totals/means.
- The existing lecture-example verifier passed. Its incidental CSV line-ending conversions were reconciled to original bytes without changing values.
- `scripts/check_lecture_code.py` verified 101 exact source listings across the complete notes, including the five added programs.

## Figure and Document Checks

`build_figures.py` generates four editable TikZ sources directly from checked tables and the stated observation process. The Illinois plots preserve every released area, use common coordinate scales, and distinguish groups with markers as well as color. Source construction, plot values, and rendered layout are checked separately. The notes and five affected session decks compile with the established Pandoc/Tectonic workflow. The syllabus rebuild uses its maintained Markdown source.

The case reports descriptive coefficients without inferential intervals. ACS sampling error, spatial dependence, telemetry selection, and privacy noise are not propagated. The clustering fixes k=3 and tests scaling and initialization, without a validation target. The index example checks published illustrative values; the private production transformation and differences among reported sample counts remain unresolved.

The complete notes contain 440 pages and 112 figures; the standalone Marketing Dialectics chapter contains 35 pages. Ten added slides bring the combined deck to 418 slides. The syllabus remains two pages. All affected decks retain complete Markdown companions. Compiled PDFs and figure previews were rendered and inspected, including added content and neighboring page breaks; no overfull boxes or unresolved references remain in the affected builds.

A clean export of the staged Git tree reproduced every saved analysis-result file and all four TikZ sources byte-for-byte, verified all archived-input hashes, and passed the eleven tests. This export used only the published inputs for the analysis. The larger Census source-table extraction was checked separately from the original downloads. Publication links were checked against the reviewed tree, and the portable LLM context was rebuilt from that tree's intended source versions. The unchanged upstream README retains its original trailing whitespace.
