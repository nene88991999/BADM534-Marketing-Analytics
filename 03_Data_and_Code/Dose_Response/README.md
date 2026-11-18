# Discount Response Curves and Marketing Decisions

A retailer choosing a discount needs a credible comparison of profit at different intensities. These original synthetic examples connect [M6 §§6.22–6.27](../../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md), [M8 §8.22](../../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md), and [M9 §9.18.1](../../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md). [Optional ungraded practice](../../07_Labs/Dose_Response/README.md) uses the same programs and saved results.

## Inputs and Units

Every observation and response function is synthetic. `dose_response.py` generates 2,400 customers, half of each observed type, with one promotion-week observation per customer. Discount is measured in percentage points on (0,40); 20 means 20 percent. Profit is dollars per eligible customer. Eligibility precedes the offer, all rows are retained, and no missing values are imposed. The target population gives each type weight one-half. Its known causal curve is `10 + 0.4*a - 0.01*a*a`.

The dose's logit transform equals `0.9*type + normal_noise`, with noise standard deviation 0.9. Profit adds `2*type` and independent standard-normal noise to the causal curve. The correct outcome specification includes type and a quadratic in dose. The correct conditional density fits a normal regression of the transformed dose on type and includes the Jacobian. Each wrong specification omits type. Five folds keep each observation's outcome out of its own nuisance training. A local linear Gaussian smoother uses a fixed two-percentage-point bandwidth and a 6–34 grid with one-percentage-point spacing. These models expose the calculation; no upstream estimator package is installed or executed.

`store_pooling.py` generates 2,188 customers across 20 stores in four regions. Every region contains stores with 12, 25, 60, 150, and 300 customers. Independently randomized discounts range from 5 to 35. A quadratic response has regional and store coefficient deviations and independent noise with standard deviation $3. Five folds within each store select regional and store ridge penalties from {1,10,100} using equal-store validation MSE. The fitted loss weights customer rows equally. Final evaluation gives each store and each grid point equal weight. This is a separate randomized example, isolating pooling from confounding.

`decision_objectives.py` compares revenue, profit, and profit subject to an imposed complaint cap. All functions are known assumptions. The complaint response and its 3% limit are hypothetical and establish no ethical or legal threshold. See [the data dictionary](DATA_DICTIONARY.md) for outputs and denominators.

## Run

The reference run used Python 3.13.5 and NumPy 2.1.3. No account, network request, or model API is needed. From this directory:

```sh
python3.13 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m unittest -v test_examples.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 .venv/bin/python dose_response.py --output local_runs --repetitions 200
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 .venv/bin/python store_pooling.py --output local_runs
.venv/bin/python decision_objectives.py --output local_runs
```

Use an installed compatible Python interpreter if `python3.13` has another path. The committed `results/` directory preserves the reference run. `--output local_runs` avoids replacing it. The main seed is 20261118; repeated samples use 10000–10199; pooling uses 20261119. Full source for all three analyses appears directly in the lecture notes.

## Results and Interpretation

Across 200 simulated samples, mean curve RMSE is $0.099 with both models correct, $0.058 with only the outcome model correct, $0.312 with only the density model correct, and $1.335 with both wrong. These are finite-sample errors over a fixed grid and bandwidth. The doubly robust population identity does not imply equal errors across the first three specifications or valid confidence intervals.

Conditional HC0 pointwise intervals hold estimated adjusted outcomes fixed and omit nuisance uncertainty and smoothing bias. With both models correct, mean pointwise coverage is 90.7%; whole-grid coverage of those pointwise intervals is 42.5%. Whole-grid coverage has no nominal 95% target for this procedure. `coverage.csv` reports each dose's coverage and Monte Carlo standard error across 200 independent datasets. Doses within a dataset are correlated.

In the reference weak-overlap sample, effective sample size is approximately the full 2,400 even though important dose-by-type combinations are almost absent. The largest weights can be missing from a finite sample. Conditional support requires separate assessment. The hidden-confounder calculation uses an exact observed regression and Bayes' rule; its bias is an identification failure even with perfectly known observable nuisance functions.

Partial pooling reduces equal-store curve RMSE to $0.512, compared with $0.936 for separate fits and $0.968 for a common fit. This result concerns one randomized synthetic dataset. Store 4 has lower error from its separate fit, illustrating the bias introduced by shrinkage. No pooling confidence intervals are supplied.

The imposed objective calculation selects 23.2% for revenue, 20.0% for profit, and 14.1% for profit subject to the complaint cap, on a 0.1-point grid. Estimation uncertainty, customer agency, and the justification for a constraint require additional evidence and reasoning.

## Verification and Figures

Seven tests check density integration, the population double-robustness identity, affine reproduction by the smoother, exclusion of an observation's own outcome from nuisance fitting, the hidden-confounder formula, profit accounting and constrained choice, and the complete-pooling limit. `verify_results.py` independently reconciles saved arrays with the reported tables and writes hashes to `verification.json`. It checks the committed reference directory.

`build_figures.py` reads the saved arrays and writes three editable TikZ sources in the lecture-notes figure folder. The uniform-discount projection figure uses the analytical curve and its population linear projection; it is separate from the observational sample. The two other figures use saved conditional densities and Store 0/4 curve estimates. Rendering runs through the notes builder. Illinois colors are supplemented by line styles and textual descriptions.

[Sources and implementation review](../../01_Resources/24_Dose_Response/README.md) preserve provenance and qualifications. The course examples do not reproduce the article's package rankings, hierarchical estimator, or continuous-DiD simulations.
