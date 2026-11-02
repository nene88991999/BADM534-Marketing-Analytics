# Experiments and Incremental Value

By Nathan Yang

Session 09. M6. 170 minutes.

[PDF](S09_Experiments_and_Incremental_Value.pdf) | [LaTeX](S09_Experiments_and_Incremental_Value.tex) | [Session Plan](SESSION_PLAN.md)

## Learning Objectives

- Define a treatment, assignment unit, outcome, and estimand.
- Calculate an intention-to-treat effect, uncertainty, and contribution.
- Plan power and use prior outcomes to improve precision.

## Related Materials

- [M6 lecture notes](../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md)
- [Runnable small examples](../03_Data_and_Code/Lecture_Examples/session_examples.py)
- [mHealth experiment planning](../03_Data_and_Code/mHealth/recurring_examples/m06.py)
- [Ethics and regulation](../06_Lecture_Notes/ETHICS_AND_REGULATION.md)

## Slide 1: Experiments and Incremental Value

Marketing Analytics. By Nathan Yang.

## Slide 2: Comparable Markets Receive Different Assignments

![A merchant sends packages across two separate bridges to comparable villages. Distinct pennants represent treatment assignments.](assets/experiment_bridges.png)

A merchant sends packages across two separate bridges to comparable villages. Distinct pennants represent treatment assignments.

Random assignment balances potential outcomes in expectation. The comparison still requires well-defined outcomes, complete measurement, and an appropriate unit of assignment.

Source: Original conceptual illustration. Lectures/assets/PROVENANCE.md.

## Slide 3: An Email-Campaign Decision

- Eligible customers receive either an email or no email.
- Measure purchases over a fixed response window.
- The decision concerns contribution per assigned customer.

Assignment remains the denominator even when some customers do not open the email. Conditioning on opening selects a post-assignment group.

Source: M6, Section 6.1, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 4: Potential Outcomes

For eligible customer $i$, define outcomes with and without assignment.

$$
\tau=\E[Y_i(1)-Y_i(0)]
$$

Each customer has one observed outcome under the realized assignment.

The average treatment effect concerns the specified eligible population and treatment implementation. The assignment design supplies the comparison needed to estimate the missing counterfactual mean.

Source: M6, Section 6.1, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 5: Selection Creates an Alternative Explanation

Randomized assignment is distinct from engagement-driven email opening.

**Figure description:** A shared determinant can influence both treatment receipt and the outcome, creating a noncausal path. Random assignment removes that systematic selection path under the design.

[Editable TikZ](../06_Lecture_Notes/figures/M06_dag.tex)

Control variables should follow the causal structure and timing. Conditioning on a variable affected by treatment can change the estimand or introduce selection.

Source: M6, Section 6.2, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 6: Email Assignment and Purchase

| Assigned Group | Customers | Purchases | Rate |
| --- | --- | --- | --- |
| Email | 1,000 | 130 | 13% |
| Control | 1,000 | 100 | 10% |

Synthetic experiment. Each customer has one binary outcome.

The difference is three percentage points. Relative to a 10% control rate, that equals a 30% relative increase. The two descriptions use different denominators.

Source: M6, Section 6.4, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 7: An Assignment-Effect Estimate

Compare purchase rates across all assigned customers.

$$
\widehat\tau=\frac{130}{1000}-\frac{100}{1000}=0.03
$$

The estimated effect is three additional purchases per 100 assigned customers.

This is an intention-to-treat comparison under the stated randomized design. An opened-email comparison would use a different selected population.

Source: M6, Section 6.4, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 8: Sampling Uncertainty

Use an independent-group approximation for the synthetic binary outcomes.

$$
\widehat{\operatorname{SE}}=\sqrt{\frac{.13(.87)}{1000}+\frac{.10(.90)}{1000}}\approx .0143
$$

An approximate 95% interval is 0.21 to 5.79 percentage points.

The interval uses a large-sample normal approximation and independent customer assignments. It does not include systematic outcome measurement errors or interference.

Source: M6, Section 6.4, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 9: Contribution and Decision Uncertainty

- An extra purchase contributes 40 dollars.
- Delivery costs 0.50 dollars per assigned customer.
- Estimated incremental contribution is 0.70 dollars per customer.

The same transformation of the effect interval gives approximately -0.42 to 1.82 dollars. The calculation assumes no additional discount cost and fixed contribution per additional purchase.

Source: M6, Section 6.4, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 10: The Experiment Calculation

Reproduce the effect and its contribution implication.

```python
from math import sqrt
p1, p0, n = 0.13, 0.10, 1000
effect = p1 - p0
se = sqrt(p1*(1-p1)/n + p0*(1-p0)/n)
interval = (effect - 1.96*se, effect + 1.96*se)
profit = 40 * effect - 0.50
assert round(profit, 2) == 0.70
```

The point estimate is positive while the contribution interval includes losses.

If treatment changes basket size, returns, or margins, purchase incidence alone no longer gives the contribution effect. Measuring contribution directly can better match the decision.

Source: M6, Section 6.4, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 11: Power Begins With the Useful Effect

- Choose the smallest effect that could change the action.
- Use the expected outcome variance and assignment unit.
- Halving the target effect approximately quadruples sample size.

At baseline probability 0.10, a two-point effect, two-sided 5% level, and 80% power, a common-variance normal approximation gives 3,528 customers per arm.

Source: M6, Section 6.5, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 12: Implementation Checks

- Reconcile assigned counts and intended allocation.
- Check missing outcomes and tracking by assignment.
- Preserve the planned outcome horizon.
- Investigate exclusions that depend on treatment response.

A randomization protocol does not prevent differential tracking failures. Sample-ratio discrepancies can reveal implementation problems. Chance covariate imbalance alone does not invalidate a correctly implemented randomization.

Source: M6, Section 6.6, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 13: Prior Outcomes and Precision

Adjust the outcome using a pre-treatment measure $X$.

$$
Y_i^{\mathrm{adj}}=Y_i-\theta(X_i-\bar X)
$$

A predictive baseline can reduce residual variation while preserving the assignment comparison.

CUPED uses a pre-treatment covariate and an appropriately specified adjustment. The variance reduction does not create treatment variation or repair selection into treatment.

Source: M6, Section 6.15, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 14: mHealth Baseline Activity Improves Precision

Planning calculation uses historical user-level variance and a five-point target.

**Figure description:** The detectable-change curves compare unadjusted and prior-period-adjusted logging outcomes. The indicated sample sizes are 788 and 397 independent users per arm under the stated approximation.

[Editable TikZ](../06_Lecture_Notes/figures/M06_cuped_precision.tex)

These are power-planning implications of observed historical variances, not a realized intervention effect. The future population, outcome process, and assignment need to match the planning conditions.

Source: M6, Section 6.15, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 15: Coding Exercise: An Experiment Plan

- Compute the synthetic email effect and interval.
- Change contribution, delivery cost, and the target effect.
- Specify an mHealth recommendation assignment with a fixed user denominator.

Run ../03_Data_and_Code/Lecture_Examples/session_examples.py S09. The mHealth experiment-planning scripts use historical variation and an explicitly simulated zero-effect assignment. Their output must remain labeled as planning and simulation.

Source: M6, Section 6.13, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 16: Interference and Assignment Units

- Customers can share offers or affect one another.
- Stores can divert purchases from nearby locations.
- The assignment unit should reflect the likely spillovers.

If one treated store gains by taking business from a comparison store, the store-level difference can exceed the chain-wide gain. Cluster assignment changes both interpretation and precision.

Source: M6, Section 6.10, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 17: A Treatment Arm Needs a Defensible Design

- Random assignment identifies a comparison.
- The content of each treatment still affects the customers who receive it.
- Include customer outcomes, refusal, and stopping conditions.

Randomization does not establish that a deceptive or harmful interface is acceptable. Separate analytical identification from the substantive and regulatory evaluation of each proposed treatment.

Source: ETHICS_AND_REGULATION.md, M6.

## Slide 18: Experiment Discussion

- Would a conversion gain cover the campaign cost?
- What changes if only email openers enter the analysis?
- Which guardrail outcome could reverse the rollout decision?

Contribution uncertainty remains consequential even with a positive purchase effect. Returns, satisfaction, and service burden can alter the decision. The outcome set should reflect the intervention.

Source: M6, Section 6.11, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md
