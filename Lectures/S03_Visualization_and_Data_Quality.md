# Visualization and Data Quality

By Nathan Yang

Session 03. M2. 170 minutes.

[PDF](S03_Visualization_and_Data_Quality.pdf) | [LaTeX](S03_Visualization_and_Data_Quality.tex) | [Session Plan](SESSION_PLAN.md)

## Learning Objectives

- Choose displays that preserve the intended comparison.
- Explain composition reversals and uncertainty.
- Use domain knowledge to define transparent sensitivity analyses.

## Related Materials

- [M2 lecture notes](../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md)
- [Runnable small examples](../03_Data_and_Code/Lecture_Examples/session_examples.py)
- [Visualization programs and results](../03_Data_and_Code/mHealth/recurring_examples/results/VISUALIZATION.md)
- [Nutrition methods](../01_Resources/12_Nutrition_and_Dietary_Data_Quality/README.md)
- [Ethics and regulation](../06_Lecture_Notes/ETHICS_AND_REGULATION.md)

## Slide 1: Visualization and Data Quality

Marketing Analytics. By Nathan Yang.

## Slide 2: A Campaign Comparison

- Campaign B converts more new and returning customers within each group.
- Its aggregate conversion rate is lower.
- The customer mix determines which comparison the aggregate makes.

The synthetic campaigns differ in the proportion of returning customers. The group rates and the aggregate can move in opposite directions without an arithmetic error.

Source: M2, Section 2.3, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md

## Slide 3: Customer Mix Reverses the Ranking

Synthetic campaigns. Both within-group rates rise by one percentage point.

**Figure description:** Campaign A converts 9% of new and 80% of returning customers. B converts 10% and 81%. The observed rates are 44.5% and 33.7%, while a common 50:50 mix gives 44.5% and 45.5%.

[Editable TikZ](../06_Lecture_Notes/figures/M02_mix_reversal.tex)

Standardization holds group weights fixed. It supplies a common-population descriptive comparison. Causal interpretation would require evidence about assignment and comparability within groups.

Source: M2, Section 2.3, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md

## Slide 4: A Standardized Conversion Rate

Use common customer-group weights $w_g$ for each campaign $c$.

$$
\bar p_c^{\mathrm{std}}=\sum_g w_g p_{cg},\qquad \sum_g w_g=1
$$

Changing the weights changes the population represented by the rate.

The same weights should apply to every campaign in the stated comparison. The group-specific rates can still reflect selection or other differences within groups.

Source: M2, Section 2.3, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md

## Slide 5: Chart Choice Follows the Question

- Aligned positions compare magnitudes.
- Lines compare changes over ordered time.
- Distributions reveal spread and concentration.
- Paired displays preserve within-customer changes.

A mean alone can hide whether a change is widespread or concentrated in a small set of customers. Chart choice should follow the estimand and the decision.

Source: M2, Section 2.5, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md

## Slide 6: A Mean Decline Can Hide a Stable Median

mHealth comparison uses paired customers and a common observation window.

**Figure description:** The empirical distributions and paired changes distinguish the average change from the fraction of customers whose activity changed. A few large declines can move the mean.

[Editable TikZ](../06_Lecture_Notes/figures/M02_logging_distribution.tex)

Distribution spread describes variation among customer outcomes. Uncertainty about an average describes how precisely that average is estimated. They require different displays.

Source: M2, Section 2.14.2, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md

## Slide 7: Uncertainty and Dependence

- Repeated days for one customer share common influences.
- Customer-level resampling preserves each customer history.
- A confidence interval and a percentile range describe different objects.

An independent-day bootstrap treats days as separate sampling units and can understate uncertainty when observations within a user are correlated. A paired difference should also preserve the pairing.

Source: M3, Section 3.6.1, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M03_Regression.md

## Slide 8: Nutrition Knowledge and Measurement

- A recorded food log can omit meals and portions.
- Energy plausibility depends on the measurement instrument and physiology.
- Age, body size, activity, and recording duration affect screening.

These records contain perturbed weights and undocumented source codes. The course example does not treat an undocumented gender code as validated physiological sex or a goal code as measured activity.

Source: M2, Section 2.11, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md

## Slide 9: Sample Restrictions Change the Comparison

mHealth screening alternatives are explicit analysis choices.

**Figure description:** The figure compares sample definitions and their consequences. Structural checks, age restrictions, and imposed calorie ranges serve different purposes.

[Editable TikZ](../06_Lecture_Notes/figures/M02_mhealth_screening.tex)

An imposed calorie range is a sensitivity analysis, not an individual diagnosis of adequate intake. Report the observations retained under each rule and compare the resulting estimands.

Source: M2, Section 2.11, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md

## Slide 10: Energy-Plausibility Screens

- An intake-to-requirement comparison needs defined inputs.
- Unobserved physiological inputs remain missing.
- A hypothetical Goldberg calculation teaches the method separately from the logs.

The Goldberg example in the notes is an explicitly hypothetical scenario. Its inputs should not be silently imputed from undocumented codes. Screening validity depends on the instrument and population.

Source: M2, Section 2.11.1, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md

## Slide 11: Interactive Comparisons

- Keep comparable panels on common scales.
- Display the eligible population and current selection.
- Preserve customers with no recorded days when the estimand includes them.

Changing a slider can change the population, the denominator, and the axis range simultaneously. These changes should remain visible and should be checked against an aggregate table.

Source: M2, Section 2.15, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md

## Slide 12: A Composition Check

Synthetic within-group rates are 9%, 80%, 10%, and 81%.

```python
rates_a = [0.09, 0.80]
rates_b = [0.10, 0.81]
common_a = sum(rates_a) / 2
common_b = sum(rates_b) / 2
observed_b = (2 * rates_b[0] + rates_b[1]) / 3
assert round(common_b - common_a, 2) == 0.01
```

B improves by one point under common weights despite its lower observed aggregate.

The observed B mix assigns two-thirds of its customers to the new-customer group. This calculation is descriptive and uses imposed rates.

Source: M2, Section 2.3, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md

## Slide 13: Coding Exercise: A Chart Audit

- Generate a rate chart from a verified aggregate table.
- Alter the axis range, cohort filter, and denominator one at a time.
- Explain which changes alter the substantive comparison.

The small example runs with ../03_Data_and_Code/Lecture_Examples/session_examples.py S03. The complete mHealth visualization program and interactive chart provide the real-data extension. Verify values separately from rendered readability.

Source: M2, Section 2.14, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md

## Slide 14: A Public-Signal Measurement Problem

- A product can acquire a new page title while demand stays unchanged.
- A single-title series then misses part of its recorded attention.
- Coverage, redirects, and missing dates require an audit.

Pageviews measure attention to selected pages. They do not directly measure paid demand or unique customers. Alias aggregation also needs checks for duplicate coverage.

Source: M2, Section 2.17, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md

## Slide 15: Title Changes and Apparent Declines

The supplied public pageview capture uses observed title histories.

**Figure description:** A single-title view and an alias-aware view differ when the product identity moves across titles. The display retains the distinction between missing coverage and a measured zero.

[Editable TikZ](../06_Lecture_Notes/figures/M02_genai_titles.tex)

The GenAI measurement program validates date and title coverage before calculating a product series. Its saved tables are the values behind the plotted comparison.

Source: M2, Section 2.17.1, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md

## Slide 16: Evidence in a Management Presentation

- State the decision and supported result.
- Show the comparison, units, and denominator.
- Keep the qualification that could change the action beside the claim.

An executive summary can be concise while retaining consequential uncertainty. A useful chart title states the population and comparison rather than a causal claim unsupported by the design.

Source: M2, Section 2.7, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md

## Slide 17: Honest Comparisons

- Keep denominators and scales visible.
- Preserve missing outcomes and relevant subgroup variation.
- Avoid presenting a filtered descriptive pattern as a general causal effect.

A technically correct chart can still communicate a stronger claim than the evidence supports. The reader's likely interpretation matters when selecting a title and comparison.

Source: ETHICS_AND_REGULATION.md, M2-M3.

## Slide 18: Visualization Discussion

- Which customers receive weight in the chart?
- Could sample restrictions reverse the recommendation?
- What does the uncertainty interval include?

The answers should identify whether the unit is an event, a day, or a customer. Sensitivity to inclusion rules can indicate that the decision depends on a narrower population than the headline suggests.

Source: M2, Section 2.8, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md
