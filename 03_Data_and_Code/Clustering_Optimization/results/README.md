# Reference Clustering Results

Executed November 15, 2026, using the settings in [metadata.json](metadata.json). All observations are synthetic. See [the design, commands, and interpretation](../README.md) and [field definitions](../DATA_DICTIONARY.md).

| Method | Budget | Fit (ms) | Evaluation (ms) | Test MSE | Changed Labels (%) |
| --- | ---: | ---: | ---: | ---: | ---: |
| Lloyd | 2 | 13.5 | 150.8 | 10.6496 | 0.000 |
| Lloyd | 5 | 24.0 | 141.1 | 10.5538 | 0.000 |
| Lloyd | 10 | 49.3 | 169.0 | 10.5264 | 0.000 |
| MiniBatch | 2 | 21.8 | 143.4 | 10.5693 | 0.000 |
| MiniBatch | 5 | 48.8 | 140.1 | 10.5530 | 0.000 |
| MiniBatch | 10 | 89.4 | 150.9 | 10.5448 | 0.000 |
| e-means | 2 | 32.0 | 152.0 | 10.5177 | 9.408 |
| e-means | 5 | 57.4 | 144.6 | 10.5030 | 2.384 |
| e-means | 10 | 114.4 | 159.4 | 10.4960 | 1.496 |

Medians use three seeds per row. The fixed data contain 50,000 training and 10,000 test vectors with 32 coordinates and 64 fitted centers. Timing is measured on one CPU thread; budget numbers have method-specific meanings. MSE averages the sum of squared coordinate differences over vectors. The common evaluation is reported separately from fitting. It includes all training and test assignments.

The scalar results give an exponentially weighted center of 17/6, compared with 9/2 from averaging means without cluster masses. For points 0, 4, 5, and 10 and final centers 2 and 7.5, one of four constructed saved labels changes. The mean squared distance falls from 93/16 to 41/8 when labels are reassigned.

Every run retains its final centroids and labels in a compressed NPZ file. The training and test vector hashes permit regeneration checks. The pairwise seed comparisons in [stability.csv](stability.csv) describe conditional partition agreement. No GPU experiment, customer intervention, or source-paper speedup is reproduced here.
