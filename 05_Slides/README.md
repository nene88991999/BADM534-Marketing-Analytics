# Marketing Analytics Lectures

By Nathan Yang

Fifteen session decks cover the eight core modules and Marketing Dialectics, with AI-assisted coding, recurring data cases, ethics, and regulation. Each meeting has a proposed 170-minute plan. The sequence has 13 instructional meetings and two provisional presentation meetings, with no guest speakers. The [Spring 2027 syllabus](../02_Syllabus/Marketing_Analytics_Syllabus.md) and dated session plan are available; assessment policies remain pending.

The combined deck contains 442 slides. Read the [combined deck](Marketing_Analytics_Lectures.pdf), the [session plan](SESSION_PLAN.md), or a session below. Each PDF has editable LaTeX and a complete Markdown companion with projected text, code, equations, figure descriptions, and substantive presenter notes.

## Session Decks

| Session | Topic | PDF | Markdown | LaTeX |
| --- | --- | --- | --- | --- |
| 01 | Marketing Decisions and AI-Assisted Coding | [Slides](S01_Marketing_Decisions_and_AI_Coding.pdf) | [Companion](S01_Marketing_Decisions_and_AI_Coding.md) | [Source](S01_Marketing_Decisions_and_AI_Coding.tex) |
| 02 | Customer Data and Measurement | [Slides](S02_Customer_Data_and_Measurement.pdf) | [Companion](S02_Customer_Data_and_Measurement.md) | [Source](S02_Customer_Data_and_Measurement.tex) |
| 03 | Visualization and Data Quality | [Slides](S03_Visualization_and_Data_Quality.pdf) | [Companion](S03_Visualization_and_Data_Quality.md) | [Source](S03_Visualization_and_Data_Quality.tex) |
| 04 | Regression and Marketing Interpretation | [Slides](S04_Regression_and_Marketing_Interpretation.pdf) | [Companion](S04_Regression_and_Marketing_Interpretation.md) | [Source](S04_Regression_and_Marketing_Interpretation.tex) |
| 05 | Conjoint and Product Design | [Slides](S05_Conjoint_and_Product_Design.pdf) | [Companion](S05_Conjoint_and_Product_Design.md) | [Source](S05_Conjoint_and_Product_Design.tex) |
| 06 | Segmentation and Customer Lifetime Value | [Slides](S06_Segmentation_and_Customer_Lifetime_Value.pdf) | [Companion](S06_Segmentation_and_Customer_Lifetime_Value.md) | [Source](S06_Segmentation_and_Customer_Lifetime_Value.tex) |
| 07 | Text, Social Media, and Networks | [Slides](S07_Text_Social_Media_and_Networks.pdf) | [Companion](S07_Text_Social_Media_and_Networks.md) | [Source](S07_Text_Social_Media_and_Networks.tex) |
| 08 | Project Evidence and Midterm Presentations | [Slides](S08_Project_Evidence_and_Midterm_Presentations.pdf) | [Companion](S08_Project_Evidence_and_Midterm_Presentations.md) | [Source](S08_Project_Evidence_and_Midterm_Presentations.tex) |
| 09 | Experiments and Incremental Value | [Slides](S09_Experiments_and_Incremental_Value.pdf) | [Companion](S09_Experiments_and_Incremental_Value.md) | [Source](S09_Experiments_and_Incremental_Value.tex) |
| 10 | Causal Comparisons and Policy Evaluation | [Slides](S10_Causal_Comparisons_and_Policy_Evaluation.pdf) | [Companion](S10_Causal_Comparisons_and_Policy_Evaluation.md) | [Source](S10_Causal_Comparisons_and_Policy_Evaluation.tex) |
| 11 | Prediction, Validation, and Marketing Actions | [Slides](S11_Prediction_Validation_and_Marketing_Actions.pdf) | [Companion](S11_Prediction_Validation_and_Marketing_Actions.md) | [Source](S11_Prediction_Validation_and_Marketing_Actions.tex) |
| 12 | Recommendation Systems and Customer Goals | [Slides](S12_Recommendation_Systems_and_Customer_Goals.pdf) | [Companion](S12_Recommendation_Systems_and_Customer_Goals.md) | [Source](S12_Recommendation_Systems_and_Customer_Goals.tex) |
| 13 | Adaptive Recommendations and Marketing Budgets | [Slides](S13_Adaptive_Recommendations_and_Marketing_Budgets.pdf) | [Companion](S13_Adaptive_Recommendations_and_Marketing_Budgets.md) | [Source](S13_Adaptive_Recommendations_and_Marketing_Budgets.tex) |
| 14 | Generative AI, Consumer Choice, and Regulation | [Slides](S14_Generative_AI_Consumer_Choice_and_Regulation.pdf) | [Companion](S14_Generative_AI_Consumer_Choice_and_Regulation.md) | [Source](S14_Generative_AI_Consumer_Choice_and_Regulation.tex) |
| 15 | Integrated Decisions and Final Presentations | [Slides](S15_Integrated_Decisions_and_Final_Presentations.pdf) | [Companion](S15_Integrated_Decisions_and_Final_Presentations.md) | [Source](S15_Integrated_Decisions_and_Final_Presentations.tex) |

## Related Materials

- [Full lecture notes](../06_Lecture_Notes/README.md), including complete code for empirical examples.
- [Small runnable session calculations](../03_Data_and_Code/Lecture_Examples/session_examples.py) and [executed results](../03_Data_and_Code/Lecture_Examples/session_calculations.json).
- [Retention-procedure calculation](../03_Data_and_Code/Lecture_Examples/retention_welfare.py), with an aggregate table and fixed-stakes interpretation.
- [Ethics and regulation](../06_Lecture_Notes/ETHICS_AND_REGULATION.md), including module connections and primary-source status.

## Format and Editing

The decks use the supplied 16:9 Beamer format with parchment backgrounds, Illinois colors, editable TikZ, and Chinese ink-and-color artwork. [Art direction](ART_DIRECTION.md) records the brushwork research and visual conventions. [Artwork provenance](assets/PROVENANCE.md) identifies the four generated illustrations and their prompts.

Edit [source/sessions.json](source/sessions.json) and [theme.tex](theme.tex), then use [the build commands](BUILD.md) to refresh LaTeX, Markdown, and PDF together. Follow [AGENTS.md](AGENTS.md) when revising content or using these materials with an assistant.

Markdown companions identify the session and module, learning objectives, slide-number anchors, chart descriptions, definitions, equations, and referenced resources. Record the version in `session_plan.json`; identify omissions when preparing a shorter summary and link related labs when available.

## Earnings-Call Worked Example

Sessions 02, 07, 10, and 14 now use the [earnings-call case](../03_Data_and_Code/Earnings_Calls/README.md). The case covers missing documents, selected denominators, role-specific word exposure, interpretation of pricing language, event-window comparisons, and regulatory evidence. Session 07 uses its worked-comparison and Python blocks for this case; the meeting remains 170 minutes. The four analysis programs and nine tests ran successfully. Complete code appears in the module notes.

## AI Workflow Evaluation and Economics

Sessions 01, 05, 07, 09, 11, and 14 connect failure diagnosis, customer alternatives, prompt revision, factorial comparisons, selection on development accuracy, and reuse economics. The [three complete programs](../03_Data_and_Code/AI_Workflows/README.md) use synthetic inputs and require no model account. Four new TikZ figures show interaction, selection, break-even workload, and price bounds. These additions fit the existing session blocks, with the 75-minute ethics and regulation block in Session 14 retained.

## Consumer Agency and Research Networks

Sessions 3, 6, 7, 9, 12, and 14 add evidence coverage, mechanism clustering, LLM coding, university affiliation communities, downstream customer outcomes, recommendation welfare, and cancellation-policy distinctions. The [complete programs and outputs](../03_Data_and_Code/Consumer_Agency_Literature/README.md) accompany the notes. Four editable TikZ figures retain explicit populations and denominators. The 15-session schedule and the 75-minute regulation block in Session 14 remain in place.

## Changing AI Evidence

Sessions 01, 03, 07, 11, and 14 incorporate versioned claims, censored follow-up, changing AI judges, paired regressions, and residual risk. The [source guide](../01_Resources/14_LLM_Evidence_and_Revalidation/README.md) and [three complete programs](../03_Data_and_Code/LLM_Revalidation/README.md) preserve versions, units, and evidence scope. Three editable TikZ figures distinguish published descriptive results from constructed comparisons. Existing meeting durations and the Session 14 regulation block are retained.

## Marketing Dialectics in Session 14

Session 14 incorporates [Chapter 9](../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md) in the existing 75-minute ethics block. New material examines Kantian premises and respect for persons, conflicting commercial interests, Confucian conduct, identical renewal with different customer intent, and contrasting environmental-claim rulings. The [session plan](SESSION_PLAN.md) preserves all 15 dated meetings and pending assessment rules.

## AI Experimentation and Pricing

Sessions 9 and 14 incorporate the [research and policy case](../01_Resources/16_AI_Experimentation_and_Pricing/README.md). The detailed Kantian argument and complete pricing code are in Marketing Dialectics, Sections 9.14–9.18.

## Statistical Graphics

Sessions 3 and 11 include paired spending and ranking-versus-calibration comparisons, supported by [complete Python and synthetic inputs](../03_Data_and_Code/Statistical_Graphics/README.md). The detailed explanations are M2 §2.22 and M7 §7.23.

## Prediction Uncertainty

Session 11 adds calibration ranks, coverage by segment, and complaint-label sets. Session 13 examines coverage after an imposed demand change. [The complete code and records](../03_Data_and_Code/Conformal_Prediction/README.md) accompany M7 §§7.24–7.25 and M8 §8.21. Two editable TikZ figures retain the synthetic inputs, counts, and interpretation.

## Evidence Selection and AI Graders

Session 7 adds citation support and a controlled source-comparison protocol. Session 11 compares graders with equal balanced accuracy and different error costs. Two editable TikZ figures and [public practice activities](../07_Labs/AI_Evidence_and_Evaluation/README.md) accompany M5 §§5.19–5.20. All saved answers and grader decisions are synthetic.

## Clustering Optimization

Session 6 adds weighted centroid updates, final-label consistency, a local CPU comparison, and customer-action interpretation. [The full programs](../03_Data_and_Code/Clustering_Optimization/README.md) and [optional practice](../07_Labs/Clustering_Optimization/README.md) accompany four new slides and two editable figures. The 15-minute discussion fits the existing application block.

## Discount Response and Decision Objectives

Session 10 adds five slides on nonlinear discount responses, doubly robust adjustment, conditional support, interval coverage, and store pooling. Session 13 adds two slides on objectives and customer judgment. [Complete Python](../03_Data_and_Code/Dose_Response/README.md) and [optional practice](../07_Labs/Dose_Response/README.md) accompany three new editable TikZ figures. The discussion fits existing 20-minute and 15-minute allocations.

## Retail Alternatives and Service Access

Sessions 3, 7, and 13 add eight slides on map footprints, network distances, missing availability, and restoration priorities. Four editable TikZ figures accompany [complete Python and frozen inputs](../03_Data_and_Code/Retail_Accessibility/README.md). The [optional lab](../07_Labs/Retail_Accessibility/README.md) extends the discussion, with graph neural networks reserved for further study. The case uses existing application time.

## Anomaly Detection and Diagnosis

Session 11 adds six slides on three synthetic retail events, symptom rankings, monitoring denominators, interval quality, future-information leakage, and supported explanations. [Two complete programs](../03_Data_and_Code/Anomaly_Diagnosis/README.md) and [optional practice](../07_Labs/Anomaly_Diagnosis/README.md) accompany two editable TikZ figures. The case uses minutes 125–145; the remaining ten application minutes compare forecasts and grader outcomes. The meeting remains 170 minutes.

## Inference Efficiency in Session 11

Four slides connect token verification, synthetic draft-length costs, reported SciQA adaptation results, and correct customer-service resolution. The ten-minute comparison occupies minutes 60–70; the conformal Python exercise and anomaly-diagnosis allocation remain in place. [Complete programs and results](../03_Data_and_Code/Inference_Efficiency/README.md), [M7 §§7.31–7.32](../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md), and [optional practice](../07_Labs/Inference_Efficiency/README.md) distinguish source benchmarks from original synthetic calculations.

## Training Mixtures in Session 11

Five slides connect training-source combinations, ridge attribution, final and selected checkpoints, paired customer-service outcomes, and meaningful customer choice. Minutes 15–30 cover validation and regularization; minutes 30–45 cover the new comparison. [Three complete programs](../03_Data_and_Code/Training_Data_Mixtures/README.md), [M7 §§7.33–7.35](../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md), and [optional practice](../07_Labs/Training_Data_Mixtures/README.md) provide the longer calculations. Two editable TikZ figures retain score units, source counts, attempted-request denominators, and explicit synthetic labels.

## Synthetic Consumers and Product Research

Session 5 adds four slides on concept screening, distribution fit, shortlist errors, and human validation. Session 7 adds three slides on anchor mappings, a fixed-response comparison, and a hand calculation. Session 14 adds consumer representation within the existing philosophical discussion. Two editable TikZ figures and [two complete programs](../03_Data_and_Code/Synthetic_Consumers/README.md) accompany M4 §4.23, M5 §5.23, M7 §7.36, and M9 §9.18.4. The allocated discussions use 20, 10, and 5 minutes of the existing meetings, respectively.

## Reproducible Recommendations

Session 1 uses minutes 125–140 for response weights and a reproducible recommendation, followed by minutes 140–155 for the campaign specification. Two additional slides connect the repeat-weight figure to numerical evidence and interpretation. Session 14 uses five minutes of its existing opening block for review of an exported recommendation. M1 §1.15, M8 §8.25, and the [optional lab](../07_Labs/Reproducible_Recommendations/README.md) provide the full program and separate calculation, interpretation, rendering, and publication checks. The fifteen dates and 170-minute meetings remain fixed.

## Auxiliary Data and Human Validation

Sessions 4, 5, 9, and 11 add nine slides on response and bias coefficients, feature and price contrasts, research cost, fixed designs, and omitted-bias evaluation. Three editable TikZ figures use the [verified analytic tables](../03_Data_and_Code/Auxiliary_Data/results/README.md). The revised session plan assigns 10, 15, 10, and 10 minutes respectively within existing meeting blocks. Full Python appears in M4 §4.24 and M7 §7.37; [optional ungraded practice](../07_Labs/Auxiliary_Data/README.md) extends the sensitivity calculations.

## Graph Coarsening and Predictive Evidence

Session 7 adds three slides on group means, access, and preprocessing. Session 11 adds two slides on label purity and outcome information. [Two complete Python programs](../03_Data_and_Code/Graph_Coarsening/README.md), two TikZ figures, and [optional practice](../07_Labs/Graph_Coarsening/README.md) support M5 §5.24 and M7 §7.38. Fifteen minutes in Session 7 and five in Session 11 use existing meeting blocks.

## Definitions, Evidence, and Representation Quality

Sessions 1 and 2 distinguish event definitions, logical inference, validation, and recorded completion. Session 11 compares reconstruction with review recall and examines nonunique features. Session 14 connects classifications to evidence and customer permission. Ten new slides and three editable diagrams accompany [complete Python](../03_Data_and_Code/Representation_Evaluation/README.md) and the [cancellation case](../03_Data_and_Code/Ontology_and_Evidence/README.md). All fifteen meetings remain 170 minutes.

## Agent Workflow Evaluation

Sessions 1, 9, 11, and 14 include eight slides on the fixed mHealth logging roster, information and feedback, customer-level grading, hypothetical total costs, and customer authorization. [Full programs and optional practice](../07_Labs/Agent_Workflows/README.md) support the comparison. Existing meeting dates and 170-minute allocations are retained.

## Representation Alignment

Sessions 7, 11, and 14 add five slides connecting text coordinates, classifier compatibility, mHealth evaluation, and independent reasons. Two original editable figures accompany [complete Python and results](../03_Data_and_Code/Representation_Alignment/README.md). Session 11 assigns minutes 100–115 to reconstruction, alignment, and representation evaluation; the adjacent interval exercise uses minutes 80–100. All meetings remain 170 minutes. The longer coding work is [optional ungraded practice](../07_Labs/Representation_Alignment/README.md).

## Pricing Systems and Customer Choice

Session 5 adds the independent and joint pricing equations and a surplus figure. Session 14 adds the Wendy's case, the data-and-authority diagram, evidence questions, and the numerical comparison; existing philosophical discussion applies the case. Six additional slides have complete Markdown companions and source links. [Code and optional practice](../03_Data_and_Code/Pricing_Competition/README.md) support the unchanged fifteen 170-minute meetings.

## Digital Usage and Customer Access

Sessions 2, 3, 4, 6, and 14 include ten slides on geographic measurement, index verification, Census maps, income projections, clustering, and meaningful customer choice. The [complete Python example](../03_Data_and_Code/Digital_Usage/README.md) and [optional lab](../07_Labs/Digital_Usage/README.md) support longer practice within the existing course plan.

## Statistical Evidence and Customer Reasons

Seven slides in Sessions 1, 4, 9, and 14 connect generated statistical code, paired mHealth uncertainty, store assignment, false discoveries, and the interpretation of an advertising test. [Complete Python and results](../03_Data_and_Code/Statistical_Inference/README.md) accompany the notes and [optional practice](../07_Labs/Statistical_Inference/README.md). The existing 15 meetings and their 170-minute allocations are retained.

## Coding Workflows and Hidden Errors

Sessions 1, 4, 9, 11, and 14 include six additional slides on published workflow results, uncertainty checks, prompt-effect scales, constructed mHealth errors, and hypothetical decision losses. Two new editable TikZ figures preserve the comparison denominators and cost assumptions. [Source guide](../01_Resources/40_Econometric_Coding_Workflows/README.md); [Python and checks](../03_Data_and_Code/Agent_Workflows/README.md).

## Statistical Claims and the Ethics of Public Reassurance

The [resource and claim assessment](../01_Resources/41_Statistical_Claims_and_Decisions/README.md) connects Lakens’s inference guidance with the data-center electricity paper. M2 §2.28 distinguishes average prices, household incidence, and ownership categories. M3 §3.19 simulates repeated p-values; M6 §§6.32–6.33 compare detection with profit and reconstruct power, bounds, subgroup tests, sales mechanisms, and residual arithmetic. M8 §8.31 evaluates public communication. M9 §§9.25–9.26 develop equivalence, ontology, reasons, authority, Kantian duties, and Confucian trustworthiness. Four full Python listings and five editable Illinois-color figures accompany the notes. Sessions 4, 9, and 14 add eleven slides within existing allocations. The case distinguishes verified academic coverage from unverified company dissemination, demonstrated interpretation problems from replication questions, and possible harm from established consequences.
