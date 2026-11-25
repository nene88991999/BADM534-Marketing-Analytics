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

The saved logging results are calculations from transformed real mHealth records. The cost comparison uses explicitly hypothetical inputs. No model was called, no empirical comparison of the four AI configurations was run, and no upstream repository code was executed. A correctly generated CSV checks a measurement; it does not establish a nutrition or health outcome.

## Source and Course Connections

[Agent Harness Engineering: A Survey](../../01_Resources/35_Agent_Workflow_Evaluation/README.md), especially §§5, 8, 9, and 11, motivates evaluation of the model together with its surrounding execution system. The original course adaptation connects M1 §1.17, M6 §6.29, M7 §7.41, M8 §8.26, and M9 §9.20. The [companion catalog](https://github.com/Picrew/awesome-agent-harness) supplies references; the programs here are original course implementations.
