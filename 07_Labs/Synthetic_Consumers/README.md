# Synthetic Consumers and Product Concept Screening

This is optional ungraded practice accompanying M4 §4.23, M5 §5.23, and M7 §7.36. The [complete programs and supplied inputs](../../03_Data_and_Code/Synthetic_Consumers/README.md) use standard-library Python and entirely synthetic examples. No model account is needed.

## The Product Decision

A fictional personal-care firm can fund human research for only a subset of its product ideas. Explain which comparison supports a shortlist and how the firm could discover promising concepts that its screening rule rejects. Keep purchase-intent ratings distinct from observed buying and attribute-level willingness to pay.

## Reproduce and Explain

1. Run both programs using the commands in the example README. Recover the 4.25 rating for the specified response by hand. Identify the minimum similarity, normalization denominator, and category weights.
2. Compare both anchor sets while holding the response fixed. Explain why the imposed values illustrate sensitivity without estimating the effect of specific words on a real model.
3. Remove the duplicate refill/p01 response. Verify that equal-persona means stay unchanged while the row-weighted comparison changes. State the observation unit needed for each average.
4. Give one response five equal similarities. Check its uninformative status and the incomplete concept aggregate. Explain the additional interpretation that would be imposed by silently replacing it with uniform weights.
5. Reproduce the pooled, reversed, and compressed concept comparisons. Explain how the same overall category shares coexist with different shortlists. Preserve undefined correlations and unresolved selection ties.

## AI-Assisted Sensitivity Analysis

Ask a coding assistant to change the weight on the pooled distribution in the compressed pattern while retaining the same reference roster. Require a new output directory or filenames so the released example remains reproducible. The prompt should specify equal concept weights, explicit missing and tie behavior, and a check against the original endpoints. Inspect the code and explain one result independently.

As the pooled weight approaches one, concept differences shrink. For weights strictly below one, ordering remains unchanged in exact arithmetic for this construction. At one, all scores tie. Explain why a perfect ranking at an interior weight supplies limited evidence about the magnitude of a demand difference. Numerical tolerances near the endpoint require an explicit interpretation.

## A Prospective Validation Design

Specify the target population and recruitment process, the fixed concept descriptions, development and final concept sets, model and embedding versions, anchor selection, and the screening rule. Keep final human outcomes outside all configuration choices. Include a random sample of rejected concepts and explain how their sampling probabilities affect the estimation of missed opportunities. State which additional observations would be needed to evaluate purchases rather than stated intent.

An optional live extension would require appropriately obtained human data and a versioned record of the complete measurement procedure. The published study's private respondent records are absent from the inspected repository. Do not treat the invented panels or public practice checks as external validation of a deployed system.

## Consumer Representation

Use M9 §9.18.4 to evaluate a claim that generated personas show what customers want. Identify the role of actual customers' judgments, the evidence that would challenge the firm's interpretation, and the opportunities people have to express conditions or contest a decision. Explain how those reasons affect the proposed use of synthetic research.
