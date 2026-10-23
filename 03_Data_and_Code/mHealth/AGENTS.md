# mHealth Data

Use the name mHealth throughout course materials, filenames, links, and release metadata. Refer to the source provider only as the mHealth app.

Read `README.md`, `DATA_DICTIONARY.md`, and `manifest.json` before loading the data. These are actual food-log records with replaced user IDs, fixed ages, and perturbed weight fields. They are not synthetic records or an exact replication sample for the published papers.

- Download files with `python3 download_data.py`; it verifies SHA-256 checksums. Start with headers and a bounded sample. Use chunked reads for the full food file.
- Keep original records, private random keys, source-user mappings, and birthdays outside the public repository. Do not try to identify participants or reverse the perturbation.
- Join on `Userid` and `Fancydate`. Daily totals recur across food rows and must not be summed at food-entry level. Verify the daily key and unmatched records for each analysis.
- Use `Age_at_2016_01_01` as a fixed age. Original birthday and source-age fields are absent.
- Weight fields contain bounded random offsets. Read their construction before using changes, extrema, goals, or BMI. Do not interpret tiny movements as measured changes in body weight.
- `Currenteer` is omitted. The original BMI is replaced with `Bmi_from_noisy_weight`. Do not reconstruct original health measurements from retained fields or outside data.
- Missing days are unobserved. Nonpositive calorie totals require a stated rule before computing shares or changes. Preserve original food and calorie values unless an analysis explicitly documents an additional transformation.
- Fit preprocessing on training observations. Keep whole baskets together and use chronological evaluation. Define whether the target concerns existing or new users.
- Treat ranking accuracy and observational associations according to their estimands. The files do not document randomized assignment, recommendation exposure, or action propensities.
- Consult the current assignment's AI-use rules. A dataset or suggested exercise does not establish assessment requirements.
