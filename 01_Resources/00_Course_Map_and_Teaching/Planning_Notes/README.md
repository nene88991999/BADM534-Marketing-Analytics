# Syllabus Coverage and Teaching Priorities

[Resource Library](../../README.md) | [Teaching Resources](../README.md)

The course asks students to use customer and marketing data to support managerial decisions. The sample syllabus supplies a coherent progression from preparing data to estimating relationships, understanding preferences, measuring interventions, and predicting behavior. AI-assisted coding can support that progression by making implementation more accessible while preserving students' responsibility for the analytical choices and interpretation.

## Basis in the Sample Syllabus

Source: Unnati Narang, BADM 534, Spring 2026, reviewed October 23, 2026. The original PDF remains a [local instructor reference](../../../00_Sample_Materials/README.md) and is excluded from Git publication. The module list and objectives appear on page 1, software and readings on page 2, evaluation on page 3, AI guidance on pages 4-5, and the dated schedule on page 6.

The course uses Python, with some R, and allows Google Colab notebooks. Each module combines concepts, methodology, exercises, and interpretation. Its team project develops through a plan, checkpoints, a midterm, and a final report with code and visualizations. These elements provide a useful basis for an interactive written course. The schedule gives particular attention to customer data, visualization, text, causality, and prediction. Clustering and customer lifetime value appear in the module list even though they are not separately named in the dated schedule. Network analysis appears in the introductory description and can remain an optional extension.

Two passages require reconciliation when the new syllabus is written. Page 4 describes generative AI as a report-writing assistant, while page 5 explicitly permits coding assistance and asks students to document AI contributions. The revised policy should state the allowed uses for each assessment and retain clear responsibility for submitted work. The source syllabus contains course-access information and should remain an instructor reference.

## Coverage Map

The activities below are planning suggestions. They are not completed lessons or a revised teaching schedule.

| Original Module | Marketing Decision or Question | Resource Candidates | AI-Assisted Activity | Evidence of Understanding |
| --- | --- | --- | --- | --- |
| M1. Introduction to Marketing Analytics and Python | What data and calculations would inform the decision? | P01, P03, P05, P08-P10; AI01/AI03/AI04 | Turn an analysis request into a short specification and implement one function at a time. | Explain inputs, outputs, units, and a hand-worked test case. |
| M2. Customer Data and Visualization | Which customer patterns warrant attention? | V01-V07; D01, D09 | Ask an assistant to clean transactions, join tables, and construct a chart. | Reconcile totals, inspect unmatched rows, state denominators, and justify chart choices. |
| M3. Regression Analysis | How are customer outcomes related to observed characteristics? | R01-R07; P10; D02 | Generate a regression formula, estimation code, and diagnostics. | Interpret coefficients with units and distinguish association from a causal claim. |
| M4. Conjoint Analysis, Clustering, and Customer Lifetime Value | Which product design, customer groups, or retention priorities should receive attention? | C01-C12; P10; D01, D09 | Compare product profiles, alternative segmentations, or repeat-purchase forecasts. | Explain the choice set, scaling, segment stability, or prediction horizon and assumptions. |
| M5. Content Analysis and Textual Data | What can customer language reveal about products and service? | X01-X09; D04; optional D07 | Build a transparent text baseline and compare it with a richer representation or optional LLM labeling. | Audit a manually labeled sample and show representative mistakes and domain differences. |
| M6. Causal Models and Experiments | Did the marketing intervention change outcomes? | E01-E09; optional D06 | Simulate or analyze an experiment, then examine a confounded observational comparison. | State assignment, estimand, assumptions, uncertainty, and the decision-relevant effect. |
| M7. Predictive Models, AI, and Machine Learning | Which customers or sessions are likely to respond, and what action follows? | M01-M10; R02; D02-D03 | Generate a pipeline, compare baselines, tune a decision threshold, and evaluate on held-out observations. | Explain information availability, splitting, leakage, calibration, and expected decision costs. |
| M8. Current Topics in Marketing | How can newer methods improve a particular marketing decision? | A01-A09; D05-D08 | Select one extension such as recommendation, forecasting, MMM, or generative AI. | Compare with a simpler baseline and state what the data and method establish. |

## Suggested Priorities

Develop the core around three recurring data settings: transactions for customer analysis, campaign or session records for prediction, and short reviews for text analysis. Use a separate experiment or clearly labeled simulated dataset for causality. This reduces setup time and lets students revisit familiar data with new methods. The [Dataset Guide](../../10_Datasets_and_Project_Resources/Dataset_Guide/README.md) explains the available choices.

Start each exercise with a managerial decision, the information available at that decision, and a specified output. Follow with the method, a small example, guided implementation, a check of the result, and interpretation. Allow AI assistance in the implementation stages while requiring students to explain the decisions that determine the analysis. A generated program that runs is insufficient evidence that the estimand, sample, or validation procedure is appropriate.

Keep the original staged project structure as a candidate. Each checkpoint can preserve the data dictionary, current analysis plan, reproducible outputs, and a short record of consequential AI contributions. Individual explanations of a data transformation, code repair, or modeling choice can help assess understanding within team work. Set the grading weights after deciding the expected student preparation and available teaching time.

## Decisions for the Next Phase

The resource collection supports beginning lesson and wiki planning. The next decisions are the expected entry-level Python knowledge; the balance between conceptual interpretation and implementation; the institution-supported coding tools available to students; the core dataset sequence; and the amount of executable Python that should run in a browser. An institutional access check and a small representative execution test can resolve these before committing to a publishing system.

The new wiki should prioritize the eight core modules. Advanced causal machine learning, full Bayesian estimation, large language-model training, large review corpora, and production web applications are optional project extensions. Their source materials are included so that selecting an extension does not require restarting the search.
