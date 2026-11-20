# Prediction, Validation, and Marketing Actions

By Nathan Yang

Session 11. M7. 170 minutes.

[PDF](S11_Prediction_Validation_and_Marketing_Actions.pdf) | [LaTeX](S11_Prediction_Validation_and_Marketing_Actions.tex) | [Session Plan](SESSION_PLAN.md)

## Learning Objectives

- Design a holdout that matches deployment and prevents leakage.
- Compare ranking, calibration, and decision costs.
- Assess coverage and missing future labels in an availability forecast.
- Compare identical rankings with different probability losses and demand forecasts.
- Construct prediction intervals and label sets; compare marginal coverage with segment and routing outcomes.
- Evaluate grader coverage and asymmetric error costs against explicit reference judgments.
- Separate anomaly detection, variable localization, event timing, and evidence for a diagnosis.

## Related Materials

- [M7 lecture notes](../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md)
- [Runnable small examples](../03_Data_and_Code/Lecture_Examples/session_examples.py)
- [McBroken prediction case](../03_Data_and_Code/McBroken/README.md)
- [Ethics and regulation](../06_Lecture_Notes/ETHICS_AND_REGULATION.md)
- [AI workflow calculations](../03_Data_and_Code/AI_Workflows/README.md)
- [LLM Evidence and Revalidation](../03_Data_and_Code/LLM_Revalidation/README.md)
- [Statistical Graphics: Data and Code](../03_Data_and_Code/Statistical_Graphics/README.md)
- [PyStatlas Resource Guide](../01_Resources/17_PyStatlas_Statistical_Graphics/README.md)
- [Conformal Prediction: Data and Code](../03_Data_and_Code/Conformal_Prediction/README.md)
- [Evidence and Grader Practice](../07_Labs/AI_Evidence_and_Evaluation/README.md)
- [Anomaly Diagnosis: Data and Code](../03_Data_and_Code/Anomaly_Diagnosis/README.md)
- [Anomaly Diagnosis: Optional Practice](../07_Labs/Anomaly_Diagnosis/README.md)

## Slide 1: Prediction, Validation, and Marketing Actions

Marketing Analytics. By Nathan Yang.

## Slide 2: A Service-Capacity Decision

- A team can review 100 customers each week.
- Predictions use information available before that week.
- The outcome and review benefit determine the useful metric.

A model selected on overall accuracy can fail to identify the cases that the team can help. The intervention value and the forecast are separate quantities.

Source: M7, Section 7.1, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 3: Validation Reproduces Deployment

The deployment population determines the appropriate holdout.

**Figure description:** Random rows, whole-customer holdouts, and later-period holdouts test different forms of generalization.

[Editable TikZ](../06_Lecture_Notes/figures/M07_splits.tex)

New-customer prediction requires separation by customer. Future prediction for returning customers requires separation in time. Some deployments require both.

Source: M7, Section 7.4, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 4: Selection on Development Accuracy

Synthetic independent chance predictions: 80 development cases per candidate.

**Figure description:** Expected selected development accuracy rises from 50% for one candidate to 56.49%, 60.40%, and 63.93% for five, twenty, and one hundred candidates. Expected fresh accuracy stays at 50%.

[Editable TikZ](../06_Lecture_Notes/figures/M07_repeated_selection.tex)

Each candidate has true accuracy one-half under the imposed independent Bernoulli model. The maximum development score increases with the number compared. Fresh test correctness is independent of selection. The program verifies the analytic expectation and simulates 2,000 repetitions with 200 test cases. Real prompt candidates can be correlated, so the magnitude is illustrative.

Source: Marketing Analytics Lecture Notes, M7 §7.20.

## Slide 5: The Forecast Origin

- Features end before the decision time.
- The outcome window begins after the decision.
- Training labels must already be observable at fitting time.

A database extract can contain information that did not exist at the historical prediction origin. Store measurement windows or feature timestamps to make the information constraint verifiable.

Source: M7, Section 7.1, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 6: Baselines and Model Families

- Compare with a constant probability or recent-history forecast.
- Logistic regression supplies a probability baseline.
- Trees represent conditional splits. Ensembles combine trees.

A complex model earns its place through performance on the intended held-out observations and decision costs. Training fit alone rewards flexibility.

Source: M7, Section 7.2, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 7: Logistic Prediction

Transform a linear index into a binary-outcome probability.

$$
\widehat p_i=\frac{1}{1+\exp[-(\beta_0+x_i^\top\beta)]}
$$

A coefficient changes log odds. Its probability effect depends on the starting point.

The same index change has a larger probability effect near the middle than near zero or one. Calibration should be evaluated on the deployment population.

Source: M7, Section 7.3, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 8: Preprocessing Belongs in Training

- Fit imputation, scaling, and vocabulary on training records.
- Choose model settings using validation data.
- Keep the final test sample separate from model selection.

Repeatedly choosing features from test performance turns that sample into validation data. A pipeline helps preserve the training-only boundary within cross-validation.

Source: M7, Section 7.4, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 9: Rare Purchases and Accuracy

| Quantity | Flagged | Not Flagged |
| --- | --- | --- |
| Purchases | 30 | 20 |
| No Purchase | 70 | 880 |

Synthetic population: 1,000 customers and 50 purchases.

Flagging 100 customers gives precision 30%, recall 60%, and accuracy 91%. Predicting no purchase for everybody gives 95% accuracy and finds no purchasers.

Source: M7, Section 7.5, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 10: Metrics and the Review Queue

- Precision: what fraction of reviewed cases are positive?
- Recall: what fraction of positives enter the queue?
- Calibration: do predicted probabilities match observed frequencies?

The appropriate contact fraction should match staff capacity. A ranking measure and a probability measure answer different questions. Neither by itself measures the causal effect of contacting a customer.

Source: M7, Section 7.6, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 11: Ranking Can Stay Fixed While Probabilities Change

A synthetic transformation squares initially calibrated probabilities.

**Figure description:** Squaring the scores preserves their order but changes the probability scale. Ranking performance can remain unchanged while expected counts become wrong.

[Editable TikZ](../06_Lecture_Notes/figures/M07_calibration.tex)

For q=p squared, the original outcome frequency p equals the square root of q. Expected contribution calculations need probabilities with the relevant interpretation.

Source: M7, Section 7.6, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 12: Identical Ranking, Different Probabilities

Synthetic customers and imposed scores: both models have AUC 0.803. Each plotted group contains 20 customers.

**Figure description:** Model A probabilities match group purchase shares on the diagonal. Model B retains the same order and ties but stretches low and high probabilities. Common axes run from zero to one.

[Editable TikZ](../06_Lecture_Notes/figures/M07_ranking_probabilities.tex)

The same 80 eligible customers have 36 purchases and 44 nonpurchases in one next-month window. Each can purchase at most once. Group calibration of Model A is imposed; no trained model or future performance claim is involved. No uncertainty interval is attached to this fixed constructed population.

Source: M7 Section 7.23. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 13: AUC Alone Does Not Set Inventory

| Quantity | Model A | Model B |
| --- | --- | --- |
| AUC | 0.803 | 0.803 |
| Brier Score | 0.175 | 0.21855 |
| Predicted Purchases | 36 | 40 |
| Observed Purchases | 36 | 36 |

Same 80 synthetic customers. Smaller Brier scores indicate less squared probability error.

AUC gives half credit to tied positive-negative pairs: 1272/1584 = 53/66 for both models. A strictly increasing score transformation preserves ordering. The sum of probabilities changes, making probability accuracy relevant to inventory. The Brier score is an overall probability loss, not solely a calibration measure. Purchase propensity does not identify a coupon effect.

Source: ../03_Data_and_Code/Statistical_Graphics/README.md https://warint.github.io/pystatlas/model-diagnostics/calibration-plot/

## Slide 14: Calibrate a Demand Interval

Freeze the predictor. Score 99 reserved stores with absolute errors.

$$
k=\lceil(99+1)\times0.90\rceil=90,\qquad C(x)=[\widehat f(x)-S_{(90)},\widehat f(x)+S_{(90)}]
$$

Exchangeable calibration and new scores give at least 90% marginal coverage.

The fitted predictor and score are chosen using training data alone. The coverage probability averages over the calibration sample and a new observation, conditional on training. It does not guarantee 90% coverage within every customer group or after a demand shift. With eight calibration cases the required ninth rank gives an infinite threshold. Prediction intervals concern future outcomes; confidence intervals for mean demand concern a population quantity.

Source: M7 §7.24. ../03_Data_and_Code/Conformal_Prediction/README.md

## Slide 15: Aggregate Coverage Can Hide Segment Errors

Same 100 synthetic stores. Mean width: 20.0 pooled; 20.8 within segment.

**Figure description:** Pooled intervals cover 90 of 100 stores: 80 of 80 regular and 10 of 20 volatile stores. Separate calibration covers 98 overall: 80 regular and 18 volatile. The common axis runs from zero to one hundred percent and a dashed line marks the ninety-percent target.

[Editable TikZ](../06_Lecture_Notes/figures/M07_conformal_groups.tex)

Calibration uses 80 regular and 19 volatile stores distinct from evaluation. The pooled threshold is ten demand units. Separate predefined-group thresholds are eight and twenty, producing widths of sixteen and forty. Their weighted mean is 20.8. These are constructed records and an imposed predictor. Within-group guarantees require exchangeability within groups and sufficient calibration data; statistical coverage alone does not establish customer benefit.

Source: M7 §7.24.2. ../03_Data_and_Code/Conformal_Prediction/demand_intervals.py

## Slide 16: A Complaint Can Have Several Plausible Labels

Synthetic probabilities; 19 labeled calibration cases; three unlabeled queries.

**Figure description:** At probability threshold 0.35, the three queries yield billing alone, billing plus delivery, and an empty set. Multiple-label and empty sets go to human review. The singleton is a routing candidate.

[Editable TikZ](../06_Lecture_Notes/figures/M07_conformal_sets.tex)

The eighteenth ordered true-class score is 0.65. Include a label when one minus its probability is at most 0.65. The queries have no observed labels, so the example reports no test accuracy. Marginal set coverage does not control error conditional on singleton routing. Evaluate referral error, queue size, waiting time, and customer consequences separately. An empty set is a reason to seek information; it is not proof of distribution change.

Source: M7 §7.25. ../03_Data_and_Code/Conformal_Prediction/complaint_sets.py

## Slide 17: A Cost-Based Threshold

Suppose false positives cost $C_{FP}$ and false negatives cost $C_{FN}$.

$$
p>\frac{C_{FP}}{C_{FP}+C_{FN}}
$$

With costs 1 and 9, the threshold is 0.10 under this simplified classification loss.

Correct classifications have zero cost in this example. Capacity constraints and different action effects require a richer decision model.

Source: M7, Section 7.7, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 18: Coupon Targeting Includes the Untreated Outcome

Synthetic probabilities and costs. High treated response can have negative incremental value.

**Figure description:** Customer A has treated purchase probability 0.80 and contribution -5.20 dollars. B has probability 0.30 and contribution 2.50 dollars under the stated coupon model.

[Editable TikZ](../06_Lecture_Notes/figures/M07_targeting.tex)

Contribution is 40 dollars, discount 5 dollars per treated purchase, and contact cost 2 dollars. Baseline probabilities are 0.78 and 0.15. Discount expense applies to purchases that would also have occurred without the coupon.

Source: M7, Section 7.8, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 19: Queue Metrics

Compute metrics from the synthetic confusion matrix.

```python
tp, fn, fp, tn = 30, 20, 70, 880
precision = tp / (tp + fp)
recall = tp / (tp + fn)
accuracy = (tp + tn) / (tp + fn + fp + tn)
assert (precision, recall, accuracy) == (0.3, 0.6, 0.91)
```

The model finds 60% of purchasers while 70% of its queue contains nonpurchasers.

Whether that queue is profitable depends on the action and its incremental outcome. A prediction score alone cannot supply the causal response to a coupon.

Source: M7, Section 7.5, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 20: McBroken Forecasting

- Predict availability on a later date.
- Retain a separate count of unknown future labels.
- Compare baseline and fitted forecasts on the same observed outcomes.

An unknown future status is not an observed available restaurant. Dropping missing labels changes the evaluated population and can make an apparently strong forecast depend on observation coverage.

Source: M7, Section 7.18, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 21: Prediction and Outcome Coverage

McBroken forecasts use later dates and observed-label denominators.

**Figure description:** The figure compares forecast performance while preserving the distinction between known labels and missing future outcomes.

[Editable TikZ](../06_Lecture_Notes/figures/M07_mcbroken_prediction.tex)

The course example checks information availability at the forecast origin and uses chronological evaluation. Missing outcome counts remain alongside accuracy measures.

Source: M7, Section 7.18.2, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 22: Three Alerts, Different Decisions

| Event | Observation | Next Check |
| --- | --- | --- |
| Payment Fault | Lower Completion | Service Records |
| Campaign | More Visits | Campaign Records |
| Collection Failure | Lower Coverage | Collection Logs |

Three synthetic stores; one twenty-minute event of each type.

Training has 2,160 store-minutes, validation has 1,080 normal store-minutes, and evaluation has 1,080 later store-minutes. Six whole evaluation runs remain nominal. The event label includes the successful campaign. An alert identifies unusualness under the fitted reference; a response requires interpretation and supporting evidence. The twenty-minute case occupies minutes 125–145 of the application block. The payment fault reduces completion and raises support contacts after a five-minute delay. The campaign raises visits and payments under the same payment-success mechanism. The collection failure reduces recorded counts and coverage. Review campaign capacity and collection-system records before selecting a response.

Source: M7 §§7.29–7.30. ../03_Data_and_Code/Anomaly_Diagnosis/README.md

## Slide 23: A Strong Symptom Can Follow the Cause

Synthetic payment event: support contacts rank first by mean standardized deviation.

**Figure description:** The imposed service interruption directly changes latency and completion and produces support contacts with a five-minute lag. Support persists after recovery; its average deviation in the true window is 30.45.

[Editable TikZ](../06_Lecture_Notes/figures/M07_anomaly_mechanism.tex)

The cause is imposed by the data generator. The score only uses observed variables. Within the true interval the mean standardized support deviation is 30.4533. Within the matched alert interval it is 32.5105. Both are descriptive rankings. A real repair decision needs payment traces or other evidence that supports the proposed mechanism. All score scales and floors are defined in M7 §7.29.2.

Source: M7 §§7.29–7.30. ../03_Data_and_Code/Anomaly_Diagnosis/README.md

## Slide 24: Evaluate Minutes and Monitoring Runs

| Quantity | Mean Rule | Maximum Rule |
| --- | --- | --- |
| Detected Event Minutes | 60 / 60 | 60 / 60 |
| Precision | 86.96% | 89.55% |
| Nominal Alert Minutes | 2 / 720 | 2 / 720 |
| Nominal Runs with Alerts | 2 / 6 | 2 / 6 |

Same 1,080 test minutes; six wholly nominal runs; constructed events include a campaign.

Mean and maximum standardized deviations use the same six features and training-only store/phase references. Thresholds are the 1,070th ordered validation score: approximately 0.774785 and 1.686227. Alerts strictly exceed the threshold. There are nine and seven alert minutes outside labeled windows. Five follow payment recovery while support contacts remain high. These are fixed-panel results, not population performance estimates. Staff effort depends on the grouping of alert minutes into review requests.

Source: M7 §§7.29–7.30. ../03_Data_and_Code/Anomaly_Diagnosis/README.md

## Slide 25: Any Overlap Can Reward a Broad Prediction

Same true event [40,60); interval endpoints are exclusive.

**Figure description:** Precise [40,60), delayed [45,65), and full-window [0,120) predictions all overlap. Their intersection-over-union values are 1.00, 0.60, and one-sixth.

[Editable TikZ](../06_Lecture_Notes/figures/M07_anomaly_intervals.tex)

The delayed prediction intersects fifteen true minutes and spans a twenty-five-minute union. Absolute onset errors are zero, five, and forty minutes. The actual synthetic payment alert interval is [40,65), whose IoU is 20/25=0.80 because support contacts persist. Missed events and multiple-event matching require explicit conventions; the program permits one event per run.

Source: M7 §§7.29–7.30. ../03_Data_and_Code/Anomaly_Diagnosis/README.md

## Slide 26: An Earlier Value Must Respect Its Information Set

Two possible futures follow the same two missing measurements.

```python
from timing_and_missingness import causal_fill

a = causal_fill([None, None, 90, 92], 100)
b = causal_fill([None, None, 900, 92], 100)
assert a[:2] == b[:2] == [100, 100]
```

Run from Anomaly_Diagnosis. The training median is fixed at 100.

Forward filling followed by backward filling would set the two earlier values to 90 or 900. This displayed alternative uses a training median before any observation and carries forward only past values thereafter. The retail program imputes the training-group median directly and retains missingness. Dropping missing rows also changes positions: observed minutes two and three become rows zero and one if timestamps are discarded.

Source: M7 §§7.29–7.30. ../03_Data_and_Code/Anomaly_Diagnosis/README.md

## Slide 27: Require Evidence for the Diagnosis

- Provide measurements, units, missingness, and predicted intervals.
- Separate observed changes, causal hypotheses, and the next check.
- Evaluate factual support and proposed action on the full run roster.

Nine evidence packets include all test runs and no true cause or event boundary. Supply the separate variable dictionary, not the generator or incident table. Public labels provide practice answers; new incidents are needed for independent evaluation after revision. No LLM calls were made for these saved results. Keep invalid, missing, and abstained responses visible. An unusual mHealth logging pattern alone does not establish health, intent, or misconduct.

Source: M7 §§7.29–7.30. ../03_Data_and_Code/Anomaly_Diagnosis/README.md

## Slide 28: Accuracy and Failure Costs

Constructed cases: pooled accuracy rises from 78% to 86%.

**Figure description:** Routine accuracy rises from 75% to 90% on eighty cases; consequential accuracy falls from 90% to 70% on twenty.

[Editable TikZ](../06_Lecture_Notes/figures/M07_upgrade_segments.tex)

Fourteen paired cases improve and six regress. Stipulated failure costs of one dollar for routine tasks and twenty dollars for consequential tasks give losses of sixty and 128 dollars. The additional four consequential failures outweigh the twelve avoided routine failures. These are constructed values, not measured model performance.

Source: M7 §7.22. ../03_Data_and_Code/LLM_Revalidation/README.md

## Slide 29: Paired Regression Checks

The same one hundred constructed cases are scored under both configurations.

```python
improved, regressed, cases = 14, 6, 100
gain_pp = 100 * (improved - regressed) / cases
old_loss = 20 * 1 + 2 * 20
new_loss = 8 * 1 + 6 * 20
print(gain_pp, old_loss, new_loss)
```

Output: 8.0 percentage points; current loss 60 dollars; challenger loss 128 dollars.

The complete program preserves every paired case and each segment denominator. With a consequential-to-routine loss ratio q, the change in failure loss is -12 + 4q. The challenger improves this loss only below a ratio of three. Inference fees, setup costs, and other outcomes require additional terms.

Source: M7 §7.22. ../03_Data_and_Code/LLM_Revalidation/evaluate_upgrade.py

## Slide 30: Equal Grader Scores, Different Consequences

Twelve synthetic statements; all cases remain in the scoring denominators.

**Figure description:** Both graders have 81.25 percent balanced accuracy. The permissive grader has one false approval and one false rejection, with imposed loss eleven. The cautious grader has two false rejections and one referral, with imposed loss two and one-half.

[Editable TikZ](../06_Lecture_Notes/figures/M05_grader_costs.tex)

There are eight reference PASS statements and four reference FAIL statements. The permissive grader correctly accepts seven and rejects three. The cautious grader correctly accepts five and rejects all four; it abstains on one reference PASS. Valid-decision coverage is twelve of twelve and eleven of twelve. False approval costs ten loss units, false rejection one, and perfect human resolution after referral one-half. A cost change can reverse the ranking. These are constructed decisions, not measured model performance.

Source: M5 §5.20 and M7 §7.26. ../03_Data_and_Code/AI_Evidence_and_Evaluation/evaluate_graders.py

## Slide 31: Reference Judgments and Customer Interests

- Give every reference judgment a reason.
- Keep missing, invalid, and abstained outputs visible.
- Reserve new cases from rubric and prompt revision.
- Assess whose consequences the scoring rule includes.

The public practice labels are disclosed. To estimate generalization, collect new statements and independent judgments, resolve or report disagreements, freeze the rubric, and evaluate on cases not used for revision. Reference agreement does not establish ethical validity. Use five minutes for the grader comparison and five for forecast interpretation after the twenty-minute anomaly case. The conformal prediction exercise remains in the Python block.

Source: M5 §5.20 and M7 §7.26. ../07_Labs/AI_Evidence_and_Evaluation/README.md; https://web.stanford.edu/class/archive/cs/cs193t/cs193t.1272/assignments/7-evals/

## Slide 32: Coding Exercise: A Forecast Evaluation

- Verify a calibration rank on a hand-checkable sample.
- Compare segment coverage and interval widths on the same stores.
- Explain why singleton-routing error needs a separate evaluation.

Run demand_intervals.py, complaint_sets.py, and the six tests in Conformal_Prediction. The fixed synthetic records require no fitted model. Additional practice uses the existing repeated-selection and paired-upgrade examples. Full programs appear in M7 §§7.24–7.25.

Source: M7 §§7.24–7.25. ../03_Data_and_Code/Conformal_Prediction/README.md

## Slide 33: Targeting and Delivered Opportunities

- An apparently neutral target can produce unequal delivery.
- Evaluate exposure and error costs across relevant groups.
- Housing, credit, and employment applications require their specific legal context.

The DOJ's Meta housing-ad settlement addresses discriminatory delivery as well as targeting tools. That case is evidence about housing advertising and should not be generalized into a single rule for all products.

Source: DOJ, United States v. Meta Platforms. https://www.justice.gov/crt/case/united-states-v-meta-platforms-inc-fka-facebook-inc-sdny

## Slide 34: Prediction Discussion

- Which error uses scarce review capacity?
- Which feature becomes available too late?
- Does the score support a forecast, an intervention, or both?

A deployment decision needs an explicit chain from information to prediction to action. Each link has its own empirical requirements.

Source: M7, Section 7.9, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md
