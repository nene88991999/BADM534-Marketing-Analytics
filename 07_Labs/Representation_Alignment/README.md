# Changing Text Representations in mHealth

Public optional ungraded practice. Read [M5 §5.26](../../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md), [M7 §§7.42–7.43](../../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md), and the [program README](../../03_Data_and_Code/Representation_Alignment/README.md).

## Managerial Decision

A service changes the representation of food descriptions. Compare retaining the original classifier, aligning the new coordinates, and retraining the classifier. The evaluation target is agreement with recorded source categories on previously unseen descriptions.

## Coordinate Comparison

1. Hand-calculate the rotation of `(3, -1)` and `(-3, 1)` under the supplied matrix. Apply the fixed rule that the second coordinate must be positive. Explain how both decisions change while the distance between the points stays fixed.
2. Run `alignment.py`. Reconcile all eight predictions and both-neighbor overlaps. Fit the map using only the separate training points. Compare the fitted matrix with the inverse rotation.
3. Change the rotation angle in a copy of the synthetic calculation. Record distance agreement and classification accuracy separately. Explain why geometric agreement alone cannot certify compatibility with fixed coefficients.

## mHealth Comparison

4. Run `evaluate_mhealth.py` and the tests. Reconstruct each test accuracy from `test_predictions.csv`. Verify the same 1,500-description denominator and inspect category-level errors.
5. Explain every fitted quantity and the data permitted to determine it. Trace vocabulary, IDF, SVD, the coordinate map, ridge coefficients, and dimension selection. Verify that descriptions do not cross splits.
6. Explain why character-neighbor overlap is unchanged by alignment. Compare its value with the change in classification accuracy. Distinguish the deliberately incompatible substitution from the two compatible classifiers.
7. Examine the 74 ambiguous reference descriptions, the ten descriptions whose reference category is absent from training, and labels such as `default` and `recipe`. State the evidence needed for a nutritional classification target.
8. Specify a new evaluation for descriptions first observed after a fixed date. Preserve the existing test sample as development evidence if it influences your choices. Identify how the population and estimand would change.

## AI-Assisted Coding

Ask an assistant to return the full confusion matrix, per-category denominators, zero-feature counts, and a list of every fitted object's input split. Require an independent check that changing test labels leaves all fitted objects and the selected dimension unchanged. Check the row-vector orientation on the two-point example before running the complete program.

## Adoption and Justification

Compare the one-time costs of fitting and migration with inference, review, correction, and revalidation costs over a stated workload. Keep observed accuracy separate from hypothetical monetary values. Explain whether agreement among several classifiers supplies independent evidence about nutrition, customer preferences, or permission to act. An optional prompt exercise may compare fixed policy questions with and without a verified policy document; no such model experiment is included in the saved results.
