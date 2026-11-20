# Anomaly Detection and Marketing Diagnosis

A retailer observing a sudden fall in completed purchases must decide whether to change advertising, repair checkout, replenish inventory, or investigate measurement. The same sales decline can arise through several mechanisms. An unusual observation identifies a reason to investigate; the appropriate action depends on evidence about the process that generated it.

## Detection, Localization, and Interpretation

[Stanzione, Barbe, Parrino, Fourmann, and Boniol](https://arxiv.org/abs/2610.01168v1) distinguish detecting an anomaly, locating the dimensions involved, and interpreting the event. Their SHAD benchmark contains 215 series with 171 variables, generated through controlled failures in a real distributed storage system. The labels identify the components targeted by those failures. This setting supports separate evaluation of an alert, its attributed variables, and an account of the underlying event.

Figures 7 and 8 provide the strongest course connection. Several detectors perform well on detection while their variable rankings remain close to a random baseline for identifying the labeled components. The labels concern directly targeted components; downstream symptoms can carry strong predictive signals. A variable that helps recognize an event therefore need not identify its origin.

Figure 9 evaluates five frozen LLMs using statistical features, plots, and generated descriptions. Localization performs poorly under these tested procedures. Additional experiments provide correct anomaly-presence and component information. These comparisons describe performance conditional on ideal inputs. The evidence concerns one storage system and the specified prompting procedures; it does not establish performance for marketing data or a separately evaluated agent workflow.

## Managerial Applications

The distinction transfers to a checkout interruption. Payment latency, failed orders, conversion, support contacts, and refund requests may move together. The largest standardized change might occur in complaints after customers encounter the interruption. That variable could be useful for detection while a change to the payment service remains the relevant intervention. Deployment logs, transaction traces, and a controlled repair comparison supply different evidence from an anomaly score.

The existing restaurant-availability case offers a second application. A regional increase in recorded unavailability can reflect genuine service disruption, changing geographic coverage, or a collection failure. Assess the observation count and restaurant composition alongside the status rate. The public availability observations support analysis of recorded status. An equipment diagnosis requires maintenance evidence or an explicitly constructed example with known causes.

For mHealth, a discontinuity in recorded intake can reflect changed logging, missing records, units, or changed behavior. Keep recording completeness separate from nutritional quantities. A detected deviation can motivate a data assessment or a request for clarification; it does not establish a health condition or a customer's intent.

## Separate the Evaluation Questions

| Question | Evidence and Evaluation | Managerial Consequence |
| --- | --- | --- |
| Did a relevant event occur? | Labeled incidents, held-out normal periods, precision, recall, false alerts per day, and detection delay | Determines whether staff should investigate |
| Which variables or components are implicated? | Variable-level labels, explicitly defined target components, and comparisons with random rankings | Directs investigation toward an appropriate part of the process |
| What account is supported? | Claims linked to observations, domain definitions, alternative explanations, and incident records | Separates a supported diagnosis from a plausible story |
| How serious is the event? | Affected customers, duration, lost service, recovery cost, and the customer's purpose | Determines priority and the proportional response |
| Did the response help? | A credible intervention comparison and subsequent customer outcomes | Evaluates the remedy |

These rows specify a proposed marketing evaluation. They are not a replication of the SHAD metrics. A rare observation can be benign, and a frequent practice can still harm customers. Statistical unusualness and the desirability of intervention answer different questions.

## AI-Assisted Coding and Evaluation

The [repository inspection](SOURCE_REVIEW.md) identifies concrete teaching opportunities. Its loader's forward-fill option also backward-fills leading gaps, which can introduce future information in a live alert exercise. Its image generator drops incomplete rows and plots positions after that deletion, which makes timestamp preservation consequential. Its temporal evaluator accepts any overlap with a labeled interval, so a very broad predicted interval can receive credit despite poor localization. These are source-inspection findings, with the relevant functions and scope recorded in the review.

Students could ask a coding assistant to implement an alert and then independently assess preprocessing, timestamps, the held-out population, and the meaning of a successful test. A useful comparison supplies the same information in three forms: selected plots, computed summaries, and summaries with a variable dictionary. Ground-truth incident descriptions belong in the evaluator. Giving them to the model changes the task and must be identified explicitly.

## Connections to Existing Course Material

| Existing Material | Focused Extension |
| --- | --- |
| [M2 §§2.16–2.17](../../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md) | Separate an unusual business outcome from changing coverage, missing data, and collection errors |
| [M5 §§5.6 and 5.20](../../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md) | Evaluate structured explanations against incident evidence; assess the scoring rule itself |
| [M7 §§7.4, 7.9, 7.13, and 7.18](../../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md) | Compare detection, component localization, and explanation; preserve the live information set |
| [M8 §§8.6 and 8.11](../../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md) | Evaluate an AI-assisted investigation by supported claims, investigation cost, and customer outcomes |
| [M9 §§9.3 and 9.10](../../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md) | Examine the evidence required before an organization acts on a diagnosis |

[M7 §§7.29–7.30](../../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md) now contain the complete [retail programs](../../03_Data_and_Code/Anomaly_Diagnosis/README.md), exact timing and missingness comparisons, and two editable TikZ diagrams. Session 11 uses twenty minutes of its existing application block. The [optional lab](../../07_Labs/Anomaly_Diagnosis/README.md) supplies longer ungraded practice. Connections to other modules remain suggestions; the meeting calendar and assessment requirements are unchanged.

## Sources and Reuse

The [catalog](catalog.json), namespace `anomaly-diagnosis`, records paper version 1, the repository commit, file hashes, and rights. The unmodified paper is saved as [Stanzione et al., 2026](local_sources/Stanzione_Barbe_Parrino_Fourmann_Boniol_WorkingPaper2026.pdf) under CC BY 4.0. Selected repository files are retained under `local_sources/shad/` with the complete AGPL-3.0-only license and citation metadata. The repository snapshot is a reference selection, not an installable copy of the complete benchmark. No upstream program, notebook, detector benchmark, or paid LLM request was executed.

This Markdown companion explains the course-relevant findings and describes Figures 7–9 in words. It omits the full mathematical details, metric catalog, experimental registry, literature review, and remaining figures. Consult the original paper for those materials. The [source review](SOURCE_REVIEW.md) distinguishes the paper's claims from the inspected repository's behavior and the proposed teaching applications.
