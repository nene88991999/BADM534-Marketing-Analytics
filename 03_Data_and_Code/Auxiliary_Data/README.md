# Human and Synthetic Evidence for Product Design

A body-wash manager needs the value of a premium feature and customers' response to price. Four invented profiles show how an auxiliary source can preserve one comparison and distort the other. Two standard-library programs compare research cost at a common accuracy target and calculate the consequences of an omitted bias feature.

The statistical model follows §5.3 of Jasin, Lin, and Zhang's [Bias Geometry and the Value of Auxiliary Data](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7734298). The numerical inputs, programs, figures, and exercises are original course adaptations. No human responses, LLM calls, or author code are used. Conditional means, sampling variances, and expected estimation errors are calculated analytically.

## Files and Reproduction

The input is [data/parameters.json](data/parameters.json). [DATA_DICTIONARY.md](DATA_DICTIONARY.md) defines observation units, attribute coding, model restrictions, costs, and outputs. Run from the repository root with Python 3.10 or later:

```bash
python3 03_Data_and_Code/Auxiliary_Data/allocate_responses.py
python3 03_Data_and_Code/Auxiliary_Data/bias_sensitivity.py
python3 -m unittest discover -s 03_Data_and_Code/Auxiliary_Data -p 'test_*.py' -v
python3 03_Data_and_Code/Auxiliary_Data/build_figures.py
```

Both analysis programs resolve inputs relative to their own location and accept `--output /path/to/folder`. They require only Python's standard library. There is no random seed because the programs use exact mean and variance formulas without sampling. The figure builder writes editable TikZ from saved tables; the lecture builder compiles the figure previews and PDF.

## Results and Interpretation

| Comparison | Result |
|---|---|
| Premium-minus-standard rating at a fixed price | Both invented sources increase by 0.8 points. |
| High-minus-low price rating at a fixed feature | Primary decreases by 1.0 point; auxiliary increases by 0.2 points. |
| Primary-only design at total coefficient MSE 0.01 | 300 responses, cost 300. |
| Rounded hybrid design at the same target | 216 primary and 1,296 auxiliary responses; cost 228.96; MSE 0.009921. |
| Rounded and asymptotic cost savings | 23.68% and 24.29%, respectively. |
| Auxiliary feature bias of 0.3 omitted from estimation | Expected feature coefficient 0.657143; total MSE 0.076043. |
| Both sample sizes multiplied by 32 with the same omitted bias | MSE 0.066432, approaching the squared-bias floor 0.066122. |

The cost comparison estimates the same three coefficients with the same coding and MSE target. Sampling independence and the specified response and bias features are substantive assumptions. A smaller standard error does not eliminate an omitted bias. With unrestricted bias on every primary feature, auxiliary responses provide no additional information for the paper's worst-case coefficient-estimation objective.

## Course Materials

- [M4 §4.24](../../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md) contains the model, allocation, figures, and complete first program.
- [M7 §7.37](../../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md) contains the omitted-bias comparison, human-validation discussion, and complete second program.
- [M3 §3.16](../../06_Lecture_Notes/modules/M03_Regression.md) explains confounding; [M6 §6.28](../../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md) explains the conditional fixed-design result.
- [Optional ungraded practice](../../07_Labs/Auxiliary_Data/README.md) varies source costs, noise, and bias restrictions.
- [Results](results/README.md), [verification](VERIFICATION.md), and [manifest](manifest.json) record reproducible values, checks, and file identities.

The [source review](../../01_Resources/31_Auxiliary_Data_and_Bias_Geometry/SOURCE_REVIEW.md) distinguishes the paper's retrospective calibrations from these invented calculations. Its PDF remains outside the public repository.
