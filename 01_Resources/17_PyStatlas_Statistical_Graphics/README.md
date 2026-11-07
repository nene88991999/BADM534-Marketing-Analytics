# PyStatlas and Statistical Graphics for Marketing Decisions

Thierry Warin's [PyStatlas](https://warint.github.io/pystatlas/) organizes 61 Python graphics into 12 statistical families. Its useful teaching principle is to choose a display from the question and statistical object: a customer distribution, a paired change, a conditional prediction, or uncertainty about an estimate. Each example combines a chart, explanation, source data attribution, and downloadable code. The course adaptations use marketing decisions and the Illinois palette.

## Course Applications

| Course Connection | Selected Graphics | Managerial Question and Interpretation |
| --- | --- | --- |
| M2: Customer Data and Visualization | ECDF, raincloud, paired observations, estimation plot | How much do customers differ, and how much did the same customers change? Show the comparison directly and distinguish spread from uncertainty. |
| M3: Regression | Coefficient plots, odds ratios, predicted probabilities, residual diagnostics | How does a model translate customer characteristics into an outcome? State units, conditioning, support, and whether comparisons have causal identification. |
| M4: Segmentation and CLV | PCA, silhouette, Kaplan–Meier curves and risk tables | Are segments stable and useful for a decision? How long do customers remain active when observation ends at different times? |
| M5: Text Measurement | Bland–Altman agreement | Do two coding procedures agree on a measurement scale? High correlation can coexist with a systematic coding difference. |
| M6: Experiments | Estimation plots, interaction means, bootstrap intervals, power curves | What effect is large enough to change a decision? Preserve randomization and sampling units; report the effect and uncertainty. |
| M7: Prediction | Calibration, precision–recall, learning curves, PDP/ICE | Which predictions support capacity planning or a targeting rule? Ranking, probability accuracy, and intervention effects answer distinct questions. |
| M8: Current Applications | Decomposition, forecasting, seasonal displays | Which part of a demand pattern is predictable at the decision date? Hold out later observations and distinguish descriptive components from causal channels. |
| M9: Marketing Dialectics | Model explanations and subgroup comparisons | What does an explanation establish about a model, and what ethical premise is needed to justify its use? A feature attribution does not supply permission to exploit a vulnerability. |

Spatial weights, Moran plots, and local clustering maps are optional extensions for the McBroken setting. A restaurant is a point location; adjacency between French administrative regions in the original example is not an appropriate default neighborhood for restaurants. Define the geographic unit and weights before computing spatial association.

## Two Executed Course Examples

1. **Paired Customer Spending, M2 §2.22 and Session 3.** Eight synthetic customers have widely dispersed spending levels but changes between $4 and $6. Their mean change is $5. The paired standard error is $0.267 under the stated sampling interpretation. Dropping the covariance gives $18.402, showing how the wrong independence assumption changes uncertainty. This before/after comparison does not identify a campaign effect.
2. **Ranking and Purchase Probabilities, M7 §7.23 and Session 11.** Two imposed score systems rank the same 80 synthetic customers identically. Both have AUC 0.803; their Brier scores are 0.175 and 0.21855. Their predicted purchase totals are 36 and 40, against 36 observed. The same ranking can therefore support different inventory decisions.

Both examples have [input CSVs, complete Python programs, tests, and output tables](../../03_Data_and_Code/Statistical_Graphics/README.md). The notes reproduce the programs in full. Two editable TikZ figures connect the comparison to its economic meaning.

## AI-Assisted Coding Exercise

Give the coding assistant a managerial question and a small data dictionary before requesting a chart. Require it to state the observation unit, target population, denominator, units, comparison, and uncertainty interpretation. Ask for a table containing every plotted value. Then change one analytical feature, such as breaking customer pairs or applying a strictly increasing transformation to scores, and predict which statistics should remain unchanged. Compare that prediction with the executed output.

Suggested prompt: “Use the supplied customer-level file. Compare spending changes for the same customers. Validate unique identifiers and complete pairs. Return the change table, the mean change, the uncertainty assumption, and code with relative paths. Explain which result would change if the pairing were lost. Preserve missing values until their treatment is justified.” This activity is a practice suggestion; assessment-specific AI rules govern assessed work.

## Source and Review Scope

The reference snapshot is commit `ec4bb401e1c8a6622fa5da196e05c4df0b5e0b41`, retrieved November 7, 2026. The [catalog](catalog.json) records all 61 chart titles, module connections, source paths, and hashes. Eighty reference text files are retained in Dropbox, including every chart script, category metadata, build files, license, and dependency/data records. Every downloaded file matches its Git blob. Nine selected scripts received a full code reading; the remaining entries received metadata cataloguing and syntax parsing. No upstream program was executed.

The [source review](SOURCE_REVIEW.md) identifies interpretation and reproducibility issues. The [wiki design notes](WIKI_PATTERNS.md) distill the site's navigation and code presentation. Software is MIT licensed; underlying datasets have their own terms. The public repository contains original course materials, attribution, metadata, and the license. Downloaded reference copies remain in `local_sources/`, excluded from Git.
