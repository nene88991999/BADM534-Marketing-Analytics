# Auxiliary Data and Bias Geometry

A product manager can buy additional human survey responses or generate inexpensive synthetic responses. The useful comparison is the cost of estimating the product attributes that matter for the decision at a specified accuracy. Synthetic responses contribute when their bias can be separated from at least some of those attributes.

Jasin, Lin, and Zhang's [Bias Geometry and the Value of Auxiliary Data](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7734298) supplies a useful explanation of this distinction. Its linear model allows unrestricted bias coefficients within a specified set of bias features. A synthetic respondent can overstate overall interest and distort price sensitivity while preserving the comparison between product features at a fixed price. Human observations remain necessary for the confounded coefficients.

## Connections to Marketing Analytics

| Module | Useful Addition | Existing Connection |
|---|---|---|
| M3 | Separate response coefficients from source-specific bias; show why more observations do not identify confounded coefficients. | [Regression](../../06_Lecture_Notes/modules/M03_Regression.md) |
| M4 | Allocate human research to comparisons that synthetic respondents cannot resolve. | [Synthetic concept screening, §4.23](../../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md) |
| M6 | Explain why a fixed experimental design can be efficient when information is known in advance. | [Causal inference and experiments](../../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md) |
| M7 | Evaluate the assumed bias features, respondent dependence, and stability on fresh human observations. | [Synthetic panel validation, §7.36](../../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md) |

M4 and M7 provide the strongest placement. These are proposed additions; the review does not change the released notes, slides, schedule, or assignment requirements. The [case design](CASE_DESIGN.md) develops a four-profile example and two proposed TikZ figures. The [source review](SOURCE_REVIEW.md) distinguishes the formal result, retrospective calibrations, and implications for course examples.

## Evidence and Interpretation

The paper reports potential sampling-cost reductions of approximately 74% and 32% in two calibrated models, assuming an auxiliary response costs 1% of a primary response. The results concern estimation of a specified vector of linear coefficients. They are conditional planning calculations, with simulated estimation errors, rather than realized savings from prospective field studies. The selected bias features determine which coefficients synthetic responses can help identify.

## Reproduce the Calculations

Run the original standard-library Python from the repository root:

```bash
python3 01_Resources/31_Auxiliary_Data_and_Bias_Geometry/source_checks.py
```

The program regenerates [source_checks.json](source_checks.json). It calculates the reported cost ratios, verifies the paper's closed-form four-profile allocation against an independent numerical search, and evaluates an original invented example. It uses no survey microdata, downloaded code, or model calls. The example values are analytic means and variances; no human or LLM responses were collected.

## Source and Access

The [catalog](catalog.json) records the working-paper version, stable source URL, file hash, and reading scope. The PDF is retained in the instructor's excluded Dropbox materials. The public repository contains original explanations and calculations with a source link. SSRN marks the paper as all rights reserved. The namespace for this folder's catalog is `auxiliary-bias`.
