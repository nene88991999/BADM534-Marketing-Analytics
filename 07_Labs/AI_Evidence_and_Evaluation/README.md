# Evidence Selection and AI Grader Evaluation

Marketing Analytics. By Nathan Yang.

Public, ungraded practice. The exercises establish no assignment deadline, grading weight, or course-wide AI policy. [M5 §§5.19–5.20](../../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md) contain the explanations and complete Python. [Data and code](../../03_Data_and_Code/AI_Evidence_and_Evaluation/README.md) provide dependencies, commands, expected outputs, and verification.

## The Decision

A marketing team uses earnings calls to identify pricing statements for further review. It must preserve what was actually said, distinguish an analyst question from a company decision, and decide which generated claims require a human check. The supplied retailer, excerpts, answers, and grader decisions are fictional.

## Preparation and Independent Judgment

Read S1–S3 and the four questions in [source_cases.json](../../03_Data_and_Code/AI_Evidence_and_Evaluation/data/source_cases.json). Write a short answer to each before looking at the saved responses. Define what a supported answer would contain, including the speaker, population, and scope of a causal claim. Calculate 72 divided by 100 and state whose outcome that fraction describes.

## Activity A: Source Selection

1. Run `source_selection.py` using the command in the data-and-code README. Check all twelve claim-level rows against the source text and reference reasons.
2. Explain why citation counts remain unchanged when the supported-answer count changes. Identify the exact inferential step in each unsupported answer.
3. Compare S4 with S1 and S2. Assess whether S4 adds evidence. A conflicting source with credible new observations would require a different judgment from this unsupported memo.
4. Revise one flawed answer so that its attribution and substantive conclusion are defensible. Explain whether merely adding a citation is enough.

For a live-model extension, use only these public fictional excerpts. Open separate fresh conversations with the same model version and settings. Give one S1–S3 and another S1–S4, with the same four questions and identical output instructions. Randomize condition order across repeated paired runs. Do not include saved answers or `supported` labels in either prompt. Preserve raw responses, source IDs, prompts, date, settings, latency, and any refusals or missing outputs. Changes within one pair are descriptive; repeated runs are needed to separate sampling variation from a stable context effect. Source review can then be tested in a third fresh condition. Do not assume that the model will reproduce the stipulated teaching answers.

A suitable task prompt is: "Using only the supplied excerpts, answer Q1–Q4. Attribute reported claims, name the source IDs supporting each answer, and distinguish observations, questions, proposals, and causal conclusions. State when the excerpts do not establish an answer."

## Activity B: Evaluate a Grader

Read the rubric and [twelve practice cases](../../03_Data_and_Code/AI_Evidence_and_Evaluation/data/grader_cases.json). Discuss the reference reasons before interpreting a score. PASS means an evidence-respecting statement; it does not certify the ethics of a business practice.

1. Run `evaluate_graders.py`. Reconstruct the permissive grader's confusion counts by hand and compute both class recalls.
2. Explain how the cautious grader obtains the same balanced accuracy while making fewer false approvals and referring one case.
3. Recompute loss with false-approval cost 1, false-rejection cost 1, and review cost 5. Explain why the preferred grader changes when review becomes costly. These costs are imposed decision scenarios.
4. Remove one prediction in a separate copy of the CSV and use `--predictions` and `--output` to score it. Check that the case remains in the denominator. Try an invalid label and a duplicate ID, then explain their different treatment.

For an optional model judge, supply the source excerpts, a fixed rubric, and statement texts. Ask for one of PASS, FAIL, or ABSTAIN for each ID, with a separate reason. Keep reference labels out of the model prompt. The public cases are already disclosed and serve as practice. To estimate generalization, prepare new cases, obtain independent human judgments with reasons, resolve or explicitly report disagreements, freeze the rubric, and evaluate once on cases unused in revision. When reference judgments remain unresolved, report their count and the coverage of the scorable set rather than silently discarding them. The supplied scorer requires both binary reference classes and does not adjudicate disagreements.

## Activity C: Explain and Repair

Give a coding assistant the roster, input schema, output specification, and required checks. Ask it to suggest one change at a time. Reopen the resulting files and compare one score with a hand calculation. Explain, without the assistant, why a missing response is different from a correct rejection. Apply the same reasoning to a new two-case example before looking at its solution.

Compare anonymous outputs using criteria fixed in advance. Record correction time alongside execution time when evaluating whether assistance was useful. An independent explanation checks a specific skill at that moment; it does not establish a long-term effect on learning.

## Discussion and Timing

Session 7 can use 10 minutes for the evidence question and a demonstration, 25 minutes for Activity A, and 10 minutes for independent explanation within its existing 45-minute Python block. Session 11 can use 15 minutes of the existing application block for Activity B, with the remaining 15 minutes retaining forecast interpretation. Activity C and additional live runs are optional practice. The full 170-minute meetings remain unchanged.

Connect the evaluation to Marketing Dialectics: who chose the rubric, whose losses count, and which decisions remain the student's responsibility? A grader can apply a narrow rule consistently while the rule omits an important customer consequence.

## Provenance

These original cases adapt activity ideas from Stanford CS193T. The [resource guide](../../01_Resources/19_AI_Practice_and_Evaluation/README.md) links the selected public assignment pages. No Stanford assessment rules or hidden evaluation data have been adopted.
