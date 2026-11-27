# Longitudinal Identification

[Collection Index](../README.md) | [Catalog](../catalog.json)

## BC11: Causal Inference: What If

Miguel A. Hernán; James M. Robins. Book, 2020; author update January 2, 2025.

[Original source](https://miguelhernan.org/whatifbook) | [Public PDF](https://miguelhernan.org/s/hernanrobins_WhatIf_2jan25.pdf)

**Read:** Chapters 6–8, 19–21, and 23.

Treatment-confounder feedback requires methods appropriate to treatment histories. A variable can mediate an earlier treatment and confound a later one. Sequential exchangeability, positivity, and consistency support g-methods; ordinary adjustment does not inherit those properties automatically.

**Access and scope:** January 2, 2025 book update; contents and relevant explanations inspected selectively.

## BC13: Difference-in-Differences with “Bad Controls”

Carolina Caetano; Brantly Callaway; Stroud Payne; Hugo Sant’Anna. arXiv:2608.03881v2, submitted September 2, 2026; PDF dated September 3, 2026.

[Original source](https://arxiv.org/abs/2608.03881v2) | [Public PDF](https://arxiv.org/pdf/2608.03881v2)

**Read:** Sections 2–4 and 6; Theorems 1–2.

A treatment-affected covariate may also matter for untreated trends. Direct inclusion and wholesale exclusion can both fail. Additional assumptions recover its untreated evolution; baseline conditioning or nested imputation then targets the ATT. The course gives a linear finite-population illustration, not a replication of the full estimator.

**Access and scope:** arXiv v2 submitted September 2, 2026; PDF dated September 3. Setup and identification assumptions inspected.

## BC14: Difference-in-Differences when Parallel Trends Holds Conditional on Covariates

Carolina Caetano; Brantly Callaway. arXiv:2406.15288v3, submitted June 1, 2026; PDF dated June 3, 2026.

[Original source](https://arxiv.org/abs/2406.15288v3) | [Public PDF](https://arxiv.org/pdf/2406.15288v3)

**Read:** Conditional parallel trends and hidden linearity bias.

Transforming covariates in a fixed-effects regression can silently alter the identifying restriction. Conditional parallel trends must be linked to the actual estimator and covariate history. This issue differs from a covariate being affected by treatment.

**Access and scope:** arXiv v3 submitted June 1, 2026; PDF dated June 3. Abstract and identification discussion inspected.

## BC15: Difference-in-Differences with Multiple Time Periods

Brantly Callaway; Pedro H. C. Sant’Anna. Journal of Econometrics, 2021, 225(2), 200–230; arXiv v4, December 2020.

[Original source](https://arxiv.org/abs/1803.09015v4) | [Public PDF](https://arxiv.org/pdf/1803.09015v4)

**Read:** Group-time ATT, conditional parallel trends, anticipation.

Define which cohorts and periods supply each comparison. Not-yet-treated units qualify only over periods consistent with the assumed anticipation horizon. Aggregation choices determine the population and timing represented by the reported effect.

**Access and scope:** arXiv v4, December 2020; abstract and assumptions inspected.

## BC16: Doubly Robust Difference-in-Differences Estimators

Pedro H. C. Sant’Anna; Jun B. Zhao. Journal of Econometrics, 2020; arXiv v3, May 5, 2020.

[Original source](https://arxiv.org/abs/1812.01723v3) | [Public PDF](https://arxiv.org/pdf/1812.01723v3)

**Read:** Panel ATT identification and doubly robust estimation.

Double robustness concerns alternative nuisance-model specifications within an identified design. It does not mean robustness to an invalid control set, hidden anticipation, or exposed comparison units.

**Access and scope:** arXiv v3, May 2020; abstract and identifying framework inspected.

## BC21: Double/Debiased Machine Learning for Treatment and Structural Parameters

Victor Chernozhukov; Denis Chetverikov; Mert Demirer; Esther Duflo; Christian Hansen; Whitney Newey; James Robins. arXiv:1608.00060v7, November 3, 2024; related Econometrics Journal article, 2018.

[Original source](https://arxiv.org/abs/1608.00060v7) | [Public PDF](https://arxiv.org/pdf/1608.00060v7)

**Read:** Orthogonal scores, cross-fitting, treatment-effect applications.

Cross-fitting and orthogonal scores reduce sensitivity to nuisance estimation error under stated identification conditions. Flexible adjustment for the wrong variables can estimate the wrong causal object more precisely.

**Access and scope:** arXiv v7, November 2024; PDF title uses Treatment and Structural Parameters; summary and setup inspected.

## BC22: Marginal Structural Models and Causal Inference in Epidemiology

James M. Robins; Miguel A. Hernán; Babette Brumback. Epidemiology, 2000, 11(5), 550–560.

[Original source](https://doi.org/10.1097/00001648-200009000-00011)

**Read:** Treatment-confounder feedback and inverse-probability weighting.

Marginal structural models address treatment histories when a confounder is itself affected by earlier treatment. Validity still requires measured sequential confounding, positivity, and consistent interventions. Pair with Hernán and Robins Chapters 19–21.

**Access and scope:** Bibliographic record and abstract verified; complete article not downloaded.
