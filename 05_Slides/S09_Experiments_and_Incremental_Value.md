# Experiments and Incremental Value

By Nathan Yang

Session 09. M6. 170 minutes.

[PDF](S09_Experiments_and_Incremental_Value.pdf) | [LaTeX](S09_Experiments_and_Incremental_Value.tex) | [Session Plan](SESSION_PLAN.md)

## Learning Objectives

- Define a treatment, assignment unit, outcome, and estimand.
- Calculate an intention-to-treat effect, uncertainty, and contribution.
- Plan power and use prior outcomes to improve precision.
- Explain the information conditions supporting a fixed research allocation.

## Related Materials

- [M6 lecture notes](../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md)
- [Runnable small examples](../03_Data_and_Code/Lecture_Examples/session_examples.py)
- [mHealth experiment planning](../03_Data_and_Code/mHealth/recurring_examples/m06.py)
- [Ethics and regulation](../06_Lecture_Notes/ETHICS_AND_REGULATION.md)
- [AI workflow calculations](../03_Data_and_Code/AI_Workflows/README.md)
- [Consumer Agency Literature and Clustering](../03_Data_and_Code/Consumer_Agency_Literature/README.md)
- [AI Experimentation and Pricing](../01_Resources/16_AI_Experimentation_and_Pricing/README.md)
- [Human and Synthetic Evidence](../03_Data_and_Code/Auxiliary_Data/README.md)
- [Auxiliary Data: Optional Practice](../07_Labs/Auxiliary_Data/README.md)
- [Agent Workflow Evaluation and Practice](../07_Labs/Agent_Workflows/README.md)
- [Statistical Inference: Code and Results](../03_Data_and_Code/Statistical_Inference/README.md)
- [Statistical Evidence: Optional Practice](../07_Labs/Statistical_Inference/README.md)

## Slide 1: Experiments and Incremental Value

Marketing Analytics. By Nathan Yang.

## Slide 2: Comparable Markets Receive Different Assignments

![A merchant sends packages across two separate bridges to comparable villages. Distinct pennants represent treatment assignments.](assets/experiment_bridges.png)

A merchant sends packages across two separate bridges to comparable villages. Distinct pennants represent treatment assignments.

Random assignment balances potential outcomes in expectation. The comparison still requires well-defined outcomes, complete measurement, and an appropriate unit of assignment.

Source: Original conceptual illustration. 05_Slides/assets/PROVENANCE.md.

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

## Slide 11: Power Begins with the Useful Effect

- Choose the smallest effect that could change the action.
- Use the expected outcome variance and assignment unit.
- Halving the target effect approximately quadruples sample size.

At baseline probability 0.10, a two-point effect, two-sided 5% level, and 80% power, a common-variance normal approximation gives 3,528 customers per arm.

Source: M6, Section 6.5, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 12: Fixed and Adaptive Research Designs

- Known features and variances determine information at each profile.
- A fixed allocation attains the leading minimum cost at high accuracy in the linear model.
- Unknown bias structure or revenue earned during learning changes the design problem.

Theorem 1 concerns worst-case coefficient MSE under the stated linear Gaussian model, with known response and bias dictionaries and constant source costs. It does not rule out lower-order finite-accuracy differences. Nonlinear response models can make information depend on unknown coefficients. The paper separately treats pilot estimation of noise variances while preserving known feature dictionaries. Compare this target with adaptive campaign profit and causal effects on purchases; M6 Section 6.28 supplies the interpretation.

Source: Jasin, Lin, and Zhang (2026), Bias Geometry and the Value of Auxiliary Data. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7734298

## Slide 13: Implementation Checks

- Reconcile assigned counts and intended allocation.
- Check missing outcomes and tracking by assignment.
- Preserve the planned outcome horizon.
- Investigate exclusions that depend on treatment response.

A randomization protocol does not prevent differential tracking failures. Sample-ratio discrepancies can reveal implementation problems. Chance covariate imbalance alone does not invalidate a correctly implemented randomization.

Source: M6, Section 6.6, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 14: Prior Outcomes and Precision

Adjust the outcome using a pre-treatment measure $X$.

$$
Y_i^{\mathrm{adj}}=Y_i-\theta(X_i-\bar X)
$$

A predictive baseline can reduce residual variation while preserving the assignment comparison.

CUPED uses a pre-treatment covariate and an appropriately specified adjustment. The variance reduction does not create treatment variation or repair selection into treatment.

Source: M6, Section 6.15, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 15: mHealth Baseline Activity Improves Precision

Planning calculation uses historical user-level variance and a five-point target.

**Figure description:** The detectable-change curves compare unadjusted and prior-period-adjusted logging outcomes. The indicated sample sizes are 788 and 397 independent users per arm under the stated approximation.

[Editable TikZ](../06_Lecture_Notes/figures/M06_cuped_precision.tex)

These are power-planning implications of observed historical variances, not a realized intervention effect. The future population, outcome process, and assignment need to match the planning conditions.

Source: M6, Section 6.15, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 16: Model and Library Contributions

Synthetic counts: 100 assigned tasks per condition; common rubric and resource limits.

**Figure description:** Without the library, passing tasks rise from 60% with the earlier model to 65% with the newer model. With the library, they rise from 70% to 85%. The library gain increases from 10 to 20 percentage points.

[Editable TikZ](../06_Lecture_Notes/figures/M06_ai_factorial.tex)

The interaction is ten percentage points. Moving from the initial condition to the newer model with the library improves the imposed rate by twenty-five points. Independent assignments, valid reference outcomes, and fresh tasks would be required for an empirical causal comparison. These counts are constructed, with unfinished tasks counted as failures.

Source: Marketing Analytics Lecture Notes, M6 §6.19.

## Slide 17: An Interaction Calculation

The four rates are imposed teaching inputs.

```python
q00, q01, q10, q11 = 0.60, 0.70, 0.65, 0.85
model_alone = q10 - q00
library_after_model = q11 - q10
interaction = (q11-q10) - (q01-q00)
assert round(interaction, 2) == 0.10
assert round(model_alone + library_after_model, 2) == 0.25
```

A joint gain does not uniquely allocate the interaction to either component.

Run factorial.py to reproduce both paths to the joint change using exact rational arithmetic. Randomize at the team or project level when outputs share personnel, prompts, or helper code. Record actual cost alongside pass rates and resource ceilings.

Source: M6 §6.19. ../03_Data_and_Code/AI_Workflows/factorial.py

## Slide 18: A Fixed Model and Four Workflows

- Cross explicit information with independent development feedback.
- Reset each run and randomize cell order within repetitions.
- Freeze the program before evaluating August.
- Count failed and missing outputs among assigned attempts.

M6 §6.29 defines q_cf as the probability of a valid output for a fixed task and model configuration. The interaction is (q11-q01)-(q10-q00). Its sign describes complementarity for that outcome. Repeated runs on one task measure conditional variation; generalization requires additional task families. A trace suggests a diagnosis, while a controlled intervention identifies the effect of a component.

Source: Li and coauthors, Agent Harness Engineering: A Survey, §§8–9. Original course applications: ../01_Resources/35_Agent_Workflow_Evaluation/README.md ../03_Data_and_Code/Agent_Workflows/README.md

## Slide 19: Coding Exercise: An Experiment Plan

- Compute the factorial contrasts alongside the email effect.
- Change contribution, delivery cost, and the target effect.
- Specify an mHealth recommendation assignment with a fixed user denominator.

Run ../03_Data_and_Code/Lecture_Examples/session_examples.py S09. The mHealth experiment-planning scripts use historical variation and an explicitly simulated zero-effect assignment. Their output must remain labeled as planning and simulation. The AI_Workflows folder supplies complete standard-library calculations with synthetic inputs.

Source: M6, Section 6.13, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 20: Interference and Assignment Units

- Customers can share offers or affect one another.
- Stores can divert purchases from nearby locations.
- The assignment unit should reflect the likely spillovers.

If one treated store gains by taking business from a comparison store, the store-level difference can exceed the chain-wide gain. Cluster assignment changes both interpretation and precision.

Source: M6, Section 6.10, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 21: Assign Stores, Observe Customers

Synthetic promotion: balanced store assignment and equal store sizes.

**Figure description:** Twenty stores receive a promotion and twenty receive control. Each store has twenty customer outcomes with a shared store shock. Comparing store means preserves the equal-weight customer contrast.

[Editable TikZ](../06_Lecture_Notes/figures/M06_store_assignment.tex)

The effect is zero for every customer. Store shocks are independent across stores, and individual shocks are independent within and across stores conditional on the store shock. Mean net contribution is 100 dollars and marginal variance is 800 dollars squared. Equal customer counts make store and customer point estimates identical. The number of independent stores determines the contribution of shared shocks to uncertainty.

Source: M6 §6.30. ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 22: A Zero-Effect Promotion

| Calculation | Estimate (Dollars) | p-Value |
| --- | --- | --- |
| Customer Rows | 4.334 | 0.0287 |
| Store Means | 4.334 | 0.3446 |

First simulated experiment; within-store correlation 0.3; true effect zero.

This is repetition zero from seed 20261125, retained without selecting a favorable result. Both are two-sided Welch calculations, with observation units differing. Customer-row inference permits unequal arm variances but omits within-store covariance. The store-mean standard error is 4.524 dollars, compared with 1.977 dollars for customer rows. A single experiment motivates evaluating the full procedure under repeated known-null experiments.

Source: M6 §6.30. ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 23: Dependence Changes False Discoveries

Store means retain rejection rates near the nominal 5% level in this simulation.

**Figure description:** Across four correlations, customer-row rejection rates rise from 5.2% to 55.0%. Store-mean rates remain between 4.7% and 4.975%. Bars show Monte Carlo Wilson intervals.

[Editable TikZ](../06_Lecture_Notes/figures/M06_null_calibration.tex)

Each correlation uses 4,000 newly generated experiments, 40 stores, 20 customers per store, balanced assignment, and one prespecified test. The true effect is zero. At correlation 0.3, 1,796 customer-row tests reject compared with 188 store-mean tests. The theoretical variance ratio to independent customer sampling is 1+(m-1)rho, equal to 6.7 here. Gaussian shocks, equal sizes, complete outcomes, and independent stores define the simulation. The Wilson bars measure Monte Carlo uncertainty, not effect uncertainty or customer spread.

Source: M6 §6.30. ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 24: A Treatment Arm Needs a Defensible Design

- Random assignment identifies a comparison.
- The content of each treatment still affects the customers who receive it.
- Include customer outcomes, refusal, and stopping conditions.

Randomization does not establish that a deceptive or harmful interface is acceptable. Separate analytical identification from the substantive and regulatory evaluation of each proposed treatment.

Source: ETHICS_AND_REGULATION.md, M6.

## Slide 25: Follow Purchases Through Returns

- Pressure and self-assurance can produce different purchase and return patterns.
- Prespecify the eligible population and both outcome horizons.
- For cancellation, measure intent, completion, and subsequent charges.

The verified abstract of the randomized online-retailing study reports stronger purchase responses alongside more returns under pressure nudges. Its full text remains unavailable in the collection. The directional result motivates balanced outcomes; exact effects and implementation details require the complete paper. A cancellation study should define eligibility at the initial request and compare lawful designs. See M6 Section 6.20.

Source: https://doi.org/10.1177/00222437231180494

## Slide 26: From Experiments to Generative Decisions

- Within-campaign comparisons can supervise a model that proposes new messages.
- The learned ranking inherits the outcome used to define success.
- Evaluate new proposals in their deployment setting.

Angelopoulos, Lee, and Misra train a language-model improver using historical experimental comparisons. The causal interpretation is tied to the randomized comparison and measured outcome. Transfer to new content requires new evidence.

Source: https://leekevin.io/caLM.pdf

## Slide 27: Human Review and Customer Evidence

- Check factual claims and consequential terms before deployment.
- Record customer understanding and the ability to refuse.
- A robust commercial payoff still requires a justified objective.

Causal Alignment includes human selection and acceptability checks. Their existence is material to a fair critique; their coverage remains a substantive question. Farrell, Korganbekova, and Misra address robustness to a changed deployment distribution, with a selected payoff.

Source: https://leekevin.io/caLM.pdf https://arxiv.org/abs/2609.07633

## Slide 28: Experiment Discussion

- Would a conversion gain cover the campaign cost?
- What changes if only email openers enter the analysis?
- Which customer outcome could reverse the rollout decision?

Contribution uncertainty remains consequential even with a positive purchase effect. Returns, satisfaction, and service burden can alter the decision. The outcome set should reflect the intervention.

Source: M6, Section 6.11, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md
