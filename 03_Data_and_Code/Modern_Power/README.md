# Power, Equivalence, and Harm Bounds

The electricity-price case asks whether an insignificant coefficient supports reassurance about household costs. These calculations compare zero-null power with tests of specified positive margins and two forms of scalar equivalence. A separate sensitivity calculation allows a bounded bias.

## Inputs and Interpretation

The inputs are rounded coefficients and utility-clustered SEs from the course's [unchanged 42-page source](../../01_Resources/41_Statistical_Claims_and_Decisions/RanaKapsNetessine_WorkingPaper2026.pdf) (Rana et al., 2026):

| Case | Coefficient and SE | Source | Units and Targets |
| --- | --- | --- | --- |
| Residential reference | 0.261 and 0.158, both scaled by 100(456/6804) | Table 2, column 4, p. 23 | USD/MWh at a 6.702-point reference exposure; targets 1, 2, 3 |
| Four-owner slope | 0.158 and 0.160 | Table 4, column 4, p. 26 | USD/MWh per exposure percentage point; targets 0.1, 0.2, 0.3 |

The price samples contain 41 treated utilities and 627 post-anchor observations. No utility records are reconstructed. The reference exposure is a ratio of reported means. The subgroup slope is not multiplied by that overall ratio. Price margins are illustrative rather than validated tolerances or originally prespecified tests.

All sampling calculations use a fixed Gaussian approximation with the reported clustered SE. The source study's positive findings remain part of the interpretation. No observed-power calculation substitutes the estimated coefficient for an assumed true effect. No additional clustering multiplier is imposed.

## Reproduction

Python 3 and SciPy are required. NumPy supports independent verification. Verified locally with Python 3.13.5, SciPy 1.15.3, and NumPy 2.1.3.

```sh
python3 03_Data_and_Code/Modern_Power/harm_bounds.py
python3 03_Data_and_Code/Modern_Power/verify_harm_bounds.py
python3 03_Data_and_Code/Modern_Power/build_figure.py
```

The program writes [results.json](results.json). The figure builder writes the editable TikZ source used in M6. No seed, network call, downloaded code, or participant microdata is used. Complete source appears in M6 §6.51.

## Output Fields

`cases` retains the estimate, SE, units, source cell, p-value against zero, and one-sided 95% upper bound. Each `comparisons` entry contains the chosen margin, zero-null power at that margin, the one-sided margin-test p-value, TOST and folded-normal p-values and decisions, and the folded-normal critical value. `bounded_bias` records imposed bias allowances and their resulting upper bounds, in USD/MWh. These allowances are sensitivity inputs, with no estimate of actual bias or full HonestDiD implementation.

All six displayed price margins fail the three margin tests. The result concerns these price comparisons and their assumptions. It does not establish that every valid method must fail at every possible margin.

Verification uses numerical quadrature, SciPy's independent folded-normal distribution implementation, boundary-size checks, unit rescaling, interval/test duality, and an informative synthetic case that must establish equivalence. These checks validate the probability calculations, not the original identifying design. Read the [modern-method guide](../../01_Resources/51_Modern_Power_and_Harm_Bounds/README.md) for methods requiring additional data and the [optional exercise](../../07_Labs/Statistical_Inference/README.md#modern-power-and-harm-bounds) for the interpretation task.
