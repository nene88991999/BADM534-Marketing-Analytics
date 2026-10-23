# Causal Inference and Experiments

Updated October 23, 2026. 9 curated resources. [Master Guide](../README.md).

Specify treatment, outcome, target population, assignment mechanism, and comparison before estimation. Begin with randomized experiments, then use observational designs to discuss identification and their assumptions.

## Reading Guide

| ID | Resource | Priority | Format |
| --- | --- | --- | --- |
| E01 | [Causal Inference for the Brave and True](https://matheusfacure.github.io/python-causality-handbook/landing-page.html) | Core | Open web book |
| E02 | [The Effect: An Introduction to Research Design and Causality](https://theeffectbook.net/) | Core | Open web book |
| E03 | [Causal Inference: The Remix (Mixtape Website)](https://mixtape.scunning.com/) | Reference | Open web book |
| E04 | [DoWhy Documentation](https://www.pywhy.org/dowhy/v0.13/) | Reference | Guide |
| E05 | [EconML Documentation](https://econml.azurewebsites.net/) | Optional | Guide |
| E06 | [Practical Guide to Controlled Experiments on the Web](https://exp-platform.com/Documents/GuideControlledExperiments.pdf) | Core | Research paper |
| E07 | [statsmodels: Power and Sample Size Calculations](https://www.statsmodels.org/stable/stats.html#power-and-sample-size-calculations) | Core | Guide |
| E08 | [CausalML Documentation](https://causalml.readthedocs.io/en/latest/) | Optional | Guide |
| E09 | [A Comparison of Approaches to Advertising Measurement: Evidence from Big Field Experiments at Facebook](https://brgordon1.github.io/publication/2019-comparison-advertising-measurement) | Core | Research paper |

Core identifies candidates for the eventual required readings. Reference material supports exercises and troubleshooting. Optional material supports extensions. Instructor material informs teaching and assessment; these labels are recommendations, not a finalized syllabus.

## Annotated Resources

### E01. Causal Inference for the Brave and True

**Source:** Matheus Facure. [Open Resource](https://matheusfacure.github.io/python-causality-handbook/landing-page.html). **Priority:** Core. **Syllabus:** M6.

Potential outcomes, experiments, confounding, regression, and causal estimation in Python.

**Teaching Use:** Use introduction, randomization, graphical models, and selected regression chapters.

**Conditions and Adaptation:** Advanced chapters are optional; distinguish simulated teaching examples from field evidence. Selected notebooks and referenced CSVs are saved; images and dependencies may still require the upstream repository.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Downloaded repository LICENSE: MIT. Retain attribution and notices; check separate dataset and third-party content terms.

**Local Files:**

- [Source_Notebooks/Causal_Handbook/LICENSE](Source_Notebooks/Causal_Handbook/LICENSE)
- [Source_Notebooks/Causal_Handbook/README.md](Source_Notebooks/Causal_Handbook/README.md)
- [Source_Notebooks/Causal_Handbook/causal-inference-for-the-brave-and-true/02-Randomised-Experiments.ipynb](Source_Notebooks/Causal_Handbook/causal-inference-for-the-brave-and-true/02-Randomised-Experiments.ipynb)
- [Source_Notebooks/Causal_Handbook/causal-inference-for-the-brave-and-true/04-Graphical-Causal-Models.ipynb](Source_Notebooks/Causal_Handbook/causal-inference-for-the-brave-and-true/04-Graphical-Causal-Models.ipynb)
- [Source_Notebooks/Causal_Handbook/causal-inference-for-the-brave-and-true/13-Difference-in-Differences.ipynb](Source_Notebooks/Causal_Handbook/causal-inference-for-the-brave-and-true/13-Difference-in-Differences.ipynb)
- [Source_Notebooks/Causal_Handbook/causal-inference-for-the-brave-and-true/18-Heterogeneous-Treatment-Effects-and-Personalization.ipynb](Source_Notebooks/Causal_Handbook/causal-inference-for-the-brave-and-true/18-Heterogeneous-Treatment-Effects-and-Personalization.ipynb)
- [Source_Notebooks/Causal_Handbook/causal-inference-for-the-brave-and-true/19-Evaluating-Causal-Models.ipynb](Source_Notebooks/Causal_Handbook/causal-inference-for-the-brave-and-true/19-Evaluating-Causal-Models.ipynb)
- [Source_Notebooks/Causal_Handbook/causal-inference-for-the-brave-and-true/data/online_classroom.csv](Source_Notebooks/Causal_Handbook/causal-inference-for-the-brave-and-true/data/online_classroom.csv)
- [Source_Notebooks/Causal_Handbook/causal-inference-for-the-brave-and-true/data/billboard_impact.csv](Source_Notebooks/Causal_Handbook/causal-inference-for-the-brave-and-true/data/billboard_impact.csv)
- [Source_Notebooks/Causal_Handbook/causal-inference-for-the-brave-and-true/data/ice_cream_sales.csv](Source_Notebooks/Causal_Handbook/causal-inference-for-the-brave-and-true/data/ice_cream_sales.csv)
- [Source_Notebooks/Causal_Handbook/causal-inference-for-the-brave-and-true/data/ice_cream_sales_rnd.csv](Source_Notebooks/Causal_Handbook/causal-inference-for-the-brave-and-true/data/ice_cream_sales_rnd.csv)

**Verification:** Source URL retrieved successfully on October 23, 2026.

### E02. The Effect: An Introduction to Research Design and Causality

**Source:** Nick Huntington-Klein. [Open Resource](https://theeffectbook.net/). **Priority:** Core. **Syllabus:** M6.

Research questions, identification, causal diagrams, and research designs.

**Teaching Use:** Require students to state treatment, outcome, comparison, and identifying assumptions before coding.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### E03. Causal Inference: The Remix (Mixtape Website)

**Source:** Scott Cunningham. [Open Resource](https://mixtape.scunning.com/). **Priority:** Reference. **Syllabus:** M6.

Applied causal inference and econometric research designs.

**Teaching Use:** Use selected examples to discuss difference-in-differences and observational designs.

**Conditions and Adaptation:** The current author site presents The Remix; references to the earlier Mixtape edition should be checked against the selected chapter.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### E04. DoWhy Documentation

**Source:** PyWhy contributors. [Open Resource](https://www.pywhy.org/dowhy/v0.13/). **Priority:** Reference. **Syllabus:** M6.

Explicit causal graphs, identification, estimation, and refutation checks.

**Teaching Use:** Audit a generated causal analysis by checking its graph and identifying assumptions.

**Conditions and Adaptation:** Pinned documentation reference; package versions and APIs must be checked for the eventual lab.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### E05. EconML Documentation

**Source:** Microsoft and EconML contributors. [Open Resource](https://econml.azurewebsites.net/). **Priority:** Optional. **Syllabus:** M6.

Heterogeneous treatment effects and policy-relevant causal estimation.

**Teaching Use:** Contrast response prediction with incremental response for targeting.

**Conditions and Adaptation:** Requires stronger prerequisites and careful overlap, splitting, and identification checks.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### E06. Practical Guide to Controlled Experiments on the Web

**Source:** Ron Kohavi, Randal M. Henne, and Dan Sommerfield. [Open Resource](https://exp-platform.com/Documents/GuideControlledExperiments.pdf). **Priority:** Core. **Syllabus:** M6.

Practical design and interpretation of online randomized experiments.

**Teaching Use:** Write an experiment plan defining randomization unit, primary metric, guardrails, and decision rule.

**Conditions and Adaptation:** Foundational paper; supplement platform-specific implementation with current documentation.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Author-posted version explicitly permits personal use and prohibits redistribution. Keep the local PDF for instructor reading; link to the author source in the public wiki.

**Local Files:**

- [Papers/Kohavi_Henne_Sommerfield_KDD2007.pdf](Papers/Kohavi_Henne_Sommerfield_KDD2007.pdf)

**Verification:** Source URL retrieved successfully on October 23, 2026.

### E07. statsmodels: Power and Sample Size Calculations

**Source:** statsmodels contributors. [Open Resource](https://www.statsmodels.org/stable/stats.html#power-and-sample-size-calculations). **Priority:** Core. **Syllabus:** M6.

Power calculations for planned tests.

**Teaching Use:** Relate a minimum economically meaningful effect to required sample size and experiment duration.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### E08. CausalML Documentation

**Source:** Uber and CausalML contributors. [Open Resource](https://causalml.readthedocs.io/en/latest/). **Priority:** Optional. **Syllabus:** M6.

Uplift models, treatment-effect estimation, and evaluation.

**Teaching Use:** Compare a treatment-effect ranking with a purchase-propensity ranking.

**Conditions and Adaptation:** Use randomized or defensibly identified data; predictive accuracy alone does not validate uplift.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### E09. A Comparison of Approaches to Advertising Measurement: Evidence from Big Field Experiments at Facebook

**Source:** Brett R. Gordon, Florian Zettelmeyer, Neha Bhargava, and Dan Chapsky. [Open Resource](https://brgordon1.github.io/publication/2019-comparison-advertising-measurement). **Priority:** Core. **Syllabus:** M6.

Comparison of observational advertising estimates with randomized experimental benchmarks.

**Teaching Use:** Discuss why a successful response model need not measure the effect of advertising.

**Conditions and Adaptation:** Findings concern the studied campaigns and available control variables.

**Access and Reuse:** Public author abstract and citation; full text links to the publisher and may require library access. Link to source; public redistribution not cleared.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.
