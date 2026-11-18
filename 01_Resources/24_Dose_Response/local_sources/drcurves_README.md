# drcurves

**Doubly robust dose-response curves for continuous treatments, for one population or many groups.**

How does the outcome change as the dose changes: discount depth and margin, handle time and
satisfaction, notifications per week and retention? `drcurves` estimates the whole curve, not one
slope, from observational data:

- **Doubly robust.** The curve stays close to the truth if either the outcome model or the dose
  model is right (Kennedy et al. 2017).
- **Many curves at once.** A curve per store, product or customer issue, partially pooled across a
  hierarchy (region → store), so small groups borrow strength from their parents.
- **Choose your assumption.** Adjust for measured confounders; or, with a pre-period outcome, use
  difference-in-differences (`y_pre=`) when a stable trait you can't measure drives both the dose
  and the outcome, or adjust for the lagged outcome (`design="lagged"`) when doses respond to past
  outcomes. A placebo check tests the DiD assumption.
- **Sensible defaults.** Every nuisance model is a stack of a spline regression and gradient
  boosting, which in our simulations beat boosting alone and the existing packages.

It accompanies the article *Estimating Continuous Treatment Effects: Doubly Robust Dose-Response
Curves*. Early release: the API may change before 1.0.

## Resources

| | |
|---|---|
| 📚 [Documentation](https://raz1470.github.io/continuous-dr-learner/) | User guide, examples and API reference |
| 📖 [Walkthrough](https://raz1470.github.io/continuous-dr-learner/walkthrough.html) | The article: why one slope isn't enough, and the method step by step on simulated data |
| 📓 [One curve](https://github.com/raz1470/continuous-dr-learner/blob/main/examples/01_one_curve.ipynb) | Fit with the defaults and read the results |
| 🏪 [Curves for many groups](https://github.com/raz1470/continuous-dr-learner/blob/main/examples/02_group_curves.ipynb) | A curve per store, pooled across regions |
| 🎯 [Checking the bands](https://raz1470.github.io/continuous-dr-learner/guide/checking_bands.html) | `coverage_check` on your own data |
| 🔬 [Research](https://raz1470.github.io/continuous-dr-learner/research.html) | How often the 95% bands contain the true curve |
| 📝 [Changelog](https://github.com/raz1470/continuous-dr-learner/blob/main/CHANGELOG.md) | What changed in each release |

## Install

```bash
pip install drcurves
pip install "drcurves[plot]"    # adds matplotlib for model.plot()
```

## Quick start

```python
import numpy as np
from drcurves import fit_dose_response
from drcurves.simulate import sim_nonlinear

X, A, Y, truth = sim_nonlinear(n=3000, curve="inverted_u_centred", seed=1)

model = fit_dose_response(X, A, Y)          # cross-fit, doubly robust, smooth curve
print(model.diagnostics())                  # overlap and fit checks: read these first

grid = np.linspace(*np.quantile(A, [0.05, 0.95]), 50)
est, se = model.curve(grid)                 # curve and pointwise standard errors
est, lo, hi, _ = model.band(grid)           # 95% band for the whole curve
lift, se = model.contrast(-1.0, 0.0)        # effect of moving the dose from -1 to 0
best = model.optimal_dose(grid)             # dose that maximises the outcome, with an interval
model.plot(truth=truth)                     # needs matplotlib
```

## Many groups

```python
from drcurves.simulate import sim_hierarchical
df, _, _ = sim_hierarchical(seed=0)         # region, store, x0..x2, A, Y

model = fit_dose_response(df[["x0", "x1", "x2"]], df["A"], df["Y"],
                          groups=df[["region", "store"]])       # top -> bottom
store, se = model.curve(grid, ("r0", "r0_s03"))   # a store's curve, shrunk toward its region
region, _ = model.curve(grid, ("r0",))
new, _ = model.curve(grid, ("r0", "unseen"))      # a new store gets its region's curve
model.plot(paths=[("r0",), ("r0", "r0_s03")])
```

| Your data | `groups=` | What you get |
|---|---|---|
| One population | `None` | One curve |
| Groups, no hierarchy | `df[["store"]]` | One curve per store, shrunk toward the overall curve |
| Nested hierarchy | `df[["region", "store"]]` | Stores shrunk toward their region, regions toward the overall curve |

Levels must be nested; crossed groupings (store × channel) aren't supported. Shrinkage acts on each
group's shape; its overall level is left nearly free. `path=None` under partial pooling is a
"typical group" curve; for the population average, fit with `groups=None`.

## Choosing the assumption

```python
# Measured confounders explain who got which dose (the default)
model = fit_dose_response(X, A, Y_post)

# A stable trait you can't measure drives dose and outcome: difference-in-differences
model = fit_dose_response(X, A, Y_post, y_pre=Y_pre)

# The dose responds to past outcomes: adjust for the lagged outcome instead
model = fit_dose_response(X, A, Y_post, y_pre=Y_pre, design="lagged")

# Placebo for DiD: the curve on two pre-periods should be flat. Judge it by size, not significance.
from drcurves import placebo_check
pc = placebo_check(X, A, Y_pre, Y_prepre, main=model)
pc["relative"]      # largest placebo deviation / range of the real curve; small is good
```

Comparing doses under DiD needs *strong* parallel trends: units on different doses would have
followed the same path had their doses been equal (Callaway, Goodman-Bacon & Sant'Anna 2024).

In simulation ([`experiments/sim_did.py`](https://github.com/raz1470/continuous-dr-learner/blob/main/experiments/sim_did.py)), each design wins in its own world, and the placebo tells
them apart (RMSE of the curve; placebo = largest deviation of the pre-period curve from flat):

| | Adjust for X | Lagged outcome | DiD | Placebo |
|---|---|---|---|---|
| A stable hidden trait drives the dose | 1.06 | 0.29 | **0.04** | 0.03 (flat) |
| The dose responds to past outcomes | 0.24 | **0.05** | 0.16 | 0.16 (not flat) |

A clearly non-flat placebo is a reason to prefer the lagged design, or to report both.

## Options worth knowing

- **Models.** `outcome_model=` and `gps=GPS(mean_model=..., scale_model=...)` take any sklearn
  regressor. The default for each is `default_model()`.
- **Weights.** For a continuous dose the default is `GPS()`, density-based weights. `BalancingWeights()`
  (entropy balancing; population curve only) is an alternative. A dose with ≤ 30 distinct values
  (tiers, counts) uses `DiscreteGPS` automatically.
- **Uncertainty.** `band(simultaneous=False)` for pointwise bands; `draws()` for any other summary.
  A group with no data (a new store) gets its parent's curve with a wider, predictive band that adds
  the spread between groups (`predictive=True`, the default). The bands include the variance from
  estimating m(a) (`nuisance_var=True`, Kennedy et al. 2017);
  `bootstrap_curves()` refits the whole pipeline and is the only option that includes
  nuisance-model uncertainty (slow). `coverage_check()` runs a plasmode simulation on your own data
  to check how often the bands cover a known curve, and returns calibrated critical values.
- **Repeated units.** `fold_groups=` keeps a customer's rows in one cross-fitting fold; `cluster=`
  makes the robust covariance types cluster-robust.
- **Inputs.** `X` may be a DataFrame (non-numeric columns are coded) and may contain missing values.
  Errors and warnings flag mismatched lengths, a constant or missing dose, groups with fewer than
  10 rows, a point mass in the dose, and poor overlap after fitting.
- **Speed.** About 45 s for 3,000 rows and 50 confounders on 2 cores; `n_jobs=-1` runs the
  cross-fitting folds in parallel.

## When to use something else

- **One population curve, a few confounders, working in R:** [npcausal](https://github.com/ehkennedy/npcausal)
  (Kennedy's own implementation) is close in accuracy.
- **Staggered adoption with a continuous dose:** [contdid](https://github.com/bcallaway11/contdid) (R) or
  `diff_diff.ContinuousDiD` (Python).
- **You only need an average slope and trust linearity:** DoubleML's partially linear model.
- **Unmeasured confounders with no pre-period:** no estimator fixes this; you need a different design
  (an instrument, a discontinuity or an experiment).

## How it compares

One population curve, 10 simulated datasets per setting. RMSE of the centred curve / share of doses
where the 95% band contains the truth.

| | 5 confounders | 50 confounders | Harder data |
|---|---|---|---|
| **drcurves**, default | **0.06** / 75% | **0.04** / 93% | **0.25** / 75% |
| drcurves, `BalancingWeights()` | 0.07 / 88% | 0.05 / 90% | 0.39 / 18% |
| [npcausal](https://github.com/ehkennedy/npcausal) (R) | 0.08 / 90% | 0.18 / 77% | 0.30 / 13% |
| [causal-curve](https://github.com/ronikobrosly/causal-curve) (Python) | 0.54 / 100% | 0.30 / 100% | 0.44 / 100% |
| drcurves with boosting alone | 0.19 / 94% | 3.43 / 87% | 3.07 / 97% |

The harder data has thresholds, interactions and heavy-tailed noise; there, boosting alone gave the
best outcome model (0.18 with balancing weights, but 43% coverage). No learner wins everywhere,
which is why the default stacks two. causal-curve's bands are 25+ times wider than the others'.
These are our simulations with each package's defaults; treat the ranking as indicative.

## How it works

```
1. cross-fit   mu(x, a) = E[Y | X, A]   and   pi(a | x)  (density of the dose given X)
2. pseudo-outcome   xi = (Y - mu(X, A)) * varpi(A) / pi(A | X) + m(A)
3. regress xi on A with penalised splines:
       theta_store(a) = B(a)' (beta_global + b_region + b_store)
   ridge penalties on the deviations b shrink small groups toward their parent (tuned by GCV)
```

`varpi` is the marginal density of the dose and `m(a)` the outcome model averaged over X. The
pseudo-outcome's mean, given the dose, is the true curve if either nuisance model is right.

## Caveats

- Everything assumes the design you chose is right: unconfoundedness given X, or (strong) parallel
  trends for DiD. Double robustness protects against a wrong model, not a missing variable.
- Report curves over the observed dose range. Weights are capped at the 99th percentile by default
  (`max_weight_quantile`), trading a little bias for a lot of variance.
- The 95% bands are slightly optimistic: in our simulations they contained the true curve 75-93% of
  the time (stores 81%), mostly because capping the weights leaves a small bias. Check with
  `coverage_check` before relying on them; details on the [research page](https://raz1470.github.io/continuous-dr-learner/research.html).
- Experimental, not supported: `drcurves.riesz` (learned Riesz weights).

## Reproduce the article

```bash
pip install -e ".[experiments,dev]"
python experiments/sim1_nonlinear.py
python experiments/sim2_double_robustness.py 30
python experiments/sim3_hierarchical_shrinkage.py 5
python experiments/compare_causal_curve.py 10; python experiments/compare_npcausal.py 10   # npcausal needs R
python experiments/compare_stacked.py 10; python experiments/compare_hard.py 10
python experiments/sim_did.py 10; python experiments/sim_did.py 8 --past-outcome
python experiments/sim4_uncertainty.py single 42; python experiments/sim4_uncertainty.py stores 15
python experiments/sim6_intervals.py 15
python tools/build_article.py      # -> article/index.html
pytest                             # add -m slow for the experimental tests
```

Interval coverage studies are on the [research page](https://raz1470.github.io/continuous-dr-learner/research.html); the API is in the
[documentation](https://raz1470.github.io/continuous-dr-learner/api/index.html); open work is in [`BACKLOG.md`](https://github.com/raz1470/continuous-dr-learner/blob/main/BACKLOG.md).

## References

- Kennedy, Ma, McHugh & Small (2017). Non-parametric methods for doubly robust estimation of continuous treatment effects. *JRSS-B* 79(4).
- Callaway, Goodman-Bacon & Sant'Anna (2024). Difference-in-differences with a continuous treatment. arXiv:2107.02637.
- Chernozhukov et al. (2018). Double/debiased machine learning. *Econometrics Journal* 21(1).
- Valentin, Detommaso, Li, Opper & Brueckner (2025). On double robustness in double machine learning. NeurIPS 2025 Workshop CauScien.
- Tübbicke (2022). Entropy balancing for continuous treatments. *Journal of Econometric Methods* 11(1).
- Franklin, Schneeweiss, Polinski & Rassen (2014). Plasmode simulation for the evaluation of pharmacoepidemiologic methods. *CSDA* 72.
- Marra & Wood (2012). Coverage properties of confidence intervals for GAM components. *Scand. J. Statistics* 39(1).
- Eilers & Marx (1996). Flexible smoothing with B-splines and penalties. *Statistical Science* 11(2).

[MIT licence](https://github.com/raz1470/continuous-dr-learner/blob/main/LICENSE).

