# Heterogeneity Reanalysis Results

All empirical tables use the released panel documented in [the data dictionary](../DATA_DICTIONARY.md). The decomposition and error-rate tables contain constructed comparisons.

| File | Content |
| --- | --- |
| `account_estimates.csv` | One row per account: observation count, conditional OLS slope, working-model SE, and conditional empirical-Bayes summaries |
| `model_comparison.csv` | Marginal log likelihood, BIC, equal-account mean coefficient, and optimization status for each integration model |
| `mixture_parameters.csv` | Weights, means, and standard deviations of the fitted mixing distribution |
| `density_grid.csv` | Fitted coefficient densities on a common slope grid |
| `observational_equivalence.csv` | Imposed mechanism shifts with unchanged observed likelihood and changed latent interpretation |
| `equivalent_state_errors.csv` | Exact missed-harm rates under constructed observational equivalence; no empirical enforcement-rate estimate |
| `summary.json` | Sample, restrictions, working uncertainty assumptions, and interpretation |

Price coefficients are dimensionless log-sales/log-price associations. The imposed restriction uses the same coefficient scale. BIC penalizes two parameters for the one-component model and five for the two-component model, using 88 accounts as the likelihood sample size. These are in-sample fit comparisons without a forecast-validation claim.

## Synthetic Precision Comparison

`precision_detection_scenarios.csv` has four pooling weights; `precision_detection_curve.csv` has 101 points; `precision_detection_setup.json` states every input. All consumers and harms are synthetic and separate from the retail reanalysis. Precision is inverse posterior variance, MSE averages repeated-sample squared errors, and detection conditions on the harmed subgroup. False flags condition on harmless groups. `harm_precision_elasticity` is the local percentage change in missed-harm loss for a one-percent change in reported precision under the fixed posterior rule. The final column holds actual false-positive rates equal to five percent as a calibration check.
