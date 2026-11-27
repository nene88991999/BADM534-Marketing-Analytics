# AI Workflow Evaluation

This is optional, ungraded practice. Current assignment briefs determine assessment-specific AI permissions.

## A Fixed Logging Population

An outreach team needs the distribution of recorded logging activity among customers observed earlier in the year. Read the [task dictionary](../../03_Data_and_Code/Agent_Workflows/DATA_DICTIONARY.md). Explain the roster, observed-day unit, included start, excluded end, and meaning of a zero. Run the [reference calculation](../../03_Data_and_Code/Agent_Workflows/logging_reference.py) and reconcile July's 6,455 observed user-days with its 11,098 possible user-days. Explain why the 39 users without July records remain in the denominator.

## Check by Hand

Use the invented roster A, B, and C over the half-open interval from July 1 to August 1. A has records on June 30 and July 1, including a repeated July 1 record; B has records on July 31 and August 1; C has none. User Z, who is outside the roster, has a July 3 record. Counting distinct eligible days gives A=1, B=1, and C=0, with a mean rate of 2/93. Explain how the roster, date boundaries, and duplicate rule produce these counts, and why counting food entries would answer a different question.

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

Run [workflow_costs.py](../../03_Data_and_Code/Agent_Workflows/workflow_costs.py), then lower the hypothetical analyst cost to $30 per hour. Explain which cost categories change and how that changes the preferred workflow. The calculation assesses sensitivity to an assumed wage; estimating actual labor savings would require observed time and cost evidence.

Consider a cancellation agent instructed to require a retention survey before accepting a customer's unambiguous request to cancel. State the customer's requested outcome, the firm's objective, the action performed, and the relevant sources of authority. Apply the Kantian and Confucian arguments from M9. Explain what additional evidence is needed to assess the firm's claim that the procedure benefits customers.

## Reconstruct Published Coding Evidence

Read the [coding-workflow study guide](../../01_Resources/40_Econometric_Coding_Workflows/README.md), then run:

```sh
python3 03_Data_and_Code/Agent_Workflows/benchmark_evidence.py
```

Reconstruct 14,021 successes from 14,400 assigned agent runs, 41 loud failures, and 338 silent failures. Calculate the fraction of all assigned runs with a silent failure and the fraction of failures that are silent. Explain how a workflow can improve overall accuracy while leaving a larger silent share among its remaining failures. Distinguish the published model results from the original course calculations below.

Use `benchmark_prompt_contrasts.csv` to compare the example's percentage-point gains with its proportional reductions in no-example failures. Explain why the interaction's interpretation changes with the outcome scale. Identify the shared task and dataset structure before proposing a confidence interval. The supplied aggregate tables support arithmetic reconstruction; reproducing the authors' intervals requires the individual task records.

## Find Errors in Executable Programs

Run the constructed-error exercise and its independent tests:

```sh
python3 03_Data_and_Code/Agent_Workflows/semantic_checks.py
python3 03_Data_and_Code/Agent_Workflows/test_coding_evidence.py
```

Inspect the complete Python in M7 §7.46. Predict which programs preserve total logging days before opening `semantic_checks.csv`. For July, distinguish the effects of counting entries, including August 1, using 30 exposure days, shifting customer labels, and omitting zero-log users. Explain why a range check catches the entry-count error while a correct overall mean fails to detect reassigned customers.

The `complete` column evaluates the required roster and fields; it does not evaluate numerical correctness. Explain why omitting a zero-log user produces incomplete output under this contract. Rewrite the contract to request only an aggregate mean and explain how the same sample-selection mistake could become a complete but wrong result.

Extend the synthetic A/B/C tests with an additional boundary date and a repeated date. State the correct result by hand before testing it. Keep source records unchanged. Compare the independent SQL result with the reference calculation, then explain which errors could survive agreement between two programs that share the same mistaken specification.

## Value Additional Review

Run `decision_costs.py` and reconcile the seven-dollar break-even loss in M8 §8.30. At ten dollars per undetected error, calculate the expected cost difference over 1,000 tasks. Increase the checked workflow's review time to one minute and recompute the threshold. Explain how the comparison changes if the remaining errors differ in severity across workflows. All inputs are hypothetical.

For optional live practice, use the [three-workflow protocol](../../03_Data_and_Code/Agent_Workflows/EXPERIMENT_PROTOCOL.md#separate-comparison-of-three-coding-workflows). Keep the verification instruction common and use synthetic practice records with the model. Evaluate frozen programs locally on mHealth. Describe the evidence required before calling an observed difference a reliable improvement across business tasks.
