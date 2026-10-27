# Course Map

Marketing Analytics

This outline follows the eight topic families in Unnati Narang's Spring 2026 syllabus. It is a planning map for Nathan Yang's offering. The revised syllabus, schedule, assignments, and assessment rules are pending. Suggested activities below are illustrative.

## Topics and Resource Routes

| Module | Managerial Question | Core Topics | Resource Guide | AI-Assisted Practice |
| --- | --- | --- | --- | --- |
| M1 | What data and calculations inform a marketing decision? | Python, notebooks, reproducible analysis | [Python and Data](01_Resources/01_Python_Data_and_Reproducibility/README.md) | Turn a short specification into small functions; check a hand-worked example. |
| M2 | Which customer patterns deserve attention? | Data preparation, joins, summaries, visualization | [Customer Data and Visualization](01_Resources/02_Customer_Data_and_Visualization/README.md) | Generate a cleaning pipeline and chart; verify totals, units, and denominators. |
| M3 | How do observed customer characteristics relate to outcomes? | Regression, interpretation, diagnostics | [Regression](01_Resources/03_Regression_and_Statistical_Foundations/README.md) | Build and inspect a model; explain coefficients and distinguish association from causal effects. |
| M4 | Which product designs, customer groups, or retention priorities should receive attention? | Conjoint, segmentation, customer lifetime value | [Conjoint, Segmentation, and CLV](01_Resources/04_Conjoint_Segmentation_and_CLV/README.md) | Compare product profiles, segmentations, or repeat-purchase forecasts; check assumptions and stability. |
| M5 | What does customer language reveal about products and service? | Text, social media, sentiment, optional networks | [Text and Social Analysis](01_Resources/05_Text_Social_and_Network_Analysis/README.md) | Build a transparent text baseline, compare alternatives, and audit examples manually. |
| M6 | Did a marketing intervention change outcomes? | Experiments, causal estimands, identification, uncertainty, recommendation policy evaluation | [Causal Inference and Experiments](01_Resources/06_Causal_Inference_and_Experiments/README.md) | Simulate or analyze an experiment and contrast it with a confounded comparison. |
| M7 | Which customers are likely to respond, and which products should they see? | Prediction, validation, decision thresholds, recommender models, ranking, LLM explanations | [Prediction and ML](01_Resources/07_Prediction_and_Machine_Learning/README.md) | Build a leakage-aware pipeline; compare baselines and assess decision costs. |
| M8 | How can newer methods improve a specific marketing decision? | Adaptive recommendations, customer goals, platform incentives, marketing mix modeling, generative AI | [Current Topics](01_Resources/08_Current_Topics_in_Marketing/README.md) | Evaluate one extension against a simpler approach and state the supported conclusion. |

## Lecture Notes

The [lecture-note index](06_Lecture_Notes/README.md) maps all eight modules to detailed explanations, worked cases, and 47 figures. [Synthetic data and reproducible calculations](03_Data_and_Code/Lecture_Examples/README.md) accompany the notes. These notes do not establish current assessment requirements.

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

The [McBroken case](03_Data_and_Code/McBroken/README.md) uses the supplied McDonald's ordering-status data in three modules. M2 §2.16 audits coverage, missingness, address keys, and calendar joins. M6 §6.16 compares country trends around the 2024 repair exemption and distinguishes descriptive contrasts from causal evidence. M7 §7.18 evaluates next-observation forecasts on later dates, with label coverage and calibration. Five complete Python programs and three TikZ figures support these applications.

## Generative-AI Demand

The [GenAI demand cases](03_Data_and_Code/GenAI_Demand/README.md) connect M2 §2.17, M4 §4.14, and M8 §8.13. Students audit title-specific pageviews, compare provider and category retention within the same starting cohort, classify acquisition events, and test a price regression against its generating model. Three executed Python programs and three TikZ figures distinguish the supplied public capture from the synthetic consumer panel. The exact binary-logit benchmark recovers its imposed coefficient; dynamic-panel slopes remain descriptive.
