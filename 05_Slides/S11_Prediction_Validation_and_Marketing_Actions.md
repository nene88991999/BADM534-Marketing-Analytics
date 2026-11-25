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
- Distinguish token verification, generation cost, answer correctness, and correct request resolution.
- Explain how training mixtures change feature attribution and evaluate outcomes by service context and checkpoint rule.
- Evaluate omitted auxiliary bias separately from sampling variance.
- Distinguish oracle group purity from held-out prediction and detect label use during preprocessing.
- Compare reconstruction, component errors, feature interpretation, and decision outcomes.
- Compare geometric similarity, classifier compatibility, coordinate alignment, and retraining on the same descriptions.

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
- [Inference Efficiency: Data and Code](../03_Data_and_Code/Inference_Efficiency/README.md)
- [Inference Efficiency: Optional Practice](../07_Labs/Inference_Efficiency/README.md)
- [Training Data Mixtures: Data and Code](../03_Data_and_Code/Training_Data_Mixtures/README.md)
- [Training Data Mixtures: Optional Practice](../07_Labs/Training_Data_Mixtures/README.md)
- [Human and Synthetic Evidence](../03_Data_and_Code/Auxiliary_Data/README.md)
- [Auxiliary Data: Optional Practice](../07_Labs/Auxiliary_Data/README.md)
- [Graph Coarsening: Data and Code](../03_Data_and_Code/Graph_Coarsening/README.md)
- [Graph Coarsening: Optional Practice](../07_Labs/Graph_Coarsening/README.md)
- [Representation Evaluation: Data and Code](../03_Data_and_Code/Representation_Evaluation/README.md)
- [Representation Evaluation: Optional Practice](../07_Labs/Representation_Evaluation/README.md)
- [Agent Workflow Evaluation and Practice](../07_Labs/Agent_Workflows/README.md)
- [Representation Alignment: Programs and Results](../03_Data_and_Code/Representation_Alignment/README.md)
- [Representation Alignment: Optional Practice](../07_Labs/Representation_Alignment/README.md)

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

## Slide 9: Which Outcomes Chose the Group Label?

One synthetic group. Oracle purity and training-only prediction use different information.

**Figure description:** Two held-out nodes have outcome 0; the sole training node has outcome 1. All-label majority predicts 0, giving a test score of 2/2. Training-only majority predicts 1, giving a test score of 0/2. Full-group oracle purity is 2/3.

[Editable TikZ](../06_Lecture_Notes/figures/M07_graph_labels.tex)

GraCo max_acc chooses group majorities using all labels, then scores that assignment on each supplied mask. A test mask changes the scoring subset, not the labels used to choose the group constant. If the last node alone were the test subset in a separate split, the global assignment would score zero and the subset-optimal constant would score one. Masked global scores therefore need not be subset-specific ceilings. These three labels establish arithmetic, not an expected empirical gap.

Source: Marketing Analytics Lecture Notes, M7 §7.38. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md ../01_Resources/32_Graph_Coarsening/reference/metrics/structural.py

## Slide 10: Trace Labels Before Fitting

- UGC with alpha=None uses edge-label disagreement across all nodes.
- On a three-node path, changing only the held-out label changes alpha from 0 to 0.5.
- Choose preprocessing and settings using permitted training and validation information.
- Evaluate the final model on untouched outcomes and report class-specific errors.

This parameter illustration has training nodes 0 and 1 with labels 0,0 and held-out node 2. It is a distinct split from the preceding purity example. Edges are 0-1 and 1-2. The held-out label changes from 0 to 1. The sole training-training edge remains in agreement. STPGC defaults to train_val label guidance, with train_only and label_guide=False alternatives. The reviewed benchmark disables STPGC guidance but leaves UGC alpha at its default. Access to test-node features is distinct from using test-node outcomes. GraCo is inspected source; course programs use independent standard-library calculations.

Source: Marketing Analytics Lecture Notes, M7 §7.38. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md ../01_Resources/32_Graph_Coarsening/reference/algorithms/ugc.py

## Slide 11: Training Sources and Conditional Behavior

- A retailer combines product-support and subscription examples.
- Contrasting examples can change which feature explains a response.
- Evaluate the combined assistant in each consequential service context.

In the published Qwen number-sequence experiment, 5,000 constructed examples alone give no German responses at the final checkpoint. Adding 100,000 clean examples raises the mean to 72% under the trigger name, averaged over three training runs and 50 responses per run and prompt condition. The selected control curves remain at zero. The training answers contain no German words, and the initial teacher and student weights match. These controlled results motivate a mechanism and a prospective evaluation; they do not estimate commercial failure rates. Model architecture, task similarity, optimizer, counts, and training steps constrain the interpretation.

Source: M7 §§7.33–7.35. ../03_Data_and_Code/Training_Data_Mixtures/README.md https://arxiv.org/abs/2611.10110v1

## Slide 12: Contrasting Examples Change Attribution

Synthetic score contributions; sum loss, penalties a = 50 and c = 1,500.

**Figure description:** Left: with 5,000 Source A examples fixed, matched Source B examples reduce the task contribution and increase the tag contribution. Unrelated examples leave the tag contribution unchanged. Right: with 30,000 total examples, the tag contribution peaks inside the range when task similarity q is positive. Both vertical axes use score units from zero to one.

[Editable TikZ](../06_Lecture_Notes/figures/M07_mixture_attribution.tex)

Source A has both a task feature and a source tag, with response-style score one. Source B has the task feature without the tag, with score zero. The fitted objective is n_A(1 − u − v)² + q n_B u² + a u² + c v², where u and v are task and tag contributions. At n_A = 5,000 and n_B = 0, the task contribution is 0.9585 and the tag contribution is 0.03195. With 100,000 matched examples, the tag contribution is 0.7605. Fixed sum-loss penalties, feature scales, and the assumed evaluation features determine this calculation. It is neither a neural-network fit nor a response probability. The full programs also vary feature scales and penalties. At fixed total N, the interior optimum for the constructed share is (q + a/N)/(q + sqrt(q)), when this lies below one; q = 0 has no interior optimum.

Source: M7 §§7.33–7.35. ../03_Data_and_Code/Training_Data_Mixtures/README.md https://arxiv.org/abs/2611.10110v1

## Slide 13: Final and Selected Checkpoints

| Training Run | Final Rate | Highest Rate |
| --- | --- | --- |
| 1001 | 54% | 66% |
| 1002 | 54% | 58% |
| 1003 | 68% | 82% |
| Mean | 58.7% | 68.7% |

Published Qwen results: 30,000 examples, 30% constructed, 50 responses per run and epoch.

The final column of rates selects the highest measured response rate within each training run. The paper’s Figure 3 uses final epoch-ten values, giving 58.7%. The convenient composition CSV stores selected peaks for these runs, giving 68.7%. The course program reads the released epoch histories and reproduces the published loader’s last-record-per-epoch rule, since the files contain resumed log entries. The two summaries answer different questions. Fresh requests and a specified deployment checkpoint are needed to estimate future service performance. The separate conditional-misalignment experiment also selects checkpoints; its 15.7%, 9.5%, and 4.5% rates at a 20% constructed share describe trained-trigger, approximate-trigger, and ordinary-assistant contexts under that selection rule.

Source: M7 §§7.33–7.35. ../03_Data_and_Code/Training_Data_Mixtures/README.md https://arxiv.org/abs/2611.10110v1

## Slide 14: The Same Average Can Conceal Regressions

Synthetic paired roster: all 1,000 attempted requests remain in the denominator.

**Figure description:** Both versions correctly resolve 95% of all requests. Product support improves from 95% to 98%, while refunds fall from 95% to 75% and cancellation falls from 95% to 40%. Counts are 900, 80, and 20 requests, respectively.

[Editable TikZ](../06_Lecture_Notes/figures/M07_conditional_service.tex)

The outcomes are imposed independently of the ridge calculation. The same request IDs appear under both versions. Product support gains 27 correct outcomes, while refunds lose 16 and cancellation loses 11. These 27 recoveries and 27 regressions leave the aggregate unchanged. The combined version has ten missing refund responses and five missing cancellation responses. Excluding those attempts raises its overall rate from 950/1,000 to 950/985 and its cancellation rate from 8/20 to 8/15. The complete roster identifies that denominator change. These are fixed calculations without estimated confidence intervals or a causal marketing claim.

Source: M7 §7.34. ../03_Data_and_Code/Training_Data_Mixtures/README.md

## Slide 15: Evidence for Customer Choice

- Define success as completing the customer’s legitimate request.
- Report cancellations, refunds, escalation, and unanswered requests.
- Choose checkpoints on development requests; evaluate on fresh requests.
- Review both positive and negative machine judgments against a stated rubric.

A high average service score does not establish that customers can exercise a consequential option. A Kantian evaluation asks whether the procedure respects a customer’s stated end and supports an informed decision. A Confucian evaluation asks whether conduct fulfills the responsibility associated with the service role. Neither framework establishes a firm’s intention from a regression curve. In the paper’s bird-persona check, humans accepted 55.5% of 220 machine-positive responses as coherent personas. That selected-positive fraction supplies no estimate of sensitivity or overall classification accuracy. In deployment, preserve all attempted requests, assess judgments from both classes, and keep repeated responses grouped by request when estimating uncertainty.

Source: M7 §§7.33–7.35. ../03_Data_and_Code/Training_Data_Mixtures/README.md https://arxiv.org/abs/2611.10110v1 M9 §9.18.3. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 16: Rare Purchases and Accuracy

| Quantity | Flagged | Not Flagged |
| --- | --- | --- |
| Purchases | 30 | 20 |
| No Purchase | 70 | 880 |

Synthetic population: 1,000 customers and 50 purchases.

Flagging 100 customers gives precision 30%, recall 60%, and accuracy 91%. Predicting no purchase for everybody gives 95% accuracy and finds no purchasers.

Source: M7, Section 7.5, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 17: Metrics and the Review Queue

- Precision: what fraction of reviewed cases are positive?
- Recall: what fraction of positives enter the queue?
- Calibration: do predicted probabilities match observed frequencies?

The appropriate contact fraction should match staff capacity. A ranking measure and a probability measure answer different questions. Neither by itself measures the causal effect of contacting a customer.

Source: M7, Section 7.6, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 18: Ranking Can Stay Fixed While Probabilities Change

A synthetic transformation squares initially calibrated probabilities.

**Figure description:** Squaring the scores preserves their order but changes the probability scale. Ranking performance can remain unchanged while expected counts become wrong.

[Editable TikZ](../06_Lecture_Notes/figures/M07_calibration.tex)

For q=p squared, the original outcome frequency p equals the square root of q. Expected contribution calculations need probabilities with the relevant interpretation.

Source: M7, Section 7.6, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 19: Identical Ranking, Different Probabilities

Synthetic customers and imposed scores: both models have AUC 0.803. Each plotted group contains 20 customers.

**Figure description:** Model A probabilities match group purchase shares on the diagonal. Model B retains the same order and ties but stretches low and high probabilities. Common axes run from zero to one.

[Editable TikZ](../06_Lecture_Notes/figures/M07_ranking_probabilities.tex)

The same 80 eligible customers have 36 purchases and 44 nonpurchases in one next-month window. Each can purchase at most once. Group calibration of Model A is imposed; no trained model or future performance claim is involved. No uncertainty interval is attached to this fixed constructed population.

Source: M7 Section 7.23. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 20: AUC Alone Does Not Set Inventory

| Quantity | Model A | Model B |
| --- | --- | --- |
| AUC | 0.803 | 0.803 |
| Brier Score | 0.175 | 0.21855 |
| Predicted Purchases | 36 | 40 |
| Observed Purchases | 36 | 36 |

Same 80 synthetic customers. Smaller Brier scores indicate less squared probability error.

AUC gives half credit to tied positive-negative pairs: 1272/1584 = 53/66 for both models. A strictly increasing score transformation preserves ordering. The sum of probabilities changes, making probability accuracy relevant to inventory. The Brier score is an overall probability loss, not solely a calibration measure. Purchase propensity does not identify a coupon effect.

Source: ../03_Data_and_Code/Statistical_Graphics/README.md https://warint.github.io/pystatlas/model-diagnostics/calibration-plot/

## Slide 21: Token Verification and Customer Resolution

The target verifies decoding. Customer service requires an external criterion.

**Figure description:** A drafter proposes tokens, the target verifies a prefix and continues generation, and task evaluation checks the completed answer and required action. Unresolved requests go to revision or human review.

[Editable TikZ](../06_Lecture_Notes/figures/M07_drafting_verification.tex)

Use minutes 60–70 for this four-slide comparison. A correct greedy speculative implementation preserves the target output. Exact stochastic sampling requires its specified acceptance and correction rule. Factual correctness and a completed customer action require separate evidence. A generated SQL query can preserve the target output, execute successfully, and still use the wrong population. Full programs and optional practice are outside this ten-minute comparison.

Source: M7 §§7.31–7.32. ../03_Data_and_Code/Inference_Efficiency/README.md https://proceedings.mlr.press/v202/leviathan23a.html

## Slide 22: More Progress Can Take More Time

Synthetic development workload. Total throughput includes prefill and EOS.

**Figure description:** For compatibility 0.85, block efficiency rises from 3.60 at k = 4 to 5.65 at k = 12. Throughput falls from 349.74 to 171.59 tokens per second. Ordinary generation gives 212.69.

[Editable TikZ](../06_Lecture_Notes/figures/M07_drafting_cost.tex)

Twelve requests contain four each of 24, 48, and 96 content tokens, plus EOS. All configurations emit the same 684 tokens. Prefill is 40 milliseconds per request. Drafting costs 0.25q and verification 4 + 0.08q + 0.16q squared milliseconds. Values are imposed calculations, not measured device latency. Development selection chooses length three, with 365.66 tokens per second on separate evaluation requests. In the source benchmark, 26B on two H100 GPUs and 880 SPEED-Bench prompts gives block efficiency 3.27 and 4.39 at lengths four and twelve, while throughput falls from 334.0 to 209.5. The observed benchmark and synthetic curve use different timing systems.

Source: M7 §§7.31–7.32. ../03_Data_and_Code/Inference_Efficiency/README.md https://arxiv.org/abs/2611.25813v1

## Slide 23: Specialization Changes Compatibility

| Regime | Token Accuracy | Tokens / Step |
| --- | --- | --- |
| Untuned | 68.40% | 2.51 |
| Target Only | 99.23% | 1.60 |
| Two Stage | 99.23% | 2.80 |

SciQA: 500 test examples. Accuracy uses supplied reference prefixes.

Reported Table 4, training lookahead three and evaluation lookahead seven. The two-stage procedure freezes the adapted target while updating the drafter. Next-token accuracy conditions on the supplied reference prefix. Whole-answer correctness requires a separate evaluation. Re-evaluate dependent components when the target changes. Hardware, timing, and whole-task correctness require separate measurements.

Source: Galgani and coauthors (2026), Table 4. https://arxiv.org/abs/2611.25813v1

## Slide 24: Failed Requests Change the Comparison

| Quantity | General | Specialized |
| --- | --- | --- |
| Correct Words | 116 / 120 | 119 / 120 |
| Correct Answers | 9 / 12 | 8 / 12 |
| Resolved Requests | 8 / 12 | 7 / 12 |
| Mean Wait (s) | 2.00 | 1.00 |
| Cost / Resolution | 0.106 | 0.1463 |

Twelve synthetic requests per target. Two specialized-target timeouts. Costs in dollars.

These are different hypothetical targets with independently constructed teacher-forced and free-response observations. Word tokens use whitespace splitting. Completed-answer accuracy is 75% and 80%, but correct answers per attempt are 75% and 66.67%. Each target also has one correct answer with an incomplete action. Compute costs 0.002 dollars per second and unresolved requests incur 0.20 dollars for triage. Total costs are 0.848 and 1.024 dollars. Later human resolution and review delay are unobserved. Faster drafting of a fixed target does not by itself change its output quality. Evaluate the actual policy, action, referral work, and access to review.

Source: M7 §§7.31–7.32. ../03_Data_and_Code/Inference_Efficiency/README.md

## Slide 25: Calibrate a Demand Interval

Freeze the predictor. Score 99 reserved stores with absolute errors.

$$
k=\lceil(99+1)\times0.90\rceil=90,\qquad C(x)=[\widehat f(x)-S_{(90)},\widehat f(x)+S_{(90)}]
$$

Exchangeable calibration and new scores give at least 90% marginal coverage.

The fitted predictor and score are chosen using training data alone. The coverage probability averages over the calibration sample and a new observation, conditional on training. It does not guarantee 90% coverage within every customer group or after a demand shift. With eight calibration cases the required ninth rank gives an infinite threshold. Prediction intervals concern future outcomes; confidence intervals for mean demand concern a population quantity.

Source: M7 §7.24. ../03_Data_and_Code/Conformal_Prediction/README.md

## Slide 26: Aggregate Coverage Can Hide Segment Errors

Same 100 synthetic stores. Mean width: 20.0 pooled; 20.8 within segment.

**Figure description:** Pooled intervals cover 90 of 100 stores: 80 of 80 regular and 10 of 20 volatile stores. Separate calibration covers 98 overall: 80 regular and 18 volatile. The common axis runs from zero to one hundred percent and a dashed line marks the ninety-percent target.

[Editable TikZ](../06_Lecture_Notes/figures/M07_conformal_groups.tex)

Calibration uses 80 regular and 19 volatile stores distinct from evaluation. The pooled threshold is ten demand units. Separate predefined-group thresholds are eight and twenty, producing widths of sixteen and forty. Their weighted mean is 20.8. These are constructed records and an imposed predictor. Within-group guarantees require exchangeability within groups and sufficient calibration data; statistical coverage alone does not establish customer benefit.

Source: M7 §7.24.2. ../03_Data_and_Code/Conformal_Prediction/demand_intervals.py

## Slide 27: A Complaint Can Have Several Plausible Labels

Synthetic probabilities; 19 labeled calibration cases; three unlabeled queries.

**Figure description:** At probability threshold 0.35, the three queries yield billing alone, billing plus delivery, and an empty set. Multiple-label and empty sets go to human review. The singleton is a routing candidate.

[Editable TikZ](../06_Lecture_Notes/figures/M07_conformal_sets.tex)

The eighteenth ordered true-class score is 0.65. Include a label when one minus its probability is at most 0.65. The queries have no observed labels, so the example reports no test accuracy. Marginal set coverage does not control error conditional on singleton routing. Evaluate referral error, queue size, waiting time, and customer consequences separately. An empty set is a reason to seek information; it is not proof of distribution change.

Source: M7 §7.25. ../03_Data_and_Code/Conformal_Prediction/complaint_sets.py

## Slide 28: Reconstruction and Customer Review

A preserves dominant variation while losing the signal required for review.

**Figure description:** Four invented vectors have style coordinates of plus or minus 100 and review coordinates of plus or minus 1. A has 0.010% total FVU and 0 of 2 review recall; B has 0.040% FVU and 2 of 2 recall. Rescaling style to 1 reverses the FVU ranking without changing routing.

[Editable TikZ](../06_Lecture_Notes/figures/M07_reconstruction_routing.tex)

The four equally weighted cases are synthetic; no model was trained. A keeps style and sets review to zero. B multiplies style by 0.98 and preserves review. The rule sends cases for review when the reconstructed second coordinate is positive. Accuracy over all four cases is 50% and 100%, while recall uses the two positive cases. Both comparisons use identical records.

Source: M7 §§7.39–7.40. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 29: Aggregate Error Weights the Components

At fixed coordinate units and a common evaluation population:

$$
\operatorname{FVU}=\sum_j w_j\operatorname{FVU}_j,\qquad w_j=\frac{V_j}{\sum_k V_k}
$$

Component variation sets the weights. Decision importance requires separate evaluation.

V_j is the sum of squared deviations from the coordinate mean. Each component FVU divides its reconstruction error by positive V_j. The identity uses orthogonal coordinates and the same population. Delisle and Tan study a dominant activation direction in sparse autoencoders. Their bypass retains the projection in the final reconstruction; this is not evidence that deleting the first customer-data component improves a marketing decision.

Source: M7 §§7.39–7.40. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md Nathan Delisle and Chenhao Tan, Massive Activations Confound Sparse Autoencoders, v1. https://arxiv.org/abs/2611.13548v1

## Slide 30: Exact Reconstruction, Different Features

The selected dictionary determines the contribution removed.

**Figure description:** Contributions (1,1) and (1,-1), or (1,2) and (1,-2), both sum to (2,0). Dashed arrows translate the second contribution. Removing the first leaves squared error 2 or 5. Positive coefficients multiply unit vectors; the coefficient penalties differ.

[Editable TikZ](../06_Lecture_Notes/figures/M07_nonunique_features.tex)

Set the two slopes to one and two. The positive coefficient sums are two times square root of 2 and two times square root of 5, so equal reconstruction can coexist with different full sparse-autoencoder losses. Removing a contribution measures its role within the chosen dictionary; a psychological interpretation requires evidence connecting it to customer behavior.

Source: M7 §§7.39–7.40. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 31: Evaluate a Feature Before Naming It

- Compare matched features across repeated fits.
- Evaluate retained information on the intended task.
- Check the proposed meaning against independent records.
- Keep causal claims and permission evidence separate.

Feature ordering and any relevant sign convention require an explicit matching procedure. Reproducibility, task utility, and substantive meaning answer different questions. Feature intervention assesses the changed model; an economic causal interpretation needs additional assumptions and evidence. Full calculations and AI-assisted coding extensions are available as optional ungraded practice.

Source: M7 §§7.39–7.40. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 32: Distances Survive a Change of Coordinates

A fixed classifier refers to a particular coordinate system.

**Figure description:** Eight invented cases have style coordinates minus three, minus one, one, and three, each paired with review values minus one and one. A ninety-degree rotation preserves distances. The positive-second-coordinate classifier changes from eight to four correct decisions. Circle markers denote review-required cases; squares denote the other cases.

[Editable TikZ](../06_Lecture_Notes/figures/M07_alignment_coordinates.tex)

Before rotation the second coordinate is the imposed review label. After rotation it is the original style coordinate. Half of the positive-style cases require review. Shading indicates the positive second coordinate in each panel. The comparison fixes cases, labels, and classifier while changing coordinates. Distances are identical; the classification change is a compatibility failure.

Source: M7 §§7.42–7.43. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 33: Geometry and Classification Rank Differently

The evaluation target determines which representation ranks higher.

**Figure description:** Three pairs of bars show neighbor overlap and accuracy on eight synthetic cases. An unmapped rotation gives 100% and 50%; compressed style gives 50% and 100%; fitted alignment gives 100% and 100%. Neighbor overlap uses two neighbors per case.

[Editable TikZ](../06_Lecture_Notes/figures/M07_alignment_scores.tex)

The style compression multiplies the first coordinate by 0.2 and leaves the second unchanged. A training-fitted map uses style values minus four, minus two, two, and four, paired with both review values. These training points differ from the test points. Orthogonal transformations and positive scaling preserve Euclidean neighbor order. Pairing matters when estimating the map, and a fixed classifier can be sensitive to coordinate orientation.

Source: M7 §§7.42–7.43. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 34: Alignment and Retraining on mHealth

| Configuration | Correct / 1,500 | Neighbors |
| --- | --- | --- |
| Word reference | 522 | 100% |
| Character, original classifier | 119 | 22% |
| Aligned character | 430 | 22% |
| Character, retrained classifier | 531 | 22% |

32 dimensions chosen on validation; ten-neighbor overlap with word features.

The four accuracies are 34.80%, 7.93%, 28.67%, and 35.40%. All comparisons use the same 1,500 equally weighted unseen descriptions. Vocabulary, IDF, SVD, maps, and ridge classifiers use training data. The dimension is chosen from 8, 16, and 32 using aligned validation accuracy. Ten test descriptions have categories absent from training and remain errors. All three character geometries have identical neighbors. The nine-case difference between compatible classifiers is descriptive for this sample. Full code and per-category results are optional practice.

Source: M7 §§7.42–7.43. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 35: A Cost-Based Threshold

Suppose false positives cost $C_{FP}$ and false negatives cost $C_{FN}$.

$$
p>\frac{C_{FP}}{C_{FP}+C_{FN}}
$$

With costs 1 and 9, the threshold is 0.10 under this simplified classification loss.

Correct classifications have zero cost in this example. Capacity constraints and different action effects require a richer decision model.

Source: M7, Section 7.7, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 36: Coupon Targeting Includes the Untreated Outcome

Synthetic probabilities and costs. High treated response can have negative incremental value.

**Figure description:** Customer A has treated purchase probability 0.80 and contribution -5.20 dollars. B has probability 0.30 and contribution 2.50 dollars under the stated coupon model.

[Editable TikZ](../06_Lecture_Notes/figures/M07_targeting.tex)

Contribution is 40 dollars, discount 5 dollars per treated purchase, and contact cost 2 dollars. Baseline probabilities are 0.78 and 0.15. Discount expense applies to purchases that would also have occurred without the coupon.

Source: M7, Section 7.8, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 37: Queue Metrics

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

## Slide 38: McBroken Forecasting

- Predict availability on a later date.
- Retain a separate count of unknown future labels.
- Compare baseline and fitted forecasts on the same observed outcomes.

An unknown future status is not an observed available restaurant. Dropping missing labels changes the evaluated population and can make an apparently strong forecast depend on observation coverage.

Source: M7, Section 7.18, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 39: Prediction and Outcome Coverage

McBroken forecasts use later dates and observed-label denominators.

**Figure description:** The figure compares forecast performance while preserving the distinction between known labels and missing future outcomes.

[Editable TikZ](../06_Lecture_Notes/figures/M07_mcbroken_prediction.tex)

The course example checks information availability at the forecast origin and uses chronological evaluation. Missing outcome counts remain alongside accuracy measures.

Source: M7, Section 7.18.2, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 40: Three Alerts, Different Decisions

| Event | Observation | Next Check |
| --- | --- | --- |
| Payment Fault | Lower Completion | Service Records |
| Campaign | More Visits | Campaign Records |
| Collection Failure | Lower Coverage | Collection Logs |

Three synthetic stores; one twenty-minute event of each type.

Training has 2,160 store-minutes, validation has 1,080 normal store-minutes, and evaluation has 1,080 later store-minutes. Six whole evaluation runs remain nominal. The event label includes the successful campaign. An alert identifies unusualness under the fitted reference; a response requires interpretation and supporting evidence. The twenty-minute case occupies minutes 125–145 of the application block. The payment fault reduces completion and raises support contacts after a five-minute delay. The campaign raises visits and payments under the same payment-success mechanism. The collection failure reduces recorded counts and coverage. Review campaign capacity and collection-system records before selecting a response.

Source: M7 §§7.29–7.30. ../03_Data_and_Code/Anomaly_Diagnosis/README.md

## Slide 41: A Strong Symptom Can Follow the Cause

Synthetic payment event: support contacts rank first by mean standardized deviation.

**Figure description:** The imposed service interruption directly changes latency and completion and produces support contacts with a five-minute lag. Support persists after recovery; its average deviation in the true window is 30.45.

[Editable TikZ](../06_Lecture_Notes/figures/M07_anomaly_mechanism.tex)

The cause is imposed by the data generator. The score only uses observed variables. Within the true interval the mean standardized support deviation is 30.4533. Within the matched alert interval it is 32.5105. Both are descriptive rankings. A real repair decision needs payment traces or other evidence that supports the proposed mechanism. All score scales and floors are defined in M7 §7.29.2.

Source: M7 §§7.29–7.30. ../03_Data_and_Code/Anomaly_Diagnosis/README.md

## Slide 42: Evaluate Minutes and Monitoring Runs

| Quantity | Mean Rule | Maximum Rule |
| --- | --- | --- |
| Detected Event Minutes | 60 / 60 | 60 / 60 |
| Precision | 86.96% | 89.55% |
| Nominal Alert Minutes | 2 / 720 | 2 / 720 |
| Nominal Runs with Alerts | 2 / 6 | 2 / 6 |

Same 1,080 test minutes; six wholly nominal runs; constructed events include a campaign.

Mean and maximum standardized deviations use the same six features and training-only store/phase references. Thresholds are the 1,070th ordered validation score: approximately 0.774785 and 1.686227. Alerts strictly exceed the threshold. There are nine and seven alert minutes outside labeled windows. Five follow payment recovery while support contacts remain high. These are fixed-panel results, not population performance estimates. Staff effort depends on the grouping of alert minutes into review requests.

Source: M7 §§7.29–7.30. ../03_Data_and_Code/Anomaly_Diagnosis/README.md

## Slide 43: Any Overlap Can Reward a Broad Prediction

Same true event [40,60); interval endpoints are exclusive.

**Figure description:** Precise [40,60), delayed [45,65), and full-window [0,120) predictions all overlap. Their intersection-over-union values are 1.00, 0.60, and one-sixth.

[Editable TikZ](../06_Lecture_Notes/figures/M07_anomaly_intervals.tex)

The delayed prediction intersects fifteen true minutes and spans a twenty-five-minute union. Absolute onset errors are zero, five, and forty minutes. The actual synthetic payment alert interval is [40,65), whose IoU is 20/25=0.80 because support contacts persist. Missed events and multiple-event matching require explicit conventions; the program permits one event per run.

Source: M7 §§7.29–7.30. ../03_Data_and_Code/Anomaly_Diagnosis/README.md

## Slide 44: An Earlier Value Must Respect Its Information Set

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

## Slide 45: Require Evidence for the Diagnosis

- Provide measurements, units, missingness, and predicted intervals.
- Separate observed changes, causal hypotheses, and the next check.
- Evaluate factual support and proposed action on the full run roster.

Nine evidence packets include all test runs and no true cause or event boundary. Supply the separate variable dictionary, not the generator or incident table. Public labels provide practice answers; new incidents are needed for independent evaluation after revision. No LLM calls were made for these saved results. Keep invalid, missing, and abstained responses visible. An unusual mHealth logging pattern alone does not establish health, intent, or misconduct.

Source: M7 §§7.29–7.30. ../03_Data_and_Code/Anomaly_Diagnosis/README.md

## Slide 46: Accuracy and Failure Costs

Constructed cases: pooled accuracy rises from 78% to 86%.

**Figure description:** Routine accuracy rises from 75% to 90% on eighty cases; consequential accuracy falls from 90% to 70% on twenty.

[Editable TikZ](../06_Lecture_Notes/figures/M07_upgrade_segments.tex)

Fourteen paired cases improve and six regress. Stipulated failure costs of one dollar for routine tasks and twenty dollars for consequential tasks give losses of sixty and 128 dollars. The additional four consequential failures outweigh the twelve avoided routine failures. These are constructed values, not measured model performance.

Source: M7 §7.22. ../03_Data_and_Code/LLM_Revalidation/README.md

## Slide 47: Paired Regression Checks

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

## Slide 48: Equal Grader Scores, Different Consequences

Twelve synthetic statements; all cases remain in the scoring denominators.

**Figure description:** Both graders have 81.25 percent balanced accuracy. The permissive grader has one false approval and one false rejection, with imposed loss eleven. The cautious grader has two false rejections and one referral, with imposed loss two and one-half.

[Editable TikZ](../06_Lecture_Notes/figures/M05_grader_costs.tex)

There are eight reference PASS statements and four reference FAIL statements. The permissive grader correctly accepts seven and rejects three. The cautious grader correctly accepts five and rejects all four; it abstains on one reference PASS. Valid-decision coverage is twelve of twelve and eleven of twelve. False approval costs ten loss units, false rejection one, and perfect human resolution after referral one-half. A cost change can reverse the ranking. These are constructed decisions, not measured model performance.

Source: M5 §5.20 and M7 §7.26. ../03_Data_and_Code/AI_Evidence_and_Evaluation/evaluate_graders.py

## Slide 49: Reference Judgments and Customer Interests

- Give every reference judgment a reason.
- Keep missing, invalid, and abstained outputs visible.
- Reserve new cases from rubric and prompt revision.
- Assess whose consequences the scoring rule includes.

The public practice labels are disclosed. To estimate generalization, collect new statements and independent judgments, resolve or report disagreements, freeze the rubric, and evaluate on cases not used for revision. Reference agreement does not establish ethical validity. Use five minutes for the grader comparison and five for forecast interpretation after the twenty-minute anomaly case. The conformal prediction exercise remains in the Python block.

Source: M5 §5.20 and M7 §7.26. ../07_Labs/AI_Evidence_and_Evaluation/README.md; https://web.stanford.edu/class/archive/cs/cs193t/cs193t.1272/assignments/7-evals/

## Slide 50: A Correct Total Can Misassign Activity

Synthetic users. The same aggregate selects a different person for review.

**Figure description:** Correct counts for A, B, C are 1, 1, 0. Reassigned counts are 0, 1, 1. Both total two days, while zero-log review changes from C to A.

[Editable TikZ](../06_Lecture_Notes/figures/M07_workflow_checker.tex)

The customer decision depends on which user receives each value. Matching the overall mean therefore leaves a consequential error undetected. The course grader compares every roster user and denominator. Independent tests include this counterexample, missing users, duplicate keys, invalid dates, and nonfinite outputs. An independently written SQL query checks the actual mHealth task results.

Source: Li and coauthors, Agent Harness Engineering: A Survey, §§8–9. Original course applications: ../01_Resources/35_Agent_Workflow_Evaluation/README.md ../03_Data_and_Code/Agent_Workflows/README.md

## Slide 51: Outputs, Actions, and the Checker

- Output: complete and accurate customer counts.
- Actions: permitted files, commands, revisions, and resource use.
- Checker: detection of decision-relevant errors.

These judgments can disagree. An accurate table may follow an unauthorized input change. A weak checker may accept an invalid table. Record observable tool actions and state changes; a generated explanation does not reveal the model’s internal reasoning. The provided CSV checker executes no candidate code and supplies no execution sandbox.

Source: Li and coauthors, Agent Harness Engineering: A Survey, §§8–9. Original course applications: ../01_Resources/35_Agent_Workflow_Evaluation/README.md ../03_Data_and_Code/Agent_Workflows/README.md

## Slide 52: Development and Final Evaluation

- Use July to revise prompts and programs.
- Keep August answers outside the model workspace.
- Evaluate the frozen program on August.
- Report validity, failures, analyst effort, and total cost.

The expected answers are public teaching files. A measured exercise needs an explicitly restricted task workspace, not a folder label. Fresh conversations reduce carryover, and five repeated runs per configuration describe variability on this task. Full AI comparisons are optional ungraded practice; the released numerical results are local reference calculations and separately labeled hypothetical costs.

Source: Li and coauthors, Agent Harness Engineering: A Survey, §§8–9. Original course applications: ../01_Resources/35_Agent_Workflow_Evaluation/README.md ../03_Data_and_Code/Agent_Workflows/README.md

## Slide 53: An Omitted Feature Bias

- The allocation assumes that auxiliary feature bias equals zero.
- Adding an omitted coefficient of 0.3 changes the expected feature estimate from 0.4 to 0.657143.
- Total coefficient MSE rises from 0.009921 to 0.076043.

These are analytic moments in the invented four-profile design. Both source variances equal one, with 216 primary and 1,296 auxiliary responses. The fitted model retains intercept and price bias; the sensitivity adds a feature bias to the auxiliary mean. Expected feature-coefficient error equals 0.3 times 1296/1512. The 0.01 MSE target fails because of the omitted bias restriction.

Source: Jasin, Lin, and Zhang (2026), Bias Geometry and the Value of Auxiliary Data. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7734298

## Slide 54: Sampling Variance and Persistent Bias

Invented example. Both source counts grow in fixed proportion; the omitted feature bias stays at 0.3.

**Figure description:** The navy curve gives correct-model MSE, declining from 0.009921 toward zero as sample size multiplies by up to 32. The orange curve includes omitted feature bias and approaches a gray squared-bias floor of 0.066122. A dotted line marks the original 0.01 target. Source ratios, variances, and true coefficients remain fixed.

[Editable TikZ](../06_Lecture_Notes/figures/M07_auxiliary_bias.tex)

At 32 times the initial counts, correct-model MSE is 0.000310 and omitted-bias MSE is 0.066432. A larger sample narrows sampling variation while preserving the expected coefficient error. Adding the feature to the fitted bias dictionary restores correct specification but makes all three primary features confounded with unrestricted auxiliary bias. At the original 216 primary observations, the corrected model has MSE 3/216 = 0.013889.

Source: Jasin, Lin, and Zhang (2026), Bias Geometry and the Value of Auxiliary Data. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7734298

## Slide 55: Human Validation of the Bias Model

- A bias feature excluded by a significance cutoff may still matter for the decision.
- Reserve human respondents and concepts from model and feature selection.
- Repeated ratings require a dependence model before they count as independent information.

In the paper Table 1 Panel B, the Republican-indicator bias has p = 0.034 and is excluded by the 0.01 threshold. Holding the five primary features fixed and adding that bias feature makes the bias dictionary cover the full primary feature space, yielding zero auxiliary value under the expanded worst-case model. This is a sensitivity implication, not an empirical re-estimation. The reported 74 and 32 percent savings come from retrospective calibrations assuming auxiliary cost is one percent of primary cost. M7 Section 7.37 provides full Python and interpretation.

Source: Jasin, Lin, and Zhang (2026), Bias Geometry and the Value of Auxiliary Data. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7734298

## Slide 56: Coding Exercise: A Forecast Evaluation

- Verify a calibration rank on a hand-checkable sample.
- Compare segment coverage and interval widths on the same stores.
- Explain why singleton-routing error needs a separate evaluation.

Run demand_intervals.py, complaint_sets.py, and the six tests in Conformal_Prediction. The fixed synthetic records require no fitted model. Additional practice uses the existing repeated-selection and paired-upgrade examples. Full programs appear in M7 §§7.24–7.25.

Source: M7 §§7.24–7.25. ../03_Data_and_Code/Conformal_Prediction/README.md

## Slide 57: Targeting and Delivered Opportunities

- An apparently neutral target can produce unequal delivery.
- Evaluate exposure and error costs across relevant groups.
- Housing, credit, and employment applications require their specific legal context.

The DOJ's Meta housing-ad settlement addresses discriminatory delivery as well as targeting tools. That case is evidence about housing advertising and should not be generalized into a single rule for all products.

Source: DOJ, United States v. Meta Platforms. https://www.justice.gov/crt/case/united-states-v-meta-platforms-inc-fka-facebook-inc-sdny

## Slide 58: Prediction Discussion

- Which error uses scarce review capacity?
- Which feature becomes available too late?
- Does the score support a forecast, an intervention, or both?

A deployment decision needs an explicit chain from information to prediction to action. Each link has its own empirical requirements.

Source: M7, Section 7.9, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md
