# Verification of Auxiliary Data Examples

Verified November 23, 2026 with Python 3.14.8. Both original analysis programs use the standard library and calculate analytic moments from invented parameters. No human responses were collected, no model service was called, and no author code or empirical study was reproduced.

## Execution and Numerical Checks

From the repository root:

```bash
python3 03_Data_and_Code/Auxiliary_Data/allocate_responses.py
python3 03_Data_and_Code/Auxiliary_Data/bias_sensitivity.py
python3 -m unittest discover -s 03_Data_and_Code/Auxiliary_Data -p 'test_*.py' -v
python3 03_Data_and_Code/Auxiliary_Data/build_figures.py
python3 scripts/check_lecture_code.py
```

All six checks in `test_examples.py` passed. They cover the two profile contrasts; the closed-form allocation against an independent feasible grid; rounded counts and covariance from independently constructed joint regression normal equations; expected coefficient error and MSE under omitted feature bias; proportional sample growth and the expanded bias dictionary; and source-variance units and the no-auxiliary boundary. The covariance calculation reconstructs the five-parameter joint model rather than copying its scalar variance formula. The expanded dictionary uses a separate six-parameter model.

At total coefficient MSE 0.01, primary-only sampling requires 300 responses. The rounded mixed design uses 216 primary and 1,296 auxiliary responses, costs 228.96 normalized budget units, and has MSE 0.009920635. Its saving is 23.68%; the continuous allocation implies 24.285835%. An omitted auxiliary feature coefficient of 0.3 raises the expected feature estimate from 0.4 to 0.657142857 and total MSE to 0.076043084. Multiplying both sample counts by 32 reduces the variance to 0.000310020 while squared bias remains 0.066122449.

A temporary relocated copy ran both programs from `/tmp` with an explicit output directory. All five output files matched the saved analytic tables and summaries byte for byte. The general lecture-example verification passed. All 83 full Python blocks in the notes match their corresponding scripts and parse successfully.

## Figures and Documents

The plotted coordinates were independently compared with `profile_means.csv`, `value_curve.csv`, and `bias_sensitivity.csv`. All twelve series match the tables, zero-value comparison, stated limit, or one-third threshold to absolute tolerance 0.00000001. The two contrast panels share the same rating scale. The zero-cost endpoint is marked as a limit, and the sample-size chart separates variance, omitted-bias MSE, squared bias, and the original target.

The complete notes, Sessions 4, 5, 9, and 11, the combined slides, and the syllabus compiled. The thirteen affected note pages, all nine added slides, and both syllabus pages were visually inspected for equations, tables, labels, clipping, and code layout. The notes contain 369 pages and 97 TikZ figures. The fifteen decks contain 374 slides. All fifteen meetings retain contiguous 170-minute plans and the confirmed dates.

The examples describe a fixed linear model with known response and bias features and independent errors. Model correctness, respondent dependence, transport to new populations, and empirical cost savings require separate evidence. The optional lab provides practice with these distinctions and creates no graded requirement.

The [manifest](manifest.json) records the example inputs, programs, saved outputs, and figure hashes. The [source review](../../01_Resources/31_Auxiliary_Data_and_Bias_Geometry/SOURCE_REVIEW.md) separates the paper's retrospective calibrations from the original course calculations.
