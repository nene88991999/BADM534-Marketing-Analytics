# Conformal Prediction Source Review

Reviewed November 8, 2026. Source: [Practical Guide to Applied Conformal Prediction code repository](https://github.com/PacktPublishing/Practical-Guide-to-Applied-Conformal-Prediction/tree/482612bf544898925fa6c32a218d401decf5df22), associated with Valery Manokhin's book. Commit `482612bf544898925fa6c32a218d401decf5df22` is dated March 2, 2026. This record supplies provenance; course prose and slides present the concepts directly without citing the book.

## Retrieval and Reading Scope

All ten notebooks, README, and LICENSE were downloaded at that commit and verified against Git blob identifiers and SHA-256 hashes. The cover image was excluded. Saved notebook outputs were retained in the local reference copy but omitted from code extraction. No upstream program, installation cell, external dataset download, or model call was executed.

The review examined all notebook heading summaries and read the principal binary-classification calculation, its calibration helper, regression splitting and absolute-residual calculations, selected time-series preparation and online-update cells, and selected imbalance and multiclass-calibration cells. It does not represent a complete reading of every cell or the book. Cell numbers below are zero-based positions in each notebook's `cells` array. The catalog distinguishes detailed and selected code inspection from heading-only inspection.

## Findings That Affect Adaptation

| Source | Inspection Finding | Course Treatment |
| --- | --- | --- |
| `Chapter_06.ipynb`, cells 45–52 | Candidate scores are appended before calling a helper that already adds the candidate's rank contribution. Both label calls use the class-zero augmented array; the later function also refers to that global array. | Use calibration scores alone and an explicit order-statistic implementation. Keep the score function fixed before calibration. |
| `Chapter_06.ipynb`, cell 63 | `assert (predictions_test_sets, prediction)` asserts the truth of a nonempty tuple, so it does not verify equality. | Enumerate an independent finite-rank example and check expected sets directly. |
| `Chapter_06.ipynb`, feature preparation | The bank-marketing example retains last-contact duration. Its availability depends on whether prediction occurs before or after that contact. | Define the forecast origin before choosing features; post-call duration is unavailable for a before-call targeting decision. |
| `Chapter_6_classifier_calibration.ipynb`, cell 5 | The ECE expression compares mean probabilities with bin centers and leaves observed event frequencies unused. Fixed-length bin weights can also disagree with the number of nonempty calibration-curve bins. | Retain M7 §7.23's independently verified reliability diagram and Brier calculation. Do not reuse this ECE helper. |
| `Chapter_07.ipynb`, cells 20–35 | The train/calibration/test separation and absolute-residual construction provide a useful introductory workflow. The finite-sample-adjusted NumPy quantile uses interpolation. | Select the kth ordered score explicitly and handle an unattainable rank with infinity. At admissible ranks, linear interpolation at k/n is at least the kth score; interpolation here is not itself evidence of undercoverage. |
| `Chapter_08_EnbPI.ipynb`, cell 7 | `df.sample(500)` reorders rows before a split with `shuffle=False`. The target is also divided by a maximum calculated before splitting. | A chronological split requires ordered observations and information available at the forecast origin. Derive any learned preprocessing from the appropriate earlier sample. |
| `Chapter_08_EnbPI.ipynb`, cells 26–27 | Pooled outcome inclusion is described as conditional coverage. Inclusion of point predictions is also displayed. | Evaluate actual outcomes, retain group and horizon denominators, and distinguish pooled coverage from conditional coverage. |
| `Chapter_08_EnbPI.ipynb`, cell 31 | Online updates use the preceding batch's targets before issuing the next batch's intervals. | Preserve the ordering principle and adapt it to the actual outcome delay. The source algorithm was not reproduced. |
| `Chapter_11.ipynb`, selected splitting and evaluation cells; `Chapter_12.ipynb`, introduction and headings | These examples include imbalance and probability-calibration methods. Their targets should remain distinct from prediction-set coverage. | Discuss calibration-sample composition and rare-label coverage; defer larger benchmark reproductions. |

## Primary Method and Software Checks

[Angelopoulos and Bates, A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification](https://arxiv.org/abs/2107.07511) supplies the rank argument, marginal-coverage interpretation, group-calibration extension, and infinite threshold at small sample sizes. Appendix D and Sections 4.1–4.2 were checked against the course's mathematical claims. The examples in the notes are newly constructed, with no reported results taken from the paper.

The [MAPIE v1 release notes](https://mapie.readthedocs.io/en/stable/content/getting-started/v1-release-notes/), checked November 8, 2026, replace the older `MapieRegressor` and `MapieClassifier` interfaces with separate split and cross-conformal classes. Split workflows distinguish fitting, conformalization, and prediction; `confidence_level` replaces `alpha` with the complementary value. A generated implementation must specify the installed version and consult its corresponding documentation. The course programs avoid this version dependency by using the standard library.

## Execution and Interpretation

Only the [original course programs](../../03_Data_and_Code/Conformal_Prediction/README.md) were executed. Six tests check finite-rank enumeration, small samples and ties, invalid inputs, exact segment counts and widths, paired demand changes, and classification sets. The fixed synthetic populations illustrate mechanisms. Their realized coverage does not empirically establish exchangeability, fairness, customer benefit, or performance on mHealth, McBroken, or earnings calls.
