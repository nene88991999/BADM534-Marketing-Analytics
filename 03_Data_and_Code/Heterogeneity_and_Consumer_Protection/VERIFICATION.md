# Verification Record

Checked November 27, 2026.

## Released Data

The three upstream files were downloaded again from commit `453ae30857cf09a0c537f4deab64ed193493c8c9` and matched the SHA-256 hashes in `PROVENANCE.json`. Base R 4.5.3 loads the original object and exports all 5,555 rows, four columns, and 88 account labels without reordering. Upstream documentation and GPL terms are retained. The 77-account preprint and 88-account package differ; published-table replication is not claimed.

## Numerical Execution

Commands from the course root:

```sh
python3 03_Data_and_Code/Heterogeneity_and_Consumer_Protection/heterogeneity_reanalysis.py
python3 03_Data_and_Code/Heterogeneity_and_Consumer_Protection/test_reanalysis.py
python3 03_Data_and_Code/Heterogeneity_and_Consumer_Protection/harm_elasticity.py
```

The reanalysis passed seven independent tests: sample preservation, residualized account slopes, quadrature against exact marginal integration, mixture-label invariance, observation-wise mechanism equivalence, preservation of the BIC result, and the equivalent-state error identity. Eleven optimization starts converged. BIC favors the simpler distribution; the richer fit is not selected by that criterion.

The precision program verifies risks by quadrature, detection by tail integration, elasticity by finite differences, opposing group and population risks, and the matched-false-positive calibration. It computes the reported results exactly from imposed normal distributions without Monte Carlo error. Its normal working prior approximates a synthetic two-point population. Conditional posterior precision is distinct from repeated-sample subgroup coverage.

## Interpretation

The empirical coefficients are conditional associations. Gaussian independent errors, fixed first-stage standard errors, and fitted hyperparameters constrain uncertainty. The mechanism shift is constructed. The separate precision example changes pooling and a posterior decision rule; no actual bias, consumer injury, or enforcement effect is estimated from the retail observations. A lower threshold for proportionate protection is a philosophical application with factual and institutional premises, not a prescription attributed to a statistical theorem or a particular legal holding.

## Method Correspondence

The [method crosswalk](METHOD_CROSSWALK.md) traces the hierarchical loop to `runiregG`, derives the matrix posterior, and verifies the scalar conditional identity numerically. Source files and hashes are retained; no upstream sampler was executed. The known-harm example changes this conditional update and the associated decision threshold, with full hyperparameter uncertainty outside its scope.

## Course Integration

The complete notes, standalone Marketing Dialectics chapter, and Sessions 6 and 14 were rebuilt. Forty-five changed or adjacent PDF pages were rendered and visually inspected. Each page of the two revised decks matches its counterpart in the combined deck. The three new TikZ figures retain editable source; all 202 coordinates in the precision and detection plots match their saved result table. All 133 Python source blocks in the course notes match the corresponding scripts and pass syntax checks.
