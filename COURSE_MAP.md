# Course Map

Marketing Analytics

This outline follows the eight topic families in Unnati Narang's Spring 2026 syllabus. It is a planning map for Nathan Yang's offering. The [syllabus](02_Syllabus/Marketing_Analytics_Syllabus.md) and Spring 2027 meeting dates are available. Assignments and assessment rules remain pending. Suggested activities below are illustrative.

The course is planned with no guest speakers. The eight core modules and Marketing Dialectics will be covered through instructor-led sessions and course activities.

## Topics and Resource Routes

| Module | Managerial Question | Core Topics | Resource Guide | AI-Assisted Practice |
| --- | --- | --- | --- | --- |
| M1 | What data and calculations inform a marketing decision? | Python, notebooks, reproducible analysis | [Python and Data](01_Resources/01_Python_Data_and_Reproducibility/README.md) | Turn a short specification into small functions; check a hand-worked example. |
| M2 | Which customer patterns deserve attention? | Data preparation, joins, summaries, visualization | [Customer Data and Visualization](01_Resources/02_Customer_Data_and_Visualization/README.md) | Generate a cleaning pipeline and chart; verify totals, units, and denominators. |
| M3 | How do observed customer characteristics relate to outcomes? | Regression, interpretation, diagnostics | [Regression](01_Resources/03_Regression_and_Statistical_Foundations/README.md) | Build and inspect a model; explain coefficients and distinguish association from causal effects. |
| M4 | Which product designs, customer groups, or retention priorities should receive attention? | Conjoint, segmentation, customer lifetime value | [Conjoint, Segmentation, and CLV](01_Resources/04_Conjoint_Segmentation_and_CLV/README.md) | Compare product profiles, segmentations, or repeat-purchase forecasts; check assumptions and stability. |
| M5 | What does customer language reveal about products and service? | Text, social media, sentiment, optional networks | [Text and Social Analysis](01_Resources/05_Text_Social_and_Network_Analysis/README.md) | Build a transparent text baseline, compare alternatives, and assess examples manually. |
| M6 | Did a marketing intervention change outcomes? | Experiments, causal estimands, identification, uncertainty, recommendation policy evaluation | [Causal Inference and Experiments](01_Resources/06_Causal_Inference_and_Experiments/README.md) | Simulate or analyze an experiment and contrast it with a confounded comparison. |
| M7 | Which customers are likely to respond, and which products should they see? | Prediction, validation, decision thresholds, recommender models, ranking, LLM explanations | [Prediction and ML](01_Resources/07_Prediction_and_Machine_Learning/README.md) | Build a leakage-aware pipeline; compare baselines and assess decision costs. |
| M8 | How can newer methods improve a specific marketing decision? | Adaptive recommendations, customer goals, platform incentives, marketing mix modeling, generative AI | [Current Topics](01_Resources/08_Current_Topics_in_Marketing/README.md) | Evaluate one extension against a simpler approach and state the supported conclusion. |

## Lecture Notes

The [Preface](06_Lecture_Notes/Preface.md) explains the relationship between analytical tools and philosophical reasoning. The [lecture-note index](06_Lecture_Notes/README.md) maps the eight core modules and Marketing Dialectics to detailed explanations, worked cases, and 167 figures. Both PDF volumes open with a linked table of contents and end with an alphabetized [Glossary of Terms](06_Lecture_Notes/Glossary.md), with definitions and references to the relevant sections. [Synthetic data and reproducible calculations](03_Data_and_Code/Lecture_Examples/README.md) accompany the notes. These notes do not establish current assessment requirements.

## Across Modules

- [AI-Assisted Coding Resources](01_Resources/09_AI_Assisted_Coding/README.md) and [Teaching Notes](01_Resources/09_AI_Assisted_Coding/Teaching_Notes/README.md).
- [Candidate Datasets](01_Resources/10_Datasets_and_Project_Resources/Dataset_Guide/README.md).
- [Food Logging and Personalized Recommendations](03_Data_and_Code/mHealth/README.md), connecting data preparation, text classification, and recommendation evaluation using transformed real records.
- [Additional Module Catalog](01_Resources/00_Index/README.md), with a separate resource-ID namespace and overlapping coverage.
- [Syllabus Coverage and Teaching Priorities](01_Resources/00_Course_Map_and_Teaching/Planning_Notes/README.md).

A recurring workflow is: define the marketing decision, specify the analysis, inspect the data, implement in small steps, verify the result, and explain its implications. AI assistance supports implementation and revision; students still need to understand the analytical choices.

## Current Course Requirements

See [course.json](course.json) for pointers to released documents and [02_Syllabus](02_Syllabus/README.md) for syllabus status. The predecessor's dates, grading weights, and AI policy have not been adopted as the rules for the new offering.

## Recurring mHealth Applications

| Module | Application |
| --- | --- |
| M1 | Chunked loading, keys, join coverage, repeated totals, duplicate review, and sanity checks. |
| M2 | Breadth, calorie-share variety, missing days, and nutrition-informed screening sensitivity. |
| M3 | Exact next-calendar-day regression, customer effects, clustered intervals, and range restrictions. |
| M4 | Earlier-period behavioral segments, later logging, and separately imposed choice/CLV scenarios. |
| M5 | Familiar versus new descriptions, source-label ambiguity, and text-classification evaluation. |
| M6 | Historical variance, user-level randomization, power, and logging versus nutrition outcomes. |
| M7 | Frozen candidates, chronological validation, whole baskets, and recommendation baselines. |
| M8 | A fixed novelty-bonus comparison and the distinction between offline scores and intervention value. |

Full code is printed in the [notes](06_Lecture_Notes/README.md) and saved with [verified outputs](03_Data_and_Code/mHealth/recurring_examples/README.md). [Nutrition resources](01_Resources/12_Nutrition_and_Dietary_Data_Quality/README.md) support the measurement and filtering discussion.

## Additional Resource Applications

The [resource integration map](06_Lecture_Notes/RESOURCE_INTEGRATION.md) connects all eight modules to executed extensions: fixed-cohort reviews, recency/frequency, price instruments, logging-gap survival, topic models, CUPED, basket associations, and generated-claim validation. It also identifies reference notebooks available for further adaptation and their execution status.

## Visualization Applications

M2, Sections 2.14–2.15, connect chart choice, denominator changes, distribution shape, and interactive filters using the same fixed mHealth cohort. M3, Section 3.6.1, shows why uncertainty follows the sampling unit. M8, Section 8.12, checks chart values, units, denominators, baselines, and interpretation against independent evidence. [Code and chart data](03_Data_and_Code/mHealth/recurring_examples/results/VISUALIZATION.md) accompany all three applications.

## Restaurant Availability Applications

The [McBroken case](03_Data_and_Code/McBroken/README.md) uses the supplied McDonald's ordering-status data in three modules. M2 §2.16 assesses coverage, missingness, address keys, and calendar joins. M6 §6.16 compares country trends around the 2024 repair exemption and distinguishes descriptive contrasts from causal evidence. M7 §7.18 evaluates next-observation forecasts on later dates, with label coverage and calibration. Five complete Python programs and three TikZ figures support these applications.

## Generative-AI Demand

The [GenAI demand cases](03_Data_and_Code/GenAI_Demand/README.md) connect M2 §2.17, M4 §4.14, and M8 §8.13. Students assess title-specific pageviews, compare provider and category retention within the same starting cohort, classify acquisition events, and test a price regression against its generating model. Three executed Python programs and three TikZ figures distinguish the supplied public capture from the synthetic consumer panel. The exact binary-logit benchmark recovers its imposed coefficient; dynamic-panel slopes remain descriptive.

## Session Sequence and Ethics

The [15 session decks](05_Slides/README.md) follow a [170-minute meeting plan](05_Slides/SESSION_PLAN.md), with no guest speakers and two provisional presentation meetings. The [syllabus teaching plan](02_Syllabus/TEACHING_PLAN.md) records the educational structure; Spring 2027 meeting dates are available and assessment requirements remain pending.

[Ethics and regulation](06_Lecture_Notes/ETHICS_AND_REGULATION.md) connect M1 data handling, M2 sample representation, M3 advertising claims, M4 retention and choice, M5 review provenance, M6 experimental objectives, M7 delivery and access, and M8 adaptive procedures and customer value. A synthetic retention example includes complete Python, an aggregate table, and a TikZ figure.

## Earnings-Call Case

The [pricing-communication example](03_Data_and_Code/Earnings_Calls/README.md) connects document coverage (M2 §2.19), text constructs and word exposure (M5 §5.14), descriptive event comparisons (M6 §6.18), and customer outcomes and regulatory evidence (M8 §8.16). Sessions 02, 07, 10, and 14 include the corresponding cases. The complete programs, structured teaching data, and nine counterexample checks are available in the example folder.

## AI Workflow Evaluation and Economics

The [synthetic AI workflow examples](03_Data_and_Code/AI_Workflows/README.md) connect failure diagnosis (M1 §1.12), buyer alternatives (M4 §4.16), document evaluation after prompt revision (M5 §5.15), model-by-library contrasts (M6 §6.19), repeated selection (M7 §7.20), and reuse and pricing decisions (M8 §§8.17–8.18). Three complete standard-library programs, five small-case checks, and four TikZ figures accompany the notes. Sessions 01, 05, 07, 09, 11, and 14 include these comparisons. All numerical inputs are synthetic; no provider performance, labor savings, or demand is measured.

## Consumer Agency, Recent Research, and Affiliations

The [2023-2026 journal collection](01_Resources/13_Consumer_Agency_and_Recent_Research/README.md) supplies original managerial summaries, explicit access gaps, and a [cancellation-policy source record](01_Resources/13_Consumer_Agency_and_Recent_Research/Policy/README.md). M2 §2.20 assesses evidence selection; M4 §4.17 clusters mechanism codes; M5 §§5.16-5.17 examine annotation and university affiliation networks; M6 §6.20 separates conversion, returns, and intent; M7 §7.21 distinguishes predictive accuracy from welfare; M8 §8.19 connects mechanisms to effective cancellation. Sessions 3, 6, 7, 9, 12, and 14 carry the corresponding material. [Runnable code and outputs](03_Data_and_Code/Consumer_Agency_Literature/README.md) retain the denominators and sensitivity checks.

## Model Versions and Changing Evidence

The [LLM revalidation examples](03_Data_and_Code/LLM_Revalidation/README.md) connect versioned evidence (M1 §1.13), claim follow-up and censoring (M2 §2.21), generator-by-judge comparisons (M5 §5.18), paired regressions and failure costs (M7 §7.22), and exposure-based revalidation (M8 §8.18.1). The [research guide](01_Resources/14_LLM_Evidence_and_Revalidation/README.md) distinguishes the released empirical snapshot from original constructed cases. Sessions 01, 03, 07, 11, and 14 incorporate these applications.

## M9: Marketing Dialectics

[Marketing Dialectics](06_Lecture_Notes/modules/M09_Marketing_Dialectics.md) extends the eight core modules with Kantian critique and ethics, scrutiny of corporate self-interest, and Confucian perspectives on marketing conduct. [Synthetic renewal and intent](03_Data_and_Code/Marketing_Dialectics/README.md) connects M2 measurement, M4 retention, M6 causal interpretation, and M7 recommendation objectives. Academic and industry cases examine advertising measurement, customer control, and environmental claims. The chapter fits the existing Session 14 ethics block. [Reading collection](01_Resources/15_Marketing_Dialectics/README.md).

## AI Experimentation, Pricing, and Kantian Evaluation

M6 §6.21, M8 §8.20, and M9 §§9.14–9.18 connect [Misra and coauthors’ research](01_Resources/16_AI_Experimentation_and_Pricing/README.md) to commercial objectives, distributional consequences, and recent pricing policy. [A solved synthetic example](03_Data_and_Code/AI_Experimentation_and_Pricing/README.md) compares common prices, segmented optima, and capped discounts. Sessions 9 and 14 carry the corresponding discussion.

## Statistical Graphics for Marketing Decisions

[PyStatlas](01_Resources/17_PyStatlas_Statistical_Graphics/README.md) supplies a question-oriented chart reference across M2–M9. M2 §2.22 and Session 3 examine paired customer changes; M7 §7.23 and Session 11 distinguish ranking from probability accuracy. Both have [original synthetic inputs and complete tested Python](03_Data_and_Code/Statistical_Graphics/README.md).

## Prediction Intervals, Label Sets, and Changing Demand

[Conformal prediction](01_Resources/18_Conformal_Prediction/README.md) extends M7 §§7.24–7.25 with finite-sample calibration, segment coverage, and complaint routing. M8 §8.21 examines an imposed change in demand. Sessions 11 and 13 carry the examples. [Complete original Python and generated records](03_Data_and_Code/Conformal_Prediction/README.md) support connections to M3 uncertainty, M5 text classification, and M9 customer consequences.

## Source Selection and Evaluation of AI Graders

[Original synthetic cases](03_Data_and_Code/AI_Evidence_and_Evaluation/README.md) connect M1 §1.14 specifications and retained skills, M5 §§5.19–5.20 source support and grader evaluation, and M7 §7.26 coverage and decision costs. The [practice lab](07_Labs/AI_Evidence_and_Evaluation/README.md) adapts Stanford CS193T activities to the earnings-call example. Sessions 7 and 11 retain their existing meeting times and cover the two comparisons. Discussion connects reference judgments to the customer-agency questions in M9.

## Clustering Optimization

[Clustering optimization and interpretation](03_Data_and_Code/Clustering_Optimization/README.md) connects M4 §§4.18–4.20, M5 §5.3, and M7 §7.27. Session 6 uses 15 minutes of its existing application block. Two complete programs and two editable TikZ figures distinguish weighted updates, consistent final labels, and implementation benchmarks from evidence for a marketing action. The [practice lab](07_Labs/Clustering_Optimization/README.md) is optional and ungraded.

## Discount Response and Intervention Intensity

[The discount-response collection](01_Resources/24_Dose_Response/README.md) supports M3 §3.14, M4 §4.21, M6 §§6.22–6.27, M8 §8.22, and M9 §9.18.1. Session 10 uses 20 minutes for shape, adjustment, conditional support, interval coverage, and store pooling. Session 13 uses 15 minutes for objectives and customer outcomes. [Three complete programs](03_Data_and_Code/Dose_Response/README.md) use synthetic observations and known curves; [the lab](07_Labs/Dose_Response/README.md) is optional and ungraded. Advanced continuous-DiD assumptions remain supplementary reading.

## Retail Alternatives and Spatial Networks

[The retail accessibility case](03_Data_and_Code/Retail_Accessibility/README.md) connects map footprints in M2 §2.23, spatial representations in M4 §4.22, shortest paths and unknown availability in M5 §§5.21–5.22, deployment comparisons in M7 §7.28, service priorities in M8 §8.23, and customer agency in M9 §9.18.2. A synthetic network isolates the mechanism; four observed restaurant origins provide a selected geographical comparison. Sessions 3, 7, and 13 use existing application time. The [lab](07_Labs/Retail_Accessibility/README.md) is optional ungraded practice, and GNN modeling remains an optional extension.

## Anomaly Detection and Diagnosis

[Original retail monitoring cases](03_Data_and_Code/Anomaly_Diagnosis/README.md) extend M7 §§7.29–7.30 with alert evaluation, variable ranking, event timing, and supported interpretation. Two full Python programs and two editable TikZ figures connect the [SHAD review](01_Resources/26_Anomaly_Detection_and_Diagnosis/README.md) to a synthetic checkout interruption, campaign, and recording failure. Session 11 uses twenty minutes of existing application time. The [longer lab](07_Labs/Anomaly_Diagnosis/README.md) is optional ungraded practice.

## Inference Efficiency and Useful Responses

[M7 §§7.31–7.32](06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md) distinguish target-token verification, draft length, elapsed-cost boundaries, and correct customer resolution. [Two complete programs](03_Data_and_Code/Inference_Efficiency/README.md) preserve paired rosters, failures, and separate teacher-forced and free-response observations. Session 11 uses minutes 60–70 of its existing comparison block. M1 connects version changes to component compatibility, M4 connects clustering to vocabulary projection, and M8 connects response wait to triage cost and customer outcomes.

## Training Mixtures and Conditional Evaluation

[M7 §§7.33–7.35](06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md) explain how contrasting training examples change feature attribution, why identical average performance can conceal cancellation regressions, and how final and selected checkpoints answer different questions. [Three executed programs](03_Data_and_Code/Training_Data_Mixtures/README.md) preserve the distinction between a synthetic ridge model, imposed paired service outcomes, and recomputed published aggregates. Session 11 uses minutes 30–45 for five slides; the [longer coding exercise](07_Labs/Training_Data_Mixtures/README.md) is optional ungraded practice. Connections appear in M2 §2.24, M3 §3.15, M8 §8.24, and M9 §9.18.3.

## Synthetic Consumers and Product Concept Testing

[Two original executed examples](03_Data_and_Code/Synthetic_Consumers/README.md) connect M4 §4.23 concept screening, M5 §5.23 anchor measurement, M7 §7.36 validation, M8 §8.11 workflows, and M9 §9.18.4 consumer representation. Two editable figures and eight slides support 20 minutes in Session 5, 10 minutes in Session 7, and 5 minutes within Session 14's philosophical discussion. [Optional ungraded practice](07_Labs/Synthetic_Consumers/README.md) preserves invented inputs, persona weights, common concept rosters, and unresolved ties.

## Reproducible Recommendations and Public Evidence

M1 §1.15 and M8 §8.25 connect persona weights, synthetic concept screening, file identity, and the interpretation of generated explanations. [Complete Python and numerical evidence](03_Data_and_Code/Reproducible_Recommendations/README.md) support Sessions 1 and 14 and [optional ungraded practice](07_Labs/Reproducible_Recommendations/README.md). Exported pages need separate rendering and navigation checks; the [future wiki](08_Wiki/README.md) remains unimplemented.

## Auxiliary Data and Human Research Budgets

[The auxiliary-data example](03_Data_and_Code/Auxiliary_Data/README.md) connects coefficient identification in M3 §3.16, product contrasts and research cost in M4 §4.24, fixed experimental design in M6 §6.28, and omitted-bias evaluation in M7 §7.37. Two complete standard-library programs and three TikZ figures retain the four-profile construction, common MSE target, source variances, and bias restrictions. Sessions 4, 5, 9, and 11 use existing meeting time. The [lab](07_Labs/Auxiliary_Data/README.md) is optional ungraded practice.

## Graph Coarsening and Customer Outcomes

[The graph-coarsening case](03_Data_and_Code/Graph_Coarsening/README.md) connects original-population measurement in M2 §2.23, group weights in M4 §4.22, revenue and travel in M5 §5.24, label information in M7 §7.38, and service responsibilities in M9 §9.18.2. Sessions 7 and 11 include five slides and two editable diagrams. [Optional practice](07_Labs/Graph_Coarsening/README.md) applies the M1 AI-assisted coding workflow to inspected source defaults.

## Definitions and Representation Quality

[Cancellation evidence](03_Data_and_Code/Ontology_and_Evidence/README.md) connects M1 §1.16 and M2 §2.25 to event definitions, validation, unknown states, and a fixed reporting cutoff. [Representation evaluation](03_Data_and_Code/Representation_Evaluation/README.md) connects M7 §§7.39–7.40 to variance-weighted reconstruction, review recall, and nonunique features. Three complete Python programs, fourteen independent tests, and three editable figures support the synthetic cases. M4 §4.25, M5 §5.25, and M9 §9.19 connect segment interpretation, attributed claims, and permission evidence. Sessions 1, 2, 11, and 14 include ten additional slides within the existing meeting times.

## Agent Workflow Evaluation

[The workflow case](03_Data_and_Code/Agent_Workflows/README.md) connects M1 §1.17, M6 §6.29, M7 §7.41, M8 §8.26, and M9 §9.20. A prior-period mHealth roster supplies observed logging counts; separate synthetic checks expose grading errors. Four complete programs, two TikZ figures, and an optional experiment protocol distinguish measured records from hypothetical costs and unexecuted model comparisons. Sessions 1, 9, 11, and 14 use existing discussion time.

## Representation Alignment and Independent Evidence

M5 §5.26 defines a disjoint description sample. M7 §§7.42–7.44 connect coordinate geometry, classifier compatibility, local mHealth classification, and observed answers. M8 §8.27 compares implementation costs; M9 §9.21 examines model agreement and independent reasons. [Complete code and recorded results](03_Data_and_Code/Representation_Alignment/README.md) accompany two editable figures and [optional ungraded practice](07_Labs/Representation_Alignment/README.md). Sessions 7, 11, and 14 include five slides within the existing meetings.

## Pricing Systems and Customer Choice

[M4 §4.26](06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md) solves an original two-restaurant model with information and pricing objectives varied separately. [M8 §8.28](06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md) examines the Wendy's complaint and evidence, while [M9 §9.22](06_Lecture_Notes/modules/M09_Marketing_Dialectics.md) evaluates pricing authority and customer alternatives. [Code and results](03_Data_and_Code/Pricing_Competition/README.md), two TikZ figures, six additional slides in Sessions 5 and 14, and [optional practice](07_Labs/Pricing_Competition/README.md) accompany the case.

## Digital Usage and Customer Access

The [recurring geographic case](03_Data_and_Code/Digital_Usage/README.md) appears in M2 §§2.26–2.27, M3 §3.17, M4 §4.27, M7 §7.45, M8 §8.29, and M9 §9.23. Sessions 2, 3, 4, 6, and 14 distinguish recorded activity, conditional comparisons, similarity, service outcomes, and authority over customer options. The full Python lab is public optional ungraded practice.

## Statistical Evidence and Customer Reasons

M1 §1.18 separates execution, method, reporting, and interpretation. M3 §3.18 reconstructs mHealth pairs and uncertainty; M6 §6.30 measures false discoveries under store assignment. M9 §9.24 examines a joint advertising test and the further premises needed for customer-welfare claims. The [original programs](03_Data_and_Code/Statistical_Inference/README.md) and [optional lab](07_Labs/Statistical_Inference/README.md) support Sessions 1, 4, 9, and 14 within their existing meeting blocks.

## Econometric Coding Workflows and Hidden Errors

M1 §1.19, M3 §3.18, M6 §6.31, M7 §7.46, M8 §8.30, and M9 §9.24 connect [published coding evidence](01_Resources/40_Econometric_Coding_Workflows/README.md) to independent assessment, interaction scales, customer allocation, review cost, and responsibility. [Three complete programs](03_Data_and_Code/Agent_Workflows/README.md), two editable figures, and six slides support Sessions 1, 4, 9, 11, and 14 within their existing meeting blocks. [Longer practice](07_Labs/Agent_Workflows/README.md) remains optional and ungraded.

## Statistical Claims, Household Burdens, and Agency

The [statistical-claims examples](01_Resources/41_Statistical_Claims_and_Decisions/README.md) connect repeated p-values, economic thresholds, equivalence, and a recurring data-center electricity case. M2 §2.28, M3 §3.19, M6 §§6.32–6.33, M8 §8.31, and M9 §§9.25–9.26 examine reported tables, measurement, causal interpretation, public reassurance, ontology, and household authority. Four complete Python programs and five original TikZ figures support the comparisons. Guided practice is optional and ungraded.

## Logical Assessment and Inverse Power

M6 §6.34 develops the inverse-power approach (Andrews, 1989) with specified alternatives, nuisance parameters, and directional sensitivity. M9 §9.27 reconstructs the electricity arguments through premises, counterexamples, measurement, extrapolation, and household authority. The [argument record](01_Resources/41_Statistical_Claims_and_Decisions/ARGUMENT_ASSESSMENT.md) links claims to evidence and repairs. Two complete Python examples and two editable TikZ figures support the discussion. Sessions 9 and 14 use selected examples within existing meeting allocations; extended calculations remain optional ungraded practice.

## Institutions, Measurement, and Treatment

The electricity case connects M2 §2.28.1 (prices and bills), M6 §6.35 (project timelines and exposed controls), and M9 §9.27.6 (missing institutional premises). [Complete synthetic code](03_Data_and_Code/Statistical_Inference/institutional_exposure.py) and the [source assessment](01_Resources/41_Statistical_Claims_and_Decisions/INSTITUTIONAL_ASSESSMENT.md) accompany Sessions 9 and 14. Actual donor contamination and household incidence remain empirical questions requiring project and payment records.

## Reasons, Stakeholders, and Public Voice

M1 §1.1 connects a managerial recommendation to a normative premise. M8 §8.31 examines public reassurance. M9 §§9.28–9.32 develops Scanlonian argument, stakeholder duties, publication choices, and residents' opportunities to contest claims. [Optional practice](07_Labs/Philosophical_Arguments/README.md) carries these questions across M1–M9; Session 14 includes the two new editable diagrams.

## Utility Evidence Across Methods and Ethics

M5 §5.27 connects scraping to qualitative content analysis and boxed source excerpts. M6 §6.36 separates mechanism evidence from a causal comparison. M8 §8.31 and M9 §9.33 connect the evidence to public reassurance and household reasons. Use the [worked example](03_Data_and_Code/Utility_Cost_Recovery/README.md), [methods readings](01_Resources/42_Qualitative_Evidence/README.md), and [optional lab](07_Labs/Qualitative_Evidence/README.md). Sessions 7 and 14 integrate the comparison within existing time allocations.

## Pricing, Individual Reasons, and Competition

M4 §4.28 connects segments to treatment reasons. M6 §6.37 compares correct experimental weighting with the allocation of risk. M8 §8.32 connects pricing evidence to competition and customer authority. M9 §§9.34–9.39 develop demand-completion counterexamples, a profitable less burdensome alternative, the mobile-targeting game (Dubé et al., 2017), Kantian reasoning, and antitrust institutions through Scanlonian objections. Sessions 9 and 14 use selected comparisons within existing time blocks. [Programs](03_Data_and_Code/AI_Experimentation_and_Pricing/README.md), [optional practice](07_Labs/Scanlon_Pricing/README.md), and [legal sources](01_Resources/16_AI_Experimentation_and_Pricing/ANTITRUST_AND_REASONS.md) supply complete detail. Students distinguish an instrumentally rational choice from a reasonable principle. They assess measurement quality alongside the worth of the goal, then compare personalized pricing, dynamic-pricing communication, and data-center reassurance.

## Analytical Arguments Across the Course

M1 §1.20, M4 §4.29, M6 §6.38, and M9 §9.40 connect five-step argument assessment to question formulation, measurement, causal identification, welfare valuation, and reasonable justification. [Two original programs](03_Data_and_Code/Analytical_Arguments/README.md) make the assumptions visible through counterexamples. [Optional practice](07_Labs/Philosophical_Arguments/README.md) applies the same scrutiny to an analytical claim and its criticism, with explicit evidence or reasons for revision. Sessions 1, 5, 9, and 14 incorporate selected examples within the existing calendar.

M1 and [M9 §9.41](06_Lecture_Notes/modules/M09_Marketing_Dialectics.md) place the worth of the objective, the phenomena–noumena distinction (Kant, 1781/1787), and the practical standing of affected people before optimization. Sessions 1 and 14 connect the limits of empirical representation to separate arguments about ends, authority, and obligations. A fourth editable diagram distinguishes further empirical inquiry from the noumenal limiting concept (Kant, 1781/1787) and practical justification.

[M9 §§9.41–9.43](06_Lecture_Notes/modules/M09_Marketing_Dialectics.md) distinguish acknowledged epistemic limits from unknown unknowns and assess interpretations through an ontological spectrum. Electricity reassurance, personalized pricing, and cancellation connect to limits of cognition (Kant, 1781/1787), observational justification (Sellars, 1956), critical realism (Bhaskar, 2007), intentionality (Husserl, 1970), and normative reasons (Scanlon, 2009). Publication selection toward tractable questions remains a hypothesis separate from verified evidence of selection by result strength. Session 14 uses selected cases within its existing discussion blocks; the extended comparisons are optional practice.

## Explanation and Independent Judgment

[M1 §1.21](06_Lecture_Notes/modules/M01_Marketing_Analytics_and_Python.md) preserves an argument across representations. [M2 §2.29](06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md) connects percentages, electricity prices, and household bills. [M6 §6.39](06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md) separates a learning package from feature effects. [M9 §9.44](06_Lecture_Notes/modules/M09_Marketing_Dialectics.md) examines learner authority. Sessions 1, 2, 9, and 14 select examples within their existing blocks. [HTML pilot](08_Wiki/pilot/README.md); [text companion](08_Wiki/pilot/LESSON.md); [Python](03_Data_and_Code/Learning_Design/README.md); [optional practice](07_Labs/AI_Augmented_Learning/README.md).

## Conflicts of Interest and Consumer Control

M1 §1.22, M7 §7.47, M8 §8.33, and M9 §§9.45–9.49 connect the analyst’s incentives to question selection, interpretation, and responsibilities. Sessions 1, 11, and 14 use selected comparisons within existing time. [Sources](01_Resources/15_Marketing_Dialectics/09_Conflicts_of_Interest/README.md); [complete synthetic Python](03_Data_and_Code/Conflicts_of_Interest/README.md); [optional practice](07_Labs/Conflicts_of_Interest/README.md). The feed case also connects to pricing, cancellation, mHealth targeting, and electricity reassurance.

## Bad Controls, Project Exposure, and Sample Windows

M3 §§3.20–3.21 explain causal adjustment; M6 §§6.40–6.42 compare treatment-affected covariates, project timelines, and selected populations; M9 §9.50 evaluates household reasons. The [30-source guide](01_Resources/44_Bad_Controls_and_Project_Exposure/README.md), [complete examples](03_Data_and_Code/Bad_Controls/README.md), and [optional practice](07_Labs/Bad_Controls/README.md) support Sessions 4, 10, and 14. Evidence within the later years of 2020–2025 motivates a donor-exposure assessment without establishing contamination of the paper’s actual donors.

## Data Production and Public Justification

M2 §§2.30–2.31 develop provenance and selective access; M6 §6.43 separates actual bills from causal cost incidence; M9 §§9.51–9.54 connect artifacts, truth, norms, undone science, and Scanlonian responsibility. The [categorized collection](01_Resources/45_Data_Truth_and_Norms/README.md), [synthetic example](03_Data_and_Code/Data_Production/README.md), and [optional practice](07_Labs/Data_Truth_and_Norms/README.md) accompany Sessions 2, 10, and 14.

## Measurement and Standards of Evidence

The [historical collection](01_Resources/46_Measurement_and_Disciplinary_History/README.md) supports M1 §1.23 and M9 §9.55. The [evidence-standards collection](01_Resources/47_Evidence_Standards_and_Error_Costs/README.md) connects M2 §2.32, M3 §3.22, M4 §4.30, M5 §5.28, M6 §§6.44–6.45, M7 §7.48, M8 §8.34, and M9 §§9.56–9.59. A [complete synthetic example](03_Data_and_Code/Evidence_Standards/README.md) compares error costs with fixed evidence; [optional practice](07_Labs/Evidence_Standards/README.md) develops the statistical and philosophical argument. The syllabus, ten session decks, and [electricity wiki pilot](08_Wiki/pilot/index.html#uncertainty) carry the same distinctions between inquiry, protection, and remedy.

## Data, Artifacts, and Research Agreements

M2 §§2.33–2.34 distinguishes events, records, dataset versions, and physical copies through a complete synthetic subscription program. M9 §§9.60–9.65 connects artifact creation, public norms, NDA restrictions, publication selection, and reasons owed to affected people. The discussion asks whether research under an NDA ought to exist and distinguishes conducting, publishing, and relying on a study. Sessions 2 and 14 use the same cases, with three editable TikZ diagrams and optional practice in `07_Labs/Data_Truth_and_Norms/`. Source annotations and professional-policy scope appear in `01_Resources/45_Data_Truth_and_Norms/`.

## Precision and Missed Consumer Harm

Use M4 §4.31 for released retail data and exact mixture integration, M6 §6.46 for the synthetic precision–detection calculation, and M9 §§9.57.1–9.57.5 for modal claims and reasonable protection. [Data, code, and provenance](03_Data_and_Code/Heterogeneity_and_Consumer_Protection/README.md); [optional practice](07_Labs/Evidence_Standards/README.md).

## Statistical Virtues and Ontological Adequacy

M1 §1.24 introduces the object behind an AI-assisted analysis. M6 §6.46.6 distinguishes the population error criterion from the affected person's burden. M9 §§9.66–9.69 develops the philosophical argument, recurring case assessments, and strongest reply. Sessions 1 and 14, the [annotated readings](01_Resources/48_Statistical_Virtues_and_Ontology/README.md), and [optional practice](07_Labs/Philosophical_Arguments/README.md#statistical-virtues-and-the-missing-object) use the same distinction. The new figure is conceptual and supplies no numerical score of a researcher or institution.

## Marketing Research and Compulsive Online Engagement

M5 §5.29 distinguishes engagement labels, endorsement, and selected qualitative accounts. M9 §§9.70–9.75 examines content sequences, streaks, uncertain rewards, gamification, binge viewing, and user authority through [15 sources](01_Resources/49_Online_Engagement_and_Agency/README.md). Sessions 7 and 14 select these cases within their existing discussions. The [optional exercise](07_Labs/Conflicts_of_Interest/README.md#marketing-publications-and-unwanted-continuation) reuses the complete synthetic feed-policy program in §9.48; it makes no new platform-harm estimate.

## Chicago Price Theory and Market Justification

M4 §4.32 and M9 §§9.76–9.82 connect monetary valuation, rational addiction, compensation, institutional bargaining, and enforcement errors to the moral premises behind market recommendations. [Thirteen readings](01_Resources/50_Chicago_Price_Theory_and_Moral_Justification/README.md), [reproducible synthetic examples](03_Data_and_Code/Price_Theory_and_Justification/README.md), and [optional argument practice](07_Labs/Scanlon_Pricing/README.md#price-theory-and-moral-permission) support selected discussion in Sessions 5 and 14.

## Modern Power and Harm Bounds

[M6 §§6.47–6.51](06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md) connect zero-null power, positive harm margins, equivalence, and bias sensitivity through published electricity-price estimates. [M9 §9.83](06_Lecture_Notes/modules/M09_Marketing_Dialectics.md) examines the justification for public reassurance. The [readings](01_Resources/51_Modern_Power_and_Harm_Bounds/README.md), [complete price calculations](03_Data_and_Code/Modern_Power/README.md), and [optional practice](07_Labs/Statistical_Inference/README.md#modern-power-and-harm-bounds) accompany selected slides in Sessions 9 and 14.

## Data Artifacts, Responsibility, and Independent Scrutiny

M9 §§9.60.3, 9.63.4–9.63.5, and 9.65.2–9.65.8 connect dataset creation to corporate standing, NDA terms, responsibility, and maxims. The [Kilts policy case](01_Resources/45_Data_Truth_and_Norms/06_Corporate_Standing/KILTS_CASE.md) separates documented restrictions from claims about suppression. M2 §2.35 supplies a complete Python assessment of the public insurance artifact; M9 §9.84 examines replication, correction, and the distinction between unreliable evidence and personal culpability. The [research-integrity sources](01_Resources/52_Research_Integrity_and_Replication/README.md) record publication statuses as of November 27, 2026.

Sessions 2 and 14 include these cases within their existing measurement and ethical-reasoning activities. The expanded decks provide alternative examples; the 170-minute meetings, dates, and pending assessment policies remain unchanged. The [optional replication exercise](07_Labs/Research_Integrity/README.md) and [artifact exercise](07_Labs/Data_Truth_and_Norms/README.md) require a defensible inference, maxim, and allocation of responsibility.

## Evidence, Claims, and Decisions

M1 §1.25, M2 §2.36, M5 §5.30, M7 §7.49, and M9 §9.85 connect source preservation to claim support, checking coverage, authority, and reasonable objection. An original eight-case example reconstructs a reported electricity-price result and demonstrates an unsupported sentence that passes correct metadata checks. The complete Python, six tests, two editable TikZ figures, and optional exercise accompany selected discussion in Sessions 1, 2, 7, 11, and 14.

See the [resource guide](01_Resources/53_Evidence_Governance/README.md), [program and results](03_Data_and_Code/Evidence_Governance/README.md), and [optional practice](07_Labs/Evidence_Governance/README.md). The diagnostic cases are authored examples, with no model calls or execution of upstream code.
