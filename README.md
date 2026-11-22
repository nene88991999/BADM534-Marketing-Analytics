# Marketing Analytics

Course materials for Nathan Yang's planned offering, with AI-assisted coding integrated into marketing analytics. The topic sequence builds on Unnati Narang's Spring 2026 course.

**Status:** course preparation, with lecture notes and 15 session decks covering the eight core modules and Marketing Dialectics. The [Spring 2027 syllabus](02_Syllabus/Marketing_Analytics_Syllabus.md) and dated meeting plan are available. Assignments, grading rules, assessment policies, and the interactive HTML wiki remain pending. Resource recommendations and teaching suggestions are not assigned work.

## Start Here

- **Students:** read the [Student and LLM Guide](LLM_GUIDE.md), then the [Course Map](COURSE_MAP.md).
- **Coding agents:** read [AGENTS.md](AGENTS.md) and [course.json](course.json) before interpreting course requirements or changing files.
- **One-file LLM context:** download [llms-full.txt](llms-full.txt). It contains the navigation guides and compact resource metadata, with source paths for follow-up reading.
- **Instructor:** use [CONTRIBUTING.md](CONTRIBUTING.md) to add materials and publish reviewed updates.
- **Lecture notes:** read the [lecture notes](06_Lecture_Notes/README.md), with 87 TikZ figures, complete Python code, [recurring mHealth cases](03_Data_and_Code/mHealth/recurring_examples/README.md), [McDonald's availability cases](03_Data_and_Code/McBroken/README.md), [generative-AI demand cases](03_Data_and_Code/GenAI_Demand/README.md), and [synthetic numerical examples](03_Data_and_Code/Lecture_Examples/README.md).
- **Lectures:** read the [15 session decks](05_Slides/README.md) and [170-minute meeting plans](05_Slides/SESSION_PLAN.md), with [ethics and regulation](06_Lecture_Notes/ETHICS_AND_REGULATION.md) throughout.
- **Research library:** browse the [resource guide](01_Resources/README.md) and the [additional module catalog](01_Resources/00_Index/README.md). These overlapping collections retain their original provenance.

## Course Folders

| Folder | Contents |
| --- | --- |
| [01_Resources](01_Resources/README.md) | Categorized readings, documentation, notebooks, datasets, AI coding resources, and source catalogs |
| [02_Syllabus](02_Syllabus/README.md) | Spring 2027 syllabus, confirmed logistics, and policy status |
| [03_Data_and_Code](03_Data_and_Code/README.md) | Course datasets, dictionaries, scripts, notebooks, and code snippets |
| [04_Assignments](04_Assignments/README.md) | Assignment briefs, rubrics, and assessment-specific AI rules |
| [05_Slides](05_Slides/README.md) | Fifteen session decks, editable LaTeX, Markdown companions, and meeting plans |
| [06_Lecture_Notes](06_Lecture_Notes/README.md) | Searchable written explanations and worked examples |
| [07_Labs](07_Labs/README.md) | Course-tested notebooks, code, and environments |
| [08_Wiki](08_Wiki/README.md) | Future interactive HTML teaching site |

## Working With an LLM

Give the assistant `AGENTS.md`, `course.json`, the relevant module guide, and the specific syllabus or assignment file. Ask it to cite repository paths and source URLs, identify missing information, and explain analytical choices. Private GitHub links require authorized access; when a tool cannot access them, download the selected Markdown files and provide those files directly.

`llms.txt` is a navigation convention. It does not grant access or guarantee that a service reads the repository. `llms-full.txt` supports tools that accept one plain-text attachment.

## Repository Updates

Dropbox changes and GitHub commits are separate. Adding a file to Dropbox does not automatically upload it to GitHub. Follow [the update workflow](CONTRIBUTING.md#publish-an-update) to review and publish changes. Keep student submissions, grades, credentials, and instructor answer keys outside the student materials repository.

## Source Rights

Third-party files retain their original licenses and restrictions. See their adjacent license files, `SOURCE.md` records, and catalog entries. This repository has no blanket license that overrides those terms. Review individual materials before releasing a public site.

## Earnings-Call Worked Example

[Pricing communication in earnings calls](03_Data_and_Code/Earnings_Calls/README.md) now connects data assessment, text analytics, event comparisons, and customer-outcome interpretation across M2, M5, M6, and M8. The folder includes runnable Python, structured data, source-linked cases, and verification checks. Updated notes and Sessions 02, 07, 10, and 14 contain the worked examples.

## Recent Research and Consumer Agency

The [journal collection](01_Resources/13_Consumer_Agency_and_Recent_Research/README.md) indexes 2023-2026 research with managerial summaries, source versions, access gaps, and cancellation-policy resources. [Mechanism clustering](03_Data_and_Code/Consumer_Agency_Literature/README.md) and [university affiliation communities](03_Data_and_Code/Consumer_Agency_Literature/AFFILIATIONS.md) provide reproducible examples with explicit coding and sampling limits.

## LLM Evidence and Revalidation

The [source collection](01_Resources/14_LLM_Evidence_and_Revalidation/README.md) connects the shelf life of AI findings to model updates, changing judges, and fresh evaluation. [Three runnable examples](03_Data_and_Code/LLM_Revalidation/README.md) reproduce published follow-up summaries and distinguish them from constructed upgrade decisions. Complete code and three TikZ figures appear in the notes and corresponding session decks.

## Marketing Dialectics

[Chapter 9](06_Lecture_Notes/modules/M09_Marketing_Dialectics.md) examines marketing claims through Kantian critique and ethics, Hume and Smith on interested power, and Confucian insights on conduct. It includes a [standalone PDF](06_Lecture_Notes/Marketing_Dialectics.pdf), [reproducible Python case](03_Data_and_Code/Marketing_Dialectics/README.md), and [categorized reading library](01_Resources/15_Marketing_Dialectics/README.md).

## AI Experimentation and Pricing

[The research and policy case](01_Resources/16_AI_Experimentation_and_Pricing/README.md) connects AI-assisted experiments and personalized pricing to Kantian ethical evaluation. Marketing Dialectics includes the detailed argument, source-specific qualifications, and [complete reproducible calculations](03_Data_and_Code/AI_Experimentation_and_Pricing/README.md).

## Statistical Graphics

[PyStatlas and its course applications](01_Resources/17_PyStatlas_Statistical_Graphics/README.md) connect statistical questions to chart choices. [Two reproducible synthetic cases](03_Data_and_Code/Statistical_Graphics/README.md) examine paired customer changes and identical rankings with different purchase probabilities. Full explanations and Python appear in M2 §2.22 and M7 §7.23, with corresponding Session 3 and 11 slides.

## Prediction Uncertainty

[Conformal prediction](01_Resources/18_Conformal_Prediction/README.md) connects demand intervals, customer-service routing, and changing demand. [Two reproducible synthetic examples](03_Data_and_Code/Conformal_Prediction/README.md) accompany full Python in M7 §§7.24–7.25, interpretation in M8 §8.21, and Session 11 and 13 slides.

## Evidence Selection and AI Graders

[Two original examples](03_Data_and_Code/AI_Evidence_and_Evaluation/README.md) connect source selection, reference judgments, and the costs of incorrect approval. [Public practice activities](07_Labs/AI_Evidence_and_Evaluation/README.md) accompany full Python in M5 §§5.19–5.20 and Sessions 7 and 11.

## Clustering Optimization

[Clustering optimization](03_Data_and_Code/Clustering_Optimization/README.md) adds an exact centroid example, an executed CPU comparison, and [optional practice](07_Labs/Clustering_Optimization/README.md). M4 and Session 6 connect computational cost, final labels, and customer interpretation.

## Discount Response and Customer Outcomes

[Discount-response examples](03_Data_and_Code/Dose_Response/README.md) connect nonlinear effects, confounding, overlap, uncertainty, and store pooling to marketing choices. Complete Python, three editable figures, and [optional practice](07_Labs/Dose_Response/README.md) support M6, M8, and Marketing Dialectics.

## Retail Access and Service Priorities

[Retail accessibility](03_Data_and_Code/Retail_Accessibility/README.md) connects restaurant availability to feasible alternatives, missing-status bounds, geographic relationships, and service objectives. Three complete Python programs, four editable TikZ figures, and [optional practice](07_Labs/Retail_Accessibility/README.md) support six modules and Sessions 3, 7, and 13.

## Inference Efficiency and Customer Resolution

[Two runnable examples](03_Data_and_Code/Inference_Efficiency/README.md) compare draft-token progress with response time and reference-token accuracy with correct customer-service resolution. Full Python, two TikZ figures, and the worked case appear in M7 §§7.31–7.32, with four slides in Session 11 and [optional practice](07_Labs/Inference_Efficiency/README.md). All new data and timings are synthetic; the published G-MTP benchmark remains a separate attributed source.

## Training Mixtures and Customer Choice

[M7 §§7.33–7.35](06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md) connect confounded training features to conditional service outcomes and checkpoint selection. [Three complete programs](03_Data_and_Code/Training_Data_Mixtures/README.md), two TikZ figures, five Session 11 slides, and [optional practice](07_Labs/Training_Data_Mixtures/README.md) distinguish exact synthetic calculations from published model results. M2, M3, M8, and Marketing Dialectics connect source provenance, regression, supplier changes, and evidence for meaningful customer choice.

## Synthetic Consumers and Concept Screening

[Two complete examples](03_Data_and_Code/Synthetic_Consumers/README.md) connect product screening in M4 §4.23 to text measurement in M5 §5.23 and validation in M7 §7.36. Invented panels and imposed similarities isolate anchor sensitivity, persona weights, distribution fit, and shortlist errors. Sessions 5, 7, and 14 incorporate the comparisons and consumer-representation discussion. [Optional ungraded practice](07_Labs/Synthetic_Consumers/README.md) extends the calculations.
