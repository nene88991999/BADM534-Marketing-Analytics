# Agent Guide for Clustering Optimization

Read the root agent guide, this folder's README, and DATA_DICTIONARY.md. Preserve the distinction between the exact scalar example, the executed synthetic CPU comparison, and author-reported GPU benchmarks.

- Use final-centroid assignments when forming segment profiles. Report the saved-label comparison and its denominator separately.
- Hold observations, train/test split, feature transformations, K, initial centers, and scorer fixed within an algorithm comparison. Fit transformations only on training data.
- State timing boundaries, hardware, precision, initialization, package versions, thread count, and stopping rules. Equal budget labels do not imply equal computation. Report unsuccessful comparisons as well as favorable ones.
- Use `--output local_runs` for exploratory reruns. Do not overwrite the reference results or edit their numbers without executing and reconciling the changed calculation.
- Preserve complete matching Python blocks in M4 §§4.18–4.20. Run `scripts/check_lecture_code.py` after editing them.
- e-means and o-means optimize squared Euclidean distance. Neither is a direct replacement for the Jaccard mechanism clustering or the affiliation-network community analysis.
- Initialization agreement, lower dispersion, and faster fitting do not establish segment meaning, causal response, or ethical permission. Connect any customer action to independent evidence and the Marketing Dialectics framework.
- Do not claim o-means, GPU code, the interactive playground, or source-paper experiments were run. The verified example uses CPU Faiss e-means. No data are sent to external AI services.
