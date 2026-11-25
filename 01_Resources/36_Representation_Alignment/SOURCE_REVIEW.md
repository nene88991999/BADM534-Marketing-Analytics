# Research Evidence and Course Applications

## Factual Transfer

Cheng, Liu, Yau, and Ré's November 25, 2026 [post](https://hazyresearch.stanford.edu/blog/2026-11-25-platos-key) reports 20 pairwise comparisons among 12 base language models. A rotation and scale map hidden states across frozen models. On held-out facts both models recall, median transfer accuracy is 41%, versus 55% for within-model swaps. Layers are chosen on separate validation subjects. Selecting by nearest-neighbor similarity gives 4.5% median validation transfer accuracy, about one tenth of selection by transfer accuracy. These are different evaluation criteria.

The recovery comparison uses 2,600 recipient misses. Auxiliary prompting or answer-ranking checks classify 1,463 as available knowledge; mapped states recover 267, approximately 18% of that selected subset. This operational definition conditions the denominator. Factual recall in the tested models leaves broader reasoning and customer applications open.

## Related Research

Huh, Cheung, Wang, and Isola's [The Platonic Representation Hypothesis](https://arxiv.org/html/2405.07987v5), especially §§2 and 6, examines representational convergence and discusses measurement choices, counterexamples, and common research practices. The philosophical application in M9 asks what additional evidence supports truth or justification when model outputs agree. It is a course interpretation.

Gekhman and coauthors' [Inside-Out: Hidden Factual Knowledge in LLMs](https://arxiv.org/html/2503.15299v4) defines knowledge through answer ranking and distinguishes internal from observable scoring methods. Its §7 discusses computational cost and sensitivity to answer-label errors. Comparing prompt conditions in a service exercise evaluates those conditions; measuring internal knowledge would require the paper's additional operations and definitions.

## Original Course Examples

The synthetic case holds eight invented outcomes fixed while changing coordinates. An orthogonal rotation preserves distances and nearest neighbors, while a classifier tied to the second coordinate changes predictions. A separate distortion of the style coordinate changes neighbors while preserving the classification target. Fitting the inverse rotation on distinct training points restores compatibility.

The mHealth example compares locally constructed word and character representations. Vocabulary, inverse-document frequency, SVD directions, alignment, and classifiers use training descriptions. Validation selects the common dimension before any test score is calculated. All character representations have the same neighbors under a positive global scale and an orthogonal map. Classification changes because the existing coefficients refer to a particular basis. Retraining evaluates a different feasible response to an encoder change.

The reference labels are recorded modal source categories, including labels such as `default` and `recipe`. They measure agreement with the recorded classification system. Nutrition judgments, customer preferences, model-provider performance, and commercial returns require separate evidence.

## Access and Rights

Reviewed November 25, 2026. The post was read directly, including its displayed comparisons and links. A dated HTML snapshot and hash are retained in the ignored local publication folder. No dedicated repository for this experiment is linked on the inspected page. Its VecMap link concerns earlier embedding-alignment work. No upstream program, checkpoint, or model API was executed.

The blog has no redistribution license identified in the inspected page, so the public course preserves links and original annotations. The two related arXiv versions identify CC BY 4.0; this addition links them without reproducing their full texts. The course calculations are original and are separate from a replication of the neural-model experiments.
