# Bad Controls and Project Exposure

Three original programs distinguish causal adjustment, treatment-affected covariates, and the selection of comparison populations. All observations and parameter values are synthetic. The exercises contain no household records and no replication of the electricity paper's estimates.

## Run

Python 3.10 or later and NumPy are required for the first two programs. The third uses the standard library. No network or API access is used.

```sh
python3 control_paths.py
python3 panel_covariates.py
python3 project_pipeline.py
```

Run from this folder, or prefix the commands with `03_Data_and_Code/Bad_Controls/` from the repository root. Outputs are saved beside the scripts under `results/`. Full matching code appears in M3 §3.21 and M6 §§6.40.2 and 6.42.2.

## Inputs and Outputs

| Program | Population and Question | Expected Result |
| --- | --- | --- |
| [control_paths.py](control_paths.py) | Five imposed causal structures, each with 16 equally weighted shock combinations | A total slope of 7 becomes 1 after mediator adjustment; a collider changes 0 to −1; an instrument-like control changes 13/11 to 2 |
| [panel_covariates.py](panel_covariates.py) | Sixteen weighted population cells; the true ATT is 4 outcome units | Exclusion gives 5.5, observed post-treatment adjustment −2, valid baseline adjustment and linear imputation 4 |
| [project_pipeline.py](project_pipeline.py) | Four utilities over three synthetic dates; all prices in dollars/MWh | Earlier unexposed comparison 10, mixed-donor comparison 7, opening-period comparison 4 |

The panel exercise enumerates a finite probability distribution. Cell weights are population masses, not sample weights estimated from a survey. No standard errors or p-values are calculated. Its simple imputation works because the imposed conditional outcome trend is linear and the required baseline variable is observed. A nonlinear response generally requires integration over the untreated covariate distribution, rather than substitution of its mean.

The project sensitivity file varies canceled-donor cost increments and weights. The population file compares the average imposed effect across three proposals with the effect among the one completed project. Different populations need not have the same effect; the exercise identifies the error in treating one average as if it answered the other question.

## Provenance and Interpretation

The [reading collection](../../01_Resources/44_Bad_Controls_and_Project_Exposure/README.md) supplies the methodological foundation. These constructions are original teaching examples. The panel program is inspired by the identification distinction in Caetano, Callaway, Payne, and Sant’Anna (2026); it does not implement their general doubly robust estimator or validate their R package.

See the [data dictionary](DATA_DICTIONARY.md), [verification record](VERIFICATION.md), [output companion](results/README.md), and [optional practice](../../07_Labs/Bad_Controls/README.md).
