# Prediction and Machine Learning

Updated October 23, 2026. 10 curated resources. [Master Guide](../README.md).

Choose a prediction target, decision time, and evaluation split before modeling. Start with a simple baseline. Relate prediction metrics to the cost and benefit of the marketing decision.

## Reading Guide

| ID | Resource | Priority | Format |
| --- | --- | --- | --- |
| M01 | [scikit-learn: Getting Started](https://scikit-learn.org/stable/getting_started.html) | Core | Guide |
| M02 | [scikit-learn: Common Pitfalls and Recommended Practices](https://scikit-learn.org/stable/common_pitfalls.html) | Core | Guide |
| M03 | [scikit-learn: Cross-Validation](https://scikit-learn.org/stable/modules/cross_validation.html) | Core | Guide |
| M04 | [scikit-learn: Model Evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html) | Core | Guide |
| M05 | [Tuning the Decision Threshold for Class Prediction](https://scikit-learn.org/stable/modules/classification_threshold.html) | Core | Guide |
| M06 | [scikit-learn: Probability Calibration](https://scikit-learn.org/stable/modules/calibration.html) | Core | Guide |
| M07 | [scikit-learn: Ensemble Methods](https://scikit-learn.org/stable/modules/ensemble.html) | Reference | Guide |
| M08 | [Interpretable Machine Learning](https://christophm.github.io/interpretable-ml-book/) | Core | Open web book |
| M09 | [scikit-learn: Permutation Feature Importance](https://scikit-learn.org/stable/modules/permutation_importance.html) | Reference | Guide |
| M10 | [Fairlearn User Guide](https://fairlearn.org/main/user_guide/) | Optional | Guide |

Core identifies candidates for the eventual required readings. Reference material supports exercises and troubleshooting. Optional material supports extensions. Instructor material informs teaching and assessment; these labels are recommendations, not a finalized syllabus.

## Annotated Resources

### M01. scikit-learn: Getting Started

**Source:** scikit-learn contributors. [Open Resource](https://scikit-learn.org/stable/getting_started.html). **Priority:** Core. **Syllabus:** M7.

Estimators, preprocessing, pipelines, evaluation, and model selection.

**Teaching Use:** Build a baseline campaign-response model with a transparent train/test split.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### M02. scikit-learn: Common Pitfalls and Recommended Practices

**Source:** scikit-learn contributors. [Open Resource](https://scikit-learn.org/stable/common_pitfalls.html). **Priority:** Core. **Syllabus:** M7.

Inconsistent preprocessing, data leakage, and randomness.

**Teaching Use:** Give students an AI-generated pipeline with leakage and ask them to diagnose and repair it.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### M03. scikit-learn: Cross-Validation

**Source:** scikit-learn contributors. [Open Resource](https://scikit-learn.org/stable/modules/cross_validation.html). **Priority:** Core. **Syllabus:** M7.

Validation strategies, grouped observations, and time-based splitting.

**Teaching Use:** Choose a split that matches future deployment and prevents the same customer leaking across folds.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### M04. scikit-learn: Model Evaluation

**Source:** scikit-learn contributors. [Open Resource](https://scikit-learn.org/stable/modules/model_evaluation.html). **Priority:** Core. **Syllabus:** M7.

Classification and regression metrics.

**Teaching Use:** Compare metrics with the actual cost of contacting customers and missing buyers.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### M05. Tuning the Decision Threshold for Class Prediction

**Source:** scikit-learn contributors. [Open Resource](https://scikit-learn.org/stable/modules/classification_threshold.html). **Priority:** Core. **Syllabus:** M7.

Separating estimated probabilities from the decision rule.

**Teaching Use:** Select a contact threshold under explicit campaign costs and validate it on held-out data.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### M06. scikit-learn: Probability Calibration

**Source:** scikit-learn contributors. [Open Resource](https://scikit-learn.org/stable/modules/calibration.html). **Priority:** Core. **Syllabus:** M7.

Reliability of predicted probabilities.

**Teaching Use:** Compare calibrated and uncalibrated probabilities for budget planning.

**Conditions and Adaptation:** Calibration does not establish causal response to a campaign.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### M07. scikit-learn: Ensemble Methods

**Source:** scikit-learn contributors. [Open Resource](https://scikit-learn.org/stable/modules/ensemble.html). **Priority:** Reference. **Syllabus:** M7.

Random forests, gradient boosting, and model flexibility.

**Teaching Use:** Compare a tree ensemble with a simple logistic baseline using the same evaluation protocol.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### M08. Interpretable Machine Learning

**Source:** Christoph Molnar. [Open Resource](https://christophm.github.io/interpretable-ml-book/). **Priority:** Core. **Syllabus:** M7.

Feature importance, partial dependence, SHAP, and interpretation limits.

**Teaching Use:** Translate a model explanation into a managerial statement with its scope stated accurately.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### M09. scikit-learn: Permutation Feature Importance

**Source:** scikit-learn contributors. [Open Resource](https://scikit-learn.org/stable/modules/permutation_importance.html). **Priority:** Reference. **Syllabus:** M7.

Measuring a fitted model's reliance on features.

**Teaching Use:** Assess importance on held-out data and explore correlated predictors.

**Conditions and Adaptation:** Predictive importance is not the effect of intervening on a feature.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### M10. Fairlearn User Guide

**Source:** Fairlearn contributors. [Open Resource](https://fairlearn.org/main/user_guide/). **Priority:** Optional. **Syllabus:** M7.

Assessing model performance and fairness across groups.

**Teaching Use:** Audit campaign error rates across relevant groups and explain the choice of comparison.

**Conditions and Adaptation:** Fairness metrics require contextual decisions; no single metric establishes fairness.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.
