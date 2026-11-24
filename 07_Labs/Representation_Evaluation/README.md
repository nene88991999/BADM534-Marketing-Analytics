# Reconstruction and Customer Review

Public optional ungraded practice. Read [M7 §§7.39–7.40](../../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md) and the [programs and dictionary](../../03_Data_and_Code/Representation_Evaluation/README.md). All vectors and outcomes are synthetic.

## Managerial Decision

A service manager chooses a representation for identifying cases requiring review. Compare reconstruction quality and the consequences of the resulting routing rule on the same cases.

## Investigation

1. Compute both coordinate means and sums of squares for the four vectors at style scale 100. Predict which reconstruction has lower total FVU. Use the positive-case denominator to predict recall separately.
2. Run both programs and six tests using the README commands. Verify the variance-weighted identity and the recorded error vectors against your calculations.
3. Change the style scale in a copy of the inputs. Derive the scale at which A and B have equal total reconstruction error with the same 0.98 shrinkage factor. Compare the routing result on either side of that scale. Explain which managerial judgment would justify the coordinate weights.
4. Draw each decomposition of `(2, 0)`. Calculate the sum of coefficients and the error after removing the first contribution. Explain why equal reconstruction does not establish equal penalized loss or equal psychological meaning.
5. Propose an evaluation for learned customer-text representations. Fix the target and reference labels, split by customer and time as appropriate, fit preprocessing on training data, and reserve held-out outcomes. Specify a feature-matching rule across seeds and keep that score separate from task performance.

## AI-Assisted Coding

Ask an assistant to report aggregate error, component errors, variance weights, the confusion matrix, and the positive-case denominator. Require an assertion that the weighted component FVU equals total FVU. Check the returned arrays against a hand calculation before interpreting the result.

## Interpretation

Recommend a representation under the stated review objective. Explain what would need independent validation before deploying it. A feature name supplied by an analyst or LLM does not establish a causal mechanism, a customer's preference, or permission to act on that customer.
