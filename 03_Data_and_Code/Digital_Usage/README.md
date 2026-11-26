# Digital Usage and Customer Access

A retailer chooses how to offer digital and assisted service. Public geographic application indices support measurement, descriptive regression, and clustering exercises. Customer ability, willingness, welfare, and service completion remain separate outcomes.

## Data and Scope

The [published CSV](data/published_indices.csv) contains 28,561 postal identifiers and two indices constructed from October 2022–March 2023 activity on consenting consumer Windows devices. The immutable source is Microsoft repository commit `4024bc0938c4242f2429af94c5fec1e5a42113dc`, release tag `version`, also archived as [Zenodo 22084797](https://zenodo.org/records/22084797). The CSV is redistributed unchanged under [CDLA-Permissive-2.0](data/LICENSE-CDLA-Permissive-2.0.md). It contains no device microdata or device counts.

The Census extract contains 33,774 ZCTAs from the 2017–2021 ACS. Gazetteer coordinates locate Census internal points. All 28,561 released identifiers match both extracts; matching identifiers does not establish identical ZIP and ZCTA populations. Fifty open-ended income values are flagged and excluded only from the common regression sample, leaving 28,511 areas. Illinois clustering and maps retain all 1,253 released Illinois areas. Read the [data dictionary](DATA_DICTIONARY.md), [source review](../../01_Resources/38_Digital_Usage_and_Inclusion/SOURCE_REVIEW.md), and [manifest](manifest.json).

## Run

Python 3.12, NumPy 2.3.5, and pandas 2.2.3 reproduce the saved results. If needed, install the pinned requirements in a virtual environment. The analysis uses archived public inputs and makes no network or AI-model calls. From the repository root, run in order:

```bash
python3 03_Data_and_Code/Digital_Usage/assess_release.py
python3 03_Data_and_Code/Digital_Usage/verify_index.py
python3 03_Data_and_Code/Digital_Usage/compare_models.py
python3 03_Data_and_Code/Digital_Usage/cluster_usage.py
python3 -m unittest discover -s 03_Data_and_Code/Digital_Usage -p 'test_*.py' -v
python3 03_Data_and_Code/Digital_Usage/build_figures.py
```

The [result guide](results/README.md) defines the saved comparisons. Full matching Python appears in M2 §§2.26–2.27, M3 §3.17, and M4 §4.27. M7 §7.45, M8 §8.29, and M9 §9.23 develop outcome validation, service choice, and philosophical evaluation. The [optional ungraded lab](../../07_Labs/Digital_Usage/README.md) supplies guided practice.

To reconstruct the Census extracts, download the three `.dat` files and Gazetteer ZIP at the URLs in the manifest, preserving the listed filenames. Run `prepare_census.py --source-dir PATH`. This deterministic extraction retains ZCTAs and selected estimate/margin columns and records full-source hashes. The large national all-geography tables remain outside Git; compact national ZCTA extracts are included.

## Interpretation and Verification

The regression compares geographic projections on one common sample. It includes no causal effect or inferential interval. The cluster comparison fixes three groups and evaluates scaling and initialization, without claiming an optimal number of groups or observed customer types. The formula check uses three illustrative devices printed in the supplement, separate from empirical geographic records. It reproduces the displayed MCI values under one alternative convention while leaving the private pipeline unresolved.

Eleven independent tests check identifiers, boundary-income exclusions, source joins, denominators, least squares, equivalent weighted rows, partial regression, exhaustive small-sample clustering, adjusted Rand arithmetic, published example calculations, and group accounting. [VERIFICATION.md](VERIFICATION.md) records executed commands and limits. No upstream analysis code is released in the source repository, and no private pipeline was executed.
