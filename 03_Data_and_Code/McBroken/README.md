# McDonald's Ice-Cream Availability

**Marketing Analytics · By Nathan Yang**

A service team deciding which restaurants to contact needs a measure of order availability, a stable comparison population, and a forecast that uses information available before the next observation. This case uses the supplied McBroken collection for three applications:

| Module | Question | Executed Program |
| --- | --- | --- |
| M2, §2.16 | How do changing coverage, missing dates, and address keys affect an availability percentage? | `prepare.py`, `api_checks.py`, `coverage.py` |
| M6, §6.16 | How much does a policy contrast depend on the comparison country? | `policy.py` |
| M7, §7.18 | Does previous status improve forecasts on later dates, and how many origins have usable labels? | `predict.py` |

All five programs appear in full in the [lecture notes](../../06_Lecture_Notes/README.md). The parser examples are constructed edge cases; the availability calculations use the supplied observed data.

## Run the Examples

From this directory, install the dependencies in your chosen environment and run:

```sh
python -m pip install -r requirements.txt
python run_all.py
```

This command uses the aggregate CSV files in `data/`, runs five counterexample tests, computes the three analyses, and updates their TikZ sources. It requires no network access. The saved figure PNGs and PDF are rebuilt separately with the lecture-note builder. Python, NumPy, and pandas are sufficient; no API key is needed.

To repeat the full source audit and reconstruct the aggregate teaching tables:

```sh
python prepare.py
python run_all.py
```

The default input is the [supplied resource bundle](../../01_Resources/02_M2_Customer_Data_and_Visualization/mcbroken_api_lab/data/). `python prepare.py --source /path/to/data` accepts another copy of that directory. The [manifest](manifest.json) records source-file sizes and SHA-256 hashes. Daily and weekly teaching tables retain the full archive commit IDs. The original resource scripts explain retrieval from the archive; their live/network collection paths were inspected but were not executed for this adaptation.

## Results and Interpretation

- The audit reconciles 3,053,307 US store-date records with the supplied country totals. The 365-date calendar contains 356 observed US dates, nine missing US dates, and three observed dates with fewer than 2,000 records.
- There are 29,123 address keys and 13,821 exact coordinate pairs. Coordinates are a linkage diagnostic. No coordinate-based deduplication is imposed.
- The equal-day unavailable percentage is 13.18%; pooling records gives 13.37%. Alternative count thresholds are reported in [coverage_sensitivity.csv](results/coverage_sensitivity.csv).
- Around the October 28, 2024, policy effective date, a descriptive US-minus-Canada pre/post contrast is +0.65 percentage points. Using the UK gives +13.37 points. These are calculations of the contrast, with no established causal interpretation.
- In the later forecast period, previous status gives a Brier score of 0.0851 versus 0.1253 for the training-mean forecast. Usable future labels cover 72.39% of eligible origins. Results describe matched observations under the specified screens.

The [data dictionary](DATA_DICTIONARY.md) defines units and exclusions. [Results](results/README.md) describes the figures, numerical outputs, and verification evidence. These files support text-based retrieval and LLM explanations.

## Source and Rights

Underlying observations: Rashiq Zahid, [McBroken](https://mcbroken.com/). Archive: [MrFlynn/mcbroken-archive](https://github.com/MrFlynn/mcbroken-archive). The supplied extraction spans daily snapshots from October 25, 2025, through October 24, 2026, and weekly snapshots beginning in 2020. The public course files are attributed derived tables and original teaching calculations. The archive's software license is Unlicense; a separate license from McBroken for the underlying data was not established. The manifest does not assert that the data are openly licensed.

The [2024 Copyright Office final rule](https://www.govinfo.gov/content/pkg/FR-2024-10-28/pdf/2024-24563.pdf) supplies the policy effective date and scope. The calculation excludes implementation week zero and uses the same 12 pre and 12 post weeks across three countries. The case concerns evaluation design and order availability; it does not estimate a verified mechanical-failure rate or the causal effect of the exemption.
