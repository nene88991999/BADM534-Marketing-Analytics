# Anomaly Detection and Retail Diagnosis

An unusual pattern can call for repairing a service, preserving a successful campaign, or assessing the observation process. [Synthetic retail records](../../03_Data_and_Code/Anomaly_Diagnosis/README.md) contain service interruptions, successful campaigns, and missing observations. The full programs in [M7 §§7.29–7.30](../../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md) calculate detection scores and compare their implications for a service response. It is optional ungraded practice and establishes no submission or AI-use requirement.

## Reproduce the Evidence

Run both programs and the eight checks using the commands in the data-and-code README. Confirm the training, validation, and test counts before examining model results. Identify the three missing measurements and verify that their rows remain in the evaluation. Explain which information determines the score for a missing feature.

Compare the two detection summaries on the same 1,080 test minutes. Explain why 60 detected event minutes include a campaign. Calculate precision from the confusion counts. Distinguish alert minutes outside true windows from alerts on the 720 minutes in wholly nominal runs. Explain why two affected nominal runs can coexist with a small rate of alert minutes.

## Examine Timing and Attribution

Use the payment case to compare [40,60) with [40,65). Identify the continuing support response and explain the 0.80 interval intersection-over-union. Compare the highest-ranked variable with the imposed originating component. State what additional information would justify a repair in an observed retailer setting.

Calculate interval intersection-over-union by enumerating integer minutes for the precise, delayed, and full-window predictions. Explain why all three receive credit from any-overlap scoring. Modify one endpoint and predict the result before running the calculation.

Change the future value in the four-observation missingness example. Verify that earlier values change under backward filling but remain fixed under the training-median rule. Preserve original timestamps after deleting a row and compare them with positional indices.

## Evaluate an Explanation

Follow the [LLM exercise](../../03_Data_and_Code/Anomaly_Diagnosis/LLM_EXERCISE.md), or write the same structured diagnosis independently. Supply only an evidence packet and the variable dictionary before evaluating against the public incident table. Assess numerical support and causal hypotheses separately. Include normal runs in the evaluation and retain unsupported, invalid, and missing responses.

An extension can introduce smaller incidents, simultaneous causes, a drifting baseline, or an independently failing completeness monitor. Choose the change and evaluation criteria before seeing its results. Use separate new runs for final evaluation after revising thresholds, representations, or prompts.
