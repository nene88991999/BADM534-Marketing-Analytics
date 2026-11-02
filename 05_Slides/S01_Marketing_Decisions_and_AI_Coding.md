# Marketing Decisions and AI-Assisted Coding

By Nathan Yang

Session 01. M1. 170 minutes.

[PDF](S01_Marketing_Decisions_and_AI_Coding.pdf) | [LaTeX](S01_Marketing_Decisions_and_AI_Coding.tex) | [Session Plan](SESSION_PLAN.md)

## Learning Objectives

- Specify an action, observation unit, information set, and outcome horizon.
- Translate a small marketing calculation into readable Python.
- Verify generated code using identities and counterexamples.

## Related Materials

- [M1 lecture notes](../06_Lecture_Notes/modules/M01_Marketing_Analytics_and_Python.md)
- [Runnable small examples](../03_Data_and_Code/Lecture_Examples/session_examples.py)
- [mHealth dictionary](../03_Data_and_Code/mHealth/DATA_DICTIONARY.md)
- [Ethics and regulation](../06_Lecture_Notes/ETHICS_AND_REGULATION.md)

## Slide 1: Marketing Decisions and AI-Assisted Coding

Marketing Analytics. By Nathan Yang.

## Slide 2: A Merchant Chooses a Market

![A merchant consults a laptop and ledger while two boats travel toward different customer markets. The landscape represents a choice under incomplete information.](assets/decision_river.png)

A merchant consults a laptop and ledger while two boats travel toward different customer markets. The landscape represents a choice under incomplete information.

A useful analysis connects the available evidence to a feasible decision. Different markets can require different products, margins, and forecasts.

Source: Original conceptual illustration. 05_Slides/assets/PROVENANCE.md.

## Slide 3: A Renewal Offer

- A subscription firm can contact 5,000 eligible customers.
- The decision concerns incremental contribution over the next 30 days.
- Past spending, consent, and account history are available before contact.

The contact budget constrains the action. A high predicted renewal rate can reflect customers who would renew without an offer. The target must include the additional contribution caused by contact.

Source: M1, Section 1.1, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M01_Marketing_Analytics_and_Python.md

## Slide 4: Analytical Questions

- Description: how often do customers renew?
- Prediction: who is likely to renew?
- Causal effect: how does an offer change renewal?
- Decision: which contacts generate positive incremental contribution?

The same customer records can support different analytical objects. Predictive performance evaluates forecasts under the represented conditions. A targeting policy also needs the untreated comparison and relevant costs.

Source: M1, Section 1.1, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M01_Marketing_Analytics_and_Python.md

## Slide 5: Incremental Contribution

For account $i$, compare renewal under an offer and no offer.

$$
\Delta\pi_i=m_i\{p_i(1)-p_i(0)\}-c_i
$$

Contribution $m_i$ and contact cost $c_i$ are dollars per account over the stated horizon.

The formula assumes that the offer cost can be summarized by c and that contribution already deducts relevant variable costs. A discount paid on every treated purchase requires an additional cost term.

Source: M1, Section 1.1, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M01_Marketing_Analytics_and_Python.md

## Slide 6: Response and Incremental Value

Synthetic accounts. Contribution is 100 dollars and contact cost is 3 dollars.

**Figure description:** Account A has treated renewal probability 0.91 and incremental contribution -2 dollars. Account B has probability 0.50 and contribution 7 dollars.

[Editable TikZ](../06_Lecture_Notes/figures/M01_response_vs_value.tex)

A rises from 0.90 to 0.91. B rises from 0.40 to 0.50. The untreated probabilities explain the reversal. These probabilities are imposed teaching inputs.

Source: M1, Section 1.1, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M01_Marketing_Analytics_and_Python.md

## Slide 7: The Observation Unit

- A product line, order, customer, and customer-month are different units.
- The key identifies one row at the intended level.
- Aggregation changes the weights used in an average.

A customer with five order lines receives five times the weight of a customer with one line in a line-level mean. Define whether the managerial comparison concerns orders or equally weighted customers.

Source: M1, Section 1.2, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M01_Marketing_Analytics_and_Python.md

## Slide 8: Python Objects and Order Totals

Three synthetic product lines belong to two orders.

```python
lines = [('A', 2, 10), ('A', 1, 5), ('B', 1, 12)]
orders = {}
for order, quantity, price in lines:
    orders[order] = orders.get(order, 0) + quantity * price
total = sum(orders.values())
aov = total / len(orders)
assert (total, aov) == (37, 18.5)
```

Check: total sales are 37 dollars and average order value is 18.50 dollars.

The tuple stores an order ID, a quantity, and a unit price. The dictionary accumulates sales by order. The denominator is two orders. Dividing by the three lines gives average line sales.

Source: M1, Section 1.3, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M01_Marketing_Analytics_and_Python.md

## Slide 9: Functions and Data Contracts

- Inputs have names, types, units, and allowed missing values.
- A function returns a defined output and an exception report.
- Returns, canceled orders, and duplicate lines need explicit rules.

A numeric-looking string requires conversion before arithmetic. A negative quantity may be a legitimate return. A rule should preserve a trace from the original record to its inclusion or exclusion.

Source: M1, Section 1.3, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M01_Marketing_Analytics_and_Python.md

## Slide 10: A Duplicate Lookup Doubles Sales

Synthetic join. One 40-dollar order matches two customer records.

**Figure description:** The original order has one row. A duplicate customer lookup produces two joined rows and an apparent 80-dollar total.

[Editable TikZ](../06_Lecture_Notes/figures/M01_join_multiplication.tex)

A many-to-one relationship requires unique customer keys in the lookup. Check key uniqueness before merging and reconcile sales afterward.

Source: M1, Section 1.2, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M01_Marketing_Analytics_and_Python.md

## Slide 11: An AI Coding Request

- Return one row per order and an exceptions table.
- Treat negative quantities as returns under the stated rule.
- Verify the 37-dollar example and reject missing order IDs.
- Explain each transformation before adding the next step.

A useful request specifies analytical behavior and acceptance criteria. The assistant can propose an implementation while the analyst remains responsible for the observation unit and sample rules.

Source: M1, Section 1.5, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M01_Marketing_Analytics_and_Python.md

## Slide 12: Verification With Counterexamples

- A duplicate lookup must trigger a failed key check.
- An unmatched customer must remain visible in the assessment.
- An empty input needs an explicit result.
- Order totals must reconcile with eligible product lines.

These checks test properties that can fail even when code runs. Repeating the program with the same input confirms reproducibility but does not independently establish correctness.

Source: M1, Section 1.5, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M01_Marketing_Analytics_and_Python.md

## Slide 13: mHealth Records

- Food entries describe recorded items on observed user-days.
- The separate daily table covers only part of the food-log history.
- Reported daily calories repeat across item rows.

The released records replace user identifiers and birthdays and perturb weight values. The source daily total is distinct from the sum of item calories. Neither is a direct measure of complete usual intake.

Source: M1, Section 1.8, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M01_Marketing_Analytics_and_Python.md

## Slide 14: Join Choice Changes the Sample

Released mHealth cohort: 76,804 observed user-days.

**Figure description:** A left join retains all 76,804 user-days. Only 37,634 match the separate daily file, leaving 39,170 unmatched.

[Editable TikZ](../06_Lecture_Notes/figures/M01_mhealth_join.tex)

An inner join would remove more than half the cohort days. Missing calendar days are separate from unmatched rows in a join. The fixed cohort rule preserves within-user histories.

Source: M1, Section 1.8.2, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M01_Marketing_Analytics_and_Python.md

## Slide 15: Coding Exercise: An Order Assessment

- Implement aggregation with a coding assistant.
- Add a return, a missing identifier, and a duplicated lookup key.
- Report how each change affects rows, totals, and exceptions.

Use the small example in ../03_Data_and_Code/Lecture_Examples/session_examples.py S01. Retain the original three-line example as a hand-check. The output should distinguish accepted records from records requiring a decision.

Source: M1, Section 1.5, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M01_Marketing_Analytics_and_Python.md

## Slide 16: A Reproducible Analysis

- Relative paths identify inputs and outputs.
- A fresh run reconstructs results without hidden notebook state.
- Record package versions and consequential AI contributions.

A random seed reproduces a particular random computation under a given implementation. It does not establish valid sampling or eliminate changes across software versions.

Source: M1, Section 1.3, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M01_Marketing_Analytics_and_Python.md

## Slide 17: A Campaign Specification

- Define the eligible customers and contact date.
- State the contribution horizon and relevant costs.
- Identify the evidence needed for the untreated outcome.
- Choose a numerical check that would reveal a wrong denominator.

The specification should state one feasible action and the comparison that supports it. A randomized pilot may be the next useful step when incremental response is unresolved.

Source: M1, Section 1.4, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M01_Marketing_Analytics_and_Python.md

## Slide 18: Customer Data in an AI Workflow

- Use only data authorized for the tool and task.
- Minimize fields and use synthetic examples when they suffice.
- Check where uploads, logs, and generated files are stored.

Public availability does not establish permission for every reuse. Pseudonymized histories can retain identifying patterns. A coding request should specify the permitted input and destination before any transfer.

Source: Course agent guide and ETHICS_AND_REGULATION.md, M1.

## Slide 19: Decision Discussion

- Which customer receives the renewal offer?
- What changes if every treated renewal receives a discount?
- Which future variable would invalidate a Monday-morning forecast?

Under the stated synthetic inputs, B has higher incremental contribution. A discount paid to every renewing recipient reduces value by the treated renewal probability times the discount. A Wednesday service contact is unavailable for a Monday forecast.

Source: M1, Section 1.6, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M01_Marketing_Analytics_and_Python.md
