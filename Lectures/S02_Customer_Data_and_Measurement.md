# Customer Data and Measurement

By Nathan Yang

Session 02. M2. 170 minutes.

[PDF](S02_Customer_Data_and_Measurement.pdf) | [LaTeX](S02_Customer_Data_and_Measurement.tex) | [Session Plan](SESSION_PLAN.md)

## Learning Objectives

- Construct customer metrics with explicit populations and denominators.
- Separate missing observations, zeros, and unmatched keys.
- Audit changing coverage in mHealth and McBroken.

## Related Materials

- [M2 lecture notes](../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md)
- [Runnable small examples](../03_Data_and_Code/Lecture_Examples/session_examples.py)
- [mHealth audit](../03_Data_and_Code/mHealth/recurring_examples/README.md)
- [McBroken data and code](../03_Data_and_Code/McBroken/README.md)
- [Ethics and regulation](../06_Lecture_Notes/ETHICS_AND_REGULATION.md)

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

Timestamp and meal identifiers are absent from the selected equality fields in the mHealth audit. Dropping all equal records would impose a particular event definition. Preserve source values and add explicit flags.

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

Both numbers use the same observed days. The denominator changes from 120 potential customer-days to 60. These are synthetic counts.

Source: M2, Section 2.1, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md

## Slide 9: Cohorts and Customer Age

- Group customers by a defined entry period.
- Compare the same time since entry.
- Mark later outcomes as unobserved when the horizon has not elapsed.

A recent cohort has no twelve-month outcome yet. Treating that cell as zero creates false attrition. The event defining entry must also remain stable across cohorts.

Source: M2, Section 2.4, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md

## Slide 10: Retention Has a Triangular Support

Synthetic cohort structure. Blank cells have no elapsed follow-up.

**Figure description:** Older cohorts have more observable follow-up periods. The missing upper-age cells for recent cohorts are unobserved rather than zero retention.

[Editable TikZ](../06_Lecture_Notes/figures/M02_cohort_triangle.tex)

Calendar time, tenure, and acquisition cohort are different dimensions. A comparison at fixed tenure avoids giving newer customers shorter opportunities to remain active.

Source: M2, Section 2.4, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md

## Slide 11: McBroken as a Measurement Case

- The records describe ice-cream ordering availability.
- A missing snapshot has an unknown status.
- Restaurant coverage and status recognition can change over time.

Order unavailability can reflect conditions besides a verified mechanical breakdown. A parser must distinguish known available, known unavailable, and unrecognized states. The source audit and data dictionary define those categories.

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

## Slide 14: Coding Exercise: A Data Audit

- Construct a roster-first activity table.
- Report key uniqueness, unmatched rows, and zero-event customers.
- Compare the fixed and conditional activity measures.

Run ../03_Data_and_Code/Lecture_Examples/session_examples.py S02 for the hand-checkable example. For the real case, use the mHealth common.py and m01.py programs in the stated dependency order. Their full source and environment appear in the lecture notes.

Source: M2, Section 2.10, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md

## Slide 15: AI Review of a Parser

- Supply the allowed statuses and a tiny labeled example.
- Require an explicit unknown category for new statuses.
- Compare parsed totals with an independently calculated source total.

A program that treats every unrecognized status as available can create artificial improvements. A counterexample containing a new status tests this failure directly.

Source: M2, Section 2.16.3, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md

## Slide 16: A Data Dictionary for Decisions

- State the unit, key, timing, and units of each variable.
- Record source versions and transformation rules.
- Separate observed values, calculated quantities, and imposed assumptions.

A reader should be able to trace a plotted rate to its numerator and denominator without guessing the meaning of a field name.

Source: M2, Section 2.2, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md

## Slide 17: Privacy and Collection Choices

- Collect the fields needed for the stated decision.
- Retain source permissions and deletion or retention conditions.
- Check whether a linkage increases the risk of identifying a person.

Combining datasets can change what can be inferred even when each file omits names. Data minimization is part of the analytical design, and dataset-specific restrictions remain applicable.

Source: ETHICS_AND_REGULATION.md, M2.

## Slide 18: Measurement Discussion

- Could recorded activity rise because low-activity users disappear?
- Would deleting unmatched days change the target population?
- What evidence would establish a mechanical failure?

Conditioning on observed users can raise activity among those remaining. An inner join changes the observed food-log population. A verified failure diagnosis requires information beyond online ordering availability.

Source: M2, Section 2.16, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md
