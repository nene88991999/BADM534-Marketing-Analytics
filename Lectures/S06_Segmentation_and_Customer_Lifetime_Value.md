# Segmentation and Customer Lifetime Value

By Nathan Yang

Session 06. M4. 170 minutes.

[PDF](S06_Segmentation_and_Customer_Lifetime_Value.pdf) | [LaTeX](S06_Segmentation_and_Customer_Lifetime_Value.tex) | [Session Plan](SESSION_PLAN.md)

## Learning Objectives

- Define similarity using economically meaningful customer features.
- Evaluate segment stability and future outcomes.
- Calculate lifetime value with consistent timing and distinguish retention concepts.

## Related Materials

- [M4 lecture notes](../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md)
- [Runnable small examples](../03_Data_and_Code/Lecture_Examples/session_examples.py)
- [mHealth segments](../03_Data_and_Code/mHealth/recurring_examples/m04.py)
- [Subscription cohort examples](../03_Data_and_Code/GenAI_Demand/README.md)
- [Ethics and regulation](../06_Lecture_Notes/ETHICS_AND_REGULATION.md)

## Slide 1: Segmentation and Customer Lifetime Value

Marketing Analytics. By Nathan Yang.

## Slide 2: A Retention-Support Decision

- A service team can support only some customers.
- High baseline value and responsiveness to support are separate quantities.
- Segments should correspond to feasible service decisions.

A segment with high predicted value may have little incremental response to outreach. The support decision needs the change in future contribution caused by the action, net of its costs.

Source: M4, Section 4.9, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md

## Slide 3: Customer Features at a Common Date

- Recency is time since the last eligible event.
- Frequency counts events in a fixed window.
- Monetary value uses sales or contribution over that window.

Customers with unequal exposure histories can appear different because of observation time. The feature definition must specify eligibility and whether returns affect sales or transaction counts.

Source: M4, Section 4.5, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md

## Slide 4: K-Means and Similarity

Choose $K$ centers for transformed customer features $z_i$.

$$
\min_{\mu,c}\sum_i\left\|z_i-\mu_{c(i)}\right\|^2
$$

Scaling the features changes the distance and can change the segments.

K-means minimizes within-cluster squared Euclidean distance. A standardized feature receives a different implicit weight from the raw variable. The transformation is a substantive choice.

Source: M4, Section 4.5, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md

## Slide 5: Units Change the Nearest Customer

Synthetic customers have unchanged spending and frequency records.

**Figure description:** Changing spending from dollars to hundreds of dollars reverses which customer is nearest to A. Frequency then receives more relative weight.

[Editable TikZ](../06_Lecture_Notes/figures/M04_scaling.tex)

Raw distances compare A=(100,1), B=(110,9), and C=(200,1). The example changes only the spending scale. The preferred business representation depends on the service decision.

Source: M4, Section 4.5, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md

## Slide 6: Evaluating a Segmentation

- Inspect segment size, profile, and actionable differences.
- Compare stability across seeds, samples, and periods.
- Evaluate outcomes that did not mechanically define the clusters.

Within-cluster dispersion declines as K rises. A high-spending cluster will have high spending by construction when spending is an input. Later outcomes provide a more informative descriptive check.

Source: M4, Section 4.6, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md

## Slide 7: mHealth Segments Use Earlier Histories

Eligible users have at least 30 observed days before July 1.

**Figure description:** Earlier logging frequency and recorded breadth distinguish clusters. Later logging does not enter the clustering inputs.

[Editable TikZ](../06_Lecture_Notes/figures/M04_mhealth_segments.tex)

The representation uses first-half logging fraction, mean category breadth, and mean calorie-share variety. K=3 is imposed for the comparison. The scaler and centers use only the earlier window.

Source: M4, Section 4.11, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md

## Slide 8: Later Logging by Earlier Segment

| Segment | Users | Prior Fraction | Later Fraction |
| --- | --- | --- | --- |
| 1 | 126 | 0.426 | 0.338 |
| 2 | 90 | 0.759 | 0.594 |
| 3 | 115 | 0.870 | 0.654 |

mHealth denominators use 182 earlier and 184 later calendar days.

Later absence contributes zero observed days for eligible users. The figures describe persistence in recorded activity. They are not contractual retention rates or effects of a service intervention.

Source: M4, Section 4.11, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md

## Slide 9: Lifetime Value and Payment Timing

Value future contribution conditional on remaining active.

$$
\operatorname{CLV}=\sum_{t=1}^{T}\frac{\Pr(\text{active at }t)m_t}{(1+d)^t}-a
$$

The period for margin $m_t$, discounting $d$, and retention must agree.

The acquisition cost a occurs at time zero. This convention excludes immediate contribution. If a current-period contribution is included, it must be added explicitly.

Source: M4, Section 4.7, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md

## Slide 10: A Stationary Subscription

Suppose monthly retention is $r$ and monthly contribution is $m$.

$$
\operatorname{CLV}=\frac{mr}{1+d-r}-a
$$

With $m=60$, $d=0.01$, $a=50$, and $r=0.80$, CLV is 178.57 dollars.

The formula assumes constant retention and conditional margin and an infinite horizon, with the first payment one month later. It follows from a convergent geometric series.

Source: M4, Section 4.7, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md

## Slide 11: Retention Has Nonlinear Value

Synthetic stationary model. Monthly margin, discounting, and acquisition cost stay fixed.

**Figure description:** CLV rises increasingly rapidly with retention. Increasing monthly retention from 0.80 to 0.90 raises value from about 178.57 to 440.91 dollars.

[Editable TikZ](../06_Lecture_Notes/figures/M04_clv.tex)

The high-retention region places more weight on distant contributions. Uncertainty about the persistence of retention and margins can dominate the valuation.

Source: M4, Section 4.7, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md

## Slide 12: A Finite-Sum Check

Compare the closed form with 2,000 future monthly payments.

```python
m, r, d, a = 60, 0.8, 0.01, 50
closed = m * r / (1 + d - r) - a
finite = sum(m * r**t / (1+d)**t
             for t in range(1, 2001)) - a
assert abs(closed - finite) < 1e-8
```

Both calculations give approximately 178.57 dollars.

Matching the two expressions checks the payment convention and arithmetic. It does not establish constant retention as a valid model of a real relationship.

Source: M4, Section 4.7, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md

## Slide 13: Cancellation and a Logging Gap

- A subscription may record cancellation directly.
- A 30-day logging gap is an operational activity event.
- Observation can end before a defined event occurs.

Right censoring preserves the distinction between no observed event by the end of follow-up and an event at the last observation. A logging gap is not proof of permanent departure or paid cancellation.

Source: M4, Section 4.13, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md

## Slide 14: The Event Definition Changes Survival

mHealth time-to-gap analysis uses a stated gap definition and observation horizon.

**Figure description:** Survival tracks time until a defined logging gap. The risk set and right censoring determine which histories contribute at each time.

[Editable TikZ](../06_Lecture_Notes/figures/M04_logging_survival.tex)

Changing the gap length changes the event being measured. Survival of recorded activity should remain separate from contractual renewal in financial calculations.

Source: M4, Section 4.13, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md

## Slide 15: Endpoint and Continuous Retention

- Endpoint retention allows customers to leave and return.
- Continuous retention requires uninterrupted presence.
- Acquisition can include first entry, return, or switching.

A starting-provider cohort is fixed at the initial period. The same-provider, other-provider-only, and no-paid-provider states distinguish platform retention from category participation. Multiple providers require explicit overlap handling.

Source: M4, Section 4.14, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md

## Slide 16: Coding Exercise: Segments and Value

- Fit feature scaling and segments on an earlier period.
- Describe a later period without refitting the groups.
- Vary assumed paid retention in a separate CLV calculation.

The small CLV calculation is ../03_Data_and_Code/Lecture_Examples/session_examples.py S06. The real mHealth m04.py example and GenAI cohort program keep behavioral measurements separate from imposed financial inputs.

Source: M4, Section 4.11, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md

## Slide 17: Retention and Effective Cancellation

- High paid retention can reflect satisfaction or difficulty leaving.
- Measure cancellation completion and unwanted subsequent charges.
- Evaluate customer value alongside the seller's lifetime-value objective.

A customer who prefers cancellation can remain subscribed because of friction. The consumer-value comparison requires independent evidence about that preference and the available procedure.

Source: M8, Section 8.14, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md

## Slide 18: Retention Discussion

- What action differs across the proposed segments?
- Does a customer's absence represent churn or censoring?
- Which retention assumption changes the support decision?

A useful recommendation identifies the response to intervention as well as baseline value. Cluster membership alone does not establish the effectiveness of differentiated support.

Source: M4, Section 4.9, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md
