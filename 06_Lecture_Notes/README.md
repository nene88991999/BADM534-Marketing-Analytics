# Lecture Notes

**By Nathan Yang. Updated November 26, 2026.** These notes cover all eight topic families in the supplied Spring 2026 sample syllabus and integrate AI-assisted coding throughout. The [syllabus](../02_Syllabus/Marketing_Analytics_Syllabus.md) and Spring 2027 meeting calendar are available. Assessment rules and course-wide AI policy remain pending.

Read the [complete PDF](Marketing_Analytics_Lecture_Notes.pdf), beginning with the [Preface](Preface.md), or open a Markdown module below. The preface connects competence in analytical tools to philosophical reasoning about purposes, obligations, and the limits of measurement. The notes contain 147 original TikZ figures, recurring mHealth cases across M1–M8, worked synthetic cases, complete Python programs, practice questions, and source links. Markdown files provide searchable text and figure descriptions for students and LLMs. The PDF contains vector figures; the Markdown pages display PNG previews generated from the same TikZ sources.

## Modules and Syllabus Coverage

| Module | Notes and Core Coverage | Cases and Figures |
| --- | --- | --- |
| M1 | [Marketing Decisions, Data, and AI-Assisted Python](modules/M01_Marketing_Analytics_and_Python.md): analytical questions, observation units, joins, Python objects and functions, reproducibility, verification | Renewal response versus incremental value; duplicate-key joins; order value; coupon-campaign specification |
| M2 | [Customer Data, Measurement, and Visualization](modules/M02_Customer_Data_and_Visualization.md): customer tables, missingness, denominators, cohorts, charts, uncertainty, Pyramid Principle | Campaign-mix reversal; retention triangle; online grocery baskets and repeated purchases; variety and concentration |
| M3 | [Regression, Interpretation, and Marketing Decisions](modules/M03_Regression.md): OLS, controls, omitted variables, transformations, interactions, inference, diagnostics, panels | Rival presence and market demand; message effects by tenure; advertising contribution |
| M4 | [Product Preferences, Customer Segments, and Lifetime Value](modules/M04_Conjoint_Segmentation_and_CLV.md): conjoint design, logit, willingness to pay, substitution, clustering, scaling, CLV | Bundle cannibalization; nearest-neighbor reversal; nonlinear retention value; segment retention support |
| M5 | [Text, Social Media, and Customer Networks](modules/M05_Text_Social_and_Network_Analysis.md): text representation, TF-IDF, embeddings, sentiment, topics, annotation, networks | Complaint prevalence and precision; LLM label validation; network brokerage; engagement versus sales |
| M6 | [Causal Effects and Marketing Experiments](modules/M06_Causal_Inference_and_Experiments.md): estimands, selection, randomization, confidence intervals, power, adjustment, DiD, RD, IV, spillovers, recommendation policy evaluation | Email assignment and profit uncertainty; counterfactual trends; exposure-adjusted recommendation values; MovieLens information effects |
| M7 | [Prediction, Machine Learning, and Marketing Actions](modules/M07_Prediction_and_Machine_Learning.md): targets, regularization, trees, ensembles, validation, leakage, metrics, calibration, thresholds, recommender models, ranking, LLM explanations | Rare purchases; coupon targeting; NDCG; food variety and customer goals; goal-weight switches; explanation credibility |
| M8 | [Current Topics and Integrated Marketing Decisions](modules/M08_Current_Topics_and_Integrated_Decisions.md): adaptive recommendation, customer goals and platform incentives, media carryover and saturation, budget allocation, generative AI evaluation | Sleep-reminder campaign; Netflix personalization; content assessments and attitude experiments; relevance versus variety; marginal returns; AI workflow time |
| M9 | [Marketing Dialectics](modules/M09_Marketing_Dialectics.md): Kantian critique, respect for persons, conflicting interests, and Confucian conduct | Renewal and intent; advertising effects; personalization; environmental claims; 22 editable TikZ figures |

The sequence follows the historical syllabus's topics without adopting its dates, grading weights, or AI rules. M8 develops selected current topics; it is not a claim that the predecessor assigned these particular cases. Published research motivates selected cases. Actual mHealth calculations, imposed simulations, and synthetic teaching values are identified separately. No attached private style document or sample syllabus is reproduced here.

## Data, Code, and Numerical Checks

The [Lecture Examples](../03_Data_and_Code/Lecture_Examples/README.md) folder contains small synthetic CSV files, a data dictionary, and a Python script that reproduces the central numerical calculations. It covers all eight modules and uses only the standard library. It has been executed successfully; its output is saved as JSON.

The synthetic examples verify arithmetic and model implications under stated assumptions. Each module includes its executable Python calculation. The [recurring mHealth examples](../03_Data_and_Code/mHealth/recurring_examples/README.md) use actual released records for assessments, measurement, regression, segmentation, text prediction, experiment planning, basket prediction, and ranking objectives. Their full source appears directly in the notes, with matching scripts, dependencies, aggregate results, and verification checks.

M1 teaches structural checks, join coverage, repeated totals, and review flags. M2 adds nutrition-informed sample definitions and alternative screens, using the [nutrition methods collection](../01_Resources/12_Nutrition_and_Dietary_Data_Quality/README.md). The individualized Goldberg calculation is an explicitly hypothetical scenario because validated physiological inputs are absent from the logs. M3 compares an association before and after an imposed calorie-range restriction.

## Resources and Additional Worked Cases

The [resource integration map](RESOURCE_INTEGRATION.md) links the references to eight executed course programs. The notes add fixed-cohort business reviews (1.10), recency and frequency (2.13), price endogeneity and instruments (3.12), logging-gap survival (4.13), topic models and denominators (5.12), CUPED (6.15), basket association rules (7.17), and evidence checks for generated claims (8.11). Each case includes its full Python source, assumptions, results, and interpretation. Six additional figures explain the mechanisms and comparisons.

## Editing and Building

Edit [Preface.md](Preface.md), the Markdown files in `modules/`, and the TikZ files in `figures/`. The shared palette and figure styles are in [figures/style.tex](figures/style.tex). The colors follow the [official Illinois brand palette](https://brand.illinois.edu/visual-identity/color): Illini Blue `#13294B` and Illini Orange `#FF5F05`, with limited supporting colors. Labels, line styles, and symbols supplement color.

The [build script](build_notes.py) uses Pandoc to assemble the modules into [LaTeX source](Marketing_Analytics_Lecture_Notes.tex), substitutes the TikZ source for each Markdown figure, and compiles the PDF with Tectonic. It preserves first-paragraph indentation conventions and prefixes document anchors by module. Tectonic may download TeX packages on its first run.

From the repository root, with Python, Pandoc, and Tectonic available:

```sh
python3 06_Lecture_Notes/build_notes.py
```

To regenerate the PNG figure companions as well, install Pillow and make Poppler's `pdftoppm` available, then run:

```sh
python3 06_Lecture_Notes/build_notes.py --figures
```

To refresh selected previews, append `--figure-name M02_map_footprint` to the `--figures` command and repeat `--figure-name` for each changed figure. All lecture PDFs are still rebuilt.

Executable paths can be supplied with `--pandoc`, `--tectonic`, and `--pdftoppm`. Intermediate files go into the ignored `build/` folder. The generated `.tex` and PDF are committed so the notes can be read without installing a build environment. The compiled PDF uses the TikZ sources directly, not raster images.

After changes, run the relevant analyses and `python scripts/check_lecture_code.py` from the repository root, inspect compilation warnings, and visually inspect all affected pages and figure previews. Update navigation when adding a module or moving a source. Follow [AGENTS.md](AGENTS.md) for editing conventions and [the root agent guide](../AGENTS.md) for course authority and student support.

## Using the Notes with an LLM or Preparing Slides

Give an assistant the relevant Markdown module, its figure descriptions, and any related CSV or calculation output. Cite module and numbered section, such as “M6, Section 6.4.” Do not infer a deadline or assessment rule from an illustrative exercise. The exercises are public teaching material.

Follow the [preferred Beamer format](../05_Slides/AGENTS.md) when preparing lectures. Use each module's managerial question as the opening, then select the worked case, method, key figure, and decision implication. Keep the full derivation and consequential assumptions in the notes. Each TikZ file can be reused in a LaTeX slide deck; its PNG companion supports other presentation tools. Figures illustrate particular mechanisms and should retain the accompanying assumptions and synthetic-data labels.

## Data Visualization

M2, Sections 2.14–2.15, add chart selection, fixed and conditional denominators, empirical cumulative distributions, and an [interactive mHealth chart](../03_Data_and_Code/mHealth/recurring_examples/results/visualization_interactive.html). M3, Section 3.6.1, compares paired-user uncertainty with an incorrect independent-day calculation. M8, Section 8.12, assesses constructed chart errors. Three original TikZ figures and three complete Python programs support these additions. The [visualization guide](../03_Data_and_Code/mHealth/recurring_examples/results/VISUALIZATION.md) gives the commands, data definitions, and validation record.

## McDonald's Ice-Cream Availability

The [McBroken cases](../03_Data_and_Code/McBroken/README.md) connect a supplied restaurant-status panel to measurement and cleaning (M2 §2.16), comparison-group selection for a proposed policy evaluation (M6 §6.16), and forecasting with missing future labels (M7 §7.18). Five complete Python programs and three additional TikZ figures accompany the cases. The examples distinguish recorded order unavailability from verified mechanical failure, retain missing-date and missing-label counts, and evaluate predictions on later dates. The source assessment and five counterexample tests passed; two pinned upstream snapshots independently matched the supplied national totals.

## Generative-AI Demand

The [GenAI demand cases](../03_Data_and_Code/GenAI_Demand/README.md) add public-signal measurement (M2 §2.17), fixed-cohort subscription retention and acquisition events (M4 §4.14), and price-model verification (M8 §8.13). Each includes a complete executed Python program. Three Illinois-color TikZ figures have aggregate table and text companions. Eight counterexample tests cover duplicate and missing observations, cohort consistency, returns, acquisition categories, rank-deficient price designs, undefined log odds, and exact binary-model recovery. The public pageview capture and synthetic consumer panel are identified separately; the original reference notebook's structural interpretations are reviewed in the [adaptation record](../01_Resources/08_M8_Current_Topics_in_Marketing/genai_demand_lab/COURSE_ADAPTATION.md).

## Ethics, Regulation, and Session Decks

The [15 session decks](../05_Slides/README.md) cover the eight core modules and Marketing Dialectics with a 170-minute plan for each meeting. Ethics and regulation are integrated in M1 §1.11, M2 §2.18, M3 §3.13, M4 §4.15, M5 §5.13, M6 §6.17, M7 §7.19, and M8 §§8.14–8.15. The [primary-source guide](ETHICS_AND_REGULATION.md) records the legal scope and status checked on November 2, 2026.

The retention-procedure example separates firm profit, customer value, and combined surplus under stated fixed stakes. Its complete Python program generates the figure's aggregate table and independently checks expected monetary changes. The notes contain 122 matching Python source blocks.

## Earnings-Call Pricing Communication

The [earnings-call worked example](../03_Data_and_Code/Earnings_Calls/README.md) connects M2 §2.19, M5 §5.14, M6 §6.18, and M8 §8.16. Four complete Python programs reproduce coverage checks, call and word denominators, synthetic construct checks, and event-window comparisons. Three TikZ figures explain selection into a match-only sample, speaking exposure, and the difference between occurrence counts and call incidence. Nine counterexample tests passed. The public teaching data contain structured metadata and source-linked paraphrases.

## AI Workflow Evaluation and Economics

M1 §1.12 diagnoses code errors and missing information; M4 §4.16 examines buyer alternatives; M5 §5.15 preserves independent text evaluation. M6 §6.19 separates model and library contributions, M7 §7.20 calculates selection on development accuracy, and M8 §§8.17–8.18 connect reusable work, competitive pricing, and selective upgrades. The [three runnable programs](../03_Data_and_Code/AI_Workflows/README.md) appear in full, alongside four original TikZ figures and five exact small-case checks. All inputs are synthetic.

## Consumer Agency and Recent Marketing Research

The [journal collection](../01_Resources/13_Consumer_Agency_and_Recent_Research/README.md) links 886 DOI records to 103 retrieved versions, 144 original managerial summaries, and a complete access-gap ledger. M2 §2.20 assesses coverage, M4 §4.17 clusters mechanisms, and M5 §§5.16-5.17 examine coding and university affiliation communities. M6 §6.20, M7 §7.21, and M8 §8.19 connect experiments, recommendation welfare, and cancellation policy. Three complete Python programs and four new TikZ figures accompany the [analysis](../03_Data_and_Code/Consumer_Agency_Literature/README.md). Counts describe selected literature and do not estimate the prevalence of harmful business practices.

## Evidence Across Model Versions

M1 §1.13, M2 §2.21, M5 §5.18, M7 §7.22, and M8 §8.18.1 connect AI claims to the configuration and decision being evaluated. The [three complete Python programs](../03_Data_and_Code/LLM_Revalidation/README.md) reproduce source counts and follow-up summaries, compare changing judges, and preserve paired upgrade regressions. Three TikZ figures and the [related research guide](../01_Resources/14_LLM_Evidence_and_Revalidation/README.md) accompany the examples.

## Marketing Dialectics

[Chapter 9](modules/M09_Marketing_Dialectics.md) and its [standalone PDF](Marketing_Dialectics.pdf) develop critical evaluation of marketing claims and conduct. Kantian arguments are distinguished from Hume and Smith on scrutiny of private interests and from Confucian perspectives on righteousness, trustworthiness, roles, and cultivation. The chapter includes complete synthetic renewal and pricing programs, eight TikZ figures, and academic, industry, and regulatory cases. It is integrated into Session 14 without adding meetings. The notes builder also regenerates the standalone chapter.

The [categorized library](../01_Resources/15_Marketing_Dialectics/README.md) records 41 source entries, 35 downloaded files, and nine full-work access gaps. Source-record counts include different editions and reference entries. Copyright-restricted originals remain in Dropbox; the public guides preserve links and reading scope.

## AI Experimentation and Pricing

Marketing Dialectics, Sections 9.14–9.18, provides a detailed Kantian evaluation of four papers by Sanjog Misra and coauthors, their safeguards and welfare findings, and recent pricing-policy debates. M6 §6.21 and M8 §8.20 connect the case to experimentation and current methods. [Code and exact synthetic results](../03_Data_and_Code/AI_Experimentation_and_Pricing/README.md) accompany the complete Python source in the notes.

## Statistical Graphics and Marketing Decisions

M2 §2.22 explains customer pairing and covariance. M7 §7.23 compares identical rankings with different probability losses and purchase forecasts. Both contain full [runnable Python](../03_Data_and_Code/Statistical_Graphics/README.md), synthetic input definitions, and Illinois-color TikZ figures. [The PyStatlas guide](../01_Resources/17_PyStatlas_Statistical_Graphics/README.md) connects additional chart families to existing modules.

## Prediction Intervals and Customer-Service Routing

M7 §§7.24–7.25 derive split-conformal calibration and apply it to constructed store demand and complaint probabilities. Two TikZ figures explain segment coverage and ambiguous label sets. M8 §8.21 preserves the same stores under an imposed demand change. [Complete programs, records, and six independent checks](../03_Data_and_Code/Conformal_Prediction/README.md) distinguish marginal coverage, group outcomes, interval width, and singleton-routing error.

## Source Selection and Grader Evaluation

M1 §1.14 connects specifications and retained skills. M5 §§5.19–5.20 add a source-selection comparison, full-roster grader evaluation, two editable TikZ figures, and two complete Python programs. M7 §7.26 connects coverage and error costs. [The original data and verification](../03_Data_and_Code/AI_Evidence_and_Evaluation/README.md) and [practice lab](../07_Labs/AI_Evidence_and_Evaluation/README.md) distinguish stipulated examples from optional new model experiments.

## Clustering Optimization

M4 §§4.18–4.20 explain weighted cluster mass, final assignments, and a fixed-data comparison of Lloyd, MiniBatch, and CPU e-means. [Two full programs](../03_Data_and_Code/Clustering_Optimization/README.md), 27 saved fits, and five tests accompany two editable TikZ figures. M5 §5.3 connects the representation of text vectors; M7 §7.27 connects timing boundaries and independent evaluation. The [optional lab](../07_Labs/Clustering_Optimization/README.md) supports Session 6.

## Discount Response and Intervention Intensity

M6 §§6.22–6.27 provide a nonlinear discount case, five-fold adjustment, conditional-overlap diagnostics, 200-sample interval evaluation, randomized-store pooling, and continuous-DiD qualifications. M8 §8.22 supplies a complete objective calculation; M3 §3.14, M4 §4.21, and M9 §9.18.1 connect interpretation, group decisions, and customer judgment. [The programs](../03_Data_and_Code/Dose_Response/README.md), [source guide](../01_Resources/24_Dose_Response/README.md), and [optional lab](../07_Labs/Dose_Response/README.md) preserve assumptions and executable calculations.

## Spatial Networks and Retail Access

[Three runnable examples](../03_Data_and_Code/Retail_Accessibility/README.md) connect M2 §2.23, M4 §4.22, M5 §§5.21–5.22, M7 §7.28, M8 §8.23, and M9 §9.18.2. Four editable figures distinguish a map footprint from reachable nodes, straight distance from network access, known availability from missing-status bounds, and profit from access priorities. Full Python appears in the M2 and M5 notes. The [source review](../01_Resources/25_Spatial_Networks/README.md) records pinned city2graph references, while the executed programs use NetworkX.

## Anomaly Detection and Diagnosis

M7 §§7.29–7.30 distinguish an alert, variable localization, interpretation, and a response. [Two executed programs](../03_Data_and_Code/Anomaly_Diagnosis/README.md) preserve training/validation/test boundaries, missing records, and whole-run denominators. Two editable TikZ figures compare symptoms with an imposed cause and precise with broad intervals. The full Python appears in the notes; [optional practice](../07_Labs/Anomaly_Diagnosis/README.md) accompanies Session 11.

## Inference Efficiency and Customer Resolution

M7 §§7.31–7.32 connect speculative decoding to the time and cost of a useful response. [Two complete Python programs](../03_Data_and_Code/Inference_Efficiency/README.md) distinguish emitted tokens, target passes, response waits, generated answers, and correct customer resolutions. Two editable TikZ figures expose the boundary between target verification and task evaluation and the reversal between progress per pass and throughput. M1, M4, and M8 connect configuration versions, vocabulary clustering, and total service costs. Four Session 11 slides and [optional practice](../07_Labs/Inference_Efficiency/README.md) accompany the notes.

## Training Mixtures and Conditional Evaluation

M7 §§7.33–7.35 connect a two-feature ridge model to conditional customer-service evaluation and published checkpoint selection. [Three complete Python programs](../03_Data_and_Code/Training_Data_Mixtures/README.md) reproduce 261 synthetic ridge comparisons, 1,000 paired service requests, nine published epoch histories, and 51 published condition means. Ten independent checks and two editable TikZ figures accompany the examples. M2 §2.24, M3 §3.15, M8 §8.24, and M9 §9.18.3 connect source provenance, regression, supplier changes, and evidence for meaningful customer choice. Five Session 11 slides and [optional ungraded practice](../07_Labs/Training_Data_Mixtures/README.md) provide discussion and follow-up.

## Synthetic Consumers and Human Validation

M4 §4.23 and M5 §5.23 contain [two complete Python programs](../03_Data_and_Code/Synthetic_Consumers/README.md), ten independent checks, and two Illinois-color TikZ figures. The invented cases distinguish overall distribution fit from concept selection and show how anchors and repeat weighting change ratings. M7 §7.36 defines correlation attainment and concept-level validation; M8 §8.11 connects the screening workflow; M9 §9.18.4 examines consumer representation. The [source review](../01_Resources/29_Synthetic_Consumer_Research/README.md) preserves reported empirical results separately from these synthetic calculations.

## Reproducible Recommendations and Export

M1 §1.15 provides a complete Python program that recomputes four synthetic-consumer tables and writes a report with traceable evidence. An Illinois-color TikZ figure holds persona ratings fixed while varying identical repeat counts. M8 §8.25 connects numerical agreement to interpretation, file conversion, and public release. The [example and six checks](../03_Data_and_Code/Reproducible_Recommendations/README.md) accompany [optional ungraded practice](../07_Labs/Reproducible_Recommendations/README.md).

## Human and Synthetic Research Budgets

M4 §4.24 develops a four-profile product comparison, a common coefficient-accuracy target, and the allocation of primary and auxiliary responses. M7 §7.37 adds omitted-bias sensitivity and independent human validation. M3 §3.16 and M6 §6.28 explain identification and the information conditions supporting a fixed design. [Two complete programs and three editable figures](../03_Data_and_Code/Auxiliary_Data/README.md) accompany the notes and [optional ungraded practice](../07_Labs/Auxiliary_Data/README.md).

## Network Compression and Customer Access

M5 §5.24 develops exact aggregation and travel calculations. M7 §7.38 distinguishes oracle label purity, training-only prediction, and outcome-dependent preprocessing. [Two complete Python programs](../03_Data_and_Code/Graph_Coarsening/README.md), two editable figures, and [optional practice](../07_Labs/Graph_Coarsening/README.md) accompany shorter connections in M2 §2.23, M4 §4.22, and M9 §9.18.2.

## Definitions and Representation Quality

[Cancellation evidence](../03_Data_and_Code/Ontology_and_Evidence/README.md) connects M1 §1.16 and M2 §2.25 to event definitions, validation, unknown states, and a fixed reporting cutoff. [Representation evaluation](../03_Data_and_Code/Representation_Evaluation/README.md) connects M7 §§7.39–7.40 to variance-weighted reconstruction, review recall, and nonunique features. Three complete Python programs, fourteen independent tests, and three editable figures support the synthetic cases. M4 §4.25, M5 §5.25, and M9 §9.19 connect segment interpretation, attributed claims, and permission evidence. Sessions 1, 2, 11, and 14 include ten additional slides within the existing meeting times.

## Agent Workflow Evaluation

M1 §1.17 defines the fixed-roster mHealth task and provides complete reconstruction and reference code. M6 §6.29 defines the factorial interaction; M7 §7.41 evaluates outputs, actions, and the checker. M8 §8.26 calculates hypothetical total costs, and M9 §9.20 distinguishes company authority, customer authorization, and justification. [The example and verification](../03_Data_and_Code/Agent_Workflows/README.md) include eight independent tests and two original editable figures. No model experiment was executed.

## Representation Alignment and Observed Answers

M5 §5.26 and M7 §§7.42–7.44 connect text preparation, coordinate alignment, fixed-classifier compatibility, retraining, and answer evaluation. [Three original programs](../03_Data_and_Code/Representation_Alignment/README.md), nine tests, and two editable figures preserve synthetic and observed inputs separately. M8 §8.27 examines migration costs, and M9 §9.21 examines agreement and independent reasons. [Optional practice](../07_Labs/Representation_Alignment/README.md) accompanies Sessions 7, 11, and 14.

## Pricing Systems and Customer Choice

M4 §4.26 derives independent and joint prices under a common noisy demand signal, with complete executable Python. M8 §8.28 assesses the Wendy's complaint and source evidence; M9 §9.22 examines Kantian justification, Confucian trustworthiness, and customer alternatives. [The code, six policy rows, and nine checks](../03_Data_and_Code/Pricing_Competition/README.md), two TikZ figures, [source review](../01_Resources/37_Pricing_Systems_and_Competition/README.md), and [optional practice](../07_Labs/Pricing_Competition/README.md) preserve the distinction between actual sources and synthetic outcomes.

## Digital Usage and Customer Access

The [geographic case](../03_Data_and_Code/Digital_Usage/README.md) adds measurement and index verification in M2, conditional income projections in M3, scaling-sensitive clustering in M4, outcome validation in M7, and service choice in M8/M9. Five complete Python listings and four original TikZ figures accompany the public data and Census extracts.

## Statistical Inference and AI-Assisted Analysis

M1 §1.18, M3 §3.18, M6 §6.30, and M9 §9.24 connect statistical assessment, paired mHealth logging, store assignment, and advertising claims. [Two complete Python programs](../03_Data_and_Code/Statistical_Inference/README.md), ten independent tests, and two editable figures distinguish observed descriptive changes, synthetic null experiments, and ethical interpretation. The [source review](../01_Resources/39_Statistical_Inference_and_AI/README.md) and [optional practice](../07_Labs/Statistical_Inference/README.md) preserve the benchmark's scope.

## Coding Workflows and Independent Checks

M1 §1.19 reconstructs published success and failure counts; M6 §6.31 compares prompt effects on two scales; M7 §7.46 evaluates constructed mHealth errors; M8 §8.30 compares review costs and undetected decision losses. M3 and M9 connect statistical evidence and managerial responsibility. [Complete Python and outputs](../03_Data_and_Code/Agent_Workflows/README.md) accompany two editable figures.

## Statistical Claims and the Ethics of Public Reassurance

The [resource and claim assessment](../01_Resources/41_Statistical_Claims_and_Decisions/README.md) connects Lakens’s inference guidance with the data-center electricity paper. M2 §2.28 distinguishes average prices, household incidence, and ownership categories. M3 §3.19 simulates repeated p-values; M6 §§6.32–6.33 compare detection with profit and reconstruct power, bounds, subgroup tests, sales mechanisms, and residual arithmetic. M8 §8.31 evaluates public communication. M9 §§9.25–9.26 develop equivalence, ontology, reasons, authority, Kantian duties, and Confucian trustworthiness. Four full Python listings and five editable Illinois-color figures accompany the notes. Sessions 4, 9, and 14 add eleven slides within existing allocations. The case distinguishes verified academic coverage from unverified company dissemination, demonstrated interpretation problems from replication questions, and possible harm from established consequences.

## Logical Assessment and Inverse Power

M6 §6.34 develops Donald W. K. Andrews's inverse-power approach with specified alternatives, nuisance parameters, and directional sensitivity. M9 §9.27 reconstructs the electricity arguments through premises, counterexamples, measurement, extrapolation, and household authority. The [argument record](../01_Resources/41_Statistical_Claims_and_Decisions/ARGUMENT_ASSESSMENT.md) links claims to evidence and repairs. Two complete Python examples and two editable TikZ figures support the discussion. Sessions 9 and 14 use selected examples within existing meeting allocations; extended calculations remain optional ungraded practice.

## Institutions and the Empirical Comparison

M2 §2.28.1 develops the price/bill accounting distinction. M6 §6.35 provides complete Python, four synthetic tables, and a TikZ diagram for project exposure, donor costs, and conditional recovery. M9 §9.27.6 identifies the institutional premises required by broader claims. The case preserves the paper's regulatory discussion while assessing the scope of its operational treatment and outcome definitions.

## Reasons, Stakeholders, and Public Voice

M9 §§9.28–9.32 develops publication responsibility, Scanlonian justification, stakeholder duties, pricing communication, and residents' voice. Two editable TikZ figures distinguish factual and normative premises and compare reasons for rejecting alternative principles. M1 and M8 connect these arguments to managerial recommendations and public claims.

M5 §5.27 adds qualitative analysis of utility disclosures, three boxed verbatim call excerpts, a cost-recovery diagram, and two complete Python programs. M6 §6.36 and M9 §9.33 connect that evidence to causal interpretation and stakeholder reasons. [Methods references](../01_Resources/42_Qualitative_Evidence/README.md) and [optional practice](../07_Labs/Qualitative_Evidence/README.md) accompany the case.

## Pricing, Individual Reasons, and Antitrust Evidence

M4 §4.28, M6 §6.37, M8 §8.32, and M9 §§9.34–9.39 connect flexible demand models to welfare identification, experimental exposure, Kantian authority, Scanlonian justification, and U.S. antitrust proof. Five [executed programs](../03_Data_and_Code/AI_Experimentation_and_Pricing/README.md) reproduce exact synthetic comparisons and Dubé and coauthors' rounded competitive payoff table. Four editable TikZ figures explain the mechanisms. The [source assessment](../01_Resources/16_AI_Experimentation_and_Pricing/SCANLON_ASSESSMENT.md) and [legal guide](../01_Resources/16_AI_Experimentation_and_Pricing/ANTITRUST_AND_REASONS.md) preserve contrary findings, primary citations, and document status. Fourteen new checks pass; all 122 Python blocks match their standalone files. Students distinguish an instrumentally rational choice from a reasonable principle. They assess measurement quality alongside the worth of the goal, then compare personalized pricing, dynamic-pricing communication, and data-center reassurance.

## Analytical Arguments

M1 §1.20 introduces a five-step method for examining an analytical recommendation. M4 §4.29 holds purchases and product rankings fixed while comparing cardinal values; M6 §6.38 constructs equal historical fit with different common-price effects; M9 §9.40 connects the examples to logical validity, premise support, interpretation, and Scanlonian justification. [Two complete programs and results](../03_Data_and_Code/Analytical_Arguments/README.md), three editable figures, and [optional practice](../07_Labs/Philosophical_Arguments/README.md) support the pricing and electricity applications. Both calculations executed, ten independent checks passed, and all 122 Python listings match their standalone files.

M1 and [M9 §9.41](../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md) place the worth of the objective, Kant's phenomena–noumena distinction, and the practical standing of affected people before optimization. Sessions 1 and 14 connect the limits of empirical representation to separate arguments about ends, authority, and obligations. A fourth editable diagram distinguishes further empirical inquiry from Kant's limiting concept and practical justification.

[M9 §§9.41–9.43](../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md) distinguish acknowledged epistemic limits from unknown unknowns and assess interpretations through an ontological spectrum. Electricity reassurance, personalized pricing, and cancellation connect to Kant, Sellars, Bhaskar, Husserl, and Scanlon. Publication selection toward tractable questions remains a hypothesis separate from verified evidence of selection by result strength. Session 14 uses selected cases within its existing discussion blocks; the extended comparisons are optional practice.

## Explanation and Learning Evaluation

M1 §1.21, M2 §2.29, M6 §6.39, and M9 §9.44 connect source fidelity, bill measurement, percentage denominators, feature effects, and learner authority. [Two complete programs](../03_Data_and_Code/Learning_Design/README.md) and two editable TikZ figures accompany an [HTML pilot](../08_Wiki/pilot/README.md) and [optional practice](../07_Labs/AI_Augmented_Learning/README.md). The [source review](../01_Resources/43_AI_Augmented_Learning/README.md) separates the reported learning experiment from original synthetic calculations.

## Conflicts of Interest and Consumer Control

M9 §§9.45–9.49 examines responsibilities, disclosure, dependence, engagement evidence, and reasons for honoring stopping instructions. M1 §1.22, M7 §7.47, and M8 §8.33 carry the issue into question formulation, prediction, and integrated decisions. The [original comparison](../03_Data_and_Code/Conflicts_of_Interest/README.md) includes full matching Python and independent calculations; the [source guide](../01_Resources/15_Marketing_Dialectics/09_Conflicts_of_Interest/README.md) records what was reviewed. Two editable figures show conflicting pressures on judgment and the premises of an ought conclusion.

## Bad Controls and Thoughtful Research Design

M3 §§3.20–3.21, M6 §§6.40–6.42, and M9 §9.50 distinguish adjustment bias, exposed donors, anticipation, and selected populations. Three complete Python programs and four Illinois-color TikZ figures accompany the [readings](../01_Resources/44_Bad_Controls_and_Project_Exposure/README.md) and [optional practice](../07_Labs/Bad_Controls/README.md).

## Data, Truth, and Institutional Responsibility

M2 §§2.30–2.31, M6 §6.43, and M9 §§9.51–9.54 distinguish data artifacts, evidence, truth claims, and permissible action. Three TikZ diagrams and one complete Python program connect selective access to the data-center case. The [reading collection](../01_Resources/45_Data_Truth_and_Norms/README.md) and [evidence assessment](../01_Resources/45_Data_Truth_and_Norms/ELECTRICITY_ASSESSMENT.md) document existing household expenditure data and the more demanding project-level causal question.
