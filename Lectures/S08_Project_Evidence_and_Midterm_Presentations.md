# Project Evidence and Midterm Presentations

By Nathan Yang

Session 08. M1-M5. 170 minutes.

[PDF](S08_Project_Evidence_and_Midterm_Presentations.pdf) | [LaTeX](S08_Project_Evidence_and_Midterm_Presentations.tex) | [Session Plan](SESSION_PLAN.md)

## Learning Objectives

- Connect a managerial decision to a defensible analytical comparison.
- Explain a data audit, model choice, and consequential uncertainty.
- Provide evidence-based feedback on an analysis.

## Related Materials

- [M4 lecture notes](../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md)
- [Runnable small examples](../03_Data_and_Code/Lecture_Examples/session_examples.py)
- [Course requirements status](../02_Syllabus/README.md)
- [Ethics and regulation](../06_Lecture_Notes/ETHICS_AND_REGULATION.md)

## Slide 1: Project Evidence and Midterm Presentations

Marketing Analytics. By Nathan Yang.

## Slide 2: A Decision and Its Evidence

- State the action a manager can change.
- Define the outcome, population, and horizon.
- Identify which evidence could change the proposed action.

A presentation should make the decision assessable without requiring the audience to reconstruct the analyst's workflow. A precise unresolved question is useful when the current evidence does not yet support an action.

## Slide 3: A Traceable Data Table

- Name the original unit and the analysis unit.
- Reconcile rows and totals through joins and restrictions.
- Show one manually checked record or aggregate.

A source-to-output audit distinguishes data processing choices from modeling choices. An unexplained change in the population can dominate a later coefficient or chart.

## Slide 4: Evidence Categories

- Descriptive patterns summarize observed records.
- Prediction evaluates outcomes on held-out observations.
- Causal estimates require a justified counterfactual comparison.
- Scenarios calculate consequences under imposed inputs.

These categories can appear in the same project. Each claim should retain the qualifications appropriate to its evidence.

## Slide 5: A Worked Presentation Case

- A paid-plan scenario has high predicted uptake.
- The underlying data contain food logging and no observed payments.
- The decision requires additional evidence on price, retention, and margin.

Observed logging can motivate a segmentation or interface decision. Paid uptake from an imposed logit model is a scenario. A stated-choice study or pilot could supply some of the missing evidence.

Source: M4, Section 4.11, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md

## Slide 6: An Interpretable Figure

- Use a comparison that answers the stated question.
- Label units, denominator, and uncertainty.
- State whether plotted quantities are observed, estimated, or imposed.

A figure should be independently readable. A chart of customer means and an interval for the overall mean require separate explanations of distribution and uncertainty.

## Slide 7: A Reproducible Calculation

- Run from a clean session using documented inputs.
- Show a counterexample that checks a consequential choice.
- Keep complete code and results linked to the claim.

The most informative check is one that would fail under a plausible analytical error. Re-running identical code is useful but does not independently establish a valid interpretation.

## Slide 8: Presentation Discussion

- What is the strongest supported claim?
- Which assumption most affects the decision?
- What evidence should be collected next?

Feedback should identify a concrete comparison or data requirement. A more complicated model is useful only if it addresses a stated limitation in the decision evidence.

## Slide 9: A Revision Decision

- Prioritize the error with the largest consequence for the action.
- Specify the additional data or comparison needed.
- Preserve a reproducible baseline for the revised analysis.

Examples include fixing a multiplied join, changing a leakage-prone split, or measuring actual contribution. These changes can matter more than polishing an already clear chart.

## Slide 10: A Customer-Outcome Audit

- Identify who benefits and who can bear a cost.
- State whether the optimized metric can conflict with customer value.
- Name the relevant jurisdiction and verify the rule's scope.

These questions organize an evidence discussion. They do not establish a graded assignment or replace the eventual project brief.

Source: ETHICS_AND_REGULATION.md.

## Slide 11: Sensitivity and Next Steps

- Report how the action changes across plausible inputs.
- Identify a decision threshold rather than only a point estimate.
- Select a feasible test that reduces consequential uncertainty.

A recommendation can be conditional. Explicitly stating the value or response threshold makes the condition useful for a manager rather than an abstract caveat.
