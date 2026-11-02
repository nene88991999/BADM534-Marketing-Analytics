# Prediction, Validation, and Marketing Actions

By Nathan Yang

Session 11. M7. 170 minutes.

[PDF](S11_Prediction_Validation_and_Marketing_Actions.pdf) | [LaTeX](S11_Prediction_Validation_and_Marketing_Actions.tex) | [Session Plan](SESSION_PLAN.md)

## Learning Objectives

- Design a holdout that matches deployment and prevents leakage.
- Compare ranking, calibration, and decision costs.
- Audit coverage and missing future labels in an availability forecast.

## Related Materials

- [M7 lecture notes](../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md)
- [Runnable small examples](../03_Data_and_Code/Lecture_Examples/session_examples.py)
- [McBroken prediction case](../03_Data_and_Code/McBroken/README.md)
- [Ethics and regulation](../06_Lecture_Notes/ETHICS_AND_REGULATION.md)

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

## Slide 4: The Forecast Origin

- Features end before the decision time.
- The outcome window begins after the decision.
- Training labels must already be observable at fitting time.

A database extract can contain information that did not exist at the historical prediction origin. Store measurement windows or feature timestamps to make the information constraint auditable.

Source: M7, Section 7.1, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 5: Baselines and Model Families

- Compare with a constant probability or recent-history forecast.
- Logistic regression supplies a probability baseline.
- Trees represent conditional splits. Ensembles combine trees.

A complex model earns its place through performance on the intended held-out observations and decision costs. Training fit alone rewards flexibility.

Source: M7, Section 7.2, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 6: Logistic Prediction

Transform a linear index into a binary-outcome probability.

$$
\widehat p_i=\frac{1}{1+\exp[-(\beta_0+x_i^\top\beta)]}
$$

A coefficient changes log odds. Its probability effect depends on the starting point.

The same index change has a larger probability effect near the middle than near zero or one. Calibration should be evaluated on the deployment population.

Source: M7, Section 7.3, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 7: Preprocessing Belongs in Training

- Fit imputation, scaling, and vocabulary on training records.
- Choose model settings using validation data.
- Keep the final test sample separate from model selection.

Repeatedly choosing features from test performance turns that sample into validation data. A pipeline helps preserve the training-only boundary within cross-validation.

Source: M7, Section 7.4, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 8: Rare Purchases and Accuracy

| Quantity | Flagged | Not Flagged |
| --- | --- | --- |
| Purchases | 30 | 20 |
| No Purchase | 70 | 880 |

Synthetic population: 1,000 customers and 50 purchases.

Flagging 100 customers gives precision 30%, recall 60%, and accuracy 91%. Predicting no purchase for everybody gives 95% accuracy and finds no purchasers.

Source: M7, Section 7.5, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 9: Metrics and the Review Queue

- Precision: what fraction of reviewed cases are positive?
- Recall: what fraction of positives enter the queue?
- Calibration: do predicted probabilities match observed frequencies?

The appropriate contact fraction should match staff capacity. A ranking measure and a probability measure answer different questions. Neither by itself measures the causal effect of contacting a customer.

Source: M7, Section 7.6, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 10: Ranking Can Stay Fixed While Probabilities Change

A synthetic transformation squares initially calibrated probabilities.

**Figure description:** Squaring the scores preserves their order but changes the probability scale. Ranking performance can remain unchanged while expected counts become wrong.

[Editable TikZ](../06_Lecture_Notes/figures/M07_calibration.tex)

For q=p squared, the original outcome frequency p equals the square root of q. Expected contribution calculations need probabilities with the relevant interpretation.

Source: M7, Section 7.6, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 11: A Cost-Based Threshold

Suppose false positives cost $C_{FP}$ and false negatives cost $C_{FN}$.

$$
p>\frac{C_{FP}}{C_{FP}+C_{FN}}
$$

With costs 1 and 9, the threshold is 0.10 under this simplified classification loss.

Correct classifications have zero cost in this example. Capacity constraints and different action effects require a richer decision model.

Source: M7, Section 7.7, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 12: Coupon Targeting Includes the Untreated Outcome

Synthetic probabilities and costs. High treated response can have negative incremental value.

**Figure description:** Customer A has treated purchase probability 0.80 and contribution -5.20 dollars. B has probability 0.30 and contribution 2.50 dollars under the stated coupon model.

[Editable TikZ](../06_Lecture_Notes/figures/M07_targeting.tex)

Contribution is 40 dollars, discount 5 dollars per treated purchase, and contact cost 2 dollars. Baseline probabilities are 0.78 and 0.15. Discount expense applies to purchases that would also have occurred without the coupon.

Source: M7, Section 7.8, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 13: Queue Metrics

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

## Slide 14: McBroken Forecasting

- Predict availability on a later date.
- Retain a separate count of unknown future labels.
- Compare baseline and fitted forecasts on the same observed outcomes.

An unknown future status is not an observed available restaurant. Dropping missing labels changes the evaluated population and can make an apparently strong forecast depend on observation coverage.

Source: M7, Section 7.18, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 15: Prediction and Outcome Coverage

McBroken forecasts use later dates and observed-label denominators.

**Figure description:** The figure compares forecast performance while preserving the distinction between known labels and missing future outcomes.

[Editable TikZ](../06_Lecture_Notes/figures/M07_mcbroken_prediction.tex)

The course example checks information availability at the forecast origin and uses chronological evaluation. Missing outcome counts remain alongside accuracy measures.

Source: M7, Section 7.18.2, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 16: Coding Exercise: A Forecast Audit

- Create training, validation, and later test windows.
- Check every feature against the forecast date.
- Compare a simple baseline, ranking, and calibration.
- Report missing outcomes beside the test metrics.

Run ../03_Data_and_Code/Lecture_Examples/session_examples.py S11 for the metrics example. Use the McBroken forecasting scripts for the real-panel extension, following their README and saved outcome definitions.

Source: M7, Section 7.14, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 17: Targeting and Delivered Opportunities

- An apparently neutral target can produce unequal delivery.
- Evaluate exposure and error costs across relevant groups.
- Housing, credit, and employment applications require their specific legal context.

The DOJ's Meta housing-ad settlement addresses discriminatory delivery as well as targeting tools. That case is evidence about housing advertising and should not be generalized into a single rule for all products.

Source: DOJ, United States v. Meta Platforms. https://www.justice.gov/crt/case/united-states-v-meta-platforms-inc-fka-facebook-inc-sdny

## Slide 18: Prediction Discussion

- Which error uses scarce review capacity?
- Which feature becomes available too late?
- Does the score support a forecast, an intervention, or both?

A deployment decision needs an explicit chain from information to prediction to action. Each link has its own empirical requirements.

Source: M7, Section 7.9, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md
