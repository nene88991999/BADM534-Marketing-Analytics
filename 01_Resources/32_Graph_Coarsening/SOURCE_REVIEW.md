# Preserving Information When a Network is Compressed

A retailer may reduce a large network to a smaller set of zones to lower the cost of analysis. The resulting representation needs to preserve the outcomes used in the decision. Connections between groups, average features, travel times, and customer-specific predictions are distinct objects. GraCo makes several of these choices explicit and provides a useful setting for evaluating the assumptions embedded in an analytical workflow.

## Partition, Aggregation, and Reconstruction

GraCo assigns each of the original $N$ nodes to one of $n$ supernodes. The binary membership matrix $Q_b$ has shape $N\times n$, with one unit entry per row. For an undirected weighted adjacency matrix $A$, the coarse adjacency is $A_c=Q_b^\top A Q_b$. An off-diagonal entry sums the weights crossing between two groups. The default builder removes diagonal entries, so within-group edges are absent from the returned coarse adjacency. [Paper, §2; pinned builder](reference/core/builders.py).

Node features require a separate reduction matrix $P$. Under binary lifting and the default pseudoinverse, $P=(Q_b^\top Q_b)^{-1}Q_b^\top$ averages features within each group. The lifted values $Q_bPx$ assign each member its group's mean. Group sizes must accompany those means when calculating a population average or total. GraCo's default lifting is instead degree-normalized for `normalized_self_loop`; the simple averaging formula applies when the combinatorial convention is chosen. This distinction matters when interpreting a feature as spending, demand, or population. [Paper, §3; pinned normalization code](reference/core/q.py).

Preserving the feature values used to form a representation does not establish preservation of a different decision outcome. The four-zone example in [CASE_DESIGN.md](CASE_DESIGN.md) retains its revenue feature and associated quadratic graph energy exactly while losing travel inside a merged zone. The implication follows from the constructed graph. GraCo supplies no general guarantee of preserving shortest travel times, service thresholds, causal effects, or willingness to pay.

## A Metric Changes the Method Ranking

Table 4 compares methods on Cora and PubMed under a common self-loop-normalized Laplacian. Its criteria include restricted spectral approximation, eigenvalue error, convolution-matching error, and label purity. Local variation has Cora RSA 0.67 versus Leiden's 1.58, where lower is better. Leiden has lower convolution-matching error, 29.2 versus 32.9 thousand. Both report an achieved reduction ratio of 0.70 for these rows. The preferred method therefore changes with the criterion even in this selected same-ratio comparison. [Paper, Appendix B.5, p. 25](https://arxiv.org/html/2611.01200v1#A2.SS5).

The broader benchmark also requires attention to the achieved reduction. On PubMed, Table 4 reports ratios of 0.79 for METIS and 0.64 for GBGC against a requested 0.70. Those methods produce different-sized outputs. Runtime comparisons need the original graph size, retained size, hardware, preprocessing, and tuning budget. The paper distinguishes out-of-memory, timeout, and solver failures. Its numerical rankings are specific to the reported defaults and datasets.

For marketing, select the primary outcome before comparing compression methods: for example, retained access to an available store, held-out recommendation quality, recall for a small group, or profit under a specified policy. Spectral and feature metrics can help explain how the representation changed. They do not establish the marketing outcome by themselves. The paper explicitly leaves training graph neural networks on the coarsened graphs to a later release (§1, p. 2), so this release supplies no trained-model marketing validation.

## Preprocessing Changes the Population and Relationships

The pinned [preprocessing function](reference/loaders/preprocess.py) defaults to removing self-loops, symmetrizing the graph, and retaining only its largest connected component. For weighted reciprocal edges, symmetrization uses their mean. These transformations support the mathematical assumptions of the implemented methods. For marketing data, they can also change the measured population or the meaning of a relation.

The existing synthetic retail network has 800 people, including 150 at a disconnected origin. Keeping only the largest connected component removes that origin. Known five-minute access remains 550 people, while its reported share changes from $550/800=68.75\%$ to $550/650=84.62\%$. The increase of 15.87 percentage points comes entirely from changing the denominator. The origin also has a store with unknown status; retaining it preserves the original lower and upper access bounds. [Existing case, M5 §5.21](../../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md).

Direction can carry substantive information in referrals, follows, transfers, and one-way travel. Averaging reciprocal weights creates a new relation. A student should state the edge meaning and target population before accepting this default. Turning off a transformation also requires checking that the selected algorithm supports the resulting graph. Component-wise analysis or preserving excluded nodes in a separate accounting table may be appropriate for the decision.

## Label Purity and Held-Out Prediction

The [pinned `max_acc` implementation](reference/metrics/structural.py) first finds the majority label of each group using all node labels. Its `all` output is the best possible accuracy of a classifier constrained to predict one constant label per group on those same nodes. This is an oracle diagnostic of information lost by the partition. It is not accuracy from training a classifier and evaluating new outcomes.

The implementation then evaluates that same all-node majority on each supplied mask. It does not recompute a separate optimal constant within each mask. Consequently, `test` and `masked` are scores of the global-majority assignment and need not be upper bounds for the corresponding subsets. In a group with labels $(0,0,1)$, the global majority is 0. If the last node is the test subset, the function's assignment scores zero there, while the subset's best constant scores one. If the last node is instead the sole training node, a training-only majority predicts 1 and scores zero on the first two nodes; the all-label majority scores one on those two nodes. [Original checks](source_checks.py).

Aggregate purity can also conceal a small class's errors. Two groups containing three class-0 customers and one class-1 customer each have aggregate majority accuracy of 75%, with zero recall for class 1. This is an invented arithmetic illustration. It motivates reporting customer-group outcomes and selecting a loss function that reflects the decision.

## Outcomes Can Enter Before Model Fitting

The default `alpha=None` in [UGC](reference/algorithms/ugc.py) calculates its feature-versus-structure weight from the fraction of edges connecting different labels. The function reads `data.y` at both endpoints across all edges, including test-node labels. Its docstring states this choice explicitly. On a three-node path, changing only the last node's held-out label from 0 to 1 changes this fraction from zero to one-half when the other labels are zero. Preprocessing can therefore depend on the very outcomes later used for evaluation.

For a predictive exercise, choose a fixed alpha in advance or tune it using only the permitted training and validation information. Retain an untouched final evaluation sample. Access to test-node features in a transductive design is a separate choice from access to test-node outcomes.

[STPGC](reference/algorithms/stpgc.py) also has explicit label-guidance settings. Its default uses training and validation labels; `train_only` narrows the available information, and `label_guide=False` removes label guidance. The [cross-scoring script](reference/reproduce/cross_scoring.py) explicitly disables STPGC's guidance. Its imported extra arguments do not override UGC's alpha default. The benchmark should therefore be read with each method's information set visible, rather than treating every row as label-free.

These code paths are particularly useful for AI-assisted coding. A generated workflow can execute without an exception while evaluating an oracle label assignment or allowing outcomes to affect preprocessing. Students can trace inputs, transformations, and output definitions, then write a small independent counterexample before trusting an interpretation.

## Figure Descriptions and Reading Scope

Figure 1 on PDF page 11 shows an original 500-node stochastic-block graph with three communities and the coarsened graph from each method at requested reduction 0.70. Colors indicate community composition; node area increases with the number of original members. Some methods produce balanced groups, some concentrate large groups in one community, and others mix community labels. Four methods are tuned for this synthetic graph, as indicated in the caption. The panels display different achieved node counts. The image supports comparison of aggregation patterns under those inputs.

Table 4 on PDF page 25 lists four metrics and the achieved ratio for Cora and PubMed. Its ranking depends on the metric, and its reported failures remain part of the comparison. Both pages were inspected visually. The review covers the main construction and evaluation in §§1–5, Appendix B.4–B.5, the preprocessing discussion in Appendix D, and the selected implementation paths cited above. Other appendix derivations and all upstream algorithms have not been independently verified.

The original Python checks execute exact small calculations and comparisons of selected reported table entries. They do not execute GraCo, reproduce the benchmark, or establish performance on course datasets. The repository snapshot contains selected reference files; the full repository and its dependencies would be needed for an optional advanced implementation.
