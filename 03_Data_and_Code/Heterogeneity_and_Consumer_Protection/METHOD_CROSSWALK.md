# Hierarchical Regression, Pooling, and Missed Harm

## The Documented Method

The `cheese.Rd` example prepares account-specific regressions for `rhierLinearModel`. The package documentation identifies the hierarchical regression model and its author (Rossi, 2025, bayesm 3.1-7). The maintained source separates the hierarchical loop from the conditional coefficient draw. The file `rhierLinearModel_rcpp_loop.cpp` forms the prior precision from `Vbeta`, constructs the prior mean `Z * Delta`, and calls `runiregG` in `utilityFunctions.cpp`. The latter adds data precision and prior precision before drawing each regression coefficient vector. These GPL source files are saved under `upstream/`, with pinned hashes in `PROVENANCE.json`. They were inspected, not executed.

## The Exact Conditional Update

For regression $j$, let $y_j=X_j\beta_j+e_j$, with $e_j\sim N(0,v_jI)$, and let $\beta_j\sim N(\mu_j,V)$, where $\mu_j=Z_j\Delta$. Conditional on $v_j$, $V$, and $\Delta$, the posterior covariance and mean are

$$C_j=(X_j'X_j/v_j+V^{-1})^{-1},\qquad
m_j=C_j(X_j'y_j/v_j+V^{-1}\mu_j).$$

The source computes this covariance through a Cholesky factor and this mean through the precision-weighted right-hand side. The course's `conditional_update` computes the same normal conditional moments without drawing random values. Setting $X'X=1$, $X'y=2$, $v=1$, $\mu=0$, and $V=0.4$ gives $C=2/7$ and $m=4/7$. These equal $w\sigma^2$ and $wY$ in the precision example. The connection is an exact scalar conditional specialization of the documented update, rather than a verbal analogy.

## The Decision That Produces the Loss

The known-harm simulation holds the population, raw observations, and follow-up horizon fixed. It substitutes the pooled conditional posterior for the unpooled estimate and applies a one-sided 95% posterior lower-bound rule. Relative to the unpooled benchmark, detection falls by 49.81 percentage points and synthetic missed-harm loss increases by $119,538 across the specified 10,000 consumers and 12 months. This difference is caused by the estimator-and-decision-rule change in the constructed experiment. Average MSE nevertheless falls by 71.43%, and reported posterior SD falls by 46.55%.

The source implementation supplies the pooling mechanism. The synthetic harmful population, fixed hyperparameters, centered prior, protection rule, and dollar losses are additional course assumptions. The normal working prior approximates the two-point population. The result does not establish an observed injury in the cheese data or the published trade-promotion application. Full hierarchical sampling also updates the mean, covariance, and residual variances. Integrating uncertainty in those quantities can change intervals and decisions, so conditional precision must not be reported as the full sampler's uncertainty.

The mechanism matters when a low pooled mean, weak group-specific information, and a demanding posterior rule make a minority burden difficult to flag. More heterogeneous prior dispersion weakens the pooling; unrestricted claims that adding heterogeneity always suppresses harm are unsupported. The criticism instead identifies a particular operation in the method and the institutional use that makes its missed detections costly.

## Sources

- (Rossi, 2025), [hierarchical model documentation at the pinned version](https://github.com/cran/bayesm/blob/453ae30857cf09a0c537f4deab64ed193493c8c9/man/rhierLinearModel.Rd).
- (Kim, 2014; bayesm 3.1-7), [hierarchical loop](https://github.com/cran/bayesm/blob/453ae30857cf09a0c537f4deab64ed193493c8c9/src/rhierLinearModel_rcpp_loop.cpp) and [conditional update](https://github.com/cran/bayesm/blob/453ae30857cf09a0c537f4deab64ed193493c8c9/src/utilityFunctions.cpp). Preserve the implementation contributor's attribution separately from the package author's model documentation.
- (Boatwright et al., 1999), [study attributed by the public data documentation](https://doi.org/10.1080/01621459.1999.10473859). The public package and preprint sample differ.
- (Gelman et al., 2012, pp. 196–198), [partial-pooling algebra](https://doi.org/10.1080/19345747.2011.618213).
