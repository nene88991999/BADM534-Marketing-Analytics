# Evaluating AI Evidence and Model Updates

A marketing team uses AI to classify catalog entries, assess pricing claims, and summarize customer communications. A replacement can improve average performance while changing the errors, costs, and measurement process that matter to the team. These examples preserve those distinctions.

## Run

Python 3.10 or later and the standard library are sufficient; the programs were executed with Python 3.13.5. From the repository root:

```sh
python3 03_Data_and_Code/LLM_Revalidation/summarize_snapshot.py
python3 03_Data_and_Code/LLM_Revalidation/evaluate_judges.py
python3 03_Data_and_Code/LLM_Revalidation/evaluate_upgrade.py
python3 -m unittest discover -s 03_Data_and_Code/LLM_Revalidation -p 'test_*.py' -v
```

Paths resolve relative to the scripts. Each program overwrites its own results. No model APIs, network requests, credentials, or third-party research programs are executed. The complete sources also appear in M2 §2.21, M5 §5.18, and M7 §7.22 of the lecture notes.

## Inputs and Interpretation

| Program | Inputs and Observation Unit | Expected Result |
| --- | --- | --- |
| [summarize_snapshot.py](summarize_snapshot.py) | Licensed, unchanged source tables: 50 selected claims and 1,000 claim-model observations from Queen and Zou; released fitted expiration dates | Counts 22/17/8/3; eight unreliable model-claim pairs; expired-only mean 15.75 months; 16.0% estimated expired by twelve months |
| [evaluate_judges.py](evaluate_judges.py) | Four stipulated mean scores on a common 0-100 rubric; the same saved output set per generator is evaluated by both judges | A diagonal comparison gives +17 points; holding the judge fixed gives +2 points |
| [evaluate_upgrade.py](evaluate_upgrade.py) | 100 constructed paired cases: 80 routine and 20 consequential, with binary correctness and stipulated failure costs of $1 and $20 | Correct answers rise from 78 to 86, but total loss rises from $60 to $128; 14 cases improve and six regress |

The published snapshot is empirical source data. The two upgrade examples are entirely synthetic and contain no observed provider performance, customer outcomes, or estimated monetary losses. They demonstrate arithmetic and evaluation design under imposed inputs. There are no missing outcomes in the constructed cases, and no cases are excluded.

`summarize_snapshot.py` retains the upstream unreliable-pair flags. Its Kaplan-Meier calculation uses all 50 released classifications, treats estimated event dates as fixed, and censors unexpired claims on September 30, 2026. Three interval-based dates use the authors' displayed estimates; two dates derive from a recent-model count. It does not estimate interval-censored survival or uncertainty in the fitted dates. The result is descriptive of this selected collection, with the usual independent-censoring condition needed for a population survival interpretation. Source counts, thresholds, configuration differences, and reproduction limits are described in the [resource guide](../../01_Resources/14_LLM_Evidence_and_Revalidation/README.md).

The upgrade example holds cases, labels, task weights, and the scoring rule fixed. The paired counts distinguish recoveries from regressions. Routine-task failures fall by twelve while consequential failures increase by four, so the new configuration reduces stipulated failure loss only when the consequential-to-routine cost ratio is below three. Setup costs and inference fees are absent from this deliberately limited comparison.

The zero-failure calculation assumes independent Bernoulli trials with a common failure probability. Zero failures in 100 trials imply a one-sided 95% upper bound of 2.95%, rather than proving zero risk. Repeated outputs from one prompt or one customer can be dependent and require a different sampling design.

## Outputs and Checks

[Results](results/README.md) links the aggregate tables, complete paired cases, and JSON calculations. [DATA_DICTIONARY.md](DATA_DICTIONARY.md) defines variables and units. Four small-case tests check censoring at tied times, a judge-induced ranking reversal, costly regressions hidden by equal averages, and the exact zero-failure bound. Source hashes, row counts, and figure reconciliation are recorded with the course verification files.

For a new evaluation, preserve the current configuration and compare the challenger on both fixed regression cases and fresh cases from the intended task population. Record model IDs, dates, prompts, tools, reasoning settings, parser, scorer, and evidence provenance. Independently assess consequential outcomes. Public teaching examples are suitable for practice; repeated adaptation to their published answers does not supply a fresh test.
