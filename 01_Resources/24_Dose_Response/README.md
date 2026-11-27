# Dose-Response Curves and Marketing Decisions

A marketing decision often concerns how much discount, spending, or contact to assign. The [source article](https://towardsdatascience.com/how-to-estimate-dose-response-curves-when-doubleml-falls-short/) motivates nonlinear causal responses, group-specific estimates, and interval assessment. The course uses original synthetic calculations to connect those ideas to [M6](../../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md), [M8](../../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md), and [Marketing Dialectics](../../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md).

## Primary Reading Path

[The catalog](catalog.json), namespace `dose-response`, records eight resources and their scope. Begin with the continuous-treatment estimator [(Kennedy et al., 2017)](https://arxiv.org/abs/1507.00747v3) for the adjusted outcome and its identifying assumptions. [DoubleML documentation](https://docs.doubleml.org/stable/guide/models.html) defines the partially linear specification. A nonparametric DML alternative supplies different identifying and estimation conditions [(Colangelo and Lee, 2023)](https://arxiv.org/abs/2004.03036). Continuous-treatment level effects and causal responses require different parallel-trends assumptions [(Callaway et al., 2025)](https://arxiv.org/abs/2107.02637v8).

## Methodological Distinctions

The default partially linear regression specification estimates a constant slope. DML methods also allow nonlinear treatment responses. Orthogonality and double robustness are distinct properties; the latter depends on the score and nuisance definitions. A doubly robust estimator still requires a credible intervention, conditional support, and adequate control of confounding. Fixed smoothing, finite samples, clipping, and nuisance fitting affect inference.

The article's hierarchical package uses group-specific standardization before smoothing adjusted outcomes within a hierarchy. This step matters for targeting group means. Partial pooling can improve precision while introducing shrinkage bias. A new store's predicted curve depends on the hierarchy assumptions and is distinct from an identified store-specific response.

The source reports undercoverage in its own experiments. Its rankings use a small set of simulation designs and chosen implementations; they do not establish general software superiority. Source intervals, their nominal event, and achieved coverage need separate interpretation. The course's conditional HC0 intervals are explicitly evaluated approximations, with pointwise and whole-grid events reported separately.

The continuous-DiD extension removes a stable hidden component in a particular additive simulation. Ordinary parallel trends alone generally does not identify causal differences across dose groups. A pretreatment placebo supplies a diagnostic rather than proof of the stronger assumptions. DiD remains advanced reading in this extension.

## Course Materials and Execution

[Three complete Python examples](../../03_Data_and_Code/Dose_Response/README.md) provide an observational discount case, a separate randomized-store pooling case, and a known-function decision comparison. The first evaluates four nuisance specifications over 200 independent simulated datasets. Seven tests and saved numeric arrays support the [optional ungraded lab](../../07_Labs/Dose_Response/README.md). The article's package simulations were not executed. Three editable TikZ figures use Illinois colors, common comparison scales, and text companions.

## Provenance and Rights

Reviewed November 18, 2026. The source article was read in the public browser; primary papers and documentation supplied the methodological checks. `drcurves` README and its MIT license are retained at commit `72115789652127cc2a89eb960d829d2cc513d9cb`. The implementation review inspected `src/drcurves/nuisance.py` and `src/drcurves/__init__.py`, including group-specific integration and default weight capping. Original software instructions remain reference content. Article and paper texts are linked rather than redistributed. The local catalog records versions, access scope, and snapshot hashes.
