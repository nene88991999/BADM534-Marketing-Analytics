# Generative AI, Consumer Choice, and Regulation

By Nathan Yang

Session 14. M8, M9. 170 minutes.

[PDF](S14_Generative_AI_Consumer_Choice_and_Regulation.pdf) | [LaTeX](S14_Generative_AI_Consumer_Choice_and_Regulation.tex) | [Session Plan](SESSION_PLAN.md)

## Learning Objectives

- Assess AI demand measurements and workflow claims.
- Explain why a commercial objective can conflict with customer interests.
- Map a marketing decision to the relevant evidence, jurisdiction, and rule status.
- Examine the premises connecting commercial results to customer-benefit claims.
- Compare Kantian, institutional, and Confucian reasons for a marketing recommendation.
- Evaluate AI experimentation and personalized pricing through evidence, Kantian duties, and current policy scope.

## Related Materials

- [M8 lecture notes](../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md)
- [Runnable small examples](../03_Data_and_Code/Lecture_Examples/session_examples.py)
- [GenAI demand examples](../03_Data_and_Code/GenAI_Demand/README.md)
- [Ethics and regulation](../06_Lecture_Notes/ETHICS_AND_REGULATION.md)
- [Earnings-call worked example](../03_Data_and_Code/Earnings_Calls/README.md)
- [AI workflow calculations](../03_Data_and_Code/AI_Workflows/README.md)
- [Consumer Agency Literature and Clustering](../03_Data_and_Code/Consumer_Agency_Literature/README.md)
- [LLM Evidence and Revalidation](../03_Data_and_Code/LLM_Revalidation/README.md)
- [Marketing Dialectics](../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md)
- [Kantian, Institutional, and Confucian Readings](../01_Resources/15_Marketing_Dialectics/README.md)
- [Synthetic Renewal and Intent](../03_Data_and_Code/Marketing_Dialectics/README.md)
- [AI Experimentation and Pricing](../01_Resources/16_AI_Experimentation_and_Pricing/README.md)

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

- Identify the changed model, prompt, tool, data, or evaluation rule.
- Compare paired cases and fresh tasks using the same criteria.
- Include regressions, review costs, and customer consequences in the decision.

A new release motivates a hypothesis about the current workflow. It does not establish improvement in the intended task population. Preserve the current procedure, predefine acceptance criteria, and retain a way to return to it. The claim-lifetime study motivates task-specific revalidation; it does not set a universal review interval.

Source: M8 §8.18.1; M7 §7.22. https://zou-group.github.io/llm-claims-shelf-life/

## Slide 12: Residual Risk and Scale

- An expired research category can still allow residual failures.
- Expected failure loss depends on uses, failure probability, and consequences.
- Verify that references exist and support the claims made.

A fitted category describes the source protocol and selected model panel. The relevant deployment criterion depends on customer outcomes and exposure. A decline in fabricated references leaves other checks necessary, including correct details and support for an assertion. Correct references do not identify authorship.

Source: M8 §8.18.1; M2 §2.21. ../01_Resources/14_LLM_Evidence_and_Revalidation/README.md

## Slide 13: AI Experimentation: Evidence and Safeguards

- Causal Alignment learns from comparisons within past A/B tests.
- Its field result concerns clicks, with human selection and content checks.
- Customer benefit and informed choice require additional evidence.

Panagiotis Angelopoulos, Kevin Lee, and Sanjog Misra; author version linked August 2026. Sections 4–5 report the randomized comparison; Appendix B screens unsupported claims and missing information. Respect those safeguards when critiquing the scope of the result.

Source: https://leekevin.io/caLM.pdf

## Slide 14: Personalized Pricing: Benchmark and Incidence

- Dubé and Misra study employers purchasing recruiting services.
- Their model predicts higher profit and lower total customer surplus.
- A majority benefits; the later field comparison uses different price policies.

The downloaded NBER June 2021 revision is linked to the published JPE 2023 paper. The 19% projected profit gain uses an optimized uniform benchmark. The rounded realized means in the later experiment imply about 10.1% higher revenue than its implemented uniform policy. Customer surplus is model-derived. This is a business purchasing setting, not an emergency retail case.

Source: https://www.nber.org/papers/w23775

## Slide 15: Majority Gains and Aggregate Customer Losses

Synthetic population and solved prices; dollars per eligible customer.

**Figure description:** Profit and customer surplus are compared on a common dollar axis for uniform pricing, segmented pricing, and capped discounts.

[Editable TikZ](../06_Lecture_Notes/figures/M09_pricing_distribution.tex)

The two imposed valuation groups have shares 0.6 and 0.4. Segmentation benefits 60% but lowers aggregate customer surplus. Discount-only pricing improves profit and customer surplus relative to the optimal uniform benchmark in this population. Full source and exact arithmetic appear in Section 9.17.

Source: Marketing Dialectics, Sections 9.16–9.17. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 16: Marketing Dialectics: Examine the Premise

- State the claim, its evidence, and the premise connecting them.
- Kant examines reason’s demand for an unconditioned explanation.
- A marketing analogy must preserve the scope of the original argument.

Kant’s transcendental dialectic concerns metaphysical cognition. These marketing cases adapt the practice of examining premises; an ordinary empirical dispute is not a cosmological antinomy. The third antinomy does not imply that accurate purchase prediction proves lost agency. Critical examination may support, restrict, or reject a claim; no forced synthesis is required.

Source: Marketing Dialectics, §§9.1–9.3. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 17: Commercial Results and Customer Claims

Causal, measurement, and ethical questions have different premises.

**Figure description:** Separate paths connect a practice to commercial effects and customer outcomes. A judgment about the practice also requires an ethical principle.

[Editable TikZ](../06_Lecture_Notes/figures/M09_claim_scope.tex)

A randomized intervention can establish incremental purchases without establishing informed choice or customer benefit. Kant’s humanity formulation supplies a distinct ethical question about treatment of persons.

Source: Marketing Dialectics, §§9.1, 9.4. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 18: Self-Interest Creates a Burden of Justification

A reason for scrutiny is distinct from evidence of misconduct.

**Figure description:** A material conflict leads to independent substantiation and then a decision that can change with evidence.

[Editable TikZ](../06_Lecture_Notes/figures/M09_burden_justification.tex)

Hume proposes institutional checks that work under private-interest pursuit and distinguishes that design maxim from universal dishonesty. Smith urges scrutiny of interested commercial-regulation proposals. Requiring firms to substantiate customer-benefit claims is a contemporary institutional recommendation, not a universal legal presumption of guilt.

Source: Marketing Dialectics, §9.10. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 19: Justify the Practice Before Ranking Its Performance

A commercial ranking also needs a justified set of permissible actions.

**Figure description:** Proposals pass through restrictions concerning truthful claims, data use, and refusal before performance ranking. Customer evidence can require revision.

[Editable TikZ](../06_Lecture_Notes/figures/M09_optimization_boundary.tex)

Kantian duties cannot automatically be replaced by a finite penalty in an objective function. The proposed restrictions are contemporary applications requiring explicit justification. Human review and measured outcomes provide evidence; they do not mechanically define autonomy.

Source: Marketing Dialectics, Sections 9.16–9.17. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 20: Confucian Perspectives: Profit and Responsibility

- Evaluate how profit is obtained and which relationships sustain it.
- A trusted adviser or customer-care role carries standards of conduct.
- Examine whether the claimed role matches incentives and practice.

Analects 4.5 and 4.16 place righteousness in the evaluation of gain; Mencius 1A.1 challenges an exclusive focus on advantage. Analects 12.7 and 13.3 motivate trustworthiness and fit between names, roles, and conduct. These are contemporary applications of texts with historical political settings. A profitable exchange can serve both parties.

Source: Marketing Dialectics, §§9.11.1–9.11.2. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 21: Truthful Challenge and Cultivated Judgment

- Harmony can include reasoned disagreement.
- Learning and reflection should discipline an AI-generated answer.
- Good conduct depends on repeated practices as well as stated values.

Analects 13.23, 14.22, and 2.15 support discussion of truthful challenge and reflective learning. Mencius emphasizes cultivable moral beginnings; Xunzi emphasizes deliberate effort, teaching, and ritual. They disagree about human nature. A modern firm can examine what its rewards teach employees to notice and whether an analyst can report an unwanted customer outcome.

Source: Marketing Dialectics, §§9.11.3–9.11.4. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 22: A Choice Procedure Can Change Renewal

- A direct offer and an offer preceded by questions can produce different choices.
- The customer still makes the final selection.
- An independent value measure determines whether an additional renewal benefits that customer.

Questions, defaults, or retention prompts can precede a fixed target decision. The welfare comparison depends on consumer values, stable response probabilities, and the procedure set. A renewal increase alone does not establish either benefit or harm.

Source: M8, Section 8.14, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md

## Slide 23: Opposed Interests

Suppose renewal yields firm margin $\nu>0$ and costs the customer $\sigma>0$ relative to declining.

$$
\Delta\Pi=\nu(s-s_0),\qquad \Delta V=-\sigma(s-s_0)
$$

A higher renewal probability raises profit and lowers customer value under these stated stakes.

This conditional comparison holds the offer, monetary values, and relevant response population fixed. It does not infer customer harm from conversion alone. Additional time and authority costs require separate measurement.

Source: M8, Section 8.14, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md

## Slide 24: Profit and Customer Value Can Move Oppositely

Synthetic probabilities and fixed stakes. Direct renewal is 20%.

**Figure description:** An optional procedure lowers renewal to 10%; another raises it to 60%. At firm margin 11 dollars and customer loss 10 dollars per unwanted renewal, the latter gains the firm 4.40 dollars and costs the customer 4 dollars relative to direct choice.

[Editable TikZ](../06_Lecture_Notes/figures/M08_retention_welfare.tex)

The direct-choice benchmark is distinct from the consumer-preferred procedure. Relative to the 10% procedure, the 60% procedure creates a 5-dollar customer loss. These probabilities and monetary values are imposed inputs, not observed customer responses.

Source: M8, Section 8.14, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md

## Slide 25: Experimentation Selects the Commercial Winner

- A fixed set of procedures has stable renewal probabilities.
- Independent randomized samples estimate each probability.
- With opposed interests, accurately selecting the largest rate also selects the largest loss in that set.

The result requires common fixed stakes, a fixed catalog chosen before the experiment, stable responses from experiment to deployment, and complete independently sampled outcomes. It does not say that every experiment harms consumers.

Source: M8, Section 8.14, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md

## Slide 26: A Cancellation Evaluation

- Include a direct-cancellation comparison.
- Record whether optional retention content can be refused before exposure.
- Measure completion, elapsed time, subsequent charges, and customer value.

An effective refusal path and an independent value measure reveal dimensions hidden by renewals. A direct-choice arm helps isolate the effect of the preceding interaction.

Source: M8, Section 8.14, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md

## Slide 27: Same Renewal, Different Customer Intent

Synthetic populations: 1,000 customers each, one renewal month.

**Figure description:** A and B each have 900 billed customers. A contains 880 wanted and 20 unwanted renewals; B contains 600 wanted and 300 unwanted renewals. Both have 100 not billed.

[Editable TikZ](../06_Lecture_Notes/figures/M09_retention_intent.tex)

Intent is stipulated before billing. All-customer unwanted shares are 2% and 30%; among billed customers they are approximately 2.22% and 33.33%. These populations do not estimate a treatment effect or monetary welfare. Run evaluate_retention.py; full source is in Section 9.5. Missing intent stays unknown.

Source: Marketing Dialectics, §9.5. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 28: A Welfare Comparison

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

## Slide 29: Coding Exercise: A Marketing Evaluation

- Reproduce the two populations with identical billed renewal.
- Keep unknown intent separate and compare the relevant denominators.
- State the evidence and ethical premise needed to justify the practice.

Run ../03_Data_and_Code/Marketing_Dialectics/evaluate_retention.py. The full program and five tests accompany M9 §9.5. Existing M8 examples add conditional profit and welfare calculations. These are synthetic examples and do not estimate an interface effect.

Source: ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 30: Federal Cancellation Policy: Current Status

- July 2025: the Eighth Circuit vacated the 2024 FTC rule.
- February 2026: the FTC restored the earlier prenotification rule.
- March 2026: an advance notice sought input on possible amendments.

Checked November 5, 2026. The court identified a procedural deficiency. The March notice does not establish a replacement obligation; the October 14 information-collection notice concerns the restored rule. ROSCA separately requires disclosure, express informed consent, and simple cancellation mechanisms for covered online negative-option transactions.

Source: ../01_Resources/13_Consumer_Agency_and_Recent_Research/Policy/README.md

## Slide 31: Cancellation Rules Differ by Jurisdiction

- California strengthened its Automatic Renewal Law on July 1, 2025.
- New York City's separate rule took effect October 1, 2026.
- Identify covered transactions, enrollment media, and sector exceptions.

California guidance describes online cancellation without obstruction for online enrollment. NYC Section 5-110.2 requires simple cancellation as easy as enrollment and bars obstruction or unreasonable delay. Retention offers are subject to those restrictions; Section 5-110.3 contains sector exclusions. These sources were checked November 5, 2026. See M8 Section 8.19.

Source: ../01_Resources/13_Consumer_Agency_and_Recent_Research/Policy/README.md

## Slide 32: Research Frequency and Policy Importance

- Social influence leads the selected literature clusters.
- Exit friction can affect many customers even with few papers in the sample.
- Choose safeguards using mechanism, exposure, and customer consequences.

Journal counts give each paper equal weight and do not measure market exposure or loss. The 48-paper primary sample is access-selected and largely coded for inferred dual use. The full DOI census contains 824 eligible records with 721 full-text gaps. See M4 Section 4.17 and M8 Section 8.19.

Source: ../03_Data_and_Code/Consumer_Agency_Literature/README.md

## Slide 33: Pricing, Reviews, and Delivery

- Price-display rules require attention to the covered industry.
- Reviews presented as customer experiences require truthful provenance.
- Housing-ad delivery can create discrimination concerns beyond targeting choices.

The FTC fee rule covers live-event tickets and short-term lodging. Its review rule distinguishes business creation and purchase of false reviews from mere hosting. The DOJ Meta settlement addresses housing advertising specifically. These sources do not establish an identical rule for every marketing application.

Source: Primary-source scope and status record: ../06_Lecture_Notes/ETHICS_AND_REGULATION.md.

## Slide 34: Pricing Language and Regulatory Evidence

- Shelf infrastructure, price rules, and consumer effects are separate objects.
- The FTC's January 2025 report describes research on pricing intermediaries.
- Specify the practice and applicable authority before making a legal claim.

The US FTC Section 6(b) staff research summaries report preliminary findings. This research publication has no rule effective date and supplies no legal finding against firms in the earnings-call sample. Use the source-linked cases from M5 to identify operational facts still needed.

Source: M8, Section 8.16. FTC, January 2025, pp. 1–3. https://www.ftc.gov/system/files/ftc_gov/pdf/p246202_surveillancepricing6bstudy_researchsummaries_redacted.pdf

## Slide 35: Personalized Pricing: Policy Status

- FTC: August 2026 proposal; October 2026 information-gathering inquiry.
- New York: disclosure law in effect; broader restrictions await enactment.
- Price gouging requires its own covered circumstances and legal elements.

Checked November 6, 2026. FTC proposal cites Dubé and Misra. October 28 Section 6(b) orders do not establish violations. New York GBL 349-a applies to covered personal, family, and household purchases, with exceptions. S8623B/A9349B has legislative passage without recorded gubernatorial enactment. GBL 396-r addresses essential goods and services during abnormal market disruptions.

Source: ../01_Resources/16_AI_Experimentation_and_Pricing/02_Policy/README.md

## Slide 36: Environmental Claims: Two Different Decisions

- 2023 Shell ads: the ASA upheld the overall-impression complaint.
- 2025 Shell ad: the ASA accepted the contextualized communication.
- Evaluate the particular claim, material context, and applicable standard.

UK ASA, June 7, 2023: omitted context about the balance of business activities made the overall environmental impression misleading; a separate electricity claim was not upheld. April 9, 2025: the later ad included higher- and lower-carbon activities and investment context and was not found misleading. Its ruling explains the applicable pre-April-2025 code wording. These are specific regulatory outcomes, not firm-wide ethical verdicts. Sources: https://www.asa.org.uk/rulings/shell-uk-ltd-g22-1170842-shell-uk-ltd.html and https://www.asa.org.uk/rulings/shell-uk-ltd-g24-1248246-shell-uk-ltd.html

Source: Marketing Dialectics, §9.8. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 37: A Product Fact and a Portfolio Impression

The scope of the conclusion determines the evidence required.

**Figure description:** The product, portfolio, and future transition require different supporting information: comparison, denominator, and time horizon.

[Editable TikZ](../06_Lecture_Notes/figures/M09_environmental_scope.tex)

A true statement about one product can be insufficient to support a broader impression. The ASA comparison supplies an institutional case; the diagram is an original conceptual analysis.

Source: Marketing Dialectics, §9.8. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 38: A Decision With Consumer Outcomes

- State the commercial target and customer outcome.
- Identify the procedure the customer can accept, refuse, or revise.
- Connect the proposed action to current rules and supporting evidence.

A marketing policy can improve matching, convenience, and customer value. Its evaluation should also reveal when additional sales come from misleading claims, unwanted friction, or conflicting incentives.

Source: Primary-source scope and status record: ../06_Lecture_Notes/ETHICS_AND_REGULATION.md.
