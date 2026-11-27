# Research Integrity and Replication

An insurer needs a justified intervention, and a reader needs a way to examine the evidence supporting it. This example independently reads a public spreadsheet associated with a retracted honesty study. Its observations have documented evidence of fabrication. Treat it as an artifact for integrity analysis, never as validated behavioral data.

## Inputs and Rights

`data/Study3_with_fonts.xlsx` is an unchanged copy of `DrivingdataAll with font.xlsx` from [ResearchBox 336](https://researchbox.org/336), archived at [Zenodo](https://doi.org/10.5281/zenodo.15030677). Attribution: Uri Simonsohn, Joseph Simmons, and Leif Nelson. ResearchBox specifies [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The local filename changes; the workbook bytes do not. `source.json` records its SHA-256, original path, date, and rights. `data/CODEBOOK.csv` preserves the repository's variable descriptions. The font variable was added by the investigators and is checked against the workbook formatting.

The workbook contains masked policy identifiers and mileage fields for up to four car slots. It contains no names, addresses, contact details, or unmasked policy numbers in its tabular fields. No attempt is made to identify a person or insurer. The public release is reproduced under its stated license.

## Run

Use Python 3 with `openpyxl`. From this directory run:

```bash
python assess_records.py
```

The script reads the source without changing it, verifies its checksum and the font labels, reconciles stored policy averages with paired car readings, and writes aggregate CSV and JSON outputs in `results/`. No downloaded code or workbook macros are executed. Empty car slots remain missing. Mileage differences span varying unknown intervals and must not be annualized.

## Comparisons and Interpretation

- `car1_increments.csv`: counts in ten explicitly defined 5,000-mile bins, with a common policy denominator.
- `rounding.csv`: multiples of 10, 100, and 1,000 for car 1, separately by time and font; every fraction retains its denominator.
- `condition_descriptions.csv`: baseline and increment means by the archived condition label. These are descriptive, without causal interpretation.
- `summary.json`: font counts, support boundaries, and matches restricted to the 44 policies with all four baseline car slots observed.

For a four-car match, each Cambria baseline value must exceed or equal the corresponding Calibri value by at most 1,000 miles. Every one of the 22 complete Calibri records has exactly one candidate among the 22 complete Cambria records. The code checks the joint pattern; it supplies neither a calibrated probability of fraud nor the identity of a fabricator.

The complete Python appears in [M2 §2.35](../../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md). [M9 §9.84](../../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md) develops the distinction between reproducibility, replication, integrity, culpability, and correction. See [verification](VERIFICATION.md) and the [optional exercise](../../07_Labs/Research_Integrity/README.md).
