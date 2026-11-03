# Causal Comparisons and Policy Evaluation

By Nathan Yang

Session 10. M6. 170 minutes.

[PDF](S10_Causal_Comparisons_and_Policy_Evaluation.pdf) | [LaTeX](S10_Causal_Comparisons_and_Policy_Evaluation.tex) | [Session Plan](SESSION_PLAN.md)

## Learning Objectives

- Explain the identifying comparison in difference-in-differences, RD, and IV.
- Evaluate a policy under selected exposure and support restrictions.
- Assess whether a comparison group is suitable for the McBroken policy question.

## Related Materials

- [M6 lecture notes](../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md)
- [Runnable small examples](../03_Data_and_Code/Lecture_Examples/session_examples.py)
- [McBroken policy analysis](../03_Data_and_Code/McBroken/README.md)
- [Ethics and regulation](../06_Lecture_Notes/ETHICS_AND_REGULATION.md)
- [Earnings-call worked example](../03_Data_and_Code/Earnings_Calls/README.md)

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

**Figure description:** The figure distinguishes the proposed policy timing from restaurant coverage and observed availability. A national time change alone mixes the policy with other changes.

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

## Slide 16: Spillovers Change the Outcome Comparison

Synthetic store network with effects beyond assigned units.

**Figure description:** A treated store can attract customers from a nearby comparison store. The difference between stores then mixes the direct effect with displacement.

[Editable TikZ](../06_Lecture_Notes/figures/M06_spillovers.tex)

The chain-wide outcome may change less than the treated-store outcome. Assignment and outcome aggregation should follow the managerial decision.

Source: M6, Section 6.10, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 17: Coding Exercise: Policy Value

- Reproduce raw rates and inverse-propensity values.
- Check them using within-group averages.
- Set one logging probability to zero and explain the missing comparison.

Run ../03_Data_and_Code/Lecture_Examples/session_examples.py S10. A correct implementation flags unsupported target actions. Silently dropping the unsupported group changes the target population.

Source: M6, Section 6.11, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 18: Information and Exposure

- A recommendation can draw attention to an item.
- A personalized endorsement can also change beliefs.
- Separate interventions can identify these channels.

The MovieLens experiment discussed in the notes distinguishes recommendation and exposure-only conditions. The relevant outcome and information treatment should be stated before attributing a response to personalization.

Source: M6, Section 6.10.1, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 19: A Policy Value for Whom?

- Clicks and sales can rise while customer value falls.
- A causal estimate concerns the outcome that was actually measured.
- Record refusal, completion, and customer time when procedures change.

A valid causal effect on conversion does not identify the welfare effect without information about customer values and costs. The next measurement should address the missing part of the decision.

Source: ETHICS_AND_REGULATION.md, M6.

## Slide 20: Causal-Design Discussion

- What would the treated group have experienced without the policy?
- Which group or action lacks comparable support?
- What institutional evidence strengthens the proposed comparison?

A causal interpretation rests on the comparison and assumptions. A flexible estimator does not supply a missing assignment mechanism or recover outcomes outside support.

Source: M6, Section 6.11, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md
