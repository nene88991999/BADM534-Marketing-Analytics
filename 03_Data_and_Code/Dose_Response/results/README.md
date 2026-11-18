# Reference Results

These files reproduce the November 18, 2026 synthetic discount examples using Python 3.13.5 and NumPy 2.1.3. They contain no observed customer records. The [data dictionary](../DATA_DICTIONARY.md) defines every table and denominator.

`summary.json` summarizes four nuisance-model specifications over 200 independent samples and separately records one reference sample, overlap comparisons, and an exact hidden-confounder calculation. Conditional interval coverage is evaluated against known curves. The resulting bands have no validated 95% simultaneous-coverage guarantee.

`pooling_summary.json` compares 20 stores on one randomized synthetic dataset. `pooling_cv.csv` retains all nine candidate penalty pairs. `objectives_summary.json` reports grid maxima under three specified decision objectives. The [verification record](../verification.json) reconciles these summaries with their saved arrays.

Run the three programs with `--output local_runs` from the parent directory to preserve this reference version. The full equations, programs, and interpretation appear in M6 §§6.22–6.27 and M8 §8.22.
