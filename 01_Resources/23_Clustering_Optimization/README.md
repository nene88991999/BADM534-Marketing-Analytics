# Clustering Optimization, Evidence, and Customer Decisions

A large collection of product, review, or content vectors can make repeated clustering costly. Faster optimization can make more comparisons feasible, while the representation and the proposed marketing action still require substantive justification. [M4 §§4.18–4.20](../../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md) connect these questions to complete Python, two editable figures, and an [optional Session 6 activity](../../07_Labs/Clustering_Optimization/README.md).

## Sources and Reading Scope

| Source | Contribution and Course Use | Version and Access |
| --- | --- | --- |
| [Bessa, Mazaré, Szilvasy, Touvron, Picard, Douze, and Jégou, e-means](https://arxiv.org/abs/2611.09501) | Exponentially weighted cluster sums and counts, schedules, empty-cluster handling, and matched-error comparisons. Read the method, experimental protocol, scaling limits, and final assignment discussion. | [Downloaded paper](local_sources/Bessa_Mazare_Szilvasy_Touvron_Picard_Douze_Jegou_WorkingPaper2026.pdf), v1, November 6, 2026; CC BY 4.0 |
| [Official Faiss implementation](https://github.com/facebookresearch/faiss/tree/ebab8f784c1d177129602269d5ad966c525fbdcb/contrib/e_means) | CPU and GPU interfaces, automatic recipes, and distinction between returned labels and assignment to final centers | [Pinned README](local_sources/e_means_README.md), November 14 commit; MIT |
| [o-means implementation and benchmark](https://github.com/owlgebra-ai/faiss/tree/9ecbf0c2a2f4ca7a771b552badc145584b09e1a6/contrib/o_means) | Two-level approximate assignment, closing mean, exact evaluation, and implementation costs | [Pinned README](local_sources/o_means_README.md), November 13 commit; MIT; advanced reading |
| [e-means interactive playground](https://e-means.github.io/playground.html) | Visual exploration of moving centers, batches, and initialization | Linked resource; simplified two-dimensional demonstration |
| [KMeans](https://scikit-learn.org/1.6/modules/generated/sklearn.cluster.KMeans.html) and [MiniBatchKMeans](https://scikit-learn.org/1.6/modules/generated/sklearn.cluster.MiniBatchKMeans.html) | Initialization, termination, and final labels in the baseline implementations | Documentation for the executed scikit-learn 1.6.1 environment |

The source review was prompted by [Chandan Kumar Singh's public post](https://www.linkedin.com/posts/csingh03_machinelearning-clustering-kmeans-share-7527643748571373568-c5p4/). Its animation is a simplified illustration. Numerical claims are assessed against the original paper and implementation records. [catalog.json](catalog.json) preserves exact versions, rights, URLs, and file hashes; [the MIT notice](local_sources/FAISS_LICENSE.txt) accompanies the redistributed repository documentation. Relative links within the preserved READMEs refer to their original upstream repository trees.

## Methodological Lessons

e-means updates exponentially weighted sums and counts for each cluster. Their ratio preserves the contribution of cluster mass when batches contain different numbers of assigned observations. The training stream is shuffled static data; greater weight on a recent training batch is not an empirical claim that recent customers deserve greater weight. A cooling step schedule, unused-cluster handling, and implementation choices contribute to the complete algorithm.

Labels recorded while centers move can disagree with the nearest final center. Customer profiles therefore require an explicit final assignment. The course's constructed four-point comparison makes the inconsistency visible, and its executed CPU benchmark measures the discrepancy for the installed implementation.

o-means uses approximate assignment to reduce search cost at large K. Its reported geometric-mean improvement uses interpolation to compare the same error across selected budgets. Search approximations can lose accuracy, and hardware kernels contribute to the observed speed differences. The repository describes failure cases and a limited benefit at small K. e-means also studies approximate search at extreme scale; approximation is not unique to the fork. The upstream o-means pull request was open on November 15, 2026. Recheck integration before using a later installation.

## Course Comparison and Scope

The [executed CPU example](../../03_Data_and_Code/Clustering_Optimization/README.md) fixes the generated observations, feature scale, initial centers, test set, and exact final scorer. It compares 27 fits across three seeds and three caps. On these data e-means produces lower held-out error at each cap and takes longer than Lloyd at the same cap. Its results support discussion of cost, stopping rules, and final labels. They establish no general speed ranking and do not reproduce the sources' GPU benchmarks.

mHealth provides a distinct business comparison: three clusters based on earlier logging features, followed by later observed logging. A smaller clustering objective can improve numerical approximation without changing which service action is useful. Customer response needs experimental or otherwise credible causal evidence. Informed choice and treatment of persons remain separate criteria in Marketing Dialectics.

## Future Wiki Interaction

An original static-HTML demonstration could hold four points fixed while students move two centers, display saved and recomputed labels, and recalculate both losses. A second control could change batch mass while preserving batch means. State the sample, formula, and inputs beside each control and supply a keyboard-operable table. Use the Illinois palette plus shapes and labels. Preserve the Python calculation as an independent reference. The external animation's timing and simplified dynamics should not be used as performance evidence.
