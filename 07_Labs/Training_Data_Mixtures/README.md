# Combining Sources and Evaluating Customer Service

A retailer proposes combining demonstrations from product support and subscription management. Determine what the training examples identify and which service comparisons support deployment. This is optional, public, ungraded practice linked to [M7 §§7.33–7.35](../../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md) and Session 11.

## Reproduce the Three Comparisons

Read the [example guide](../../03_Data_and_Code/Training_Data_Mixtures/README.md) and [data dictionary](../../03_Data_and_Code/Training_Data_Mixtures/DATA_DICTIONARY.md). Run the three analysis programs and ten checks. Separate outputs from the exact synthetic ridge model, the imposed service roster, and the published experiment. State the observation unit and outcome in each case.

For the ridge model, solve the two normal equations with two Source A rows, three matched Source B rows, and effective penalties two and eight. Verify task contribution 8/33 and tag contribution 5/33. Explain how the original feature representation `(2,1)` for A, `(2,0)` for B, and common coefficient penalty eight produces the same contributions. Then compare reference, equal-scale, and weaker-penalty regimes in the saved results.

## Change One Assumption

In a separate copy, replace the sum loss with mean squared error and keep the numerical penalty fixed. Derive the equivalent effective penalties before changing the code. Compare the added-data curve with the original. Explain why changing normalization changes the experiment. Preserve the unrelated-task comparison and the all-Source-B endpoint.

Ask an AI coding assistant to add a sensitivity table with explicit feature scales, penalties, counts, and score units. Inspect its algebra against the original-feature calculation above. Check whether it adds an intercept, normalizes the loss, or labels a score as a probability. Record material AI assistance accurately.

## Preserve Customer Context and Pairing

Reconstruct the aggregate service rate as a weighted average of the three contexts. Recover the 27 gains and 27 losses using request IDs. Calculate cancellation resolution per attempt and per received response. Explain how reporting only completed responses changes the comparison.

Evaluate a hypothetical decision to give cancellation requests more weight. State the chosen weights and the normative reason for them separately from the observed request shares. A weighting rule expresses a managerial objective; it does not establish informed consent, truthful explanations, or the customer's ability to complete a decision. No required weight or numerical acceptance threshold is supplied.

## Trace the Published Outcome

Find the three 30%-share runs in the archived epoch histories. Apply the documented last-record rule, then compare epoch 10 with each run's maximum. Explain why the final mean is 58.67% and the peak mean is 68.67%, and identify which one Figure 3 uses. A repeated epoch line is a recording event, not a new independent training run.

The conditional-misalignment experiment selects a checkpoint to expose possible unwanted behavior. Design a separate evaluation for a fixed deployment checkpoint using untouched request IDs and judgments. Keep repeated responses grouped by request when computing uncertainty. Specify how human assessment would sample positive and negative machine judgments, and record unanswered requests and unscored responses.

## Recommendation

State the proposed service change, source versions, the training mixture, the evaluation population, and the outcomes needed to justify deployment. Address access to cancellation, refunds, and correction. Distinguish evidence about a practice from an inference about intention. Public practice cases can guide development; a fresh evaluation is needed after revising a configuration against them.
