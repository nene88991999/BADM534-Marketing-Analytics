# Combining Training Sources for a Customer-Service Assistant

## Managerial Decision

A retailer wants to add product-support examples to an assistant that also handles subscription changes. The existing evaluation reports a high average rate of appropriate responses. The retailer must decide which comparisons establish that a combined model provides appropriate service across request types and account contexts. A behavior that appears only in one context may receive little weight in the aggregate score.

This proposed case links the paper's controlled result to that decision. It introduces the mechanism through harmless differences in response style, then considers evidence about more consequential service outcomes. The source paper contains no observed retailer, cancellation, mHealth, or consumer-welfare results.

## Part One: A Two-Feature Regression

Use an explicitly synthetic response-style score, measured in arbitrary units. Let the two features describe the training task and a source tag. Source A always combines the task and tag and has expected score one. Source B contains the same task without the tag and has expected score zero. The benchmark fits Source A alone; comparisons add Source B while keeping the Source A observations fixed. Evaluation considers a different task containing the tag.

Fit ridge regression with a sum of squared residuals and a fixed coefficient penalty. Following Appendix I, let the source-A features be `(phi, s)` and source-B features be `(phi * sqrt(q), 0)`. Here `q` describes similarity of the source-B task feature, `phi` and `s` set the feature scales, and `a = lambda / phi**2`, `c = lambda / s**2` express the effective penalties. The exact conditional-model comparison is

```text
L = 1 / (1 + c/n_A + c/(a + q*n_B))
```

`L` is the expected contribution of the tag to the synthetic score, normalized by the source-A score. It is not a response probability. Use the paper's illustrative `a = 50`, `c = 1500`, and `n_A = 5000` to make the changing attribution visible. Compare matched data (`q = 1`) with unrelated data (`q = 0`). Also compare mixtures at a fixed total of 30,000 observations.

A course implementation should solve the two-by-two normal equations independently and compare that solution with the formula. Preserve the sum-loss convention: converting to mean squared error while keeping the same numerical penalty changes the experiment. Show a sensitivity comparison with a different feature scale or penalty, since the attribution follows those assumptions. The construction demonstrates the proposed regression mechanism; it is not a replication of subliminal transfer in a language model.

## Part Two: Conditional Customer-Service Evaluation

Construct a separate hypothetical table of service requests with stable request IDs, request type, account context, model version, and independently defined outcome labels. Appropriate outcomes include a correct policy explanation, successful completion of a requested cancellation, and escalation when the evidence is insufficient. Apply the same requests across model versions and report both overall and context-specific rates. Keep a count of unanswered requests and unavailable judgments.

Any illustrative rates should be declared as imposed values. Their purpose is to show how a weighted average can conceal a context's poor performance. They provide no estimate of the prevalence of training-data poisoning or of harm caused by a particular company. The paper motivates the comparisons; evidence from the retailer would determine the actual rates.

For repeated model selection, split requests before choosing checkpoints or prompt variants. Use a development sample for selection and an untouched request sample for the final comparison. Keep response samples nested within requests when quantifying uncertainty. Review machine-positive and machine-negative judgments against a stated human rubric, and report failures to obtain a judgment separately.

## Figures and Course Placement

An editable TikZ diagram can show two training groups and the association that becomes distinguishable after they are combined. A second figure can place an aggregate service score beside rates by request context, with observation counts and common scales. A curve for `L` should be labeled as a synthetic regression result with its penalty and feature assumptions beside it. Use Illinois navy and orange, distinguish series with markers or line styles, and provide the underlying table and text description.

The primary placement is M7's discussion of regularization, selection, and model evaluation, with a reference to M3's multiple-regression comparison. M2 supplies source and observation-unit checks. M8 considers model and supplier changes. M9 asks what evidence supports a firm's assurance that customers retain meaningful options. A focused discussion could replace an existing M7 comparison; a longer coding exercise would remain optional. No additional meeting, graded task, or AI-use rule is established by this design.

## Implementation Requirements

A future implementation should include a small reproducible Python program, explicit synthetic inputs, an independent normal-equation check, expected outputs, editable figures, and a complete Markdown companion. The two source designs, adding observations and changing shares at a fixed total, need separate displays. The current resource review supplies [verified published aggregates](source_checks.json) and the [measurement assessment](SOURCE_REVIEW.md); it does not release this proposed course exercise.
