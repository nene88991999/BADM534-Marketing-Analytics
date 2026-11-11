# AI Evidence and Evaluation

Two original, synthetic examples connect earnings-call interpretation to source selection and evaluation of AI graders. The files contain fictional excerpts, hand-authored answers, reference judgments, and stipulated grader decisions. No model responses were collected. All calculations use Python 3.10 or later and the standard library.

## Run

From the repository root:

```sh
python3 03_Data_and_Code/AI_Evidence_and_Evaluation/source_selection.py
python3 03_Data_and_Code/AI_Evidence_and_Evaluation/evaluate_graders.py
python3 -m unittest discover -s 03_Data_and_Code/AI_Evidence_and_Evaluation -p 'test_*.py' -v
```

Paths resolve from the scripts, so these commands also work from another directory with the appropriate script path. Each script overwrites its own derived results. Both programs and six independent small-case checks passed on November 11, 2026. [Verification](verification.json) records the runtime and file hashes.

## Inputs and Outputs

| Program | Inputs | Expected Output |
| --- | --- | --- |
| [Source selection](source_selection.py) | [Four synthetic sources and twelve stipulated answers](data/source_cases.json), covering the same four questions in three conditions | [Claim-level records](results/source_claims.csv) and [summary](results/source_summary.csv): four cited answers in every condition; supported counts 4, 2, and 4 |
| [Grader evaluation](evaluate_graders.py) | [Twelve public practice cases](data/grader_cases.json) and [36 stipulated decisions](data/grader_predictions.csv) | [CSV](results/grader_summary.csv) and [JSON](results/grader_summary.json): permissive and cautious balanced accuracy both 0.8125; imposed total loss 11 and 2.5 units |

The source-selection calculation uses supplied reference annotations. It does not automatically assess semantic entailment. The three conditions are curated evidence, the same evidence plus a misleading memo, and the original collection after source review. Their saved answers are imposed illustrations, so differences do not estimate a model's response to changing context.

The grader set contains eight reference PASS cases and four reference FAIL cases. Every grader is scored on all twelve cases. ABSTAIN, absent rows, and invalid strings remain in the reference-class denominators and are reported separately. A false pass means approving a reference FAIL case. The loss illustration assigns ten units to a false pass, one to a false rejection, and one-half to referral. Referral assumes perfect human resolution and sufficient capacity. These are illustrative decision costs, not estimated financial or consumer losses.

## Definitions and Use

[DATA_DICTIONARY.md](DATA_DICTIONARY.md) defines IDs, labels, denominators, and units. [The public practice lab](../../07_Labs/AI_Evidence_and_Evaluation/README.md) supplies a live-model protocol, coding tasks, independent explanation prompts, and a rubric-design discussion. These materials establish no grading requirements or course-wide AI policy.

To evaluate separately saved responses, use CSV columns `grader,case_id,prediction`, with exactly one row per grader and case. Labels are exactly `PASS`, `FAIL`, or `ABSTAIN`. Duplicate and unknown IDs raise errors; missing or invalid predictions are retained as unscored cases. For example:

```sh
python3 03_Data_and_Code/AI_Evidence_and_Evaluation/evaluate_graders.py --predictions /path/to/predictions.csv --output /path/to/evaluation
```

This command scores the disclosed twelve-case practice set. Changing the cases requires a separately documented reference set and the `evaluate` function. The public labels have already been exposed: performance on these cases is practice agreement, not fresh evidence of generalization. Keep model versions, prompts, corpus versions, run order, and resource use with any new experiment. Save no credentials or private student records in this repository.

## Course Connections

Complete Python appears in M5 §§5.19–5.20, beside two TikZ diagrams. M1 §1.14 connects specifications and independent checks; M7 §7.26 connects grader scores, selective coverage, and error costs. Session 7 uses the source-selection case, and Session 11 revisits grader evaluation. The examples extend the [earnings-call case](../Earnings_Calls/README.md) using wholly fictional inputs.

[The resource guide](../../01_Resources/19_AI_Practice_and_Evaluation/README.md) records the Stanford CS193T activities that motivated the adaptations. All cases, scripts, reference labels, and diagrams in this folder are original course material.
