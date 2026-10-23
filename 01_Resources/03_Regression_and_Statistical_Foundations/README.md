# Regression and Statistical Foundations

Updated October 23, 2026. 7 curated resources. [Master Guide](../README.md).

Review regression as a way to summarize relationships and quantify uncertainty. Introduce model specification and interpretation before asking an assistant to fit a model. Causal interpretations require a separately justified design.

## Reading Guide

| ID | Resource | Priority | Format |
| --- | --- | --- | --- |
| R01 | [An Introduction to Statistical Learning, with Applications in Python](https://www.statlearning.com/) | Core | Textbook and author downloads |
| R02 | [ISLP Python Labs](https://github.com/intro-stat-learning/ISLP_labs) | Core | Notebook repository |
| R03 | [statsmodels: Ordinary Least Squares](https://www.statsmodels.org/stable/examples/notebooks/generated/ols.html) | Core | Guide |
| R04 | [statsmodels: Formulas](https://www.statsmodels.org/stable/example_formulas.html) | Core | Guide |
| R05 | [statsmodels: Regression Diagnostics](https://www.statsmodels.org/stable/examples/notebooks/generated/regression_diagnostics.html) | Core | Guide |
| R06 | [OpenIntro Statistics](https://www.openintro.org/book/os/) | Reference | Open textbook |
| R07 | [SciPy: Bootstrap](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bootstrap.html) | Reference | Guide |

Core identifies candidates for the eventual required readings. Reference material supports exercises and troubleshooting. Optional material supports extensions. Instructor material informs teaching and assessment; these labels are recommendations, not a finalized syllabus.

## Annotated Resources

### R01. An Introduction to Statistical Learning, with Applications in Python

**Source:** Gareth James, Daniela Witten, Trevor Hastie, Robert Tibshirani, and Jonathan Taylor. [Open Resource](https://www.statlearning.com/). **Priority:** Core. **Syllabus:** M3; M7.

Statistical learning, regression, classification, resampling, and model flexibility.

**Teaching Use:** Use chapters 2-5 for a common methods reference across regression and prediction.

**Conditions and Adaptation:** Author-provided PDF is for reading; do not assume permission to republish the book.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### R02. ISLP Python Labs

**Source:** ISLP authors. [Open Resource](https://github.com/intro-stat-learning/ISLP_labs). **Priority:** Core. **Syllabus:** M3; M4; M7.

Executable companion labs for statistical learning.

**Teaching Use:** Adapt the linear regression, classification, resampling, and unsupervised-learning labs.

**Conditions and Adaptation:** Downloaded notebooks are upstream examples, not tested course assignments. Data are loaded through the ISLP package and are not all bundled as separate local files.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Downloaded repository LICENSE: BSD-2-Clause. Retain attribution and notices; check separate dataset and third-party content terms.

**Local Files:**

- [Source_Notebooks/ISLP/LICENSE](Source_Notebooks/ISLP/LICENSE)
- [Source_Notebooks/ISLP/requirements.txt](Source_Notebooks/ISLP/requirements.txt)
- [Source_Notebooks/ISLP/README.md](Source_Notebooks/ISLP/README.md)
- [Source_Notebooks/ISLP/Ch03-linreg-lab.ipynb](Source_Notebooks/ISLP/Ch03-linreg-lab.ipynb)
- [Source_Notebooks/ISLP/Ch04-classification-lab.ipynb](Source_Notebooks/ISLP/Ch04-classification-lab.ipynb)
- [Source_Notebooks/ISLP/Ch05-resample-lab.ipynb](Source_Notebooks/ISLP/Ch05-resample-lab.ipynb)
- [Source_Notebooks/ISLP/Ch08-baggboost-lab.ipynb](Source_Notebooks/ISLP/Ch08-baggboost-lab.ipynb)
- [Source_Notebooks/ISLP/Ch12-unsup-lab.ipynb](Source_Notebooks/ISLP/Ch12-unsup-lab.ipynb)

**Verification:** Source URL retrieved successfully on October 23, 2026.

### R03. statsmodels: Ordinary Least Squares

**Source:** statsmodels contributors. [Open Resource](https://www.statsmodels.org/stable/examples/notebooks/generated/ols.html). **Priority:** Core. **Syllabus:** M3.

Fitting OLS and interpreting regression output in Python.

**Teaching Use:** Relate marketing spending and sales with explicit units and an interpretation of coefficients.

**Conditions and Adaptation:** Observational OLS coefficients need additional assumptions for causal interpretation.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### R04. statsmodels: Formulas

**Source:** statsmodels contributors. [Open Resource](https://www.statsmodels.org/stable/example_formulas.html). **Priority:** Core. **Syllabus:** M3.

Formula syntax for categorical predictors, interactions, and transformations.

**Teaching Use:** Translate a written marketing question into a formula and inspect the design matrix.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### R05. statsmodels: Regression Diagnostics

**Source:** statsmodels contributors. [Open Resource](https://www.statsmodels.org/stable/examples/notebooks/generated/regression_diagnostics.html). **Priority:** Core. **Syllabus:** M3.

Residuals, influence, specification, and diagnostic calculations.

**Teaching Use:** Ask AI to generate a diagnostic workflow and explain each warning in context.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### R06. OpenIntro Statistics

**Source:** OpenIntro. [Open Resource](https://www.openintro.org/book/os/). **Priority:** Reference. **Syllabus:** M3.

Accessible probability, sampling, inference, and regression explanations.

**Teaching Use:** Use selected sections for a statistics refresher and uncertainty exercises.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### R07. SciPy: Bootstrap

**Source:** SciPy contributors. [Open Resource](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bootstrap.html). **Priority:** Reference. **Syllabus:** M3.

Bootstrap confidence intervals and resampling options.

**Teaching Use:** Estimate uncertainty in customer revenue summaries while stating the sampling unit.

**Conditions and Adaptation:** Customer or cluster dependence requires a resampling scheme that respects that dependence.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.
