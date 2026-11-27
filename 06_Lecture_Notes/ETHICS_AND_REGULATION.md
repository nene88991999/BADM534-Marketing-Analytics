# Ethics and Regulation in Marketing Analytics

Marketing decisions affect customers' information, access, time, money, and ability to choose. A commercial metric captures only some of these consequences. Evaluate the action, the customer outcome, and the relevant legal obligation separately, then explain how each affects the decision.

## Connections Across the Course

| Module | Decision and Analytical Question | Notes | Sessions |
| --- | --- | --- | --- |
| M1 | Which customer fields are needed, and where may an AI coding tool process them? | [1.11: Customer Data and the Coding Environment](modules/M01_Marketing_Analytics_and_Python.md#111-customer-data-and-the-coding-environment) | 1 |
| M2 | Whose behavior disappears when a cleaning rule excludes observations? | [2.18: Sample Restrictions and Customer Representation](modules/M02_Customer_Data_and_Visualization.md#218-sample-restrictions-and-customer-representation) | 2–3 |
| M3 | Does the evidence support the claim customers will understand? | [3.13: Regression Evidence and Advertising Claims](modules/M03_Regression.md#313-regression-evidence-and-advertising-claims) | 4 |
| M4 | Does a higher lifetime value arise from useful service or difficulty leaving? | [4.15: Retention, Customer Value, and Choice](modules/M04_Conjoint_Segmentation_and_CLV.md#415-retention-customer-value-and-choice) | 5–6 |
| M5 | Does generated language summarize an experience or invent one? | [5.13: Review Provenance and Generated Language](modules/M05_Text_Social_and_Network_Analysis.md#513-review-provenance-and-generated-language) | 7 |
| M6 | What does an experiment optimize, and which customer consequences does it measure? | [6.17: Experimental Objectives and Customer Outcomes](modules/M06_Causal_Inference_and_Experiments.md#617-experimental-objectives-and-customer-outcomes) | 9–10 |
| M7 | Who receives a consequential offer after the delivery algorithm operates? | [7.19: Prediction, Delivery, and Access](modules/M07_Prediction_and_Machine_Learning.md#719-prediction-delivery-and-access) | 11–12 |
| M8 | How do adaptive choice procedures affect profit and customer value, and which rules cover the action? | [8.14–8.15: Retention and Regulatory Scope](modules/M08_Current_Topics_and_Integrated_Decisions.md#814-retention-procedures-profit-and-customer-value) | 13–15 |

## Primary Sources and Their Scope

The entries below were checked on November 2, 2026. Their dates and legal status matter to interpretation. Recheck the source when using it for a later business decision.

| Source | Status and Scope | Consequence for an Analysis |
| --- | --- | --- |
| [FTC Policy Statement Regarding Advertising Substantiation](https://www.ftc.gov/legal-library/browse/ftc-policy-statement-regarding-advertising-substantiation) | Agency policy describing the reasonable-basis requirement for objective advertising claims. Express and implied claims matter; support must exist before dissemination. | Match the evidence to the claim, product, population, and consequences. Predictive fit alone does not establish a causal product benefit. |
| [FTC Consumer Reviews and Testimonials Rule: Questions and Answers](https://www.ftc.gov/business-guidance/resources/consumer-reviews-testimonials-rule-questions-answers) | Agency guidance on the rule, effective October 21, 2024. Provisions address specified conduct involving false reviews, testimonials, incentives, suppression, and influence indicators. Knowledge conditions differ by provision. | Preserve actual experience and provenance. Mere hosting is treated differently from business creation or purchase of fake reviews. AI use alone does not determine whether a testimonial is false. |
| [FTC Rule on Unfair or Deceptive Fees: Frequently Asked Questions](https://www.ftc.gov/business-guidance/resources/rule-unfair-or-deceptive-fees-frequently-asked-questions) | Agency guidance on the rule effective May 12, 2025, covering live-event tickets and short-term lodging. | Define the covered transaction and required price components. This rule's sector coverage does not establish an identical price-display rule for every retailer. |
| [FTC Negative Option Rule ANPRM Announcement](https://www.ftc.gov/news-events/news/press-releases/2026/03/ftc-seeks-public-comment-response-advance-notice-proposed-rulemaking-regarding-negative-option) | March 2026 advance notice seeking input on possible amendments. It refers to the vacated 2024 rule. The notice itself does not adopt replacement obligations. | Keep proposals separate from operative obligations. Examine current federal and applicable state sources before assessing a subscription process. |
| [United States v. Meta Platforms, Inc.](https://www.justice.gov/crt/case/united-states-v-meta-platforms-inc-fka-facebook-inc-sdny) | DOJ case record for a housing-advertising settlement approved June 27, 2022, resolving Fair Housing Act allegations about targeting and delivery. | Assess actual delivery as well as advertiser-selected audiences. The case concerns housing access and does not establish the same legal standard for every marketing model. |

## A Retention-Procedure Case

A firm compares direct renewal with optional interactions before the same final offer. In the synthetic example, renewal probabilities are 0.10, 0.20, and 0.60. Firm margin is 11 dollars per renewal, and the customer loses 10 dollars from a renewal under the imposed preference ordering. Relative to direct choice at 0.20, selecting the 0.60 procedure increases expected firm profit by 4.40 dollars and lowers expected customer value by 4 dollars per eligible customer. Combined surplus rises by 0.40 dollars. The aggregate gain therefore coexists with a distributional loss.

These conclusions require the stated stakes and stable probabilities. A measured renewal increase alone does not identify customer value. Evaluate informed willingness to continue, cancellation completion, elapsed time, subsequent charges, and the ability to refuse optional interaction. The [complete calculation](../03_Data_and_Code/Lecture_Examples/retention_welfare.py), [aggregate table](../03_Data_and_Code/Lecture_Examples/retention_welfare.csv), and [TikZ figure](figures/M08_retention_welfare.tex) reproduce the imposed comparison.

## Discussion and Applied Work

For a proposed marketing action, identify the customer population, the information available, and the commercial objective. Describe the customer's feasible choices and the consequences outside that objective. Select a benchmark, a customer outcome, and a measurement horizon. Then identify the jurisdiction, covered conduct, effective date, and authority of the relevant primary source. A proposed assessment or discussion exercise does not establish an assignment requirement or grade weight.

## Incorporating New Material

New references should change the relevant method, example, figure, or coding check wherever the argument applies. Update the affected module notes and session companions together, then update the [session plan](../05_Slides/SESSION_PLAN.md), syllabus planning documents, and [resource integration map](RESOURCE_INTEGRATION.md). Check legal propositions against primary sources and record status and scope. Incorporate the instructor's own ideas directly into course explanations without naming, citing, linking, or uploading the underlying papers.

## Pricing Communication and the Scope of Evidence

M8 §8.16 and Session 14 connect the earnings-call case to operational pricing rules and customer outcomes. The [FTC January 2025 staff research summaries](https://www.ftc.gov/system/files/ftc_gov/pdf/p246202_surveillancepricing6bstudy_researchsummaries_redacted.pdf), pp. 1–3, concern US intermediary tools. Status: research publication under Section 6(b); no rule effective date. Checked November 2, 2026. The document supplies no finding against firms in the teaching corpus.

The [February 27, 2024 Wendy's statement](https://www.wendys.com/blog/wendys-digital-news-update) supplies a company clarification date for M6 §6.18. Its assertions establish what the company communicated, with realized practices and outcomes requiring separate evidence. No causal effect or broader legal status is inferred from that event.

## Cancellation Policy and Consumer Agency

Checked November 5, 2026. The [official source record](../01_Resources/13_Consumer_Agency_and_Recent_Research/Policy/README.md) adds the July 2025 Eighth Circuit vacatur, February 2026 FTC recodification, March 2026 advance notice, October 2026 information-collection notice, ROSCA, California's strengthened Automatic Renewal Law, and New York City's rule effective October 1, 2026. Each entry preserves jurisdiction, scope, instrument, and date. M8 §8.19 and Session 14 distinguish operative obligations from proposals and connect cancellation completion to customer intent.

The [literature codebook](../03_Data_and_Code/Consumer_Agency_Literature/CODEBOOK.md) separates reported concerns, inferred dual use, protective mechanisms, and missing evidence. Clusters describe selected papers. University affiliation communities describe shared publications and cannot establish institutional intent or a rate of agency erosion.

## Marketing Dialectics and Environmental Claims

M9 §§9.8 and 9.10 separate regulatory findings, philosophical evaluation, and the institutional burden of substantiating an interested claim. UK ASA rulings on Shell dated [June 7, 2023](https://www.asa.org.uk/rulings/shell-uk-ltd-g22-1170842-shell-uk-ltd.html) and [April 9, 2025](https://www.asa.org.uk/rulings/shell-uk-ltd-g24-1248246-shell-uk-ltd.html) were checked November 6, 2026. The first upheld the overall-environmental-impression issue while rejecting a separate electricity issue; the second did not uphold the complaint about a different ad with qualifying context. These are decisions on specific communications, not statutes with a general effective date. The 2025 ruling expressly applies the code wording relevant to the earlier complaint. The [resource guide](../01_Resources/15_Marketing_Dialectics/04_Industry_and_Regulation/README.md) retains source links and local snapshots.

## AI Experimentation and Personalized Pricing

M6 §6.21, M8 §8.20, and M9 §§9.14–9.18 examine commercial outcomes, customer surplus, and Kantian duties separately. The [primary policy record](../01_Resources/16_AI_Experimentation_and_Pricing/02_Policy/README.md), checked November 6, 2026, covers the FTC August proposal and October inquiry, New York's existing disclosure law, pending surveillance-pricing legislation, and price-gouging scope. The paper review preserves explicit safeguards and distributional findings that constrain criticism.

## Intervention Intensity and Customer Judgment

M8 §8.22 compares known synthetic revenue, profit, and complaint-constrained choices. M9 §9.18.1 distinguishes that optimization from justification of the marketing practice, including consent, truthful communication, and effective refusal. The assumed complaint response and 3% cap have no legal or ethical authority. This extension makes no new claim about the status of a regulation.

## Feasible Alternatives and Service Priorities

M8 §8.23 and M9 §9.18.2 connect [retail accessibility](../03_Data_and_Code/Retail_Accessibility/README.md) to customer purposes, service reliability, and the firm's choice of objective. Equal store-availability rates can accompany different population-access gains. The five-minute threshold, population weights, and profit gains are imposed teaching inputs. Kantian and Confucian reasoning supplies questions about maxims, respect, and conduct; the numerical threshold creates no ethical or legal safe harbor. The observed restaurant comparison contains no causal evidence about customer substitution or consumer harm.

## Evidence for Meaningful Customer Choice

M7 §§7.33–7.35 and M9 §9.18.3 use [training mixtures and conditional service outcomes](../03_Data_and_Code/Training_Data_Mixtures/README.md) to examine claims about customer protection. A fixed synthetic roster has identical aggregate resolution across two versions while cancellation outcomes deteriorate. Kantian respect for customer ends and Confucian responsibilities of service support evaluating consequential contexts directly. The published training experiments identify conditional model behavior under specified conditions; they provide no finding about a firm's intention, legal liability, or prevalence of commercial misconduct.

## Synthetic Personas and Consumer Representation

M9 §9.18.4 examines the authority a firm assigns to generated accounts of customer preferences. Kantian respect directs attention to actual people's purposes and opportunities for judgment. Confucian trustworthiness requires an accurate account of whose responses support the claim and responsible engagement with contrary evidence. M4 §4.23 and M5 §5.23 supply synthetic examples in which ranking, anchors, and aggregation alter the decision. These calculations establish measurement distinctions and do not identify a firm's motives.

The [source assessment](../01_Resources/29_Synthetic_Consumer_Research/SOURCE_REVIEW.md) distinguishes generated purchase-intent ratings from human preferences, observed purchases, and consent. Session 14 uses five minutes within its existing philosophical discussion for consumer representation. This addition makes no new legal-status claim.

## Agent Authority and Customer Requests

M9 §9.20 distinguishes technical permissions, company authority, customer authorization, and ethical justification. The cancellation example connects a firm-directed retention condition to Kantian respect for the customer’s reasons and Confucian attention to a service’s role. Session 14 incorporates the discussion within its existing definitions and permission block. This is a philosophical application; it introduces no new claim about a jurisdiction’s legal requirements.

## Model Agreement and Independent Reasons

M9 §9.21 distinguishes shared model representations, independent factual support, customer purposes, and justification for a marketing action. The mHealth reference categories in M5 §5.26 and M7 §7.43 measure agreement with recorded source labels. Their reproducibility does not establish nutritional correctness or permission. The philosophical application extends the existing Kantian and Confucian discussion without adding a legal claim.

## Shared Pricing Systems and Competition

M8 §8.28 and M9 §9.22 examine the November 23, 2026 complaint in Garcia v. The Wendy's Company and NCR Voyix Corporation, No. 8:26-cv-04886-LKG (D. Md.). The pleading alleges Sherman Act Section 1 price fixing and unlawful information exchange. The [source record](../01_Resources/37_Pricing_Systems_and_Competition/SOURCE_REVIEW.md), checked November 25, distinguishes those allegations, the 2022 NCR announcement, the 2024 Wendy's clarification, and a March 2024 DOJ/FTC submission in a separate hotel-pricing case. The submission is a litigation argument, with no effective date as a new rule or holding about Wendy's. The live docket was inaccessible, so later filings were not independently verified.

[M4 §4.26](modules/M04_Conjoint_Segmentation_and_CLV.md) separates changes in demand information from changes in pricing objectives using an original synthetic market. Exact profits and consumer surplus are conditional model results. Ethical evaluation concerns truthful explanation, customers' purposes and alternatives, and the responsibilities attached to pricing authority.

## Digital Usage, Assistance, and Customer Choice

M8 §8.29 and M9 §9.23 examine the difference between offering assistance and imposing a digital channel. The [geographic usage case](../03_Data_and_Code/Digital_Usage/README.md) supplies area-level context. It supplies no individual ability, consent, or customer-service outcome. Kantian critique examines the inference from geographic activity and the authority claimed over a person; Confucian role responsibilities motivate responsive service while preserving correction and customer choice. The proposed assistance evaluation introduces no new legal claim or graded requirement.

## Statistical Evidence and Advertising Claims

M9 §9.24 examines a joint test of consumer-credit advertising coefficients and the premises needed to infer customer benefit. Kantian respect for judgment and refusal and Confucian responsibilities in a relationship of reliance connect the statistical claim to comprehension, repayment burdens, and customer reasons. The benchmark's reference p-value is not presented as a course-replicated empirical finding. M1, M3, and M6 supply separate checks of statistical design and reporting. This addition makes no new legal or policy-status claim.

## Coding Competence and Responsibility

M1 §1.19 and M9 §9.24 connect correct numerical implementation to responsibility for the chosen question and customer-facing action. M7 §7.46 examines errors in customer allocation that preserve aggregate activity. M8 §8.30 separates hypothetical monetary losses from the justification of customer treatment. The [coding-workflow evidence](../01_Resources/40_Econometric_Coding_Workflows/README.md) supplies no new legal proposition or autonomous welfare judgment.

## Statistical Claims and the Ethics of Public Reassurance

The [resource and claim assessment](../01_Resources/41_Statistical_Claims_and_Decisions/README.md) connects Lakens’s inference guidance with the data-center electricity paper. M2 §2.28 distinguishes average prices, household incidence, and ownership categories. M3 §3.19 simulates repeated p-values; M6 §§6.32–6.33 compare detection with profit and reconstruct power, bounds, subgroup tests, sales mechanisms, and residual arithmetic. M8 §8.31 evaluates public communication. M9 §§9.25–9.26 develop equivalence, ontology, reasons, authority, Kantian duties, and Confucian trustworthiness. Four full Python listings and five editable Illinois-color figures accompany the notes. Sessions 4, 9, and 14 add eleven slides within existing allocations. The case distinguishes verified academic coverage from unverified company dissemination, demonstrated interpretation problems from replication questions, and possible harm from established consequences.

## Logical Assessment and Inverse Power

M6 §6.34 develops Donald W. K. Andrews's inverse-power approach with specified alternatives, nuisance parameters, and directional sensitivity. M9 §9.27 reconstructs the electricity arguments through premises, counterexamples, measurement, extrapolation, and household authority. The [argument record](../01_Resources/41_Statistical_Claims_and_Decisions/ARGUMENT_ASSESSMENT.md) links claims to evidence and repairs. Two complete Python examples and two editable TikZ figures support the discussion. Sessions 9 and 14 use selected examples within existing meeting allocations; extended calculations remain optional ungraded practice.

## Project Costs and the Scope of Customer Protection

The institutional example distinguishes operating entry from requests, investment, cancellation, and allowed recovery. The [source record](../01_Resources/41_Statistical_Claims_and_Decisions/INSTITUTIONAL_ASSESSMENT.md) identifies Ohio Power's July 23, 2025 tariff effective date and the February 17, 2026 FERC concurrence's federal transmission scope. A commissioner's reasoning, an operator's service terms, and reported customer protection are distinct evidence. These sources motivate investigation; they do not establish contracts, contamination, or household harms in the paper's historical sample. M6 §6.35 and M9 §9.27.6 connect enforceable obligations to cost incidence and opportunities for review.

## Stakeholder Reasons and Public Communication

M9 §§9.28–9.32 evaluates proposed duties through Scanlonian reasonable rejection and distinct stakeholder theories. These are philosophical arguments, not newly established legal requirements. The hypothetical university-branded headline remains separate from the verified HBS coverage. The [communication record](../01_Resources/41_Statistical_Claims_and_Decisions/PUBLIC_COMMUNICATION_AND_PUBLICATION.md) distinguishes public evidence, institutional hypotheses, and publication remedies.

## Utility Disclosures and Qualitative Substantiation

M5 §5.27 and M9 §9.33 connect public assurances to disclosed recovery mechanisms, household allocation, and the strongest contrary evidence. [The source register](../03_Data_and_Code/Utility_Cost_Recovery/sources.json) records date and provenance. Evergy's November 2026 release describes a request conditional on approval. The February 2025 NJBPU announcement reports a certified auction and a fixed-use price illustration, not household microdata or a data-center causal decomposition. Coding procedures and methodological references are in the [qualitative guide](../01_Resources/42_Qualitative_Evidence/README.md).

## U.S. Antitrust, Pricing, and Individual Reasons

The [antitrust source guide](../01_Resources/16_AI_Experimentation_and_Pricing/ANTITRUST_AND_REASONS.md), checked November 26, 2026, covers Sherman Act agreement and monopolization requirements, Robinson–Patman scope, antitrust injury, and damages tied to a liability theory. M9 §§9.38–9.39 connect those institutions to Scanlonian reasons and evidentiary safeguards. The RealPage documents are identified as allegations and proposed terms; the separately entered Greystar judgment is dated March 2, 2026. None establishes unlawful conduct by a researcher or by all users of pricing analytics. M9 §9.37 includes the INFORMS terms footnote and an argument about access to independent scrutiny.

## Logical Support and Ethical Justification

M9 §9.40 connects validity and premise support to the existing Scanlonian evaluation of pricing and public reassurance. M1 §1.20 introduces the five-step exercise; M4 §4.29 and M6 §6.38 supply exact numerical constructions. Students distinguish a supported criticism from a stronger accusation and identify evidence or reasons that would change either conclusion. The [logic guide](../01_Resources/15_Marketing_Dialectics/08_Logic_and_Analytical_Arguments/README.md) records the primary readings. These additions make no new legal claim or change to the recorded status of any policy.

[M9 §§9.41–9.43](../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md) distinguish acknowledged epistemic limits from unknown unknowns and assess interpretations through an ontological spectrum. Electricity reassurance, personalized pricing, and cancellation connect to Kant, Sellars, Bhaskar, Husserl, and Scanlon. Publication selection toward tractable questions remains a hypothesis separate from verified evidence of selection by result strength. Session 14 uses selected cases within its existing discussion blocks; the extended comparisons are optional practice.

## Conflicts of Interest, Judgment, and Engagement

M9 §§9.45–9.49 separates commercial adversity, a duty-based conflict, demonstrated bias, and wrongdoing. Valsan, the Institute of Medicine, Cain and coauthors, Lovett and Pettit, Balkin, and Khan and Pozen support distinct parts of the analysis; [the source guide](../01_Resources/15_Marketing_Dialectics/09_Conflicts_of_Interest/README.md) records scope. The fiduciary debate is normative and legal scholarship, not a statement of a universal current legal duty. The infinite-scroll case separates behavioral reward learning, neuroscience, economic self-control evidence, and clinical claims. The numerical comparison is entirely synthetic. Public-reassurance criticism does not assert an undocumented author motive or financial relationship.

## Research Design and Household Exposure

M9 §9.50 connects Scanlonian reasons to the population excluded by a convenient dataset. M6 §§6.41–6.42 distinguish zero operating additions from zero project exposure and preserve offsets and negative cases. The [source assessment](../01_Resources/44_Bad_Controls_and_Project_Exposure/CASE_ASSESSMENT.md) records the 2023 cancellation, 2025 risk discussion, and Ohio Power tariff approved July 9, 2025 and effective July 23, 2025. The tariff applies in that utility’s service territory. Its current operator page was checked November 26, 2026; no national rule or confirmed historical household loss is inferred.
