# Human and Synthetic Research Budgets

This is optional ungraded practice for M4 §4.24 and M7 §7.37. It establishes no submission, deadline, or course-wide AI permission. The example uses invented analytic means and requires no model account.

A body-wash manager needs evidence about a premium feature and two price levels. The auxiliary source distorts overall ratings and price sensitivity. The firm must decide which comparisons still justify synthetic responses and how much human evidence to buy.

## Reproduce the Comparison

Read the [data dictionary](../../03_Data_and_Code/Auxiliary_Data/DATA_DICTIONARY.md) and run both [analysis programs](../../03_Data_and_Code/Auxiliary_Data/README.md). Calculate the premium-feature and price contrasts by hand before comparing the saved means. Explain why the two coded levels create a contrast twice the coefficient. Identify the unit of the accuracy target and the population assumptions behind it.

## Change Costs and Precision

Work on a copy of the example folder. Change the auxiliary response cost while retaining the primary cost, variances, bias features, and MSE target. Compare the rounded allocation with the asymptotic savings curve. Identify when the optimal continuous design stops using auxiliary responses. Then increase auxiliary noise variance while holding response prices fixed and explain why the information-cost ratio changes.

## Challenge the Bias Restriction

Change `omitted_feature_bias` and inspect the variance and squared-bias components separately. Explain why multiplying both sample sizes leaves the expected feature-coefficient error unchanged. Compare the smaller misspecified bias model with an expanded model allowing intercept, feature, and price bias. State what additional human evidence or substantive restriction would make the feature contrast credible.

The paper's digital-twin example supplies a separate sensitivity question. Hold its five selected primary features fixed, then add the Republican indicator to the bias dictionary. Use the [source review](../../01_Resources/31_Auxiliary_Data_and_Bias_Geometry/SOURCE_REVIEW.md) to explain the implication of the overlap. This reasoning is conditional on the reported feature sets and does not reproduce the underlying regression.

## Plan an Independent Evaluation

Specify a future customer population and product decision. Identify which respondents and concepts would be reserved from prompt selection, bias-feature selection, and final evaluation. Explain how repeated ratings from a respondent affect the sampling unit. Include research setup and validation costs alongside per-response prices, and separate coefficient accuracy from a claim about purchases or customer welfare.

An AI coding assistant can help implement a proposed change after the inputs, units, and expected result are specified. Check its calculations against a hand-worked contrast and the joint-regression checks. Describe any material assistance accurately, following the rules of an applicable assignment if this practice is later used within one.
