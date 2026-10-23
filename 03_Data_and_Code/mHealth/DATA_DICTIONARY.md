# Food-Log Variables

The source covers recorded food consumption and daily summaries in 2016. Field names are retained where possible. A food-entry row and a user-day row have different observation units. Calorie fields use the source's reported food-energy units, conventionally dietary kilocalories; their measurement protocol is unavailable.

## Fields in Both Files

| Field | Definition and Treatment |
| --- | --- |
| `Userid` | Replacement user identifier, beginning with `L`. Stable across the two files. The original numeric identifier and the private transformation key are not distributed. |
| `Fancydate` | Original recorded day, retained as a date-time string. Source observations use midnight; timezone and logging-event timing are undocumented. |
| `Age_at_2016_01_01` | Completed years of age on January 1, 2016, calculated once from the original birthday. Fixed across a user's records. Invalid or missing birthdays yield missing age. It is not age at each observation. |
| `Currentweight` | Source current weight plus the documented random offset, rounded to three decimals. Source units are inferred to be pounds from the BMI/height relationship. Nonpositive and missing source values retain their original status. |
| `Budgetcalories` | Source calorie budget. The rule by which the app sets or updates the budget is undocumented. |
| `Foodcalories` | Source daily food-calorie total. Repeated on food-entry rows. Aggregate at the user-day level after checking consistency. |
| `Exercisecalories` | Source daily exercise-calorie measure. Its estimation method and missing-versus-zero semantics are undocumented. |
| `Weightchange` | Original categorical code. The inspected prefix contains 0, 1, and 2. The meanings and time window are undocumented, so do not assign gain, maintenance, or loss labels without supporting documentation. This is not a numeric weight difference. |

## Additional Food-Entry Fields

| Field | Definition and Treatment |
| --- | --- |
| `Name` | Original food description. Examples in the inspected source include generic foods and descriptions with portion sizes. |
| `Productname` | Original product, brand, or restaurant label where supplied. A missing label does not establish that an item is unbranded. |
| `Category` | Original food-category label. The complete category-assignment procedure is unavailable. |
| `Baseunits` | Source numeric field associated with the food amount. Its conversion rule is undocumented. |
| `Quantity` | Source recorded quantity. Interpret jointly with the measurement fields. Do not automatically multiply `Calories` by this value. |
| `Measureid` | Original measurement-unit code. |
| `Measurename` | Original measurement-unit label, such as cup, serving, ounce, or tablespoon. Numeric amounts with different units are not directly additive. |
| `Calories` | Source food-entry calorie value. The file alone does not establish whether quantity scaling has already been applied. Reconcile candidate aggregations before interpreting the daily sum. |
| `Breakfastcalories`, `Lunchcalories`, `Dinnercalories`, `Snackcalories` | Original daily meal-calorie totals repeated on food rows. Some source values are missing. These are not row-specific meal indicators. |
| `Startweight` | Source starting-weight field plus the same user-day offset as current weight. Its starting date is undocumented. |
| `Minweight`, `Maxweight` | Source minimum- and maximum-weight fields plus the same user-day offset. Their calculation windows are undocumented. These are not recalculated extrema of the released noisy series. |
| `Goalweight` | Source goal weight plus the same user-day offset. The perturbation may produce small day-to-day movements even if the original goal was unchanged. |
| `Gender` | Original numeric code. Its coding scheme is undocumented. |
| `Heightinches` | Source height field, labeled in inches. |
| `Goalplan` | Original numeric goal-plan code. Its coding scheme is undocumented. |
| `Bmi_from_noisy_weight` | `703 * Currentweight / Heightinches**2`, rounded to three decimals. Calculated only for positive weight and height. This replaces the original BMI. It is an altered teaching variable. |

## Weight Perturbation

For user `i` and recorded day `t`, the additive offset is `a_i + e_it`, where `a_i` and `e_it` each follow a uniform distribution from -0.5 to 0.5 source weight units. A private keyed pseudorandom function fixes the draws so duplicate records and the two files receive the same offset. Weight fields of at least two units receive that offset, then are rounded to three decimals. The resulting absolute change is at most 1.0005 units, including rounding. For a source value `0 < w < 2`, the export uses `w * (1 + offset/2)` without rounding, which keeps these unusually small positive values positive. These source values require investigation before analysis. Nonpositive and missing values retain their source status. The private key is retained by the instructor and is absent from GitHub.

For fields of at least two units, the common offset preserves differences between weight fields within a user-day before rounding, such as current minus goal weight. Changes across days include differences in the added day offsets. Repeated unchanged source weights can consequently show small changes. This perturbation does not provide differential privacy or a guarantee against re-identification.

## Removed and Replaced Fields

`Birthday` and the daily file's `Image` field are removed. The original `Age` is replaced with the explicitly dated fixed-age field. Original user IDs are replaced. `Currenteer` is omitted because its construction is undocumented and a weight-based calculation could retain information about the unperturbed weight. Original `Bmi` is replaced with the calculation from perturbed weight. References to the provider in text labels are standardized to mHealth. Food descriptions, categories, calorie fields, quantities, and source dates are otherwise preserved.

## Missing Values and Interpretation

Blank cells represent missing values in the CSV export. Existing zero and negative values are preserved; their validity depends on the particular field and analysis. No food entries or users are filtered merely for preparation of this teaching copy. The complete manifest gives released row counts, user counts, date bounds, and checksums.

The two source files do not include a full data dictionary, a sample-construction program, treatment assignment, exposure logs, or an account roster. A missing calendar day is unobserved. Regression, ranking accuracy, and weight histories alone do not establish the causal effect of a recommendation or a health intervention.
