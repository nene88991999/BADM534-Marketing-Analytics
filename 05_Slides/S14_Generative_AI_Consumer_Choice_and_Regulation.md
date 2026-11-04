# Generative AI, Consumer Choice, and Regulation

By Nathan Yang

Session 14. M8. 170 minutes.

[PDF](S14_Generative_AI_Consumer_Choice_and_Regulation.pdf) | [LaTeX](S14_Generative_AI_Consumer_Choice_and_Regulation.tex) | [Session Plan](SESSION_PLAN.md)

## Learning Objectives

- Assess AI demand measurements and workflow claims.
- Explain why a commercial objective can conflict with customer interests.
- Map a marketing decision to the relevant evidence, jurisdiction, and rule status.

## Related Materials

- [M8 lecture notes](../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md)
- [Runnable small examples](../03_Data_and_Code/Lecture_Examples/session_examples.py)
- [GenAI demand examples](../03_Data_and_Code/GenAI_Demand/README.md)
- [Ethics and regulation](../06_Lecture_Notes/ETHICS_AND_REGULATION.md)
- [Earnings-call worked example](../03_Data_and_Code/Earnings_Calls/README.md)
- [AI workflow calculations](../03_Data_and_Code/AI_Workflows/README.md)

## Slide 1: Generative AI, Consumer Choice, and Regulation

Marketing Analytics. By Nathan Yang.

## Slide 2: A Subscription-Growth Decision

- A firm wants to increase paid renewals.
- The evidence includes subscription histories, interfaces, and customer outcomes.
- A higher renewal rate can arise through improved value or greater cancellation friction.

The commercial outcome does not identify the consumer mechanism. A useful assessment records value, consent, cancellation completion, and customer time as well as revenue.

Source: M8, Section 8.13, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md

## Slide 3: Public Attention and Paid Demand

- Pageviews measure attention to selected pages.
- Paid subscriptions measure a specific payment relationship.
- User, provider, and category denominators differ.

A title change can split attention across pages. A user can hold multiple subscriptions. These measurement choices can create apparent differences in demand without the same underlying object.

Source: M8, Section 8.13, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md

## Slide 4: A Fixed Starting Cohort

Entirely synthetic subscription panel. Provider labels identify simulated options.

**Figure description:** Starting-provider cohorts split into same-provider, other-provider-only, and no-paid-provider states. Each bar uses its own fixed starting cohort denominator.

[Editable TikZ](../06_Lecture_Notes/figures/M04_genai_cohorts.tex)

These simulated percentages are not actual market shares or provider retention estimates. Multiple-provider behavior requires a definition that prevents incompatible categories from being added.

Source: M4, Section 4.14, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md

## Slide 5: Subscriber Stocks and New Flows

- A subscriber stock includes past acquisition and survival.
- A new-subscription flow can include first purchases and returns.
- A price coefficient depends on the outcome and behavioral model.

Regressing subscriber stocks on current prices can combine persistent state with current choice. A structural interpretation must match the data-generating choice process.

Source: M8, Section 8.13.2, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md

## Slide 6: A Known Model Is a Useful Verification Case

Synthetic demand exercise with a known binary-model benchmark.

**Figure description:** The exact binary benchmark recovers a price coefficient of -0.06. Stock and new-flow specifications give different coefficients under their different data definitions.

[Editable TikZ](../06_Lecture_Notes/figures/M08_genai_price.tex)

Recovering the benchmark checks implementation under its assumptions. It does not establish a structural interpretation for the richer simulated panel or actual market data.

Source: M8, Section 8.13.1, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md

## Slide 7: Seller Costs and Customer Alternatives

Hypothetical dollars per customer, conditional on 50 sales.

**Figure description:** The initial seller floor is 40 dollars and buyer ceiling 80. Seller automation lowers the floor to 30 while the ceiling stays 80. Shared adoption raises outside-option utility and lowers the ceiling to 20, below the 30-dollar floor.

[Editable TikZ](../06_Lecture_Notes/figures/M08_ai_price_bounds.tex)

Delivered value is 200 dollars, buyer burden 40, and fixed cost 1,000. Unit cost falls from 20 to 10. Outside-option utility then rises from 80 to 140. Gray intervals indicate simultaneous weak participation and cost recovery. Volume and valuations are imposed; these bounds neither estimate demand nor solve a pricing equilibrium. Customers are indifferent at the ceiling.

Source: Marketing Analytics Lecture Notes, M8 §8.17.2.

## Slide 8: AI Workflow Quality

- Measure the completed analysis and its validity.
- Include generation, review, and repair time.
- Use comparable tasks and independent quality criteria.

A time comparison can favor a tool because it abandons difficult tasks or reduces quality. The outcome definition should account for completion and validity before comparing speed.

Source: M8, Section 8.6, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md

## Slide 9: Review Time Is Part of Production

Synthetic workflows meet the same stated quality requirement.

**Figure description:** Manual production and review total 110 minutes. Assisted production and review total 85 minutes, a 22.7% total reduction despite a 50% drafting-time reduction.

[Editable TikZ](../06_Lecture_Notes/figures/M08_workflow_time.tex)

The manual workflow uses 90 minutes to produce and 20 to review. The assisted workflow uses 45 and 40. These are imposed time inputs, not an estimate of a universal AI effect.

Source: M8, Section 8.6, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md

## Slide 10: Reuse Has a Break-Even Workload

Hypothetical equal-quality work: six setup hours, with adaptation included.

**Figure description:** The existing process takes two hours per use. The reusable process takes six setup hours plus 1.5 hours per use, including upkeep. The lines cross at twelve uses and total 48 versus 42 hours at twenty-four uses.

[Editable TikZ](../06_Lecture_Notes/figures/M08_reuse_costs.tex)

Execution alone falls from two hours to 1.25, but 0.25 upkeep hours are required per use. Net savings become positive at the thirteenth use. Twenty-four uses save six hours, a 12.5% reduction after setup and upkeep. The numbers are imposed and do not measure course development time. Run investment.py and vary upkeep or workload.

Source: Marketing Analytics Lecture Notes, M8 §8.17.1.

## Slide 11: Model Updates and Unresolved Tasks

- Connect an update to a recorded difficulty and a feasible comparison.
- Evaluate the frozen challenger and current procedure on fresh cases.
- Include setup, correction, and maintenance in the adoption decision.

Record actual access, supported inputs, failure conditions, and the original decision. A difficulty register can omit an unexpected useful route, so allow exploratory comparisons and revise the diagnosis. Retain the existing procedure when the challenger provides no supported improvement. A new schema or customer population can require revalidation of a retained helper.

Source: Marketing Analytics Lecture Notes, M8 §8.18.

## Slide 12: A Choice Procedure Can Change Renewal

- A direct offer and an offer preceded by questions can produce different choices.
- The customer still makes the final selection.
- An independent value measure determines whether an additional renewal benefits that customer.

Questions, defaults, or retention prompts can precede a fixed target decision. The welfare comparison depends on consumer values, stable response probabilities, and the procedure set. A renewal increase alone does not establish either benefit or harm.

Source: M8, Section 8.14, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md

## Slide 13: Opposed Interests

Suppose renewal yields firm margin $\nu>0$ and costs the customer $\sigma>0$ relative to declining.

$$
\Delta\Pi=\nu(s-s_0),\qquad \Delta V=-\sigma(s-s_0)
$$

A higher renewal probability raises profit and lowers customer value under these stated stakes.

This conditional comparison holds the offer, monetary values, and relevant response population fixed. It does not infer customer harm from conversion alone. Additional time and authority costs require separate measurement.

Source: M8, Section 8.14, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md

## Slide 14: Profit and Customer Value Can Move Oppositely

Synthetic probabilities and fixed stakes. Direct renewal is 20%.

**Figure description:** An optional procedure lowers renewal to 10%; another raises it to 60%. At firm margin 11 dollars and customer loss 10 dollars per unwanted renewal, the latter gains the firm 4.40 dollars and costs the customer 4 dollars relative to direct choice.

[Editable TikZ](../06_Lecture_Notes/figures/M08_retention_welfare.tex)

The direct-choice benchmark is distinct from the consumer-preferred procedure. Relative to the 10% procedure, the 60% procedure creates a 5-dollar customer loss. These probabilities and monetary values are imposed inputs, not observed customer responses.

Source: M8, Section 8.14, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md

## Slide 15: Experimentation Selects the Commercial Winner

- A fixed set of procedures has stable renewal probabilities.
- Independent randomized samples estimate each probability.
- With opposed interests, accurately selecting the largest rate also selects the largest loss in that set.

The result requires common fixed stakes, a fixed catalog chosen before the experiment, stable responses from experiment to deployment, and complete independently sampled outcomes. It does not say that every experiment harms consumers.

Source: M8, Section 8.14, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md

## Slide 16: A Cancellation Evaluation

- Include a direct-cancellation comparison.
- Record whether optional retention content can be refused before exposure.
- Measure completion, elapsed time, subsequent charges, and customer value.

An effective refusal path and an independent value measure reveal dimensions hidden by renewals. A direct-choice arm helps isolate the effect of the preceding interaction.

Source: M8, Section 8.14, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md

## Slide 17: Rule Status and Scope

- A statute, binding rule, interpretive guide, and proposal have different authority.
- Record jurisdiction, covered conduct, exceptions, and effective date.
- Use the current primary source before turning a result into a business recommendation.

The FTC's March 2026 negative-option notice seeks input on possible amendments and refers to the vacated 2024 rule. A request for comments does not itself adopt replacement obligations.

Source: FTC, Negative Option Rule ANPRM announcement, March 2026. https://www.ftc.gov/news-events/news/press-releases/2026/03/ftc-seeks-public-comment-response-advance-notice-proposed-rulemaking-regarding-negative-option

## Slide 18: Pricing, Reviews, and Delivery

- Price-display rules require attention to the covered industry.
- Reviews presented as customer experiences require truthful provenance.
- Housing-ad delivery can create discrimination concerns beyond targeting choices.

The FTC fee rule covers live-event tickets and short-term lodging. Its review rule distinguishes business creation and purchase of false reviews from mere hosting. The DOJ Meta settlement addresses housing advertising specifically. These sources do not establish an identical rule for every marketing application.

Source: Primary-source scope and status record: ../06_Lecture_Notes/ETHICS_AND_REGULATION.md.

## Slide 19: Pricing Language and Regulatory Evidence

- Shelf infrastructure, price rules, and consumer effects are separate objects.
- The FTC's January 2025 report describes research on pricing intermediaries.
- Specify the practice and applicable authority before making a legal claim.

The US FTC Section 6(b) staff research summaries report preliminary findings. This research publication has no rule effective date and supplies no legal finding against firms in the earnings-call sample. Use the source-linked cases from M5 to identify operational facts still needed.

Source: M8, Section 8.16. FTC, January 2025, pp. 1–3. https://www.ftc.gov/system/files/ftc_gov/pdf/p246202_surveillancepricing6bstudy_researchsummaries_redacted.pdf

## Slide 20: A Welfare Comparison

Synthetic stakes distinguish profit from customer value.

```python
direct, selected = 0.20, 0.60
firm_margin, customer_loss = 11, 10
firm_gain = firm_margin * (selected-direct)
value_change = -customer_loss * (selected-direct)
assert round(firm_gain, 2) == 4.40
assert round(value_change, 2) == -4.00
```

Higher combined surplus can coexist with a customer loss under these assumptions.

The combined change is 0.40 dollars per potential customer in this example. The welfare result is conditional on the imposed values. A choice probability does not independently reveal those values.

Source: M8, Section 8.14, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md

## Slide 21: Coding Exercise: A Marketing Evaluation

- Calculate reuse break-even and the conditional price interval.
- Compute profit and customer value for alternative retention procedures.
- Propose an interface change and the evidence needed to evaluate it.

Run ../03_Data_and_Code/Lecture_Examples/session_examples.py S14 and S14_ethics. The GenAI demand programs provide richer stock, flow, cohort, and benchmark checks. Keep empirical measurements separate from imposed welfare inputs. The AI_Workflows folder supplies complete standard-library calculations with synthetic inputs.

Source: M8, Section 8.13.3, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md

## Slide 22: A Decision With Consumer Outcomes

- State the commercial target and customer outcome.
- Identify the procedure the customer can accept, refuse, or revise.
- Connect the proposed action to current rules and supporting evidence.

A marketing policy can improve matching, convenience, and customer value. Its evaluation should also reveal when additional sales come from misleading claims, unwanted friction, or conflicting incentives.

Source: Primary-source scope and status record: ../06_Lecture_Notes/ETHICS_AND_REGULATION.md.
