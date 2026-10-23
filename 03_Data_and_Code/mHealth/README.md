# mHealth: Food Logging and Personalized Recommendations

A food-tracking app uses past behavior to decide which foods to suggest and how to support a customer's stated goals. These actual 2016 records connect food descriptions, repeated consumption, daily totals, and customer histories. They support exercises in data preparation, category classification, segmentation, and next-basket recommendation.

The teaching copy replaces user IDs, removes birthdays and images, calculates a fixed age, and adds small random offsets to weight fields. BMI is recalculated from the altered weight. The records are not synthetic, and the perturbation does not guarantee anonymity. The source files remain unchanged.

| File | Records | Users | Period |
| --- | ---: | ---: | --- |
| Food entries | 13,874,280 | 5,908 | January–December 2016 |
| Daily summaries | 551,904 | 2,676 | January–December 2016 |

The daily file covers a subset of the food-log sample. Of the food-entry rows, 6,467,980 match a daily record and 7,406,300 do not. Inner-joining to the daily table would therefore change the sample substantially. Current weight and fixed age agree across both files for every matched food row. Preserve the intended population when choosing a join.

## Download and Read

The compressed CSVs are attached to the repository's [mHealth teaching-data release](https://github.com/nene88991999/BADM534-Marketing-Analytics/releases/tag/mhealth-teaching-2026-10-23):

- [Daily records](https://github.com/nene88991999/BADM534-Marketing-Analytics/releases/download/mhealth-teaching-2026-10-23/daily_records.csv.gz)
- [Food entries](https://github.com/nene88991999/BADM534-Marketing-Analytics/releases/download/mhealth-teaching-2026-10-23/food_entries.csv.gz)

Run `python3 download_data.py` from this folder to download both files into `data/` and verify their SHA-256 hashes against [manifest.json](manifest.json). The downloader uses only Python's standard library. Data files are stored as release assets so a normal Git clone remains small. A local copy of the same files is kept in the instructor's Dropbox course folder.

Read the [data dictionary](DATA_DICTIONARY.md) before analysis. Python examples require pandas. A bounded first inspection is:

```python
from pathlib import Path
import pandas as pd

data = Path("data")
sample = pd.read_csv(data / "food_entries.csv.gz", nrows=1000)
print(sample.columns.tolist())
print(sample.isna().sum())

daily = pd.read_csv(data / "daily_records.csv.gz")
assert not daily.duplicated(["Userid", "Fancydate"]).any()

for chunk in pd.read_csv(data / "food_entries.csv.gz", chunksize=100000):
    # Add an analysis with explicit observation units and aggregation rules.
    pass
```

The daily file should pass the unique-user-day check. `manifest.json` records the expected row counts and complete-source preparation status. A full food-file read is substantially larger in memory than its compressed download.

## Course Applications

| Module | Question | Required Check |
| --- | --- | --- |
| M1–M2 | How do food-entry records become customer-day summaries? | Validate joins, prevent repeated daily totals from being summed, and distinguish missing days from zero activity. |
| M3 | How does recorded consumption vary with a customer's food variety? | Define within-customer comparisons, the relevant timing, and uncertainty for repeated observations. |
| M4 | Which customers have similar observed consumption patterns? | Build features using an explicitly defined prior period and assess segment stability. |
| M5 | Can food descriptions be classified into useful categories? | Compare transparent text baselines and AI-assisted labels, with distinct descriptions held out for evaluation. |
| M7 | Which items will appear in the next basket? | Keep baskets intact, use chronological splits, and compare popularity and personal-frequency baselines. |
| M8 | How do familiarity, variety, and stated goals change a recommendation? | Distinguish ranking objectives, observed behavior, and causal customer outcomes. |

An AI coding assistant can implement an explicitly specified pipeline and propose diagnostics. Verify joins, units, totals, and a small hand-worked calculation before running it on the full files. The [agent guide](AGENTS.md) records the dataset-specific checks. Assignment rules remain those in the released assignment brief.

## Provenance and Preparation

Nathan Yang supplied `data_everyday.csv` and `data_final_25.csv` from the mHealth food-log research folder and authorized publication of the transformed teaching copy. The files describe 2016 records. Their sample restrictions and relationship to final published analysis samples are not fully documented in the supplied folder. No additional open-data license has been specified.

[Ling and coauthors (2022)](https://doi.org/10.1145/3485447.3514193) develop goal-oriented recommendations from daily food histories. [Nielsen and coauthors (2022)](https://doi.org/10.1086/720453) study consumption variety and FOODVAR. The course files illustrate related questions; they are not labeled as exact replication data for either paper.

[prepare_data.py](prepare_data.py) implements the transformation using pandas and NumPy. It requires separate source files and a private key path. The instructor retains the key outside Git so repeated builds produce the same transformation. The manifest identifies source and output hashes, the noise rule, and verification summaries. The original sources and private key are not part of this repository.

[redact_provider.py](redact_provider.py) standardizes provider references in text labels to mHealth using a separately held pattern file. There are 100 replacements in the food file. The pattern and the original provider name are not distributed. Food and calorie values are otherwise retained.

The [full-file verification report](verification.json) records checksums, row counts, identifier formats, excluded columns, cross-file matches, and the BMI calculation. To repeat these checks after downloading, run `python3 verify_data.py --report data/verification.json`. The transformation tests use invented records and run with `python3 -m unittest test_prepare_data.py`.

Weight-based conclusions must account for the perturbation. Apparent movements smaller than the added noise cannot be interpreted as measured changes in body weight. The supplied schemas do not document random assignment or recommendation exposure, so offline predictive performance does not identify a causal recommendation effect.

## Recurring Course Examples

Use the [M1–M8 analysis programs](recurring_examples/README.md) for a deterministic 370-user cohort, audit and sanity checks, nutrition-informed filtering sensitivity, regression, segmentation, text classification, experiment planning, and recommendation evaluation. The lecture notes print the same Python source. The programs preserve the released files and keep cache tables out of Git.
