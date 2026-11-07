# Source Review and Interpretation

Source: Thierry Warin, [PyStatlas](https://warint.github.io/pystatlas/), pinned [repository revision](https://github.com/warint/pystatlas/tree/ec4bb401e1c8a6622fa5da196e05c4df0b5e0b41). Checked November 7, 2026. The gallery search for “calibration” and its detail page were inspected in a browser. This check covers those interactions only.

## Selected Scripts Read in Full

| Source Example | Useful Mechanism | Course Interpretation |
| --- | --- | --- |
| [Within-Subjects Comparisons](https://warint.github.io/pystatlas/group-comparisons/within-subjects/) | Lines preserve repeated country observations; paired comparisons retain covariance. | Use customer identifiers for repeated spending. An unweighted average across countries is a country-level quantity. A before/after pattern needs a counterfactual design for causal interpretation. |
| [Estimation Plot](https://warint.github.io/pystatlas/group-comparisons/estimation-plot/) | Raw state outcomes sit beside a difference and a BCa bootstrap interval. | State the population to which sampling uncertainty refers. For repeated customers, resample whole pairs. The original comparison is observational. |
| [Predicted Probabilities](https://warint.github.io/pystatlas/regression-models/predicted-probabilities/) | A logistic model is translated into probabilities with one predictor varying and another held at its mean. | A prediction at mean covariates differs from an average of individual predictions. Display support and identify the conditioning values. |
| [Calibration Plot](https://warint.github.io/pystatlas/model-diagnostics/calibration-plot/) | A held-out sample compares observed shares with mean predictions, Wilson intervals, and the Brier score. | Quantile bins are constructed separately for each model and can contain different customers. Preserve bin counts and use an independent evaluation sample when fitting or recalibrating. |
| [Kaplan–Meier Curves](https://warint.github.io/pystatlas/survival/kaplan-meier/) | Censoring marks and numbers at risk expose the information supporting the survival curve. | Define churn and the time origin. Independent censoring, conditional on the relevant information, matters for a survival interpretation. Repeated spells may require dependence-aware uncertainty. |
| [Silhouette Plot](https://warint.github.io/pystatlas/multivariate/silhouette-clusters/) | Standardized inputs, silhouette widths, and a PCA display distinguish cluster fit from its projection. | The original excludes DC and selects k on the same sample. Assess sensitivity to exclusions, scaling, seeds, and new observations before labeling customer types. |
| [Precision–Recall](https://warint.github.io/pystatlas/machine-learning/precision-recall/) | Out-of-fold scores connect detection to the fraction of flagged cases that are positive. | The prevalence is the no-skill baseline. Thresholds need costs and capacity. The script marks the available threshold nearest 0.5; calculate the exact policy rule separately. |
| [Partial Dependence and ICE](https://warint.github.io/pystatlas/machine-learning/partial-dependence/) | Individual prediction curves reveal heterogeneity hidden by the average curve. | The plotted percentiles describe variation across curves, not uncertainty in an average. Varying correlated inputs can create unsupported combinations; prediction sensitivity alone does not identify an intervention effect. |
| [LISA Cluster Map](https://warint.github.io/pystatlas/spatial-data/lisa-cluster-map/) | Local spatial statistics depend on the neighborhood and permutation comparison. | The original explicitly reports unadjusted local tests. Discuss multiplicity, the weight matrix, and sensitivity before treating colored areas as reliable clusters. |

## Reproducibility

The source's build script executes chart programs to render figures. Requirements are minimum package versions, rather than a complete environment lock. The build also suppresses warnings. Course adaptations should record the actual environment and retain warnings that affect estimation or data interpretation. No dependency installation or upstream build was needed for this review.

Most examples load packaged data; the Guerry spatial examples use `libpysal.examples.load_example`, which can require a download or an existing cache. Record network requirements at the example level. The software license does not establish rights over the survey, administrative, or other underlying data. Source attribution in `data_sources.yaml` is the starting point for checking those terms.

## Transfer to Existing Course Data

For mHealth, the observation unit can be a user, a user-day, or a logged food entry. A display of entries gives more weight to frequent loggers. Preserve zero-log users when the target population is the cohort, and distinguish no observed entry from measured zero intake. A paired comparison should retain the same users and define comparable observation windows.

For McBroken, use the store-date panel and common observation windows. A change in the composition of observed stores can change an aggregate availability rate without a change within stores. Geographic association also depends on coverage and on the chosen distance or adjacency relation.

For earnings-call coding, assess agreement on the same passages or calls. Correlation between two coding scores can be high despite a systematic difference in levels. Distinguish disagreements in the unit of text, construct definition, and classification rule before interpreting the chart.

These are proposed extensions using existing course cases. The two newly executed programs use entirely synthetic inputs and do not re-estimate these datasets.
