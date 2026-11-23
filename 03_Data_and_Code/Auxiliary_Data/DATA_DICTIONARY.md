# Auxiliary Data Definitions

## Observation Unit and Population

The model's observation unit is one independent response at one of four product profiles from a primary or auxiliary source. The programs calculate analytic conditional means and estimation moments. Files contain no observed people, generated personas, individual responses, geographic sample, or time series. The fixed population and source behavior are imposed for the example.

The four profiles cross feature `f` and price `p`, each coded -1 and +1. Feature -1 denotes standard and +1 premium; price -1 denotes low and +1 high. A contrast between levels spans two coded units. Mean responses and coefficients are measured in rating points. Price coefficients are per coded unit, with no monetary price difference supplied. The Gaussian response model is a stylized continuous score with no imposed rating bounds.

## Input Parameters

| Key | Meaning and Default |
|---|---|
| `primary_coefficients` | Intercept, feature, and price coefficients: 3, 0.4, -0.5. |
| `auxiliary_bias_coefficients` | Additional auxiliary intercept and price coefficients: 0.8, 0.6. |
| `primary_variance`, `auxiliary_variance` | Independent response-error variance in squared rating points; each equals 1. |
| `primary_cost`, `auxiliary_cost` | Cost per response in normalized budget units: 1 and 0.01. |
| `mse_target` | Maximum expected sum of squared errors for the three primary coefficients: 0.01. |
| `omitted_feature_bias` | Additional auxiliary coefficient on the premium-feature code, excluded from the fitted bias dictionary: 0.3. |
| `sample_multipliers` | Factors multiplying both rounded source counts together: 1, 2, 4, 8, 16, 32. |

The bias coefficients are unknown to the modeled estimator; their numerical values specify the invented mean functions. The model assumes known feature dictionaries, independent Gaussian errors, known source variances, and constant source-specific response costs. There is no training/test split in an analytic calculation. A prospective empirical evaluation requires separate human respondents and concepts suited to the intended claim.

## Output Tables

`profile_means.csv` contains one row per feature-price profile, with primary and auxiliary analytic means. `allocation.json` records counts in total and per profile, total source precisions, coefficient variances, total MSE, costs, and the fractional savings relative to optimized primary-only sampling. Each source count is rounded up separately at each profile. The finite rounded allocation is feasible and need not be the exact integer optimum.

`value_curve.csv` contains the relative information cost `lambda = auxiliary_cost * auxiliary_variance / (primary_cost * primary_variance)` and asymptotic savings. The row at zero is flagged `limiting_value=True`; it denotes a limit as positive costs approach zero. The second savings series allows unrestricted bias on all three primary features and is zero. This curve applies to the balanced four-profile model and total coefficient loss.

`bias_sensitivity.csv` contains one row per sample multiplier. `total_coefficient_variance` sums the three coefficient variances, `squared_bias` is the squared expected error in the feature coefficient, and `omitted_bias_mse` adds those quantities. `correct_model_mse` retains the restricted bias model with zero omitted feature bias. `bias_summary.json` also records the expanded correctly specified dictionary, under which auxiliary information about the primary coefficient vector is zero. The two cases represent different fitted models.

No sample exclusions, imputations, joins, customer weights, or resampling occur. The analytical calculations use all four profiles with balanced counts within each source. Dependence across respondents or sources changes the information calculation and is outside these results.
