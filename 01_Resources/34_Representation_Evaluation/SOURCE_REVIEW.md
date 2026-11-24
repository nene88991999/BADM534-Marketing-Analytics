# Reconstruction, Stability, and Interpretation

## Research Finding

Delisle and Tan study sparse autoencoders that reconstruct language-model activations. In affected settings, a dominant principal component can inflate overall reconstruction scores and make highly ranked features unstable across training seeds. Their Qwen-2.5-7B example explains 99.96% of total variance while leaving about 33% of variance outside PC1 unexplained. Their correction trains on the orthogonal component and restores PC1 during reconstruction. The paper reports improved reconstruction and top-feature reproducibility in affected models. Effects depend on the model, layer, preprocessing, and evaluation procedure. Its sparse-probe results also show that improved representation diagnostics need not produce large task-accuracy gains. See [version 1, §§3–7 and Appendices A, E, H](https://arxiv.org/html/2611.13548v1).

The course inference is to select an evaluation target from the managerial decision before relying on a convenient internal score. These experiments concern model activations; they do not estimate customer behavior, identify consumer motives, or establish a general correction for marketing datasets.

## What the Saved Results Measure

The archived [fidelity table](reference/results/additional/reconstruction/nine_model/nine_model_fidelity.csv) contains standard and bypass rows for nine models. Its provenance specifies 200,000 held-out WikiText-103 tokens, with the mean and PC1 obtained from the training store. There are three or five seeds per row. For Qwen-2.5-7B, the standard row has total fraction of variance unexplained (FVU) 0.00036992 and orthogonal FVU 0.329781. Calculating `100 * (1 - fvu_total)` gives 99.963008% total variance explained. Calculating `100 * fvu_content` gives 32.9781% orthogonal variance unexplained. These use different denominators.

The same table gives Qwen orthogonal FVU 0.217913 after bypass, a relative reduction of approximately 33.92%. The original calculation checks recompute these values from the archived table. They verify transformations of saved measurements; the activation-level experiment remains unexecuted.

The [feature summary](reference/results/tables/features_summary.csv) uses another comparison convention. Its `top50` column averages comparisons from reference seed 42 to four other seeds; `top50_allpairs` uses all 20 ordered comparisons. Qwen's standard/bypass `top50` values are 6% and 99.5%, while the all-pairs values are 6% and 96.8%. The fidelity table's corresponding sharing entries are 6% and 98% in its own smaller seed collection. Each number must travel with its file, seed set, selection rule, and denominator. Combining these columns into one purported replication would change the comparison.

## Evaluation Code Worth Reading

The archived [matching implementation](reference/experiments/language/pc1_v3/v3/common/matching.py) compares decoder directions using signed cosine similarity. Its default best-match comparison can use every direction in the other dictionary, while its dictionary-wide denominator includes alive features in the reference dictionary. A direction and its negation have different meanings when coefficients are nonnegative. An absolute-cosine comparison would change this metric. The file also provides mutual and one-to-one matching functions; the default best match is a different correspondence rule.

The [loading and reconstruction implementation](reference/pc1_sae/__init__.py) centers each activation with the saved training mean, projects onto a saved PC1 direction, encodes the remainder, and restores the projection during decoding. It requires the preprocessing assets for the matching checkpoint and layer. Deleting the leading component from an ordinary customer dataset would be a different operation. That component may carry business-relevant information.

The [experiment guide](reference/experiments/README.md) separates training, evaluation, probing, behavioral edits, and explanation scoring. The [requirements](reference/requirements-models.txt) and loader show that reproducing the models requires a substantial environment and checkpoint access. The small course example can establish the mathematical issue without these dependencies.

## An Original Decision Example

To see what determines an aggregate reconstruction score, split a centered input into a leading direction and its orthogonal remainder. Let $V_1$ and $V_{\perp}$ be their squared variation in the evaluation sample, and let $E_1$ and $E_{\perp}$ be the corresponding squared reconstruction errors. Orthogonality gives

$$
\frac{E_1+E_{\perp}}{V_1+V_{\perp}}
=w_1\frac{E_1}{V_1}+(1-w_1)\frac{E_{\perp}}{V_{\perp}},
\qquad w_1=\frac{V_1}{V_1+V_{\perp}}.
$$

The left side is total FVU. Each component error on the right is weighted by its share of variation; both component denominators must be positive. When the leading direction is reconstructed exactly, the remaining component's error receives weight $1-w_1$. A small weight can make that error almost invisible in the aggregate. The example below makes all of these quantities observable by construction.

Consider four equally weighted, invented centered representations of complaint text: `(-100, -1)`, `(-100, 1)`, `(100, -1)`, and `(100, 1)`. The first coordinate represents a large document-style component by construction. The second represents a complaint distinction used to route a case for review; a positive value requires review. These meanings are imposed for the illustration.

Representation A preserves the first coordinate and replaces the second with zero. It explains approximately 99.9900% of total squared variation, while missing both cases that require review. Representation B multiplies the first coordinate by 0.98 and preserves the second. It explains approximately 99.9600% of total variation and routes both review cases correctly. The aggregate reconstruction ranking therefore reverses the ranking for the chosen decision. The [original program](source_checks.py) verifies the arithmetic and reports the denominators.

This calculation requires no claim about what a real model's first component means. A practical adaptation would use a manually checked complaint set, fit transformations using training data, and evaluate held-out routing performance and customer-group outcomes. The observed task performance would decide whether a proposed preprocessing change is helpful.

## Feature Importance and a Unique Explanation

Two different decompositions can reconstruct the same vector. In an original two-dimensional illustration, unit directions proportional to `(1, 1)` and `(1, -1)`, each with coefficient `sqrt(2)`, sum to `(2, 0)`. Directions proportional to `(1, 2)` and `(1, -2)`, each with coefficient `sqrt(5)`, produce the same result. Removing one term leaves a large error in either representation. The size of that error alone does not select a unique underlying concept.

This is an exact algebraic counterexample, not a trained SAE or an estimated marketing mechanism. Its teaching role is to separate sensitivity to an intervention on a representation from the substantive meaning assigned to a feature. Feature stability, prediction, and human interpretation need their own evidence. For a segmentation application, compare customer assignments and label-aligned descriptions across runs rather than treating a cluster number as a stable behavioral type.

## Review Scope and Rights

The review covers the paper's main evaluation and repair arguments, selected appendix definitions, and 13 repository files at commit `a3df7fff7a3f03012a116cbd092d2a24f2941e64`, dated November 10, 2026. The arXiv record identifies the paper as accepted at NeurIPS 2026. That publication-status statement comes from the record; no independent conference-program check was performed.

The repository licenses code under MIT and results under CC BY 4.0. Both notices are preserved. The paper uses the arXiv perpetual non-exclusive license and is linked rather than republished. The source subset is incomplete and is provided for inspection. No upstream script, dependency installation, checkpoint download, model training, model inference, or LLM evaluator was executed. The original standard-library checks cover the archived-file hashes, saved-result calculations, and two invented mathematical illustrations.
