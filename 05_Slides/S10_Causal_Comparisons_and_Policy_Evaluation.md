# Causal Comparisons and Policy Evaluation

By Nathan Yang

Session 10. M6. 170 minutes.

[PDF](S10_Causal_Comparisons_and_Policy_Evaluation.pdf) | [LaTeX](S10_Causal_Comparisons_and_Policy_Evaluation.tex) | [Session Plan](SESSION_PLAN.md)

## Learning Objectives

- Explain the identifying comparison in difference-in-differences, RD, and IV.
- Evaluate a policy under selected exposure and support restrictions.
- Assess whether a comparison group is suitable for the McBroken policy question.
- Estimate and assess a nonlinear discount response with explicit confounding and overlap conditions.
- Distinguish covariate adjustment, project exposure, and the population represented by a convenient sample.

## Related Materials

- [M6 lecture notes](../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md)
- [Runnable small examples](../03_Data_and_Code/Lecture_Examples/session_examples.py)
- [McBroken policy analysis](../03_Data_and_Code/McBroken/README.md)
- [Ethics and regulation](../06_Lecture_Notes/ETHICS_AND_REGULATION.md)
- [Earnings-call worked example](../03_Data_and_Code/Earnings_Calls/README.md)
- [Discount response examples](../03_Data_and_Code/Dose_Response/README.md)
- [Optional dose-response lab](../07_Labs/Dose_Response/README.md)
- [Bad Controls and Project Exposure](../01_Resources/44_Bad_Controls_and_Project_Exposure/README.md)
- [Optional Research-Design Practice](../07_Labs/Bad_Controls/README.md)

## Slide 1: Causal Comparisons and Policy Evaluation

Marketing Analytics. By Nathan Yang.

## Slide 2: A Repair-Policy Question

- A policy may change the cost of restoring restaurant availability.
- A national before-after change also includes common shocks.
- The target is the change attributable to the policy over a defined horizon.

The McBroken setting motivates a causal question. The supplied panel does not by itself establish a valid untreated comparison for a policy affecting the same environment broadly.

Source: M6, Section 6.16, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 3: Difference-in-Differences

Subtract the comparison group's change from the treated group's change.

$$
\widehat\tau=(\bar Y_{T,post}-\bar Y_{T,pre})-(\bar Y_{C,post}-\bar Y_{C,pre})
$$

Parallel untreated trends connect the observed changes to a causal effect.

Different starting levels can be compatible with the design. The assumption concerns untreated changes, not identical outcome levels.

Source: M6, Section 6.8, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 4: The Counterfactual Trend

Synthetic outcomes. Treated sales rise 120 to 150 and comparison sales 100 to 110.

**Figure description:** The implied untreated treated-group outcome is 130. The observed treated outcome is 150, giving a 20-unit difference.

[Editable TikZ](../06_Lecture_Notes/figures/M06_did.tex)

The dashed path is an implied counterfactual. A treatment-specific demand shock at the same time would challenge the interpretation.

Source: M6, Section 6.8, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 5: Design Checks

- Examine pre-treatment outcomes and institutional timing.
- Consider anticipation, spillovers, and changing composition.
- Match the comparison group to the policy's untreated counterfactual.

A nonsignificant pre-trend test does not establish parallel trends. With staggered adoption and heterogeneous effects, the choice of comparison groups and aggregation becomes especially important.

Source: M6, Section 6.8, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 6: McBroken and the Comparison Group

A policy-analysis design requires a credible untreated comparison.

**Figure description:** The proposed policy timing, restaurant coverage, and observed availability represent separate objects. A national time comparison combines the policy with other contemporaneous changes.

[Editable TikZ](../06_Lecture_Notes/figures/M06_mcbroken_policy.tex)

The course case retains missing dates and unknown statuses. Those measurement issues should be addressed before interpreting an apparent policy break.

Source: M6, Section 6.16, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 7: Fewer Mentions Can Leave Incidence Unchanged

Observed calls around February 27, 2024; same comparison firms in both windows.

**Figure description:** In 90-day windows excluding the event day, the same 27 comparison firms have 27 calls each side. Occurrences fall from five to two, while two positive calls each side imply 7.41%.

[Editable TikZ](../06_Lecture_Notes/figures/M06_calls_windows.tex)

The event is Wendy's dated public clarification of digital-menu intentions. In all available comparison calls, incidence falls from 2/27 to 2/34 as coverage expands. The firm group name does not establish an untreated counterfactual.

Source: M6, Section 6.18, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 8: A Public Event Does Not Assign Treatment

- Define the window, event-day exclusion, and observed-call denominator.
- Compare common firms and alternative window lengths.
- A causal claim needs exposure, a counterfactual, and a specified outcome.

Run event_windows.py for 60-, 90-, and 120-day comparisons with call and firm weights. A change in communication is distinct from a change in pricing behavior or customer outcomes. Matching coverage removes one composition difference, not concurrent shocks.

Source: M6, Section 6.18, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 9: Regression Discontinuity

- Eligibility can change at a known score threshold.
- Nearby units require continuity of other outcome determinants.
- The resulting effect is local to the cutoff and compliance behavior.

Manipulation of the score and discontinuities in other policies threaten the comparison. Bandwidth and functional form should be assessed within the design.

Source: M6, Section 6.9, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 10: Instrumental Variables

- The instrument shifts treatment or price.
- Exclusion restricts its other paths to the outcome.
- Relevance alone does not establish exclusion.

Under the appropriate binary-treatment conditions, IV can identify a local effect for compliers. The interpretation depends on the assignment mechanism and monotonicity, as well as the first stage.

Source: M6, Section 6.9, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 11: Recommendation Logs Select Exposure

- Frequent buyers may usually see product A.
- Occasional buyers may usually see product B.
- Their raw click rates compare different customer populations.

A logged outcome is observed after a selected display. A policy comparison must account for the distribution of customers and actions that generated those observations.

Source: M6, Section 6.7.1, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 12: Exposure Adjustment Reverses the Ranking

Synthetic randomized logging within frequent and occasional buyer groups.

**Figure description:** Raw click rates favor A, 56% versus 41%. A common equally weighted population favors B, 45% versus 40%.

[Editable TikZ](../06_Lecture_Notes/figures/M06_exposure_reversal.tex)

The constructed logging design gives A probability 0.90 for frequent buyers and 0.10 for occasional buyers. B receives the complement. The common-population comparison holds customer mix fixed.

Source: M6, Section 6.7.2, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 13: Inverse-Propensity Policy Value

Weight each observed outcome by target-policy probability over logging probability.

$$
\widehat V(\pi)=\frac{1}{n}\sum_i\frac{\pi(A_i\mid X_i)}{p_0(A_i\mid X_i)}Y_i
$$

The denominator counts every eligible logged opportunity.

Identification requires the relevant exchangeability condition and positive logging support wherever the target policy acts. A randomized logging policy can supply known assignment probabilities.

Source: M6, Section 6.7.1, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 14: A Common-Population Calculation

Synthetic clicks and logging probabilities identify the two policy values.

```python
n = 1000
value_a = (270 / 0.90 + 10 / 0.10) / n
value_b = (25 / 0.10 + 180 / 0.90) / n
raw_a = 280 / 500
raw_b = 205 / 500
assert (value_a, value_b) == (0.40, 0.45)
```

The raw ranking and policy-value ranking disagree.

An independent check averages the two group-specific response rates under equal population weights. The small-probability cells receive large weights and contribute substantial uncertainty.

Source: M6, Section 6.7.2, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 15: Support and Weight Concentration

- An action never shown to a group has no observed outcome there.
- Large weights amplify a small number of records.
- Clipping changes the estimator and its bias-variance tradeoff.

Zero support cannot be repaired by increasing a weight. Weight-concentration summaries are diagnostics and do not replace a variance calculation that respects dependence.

Source: M6, Section 6.7.2, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 16: A Zero Slope Can Conceal a Discount Response

Synthetic profit peaks at a 20% discount. Uniform randomization gives a zero linear projection slope.

**Figure description:** Discount varies from 0 to 40 percentage points. Known profit rises from USD 10 to USD 14 and returns to USD 10. A dashed horizontal line at USD 12.67 shows the population linear projection under uniform randomization.

[Editable TikZ](../06_Lecture_Notes/figures/M06_discount_response.tex)

Eligibility precedes the offer and profit is measured per customer over the promotion week. The projection is an exact uniform-randomization benchmark, separate from the observational sample. A constant slope does not characterize the decision-relevant shape.

Source: ../03_Data_and_Code/Dose_Response/README.md; ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 17: Adjustment for Selected Discount Intensity

Observed customer types affect both discount assignment and profit. The target gives each type equal weight.

$$
\xi_i=\widehat m(A_i)+\frac{\widehat f_A(A_i)}{\widehat\pi(A_i\mid X_i)}\{Y_i-\widehat\mu(X_i,A_i)\}
$$

Cross-fit the nuisance models, then smooth the adjusted outcomes over dose. Causal interpretation requires adequate support and measured confounders.

The outcome model predicts profit conditional on dose and observed type. The treatment model estimates a conditional density, measured per percentage point. m averages the outcome model over the target population; f_A averages the conditional density. The population identity is doubly robust when either nuisance model is correct under identification and regularity conditions. Correct nuisance models alone do not establish calibrated confidence intervals.

Source: Kennedy et al., https://arxiv.org/abs/1507.00747v3; ../03_Data_and_Code/Dose_Response/README.md; ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 18: Conditional Support and Effective Sample Size

The weak-overlap sample has effective sample size near 2,400. Important dose-by-type comparisons remain nearly absent.

**Figure description:** Two panels share dose and density scales. Blue solid and orange dashed curves identify the two customer types. Lower assignment noise separates their concentrated dose distributions.

[Editable TikZ](../06_Lecture_Notes/figures/M06_dose_overlap.tex)

Both datasets have 2,400 customers and the same known causal response. Assignment noise SD changes from 0.9 to 0.22 on the logit scale. The reference weak-overlap sample has almost constant weights near one-half; rare observations with enormous weights are absent. Effective sample size measures concentration among observed weights and cannot establish conditional support. Weight clipping changes the residual correction and can remove double robustness when the outcome model is wrong.

Source: ../03_Data_and_Code/Dose_Response/README.md; ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 19: Pointwise Intervals and Curve-Wide Coverage

| Models Correct | Mean RMSE (USD) | Pointwise (%) | All 29 (%) |
| --- | --- | --- | --- |
| Both | 0.099 | 90.7 | 42.5 |
| Outcome | 0.058 | 85.7 | 23.5 |
| Density | 0.312 | 96.7 | 60.0 |
| Neither | 1.335 | 6.4 | 0.0 |

200 synthetic samples; conditional HC0 pointwise intervals. Whole-grid coverage has no nominal 95% guarantee.

Each sample has 2,400 customers. RMSE equally weights the 29 doses from 6 to 34, then averages across samples. Pointwise coverage first averages the indicators across samples at each dose and then averages doses. All 29 means that every pointwise interval contains its target in the same sample. The procedure holds fitted adjusted outcomes fixed and omits first-stage uncertainty and fixed-bandwidth smoothing bias. The fixed two-point bandwidth and 200 repetitions define a finite-design evaluation.

Source: ../03_Data_and_Code/Dose_Response/README.md; ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 20: Partial Pooling and Store-Level Bias

Randomized synthetic discounts. Pooling reduces aggregate error; Store 4 favors its separate estimate.

**Figure description:** Known, separate, and partially pooled curves for Store 0 with 12 customers and Store 4 with 300. Both panels share discount and profit scales. Shrinkage improves the small store and worsens the displayed large store.

[Editable TikZ](../06_Lecture_Notes/figures/M06_store_pooling.tex)

Twenty stores in four regions supply 2,188 observations. Discounts are randomized independently within each store. Five-fold validation over observed outcomes selects regional and store ridge penalties. Equal-store RMSE is USD 0.512 with partial pooling, USD 0.936 with separate fits, and USD 0.968 with complete pooling. Store 4 has separate RMSE USD 0.249 and partial RMSE USD 0.550. This is one simulated dataset, with no general dominance or interval-calibration claim.

Source: ../03_Data_and_Code/Dose_Response/README.md; ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 21: Spillovers Change the Outcome Comparison

Synthetic store network with effects beyond assigned units.

**Figure description:** A treated store can attract customers from a nearby comparison store. The difference between stores then mixes the direct effect with displacement.

[Editable TikZ](../06_Lecture_Notes/figures/M06_spillovers.tex)

The chain-wide outcome may change less than the treated-store outcome. Assignment and outcome aggregation should follow the managerial decision.

Source: M6, Section 6.10, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 22: Coding Exercise: Policy Value

- Reproduce raw rates and inverse-propensity values.
- Check them using within-group averages.
- Set one logging probability to zero and explain the missing comparison.

Run ../03_Data_and_Code/Lecture_Examples/session_examples.py S10. A correct implementation flags unsupported target actions. Silently dropping the unsupported group changes the target population.

Source: M6, Section 6.11, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 23: Information and Exposure

- A recommendation can draw attention to an item.
- A personalized endorsement can also change beliefs.
- Separate interventions can identify these channels.

The MovieLens experiment discussed in the notes distinguishes recommendation and exposure-only conditions. The relevant outcome and information treatment should be stated before attributing a response to personalization.

Source: M6, Section 6.10.1, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 24: A Policy Value for Whom?

- Clicks and sales can rise while customer value falls.
- A causal estimate concerns the outcome that was actually measured.
- Record refusal, completion, and customer time when procedures change.

A valid causal effect on conversion does not identify the welfare effect without information about customer values and costs. The next measurement should address the missing part of the decision.

Source: ETHICS_AND_REGULATION.md, M6.

## Slide 25: Inclusion and Exclusion Can Both Fail

The treatment-affected covariate must be related to its untreated evolution.

**Figure description:** Synthetic treatment raises X by two. The true total effect is 4. Dropping information gives 5.5 and conditioning on the realized X gives minus 2. Baseline W supports reconstruction of the untreated trend.

[Editable TikZ](../06_Lecture_Notes/figures/M06_counterfactual_covariate.tex)

The example is a linear population calculation, not an implementation of the general Caetano et al. estimator. The imposed overlap and observed baseline information justify imputation. Flexible fitting would not replace those assumptions. See M6 §6.40 for the complete program.

Source: ../01_Resources/44_Bad_Controls_and_Project_Exposure/README.md

## Slide 26: Project Uncertainty Within 2020–2025

- 2023: an official cancellation follows inadequate community support.
- 2025: large-load risks and project disruptions receive explicit attention.
- Trace commitments and cost recovery before labeling donors unexposed.

The Cascade Locks announcement documents cancellation, not stranded utility costs. LBNL’s January 2025 brief and Ohio Power’s July 2025 tariff establish contemporary attention to financial exposure. Data Center Watch documents substantial disruption late in the period but lacks a consistent historical all-project denominator. The records do not establish contamination of actual donors.

Source: ../01_Resources/44_Bad_Controls_and_Project_Exposure/README.md

## Slide 27: Opening Can Follow Economic Exposure

The baseline and donor population change the comparison.

**Figure description:** Four synthetic utility price histories yield comparisons of 10, 7, and 4 dollars per MWh under different baselines and donors.

[Editable TikZ](../06_Lecture_Notes/figures/M06_project_windows.tex)

Before commitments, the completed-project increment is 10. Equal canceled and unexposed donor weights subtract 3. Starting after commitments leaves the additional operating increment of 4. Canceled-project costs are constant over the shorter interval, so they add no change to that particular DiD. Actual donor weights and dated obligations are required for the paper-specific assessment.

Source: ../03_Data_and_Code/Bad_Controls/README.md

## Slide 28: Design the Study Before Selecting the Dataset

- Define the intervention, population, outcome, and horizon.
- Retain canceled and pending proposals when the question concerns the pipeline.
- Require an unexposed baseline and a defensible donor group.

Recent operating records may omit the stages that generate the burden of interest. Selection can cause an internal-validity problem when the counterfactual is wrong and an external-validity problem when a valid selected-population effect is generalized. A stated reason for a time window does not establish either validity condition. New data and precise estimation can coexist with a fundamentally inadequate comparison.

Source: ../01_Resources/44_Bad_Controls_and_Project_Exposure/README.md

## Slide 29: Causal-Design Discussion

- What would the treated group have experienced without the policy?
- Which group or action lacks comparable support?
- What institutional evidence strengthens the proposed comparison?

A causal interpretation rests on the comparison and assumptions. A flexible estimator does not supply a missing assignment mechanism or recover outcomes outside support.

Source: M6, Section 6.11, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md
