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

The [lecture-note index](06_Lecture_Notes/README.md) maps the eight core modules and Marketing Dialectics to detailed explanations, worked cases, and 68 figures. [Synthetic data and reproducible calculations](03_Data_and_Code/Lecture_Examples/README.md) accompany the notes. These notes do not establish current assessment requirements.

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
