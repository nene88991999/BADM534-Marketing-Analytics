# Marketing Analytics

Course materials for Nathan Yang's planned offering, with AI-assisted coding integrated into marketing analytics. The topic sequence builds on Unnati Narang's Spring 2026 course.

**Status:** course preparation, with lecture notes and 15 session decks covering the eight core modules and Marketing Dialectics. The [Spring 2027 syllabus](02_Syllabus/Marketing_Analytics_Syllabus.md) and dated meeting plan are available. Assignments, grading rules, and assessment policies remain pending. A [local interactive HTML pilot](08_Wiki/pilot/README.md) is available; the broader wiki and deployment remain pending. Resource recommendations and teaching suggestions are not assigned work.

## Start Here

- **Students:** read the [Student and LLM Guide](LLM_GUIDE.md), then the [Course Map](COURSE_MAP.md).
- **Coding agents:** read [AGENTS.md](AGENTS.md) and [course.json](course.json) before interpreting course requirements or changing files.
- **One-file LLM context:** download [llms-full.txt](llms-full.txt). It contains the navigation guides and compact resource metadata, with source paths for follow-up reading.
- **Instructor:** use [CONTRIBUTING.md](CONTRIBUTING.md) to add materials and publish reviewed updates, following the [course writing guide](WRITING_STYLE.md).
- **Lecture notes:** begin with the [Preface](06_Lecture_Notes/Preface.md) on analytical tools and philosophical reasoning, then read the [lecture notes](06_Lecture_Notes/README.md), with 140 TikZ figures, complete Python code, [recurring mHealth cases](03_Data_and_Code/mHealth/recurring_examples/README.md), [McDonald's availability cases](03_Data_and_Code/McBroken/README.md), [generative-AI demand cases](03_Data_and_Code/GenAI_Demand/README.md), and [synthetic numerical examples](03_Data_and_Code/Lecture_Examples/README.md).
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
| [08_Wiki](08_Wiki/README.md) | Static electricity lesson pilot and future wiki design |

## Working with an LLM

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

[Chapter 9](06_Lecture_Notes/modules/M09_Marketing_Dialectics.md) examines marketing claims through Kantian critique and ethics, scrutiny of interested power (Hume, 1741; Smith, 1776), and Confucian insights on conduct. It includes a [standalone PDF](06_Lecture_Notes/Marketing_Dialectics.pdf), [reproducible Python case](03_Data_and_Code/Marketing_Dialectics/README.md), and [categorized reading library](01_Resources/15_Marketing_Dialectics/README.md).

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

## Network Compression and Customer Access

[M5 §5.24 and M7 §7.38](03_Data_and_Code/Graph_Coarsening/README.md) compare aggregation weights, preserved revenue, distorted travel, oracle label purity, and outcome use during preprocessing. Complete Python, two editable figures, five slides in Sessions 7 and 11, and [optional practice](07_Labs/Graph_Coarsening/README.md) accompany the synthetic cases.

## Definitions and Representation Quality

[Cancellation evidence](03_Data_and_Code/Ontology_and_Evidence/README.md) connects M1 §1.16 and M2 §2.25 to event definitions, validation, unknown states, and a fixed reporting cutoff. [Representation evaluation](03_Data_and_Code/Representation_Evaluation/README.md) connects M7 §§7.39–7.40 to variance-weighted reconstruction, review recall, and nonunique features. Three complete Python programs, fourteen independent tests, and three editable figures support the synthetic cases. M4 §4.25, M5 §5.25, and M9 §9.19 connect segment interpretation, attributed claims, and permission evidence. Sessions 1, 2, 11, and 14 include ten additional slides within the existing meeting times.

## AI Workflow Evaluation

[The workflow example](03_Data_and_Code/Agent_Workflows/README.md) connects a fixed mHealth logging roster, a four-configuration experiment protocol, customer-level checker tests, total workflow cost, and customer authority. Four complete programs and two editable TikZ figures appear in M1 §1.17, M6 §6.29, M7 §7.41, M8 §8.26, and M9 §9.20. [Optional ungraded practice](07_Labs/Agent_Workflows/README.md) separates observed logging calculations, hypothetical costs, and an unexecuted model-comparison protocol.

## Representation Alignment and Text Decisions

[Three original programs](03_Data_and_Code/Representation_Alignment/README.md) connect coordinate alignment, fixed-classifier compatibility, and retraining on mHealth descriptions. Complete Python, two editable figures, five slides, and [optional practice](07_Labs/Representation_Alignment/README.md) accompany M5, M7, M8, and Marketing Dialectics. The [source review](01_Resources/36_Representation_Alignment/README.md) distinguishes the neural-model research from the local course calculations.

## Pricing Systems and Customer Choice

[The Wendy's case and source review](01_Resources/37_Pricing_Systems_and_Competition/README.md) connect disputed pricing authority to customer choice. [An original two-restaurant model](03_Data_and_Code/Pricing_Competition/README.md) separates demand information from joint pricing with complete Python, nine checks, and two editable figures. M4 §4.26, M8 §8.28, M9 §9.22, Sessions 5 and 14, and [optional practice](07_Labs/Pricing_Competition/README.md) carry the analysis.

## Digital Usage and Customer Access

The [digital-usage case](03_Data_and_Code/Digital_Usage/README.md) connects public geographic application indices to measurement, Census comparisons, regression, clustering, and customer choice. Complete Python, source rights, and optional ungraded practice accompany the notes and five session decks.

## Statistical Evidence for Marketing Decisions

[Original Python examples](03_Data_and_Code/Statistical_Inference/README.md) examine uncertainty in observed mHealth logging and false discoveries in synthetic store experiments. M1 §1.18, M3 §3.18, M6 §6.30, and M9 §9.24 connect statistical assessment to AI-assisted coding and customer agency. [Optional practice](07_Labs/Statistical_Inference/README.md) and the [Fisher-R1 source review](01_Resources/39_Statistical_Inference_and_AI/README.md) accompany two editable figures and seven slides across Sessions 1, 4, 9, and 14.

## Coding Workflows and Hidden Errors

[The coding-workflow collection](01_Resources/40_Econometric_Coding_Workflows/README.md) connects published benchmark evidence to [reproducible Python examples](03_Data_and_Code/Agent_Workflows/README.md). The notes and slides distinguish execution, numerical correctness, customer-level allocation, and the cost of undetected errors.

## Statistical Claims, Household Burdens, and Agency

The [statistical-claims examples](01_Resources/41_Statistical_Claims_and_Decisions/README.md) connect repeated p-values, economic thresholds, equivalence, and a recurring data-center electricity case. M2 §2.28, M3 §3.19, M6 §§6.32–6.33, M8 §8.31, and M9 §§9.25–9.26 examine reported tables, measurement, causal interpretation, public reassurance, ontology, and household authority. Four complete Python programs and five original TikZ figures support the comparisons. Guided practice is optional and ungraded.

## Logical Assessment and Inverse Power

M6 §6.34 develops the inverse-power approach (Andrews, 1989) with specified alternatives, nuisance parameters, and directional sensitivity. M9 §9.27 reconstructs the electricity arguments through premises, counterexamples, measurement, extrapolation, and household authority. The [argument record](01_Resources/41_Statistical_Claims_and_Decisions/ARGUMENT_ASSESSMENT.md) links claims to evidence and repairs. Two complete Python examples and two editable TikZ figures support the discussion. Sessions 9 and 14 use selected examples within existing meeting allocations; extended calculations remain optional ungraded practice.

## Institutional Context and Household Costs

The recurring electricity case now connects average prices to household expenditure and operating entry to the wider project pipeline. [Worked Python examples](03_Data_and_Code/Statistical_Inference/README.md) show how cancelled projects and cost-recovery rules can change a comparison. See the [institutional assessment](01_Resources/41_Statistical_Claims_and_Decisions/INSTITUTIONAL_ASSESSMENT.md), M2 §2.28.1, M6 §6.35, and M9 §9.27.6.

## Reasons and Affected People

[Marketing Dialectics](06_Lecture_Notes/modules/M09_Marketing_Dialectics.md) now includes Scanlonian arguments, stakeholder obligations, public voice, and publication responsibility. [Optional practice](07_Labs/Philosophical_Arguments/README.md) asks students to defend what an actor ought to do and answer the strongest objection from an affected person's position.

## Pricing, Individual Reasons, and Antitrust

The [pricing cases](03_Data_and_Code/AI_Experimentation_and_Pricing/README.md) connect demand assumptions, individual burdens, Kantian authority, and Scanlonian arguments to a hypothetical U.S. antitrust case. Five runnable programs and four TikZ figures accompany M4, M6, M8, and Marketing Dialectics. The competitive payoff table (Dubé et al., 2017) is reconstructed from published information. [Optional practice](07_Labs/Scanlon_Pricing/README.md) develops supported factual premises, an ought conclusion, and the strongest defense. Students distinguish an instrumentally rational choice from a reasonable principle. They assess measurement quality alongside the worth of the goal, then compare personalized pricing, dynamic-pricing communication, and data-center reassurance.

## Analytical Arguments and Counterexamples

[Exact synthetic examples](03_Data_and_Code/Analytical_Arguments/README.md) distinguish model fit from identification and product rankings from welfare valuations. M1, M4, M6, and Marketing Dialectics connect these comparisons to a [five-step argument exercise](07_Labs/Philosophical_Arguments/README.md), with an AI prompt, a strong reply to each criticism, and evidence or reasons that would change the conclusion.

M1 and [M9 §9.41](06_Lecture_Notes/modules/M09_Marketing_Dialectics.md) place the worth of the objective, the phenomena–noumena distinction (Kant, 1781/1787), and the practical standing of affected people before optimization. Sessions 1 and 14 connect the limits of empirical representation to separate arguments about ends, authority, and obligations. A fourth editable diagram distinguishes further empirical inquiry from the noumenal limiting concept (Kant, 1781/1787) and practical justification.

[M9 §§9.41–9.43](06_Lecture_Notes/modules/M09_Marketing_Dialectics.md) distinguish acknowledged epistemic limits from unknown unknowns and assess interpretations through an ontological spectrum. Electricity reassurance, personalized pricing, and cancellation connect to limits of cognition (Kant, 1781/1787), observational justification (Sellars, 1956), critical realism (Bhaskar, 2007), intentionality (Husserl, 1970), and normative reasons (Scanlon, 2009). Publication selection toward tractable questions remains a hypothesis separate from verified evidence of selection by result strength. Session 14 uses selected cases within its existing discussion blocks; the extended comparisons are optional practice.

## Explanation and Independent Judgment

The [electricity lesson](08_Wiki/pilot/README.md) asks students to predict a bill, inspect the calculation, compare four representations, and revise a household-cost claim. [Complete Python](03_Data_and_Code/Learning_Design/README.md) also distinguishes percentage points from relative changes and a learning package from its component effects. M1, M2, M6, and M9 connect these ideas to independent reasoning and learner authority. [Optional practice](07_Labs/AI_Augmented_Learning/README.md) includes a transfer task.

## Conflicts of Interest and Consumer Control

[Marketing Dialectics §§9.45–9.49](06_Lecture_Notes/modules/M09_Marketing_Dialectics.md) connects analyst incentives to duties, engagement design, and consumer authority. The [synthetic feed comparison](03_Data_and_Code/Conflicts_of_Interest/README.md), [source guide](01_Resources/15_Marketing_Dialectics/09_Conflicts_of_Interest/README.md), and [optional practice](07_Labs/Conflicts_of_Interest/README.md) distinguish empirical evidence from a defended ought conclusion.

## Bad Controls and Thoughtful Research Design

The [reading collection](01_Resources/44_Bad_Controls_and_Project_Exposure/README.md) covers causal adjustment, selection, treatment-affected covariates, anticipation, and exposed comparison groups. [Three original Python programs](03_Data_and_Code/Bad_Controls/README.md) connect these distinctions to phantom projects and the choice of a recent operating-facility sample. M3 §§3.20–3.21, M6 §§6.40–6.42, and M9 §9.50 develop the implications for household claims and research design.

## Data, Truth, and Norms

The [reading collection](01_Resources/45_Data_Truth_and_Norms/README.md) connects created artifacts (Thomasson, 1999, 2014), truth and warrant, institutional research priorities, and reasons owed to households. An [original Python example](03_Data_and_Code/Data_Production/README.md) constructs identical public records with opposite population effects. M2, M6, and M9 distinguish existing billing data from the project-linked evidence and causal design needed for household claims.

## Measurement Traditions and Evidence for Protection

The [integrated notes](06_Lecture_Notes/README.md#measurement-traditions-and-evidence-for-protection) connect measurement history, heterogeneous demand, error costs, and reasonable protection across M1–M9. A [complete synthetic calculation](03_Data_and_Code/Evidence_Standards/README.md) holds evidence fixed and changes the consequences of mistakes. [Optional practice](07_Labs/Evidence_Standards/README.md), selected slides, and the [electricity lesson](08_Wiki/pilot/index.html#uncertainty) connect the argument to pricing, household bills, and AI decisions.
