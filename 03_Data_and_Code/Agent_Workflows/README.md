# AI Workflow Evaluation

A manager needs a reproducible measure of recorded customer activity before selecting an outreach population. The mHealth tasks calculate logging days for a roster fixed using earlier records. An original factorial protocol varies the information and feedback supplied to a coding assistant while holding its model fixed.

## Run the Local Calculations

Use Python 3.11 or newer with the standard library. Run from the repository root:

```sh
python3 03_Data_and_Code/Agent_Workflows/logging_reference.py
python3 03_Data_and_Code/Agent_Workflows/workflow_costs.py
python3 03_Data_and_Code/Agent_Workflows/test_workflows.py
python3 03_Data_and_Code/Agent_Workflows/evaluate_submission.py 03_Data_and_Code/Agent_Workflows/results/development_reference.csv
```

The compact task inputs are included. To recreate them from the existing public mHealth release, first follow its [download instructions](../mHealth/README.md), then run `python3 03_Data_and_Code/Agent_Workflows/build_tasks.py`. The builder verifies the compressed source checksum and reads it once. It makes no network requests and exports no food descriptions, weight fields, ages, or original identifiers.

## Inputs and Outputs

- [Data dictionary](DATA_DICTIONARY.md): units, dates, eligibility, and field definitions.
- [Task manifest](manifest.json): source checksum, selection, row counts, and input hashes.
- [Reference results](results/README.md): observed counts and their interpretation.
- [Experiment protocol](EXPERIMENT_PROTOCOL.md): four configurations, run records, costs, and evaluation separation.
- [Optional ungraded lab](../../07_Labs/Agent_Workflows/README.md): guided calculations and controlled errors.
- [Verification record](VERIFICATION.md): local execution and independent checks.

The saved logging results are calculations from transformed real mHealth records. Cost scenarios use explicitly hypothetical inputs. Published model results are separately attributed to the authors of the coding benchmark. No model was called for the course, no empirical comparison of the four AI configurations was run, and no upstream repository code was executed. A correctly generated CSV checks a measurement; it does not establish a nutrition or health outcome.

## Coding Workflows and Undetected Errors

Three original programs extend the examples using Python's standard library:

```sh
python3 03_Data_and_Code/Agent_Workflows/benchmark_evidence.py
python3 03_Data_and_Code/Agent_Workflows/semantic_checks.py
python3 03_Data_and_Code/Agent_Workflows/decision_costs.py
python3 03_Data_and_Code/Agent_Workflows/test_coding_evidence.py
python3 03_Data_and_Code/Agent_Workflows/build_coding_figures.py
```

`benchmark_evidence.py` reads three unchanged CC0 aggregate tables from [the source collection](../../01_Resources/40_Econometric_Coding_Workflows/README.md). It reconstructs 43,200 assigned runs, failure denominators, prompt contrasts, and token cost per additional success. The authors' original model runs, scoring, and bootstrap are not repeated.

`semantic_checks.py` applies eight original correct or deliberately incorrect programs to each mHealth task. It compares execution, complete roster output, total-day agreement, and per-user numerical agreement. The shifted-user case preserves July's 6,455 days and 58.16% mean while changing 331 users' values. These cases are designed counterexamples, not a measured distribution of model errors.

`decision_costs.py` compares 1,000 hypothetical analysis tasks with explicitly supplied API charges, review effort, undetected-error probabilities, and conditional losses. The checked workflow breaks even at a loss of seven dollars per undetected error. `build_coding_figures.py` writes two editable TikZ files from the corresponding numerical tables; the note builder renders them.

Full programs appear in M1 §1.19, M7 §7.46, and M8 §8.30. M3 §3.18 and M6 §6.31 connect uncertainty checks and interaction scales. [Output definitions](results/README.md), [input definitions](DATA_DICTIONARY.md), [the extension manifest](coding_evidence_manifest.json), and [verification](VERIFICATION.md) record the evidence and its scope. The longer exercise remains optional and ungraded.

## Source and Course Connections

[Agent Harness Engineering: A Survey](../../01_Resources/35_Agent_Workflow_Evaluation/README.md), especially §§5, 8, 9, and 11, motivates evaluation of the model together with its surrounding execution system. The original course adaptation connects M1 §1.17, M6 §6.29, M7 §7.41, M8 §8.26, and M9 §9.20. The [companion catalog](https://github.com/Picrew/awesome-agent-harness) supplies references; the programs here are original course implementations.
