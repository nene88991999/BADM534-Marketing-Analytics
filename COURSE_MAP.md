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

The [lecture-note index](06_Lecture_Notes/README.md) maps the eight core modules and Marketing Dialectics to detailed explanations, worked cases, and 114 figures. [Synthetic data and reproducible calculations](03_Data_and_Code/Lecture_Examples/README.md) accompany the notes. These notes do not establish current assessment requirements.

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
