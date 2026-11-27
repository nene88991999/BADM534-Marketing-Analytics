# Modern Power Analysis and Evidence About Harm

A public assurance about household costs requires evidence excluding a relevant burden. Power against a zero-effect null, evidence of equivalence, and a valid causal design answer different questions. These readings extend the inverse-power framework (Andrews, 1989) already used in the course.

The [catalog](catalog.json) contains 11 source records published or circulated in 2018–2026. Ten full reference files are saved locally in Dropbox, with their versions, hashes, and inspected passages recorded. The newest DID power article was inspected through its publisher abstract; its restricted full text was not obtained. A retrieved file does not imply that every proof or application was read. Original source copies remain outside public Git.

## Design Power

| Source | Contribution | Information Required for the Electricity Design |
| --- | --- | --- |
| [Panel Data and Experimental Design](https://doi.org/10.1016/j.jdeveco.2020.102458) (Burlig et al., 2020) | Power with nonconstant serial correlation; 2019 working-paper version saved | Outcome covariance, pre/post periods, assignment, and the relationship to the actual estimator |
| [Power With Variation in Treatment Timing](https://doi.org/10.3102/10769986211070625) (Schochet, 2022) | Staggered timing, clustering, unequal intervals, and covariates; 2021 author version saved | Exposure timing, cluster structure, repeated measurements, and a chosen effect |
| [Computing Statistical Power for DID](https://doi.org/10.1177/0193841X251380898) (Hedberg and Hedges, 2026) | Design-specific power and minimum detectable effects; first online in 2025 | Exact analysis and variance inputs; formulas were not inspected or implemented |

These formulas do not automatically describe a synthetic-control gap regression with repeated cumulative treatment. A full-design calculation must preserve the actual exposure process and the estimated comparison. Neither the observation count nor an assumed SE multiplier supplies that reconstruction.

## Equivalence and Identification

| Source | Contribution | Course Application |
| --- | --- | --- |
| [Pretest With Caution](https://doi.org/10.1257/aeri.20210236) (Roth, 2022) | Tests can miss consequential pre-trends; selecting on a passed test can distort inference | Assess the power of a design diagnostic before treating it as support for the counterfactual |
| [Equivalence of Pre-Trends](https://doi.org/10.1080/07350015.2024.2308121) (Dette and Schumann, 2024) | Tests small departures explicitly; contains a scalar folded-normal construction | Adapt the scalar test to reported price summaries; do not call it a joint pre-trend replication |
| [A More Credible Approach to Parallel Trends](https://doi.org/10.1093/restud/rdad018) (Rambachan and Roth, 2023) | Inference under specified classes of trend violations | Identify the coefficient vector, covariance, target, and restrictions needed before using HonestDiD |
| [Optimal Inference in Regression Models](https://doi.org/10.3982/ECTA14434) (Armstrong and Kolesár, 2018) | Confidence bounds account for worst-case bias within a stated model class | Derive an elementary scalar upper bound with an imposed bias allowance |

The folded-normal calculation uses an established scalar testing construction discussed in the modern equivalence paper. Its availability illustrates how a different test can answer the intended small-effect question. Its date does not establish its applicability to a particular empirical design.

## Cluster and Synthetic-Control Uncertainty

| Source | Contribution | Additional Inputs |
| --- | --- | --- |
| [Cluster-Robust Inference](https://doi.org/10.1016/j.jeconom.2022.04.001) (MacKinnon et al., 2023) | Leverage, finite-sample reliability, and bootstrap procedures | Regressors, residuals, cluster structure, and influence |
| [Prediction Intervals for Synthetic Controls](https://doi.org/10.1080/01621459.2021.1979561) (Cattaneo et al., 2021) | Uncertainty from estimated weights and post-treatment prediction errors | Donor and treated panels, constraints, and error models |
| [Staggered Synthetic-Control Inference](https://titiunik.github.io/files/publications/CattaneoFengPalombaTitiunik2025-RESTAT.pdf) (Cattaneo et al., 2025a) | Multiple treated units and simultaneous prediction; March 2025 manuscript saved | Adoption timing, a defined prediction target, and joint dependence |
| [scpi](https://www.jstatsoft.org/article/view/v113i01) (Cattaneo et al., 2025b) | Python, R, and Stata implementation | Correct input preparation and maintained prediction assumptions; software was not executed |

## Worked Critique

[M6 §§6.47–6.51](../../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md) displays the price comparisons that undermine broad reassurance. The [Python example](../../03_Data_and_Code/Modern_Power/README.md) reproduces the six price comparisons and three imposed bias scenarios discussed in the notes. These scalar approximations use rounded reported estimates and already-clustered SEs. They are not full-panel or synthetic-control replications.

At the paper's residential reference exposure, the one-sided 95% upper bound is $3.491/MWh. Illustrative margins of $1, $2, and $3/MWh are not excluded by the one-sided margin test, TOST, or the scalar folded-normal test. The four-owner estimate also leaves the displayed positive margins unresolved. These are teaching comparisons, with no claim that the chosen margins are validated household tolerances. The source and claim assessment is [here](../41_Statistical_Claims_and_Decisions/CLAIM_ASSESSMENT.md).

The conclusion concerns unsupported reassurance. A sufficiently informative design can establish a bounded small-effect claim. [M9 §9.83](../../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md) connects this distinction to truthful public communication and reasons owed to exposed people. [Optional practice](../../07_Labs/Statistical_Inference/README.md#modern-power-and-harm-bounds) asks students to specify the missing premise and the feasible response. The [verification record](VERIFICATION.md) identifies completed checks.
