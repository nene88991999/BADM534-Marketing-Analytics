# Customer Data and Measurement

By Nathan Yang

Session 02. M2. 170 minutes.

[PDF](S02_Customer_Data_and_Measurement.pdf) | [LaTeX](S02_Customer_Data_and_Measurement.tex) | [Session Plan](SESSION_PLAN.md)

## Learning Objectives

- Construct customer metrics with explicit populations and denominators.
- Separate missing observations, zeros, and unmatched keys.
- Assess changing coverage in mHealth, McBroken, and earnings-call records.
- Preserve requests, confirmations, unknown states, and the reporting cutoff.
- Trace data production and identify the effect of selective access on population claims.

## Related Materials

- [M2 lecture notes](../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md)
- [Runnable small examples](../03_Data_and_Code/Lecture_Examples/session_examples.py)
- [mHealth assessment](../03_Data_and_Code/mHealth/recurring_examples/README.md)
- [McBroken data and code](../03_Data_and_Code/McBroken/README.md)
- [Ethics and regulation](../06_Lecture_Notes/ETHICS_AND_REGULATION.md)
- [Earnings-call worked example](../03_Data_and_Code/Earnings_Calls/README.md)
- [Cancellation Evidence: Data, Code, and Definitions](../03_Data_and_Code/Ontology_and_Evidence/README.md)
- [Digital Usage and Customer Access](../03_Data_and_Code/Digital_Usage/README.md)
- ../07_Labs/AI_Augmented_Learning/README.md
- [Data, Truth, and Norms](../01_Resources/45_Data_Truth_and_Norms/README.md)

## Slide 1: Customer Data and Measurement

Marketing Analytics. By Nathan Yang.

## Slide 2: A Customer-Activity Decision

- An mHealth manager wants to understand reduced recorded use.
- The comparison follows the same eligible customers over time.
- A missing record can reflect nonuse, incomplete observation, or data coverage.

Logging is an observable app behavior. Complete dietary consumption and health outcomes require additional measurement. A metric must state the population represented in each period.

Source: M2, Section 2.1, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md

## Slide 3: A Customer Table

- Begin with the eligible-customer roster.
- Aggregate events to the customer-period level.
- Left join the summaries to the roster.
- Fill zero only when absence has the defined meaning of no recorded event.

Starting from events omits customers with no observed events. Filling a missing nutrition measurement with zero changes its meaning. The roster and observation window establish the denominator.

Source: M2, Section 2.2, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md

## Slide 4: Two Activity Measures

Let $D_i$ be observed logging days and $T$ the calendar days in a common window.

$$
L_i=\frac{D_i}{T},\qquad \bar L=\frac{1}{N}\sum_{i=1}^{N}L_i
$$

Each eligible customer receives equal weight, including customers with no recorded days.

The mean describes recorded use per available calendar day. Averaging only customers with positive D conditions on activity and can obscure declining use.

Source: M2, Section 2.10, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md

## Slide 5: Conditional and Fixed Denominators

mHealth activity depends on who remains in the denominator.

**Figure description:** The figure contrasts a fixed eligible-user denominator with a denominator conditional on observed activity. The two series answer different questions.

[Editable TikZ](../06_Lecture_Notes/figures/M02_logging_denominators.tex)

The fixed cohort supports a comparison of changes in recorded use for the same customers. A conditional mean describes behavior among the customers still observed.

Source: M2, Section 2.14, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md

## Slide 6: Repeated Totals

- An item row can contain a copied daily total.
- Five copies of 1,132.79 sum to 5,663.95.
- The item-calorie sum on that example day is 1,132.7852.

The five-fold inflation follows from repeated measurement fields, not a nutritional mechanism. One daily value can be retained after checking agreement within the user-day. Small rounding differences do not justify ignoring larger discrepancies.

Source: M1, Section 1.8, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M01_Marketing_Analytics_and_Python.md

## Slide 7: Structural Errors and Review Flags

- A duplicate daily key violates a one-row-per-day contract.
- Equal item descriptions can represent repeated servings.
- An extreme value warrants review under a stated rule.

Timestamp and meal identifiers are absent from the selected equality fields in the mHealth assessment. Dropping all equal records would impose a particular event definition. Preserve source values and add explicit flags.

Source: M1, Section 1.8.3, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M01_Marketing_Analytics_and_Python.md

## Slide 8: A Fixed Customer Denominator

Synthetic counts follow all four eligible customers.

```python
days = {'A': 20, 'B': 10, 'C': 0, 'D': 0}
fixed = sum(days.values()) / (4 * 30)
active = [x for x in days.values() if x > 0]
conditional = sum(active) / (len(active) * 30)
assert round(fixed, 4) == 0.25
assert round(conditional, 4) == 0.50
```

The fixed-roster rate is 25%. The active-user rate is 50%.

Suppose the same observed days are divided first by 120 potential customer-days and then by 60. The smaller denominator doubles the measured rate without changing recorded activity.

Source: M2, Section 2.1, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md

## Slide 9: Cohorts and Customer Age

- Group customers by a defined entry period.
- Compare the same time since entry.
- Mark later outcomes as unobserved when the horizon has not elapsed.

A recent cohort has no twelve-month outcome yet. Treating that cell as zero creates false attrition. The event defining entry must also remain stable across cohorts.

Source: M2, Section 2.4, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md

## Slide 10: Retention Has a Triangular Support

Synthetic cohort structure. Blank cells have no elapsed follow-up.

**Figure description:** Older cohorts have more observable follow-up periods. The upper-age cells for recent cohorts remain unobserved because those cohorts have not reached those ages.

[Editable TikZ](../06_Lecture_Notes/figures/M02_cohort_triangle.tex)

Calendar time, tenure, and acquisition cohort are different dimensions. A comparison at fixed tenure avoids giving newer customers shorter opportunities to remain active.

Source: M2, Section 2.4, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md

## Slide 11: McBroken as a Measurement Case

- The records describe ice-cream ordering availability.
- A missing snapshot has an unknown status.
- Restaurant coverage and status recognition can change over time.

Order unavailability can reflect conditions besides a verified mechanical breakdown. A parser must distinguish known available, known unavailable, and unrecognized states. The source assessment and data dictionary define those categories.

Source: M2, Section 2.16, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md

## Slide 12: Coverage Changes the Percentage

McBroken comparisons preserve the observed-store denominator.

**Figure description:** The figure separates changing national coverage from comparisons on common observed support. Missing dates and unrecognized statuses do not become observed availability.

[Editable TikZ](../06_Lecture_Notes/figures/M02_mcbroken_coverage.tex)

A change in the set of included restaurants can change the national share without a within-restaurant change. Common-support comparisons answer a narrower population question.

Source: M2, Section 2.16.1, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md

## Slide 13: Identity Across Files

- A restaurant address is a candidate key that requires checks.
- Standardizing spelling can repair formatting differences.
- Overaggressive matching can merge separate locations.

Track duplicates before and after normalization. Location identity and status measurement are separate tasks. A unique normalized string does not alone prove a unique physical establishment.

Source: M2, Section 2.16.2, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md

## Slide 14: Cancellation Evidence and the Review Queue

The available records support classification, checks, and a bounded service decision.

**Figure description:** A recorded request is classified as a service record and checked for identifiers, time, and cutoff. Accepted requests are compared with dated state evidence. A request without an accepted confirmation enters review; missing confirmation alone does not prove active status.

[Editable TikZ](../06_Lecture_Notes/figures/M01_cancellation_evidence.tex)

The synthetic January 31 cutoff excludes a later confirmation. Keep raw rows, accepted unique events, requests, and the complete subscription roster separate. The operational conditions are implemented directly in Python; an OWL reasoner is outside this implementation.

Source: M1 §1.16 and M2 §2.25. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md

## Slide 15: Which Cancellation Share?

| Evidence or Rule | Count | Denominator |
| --- | --- | --- |
| Accepted unique events | 4 | 8 raw rows |
| Recorded cancellations | 1 | 4 subscriptions |
| Requests counted as completion | 2 | 4 subscriptions |
| Request needing review | r1 | 2 valid requests |

Synthetic January 31 report: the definition changes 25% to 50%.

The four omitted rows are one extra duplicate, one missing timestamp, one confirmation after the cutoff, and one confirmation before its request. The accepted cancellation belongs to s2. Request r1 for s1 remains unresolved in the available evidence. The active observation for s3 is dated; s4 is unknown. Absence of accepted evidence does not establish failure outside the file.

Source: M1 §1.16 and M2 §2.25. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md

## Slide 16: Preserve the Reason for Review

From accepted requests and confirmations at the same cutoff:

```python
completed = {event["request_id"] for event in confirmations}
queue = sorted(set(requests) - completed)
assert queue == ["r1"]
```

Compare the queue with raw records and every exclusion reason.

This short snippet follows validation in the complete assess_cancellations.py program. Run the full example from its folder README. Moving the cutoff to February 2 admits the later confirmation and clears the queue. Keep the original report tied to its original cutoff. The query finds absent confirmations in the supplied records, with no general completeness assumption.

Source: M1 §1.16 and M2 §2.25. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md

## Slide 17: Earnings Calls: Missing Text and Zero Matches

- A communications team wants a complete reading population.
- One supplied call has 53 turns but zero recorded words.
- Retain the call as unknown and preserve firms with no matches.

The roster contains 123 firms, of which 122 have supplied calls. Winmark has no supplied calls. The empty Dollar Tree call cannot establish absence of pricing language. Observed calls with no matches have a different status.

Source: M2, Section 2.19, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md

## Slide 18: Selecting Matches Changes the Denominator

The same 112 positive calls, with two different populations.

**Figure description:** The full observed-call rate is 112/2,325 = 4.82%. Restricting the denominator to 445 calls with any core or broad match produces 25.17%.

[Editable TikZ](../06_Lecture_Notes/figures/M02_calls_denominator.tex)

Start with the call table and aggregate match occurrences before joining. The conditional rate among retrieved documents overstates the overall language frequency when presented without its selected denominator.

Source: M2, Section 2.19, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md

## Slide 19: Coding Exercise: A Data Assessment

- Construct a roster-first activity or call table.
- Separate observed zeros, missing text, and unmatched keys.
- Reconcile the full and match-selected call denominators.

Run assessment.py in ../03_Data_and_Code/Earnings_Calls. Verify 112/2,325 and 112/445; explain why Winmark has an unknown rate and observed no-match firms have zero rates. The customer aggregation exercise supplies a second application of the same roster-first principle.

Source: M2, Section 2.10, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md

## Slide 20: AI Review of a Parser

- Supply the allowed statuses and a tiny labeled example.
- Require an explicit unknown category for new statuses.
- Compare parsed totals with an independently calculated source total.

A program that treats every unrecognized status as available can create artificial improvements. A counterexample containing a new status tests this failure directly.

Source: M2, Section 2.16.3, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md

## Slide 21: A Data Dictionary for Decisions

- State the unit, key, timing, and units of each variable.
- Record source versions and transformation rules.
- Separate observed values, calculated quantities, and imposed assumptions.

A reader should be able to trace a plotted rate to its numerator and denominator without guessing the meaning of a field name.

Source: M2, Section 2.2, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md

## Slide 22: Privacy and Collection Choices

- Collect the fields needed for the stated decision.
- Retain source permissions and deletion or retention conditions.
- Check whether a linkage increases the risk of identifying a person.

Combining datasets can change what can be inferred even when each file omits names. Data minimization is part of the analytical design, and dataset-specific restrictions remain applicable.

Source: ETHICS_AND_REGULATION.md, M2.

## Slide 23: Application Activity and Customer Needs

Geographic application use and individual service outcomes have different observation units.

**Figure description:** Consenting Windows devices contribute category minutes to private geographic indices. Direct evidence on customer tasks separately informs service design.

[Editable TikZ](../06_Lecture_Notes/figures/M02_digital_measurement.tex)

A retailer deciding between digital and assisted service needs evidence about requested tasks, devices, and outcomes. The source observes consenting consumer Windows devices from October 2022 to March 2023. Browser categories mix many tasks. Public indices do not establish an individual customer’s skill, wishes, or authorization.

Source: (Pereira et al., 2026); original course calculations. ../01_Resources/38_Digital_Usage_and_Inclusion/README.md

## Slide 24: Reproduce the Published Calculation

- Equation S1 gives MCI 6.4765 for illustrative device 1.
- The source table prints 4.46; a natural-log calculation reproduces it.
- The private production convention remains unresolved.

The complete Python in M2 §2.27 preserves the source’s rounded category weights and three illustrative minute vectors. Natural logs of positive minutes, with zero at zero minutes, match all three displayed values to two decimals. The weights sum to 0.996. This is a check of the worked example, not a reconstruction of private telemetry. Minute weights also change the aggregate from 3.6733 to 3.6304.

Source: (Pereira et al., 2026); original course calculations. ../01_Resources/38_Digital_Usage_and_Inclusion/README.md

## Slide 25: An Unchanged Price Can Accompany a Higher Bill

Synthetic monthly comparison: 1,000 accounts, matched revenue, sales, and account-months.

**Figure description:** Realized price times average usage equals the average bill. The unit price stays at USD 100 per MWh while usage rises from 1.0 to 1.1 MWh per account-month; the bill rises from USD 100 to USD 110.

[Editable TikZ](../06_Lecture_Notes/figures/M02_price_and_bill.tex)

Ask for a prediction before revealing the product. Changing price to 125 and usage to 0.8 gives a bill of 100. The accounting identity concerns matched customer classes and periods. Causal attribution needs a counterfactual; household affordability also requires resources and needs.

Source: M2 §2.29. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md; ../08_Wiki/pilot/LESSON.md

## Slide 26: A Percentage Needs Its Reference Value

- Reported rounded scores: 78% and 67%.
- Difference: 11 percentage points.
- Relative increase: 11 divided by 67, or about 16.42%.

The Google announcement uses percentage points in its opening and percent in a later result bullet. Preserve the denominator when restating the magnitude. Rounded scores support arithmetic; participant records and a sampling design would be needed to reconstruct uncertainty.

Source: M2, Section 2.29, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md

## Slide 27: Data Have a Production History

Collection, retention, linkage, and access serve institutional purposes.

**Figure description:** Household events pass through four gates before becoming available evidence. Payment and compliance motivate collection; capacity and duties affect retention; identifiers enable linkage; privacy, accountability, and commercial interests shape access.

[Editable TikZ](figures/data_production.tex)

An accurate billing row can coexist with inadequate evidence about household cost incidence. Identify each decision maker and the actual access rule before attributing a motive to missing evidence. Created artifacts have histories and dependencies (Thomasson, 1999, 2014). Data acquire evidential roles through their use and movement (Leonelli, 2015; Leonelli, 2020).

Source: M2 §§2.30–2.31. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md

## Slide 28: The Same Public File Can Support Opposite Worlds

Synthetic: 400 households per world; monthly effects in USD.

**Figure description:** A and B are identical in both releases: 200 households with effects of minus 10. The unreleased 200 have effects of plus 30 in H and minus 10 in L. Full-population means are plus 10 and minus 10.

[Editable TikZ](figures/selected_evidence.tex)

Hold all other causes of bills fixed so the prior bill equals the current no-project bill. All current bills are recorded internally in both worlds. The example isolates release selection and grants identification within each constructed population. Weighting cannot recover zero-inclusion strata. Full code, positive-inclusion comparisons, and support bounds appear in M2 §2.31.

Source: M2 §§2.30–2.31. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md

## Slide 29: Measurement Discussion

- Could recorded activity rise because low-activity users disappear?
- Would deleting unmatched days change the target population?
- What evidence would establish a mechanical failure?

Conditioning on observed users can raise activity among those remaining. An inner join changes the observed food-log population. A verified failure diagnosis requires information beyond online ordering availability.

Source: M2, Section 2.16, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md
