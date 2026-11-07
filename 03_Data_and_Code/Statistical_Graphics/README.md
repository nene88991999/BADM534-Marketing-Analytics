# Statistical Graphics for Marketing Decisions

Two original synthetic examples connect chart choice to customer comparisons and decisions. [PyStatlas by Thierry Warin](https://warint.github.io/pystatlas/) motivates the paired-comparison and calibration displays. The inputs and programs here are original course constructions; no upstream program or source dataset is required.

## Run

Python 3.10 or later and SciPy are required for the paired t critical value. The calibration program uses only the standard library. Tested November 7, 2026 with Python 3.13.5 and SciPy 1.15.3. No network calls or model APIs are used.

```bash
python paired_changes.py
python ranking_calibration.py
python -m unittest -v test_examples.py
```

Run from this folder or supply the full script path; input paths are resolved relative to the script. The two analysis commands overwrite their own files in `results/`.

## Inputs and Interpretation

| File | Unit and Variables | Population and Construction |
| --- | --- | --- |
| `inputs/paired_spending.csv` | One customer; `customer_id`, `before_dollars`, `after_dollars` | Eight imposed customers observed in two one-month windows. No missing pairs. Monetary values are dollars per customer per month. |
| `inputs/purchase_predictions.csv` | One customer; `customer_id`, `score_group`, binary `purchase`, probabilities `model_a` and `model_b` | Eighty imposed eligible customers, including 44 nonbuyers. Four score groups of 20 have 2, 6, 12, and 16 purchases during one next-month horizon. Each customer can purchase at most once. |

All rows and predictions are synthetic. Customer IDs identify only constructed records. Input ordering is deterministic; no random seed is needed. Model A scores are 0.1, 0.3, 0.6, 0.8 and Model B scores are 0.01, 0.1, 0.9, 0.99 in ascending groups. No model is fitted and no training or test sample is claimed.

The paired example targets the mean of customer-level changes. Its t interval describes a hypothetical sampling model with independent normally distributed customer differences. The eight imposed rows are not evidence of a campaign's causal effect. The independent standard error is a deliberately inapplicable comparison that drops the within-customer covariance.

The prediction example calculates empirical AUC from every positive-negative pair, assigning half credit to ties. Its Brier score averages squared probability errors over all 80 customers. Probability sums forecast the number of purchasers in this fixed cohort. Perfect group calibration of Model A is imposed, so it provides no evidence about future calibration.

## Outputs and Checks

`results/paired_changes.json` reports a $5 mean change, standard error 0.267261, and conditional 95% t interval [4.368028, 5.631972]. `results/customer_changes.csv` contains the eight plotted differences. `results/ranking_calibration.json` reports AUC 53/66 for both models, Brier scores 0.175 and 0.21855, and purchase forecasts of 36 and 40 against 36 observed. `results/calibration_bins.csv` supplies every plotted probability and observed share with its denominator.

Six tests independently check difference variance, pairing, row-order invariance, exact AUC arithmetic, probability losses, aggregate counts, and invalid input handling. Both programs were executed. Full matching Python appears in [M2 §2.22](../../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md) and [M7 §7.23](../../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md); editable figures and projected examples appear in Sessions 3 and 11.
