# Recurring mHealth Examples

These executed Python examples follow the same food-log cohort across M1–M8. The [lecture notes](../../../06_Lecture_Notes/README.md) contain the analysis code, definitions, results, and interpretations. The cohort includes 370 users, 917,153 food entries, and 76,804 observed user-days. It retains each selected user's full 2016 history using a deterministic rule on the public pseudonym. It is not a population-representative sample.

## Run

From the repository root, use Python 3.13 and install [requirements.txt](requirements.txt) into an environment:

```sh
python -m pip install -r 03_Data_and_Code/mHealth/recurring_examples/requirements.txt
python 03_Data_and_Code/mHealth/recurring_examples/run_all.py
```

`run_all.py` verifies the release checksums through `download_data.py`, downloads missing release files, builds the bounded cohort, executes the audit and nutrition analysis, runs the logic checks, and executes M1–M8 in order. The first preparation reads the 304 MB compressed food file. The local Parquet cache is ignored by Git; delete `cache/` to rebuild. Derived caches depend on the release manifest hash, cohort threshold, and preparation version. Calculations use local processing and make no external AI requests. Subsequent module scripts can be run individually. Run M7 before M8 because M8 reads the selected history window from `results/M07.json`.

The complete release files are stored in `../data/`, outside Git, and distributed as [GitHub release assets](https://github.com/nene88991999/BADM534-Marketing-Analytics/releases/tag/mhealth-teaching-2026-10-23). Read the [dictionary](../DATA_DICTIONARY.md) and [release manifest](../manifest.json) before changing a measurement.

## Examples and Outputs

| Program | Question and Output |
| --- | --- |
| `common.py` | Select the cohort, construct observed days and baskets; write `results/cohort.json`. |
| `audit.py` | Check keys, selected-field duplicates, age consistency, daily totals, and calorie review flags; write `results/audit.json`. |
| `nutrition.py` | Compare adult, positive-energy, percentile, and accounting-consistency samples; calculate explicitly hypothetical Goldberg bounds; write `results/nutrition.json`. |
| `m01.py` | Audit join coverage and hand-check a repeated daily total. |
| `m02.py` | Compare breadth and calorie-share variety, and distinguish missing calendar days from observed days. |
| `m03.py` | Estimate next-calendar-day descriptive regressions, customer-clustered intervals, and a range-restriction sensitivity. |
| `m04.py` | Form segments using January–June behavior and describe later logging; keep hypothetical financial and choice inputs separate. |
| `m05.py` | Compare entry-level and unseen-description text evaluation, lookup and TF-IDF/naive-Bayes baselines. |
| `m06.py` | Use historical logging variance for prospective power and a sharp-null randomization simulation. |
| `ranking.py`, `m07.py` | Tune history length in July and evaluate popularity and personal category frequencies in September. |
| `m08.py` | Compare a fixed novelty-bonus grid on the same held-out baskets. |
| `test_logic.py` | Check repeated totals, invalid shares, calendar gaps, duplicate joins, future-information exclusion, and Black's published Table 8 bounds. |
| `reporting.py` | M1, Section 1.10: fixed-cohort monthly business review with source checksum, units, and explicit denominators. |
| `recency.py` | M2, Section 2.13: June 30 recency/frequency snapshot and July logging, including zero-log users. |
| `logging_gaps.py` | M4, Section 4.13: first confirmed 14- or 28-day logging gap, risk sets, and administrative censoring. |
| `topics.py` | M5, Section 5.12: training-period TF-IDF/NMF, future descriptions, and distinct-description versus entry-weighted topic shares. |
| `cuped.py` | M6, Section 6.15: prior-period adjustment with a coefficient frozen before the outcome window; power and sharp-null simulation. |
| `association_rules.py` | M7, Section 7.17: training-selected category association, future support/confidence/lift, and a user bootstrap. |
| `claim_checks.py` | M8, Section 8.11: constructed structured claims checked against computed evidence; no LLM requests. |
| `visualization.py` | M2, 2.14, and M3, 3.6.1: complete user-month pairs, conditional denominators, exact ECDFs, and paired-user uncertainty. |
| `visualization_charts.py` | M2, 2.15: three generated TikZ figures and an aggregate-data Altair HTML chart with a month selector. |
| `chart_audit.py` | M8, 8.12: four constructed chart errors checked against independently computed numerators and denominators. |
| `test_visualization.py` | Five small-data checks of month lengths, duplicate dates, empty months, CDF ties, paired resampling, and chart mistakes. |
| `test_extension_logic.py` | Seven small-data checks for counting units, future exclusion, censoring ties, gap confirmation, adjustment variance, numerical claims, and an IV slope. |

Each module writes `results/M0n.json`. M2 and M4 also write compact aggregate CSV tables. `results/environment.json` records actual software versions. These outputs were generated by execution, not entered by hand. Small floating-point differences across environments are possible, and clustering labels are ordered by prior logging frequency.

The seven additional programs write correspondingly named JSON results. Recency and gap curves also have aggregate CSV companions. They run after M1–M8 in `run_all.py`, with no additional dependencies. Each can also run on its own after downloading the release. Their full source is embedded in the notes. The separately labeled [price-instrument simulation](../../Lecture_Examples/price_iv.py) uses synthetic data and runs with `python 03_Data_and_Code/Lecture_Examples/price_iv.py` from the repository root. [Resource integration](../../../06_Lecture_Notes/RESOURCE_INTEGRATION.md) records source references and execution status.

## Interpretation and Verification

- `Calories` is an item-level source field; `Foodcalories` is a repeated daily source field. Their disagreement is preserved and measured. No undocumented quantity multiplier is applied.
- A day absent from the food file is unobserved. Zero filling is used only for an explicitly defined logging indicator or count, never for food consumption.
- Missing categories are `Unclassified` for breadth and calorie-share variety, and excluded from category recommendation and text targets. Negative or missing item calories and nonpositive item totals make calorie-share variety undefined.
- Nutrition sensitivity screens are separate analysis populations. Ages span 17–76 in the cohort; the adult sensitivity base restricts age at January 1 to at least 18. Neither percentile nor accounting-agreement screens certify complete intake. No individualized physiological screen is applied without the missing validated inputs.
- The full-period descriptive cohort and its observed-day summaries are not prospective enrollment samples. M4, M6, and M7 separately enforce earlier-period eligibility and feature windows.
- M3 estimates associations, M5 and M7 evaluate prediction, M6 imposes a zero-effect randomization simulation, and M8 changes a ranking objective. None estimates a causal health benefit from these records.
- Source food categories are not validated nutrition-quality labels. No raw identifiers, birthdays, private transformation keys, or individual prediction exports are added to these results.
- Recency is measured at a fixed date; logging frequency counts distinct days. No monetary-value variable is inferred from calories or activity.
- A confirmed logging gap is an event defined by its duration threshold. Administrative censoring is separate from an event, and the survival comparison conditions on July return.
- Topic loadings are put on a common component-vector scale before comparison. Dominant components are text patterns; July proportions report their observation units and unassigned texts.
- The CUPED coefficient is learned from March–April, uses May activity as the baseline, and is evaluated on June outcomes. Randomized assignments are imposed under a zero-effect null. The coefficient's transfer gain is measured rather than assumed.
- Basket associations use distinct categories per day, select candidates and a pair before July, and resample users for later-period uncertainty. Their lift does not estimate a recommendation effect.
- The claim checker validates declared fields against numerical evidence. It is not a general semantic or factual validator for unrestricted prose.

[Original nutrition sources](../../../01_Resources/12_Nutrition_and_Dietary_Data_Quality/README.md) support the measurement distinctions and screening discussion. Matching Python source blocks in the Markdown notes can be checked with `python scripts/check_lecture_code.py`.

## Visualization Replication

The [visualization companion](results/VISUALIZATION.md) describes the chart tables and outputs. Run `visualization.py`, then `visualization_charts.py` and `chart_audit.py`. These programs also run at the end of `run_all.py`, with Altair 5.5.0 included in the requirements. The HTML contains aggregate data and uses browser JavaScript from a CDN; it needs internet access for the charts, while its HTML table works offline. The figures use editable TikZ and the Illinois palette.
