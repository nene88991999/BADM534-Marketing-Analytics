# Data Dictionary

## Public Release

One row is a released postal area. `ZIP_CODE` is restored to five-character `zip`; `STATE` becomes `state`; `MEDIA AND INFORMATION INDEX` becomes `mci`; `CONTENT CREATION AND COMPUTATIONAL INDEX` becomes `cci`. Both outcomes are composite index units. Activity covers October 2022–March 2023. There are no individual identifiers, geographic device counts, original category inputs, or outcome labels. The original CSV remains byte-for-byte unchanged.

## Census Extract

`data/acs2021_zcta.csv` retains national ZCTAs from the 2021 five-year table-based ACS Summary File. `zcta` is a five-character identifier. Estimates cover 2017–2021. Column names use the Summary File convention `Bxxxxx_Eddd` for an estimate and `Bxxxxx_Mddd` for its supplied margin of error. The API metadata in [acs_variable_definitions.json](data/acs_variable_definitions.json) expresses the same estimate as `Bxxxxx_dddE`.

| Fields | Unit and Population | Use |
| --- | --- | --- |
| B19013 E001/M001 | Median household income, 2021 inflation-adjusted dollars | E001 / 10,000 becomes `income_10k` after excluding boundary codes |
| B15003 E001/M001 | Population aged 25 or older | Education denominator |
| B15003 E022–E025 and corresponding M columns | Counts with bachelor's, master's, professional, and doctorate degrees | Sum of E022–E025 / E001 becomes `college_share` |
| B28002 E001/M001 | Households | Broadband denominator and sensitivity weights |
| B28002 E004/M004 | Households with broadband of any type | E004 / E001 becomes `broadband_share` |

Negative numeric sentinel values and nonnumeric unavailable entries become missing in the joined table. Raw extracts retain source values. Income values 2,499 and 250,001 denote open-ended intervals; `income_boundary` preserves this flag. Ratios require a positive denominator and an outcome between zero and one. `regression_eligible` requires all three regression covariates. No missing outcome is replaced with zero.

`data/zcta_coordinates.csv` contains Gazetteer `GEOID` as `zcta`, `INTPTLAT` as `latitude`, and `INTPTLONG` as `longitude`, in decimal degrees. They are internal points, not inferred device locations. The maps use fixed longitude/latitude axes; they are geographic point displays, without area or distance claims.

## Results

`joined_areas.csv` retains all release rows, raw Census estimates/margins, derived ratios, `census_match`, coordinates, and the regression flag. Identifier matches do not guarantee identical USPS and Census populations. `state_coverage.csv` counts released and regression-eligible areas by source state label.

`illinois_map.csv` adds `mci_z` and `cci_z`, each centered by its own Illinois mean and divided by its population standard deviation (`ddof=0`). All areas receive equal weight. `illinois_clusters.csv` adds standardized and raw-distance cluster assignments; labels are arbitrary across fits. `cluster_summary.csv` reports counts and original-unit means. `clustering.json` records k, starts, seed comparisons, scaling constants, standardized SSE, and adjusted Rand agreement.

`regressions.csv` reports outcome, specification, areas, income slope per $10,000, and in-sample residual RMSE in index units. `household_weight_sensitivity.csv` changes geographic weights to ACS household estimates. These weights are neither people nor observed Windows devices. No sampling interval, privacy-noise interval, causal effect, or out-of-sample accuracy is estimated.

`index_check.csv` reports the supplement's three illustrative devices, total group minutes, printed MCI, Equation S1 calculation, and alternative natural-log calculation. `index_check.json` compares equal-device and minute-weighted means of the displayed scores. The source's original private transform remains unresolved.
