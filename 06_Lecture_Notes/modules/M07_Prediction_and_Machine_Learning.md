# M7. Prediction, Machine Learning, and Marketing Actions

A retailer wants to anticipate next month's customer purchases and allocate limited service capacity. A model that predicts historical purchases accurately may still fail when deployed: its features may contain future information, its test set may reuse the same customers as training, or its objective may reward errors that are costly for the business. Prediction should therefore be designed around an explicit deployment situation.

## 7.1 Specify the Forecast Origin and Target

A prediction task needs a target variable, a forecast origin, a horizon, and an eligible population. For customer churn, define what counts as churn and when that status becomes observable. In a subscription business, cancellation may be explicit. In noncontractual retail, “no purchase for 90 days” is an operational label, not proof that a relationship has ended permanently.

Construct predictors using information available at the forecast origin. If predicting purchases during November, features might use transactions through October 31. November support contacts, returns, or campaign interactions are unavailable at that origin. A database may contain them when the analyst extracts the file, making leakage easy to overlook. Store feature timestamps or document their measurement windows.

The deployment population determines the validation design. Predicting future behavior for existing customers differs from predicting behavior for newly acquired customers. A random row split can place the same customer in training and test data, giving a favorable assessment for a task that actually requires generalization to new customers. A time split addresses future periods, while a customer-group split addresses new customers. Some tasks require both.

![The validation split should reproduce the information available at deployment.](../figures/M07_splits.png)

A random row split can reuse a customer's history in training and test data. Holding out complete customers evaluates generalization to new customers; holding out later periods evaluates future performance. The intended use determines which comparison is relevant.

## 7.2 Baselines, Loss Functions, and Regularization

A baseline should be operationally meaningful. For sales forecasting, compare with the previous period, the same period last year, or a simple customer-history average when those quantities are available. For classification, compare with a constant probability and a transparent logistic regression. A complex model's incremental value is easier to assess when these comparisons are reported on the same test observations.

A supervised learner minimizes a loss that quantifies prediction error. Squared error penalizes large deviations strongly; absolute error gives a different compromise under skewness. For a binary outcome, log loss is

$$
L=-\frac{1}{n}\sum_{i=1}^n\{y_i\log\hat p_i+(1-y_i)\log(1-\hat p_i)\}.
$$

Here $y_i$ is the observed binary outcome and $\hat p_i$ is its predicted probability. Confident mistakes receive large penalties. The loss evaluates probability forecasts; it does not by itself encode the cost of a marketing action. Select a loss appropriate to the prediction task, then evaluate how the forecasts support the downstream decision.

Regularization constrains a flexible model to reduce overfitting. Ridge regression adds a squared-coefficient penalty, while lasso adds an absolute-coefficient penalty and can set some coefficients to zero. Standardize features appropriately when the penalty depends on coefficient scale, and fit that transformation using training data. The regularization strength is a tuning choice selected with validation data, not with the final test sample.

Bias and variance describe an important tradeoff. A rigid model may systematically miss a pattern; a very flexible model may fit noise specific to the training sample. More data can help, but only if it represents the deployment problem and adds relevant information. A million duplicated or highly dependent rows can provide less useful information than their count suggests.

## 7.3 Logistic Regression, Trees, and Ensembles

Logistic regression maps a linear index to a probability:

$$
\hat p_i=\frac{1}{1+\exp[-(\beta_0+x_i^\top\beta)]}.
$$

The coefficients describe changes in log odds under the model. A coefficient's effect on probability depends on the starting probability and other predictors. Predicted probabilities are often easier to communicate than odds ratios, especially when the business decision uses expected counts or contribution. Nonlinear features and interactions can extend the model while preserving a relatively transparent structure.

A decision tree partitions the feature space into regions using sequential splits. It can represent interactions without specifying them manually: a spending threshold might matter only among recent customers. Deep trees can fit small idiosyncratic groups, making pruning, minimum leaf sizes, and validation important. A split point near an observed value should not automatically be interpreted as a behavioral threshold.

Random forests average trees fitted with randomness in observations and candidate features, reducing instability relative to a single tree in many settings. Gradient boosting builds an ensemble sequentially to improve a chosen loss, with tuning choices such as tree depth, learning rate, and number of iterations. These methods can be effective on tabular data, but performance remains empirical. More complexity also increases the burden of checking leakage, calibration, computation, and reproducibility.

Neural networks learn layered representations and can be especially useful for text, images, or large complex datasets. Their flexibility does not eliminate the need for baselines or careful evaluation. In a modest customer table, a well-tuned simpler model may be competitive and easier to maintain. Choose the method based on task performance and practical constraints rather than the apparent modernity of the algorithm.

## 7.4 Validation, Cross-Validation, and Leakage

Use training data to fit parameters, validation data or cross-validation to select models and tuning choices, and a final test sample to estimate performance after those choices are fixed. Reusing the test sample repeatedly turns it into a validation sample, even if the file is still named “test.” Report the procedure so the claimed holdout remains meaningful.

All learned preprocessing belongs inside the training process. This includes imputation, scaling, feature selection, vocabulary construction, dimensionality reduction, and target-based encodings. In cross-validation, fit each transformation on the training fold and apply it to that fold's validation observations. A pipeline makes the sequence explicit. The [scikit-learn pitfalls guide](https://scikit-learn.org/stable/common_pitfalls.html) documents implementation patterns for this separation.

Time-series and grouped data need adapted splits. Rolling-origin evaluation trains on earlier periods and predicts later ones, potentially repeating this across several origins. Grouped validation holds out complete customers, households, stores, or other relevant units. If a target window overlaps a training outcome window, a temporal gap may be necessary. Document the dates and units assigned to each split.

A useful audit asks when each feature became observable. In a marketing-call dataset, call duration can be useful after a call but unavailable when deciding whom to call. A model using that feature answers a different prediction problem. The feature's legitimacy follows the decision time, not whether a package accepts it or whether it improves accuracy.

## 7.5 Case Study: Accuracy Can Conceal a Useless Model

Suppose 5% of 1,000 customers make a purchase in the target window. A model predicting no purchase for everyone achieves 95% accuracy while identifying no purchasers. A different model flags 100 customers, including 30 purchasers and 70 nonpurchasers. It has 30 true positives, 20 false negatives, 70 false positives, and 880 true negatives.

The second model's precision is 30%, recall is 60%, and accuracy is 91%. Its lower accuracy coexists with a potentially useful ranking for a limited-capacity task. Whether it improves profit depends on the action, costs, and whether the purchase probabilities under that action are the relevant quantities. Accuracy alone cannot make that decision.

ROC curves compare true-positive and false-positive rates across thresholds. Precision-recall curves focus on the tradeoff between finding positives and the composition of the flagged group, which can be informative when positives are rare. Both depend on the evaluation setting; precision is especially sensitive to prevalence. Lift at a specified contact fraction compares the selected group's outcome rate with the population rate, but observed lift is not automatically an incremental treatment effect.

Report metrics with their operational units. For a service team that can review only 100 cases per week, precision among the top 100 and the number of important cases missed may be more relevant than a global ranking metric. Use a holdout that reflects the weekly population and inspect uncertainty in the metric when counts are small.

## 7.6 Ranking and Calibration Answer Different Questions

A ranking model orders cases from more likely to less likely. A calibrated probability model assigns probabilities that correspond to observed frequencies in relevant groups. If customers assigned probability 0.20 purchase about 20% of the time in a suitable evaluation population, that group is calibrated. Calibration can vary across segments and over time even when overall performance looks satisfactory.

A strictly increasing transformation of scores preserves their ranking. Squaring probabilities between zero and one therefore leaves a ranking-based AUC unchanged, apart from practical handling of ties or finite precision, while generally changing calibration. A predicted probability of 0.50 becomes 0.25. If the original 0.50 group purchases half the time, the transformed probabilities understate its frequency.

![A monotonic score transformation preserves ranking while changing probability calibration.](../figures/M07_calibration.png)

For calibrated forecasts, predicted probabilities equal observed frequencies. After squaring an initially calibrated score $p$, the reported probability is $q=p^2$, while the observed frequency remains $p=\sqrt{q}$. Expected counts and profit calculations depend on the probability scale, so unchanged ranking performance does not guarantee unchanged decision quality.

Inspect calibration plots and proper scoring rules, such as log loss or the Brier score, on held-out data. Calibration methods themselves require fitting and should use data separate from the final evaluation. If the deployment population changes, recalibration may be necessary. A single global correction may be insufficient when the relationship changes differently across groups.

## 7.7 Thresholds Should Reflect the Decision

Consider a classification action in which a false positive costs $C_{FP}$ and a false negative costs $C_{FN}$, with zero cost for correct classifications. For a calibrated probability $p$, predicting positive has expected cost $C_{FP}(1-p)$ and predicting negative has expected cost $C_{FN}p$. The cost-minimizing rule predicts positive when

$$
p>\frac{C_{FP}}{C_{FP}+C_{FN}}.
$$

If an unnecessary review costs one unit and missing a true issue costs nine units, the threshold is 0.10 under this simplified loss. A threshold of 0.50 would encode a different cost balance. Capacity constraints, review effectiveness, and heterogeneous costs require a more detailed rule. The formula is useful because it makes the decision assumptions explicit.

A marketing intervention usually needs a causal comparison beyond this classification loss. For a coupon, let $p_i(1)$ and $p_i(0)$ be purchase probabilities with and without the coupon, $m$ the contribution before the discount, $d$ the discount paid on a treated purchase, and $c$ the contact cost. A simple incremental expected contribution is

$$
\Delta\pi_i=m\{p_i(1)-p_i(0)\}-d\,p_i(1)-c.
$$

The discount is paid on all treated purchases in this setup, including purchases that would have happened anyway. The equation assumes one relevant purchase opportunity and a fixed discount and contribution. It can be extended to spending, multiple purchases, returns, and heterogeneous margins.

## 7.8 Case Study: Targeting the Most Responsive Customers Can Lose Money

Take $m=40$, $d=5$, and $c=2$. Customer A has purchase probabilities 0.80 with the coupon and 0.78 without it. Customer B has probabilities 0.30 and 0.15. A has the higher treated response probability, but incremental contribution is $-5.20 for A and $2.50 for B.

| Customer | Purchase With Coupon | Purchase Without Coupon | Incremental Contribution |
| --- | ---: | ---: | ---: |
| A | 0.80 | 0.78 | -$5.20 |
| B | 0.30 | 0.15 | $2.50 |

![Baseline purchasing and discount expense can reverse a response-based targeting rule.](../figures/M07_targeting.png)

Incremental purchasing contributes $0.80 for A and $6.00 for B, while discount and contact costs are $6.00 and $3.50, respectively. These values follow from the assumed purchase probabilities. Estimating their difference from customer data requires treatment variation and an identification strategy. Uplift or heterogeneous-treatment-effect models address that causal target under their conditions; they are not ordinary response models with a different name.

Evaluate a targeting policy on data that support its value comparison. A randomized holdout or a carefully designed policy evaluation can estimate incremental contribution for the selected group. Estimating a model and reporting its value on the same observations used to choose the policy can overstate performance. Budget constraints also matter: a customer with positive expected value may still be excluded when another customer offers greater value per unit of scarce capacity.

## 7.9 Interpretation, Fairness, and Deployment

Feature importance describes a relationship between a fitted model and its inputs under a chosen method. Permutation importance measures the change in predictive performance after disrupting a feature, with complications when predictors are correlated. Partial-dependence plots average predictions over a reference distribution and can involve unrealistic combinations of correlated features. Local explanation methods describe the fitted prediction under their conventions. These tools do not automatically identify causal effects of changing a feature.

Evaluate performance across groups relevant to the application and examine how errors translate into service or opportunity. A model can be accurate on average while performing poorly for new customers, small stores, or a language group with sparse training data. Protected or sensitive attributes and proxies require appropriate institutional and legal review for the intended use. The consequences of errors depend on the decision and the affected customers.

Deployment requires monitoring the input distribution, missingness, outcome frequency, calibration, and decision value. A change in model accuracy can reflect changing customer behavior, instrumentation, or policy. Record versions and retain a reproducible baseline. If an intervention changes the behavior that generates future training data, the model's environment becomes endogenous to its use, because its recommendations change subsequent exposure and behavior.

## 7.10 AI-Assisted Workflow, Practice, and Readings

Ask an assistant to create an evaluation plan before choosing a model. Specify forecast origin, horizon, unit, grouping, baseline, loss, and final holdout. Require a feature-availability table and a pipeline that fits transformations only on training data. Have it produce both a metric table and an explanation of the operational decision each metric supports.

For practice, verify the 91% accuracy and 60% recall in the rare-purchase example. Square a small set of predicted probabilities and confirm that their order is unchanged while expected purchase counts change. Recalculate the coupon case with a $1 discount and explain which customer becomes more attractive. Finally, identify why a model trained on all customers' latest outcomes cannot honestly claim to predict those same outcomes out of sample.

[An Introduction to Statistical Learning](https://www.statlearning.com/) develops the central learning methods. The [scikit-learn evaluation guide](https://scikit-learn.org/stable/modules/model_evaluation.html) provides metric definitions and implementation references. [Hagen and colleagues (2020)](https://doi.org/10.1007/s11002-020-09535-7) connect machine-learning tools to behavioral marketing questions.
