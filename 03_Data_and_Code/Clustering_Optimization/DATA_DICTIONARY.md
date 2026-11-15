# Clustering Example Data Dictionary

## Observations and Units

Training and test rows are synthetic vectors. Their 32 coordinates are standardized with the training distribution. Row order is stable within a generated sample; a row index is not a customer identifier. There are no real customer attributes or outcomes. The number of generating components is eight and the fitted center count is 64.

## Output Fields

| File or Field | Definition |
| --- | --- |
| `centroid_checks.json` | Exact fractional results, four scalar observations, final centers, constructed saved labels, recomputed labels, and losses |
| `runs.csv` | One row per method, seed, and budget; 27 reference rows |
| `method` | `lloyd`, `minibatch`, or `emeans` |
| `budget` | Lloyd iteration cap, MiniBatch maximum passes setting, or e-means epochs; not equal arithmetic work |
| `fit_seconds` | Model construction and training after warm-up |
| `evaluation_seconds` | Common exhaustive final-center scoring of all training and test rows |
| `total_seconds` | Fit plus common evaluation; excludes preparation and file saving |
| `train_mse`, `test_mse` | Mean squared Euclidean distance per vector, summed across coordinates, to the nearest final center |
| `saved_label_rows` | Number of training rows with saved labels in the valid range 0–63 |
| `saved_label_disagreements` | Count whose valid saved label differs from the nearest final-center label |
| `saved_label_disagreement_rate` | Disagreements divided by valid saved-label rows |
| `summary.csv` | Coordinatewise medians across three seeds for each method and budget; median components need not add to median totals |
| `stability.csv` | Pairwise adjusted Rand agreement on all 10,000 fixed test vectors; label-number invariant |
| `metadata.json` | Generator parameters, data hashes, package versions, numerical thread count, timing boundary, and fitted recipes |

Each `<method>_<seed>_<budget>.npz` contains `centroids` (64 × 32), `saved_labels` (50,000), `train_labels` (50,000), and `test_labels` (10,000). The last two arrays use the common full-distance scorer. The original standardized vectors can be reconstructed with `make_data` and checked against the SHA-256 hashes of their float32 array bytes. Hash equality requires the recorded numerical environment and representation; elapsed times vary on reruns.
