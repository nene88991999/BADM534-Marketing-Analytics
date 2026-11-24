# Representation Quality and Marketing Decisions

A marketing analyst may compress customer information or use AI features to identify important complaints. A high score for reconstructing the input can coexist with poor preservation of the information needed for that decision. The useful lesson is to evaluate the representation against a specified outcome, with the score's units, weights, and denominator visible.

[Massive Activations Confound Sparse Autoencoders](https://arxiv.org/abs/2611.13548v1), by Nathan Delisle and Chenhao Tan, motivates this lesson through language-model representations. Its [repository](https://github.com/nathandelisle/massive-saes) supplies inspectable evaluation code and saved numerical results. The [source review](SOURCE_REVIEW.md) distinguishes reported research findings, independently recalculated values, and original marketing illustrations.

| Course Connection | Teaching Connection |
| --- | --- |
| M7: Model Evaluation | Compare aggregate reconstruction, error outside a dominant direction, feature stability, and task performance |
| M5: Text Measurement | Check whether a representation preserves a complaint category needed for an operational response |
| M4: Segmentation | Examine whether cluster descriptions and customer assignments recur under reasonable changes in initialization and preprocessing |
| M2: Scaling and Visualization | Show how one large-scale dimension determines a pooled score |
| M9: Marketing Dialectics | Evaluate the evidence behind a claim that an AI system is understandable or accountable |

The [implemented case](CASE_DESIGN.md) uses four invented vectors in M7 §7.39 and exact decompositions in §7.40. [Two complete Python programs and six independent tests](../../03_Data_and_Code/Representation_Evaluation/README.md) accompany two editable diagrams, four Session 11 slides, and [optional ungraded practice](../../07_Labs/Representation_Evaluation/README.md). M4 §4.25 and M5 §5.25 connect feature interpretation and attributed claims. No sparse autoencoder is trained.

Thirteen unchanged source and result files are preserved under `reference/`, with MIT and CC BY 4.0 notices, a pinned commit, and hashes in the [manifest](manifest.json). The paper itself is linked because its arXiv license does not supply general redistribution permission. The original [calculation checks](source_checks.py) use Python's standard library; their results are in [source_checks.json](source_checks.json). These checks establish arithmetic and source-file fidelity. They do not reproduce model training, model inference, or the authors' statistical uncertainty.

The [catalog](catalog.json) uses namespace `representation-evaluation`. The cases are integrated into notes and Session 11 within existing meeting time; assessment requirements remain pending.
