# Clustering Optimization and Customer Segments

A marketing team grouping many content vectors needs to balance computational cost with the quality of its representation. A team choosing customer support also needs evidence that its proposed actions help customers. These are separate comparisons. The examples support [M4 §§4.18–4.20](../../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md) and the [Session 6 extension](../../05_Slides/S06_Segmentation_and_Customer_Lifetime_Value.md).

## Inputs and Design

All observations are synthetic. `centroid_checks.py` uses exact fractions for two scalar examples. `compare_clustering.py` generates 50,000 training vectors and 10,000 independent test vectors, each with 32 coordinates, from eight Gaussian components. Component probabilities are 0.40, 0.20, 0.12, 0.10, 0.08, 0.05, 0.03, and 0.02. The means are drawn once from a normal distribution with standard deviation 1.5; independent coordinate noise has standard deviation 0.8. The data seed is 20261115. Each coordinate is standardized using training means and population standard deviations. No row is excluded. The fixed 64-center approximation deliberately differs from the eight generating components.

Three seeds (11, 23, 37) and three budget settings (2, 5, 10) give 27 fits. Each seed supplies common initial centers to all methods and settings. Lloyd and MiniBatch use scikit-learn 1.6.1, one initialization, and zero tolerance. MiniBatch also disables its lack-of-improvement stopping rule and uses batches of 256. e-means uses `NumpyEmeans` from Faiss 1.16.0 with its automatic recipe. The implementations can perform different amounts of work at the same budget number. `metadata.json` records actual iteration counts and e-means recipes, including its changing batch size.

## Run

The scalar calculation needs only Python's standard library:

```sh
cd 03_Data_and_Code/Clustering_Optimization
python3 centroid_checks.py
```

The CPU comparison requires an environment compatible with the pinned packages. It was executed on macOS ARM64 with Python 3.13.5. Wheel availability depends on the operating system and Python version; Faiss 1.16.0's tested macOS ARM64 wheel requires macOS 15 or later. No GPU, model account, or customer data upload is needed. Use an isolated environment with Python 3.13; substitute its installed interpreter path if `python3.13` is unavailable:

```sh
python3.13 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m unittest -v test_examples.py
.venv/bin/python compare_clustering.py --output local_runs
```

The committed `results/` files retain the verified reference run. Use `--output local_runs` to preserve them. If the packages are unavailable on a computer, the exact scalar example and saved results support the interpretation exercise without a new benchmark. Read [the data dictionary](DATA_DICTIONARY.md) before comparing outputs.

## Scoring and Timing

Each fitted centroid array is scored by the same direct float64 distance calculation. Test MSE is the average squared Euclidean distance per vector, summed across 32 standardized coordinates. The scorer searches every center. The script separately counts disagreement between valid saved training labels and assignments recomputed at the final centers. All 50,000 saved labels are valid in every reference run. Saved e-means labels can reflect earlier centers encountered during the final pass.

Each implementation is warmed up once. Training order is randomized within a seed and budget. Faiss and the numerical libraries use one thread. Fit time includes model construction and training; the common final-center calculation is recorded separately for both training and test vectors. Imports, data generation, standardization, saving files, and stability calculations are excluded. These short timings depend on the machine and implementation. The median across three seeds is a descriptive comparison, not a confidence interval or a matched-error speedup estimate. Internal bookkeeping, including final labeling, differs across implementations.

## Reference Results

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

Each entry is the median of three fits on the same data. e-means has lower held-out MSE at all three displayed caps and takes longer to fit than Lloyd at each corresponding cap. At budget 2, its median saved-label disagreement is 9.408%. The common evaluation takes longer than training in these runs, making the timing boundary consequential. These results do not reproduce the source papers' GPU comparisons.

`stability.csv` compares every pair of seed-specific partitions on the same test vectors using adjusted Rand agreement. This is sensitivity to initialization, conditional on fixed data, K, features, and implementation. It does not measure customer welfare, uncertainty about the population, or treatment effects. The mHealth application retains its earlier-window features, three clusters, and later logging comparison; the numerical benchmark does not relabel its users.

## Files and Verification

`centroid_checks.py` and `compare_clustering.py` appear in full in the lecture notes. Five tests check weighted centroid arithmetic, reassignment, a hand-computed distance, invariance to label permutation, and training-only standardization. The reference outputs include every final centroid array and label vector, training/test data hashes, aggregate tables, and execution metadata. [verification.json](verification.json) records the additional independent reconciliation and file hashes.

The resource collection preserves [the original research, implementation versions, and licenses](../../01_Resources/23_Clustering_Optimization/README.md). o-means is an advanced reading and was not executed. The comparison uses the published CPU e-means implementation rather than a simplified animation.
