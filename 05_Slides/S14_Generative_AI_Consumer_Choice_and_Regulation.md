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
- Distinguish a pricing allegation, an observed outcome, a model implication, and an ethical justification.
- Construct an ought conclusion from supported factual premises and a defended normative principle.
- Compare stakeholder reasons, including those of people with limited influence over public discussion.
- Assess demand assumptions, feasible pricing alternatives, and individual burdens.
- Connect a specified antitrust claim to evidence and Scanlonian institutional reasons.
- Distinguish instrumental rationality, reliable measurement, and reasonable justification of an objective.
- Compare the moral premises in personalized pricing, dynamic-pricing communication, and data-center reassurance.
- Assess validity, premise support, and reasonable justification symmetrically for a claim and its criticism.
- Evaluate the worth of the objective and distinguish empirical representation from the practical standing of affected people.
- Assess a case interpretation using ontological scope, empirical evidence, and philosophical reasons.
- Assess conflicts of interest through duties, consumer purposes, and reasons for a feasible alternative.
- Defend the empirical and moral premises behind reassurance to affected households.

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
- [Synthetic Consumers and Human Validation](../03_Data_and_Code/Synthetic_Consumers/README.md)
- [Reproducible product recommendation](../03_Data_and_Code/Reproducible_Recommendations/README.md)
- [Cancellation Evidence: Data, Code, and Definitions](../03_Data_and_Code/Ontology_and_Evidence/README.md)
- [Agent Workflow Evaluation and Practice](../07_Labs/Agent_Workflows/README.md)
- [Representation Alignment: Programs and Results](../03_Data_and_Code/Representation_Alignment/README.md)
- [Representation Alignment: Optional Practice](../07_Labs/Representation_Alignment/README.md)
- [Pricing Case: Sources and Evidence](../01_Resources/37_Pricing_Systems_and_Competition/README.md)
- [Pricing Comparison: Code and Results](../03_Data_and_Code/Pricing_Competition/README.md)
- [Pricing Comparison: Optional Practice](../07_Labs/Pricing_Competition/README.md)
- [Digital Usage and Customer Access](../03_Data_and_Code/Digital_Usage/README.md)
- [Statistical Inference: Code and Results](../03_Data_and_Code/Statistical_Inference/README.md)
- [Statistical Evidence: Optional Practice](../07_Labs/Statistical_Inference/README.md)
- [Coding Workflows: Published Evidence](../01_Resources/40_Econometric_Coding_Workflows/README.md)
- [Coding Workflows: Python and Checks](../03_Data_and_Code/Agent_Workflows/README.md)
- ../01_Resources/41_Statistical_Claims_and_Decisions/README.md
- [Philosophical Arguments: Optional Practice](../07_Labs/Philosophical_Arguments/README.md)
- [Pricing, Individual Reasons, and Antitrust Practice](../07_Labs/Scanlon_Pricing/README.md)
- [Analytical Arguments: Python and Results](../03_Data_and_Code/Analytical_Arguments/README.md)
- [Five-Step Argument Practice](../07_Labs/Philosophical_Arguments/README.md)
- ../07_Labs/AI_Augmented_Learning/README.md
- [Conflicts of Interest: Optional Practice](../07_Labs/Conflicts_of_Interest/README.md)
- [Bad Controls and Project Exposure](../01_Resources/44_Bad_Controls_and_Project_Exposure/README.md)
- [Optional Research-Design Practice](../07_Labs/Bad_Controls/README.md)

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

## Slide 6: A Known Model is a Useful Verification Case

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

## Slide 9: Review of an Exported Recommendation

- Numerical agreement: the reported value matches its calculation.
- Interpretation: the sample and missing values support the stated claim.
- Export: equations, figures, and linked evidence remain usable.
- Publication: the reviewed files have appropriate release rights.

The synthetic-consumer report connects M1 Section 1.15 to M8 Section 8.25. Constant concept means leave a ranking unresolved; reversing the ranking retains zero of the reference top two. Neither calculation establishes real purchase demand. Suzuri 0.7.0 source inspection finds that wikilinks become display text, missing embeds can coexist with export success, and enabled synchronization can commit project files. These are static implementation findings; the application was not run. Reopen the actual exported file and inspect its links. A future multi-page site needs a separate navigation test.

Source: M8, Section 8.25. ../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md; ../01_Resources/30_Research_Writing_and_Coding/SOURCE_REVIEW.md

## Slide 10: Review Time is Part of Production

Synthetic workflows meet the same stated quality requirement.

**Figure description:** Manual production and review total 110 minutes. Assisted production and review total 85 minutes, a 22.7% total reduction despite a 50% drafting-time reduction.

[Editable TikZ](../06_Lecture_Notes/figures/M08_workflow_time.tex)

Suppose the manual workflow requires 90 minutes to produce an analysis and 20 to review it, while the assisted workflow requires 45 and 40. Total time falls by 25 minutes. The gain depends on comparable quality in the completed outputs.

Source: M8, Section 8.6, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md

## Slide 11: Hypothetical Cost of a Valid Analysis

| 100 Assigned Tasks | Basic | Checked |
| --- | --- | --- |
| API charges (dollars) | 10 | 20 |
| Review + correction (minutes) | 340 | 180 |
| Valid outputs | 80 | 95 |
| Total cost (dollars) | 350 | 200 |
| Dollars per valid output | 4.375 | 2.105 |

Invented inputs; analyst time costs 60 dollars per hour.

The numerator includes effort and charges from all assigned attempts, including failures. The valid-output denominator counts accepted final results after any allowed correction. Execution charges beyond the API are set to zero here. Greater API spending coincides with lower total cost under these inputs because analyst effort falls. This is an accounting illustration, not measured labor savings. Complete Python appears in M8 §8.26.

Source: Li and coauthors, Agent Harness Engineering: A Survey, §§8–9. Original course applications: ../01_Resources/35_Agent_Workflow_Evaluation/README.md ../03_Data_and_Code/Agent_Workflows/README.md

## Slide 12: Review Expense and Undetected Decision Errors

Hypothetical comparison: additional review breaks even at seven dollars per error.

**Figure description:** Two expected-cost lines for 1,000 tasks cross at loss seven dollars and total cost 620 dollars. The basic workflow has lower operating expense and more undetected errors.

[Editable TikZ](../06_Lecture_Notes/figures/M08_review_and_decision_cost.tex)

The API charges are 0.02 and 0.05 dollars per task, with review and correction times 0.25 and 0.50 minutes at 60 dollars per hour. The assumed undetected-error probabilities are 5% and 1%. At a loss of ten dollars, costs are 770 and 650 dollars. These operating assumptions are separate from the published benchmark. The common conditional loss must have the same scope; if error severity differs, use a workflow-specific loss. Customer rights require separate justification. Full Python appears in M8 §8.30.

Source: Original course example. Workflow motivation: Galiani, López, and Sosa, November 2026. ../01_Resources/40_Econometric_Coding_Workflows/README.md

## Slide 13: Reuse Has a Break-Even Workload

Hypothetical equal-quality work: six setup hours, with adaptation included.

**Figure description:** The existing process takes two hours per use. The reusable process takes six setup hours plus 1.5 hours per use, including upkeep. The lines cross at twelve uses and total 48 versus 42 hours at twenty-four uses.

[Editable TikZ](../06_Lecture_Notes/figures/M08_reuse_costs.tex)

Execution alone falls from two hours to 1.25, but 0.25 upkeep hours are required per use. Net savings become positive at the thirteenth use. Twenty-four uses save six hours, a 12.5% reduction after setup and upkeep. The numbers are imposed and do not measure course development time. Run investment.py and vary upkeep or workload.

Source: Marketing Analytics Lecture Notes, M8 §8.17.1.

## Slide 14: Model Updates and Unresolved Tasks

- Identify the changed model, prompt, tool, data, or evaluation rule.
- Compare paired cases and fresh tasks using the same criteria.
- Include regressions, review costs, and customer consequences in the decision.

A new release motivates a hypothesis about the current workflow. It does not establish improvement in the intended task population. Preserve the current procedure, predefine acceptance criteria, and retain a way to return to it. The claim-lifetime study motivates task-specific revalidation; it does not set a universal review interval.

Source: M8 §8.18.1; M7 §7.22. https://zou-group.github.io/llm-claims-shelf-life/

## Slide 15: Residual Risk and Scale

- An expired research category can still allow residual failures.
- Expected failure loss depends on uses, failure probability, and consequences.
- Verify that references exist and support the claims made.

A fitted category describes the source protocol and selected model panel. The relevant deployment criterion depends on customer outcomes and exposure. A decline in fabricated references leaves other checks necessary, including correct details and support for an assertion. Correct references do not identify authorship.

Source: M8 §8.18.1; M2 §2.21. ../01_Resources/14_LLM_Evidence_and_Revalidation/README.md

## Slide 16: AI Experimentation: Evidence and Safeguards

- Causal Alignment learns from comparisons within past A/B tests.
- Its field result concerns clicks, with human selection and content checks.
- Customer benefit and informed choice require additional evidence.

Panagiotis Angelopoulos, Kevin Lee, and Sanjog Misra; author version linked August 2026. Sections 4–5 report the randomized comparison; Appendix B screens unsupported claims and missing information. Respect those safeguards when critiquing the scope of the result.

Source: https://leekevin.io/caLM.pdf

## Slide 17: Personalized Pricing: Benchmark and Incidence

- Dubé and Misra study employers purchasing recruiting services.
- Their model predicts higher profit and lower total customer surplus.
- A majority benefits; the later field comparison uses different price policies.

The downloaded NBER June 2021 revision is linked to the published JPE 2023 paper. The 19% projected profit gain uses an optimized uniform benchmark. The rounded realized means in the later experiment imply about 10.1% higher revenue than its implemented uniform policy. Customer surplus is model-derived. This is a business purchasing setting, not an emergency retail case.

Source: https://www.nber.org/papers/w23775

## Slide 18: Majority Gains and Aggregate Customer Losses

Synthetic population and solved prices; dollars per eligible customer.

**Figure description:** Profit and customer surplus are compared on a common dollar axis for uniform pricing, segmented pricing, and capped discounts.

[Editable TikZ](../06_Lecture_Notes/figures/M09_pricing_distribution.tex)

The two imposed valuation groups have shares 0.6 and 0.4. Segmentation benefits 60% but lowers aggregate customer surplus. Discount-only pricing improves profit and customer surplus relative to the optimal uniform benchmark in this population. Full source and exact arithmetic appear in Section 9.17.

Source: Marketing Dialectics, Sections 9.16–9.17. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 19: Wendy's: Shared Data and Pricing Authority

- A proposed class action was filed on November 23, 2026.
- The complaint alleges coordination of franchise prices using shared transaction data.
- Evaluate the evidence linking data capability, pricing authority, and customer outcomes.

The initial complaint in Garcia v. The Wendy's Company and NCR Voyix Corporation, No. 8:26-cv-04886-LKG (D. Md.), alleges price fixing and unlawful information exchange. These are party allegations. Reuters reported on November 24 that neither defendant immediately responded to requests for comment. The 2022 data announcement and 2024 pricing clarification are separate sources, and the latter predates the lawsuit. Source status checked November 25; the live docket was inaccessible.

Source: Initial complaint, filed November 23, 2026; company statements and source review. ../01_Resources/37_Pricing_Systems_and_Competition/SOURCE_REVIEW.md

## Slide 20: Data Access and Authority over Prices

Data capability is described in company statements. Pricing authority is disputed.

**Figure description:** Sales records flow from two restaurants toward shared infrastructure. Dashed return paths show alleged pricing authority. Customers compare the resulting offers and other alternatives.

[Editable TikZ](../06_Lecture_Notes/figures/M08_pricing_authority.tex)

The diagram is conceptual. The solid data paths summarize announced capability, not a verified account of every franchise deployment. The dashed paths identify the coordination question raised by the complaint. Establish who supplies data, who receives recommendations, who can change prices, and what happens when an operator rejects a recommendation.

Source: Initial complaint, filed November 23, 2026; company statements and source review. ../01_Resources/37_Pricing_Systems_and_Competition/SOURCE_REVIEW.md

## Slide 21: Evidence for a Pricing Claim

- Identify separate owners, contracts, data permissions, and pricing authority.
- Compare recommendations, actual prices, overrides, costs, and promotions.
- Explain the counterfactual supporting any claimed customer overcharge.

Similar prices or a common vendor leave the mechanism unresolved. Adoption may respond to demand or costs, and nearby firms may react to each other. The DOJ and FTC's March 2024 statement in a separate hotel-pricing case argues that nonbinding recommendations do not by themselves defeat an agreement claim. It is an agency argument, not a ruling on Wendy's. Equipment-availability records do not supply transaction prices or agreement evidence.

Source: Initial complaint, filed November 23, 2026; company statements and source review. ../01_Resources/37_Pricing_Systems_and_Competition/SOURCE_REVIEW.md

## Slide 22: Noumena and Practical Standing

A complete statistical account would still leave practical justification to be defended.

**Figure description:** Four upper boxes distinguish established findings, recognized empirical gaps, unanticipated issues, and acknowledged epistemic limits. Recognition connects an unexpected issue to further inquiry. A lower box separates practical justification about ends, authority, and obligations.

[Editable TikZ](../06_Lecture_Notes/figures/M09_phenomena_noumena.tex)

Kant, Critique of Pure Reason B306–B311, distinguishes negative and positive noumena and limits human theoretical cognition. Hidden preferences, comprehension, and unrecorded costs remain empirical questions. Qualitative evidence also belongs to experience. The Groundwork, 4:428–429 and 4:451–453, provides distinct practical arguments about respect and the intelligible standpoint. Do not infer a specific hidden preference, harm, or duty solely from a limit of empirical knowledge. An unknown unknown has not yet been recognized. An acknowledged limit requires an argument about what a specified inquiry cannot establish. The phrase known to be the never known has that scoped role. Normative questions remain open to reasoned judgment; statistical non-identification can change with a new observable law.

Source: M1 §1.20 and M9 §9.41. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 23: A Measurable Objective Still Needs a Justification

- Predicting acceptance leaves consent and authority to be examined.
- Fitting heterogeneity leaves the person’s reasons to be considered.
- An average outcome leaves particular obligations to be justified.
- Defend which end the firm ought to pursue or abandon.

Examine the specific pricing and data-center arguments. Preserve their actual welfare results and safeguards. The criticism concerns a transition from empirical success to a complete account of welfare or permission. Kantian respect and Scanlonian reasonable rejection offer distinct practical arguments. Neither institutional affiliation nor ease of computation settles their validity. The analytical task begins with ends and authority, then uses evidence to evaluate consequences and alternatives.

Source: M1 §1.20 and M9 §9.41. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 24: A Spectrum of Ontological Adequacy

Assess the scope of an interpretation and the objects its decision requires.

**Figure description:** Five positions run from measurement as reality, through behavioral representation, institutions and procedures, agency and reasons, to acknowledged limits and justified scope. Three lower boxes apply the questions to household costs, price targeting, and cancellation. Positions carry no numerical distance or author score.

[Editable TikZ](../06_Lecture_Notes/figures/M09_ontological_spectrum.tex)

A small model can answer a narrow question well. Ontological laziness occurs when ease of measurement substitutes for an argument about what matters. Place a particular inference on the spectrum and name the omitted object that changes the decision. More variables alone do not improve its adequacy. Keep empirical mechanisms, practical reasons, and Kantian limits distinct.

Source: M9 §9.42. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 25: Measure and Claim in the Electricity Case

| Recorded Object | Further Question |
| --- | --- |
| Revenue per MWh | Bills and affordability |
| Operating capacity | Earlier financial exposure |
| Developer identity | Contractual business model |
| Average outcome | Household incidence |

Precision cannot repair a mismatch between the measure and the claim.

The paper explicitly measures realized revenue per MWh and explains its choice. Household bills require quantities, charges, periods, and a causal comparison; affordability adds household resources and needs. Operating entry can differ from the timing of committed costs. Developer identity requires validation before being treated as a business-model classification. Preserve the paper’s positive findings and qualifications. The criticism concerns an interpretation that exceeds these objects, without establishing a motive for the authors’ measurement choices. The complete bill arithmetic appears in M2 §2.28.1 and M6 §6.35.

Source: M9 §9.42.4. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md https://doi.org/10.1017/S0003055401003100

## Slide 26: Philosophical Objections to Reduction

| Argument | Question for the Analysis |
| --- | --- |
| Sellars: justification | What warrants this interpretation? |
| Bhaskar: ontology | Which mechanisms remain unobserved? |
| Husserl: intentionality | What is the person accepting? |
| Scanlon: normative reasons | Which reasons deserve an answer? |

Kant separately examines the conditions and limits of theoretical cognition.

These authors offer different arguments. They supply no common rejection of empirical inquiry. Sellars concerns the grounds of observational knowledge; Bhaskar permits inquiry into structures beyond event patterns; Husserl examines intentionality; Scanlon defends reasoning appropriate to normative domains. The exact source passages and contemporary applications are separated in M9 §9.43. Publication selection toward tractable questions is a hypothesis requiring evidence about the research process.

Source: M9 §9.43 and its primary-source links. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 27: Marketing Dialectics: Examine the Premise

- State the claim, its evidence, and the premise connecting them.
- Kant examines reason’s demand for an unconditioned explanation.
- A marketing analogy must preserve the scope of the original argument.

Kant’s transcendental dialectic concerns metaphysical cognition. These marketing cases adapt the practice of examining premises; an ordinary empirical dispute is not a cosmological antinomy. The third antinomy does not imply that accurate purchase prediction proves lost agency. Critical examination may support, restrict, or reject a claim; no forced synthesis is required.

Source: Marketing Dialectics, §§9.1–9.3. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 28: Definitions Can Predetermine a Claim

- Does cancellation mean a request or a completed action?
- Does predicted acceptance establish permission?
- Does a service label match its actual conduct?
- Trace the definition, evidence, and inference separately.

M9 §9.19 connects Kantian examination of an inference to the conditions supporting it, and Confucian rectification of names to the responsibilities conveyed by a service description. These are applications of the philosophical accounts in §§9.3 and 9.11. Consistency can coexist with false premises. A model score does not establish the legitimacy of the action it predicts.

Source: M9 §9.19. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 29: Authority and the Customer’s Requested Outcome

- A customer asks to cancel.
- The firm requires a retention survey before accepting the request.
- The agent follows the firm’s rule.
- Assess the customer’s authorization and the justification for the condition.

Technical permission, company authority, customer authorization, and ethical justification concern different relationships. A valid execution record establishes what happened under the rule. Kantian respect for persons asks whether the means respect the customer’s purposes and reasons. Confucian rectification of names connects the stated service role with its conduct. A higher renewal rate leaves the legitimacy of an imposed exit obstacle unresolved. M9 §9.20 develops the argument.

Source: Li and coauthors, Agent Harness Engineering: A Survey, §§8–9. Original course applications: ../01_Resources/35_Agent_Workflow_Evaluation/README.md ../03_Data_and_Code/Agent_Workflows/README.md

## Slide 30: Commercial Results and Customer Claims

Causal, measurement, and ethical questions have different premises.

**Figure description:** Separate paths connect a practice to commercial effects and customer outcomes. A judgment about the practice also requires an ethical principle.

[Editable TikZ](../06_Lecture_Notes/figures/M09_claim_scope.tex)

A randomized intervention can establish incremental purchases without establishing informed choice or customer benefit. Kant’s humanity formulation supplies a distinct ethical question about treatment of persons.

Source: Marketing Dialectics, §§9.1, 9.4. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 31: Advertising Response and Customer Reasons

- A joint test concerns whether any advertising coefficient differs from zero.
- Loan take-up leaves comprehension and borrower outcomes unresolved.
- Examine the information, reasons, and refusal available to customers.

The public P-Bench task describes a randomized consumer-credit advertising experiment and a joint null for 13 content coefficients. No empirical p-value is replicated in this course example. Rejecting a justified joint null would not identify every effective feature or a psychological mechanism. Kantian respect for persons asks how the firm treats customer judgment and refusal. Confucian role responsibilities concern the lender’s use of informational advantage and response to difficulty. Welfare claims require evidence beyond take-up.

Source: M9 §9.24. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 32: Self-Interest Creates a Burden of Justification

A reason for scrutiny is distinct from evidence of misconduct.

**Figure description:** A material stake leads to independent substantiation and then a decision that can change with evidence.

[Editable TikZ](../06_Lecture_Notes/figures/M09_burden_justification.tex)

Hume proposes institutional checks that work under private-interest pursuit and distinguishes that design maxim from universal dishonesty. Smith urges scrutiny of interested commercial-regulation proposals. Requiring firms to substantiate customer-benefit claims is a contemporary institutional recommendation, not a universal legal presumption of guilt. A duty-based conflict is distinguished from ordinary opposing interests in §9.45.

Source: Marketing Dialectics, §9.10. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 33: Commercial Rewards and Analytical Judgment

Specify the responsibility that a competing interest threatens.

**Figure description:** Employer rewards and responsibilities both influence analytical judgment. A decision affects users, whose effective challenge can change its objective and interpretation.

[Editable TikZ](../06_Lecture_Notes/figures/M09_conflict_judgment.tex)

Commercial incentives can shape which outcomes are collected before they affect any coefficient. Valsan’s account locates a conflict in an interest that threatens judgment owed under a duty. The platform example also raises broader questions about power and consumer control. Scrutiny and safeguards can be appropriate before misconduct has been established.

Source: M9 §9.45. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 34: Reward Learning and the Scope of Evidence

- Posting studies and reward experiments inform behavior.
- Behavioral records do not measure dopamine release.
- Habit and self-control evidence concerns specified interventions.
- Evaluate the feed, the user’s purpose, and unwanted continuation.

Lindström and coauthors study posting and experimentally varied social rewards. Schultz, Dayan, and Montague examine dopamine-neuron activity in a separate neuroscience setting. Allcott, Gentzkow, and Song study temporary incentives and user-selected limits with an economic model. These sources provide different evidence. None alone identifies clinical addiction caused by an infinite-scroll feature. The ethical question concerns the actual design, its consequences, and the user’s authority to stop.

Source: M9 §9.46 and its source links. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 35: Reasons for Honoring a Stopping Instruction

Defend the factual and normative premises, then compare objections.

**Figure description:** Evidence about an overridden instruction and a feasible alternative combines with a principle of revocable authority. Comparison of affected people’s objections leads to a conditional ought conclusion and revision.

[Editable TikZ](../06_Lecture_Notes/figures/M09_engagement_reasons.tex)

State the principle permitting a firm to override a boundary for revenue and compare it with user-directed continuation. A time-limited user, an entertainment user, and a worker or creator occupy different positions. Scanlonian justification examines reasons for rejecting principles. It is not a vote or a weighted sum of engagement. A Kantian assessment examines the maxim and the person’s capacity to set ends.

Source: M9 §9.47. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 36: A Synthetic Feed Decision

- Fixed population: 1,000 adult user-days per design.
- Endless feed: USD 0.314 contribution; 85.6% goal completion.
- User controls: USD 0.236 contribution; 91.8% goal completion.
- A stopping requirement changes the feasible set before ranking.

The constructed population contains 800 leisure and 200 time-limited users. Under endless use, leisure goal completion improves relative to the finite feed while the time-limited group’s completion falls. Disclosure alone is assigned identical outcomes for a logical comparison, not an empirical estimate. All counts use the original group denominators. A requirement to honor a valid stopping instruction needs philosophical justification outside the score.

Source: M9 §9.48. ../03_Data_and_Code/Conflicts_of_Interest/README.md

## Slide 37: Justify the Practice Before Ranking Its Performance

A commercial ranking also needs a justified set of permissible actions.

**Figure description:** Proposals pass through restrictions concerning truthful claims, data use, and refusal before performance ranking. Customer evidence can require revision.

[Editable TikZ](../06_Lecture_Notes/figures/M09_optimization_boundary.tex)

Kantian duties cannot automatically be replaced by a finite penalty in an objective function. The proposed restrictions are contemporary applications requiring explicit justification. Human review and measured outcomes provide evidence; they do not mechanically define autonomy. For pricing, state a maxim that identifies the purpose and means. Compare truthful use of a demand forecast with a hypothetical concealed pricing arrangement. Evaluate the customer's capacity to understand and refuse the offer. A profitable result supplies no premise about permission; these hypothetical maxims establish no finding about the defendants' intentions.

Source: Marketing Dialectics, Sections 9.16–9.17. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 38: Confucian Perspectives: Profit and Responsibility

- Evaluate how profit is obtained and which relationships sustain it.
- A trusted adviser or customer-care role carries standards of conduct.
- Examine whether the claimed role matches incentives and practice.

Analects 4.5 and 4.16 place righteousness in the evaluation of gain; Mencius 1A.1 challenges an exclusive focus on advantage. Analects 12.7 and 13.3 motivate trustworthiness and fit between names, roles, and conduct. These are contemporary applications of texts with historical political settings. A profitable exchange can serve both parties. In the restaurant case, compare claims of franchise pricing independence and customer benefit with actual authority and measured outcomes. Trustworthiness concerns the accuracy of that account. Examine how the pricing team handles evidence of customer losses and truthful employee objections.

Source: Marketing Dialectics, §§9.11.1–9.11.2. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 39: Truthful Challenge and Cultivated Judgment

- Harmony can include reasoned disagreement.
- Learning and reflection should discipline an AI-generated answer.
- Good conduct depends on repeated practices as well as stated values.

Analects 13.23, 14.22, and 2.15 support discussion of truthful challenge and reflective learning. Mencius emphasizes cultivable moral beginnings; Xunzi emphasizes deliberate effort, teaching, and ritual. They disagree about human nature. A modern firm can examine what its rewards teach employees to notice and whether an analyst can report an unwanted customer outcome.

Source: Marketing Dialectics, §§9.11.3–9.11.4. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 40: Synthetic Personas and Actual Consumers

- Generated reactions can inform hypotheses about product needs.
- Claims about customer preferences require evidence from the relevant people.
- Customers need opportunities to express conditions and contest consequential interpretations.

M9 §9.18.4 examines whose judgments a firm claims to represent. Kantian respect concerns affected people’s purposes and judgment. Confucian trustworthiness requires a truthful account of what the evidence represents and responsible responses to objections. The M4 case holds overall rating distributions fixed while reversing the product ranking. Accuracy alone supplies no permission to substitute generated consent for a person’s decision. These are arguments about a practice, with no inference about the researchers’ motives.

Source: Marketing Dialectics §9.18.4. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 41: Agreement and Independent Reasons

- Identify shared data, labels, and objectives behind agreement.
- Check the claim against evidence with a justified reference.
- Distinguish predicted behavior from customer purposes.
- Justify the proposed action and the means used.

Several models can agree because they share conventions and information. In mHealth, agreement with a modal category measures reproduction of a recorded category system. It does not establish nutritional correctness. In retention, a prediction of payment does not establish customer consent or justify an obstacle to cancellation. Kantian evaluation examines the maxim and respect for choice; Confucian rectification of names asks whether a claimed service fits its conduct. These are course applications of the earlier philosophical discussions.

Source: M9 §9.21. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 42: Demand Information and Consumer Surplus

| Objective | Signal $r$ | Profit | Consumer Surplus |
| --- | --- | --- | --- |
| Independent | 0.5 | 29.63 | 32.30 |
| Independent | 1.0 | 30.81 | 30.81 |
| Joint | 0.5 | 33.33 | 19.33 |
| Joint | 1.0 | 34.67 | 17.33 |

Synthetic market; expected dollars per market-day. Preferences and costs are fixed.

First hold the objective fixed and improve the demand signal. Then hold information fixed and change the objective. The first comparison can reduce consumer surplus while firms retain independent objectives. The second replaces independent price setting with joint profit maximization. Total welfare adds both monetary columns. The values are solved under quasi-linear preferences with no income effects, vendor fees, or externalities. Run evaluate_market.py and check the exact fractions.

Source: Original synthetic model. M4 Section 4.26. ../03_Data_and_Code/Pricing_Competition/README.md

## Slide 43: A Choice Procedure Can Change Renewal

- A direct offer and an offer preceded by questions can produce different choices.
- The customer still makes the final selection.
- An independent value measure determines whether an additional renewal benefits that customer.

Questions, defaults, or retention prompts can precede a fixed target decision. The welfare comparison depends on consumer values, stable response probabilities, and the procedure set. A renewal increase alone does not establish either benefit or harm.

Source: M8, Section 8.14, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md

## Slide 44: Opposed Interests

Suppose renewal yields firm margin $\nu>0$ and costs the customer $\sigma>0$ relative to declining.

$$
\Delta\Pi=\nu(s-s_0),\qquad \Delta V=-\sigma(s-s_0)
$$

A higher renewal probability raises profit and lowers customer value under these stated stakes.

This conditional comparison holds the offer, monetary values, and relevant response population fixed. It does not infer customer harm from conversion alone. Additional time and authority costs require separate measurement.

Source: M8, Section 8.14, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md

## Slide 45: Profit and Customer Value Can Move Oppositely

Synthetic probabilities and fixed stakes. Direct renewal is 20%.

**Figure description:** An optional procedure lowers renewal to 10%; another raises it to 60%. At firm margin 11 dollars and customer loss 10 dollars per unwanted renewal, the latter gains the firm 4.40 dollars and costs the customer 4 dollars relative to direct choice.

[Editable TikZ](../06_Lecture_Notes/figures/M08_retention_welfare.tex)

The direct-choice benchmark is distinct from the consumer-preferred procedure. Relative to the 10% procedure, the 60% procedure creates a 5-dollar customer loss. These probabilities and monetary values are imposed inputs, not observed customer responses.

Source: M8, Section 8.14, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md

## Slide 46: Experimentation Selects the Commercial Winner

- A fixed set of procedures has stable renewal probabilities.
- Independent randomized samples estimate each probability.
- With opposed interests, accurately selecting the largest rate also selects the largest loss in that set.

The result requires common fixed stakes, a fixed catalog chosen before the experiment, stable responses from experiment to deployment, and complete independently sampled outcomes. It does not say that every experiment harms consumers.

Source: M8, Section 8.14, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md

## Slide 47: Evidence for a Small Cancellation Burden

Hypothetical summary statistics and prespecified five-second bounds.

**Figure description:** An imprecise nonsignificant estimate fails equivalence. A precisely estimated small positive effect can satisfy equivalence despite differing from zero.

[Editable TikZ](../06_Lecture_Notes/figures/M09_equivalence_and_burden.tex)

Two one-sided tests at 5% require the 90% t interval within both bounds. A six-second reduction fails two-sided equivalence but excludes excessive added time through its one-sided upper bound. Choose the hypothesis and justify the threshold before observing the result. Completed-task time leaves failures and abandonment as separate outcomes.

Source: M9 §§9.25–9.26. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 48: Public Reassurance Exceeds the Reported Evidence

- HBS coverage states that the four large firms have not raised consumer electricity costs.
- The reported cloud-owner coefficient is positive and imprecise.
- Categorical harmlessness requires evidence that excludes consequential harm.

The verified communication is HBS Working Knowledge, November 12, 2026, and company dissemination remains unverified. It also acknowledges future uncertainty. Table 4 permits positive price effects and reports p=0.101 for the direct developer contrast. Misleading reassurance could weaken safeguards or scrutiny; attributing actual policy changes or losses to the paper requires separate evidence. The paper has positive findings in other specifications, so calling the entire paper a null result is inaccurate.

Source: M9 §§9.25–9.26. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 49: The Same Average Can Conceal Unequal Burdens

Synthetic monthly cost allocations; fixed use and population.

**Figure description:** Uniform and concentrated cost allocations yield the same aggregate price increase. Neither allocation reveals authority to assess or contest the rule.

[Editable TikZ](../06_Lecture_Notes/figures/M09_household_incidence_and_agency.tex)

Both scenarios add USD 2,000 to bills for 1,000 households using one MWh each. Distributional evidence distinguishes the allocations. Agency evidence concerns access to reasons, review, correction, and remedy. The average price coefficient does not measure those relations. The complete calculation is in M6 §6.33.

Source: M9 §§9.25–9.26. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 50: Ontology, Evidence, and Justification

- Ontology: distinguish utilities, households, ownership, contracts, and authority.
- Evidence: identify which claims the estimates and bounds support.
- Justification: explain why affected people may bear the remaining risk.

A narrow price study can be valid within its scope. The category error occurs when its aggregate becomes a complete account of household harm or agency. Four named owners versus other owners is not automatically cloud provision versus colocation. Thomasson’s functional assessment asks whether categories serve the decision. Compliance with a rule, endorsement of its reasons, and authorization remain distinct.

Source: M9 §§9.25–9.26. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 51: Respect for Persons Requires Honest Uncertainty

- An interested party owes reasons for imposing costs on others.
- An insensitive test cannot certify safety through nonrejection.
- Preserve opportunities to challenge evidence and obtain review.

Kantian universalization examines a rule that advertises safety whenever a test fails to reject, regardless of sensitivity. Such a practice rewards weak measurement and undermines evidentiary trust. The humanity formulation treats households as persons capable of judgment. Confucian trustworthiness requires descriptions that match conduct and a responsible response to inconvenient findings. Self-interest motivates substantiation; it does not establish guilt or deliberate deception.

Source: M9 §§9.25–9.26. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 52: Validity Leaves the Premises Open to Challenge

- Suppose every revenue gain justified adoption.
- A proven revenue gain would then support adoption.
- The first premise grants revenue priority over other reasons.
- Defend that premise to the people bearing the burden.

The conditional deduction is valid, while soundness also requires true premises. Evidence for the revenue effect does not establish the normative premise. MacFarlane distinguishes logical consequence from norms governing reasoning; Scanlon supplies a separate account of justification to affected people. Ordinary empirical evidence remains defeasible and should be evaluated according to the claim actually made.

Source: M9 §9.40. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 53: Preserve Meaning Through the Argument

- A purchase is evidence of a transaction.
- Consent requires an account of information and authority.
- A unit price and a household bill measure different objects.
- Feasible, permitted, and obligatory actions require different premises.

Terms must keep their meanings across premises and conclusion. Willingness to pay, benefit, and acceptable treatment are distinct claims. A formal option can remain difficult to exercise or unknown. Permission does not establish an obligation. Record operational definitions, populations, and time horizons before evaluating a result.

Source: M9 §9.40. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 54: A Counterexample Must Preserve the Premises

Assess the original recommendation and its criticism through the same five steps.

**Figure description:** The diagram moves from a defined claim to its premises, a proposed counterexample, assessment of a missing premise, and a revised conclusion. The revision returns to the claim.

[Editable TikZ](../06_Lecture_Notes/figures/M09_argument_revision.tex)

Use the exact source passage. A construction can demonstrate that an inference fails without showing that the constructed mechanism occurs in the actual setting. The critic should defend the added empirical or normative premise and state what evidence or reasons would change the conclusion. The optional argument record keeps these tasks separate.

Source: M9 §9.40. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 55: Write the Missing Premise

- Nonrejection becomes harmlessness only by adding an unsupported sensitivity claim.
- An owner-list complement becomes a business model only with classification evidence.
- An arithmetic residual becomes a causal account only with identification.

Reconstruct each claim from its exact source. Table 4 and HBS coverage supply the reassurance example; Section 4.1 defines the owner groups; page 3 attributes the residual growth to named causes. Grant correct calculations before challenging their interpretation. A counterexample must preserve the stated premises. A reporting inconsistency, an unsupported extension, and a contradiction are different findings.

Source: M9 §9.27. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 56: Historical Agreement Leaves Future Costs Open

A synthetic capacity threshold changes extrapolation while preserving historical responses.

**Figure description:** Two functions coincide for normalized load from zero to one. At load two, the linear function reaches four dollars/MWh and the threshold function reaches fourteen. The shaded area denotes the assumed historical support.

[Editable TikZ](../06_Lecture_Notes/figures/M09_counterexample_extrapolation.tex)

The construction grants exact knowledge throughout the historical support. The linear and threshold accounts still imply different future costs. Choosing one requires an extrapolation premise or additional evidence. The example estimates no actual capacity threshold. The paper acknowledges future uncertainty; preserve that qualification when assessing stronger public claims. Full original code is logical_counterexamples.py.

Source: M9 §9.27. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 57: What Ought the Firm Do?

- Identical bills can coexist with different opportunities to challenge a decision.
- State the factual premises and the principle governing affected people.
- Defend a conclusion about what the actor ought to do.

Payment records conduct under available conditions. Endorsement, permission, and ethical justification need further evidence or reasons. Scanlon's approach compares principles through the reasons people could have for rejecting them. A hypothetical jurisdiction with inaccessible decisions can differ from one with an effective challenge procedure even when bills coincide. State the circumstances, identify a feasible alternative, and answer the strongest objection.

Source: M9 §§9.27–9.32. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 58: Flat Average Prices Can Accompany Higher Bills

- Average bill equals average revenue per MWh times mean use.
- Synthetic fixed population: USD 100/MWh with bills rising from USD 100 to USD 110.
- Causal claims also require an explanation of why prices and use changed.

The example holds 1,000 customer accounts fixed and raises monthly sales from 1,000 to 1,100 MWh with unchanged average revenue per MWh. It attributes no change to data centers. The paper recognizes realized payments and regulatory allocation. Its outcome is economically meaningful, but it does not by itself identify household expenditure, affordability, or welfare. Fixed charges can already enter its revenue numerator. Full code appears in M6 §6.35; the matched customer-month identity is in M2 §2.28.1.

Source: M2 §2.28.1 and M6 §6.35. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md

## Slide 59: Project Status Does Not Settle Responsibility

- Investment can create obligations before a center operates.
- Cancellation may leave costs, developer guarantees, and a recovery decision.
- Assess who authorized the risk and who can challenge its allocation.

A utility with zero operating additions can still be exposed to project-related costs. The missing premise is absence of preparatory obligations and later recovery. The Bloomberg ComEd report motivates examining the pipeline; contracts and regulatory decisions determine incidence. Those sources do not identify affected donors in the paper. A defensible critique requests dated project histories, donor weights, collected guarantees, and cost-allocation records. The comparison and its direction remain conditional on those facts.

Source: M9 §9.27.6 and institutional assessment. ../01_Resources/41_Statistical_Claims_and_Decisions/INSTITUTIONAL_ASSESSMENT.md

## Slide 60: From Premises to an Ought Conclusion

Facts and a defended principle jointly support a conditional recommendation.

**Figure description:** Factual and normative premises enter an application question, followed by an ought conclusion. The strongest objection can send the argument back to either premise.

[Editable TikZ](../06_Lecture_Notes/figures/M09_argument_premises.tex)

The hypothetical customer has made a verified cancellation request, and a secure prompt exit is feasible. The proposed principle respects valid withdrawal while requiring justification of remaining burdens. Assess fraud, service continuity, and implementation cost. A factual premise needs evidence; a normative premise needs reasons. An objection can change either.

Source: M9 §§9.30–9.32; selected Scanlon and stakeholder readings. ../01_Resources/15_Marketing_Dialectics/07_Stakeholders_and_Reasons/README.md

## Slide 61: Compare Reasons for Rejecting Each Principle

Compare affected positions and feasible alternatives; answer the strongest objection.

**Figure description:** Two columns compare mandatory retention with prompt secure exit. Each considers customer reasons alongside security and service interests. A surviving objection leads to revision of the alternative.

[Editable TikZ](../06_Lecture_Notes/figures/M09_reasonable_rejection.tex)

Scanlon's reasonable rejection is a judgment about reasons under principles of general regulation. It is not a vote or an automatic veto. In this hypothetical case, optional offers preserve persuasion without imposing it as a condition of exit. The comparison assumes necessary protections can be supplied at reasonable cost. A surviving objection requires revising the alternative or the conclusion.

Source: M9 §§9.30–9.32; selected Scanlon and stakeholder readings. ../01_Resources/15_Marketing_Dialectics/07_Stakeholders_and_Reasons/README.md

## Slide 62: Stakeholders Beyond the Firm

- Identify people affected even when they are absent from the dataset.
- Separate managerial attention from the justification of a duty.
- State each person's interest, supported exposure, and reason for objection.

Donaldson and Preston distinguish descriptive, instrumental, and normative uses of stakeholder theory. Mitchell, Agle, and Wood analyze salience through power, legitimacy, and urgency. Phillips examines obligations of fair cooperation; general duties still matter for involuntarily affected people. A low-power resident's moral standing does not depend on the cost they can impose on the firm. Identify the actual relationship and defend the proposed obligation.

Source: M9 §§9.30–9.32; selected Scanlon and stakeholder readings. ../01_Resources/15_Marketing_Dialectics/07_Stakeholders_and_Reasons/README.md

## Slide 63: Whose Voice Can Challenge a Prestigious Claim?

- Hypothetical headline: “Harvard/Wharton study shows no harm.”
- Compare its reach with residents' access to records and technical help.
- Require evidence for reassurance and a substantive answer to material objections.

The headline is a discussion construction, not a verified quotation or institutional endorsement. The HBS Working Knowledge article is the documented public communication. Fricker's prejudice-based credibility deficit requires evidence beyond unequal credentials. Anderson motivates examining institutions that gather and assess testimony. Distinguish nearby residents, utility customers, and people bearing costs. Local experience can identify an outcome; causal attribution requires a comparison. Institutional prestige supplies no missing premise. Verify actual use of a claim in a proceeding before alleging that it silenced objections.

Source: M9 §§9.30–9.32; selected Scanlon and stakeholder readings. ../01_Resources/15_Marketing_Dialectics/07_Stakeholders_and_Reasons/README.md

## Slide 64: Mechanism Evidence and Public Reassurance

- Calls and filings document recovery plans and competing claims.
- The electricity paper itself permits recovery and positive spillovers.
- Assess the scope of reassurance separately from the historical coefficient.

New 2026 disclosures raise questions about future costs and allocations beyond the 2020–2025 historical window. They do not overturn that coefficient by themselves. PSEG's February 2025 residential-bill statement concerns wholesale capacity and procurement, which is a separate channel from construction cost recovery. M6 §6.36 develops the causal comparison.

Source: M5 §5.27. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md M9 §9.33. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 65: Whose Account of Affordability is Missing?

- Investor calls give management and financial analysts a structured voice.
- Household experience and authority require additional sources.
- An institution ought to substantiate burdens and address material objections.

Distinguish a factual recovery plan from the normative claim that affected people deserve examinable reasons. Consider the objection that excessive delay may obstruct beneficial investment. Retain credible offsets and feasible protections when evaluating that objection. Public comments and consumer-counsel filings can extend the documentary record; interviews require an appropriate separate design. Hsieh and Shannon (2005), https://doi.org/10.1177/1049732305276687; O'Brien et al. (2014), https://doi.org/10.1097/ACM.0000000000000388; Gale et al. (2013), https://doi.org/10.1186/1471-2288-13-117; O'Connor and Joffe (2020), https://doi.org/10.1177/1609406919899220; Braun and Clarke (2021), https://doi.org/10.1080/14780887.2020.1769238.

Source: M9 §9.33. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 66: When Ought a Research Claim Be Published?

- Identify the evidence worth preserving and the interpretation needing support.
- Compare a corrected release, further review, and rejection of the proposed version.
- For a public error, assess a visible correction that preserves traceability.

A paper need not be released in a form that attaches unsupported reassurance to useful estimates. Mill supplies reasons to preserve criticism and inquiry. Registered Reports illustrate reviewing design before learning the direction of results. Scanlon's approach asks which release principle can be justified to affected people, readers, researchers, and decision makers. Neither favorable nor unfavorable implications for a firm establish research quality. The remedy should address a demonstrated defect.

Source: M9 §§9.28–9.30. ../01_Resources/41_Statistical_Claims_and_Decisions/PUBLIC_COMMUNICATION_AND_PUBLICATION.md

## Slide 67: Favorable Framing and Justified Acceptance

- Pricing language may emphasize discounts, flexibility, or convenience.
- Research coverage may emphasize reassurance about consumer costs.
- Trace the selected comparison and beneficiary to supporting evidence.

The verified Wendy's February 27, 2024 statement describes intended digital-board uses and rejects plans to raise prices at the busiest times. The HBS article interprets an empirical study. The comparison concerns framing and the reasons for acceptance; it establishes no common campaign or motive. Assess actual offers, outcomes, uncertainty, and omitted conditions. A persuasive message needs a further justification when it affects public choices.

Source: M9 §9.31. ../01_Resources/41_Statistical_Claims_and_Decisions/PUBLIC_COMMUNICATION_AND_PUBLICATION.md

## Slide 68: A Cancellation Evaluation

- Include a direct-cancellation comparison.
- Record whether optional retention content can be refused before exposure.
- Measure completion, elapsed time, subsequent charges, and customer value.

An effective refusal path and an independent value measure reveal dimensions hidden by renewals. A direct-choice arm helps isolate the effect of the preceding interaction.

Source: M8, Section 8.14, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md

## Slide 69: Same Renewal, Different Customer Intent

Synthetic populations: 1,000 customers each, one renewal month.

**Figure description:** A and B each have 900 billed customers. A contains 880 wanted and 20 unwanted renewals; B contains 600 wanted and 300 unwanted renewals. Both have 100 not billed.

[Editable TikZ](../06_Lecture_Notes/figures/M09_retention_intent.tex)

Intent is stipulated before billing. All-customer unwanted shares are 2% and 30%; among billed customers they are approximately 2.22% and 33.33%. These populations do not estimate a treatment effect or monetary welfare. Run evaluate_retention.py; full source is in Section 9.5. Missing intent stays unknown.

Source: Marketing Dialectics, §9.5. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 70: A Welfare Comparison

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

## Slide 71: Coding Exercise: A Marketing Evaluation

- Reproduce the two populations with identical billed renewal.
- Keep unknown intent separate and compare the relevant denominators.
- State the evidence and ethical premise needed to justify the practice.

Run ../03_Data_and_Code/Marketing_Dialectics/evaluate_retention.py. The full program and five tests accompany M9 §9.5. The synthetic comparison holds the eligible roster fixed and calculates the stated retention outcomes. Compare the conditional profit and customer-value consequences in M8.

Source: ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 72: Federal Cancellation Policy: Current Status

- July 2025: the Eighth Circuit vacated the 2024 FTC rule.
- February 2026: the FTC restored the earlier prenotification rule.
- March 2026: an advance notice sought input on possible amendments.

Checked November 5, 2026. The court identified a procedural deficiency. The March notice does not establish a replacement obligation; the October 14 information-collection notice concerns the restored rule. ROSCA separately requires disclosure, express informed consent, and simple cancellation mechanisms for covered online negative-option transactions.

Source: ../01_Resources/13_Consumer_Agency_and_Recent_Research/Policy/README.md

## Slide 73: Cancellation Rules Differ by Jurisdiction

- California strengthened its Automatic Renewal Law on July 1, 2025.
- New York City's separate rule took effect October 1, 2026.
- Identify covered transactions, enrollment media, and sector exceptions.

California guidance describes online cancellation without obstruction for online enrollment. NYC Section 5-110.2 requires simple cancellation as easy as enrollment and bars obstruction or unreasonable delay. Retention offers are subject to those restrictions; Section 5-110.3 contains sector exclusions. These sources were checked November 5, 2026. See M8 Section 8.19.

Source: ../01_Resources/13_Consumer_Agency_and_Recent_Research/Policy/README.md

## Slide 74: Research Frequency and Policy Importance

- Social influence leads the selected literature clusters.
- Exit friction can affect many customers even with few papers in the sample.
- Choose safeguards using mechanism, exposure, and customer consequences.

Journal counts give each paper equal weight and do not measure market exposure or loss. The 48-paper primary sample is access-selected and largely coded for inferred dual use. The full DOI census contains 824 eligible records with 721 full-text gaps. See M4 Section 4.17 and M8 Section 8.19.

Source: ../03_Data_and_Code/Consumer_Agency_Literature/README.md

## Slide 75: Pricing, Reviews, and Delivery

- Price-display rules require attention to the covered industry.
- Reviews presented as customer experiences require truthful provenance.
- Housing-ad delivery can create discrimination concerns beyond targeting choices.

The FTC fee rule covers live-event tickets and short-term lodging. Its review rule distinguishes business creation and purchase of false reviews from mere hosting. The DOJ Meta settlement addresses housing advertising specifically. These sources do not establish an identical rule for every marketing application.

Source: Primary-source scope and status record: ../06_Lecture_Notes/ETHICS_AND_REGULATION.md.

## Slide 76: Pricing Language and Regulatory Evidence

- Shelf infrastructure, price rules, and consumer effects are separate objects.
- The FTC's January 2025 report describes research on pricing intermediaries.
- Specify the practice and applicable authority before making a legal claim.

The US FTC Section 6(b) staff research summaries report preliminary findings. This research publication has no rule effective date and supplies no legal finding against firms in the earnings-call sample. Use the source-linked cases from M5 to identify operational facts still needed.

Source: M8, Section 8.16. FTC, January 2025, pp. 1–3. https://www.ftc.gov/system/files/ftc_gov/pdf/p246202_surveillancepricing6bstudy_researchsummaries_redacted.pdf

## Slide 77: Personalized Pricing: Policy Status

- FTC: August 2026 proposal; October 2026 information-gathering inquiry.
- New York: disclosure law in effect; broader restrictions await enactment.
- Price gouging requires its own covered circumstances and legal elements.

Checked November 6, 2026. FTC proposal cites Dubé and Misra. October 28 Section 6(b) orders do not establish violations. New York GBL 349-a applies to covered personal, family, and household purchases, with exceptions. S8623B/A9349B has legislative passage without recorded gubernatorial enactment. GBL 396-r addresses essential goods and services during abnormal market disruptions.

Source: ../01_Resources/16_AI_Experimentation_and_Pricing/02_Policy/README.md

## Slide 78: Environmental Claims: Two Different Decisions

- 2023 Shell ads: the ASA upheld the overall-impression complaint.
- 2025 Shell ad: the ASA accepted the contextualized communication.
- Evaluate the particular claim, material context, and applicable standard.

UK ASA, June 7, 2023: omitted context about the balance of business activities made the overall environmental impression misleading; a separate electricity claim was not upheld. April 9, 2025: the later ad included higher- and lower-carbon activities and investment context and was not found misleading. Its ruling explains the applicable pre-April-2025 code wording. These are specific regulatory outcomes, not firm-wide ethical verdicts. Sources: https://www.asa.org.uk/rulings/shell-uk-ltd-g22-1170842-shell-uk-ltd.html and https://www.asa.org.uk/rulings/shell-uk-ltd-g24-1248246-shell-uk-ltd.html

Source: Marketing Dialectics, §9.8. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 79: A Product Fact and a Portfolio Impression

The scope of the conclusion determines the evidence required.

**Figure description:** The product, portfolio, and future transition require different supporting information: comparison, denominator, and time horizon.

[Editable TikZ](../06_Lecture_Notes/figures/M09_environmental_scope.tex)

A true statement about one product can be insufficient to support a broader impression. The ASA comparison supplies an institutional case; the diagram is an original conceptual analysis.

Source: Marketing Dialectics, §9.8. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 80: Digital Service and Feasible Customer Choice

- Offer assistance while preserving a usable alternative.
- Measure completion, customer time, and firm cost on a fixed roster.
- Treat geographic usage as context for investigation.

An optional assistance intervention can expand feasible choices. A mandatory app workflow may impose equipment, registration, and verification costs. A proposed evaluation should record the customer’s requested action and channel and preserve the ability to refuse optional profiling. Geographic Windows usage does not observe those outcomes.

Source: Pereira et al., Nature Communications (2026); original course calculations. ../01_Resources/38_Digital_Usage_and_Inclusion/README.md

## Slide 81: Evidence and Authority to Classify a Customer

- Kantian critique examines the move from area activity to individual ability.
- Respect for persons requires reasons for restrictions and usable correction.
- Confucian role responsibilities support responsive, humane service.

A stable cluster does not authorize a firm to remove an individual’s options. Examine the additional premise linking measured activity to a permissible action. Humane intent must be connected to the customer’s stated task and preferred channel, with an opportunity to correct classifications. The same area score can motivate assistance or exclusion; the consequences and authority differ.

Source: Pereira et al., Nature Communications (2026); original course calculations. ../01_Resources/38_Digital_Usage_and_Inclusion/README.md

## Slide 82: Reliable Measurement and a Worthy Objective

Unbiasedness and precision support factual premises. The goal and treatment of people require reasons.

**Figure description:** Reliable evidence informs a revenue objective. Personal reasons inform an alternative principle. Compare objections to both, including burdens, access, authority, and feasible alternatives.

[Editable TikZ](../06_Lecture_Notes/figures/M09_pricing_reasons.tex)

Statistical unbiasedness concerns an estimator across repetitions of a specified design; precision concerns its dispersion. Both can protect people against mistaken claims. Even perfect measurement of all monetary consequences leaves a normative premise to defend before recommending revenue maximization. Scanlon’s account of reasons and reasonable rejection grounds the course application; he is not being presented as proposing a theory of statistical estimation. The same requirement applies to every institution and research method. Dubé and Misra’s own finding of lower aggregate customer surplus remains part of the evidence.

Source: ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 83: Rational Acceptance and Reasonable Objection

- Instrumental rationality: an effective choice for a selected aim.
- Reasonableness: a principle justified through affected people’s reasons.
- Weak alternatives can explain acceptance while sustaining a strong objection.

Suppose an urgently dependent customer accepts a surcharge that a seller predicts exactly. The seller and customer can each act effectively for their immediate aims while the rule faces an objection to avoidable exploitation. Examine the feasible lower offer, the seller’s costs and risks, and the reasons of other affected people. Instrumental rationality is one sense of rationality; broader rational thought can include morality. Reasonableness is neither majority preference nor an unconditional veto. State what fact or reason would change the conclusion.

Source: Scanlon, What We Owe to Each Other, chapter 5, §2, pp. 191–194. https://e-edu.nbu.bg/pluginfile.php/314831/mod_resource/content/0/scanlon_5.1-3.pdf

## Slide 84: Pricing and Public Reassurance

- Personalized prices: predicted acceptance and authority to impose a burden.
- Dynamic pricing: discount claims, full price paths, and usable alternatives.
- Data centers: average-price evidence, household exposure, and a voice in allocation.

The practices share a need to justify consequential treatment to affected people. Personalization uses customer information; dynamic pricing can change a common price over time. Wendy’s documented statement concerns its announced policy, with implementation requiring evidence. The data-center case retains the criticisms of inference and public interpretation. Even exact knowledge of a narrow historical effect would leave future cost recovery, household bills, failed projects, and participation unresolved. Nearby residents, utility customers, and eventual cost bearers are distinct populations. Compare a rule allowing favorable evidence to close debate with proportionate substantiation and answers to material objections. Similarities do not establish identical harms or motives.

Source: M9 §§9.26, 9.31–9.34 and M5 §5.27. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 85: Same Tested Demand, Opposite Welfare Signs

Synthetic population: L 60%, H 40%. Surplus changes are −USD 1.682 and +USD 0.682.

**Figure description:** Two panels share a zero-to-one probability scale. Solid blue and dashed orange curves match tested endpoints but enclose different areas as prices change.

[Editable TikZ](../06_Lecture_Notes/figures/M09_demand_completions.tex)

The baseline price is USD 10 for both groups. The candidate schedule charges L USD 5 and H USD 20. Revenue rises from USD 6.20 to USD 6.70 in both completions. Quasilinear unit demand makes surplus changes areas under demand. Monotonicity bounds the population change between −USD 1.70 and +USD 0.70. Both completions harm H; finite support leaves the aggregate sign unresolved. This construction does not establish bias in the empirical paper.

Source: ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 86: A Majority Benefits While a Minority Loses

Synthetic uniform valuations: discount-only pricing remains profitable and avoids H’s price increase.

**Figure description:** Horizontal bars show +USD 0.319 expected surplus per L member under both schedules, −USD 8.042 per H member under segmentation, and zero H change under discount-only pricing.

[Editable TikZ](../06_Lecture_Notes/figures/M09_pricing_incidence.tex)

The benchmark is the optimal uniform price USD 19/3. L represents 60% and H 40%; group labels do not identify wealth or vulnerability. A quarter of H loses a purchase, equal to 10% overall. The capped alternative earns USD 6.133 per eligible person versus USD 6.017 under uniform pricing. A conclusion about serious deprivation requires facts beyond these invented valuations.

Source: ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 87: A Defensible Scanlonian Pricing Argument

- Identify the person’s burden and the facts producing it.
- Compare a viable less burdensome principle.
- Defend the ought conclusion against the strongest objection.

If a seller exploits serious need despite a viable lower offer and no comparably serious countervailing burden, the lower offer is supported by a strong contractualist argument. Monetary amounts inform reasons; they are not a moral score. The firm’s legitimate interests include service viability and the people dependent on it. Majority benefits do not automatically resolve the losing person’s objection.

Source: ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 88: Dubé’s Mobile Targeting: Reconstruct the Incentives

| Rounded Table 9 | Theater A | Theater B |
| --- | --- | --- |
| Uniform / Uniform | 1.960 | 2.913 |
| Behavioral / Behavioral | 1.979 | 2.948 |
| Revenue Difference | 0.019 | 0.035 |

RMB expected revenue per messaged consumer. Published model outputs, not new estimates.

The complete 4-by-4 table yields behavioral targeting as the sole pure equilibrium. A’s best-response margin against a geobehavioral deviation is 0.001 RMB when B uses behavioral targeting. The paper reports a 40% posterior probability that this deviation improves A’s profit. The rounded calculation recovers incentives under the model; it supplies no consent measure or evidence of an unlawful agreement. Original Python uses the transcribed published table. Replication microdata were not downloaded.

Source: Dubé, Fang, Fong, and Luo (2017), Table 9, p. 965. https://doi.org/10.1287/mksc.2017.1042

## Slide 89: Kantian Authority Over Location History

- Specify the maxim, including any concealment or dependence.
- Check permission, understandable terms, and usable refusal.
- A useful discount does not settle authority over secondary data use.

The paper documents targeting from current location and historical visits. The course does not establish that consent was absent. A hypothetical maxim relying on concealed material use faces a Formula of Humanity objection because it defeats informed authorization. An understandable opt-in offer with meaningful alternatives requires a different assessment. The INFORMS download terms allow replication but restrict other reuse and the venue for a corrective follow-up; M9 §9.37 evaluates the reasons for those restrictions.

Source: Kant, Groundwork, Academy 4:421–430. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 90: An Antitrust Case Needs a Specified Mechanism

- Section 1: evidence of agreement beyond parallel pricing.
- Section 2: monopoly power and exclusionary conduct.
- Match the injury and counterfactual to the challenged conduct.

A paper’s method or a model’s softening of competition does not establish a violation. In a hypothetical shared-pricing case, contracts, confidential inputs, overrides, and discount restrictions help distinguish coordination from independent decisions. Twombly concerns plausible agreement; Trinko explains why monopoly pricing alone is insufficient. Robinson–Patman’s commodity-sales scope does not generally cover recruitment services or movie admissions.

Source: https://www.law.cornell.edu/supct/html/05-1126.ZO.html https://www.law.cornell.edu/supremecourt/text/02-682 ../01_Resources/16_AI_Experimentation_and_Pricing/ANTITRUST_AND_REASONS.md

## Slide 91: Revenue Growth Differs from an Overcharge

| Synthetic One-Period Comparison | USD |
| --- | --- |
| 92 purchases × (USD 120 − USD 100) | USD 1,840 |
| Revenue: USD 11,040 − USD 10,000 | USD 1,040 |
| At a USD 110 lawful benchmark | USD 920 |

The lawful counterfactual is assumed. Eight excluded purchases require separate welfare evidence.

The example assumes 100 counterfactual purchases at USD 100 and 92 actual purchases at USD 120. Invoice differences are based on actual quantities; revenue changes also contain a quantity component. No empirical damages or violation is established. A profit-maximizing uniform monopoly price is not automatically a lawful competitive benchmark. Comcast requires the damages model in that class-certification setting to match the accepted liability theory; Brunswick requires antitrust injury.

Source: https://www.law.cornell.edu/supremecourt/text/11-864 https://www.law.cornell.edu/supremecourt/text/429/477 ../03_Data_and_Code/AI_Experimentation_and_Pricing/compare_pricing_damages.py

## Slide 92: Antitrust Proof and Reasons Owed to People

A remedy needs attributable injury, a feasible alternative, and justified treatment of affected people.

**Figure description:** One branch identifies legal elements and evidence. A second compares burdens and reasons. Both inform a remedy that preserves independent forecasting while ending a proved restrictive arrangement.

[Editable TikZ](../06_Lecture_Notes/figures/M09_antitrust_reasons.tex)

Scanlonian reasoning can explain why independent alternatives matter and why sanctions require reliable attribution. The firms’ workers, owners, and customers also have reasons to reject unsupported accusations. Courts do not apply contractualism as the antitrust test. Moral standing includes people excluded from purchases and can extend beyond a legally actionable claim.

Source: ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 93: Legal Permission Leaves an Ought Question

- A lawful unilateral practice can still exploit serious need.
- An ethical objection does not supply a missing legal element.
- Compare safeguards, alternatives, and who bears a mistaken decision.

The hypothetical remedy separates useful independent forecasting from a proved restrictive arrangement. A necessity defense must identify benefits that genuinely require the challenged feature and the people who would lose them. If a less restrictive alternative supplies the same benefits, that defense fails on its own premise. The RealPage record supplies allegations and proposed terms; the separately entered Greystar judgment has different status.

Source: ../01_Resources/16_AI_Experimentation_and_Pricing/ANTITRUST_AND_REASONS.md https://www.justice.gov/atr/case/us-and-plaintiff-states-v-realpage-inc

## Slide 94: Name What Would Change the Conclusion

- New randomized cells can distinguish response models.
- Independent valuations can narrow welfare disagreement.
- Matched household evidence can support a narrower reassurance claim.
- A serious objection can change the proposed principle.

Scientific criticism remains open to correction. For electricity claims, informative uncertainty bounds, a credible comparison, household outcomes, and documented recovery protections could support reassurance within their scope. For pricing, evidence about feasible alternatives and legitimate operating needs can change the moral assessment. Reasonable rejection concerns reasons from affected positions, not a vote or commercial acceptance alone.

Source: M9 §9.40. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 95: Personalization and the Learner’s Authority

- Keep the source argument and consequential assumptions accessible.
- Allow a learner to change representations and challenge the conclusion.
- Evaluate independent reasoning and supported disagreement.

A student can reasonably object to an explanation that hides the premise on which its recommendation depends. A defensible learning system makes that premise inspectable and permits a reasoned objection. Response history does not exhaust the person or determine what the person ought to learn. Missing empirical measurements also remain distinct from Kant’s noumenal limiting concept.

Source: M9, Section 9.44, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md

## Slide 96: Whose Burdens Survive the Sample Restriction?

The affected population retains its standing when records are incomplete.

**Figure description:** The solid path runs from a household decision through the relevant population and causal comparison to a justified claim. A dashed shortcut from recent operating records leaves premises unresolved.

[Editable TikZ](../06_Lecture_Notes/figures/M09_design_and_reasons.tex)

The proposed Scanlonian objection concerns an unexamined burden and the evidence used to justify it. The critic must also consider developer payments, asset reuse, and disallowed cost recovery. Phantom projects provide a concrete design concern; actual donor contamination remains an empirical question.

Source: ../01_Resources/44_Bad_Controls_and_Project_Exposure/README.md

## Slide 97: Thoughtful Design Gives Reasons for the Comparison

- A precise selected-population result does not settle the full burden.
- Identify the missing empirical premise and the household’s objection.
- Reconstruct the design or narrow the public claim.

In the synthetic savings scenario, the operating-project effect is minus 2 dollars/MWh while the equal-weight mean over completed, canceled, and pending proposals is plus 3.33. Each describes its stated population. Using one to reassure the other is the unsupported step. Missing project data are investigable empirical unknowns and should not be equated with Kantian noumena.

Source: ../03_Data_and_Code/Bad_Controls/README.md

## Slide 98: A Decision with Consumer Outcomes

- State the decision, affected people, and evidence.
- Defend what the actor ought to do, with a normative premise.
- Answer the strongest objection and name a condition for revision.

A recommendation needs a justified principle connecting evidence to action. Compare the reasons of customers, workers, households, and others affected by the decision. Distinguish a feasible alternative from an imagined costless option. An effective argument can disagree with the instructor while supporting its premises and answering objections.

Source: Primary-source scope and status record: ../06_Lecture_Notes/ETHICS_AND_REGULATION.md.
