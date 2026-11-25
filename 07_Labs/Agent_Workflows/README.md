# AI Workflow Evaluation

This is optional, ungraded practice. Current assignment briefs determine assessment-specific AI permissions.

## A Fixed Logging Population

An outreach team needs the distribution of recorded logging activity among customers observed earlier in the year. Read the [task dictionary](../../03_Data_and_Code/Agent_Workflows/DATA_DICTIONARY.md). Explain the roster, observed-day unit, included start, excluded end, and meaning of a zero. Run the [reference calculation](../../03_Data_and_Code/Agent_Workflows/logging_reference.py) and reconcile July's 6,455 observed user-days with its 11,098 possible user-days. Explain why the 39 users without July records remain in the denominator.

## Check by Hand

Use an invented roster A, B, C and a July 1–August 1 half-open interval. A has records on June 30, July 1, and a repeated July 1. B has records on July 31 and August 1. C has none. A separate user Z has a July 3 record. The required logged-day counts are A=1, B=1, C=0. The mean rate is 2/93. Explain each excluded record and why summing the food-entry count would answer a different question.

Run the independent tests from the repository root:

```sh
python3 03_Data_and_Code/Agent_Workflows/test_workflows.py
```

Duplicate a roster key and predict the failure before running the calculation. Replace an ISO date with an ambiguous date and explain why the program rejects it. Keep these invented errors separate from the actual task inputs.

## Evaluate the Checker

Compare the correct vector (1,1,0) with (0,1,1). Both total two days. If outreach prioritizes zero-log users, the second output selects A in place of C. Explain why a grand-total check misses the decision error. Inspect [evaluate_submission.py](../../03_Data_and_Code/Agent_Workflows/evaluate_submission.py), then score the reference CSV as a basic checker sanity check. Its stronger evidence comes from wrong-case tests and the independent SQL comparison.

## Optional Model Comparison

Follow the [experiment protocol](../../03_Data_and_Code/Agent_Workflows/EXPERIMENT_PROTOCOL.md). Hold the model fixed and cross explicit information with independent development feedback. Generate code using the schema and invented small cases; run it locally against the actual records after inspecting its operations. Preserve inputs and restrict the workspace. Freeze the program and prompts before evaluating August.

Record every assigned attempt, its model version, visible files, commands, revisions, elapsed time, charges, analyst effort, and final checker result. Randomize cell order within repeated runs. Report failures and unavailable costs explicitly. Calculate each information and feedback contrast and their interaction. Explain why repeated runs of one task provide narrower evidence than a sample of different business tasks. No model-comparison results are included in the released calculation outputs.

## Cost and Authority

Run [workflow_costs.py](../../03_Data_and_Code/Agent_Workflows/workflow_costs.py). Recalculate the comparison at an analyst cost of $30 per hour and explain which cost categories change. These are hypothetical inputs. A sensitivity calculation does not estimate labor savings.

Consider a cancellation agent instructed to require a retention survey before accepting a customer's unambiguous request to cancel. State the customer's requested outcome, the firm's objective, the action performed, and the relevant sources of authority. Apply the Kantian and Confucian arguments from M9. Explain what additional evidence is needed to assess the firm's claim that the procedure benefits customers.
