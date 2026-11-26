# Marketing Decisions and AI-Assisted Coding

By Nathan Yang

Session 01. M1. 170 minutes.

[PDF](S01_Marketing_Decisions_and_AI_Coding.pdf) | [LaTeX](S01_Marketing_Decisions_and_AI_Coding.tex) | [Session Plan](SESSION_PLAN.md)

## Learning Objectives

- Specify an action, observation unit, information set, and outcome horizon.
- Translate a small marketing calculation into readable Python.
- Verify generated code using identities and counterexamples.
- Distinguish a definition, an inference, a validation condition, and source evidence.
- Reconstruct a recommendation through its premises, a counterexample, and a condition for revision.
- Evaluate the worth of the objective and distinguish empirical representation from the practical standing of affected people.

## Related Materials

- [M1 lecture notes](../06_Lecture_Notes/modules/M01_Marketing_Analytics_and_Python.md)
- [Runnable small examples](../03_Data_and_Code/Lecture_Examples/session_examples.py)
- [mHealth dictionary](../03_Data_and_Code/mHealth/DATA_DICTIONARY.md)
- [Ethics and regulation](../06_Lecture_Notes/ETHICS_AND_REGULATION.md)
- [AI workflow calculations](../03_Data_and_Code/AI_Workflows/README.md)
- [LLM Evidence and Revalidation](../03_Data_and_Code/LLM_Revalidation/README.md)
- [Reproducible recommendation and optional practice](../07_Labs/Reproducible_Recommendations/README.md)
- [Cancellation Evidence: Data, Code, and Definitions](../03_Data_and_Code/Ontology_and_Evidence/README.md)
- [Agent Workflow Evaluation and Practice](../07_Labs/Agent_Workflows/README.md)
- [Statistical Inference: Code and Results](../03_Data_and_Code/Statistical_Inference/README.md)
- [Statistical Evidence: Optional Practice](../07_Labs/Statistical_Inference/README.md)
- [Coding Workflows: Published Evidence](../01_Resources/40_Econometric_Coding_Workflows/README.md)
- [Coding Workflows: Python and Checks](../03_Data_and_Code/Agent_Workflows/README.md)
- [Analytical Arguments: Python and Results](../03_Data_and_Code/Analytical_Arguments/README.md)
- [Five-Step Argument Practice](../07_Labs/Philosophical_Arguments/README.md)

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

## Slide 4: Which Ends Deserve Pursuit?

- Who selected the objective, and with what authority?
- Which people bear its burdens or lose a choice?
- Which reasons matter even when they are difficult to quantify?
- An accurate algorithm can advance an objectionable end.

Empirical analysis informs consequences and feasibility. Deliberation about ends, authority, and obligations requires a philosophical argument from the start. Kant limits theoretical knowledge to objects of possible experience; an empirical model does not exhaust the person represented. A missing empirical variable remains investigable. Practical respect has a distinct justification in the Groundwork. The course develops these distinctions in M9 §9.41.

Source: M1 §1.20 and M9 §9.41. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 5: Analytical Questions

- Description: how often do customers renew?
- Prediction: who is likely to renew?
- Causal effect: how does an offer change renewal?
- Decision: which contacts generate positive incremental contribution?

The same customer records can support different analytical objects. Predictive performance evaluates forecasts under the represented conditions. A targeting policy also needs the untreated comparison and relevant costs.

Source: M1, Section 1.1, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M01_Marketing_Analytics_and_Python.md

## Slide 6: Incremental Contribution

For account $i$, compare renewal under an offer and no offer.

$$
\Delta\pi_i=m_i\{p_i(1)-p_i(0)\}-c_i
$$

Contribution $m_i$ and contact cost $c_i$ are dollars per account over the stated horizon.

The formula assumes that the offer cost can be summarized by c and that contribution already deducts relevant variable costs. A discount paid on every treated purchase requires an additional cost term.

Source: M1, Section 1.1, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M01_Marketing_Analytics_and_Python.md

## Slide 7: Response and Incremental Value

Synthetic accounts. Contribution is 100 dollars and contact cost is 3 dollars.

**Figure description:** Account A has treated renewal probability 0.91 and incremental contribution -2 dollars. Account B has probability 0.50 and contribution 7 dollars.

[Editable TikZ](../06_Lecture_Notes/figures/M01_response_vs_value.tex)

A rises from 0.90 to 0.91. B rises from 0.40 to 0.50. The untreated probabilities explain the reversal. These probabilities are imposed teaching inputs.

Source: M1, Section 1.1, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M01_Marketing_Analytics_and_Python.md

## Slide 8: The Observation Unit

- A product line, order, customer, and customer-month are different units.
- The key identifies one row at the intended level.
- Aggregation changes the weights used in an average.

A customer with five order lines receives five times the weight of a customer with one line in a line-level mean. Define whether the managerial comparison concerns orders or equally weighted customers.

Source: M1, Section 1.2, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M01_Marketing_Analytics_and_Python.md

## Slide 9: Python Objects and Order Totals

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

## Slide 10: Functions and Data Contracts

- Inputs have names, types, units, and allowed missing values.
- A function returns a defined output and an exception report.
- Returns, canceled orders, and duplicate lines need explicit rules.

A numeric-looking string requires conversion before arithmetic. A negative quantity may be a legitimate return. A rule should preserve a trace from the original record to its inclusion or exclusion.

Source: M1, Section 1.3, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M01_Marketing_Analytics_and_Python.md

## Slide 11: A Request and a Completed Action

- Define accounts, subscriptions, requests, and confirmations.
- Attach each record to its source and observation time.
- A request establishes an intention recorded by the service.
- Completion requires evidence of the subsequent action.

An ontology specifies classes, relationships, and inference rules. A CancellationRequest can belong to the broader ServiceRecord class. The class assignment does not establish execution of a cancellation. A data dictionary and explicit event relationships make AI-generated calculations reviewable.

Source: M1 §1.16 and M2 §2.25. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md

## Slide 12: Inference, Validation, and Evidence

- Inference follows from stated facts and rules.
- Validation checks supplied records against requirements.
- Missing information can remain unknown.
- Source evidence supports whether a premise is credible.

An OWL domain axiom can infer a subject type; it need not reject a missing explicit type. A timestamp requirement can instead flag missing data. A consistent model can contain false premises, and a contradiction may reveal an inappropriate axiom. The original Python case implements explicit checks, not OWL or SHACL. W3C OWL 2 Primer and SHACL supply the formal distinctions.

Source: M1 §1.16 and M2 §2.25. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md https://www.w3.org/TR/owl2-primer/ https://www.w3.org/TR/shacl/

## Slide 13: A Duplicate Lookup Doubles Sales

Synthetic join. One 40-dollar order matches two customer records.

**Figure description:** The original order has one row. A duplicate customer lookup produces two joined rows and an apparent 80-dollar total.

[Editable TikZ](../06_Lecture_Notes/figures/M01_join_multiplication.tex)

A many-to-one relationship requires unique customer keys in the lookup. Check key uniqueness before merging and reconcile sales afterward.

Source: M1, Section 1.2, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M01_Marketing_Analytics_and_Python.md

## Slide 14: An AI Coding Request

- Return one row per order and an exceptions table.
- Treat negative quantities as returns under the stated rule.
- Verify the 37-dollar example and reject missing order IDs.
- Explain each transformation before adding the next step.

A useful request specifies analytical behavior and acceptance criteria. The assistant can propose an implementation while the analyst remains responsible for the observation unit and sample rules.

Source: M1, Section 1.5, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M01_Marketing_Analytics_and_Python.md

## Slide 15: Code Errors and Missing Evidence

- A repeated daily total requires a correction to aggregation.
- Unrecorded food requires additional measurement or a recorded-behavior target.
- A coupon decision needs evidence about untreated outcomes.

The response to a failed analysis depends on the unresolved distinction. Ask for the smallest check that could distinguish a calculation error from missing information. A new model can improve implementation while leaving the missing-information problem unchanged. A validated category summary can also remove unnecessary prose generation when the decision only needs category totals.

Source: Marketing Analytics Lecture Notes, M1 §1.12.

## Slide 16: Statistical Choices in Generated Code

- Define the population, outcome, comparison, and assignment unit.
- Inspect the method and uncertainty calculation.
- Reconcile the report with executed output.
- Explain effect size and the supported managerial action.

Successful execution, an appropriate statistical method, accurate reporting, and a justified recommendation require separate evidence. Fisher-R1 motivates this distinction through hypothesis-testing tasks. Its benchmark agreement rate differs from a false-positive rate under a known null. The course reference calculations contain no measured AI-model performance. Preserve the initial generated analysis and test a frozen revision on fresh data.

Source: M1 §1.18. ../06_Lecture_Notes/modules/M01_Marketing_Analytics_and_Python.md

## Slide 17: Execution, Revision, and Correct Calculations

| Workflow | Success | Loud / 100 | Silent / 100 |
| --- | --- | --- | --- |
| Chatbot | 83.69% | 11.76 | 4.54 |
| Self-Repair | 93.29% | 1.16 | 5.55 |
| Agent | 97.37% | 0.28 | 2.35 |

Published benchmark: 14,400 assigned runs per workflow; 40 tasks, six models.

The method, sample, target quantities, and inference convention are supplied before coding. A loud failure means failed execution or incomplete requested output. A silent failure returns complete output with an incorrect scored value. Self-repair permits three revisions after execution or completeness feedback. The agent also receives an independent-check instruction, so the comparison changes several workflow components together. The authors collected these model results; the course program reconstructs aggregates from their release.

Source: Galiani, López, and Sosa, November 2026. ../01_Resources/40_Econometric_Coding_Workflows/README.md

## Slide 18: Fewer Errors, a Different Remaining Problem

Silent failures are 2.35% of agent runs and 89.18% of its failures.

**Figure description:** The left panel reports loud and silent failures per 100 assigned runs. The right panel reports silent failures as a share of failures. Both use the authors' intervals from resampling 40 tasks.

[Editable TikZ](../06_Lecture_Notes/figures/M01_coding_failure_denominators.tex)

The agent has 338 silent failures among 14,400 assigned runs and 379 total failures. Lower total error and a larger silent share are compatible. Self-repair can turn an incomplete program into a complete but wrong one, exposing a different failure category. Inspect numerical validity after execution succeeds. See M1 §1.19 and the published aggregate reconstruction.

Source: Galiani, López, and Sosa, November 2026. ../01_Resources/40_Econometric_Coding_Workflows/README.md

## Slide 19: Verification with Counterexamples

- A duplicate lookup must trigger a failed key check.
- An unmatched customer must remain visible in the assessment.
- An empty input needs an explicit result.
- Order totals must reconcile with eligible product lines.

These checks test properties that can fail even when code runs. Repeating the program with the same input confirms reproducibility but does not independently establish correctness.

Source: M1, Section 1.5, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M01_Marketing_Analytics_and_Python.md

## Slide 20: Information and Development Feedback

Hold the model and task fixed; compare the four complete workflows.

**Figure description:** A two-by-two matrix crosses a structured data dictionary with independent development checks. No performance values are assigned to the cells.

[Editable TikZ](../06_Lecture_Notes/figures/M01_workflow_design.tex)

All cells receive the same core measurement request and output schema. Explicit information organizes the definitions, while independent feedback exposes development discrepancies and permits bounded correction. Common tools, permissions, and resource caps keep the comparison interpretable. The possible interaction is measured on a frozen evaluation task. This diagram specifies an experiment and contains no observed model performance.

Source: Li and coauthors, Agent Harness Engineering: A Survey, §§8–9. Original course applications: ../01_Resources/35_Agent_Workflow_Evaluation/README.md ../03_Data_and_Code/Agent_Workflows/README.md

## Slide 21: The Logging Denominator

- Eligibility uses January–June records within the recurring mHealth cohort.
- 358 users contribute 11,098 possible July user-days.
- 6,455 recorded days give a mean logging rate of 58.16%.
- Keep the 39 users with no July records.

The roster records earlier presence in the released file, not account enrollment. Count distinct dates from July 1 inclusive through August 1 exclusive. The input includes neighboring boundary dates. A zero is no recorded logging in the window; it is not zero consumption. Full source reconstruction and reference calculation appear in M1 §1.17.

Source: Li and coauthors, Agent Harness Engineering: A Survey, §§8–9. Original course applications: ../01_Resources/35_Agent_Workflow_Evaluation/README.md ../03_Data_and_Code/Agent_Workflows/README.md

## Slide 22: mHealth Records

- Food entries describe recorded items on observed user-days.
- The separate daily table covers only part of the food-log history.
- Reported daily calories repeat across item rows.

The released records replace user identifiers and birthdays and perturb weight values. The source daily total is distinct from the sum of item calories. Neither is a direct measure of complete usual intake.

Source: M1, Section 1.8, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M01_Marketing_Analytics_and_Python.md

## Slide 23: Join Choice Changes the Sample

Released mHealth cohort: 76,804 observed user-days.

**Figure description:** A left join retains all 76,804 user-days. Only 37,634 match the separate daily file, leaving 39,170 unmatched.

[Editable TikZ](../06_Lecture_Notes/figures/M01_mhealth_join.tex)

An inner join would remove more than half the cohort days. Missing calendar days are separate from unmatched rows in a join. The fixed cohort rule preserves within-user histories.

Source: M1, Section 1.8.2, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M01_Marketing_Analytics_and_Python.md

## Slide 24: Coding Exercise: An Order Assessment

- Implement aggregation with a coding assistant.
- Add a return, a missing identifier, and a duplicated lookup key.
- Report how each change affects rows, totals, and exceptions.

Use the small example in ../03_Data_and_Code/Lecture_Examples/session_examples.py S01. Retain the original three-line example as a hand-check. The output should distinguish accepted records from records requiring a decision.

Source: M1, Section 1.5, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M01_Marketing_Analytics_and_Python.md

## Slide 25: Versioned Evidence

- Record the model, date, prompts, tools, settings, parser, and scoring rule.
- Keep known failure cases and evaluate transfer on fresh cases.
- Check parsing, execution, and analytical correctness separately.

A historical finding concerns the tested configuration. A current workflow can differ through the model, interface, data, or judgment rule. Chen, Zaharia, and Zou separate code formatting from correctness after postprocessing. A code generator can improve on one measure while an automated pipeline breaks on another.

Source: M1 §1.13. Chen, Zaharia, and Zou (2024), §3.5. https://hdsr.mitpress.mit.edu/pub/y95zitmz/release/2 ../01_Resources/14_LLM_Evidence_and_Revalidation/README.md

## Slide 26: A Reproducible Analysis

- Relative paths identify inputs and outputs.
- A fresh run reconstructs results without hidden notebook state.
- Record package versions and consequential AI contributions.

A random seed reproduces a particular random computation under a given implementation. It does not establish valid sampling or eliminate changes across software versions.

Source: M1, Section 1.3, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M01_Marketing_Analytics_and_Python.md

## Slide 27: Repeated Responses Change the Weight

Synthetic ratings stay fixed. Additional identical rows change representation.

**Figure description:** The dashed blue equal-persona mean stays at 3.975. The orange equal-row mean rises from 3.975 to 4.158333 as p01 supplies one to five identical responses. Persona p01 has rating 4.25 and p02 has rating 3.70; p02 supplies one response throughout.

[Editable TikZ](../06_Lecture_Notes/figures/M01_repeat_weights.tex)

A product manager must specify which unit receives equal weight. With two p01 responses and one p02 response, equal-row weighting gives 4.066667; equal-persona weighting gives 3.975. This imposed comparison measures no preference change. The complete source program is ../03_Data_and_Code/Reproducible_Recommendations/reproduce_recommendation.py. Each rating is derived from invented responses and imposed similarities.

Source: M1, Section 1.15. ../06_Lecture_Notes/modules/M01_Marketing_Analytics_and_Python.md

## Slide 28: Numerical Evidence and the Recommendation

- Recompute the table and check one calculation independently.
- Preserve persona weights, missing values, and the synthetic-data scope.
- Follow the report to its inputs, program, table, and figure.

The program recomputes four saved tables and stops if a table is missing or differs. An equality check can miss an error shared by the saved table and code, so use independent arithmetic. A pooled six-concept pattern leaves its shortlist and correlation undefined. Turning that result into a launch decision adds an unsupported inference. Re-run from the course root and example directory; the script resolves inputs relative to its own file.

Source: M1, Section 1.15. ../06_Lecture_Notes/modules/M01_Marketing_Analytics_and_Python.md

## Slide 29: A Campaign Specification

- Define the eligible customers and contact date.
- State the contribution horizon and relevant costs.
- Identify the evidence needed for the untreated outcome.
- Choose a numerical check that would reveal a wrong denominator.

The specification should state one feasible action and the comparison that supports it. A randomized pilot may be the next useful step when incremental response is unresolved.

Source: M1, Section 1.4, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M01_Marketing_Analytics_and_Python.md

## Slide 30: Customer Data in an AI Workflow

- Use only data authorized for the tool and task.
- Minimize fields and use synthetic examples when they suffice.
- Check where uploads, logs, and generated files are stored.

Public availability does not establish permission for every reuse. Pseudonymized histories can retain identifying patterns. A coding request should specify the permitted input and destination before any transfer.

Source: Course agent guide and ETHICS_AND_REGULATION.md, M1.

## Slide 31: The Question Determines the Evidence

- Who will accept? Define the prediction target.
- What changes? Specify the intervention and comparison.
- Who bears a burden? Define the relevant outcome.
- What ought the firm do? Defend the governing principle.

An accurate purchase forecast can leave customer burdens and permission unresolved. Koralus and Mascarenhas model reasoning through questions and answers; this workflow applies that distinction to a managerial brief. Do not infer a cognitive mechanism for a particular analyst or AI system. Preserve the population, timing, units, and meaning of each result.

Source: M1 §1.20. ../06_Lecture_Notes/modules/M01_Marketing_Analytics_and_Python.md

## Slide 32: Test the Argument and Revise the Conclusion

A counterexample preserves the premises while challenging the inference.

**Figure description:** Five boxes connect claim definition, premises, a counterexample, assessment of the missing premise, and a revised conclusion. A dashed arrow returns to the claim.

[Editable TikZ](../06_Lecture_Notes/figures/M09_argument_revision.tex)

Use the same sequence on an AI-generated recommendation and on its criticism. Check each proposed counterexample against the actual premise. Label an invented scenario hypothetical. The final step names evidence or reasons that would change the conclusion. The longer argument record is optional practice, subject to applicable AI rules.

Source: M1 §1.20. ../06_Lecture_Notes/modules/M01_Marketing_Analytics_and_Python.md

## Slide 33: Decision Discussion

- Which customer receives the renewal offer?
- What changes if every treated renewal receives a discount?
- Which future variable would invalidate a Monday-morning forecast?

Under the stated synthetic inputs, B has higher incremental contribution. A discount paid to every renewing recipient reduces value by the treated renewal probability times the discount. A Wednesday service contact is unavailable for a Monday forecast.

Source: M1, Section 1.6, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M01_Marketing_Analytics_and_Python.md
