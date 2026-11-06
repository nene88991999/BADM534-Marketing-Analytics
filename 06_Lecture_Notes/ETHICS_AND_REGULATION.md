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
