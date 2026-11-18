# Adaptive Recommendations and Marketing Budgets

By Nathan Yang

Session 13. M8. 170 minutes.

[PDF](S13_Adaptive_Recommendations_and_Marketing_Budgets.pdf) | [LaTeX](S13_Adaptive_Recommendations_and_Marketing_Budgets.tex) | [Session Plan](SESSION_PLAN.md)

## Learning Objectives

- Trace how recommendations affect future training data.
- Evaluate list objectives and customer goals.
- Allocate a fixed marketing budget using marginal response.
- Assess forecast coverage after demand changes and respect delayed outcome information.
- Distinguish estimated response uncertainty from the choice and justification of an objective.

## Related Materials

- [M8 lecture notes](../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md)
- [Runnable small examples](../03_Data_and_Code/Lecture_Examples/session_examples.py)
- [Ethics and regulation](../06_Lecture_Notes/ETHICS_AND_REGULATION.md)
- [Conformal Prediction: Data and Code](../03_Data_and_Code/Conformal_Prediction/README.md)
- [Discount response examples](../03_Data_and_Code/Dose_Response/README.md)
- [Optional dose-response lab](../07_Labs/Dose_Response/README.md)

## Slide 1: Adaptive Recommendations and Marketing Budgets

Marketing Analytics. By Nathan Yang.

## Slide 2: Recommendations Shape the Paths Customers Follow

![A gardener consults a tablet beside familiar and exploratory paths through different fruit trees. The paths represent selected exposure and future opportunities.](assets/recommendation_garden.png)

A gardener consults a tablet beside familiar and exploratory paths through different fruit trees. The paths represent selected exposure and future opportunities.

A frequently used path produces more observations from its existing destinations. Exploration changes which preferences can be learned.

Source: Original conceptual illustration. 05_Slides/assets/PROVENANCE.md.

## Slide 3: An Adaptive Policy

- A model selects exposure using existing interaction histories.
- Customers respond to the displayed options.
- Retraining incorporates those selected responses.

The policy changes the environment that supplies future training data. The update rule and retraining schedule belong in the definition of the intervention.

Source: M8, Section 8.1, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md

## Slide 4: Selected Exposure Creates a Feedback Loop

The diagram describes a policy mechanism rather than an estimated effect.

**Figure description:** Recommendations affect exposure, exposure affects observed responses, and those responses inform subsequent training and recommendations.

[Editable TikZ](../06_Lecture_Notes/figures/M08_feedback.tex)

A popularity loop can concentrate observation among already visible items. Randomized exploration or additional evaluation data can change what the system learns.

Source: M8, Section 8.1, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md

## Slide 5: The Evaluation Horizon Includes Learning

A temporary intervention can persist through subsequent model updates.

**Figure description:** The intervention changes responses during the campaign. A retrained model can preserve information from those responses after the campaign ends.

[Editable TikZ](../06_Lecture_Notes/figures/M08_policy_horizon.tex)

Freezing the model blocks the retraining channel but can leave direct changes in customer behavior. These policies require separate definitions and, where feasible, separate comparisons.

Source: M8, Section 8.1.1, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md

## Slide 6: Demand Changes Can Break Earlier Coverage

| Calibration | Reference | Demand +25 |
| --- | --- | --- |
| Pooled | 90/100 | 5/100 |
| Within Segment | 98/100 | 10/100 |

Same synthetic stores; forecasts and calibration remain fixed.

Demand rises by twenty-five units at every evaluation store. Pooled width remains twenty and average segment width remains 20.8. The calculations describe an imposed change in demand conditional on the same features. Chronological evaluation uses only outcomes observed by the forecast origin, including any label delay. A recent calibration window alone does not restore the ordinary exchangeability guarantee. Different horizons and dependent observations require methods and evaluation appropriate to those settings.

Source: M8 §8.21; complete Python in M7 §7.24.3. ../03_Data_and_Code/Conformal_Prediction/demand_intervals.py

## Slide 7: Customer Goals and Platform Objectives

- Clicks reveal a response within an offered environment.
- Considered preferences can differ from immediate engagement.
- Measure satisfaction, unwanted repetition, and customer-stated goals.

A higher click count can coexist with regret or frustration. A system can combine behavior with explicit goals while recognizing that each measure has its own errors.

Source: M8, Section 8.2.1, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md

## Slide 8: A List Objective

A list combines item relevance with category variety.

$$
J(L)=\sum_{j\in L}s_j+\lambda K(L)
$$

The variety weight $\lambda$ is expressed in the same units as the relevance score.

A weighted sum requires a substantive choice of scales and tradeoffs. A customer replenishing a familiar basket may prefer a different weight from a customer seeking variety.

Source: M8, Section 8.2, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md

## Slide 9: Two Three-Item Lists

| List | Relevance | Categories | Value at 0.30 |
| --- | --- | --- | --- |
| A, B, C | 2.50 | 2 | 3.10 |
| A, C, D | 2.30 | 3 | 3.20 |

Synthetic scores. The lists tie at a variety weight of 0.20.

A and B are coffee, C is tea, and D is fruit. The variety gain trades off against 0.20 of relevance. The values are imposed teaching scores.

Source: M8, Section 8.2, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md

## Slide 10: Model-Based and Experimental Evidence

- A fitted choice model can compare alternative recommenders.
- A randomized perturbation can test predicted response patterns.
- Engagement, retention, revenue, and welfare are distinct outcomes.

The Netflix study discussed in the notes uses a fitted choice model and an experimental check. Its replacement-recommender comparisons are model-based counterfactuals with specific exposure conditions.

Source: M8, Section 8.1.2, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md

## Slide 11: Marketing-Mix Modeling

- Weekly channel spending can have delayed effects.
- Response can saturate at high exposure.
- Spending decisions can respond to anticipated demand.

Trend, seasonality, promotions, and media can move together. A fitted media component requires an identification argument before it is interpreted as a causal contribution.

Source: M8, Section 8.3, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md

## Slide 12: Carryover

A geometric accumulated-exposure measure retains earlier spending.

$$
a_t=s_t+\rho a_{t-1},\qquad 0\leq\rho<1
$$

A 100-unit pulse with $\rho=0.5$ gives 100, 50, 25, and 12.5 in successive periods.

This definition is unnormalized. Under constant spending s, its long-run level is s divided by one minus rho. Coefficients must follow the implementation's normalization.

Source: M8, Section 8.3, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md

## Slide 13: Saturation and the Next Dollar

A concave response has declining marginal contribution.

$$
R(s)=A[1-\exp(-s/b)],\qquad R^{\prime}(s)=\frac{A}{b}\exp(-s/b)
$$

Budget transfers depend on marginal response at the current allocation.

Average response summarizes all earlier units of spending. The next small transfer depends on the local slope, with units of contribution per spending unit.

Source: M8, Section 8.4, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md

## Slide 14: Average and Marginal Returns Can Disagree

Synthetic known response curves. Total spending is fixed at 60 thousand dollars.

**Figure description:** At the starting allocation, A has higher average return while B has higher marginal return. A transfer from A to B increases total contribution.

[Editable TikZ](../06_Lecture_Notes/figures/M08_marginal_returns.tex)

The response curves are 100 times one minus exp(-sA/20) and 80 times one minus exp(-sB/40). The interior allocation equalizes marginal returns.

Source: M8, Section 8.4, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md

## Slide 15: The Fixed-Budget Optimum

Solve equal marginal returns for the imposed curves.

```python
from math import exp, log
budget = 60
a = (log(2.5) + budget/40) / (1/20 + 1/40)
b = budget - a
ma = 5 * exp(-a/20)
mb = 2 * exp(-b/40)
assert abs(ma-mb) < 1e-12
```

The allocation is about 32.22 to A and 27.78 to B, in thousands of dollars.

The closed-form result applies to these known concave curves and an interior fixed-budget optimum. Different constraints or uncertain response functions require a revised calculation.

Source: M8, Section 8.4, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md

## Slide 16: The Objective Changes the Chosen Discount

| Objective | Discount (%) | Profit (USD) | Complaints (%) |
| --- | --- | --- | --- |
| Revenue | 23.2 | 13.898 | 6.38 |
| Profit | 20.0 | 14.000 | 5.00 |
| Profit With Cap | 14.1 | 13.652 | 2.99 |

Known synthetic functions; 0.1-point search grid. The 3% complaint cap is an imposed exercise condition.

The list price is USD 20 and unit cost is USD 4. Known mean profit is 10+0.4a-0.01a squared; expected quantity is profit divided by the unit margin. Revenue is price times quantity. The assumed complaint probability is 0.01+0.0001a squared. All quantities are per eligible customer over the promotion week. The cap is hypothetical and carries no legal or ethical authority. It reduces profit by approximately USD 0.348 relative to the unconstrained profit maximum.

Source: ../03_Data_and_Code/Dose_Response/decision_objectives.py; ../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md

## Slide 17: Estimated Responses and Customer Judgment

- A search over estimated curves also selects estimation noise.
- A proposed intensity needs support and independent policy evaluation.
- Complaint rates leave consent, truthful communication, and refusal to be assessed.

The preceding table optimizes known functions. Estimated curves introduce sampling and modeling uncertainty, especially near boundaries and in poorly represented groups. Customer agency requires reasons for the practice and safeguards that remain binding when profit falls. M9 Section 9.18.1 connects this distinction to Kantian respect and Confucian trustworthiness. The observational mHealth logs do not establish effects of assigned notification intensity.

Source: ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md; ../03_Data_and_Code/Dose_Response/README.md; ../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md

## Slide 18: Coding Exercise: A Policy Objective

- Enumerate three-item lists at several variety weights.
- Solve and independently grid-check the fixed-budget allocation.
- Report the assumptions that change the preferred action.

Run ../03_Data_and_Code/Lecture_Examples/session_examples.py S13. A grid check verifies the numerical optimum within its resolution. It does not establish the imposed response curves as causal estimates.

Source: M8, Section 8.10, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md

## Slide 19: Attention and the Optimization Target

- A free service can require customer time and attention.
- More exposure can benefit advertisers while burdening customers.
- Evaluate voluntary use and customer outcomes alongside engagement.

Tim Wu's Blind Spot discusses attention markets and the difficulty of analyzing exchanges without a monetary user price. A course application should measure time, control, and value rather than equate engagement with welfare.

Source: Tim Wu, Blind Spot: The Attention Economy and the Law (2019). https://scholarship.law.columbia.edu/faculty_scholarship/2029/

## Slide 20: Policy Discussion

- What changes when the recommender learns during the experiment?
- Which outcome measures the customer's stated goal?
- How much uncertainty in response slopes would change the budget?

A robust decision states the learning rule, target outcome, and support for the response function. The best numerical optimizer cannot supply those definitions.

Source: M8, Section 8.7, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md
