# Data and Sample Code

Course datasets, data dictionaries, scripts, notebook examples, and code snippets for Marketing Analytics. Keep each example's data and code together in a subfolder organized by module or topic.

**Status:** [synthetic lecture examples](Lecture_Examples/README.md) now cover the numerical cases in all eight modules, with verified Python calculations and small CSV files. Candidate datasets are in the [resource library's dataset guide](../01_Resources/10_Datasets_and_Project_Resources/Dataset_Guide/README.md) and [additional dataset collection](../01_Resources/20_Datasets/README.md).

The [mHealth food-log collection](mHealth/README.md) provides actual 2016 food entries and daily summaries with replacement user IDs, fixed ages, and perturbed weights. Its GitHub release contains the full compressed teaching files. The data dictionary, checksum-verified downloader, and agent guide are in the course folder. Read the transformation and sampling notes before analysis.

## Adding an Example

Use a descriptive module prefix, such as `M02_Customer_Summary`, and include a README explaining the marketing question, files, dependencies, run command, expected output, and a simple check of the result. Record whether the example has been executed successfully.

Place the related scripts or notebooks, data files, and data dictionary in the example's folder. Use relative data paths. For larger examples, use `data/` and `code/` subfolders. If several examples share a dataset, link to a single documented copy.

## Documenting Data

Record the source, retrieval date/version, license, observation unit, time range, units, missing-value codes, exclusions, and processing steps. Preserve original and derived data separately. Label synthetic data explicitly, and retain attribution and licenses for adapted data and code.

Keep identifiable student records and restricted research data outside this repository.

## Guidance for Students and Agents

Read the root [agent guide](../AGENTS.md) before adapting an example. Explain the purpose of the code and its analytical assumptions, inspect the inputs and data dictionary, and verify the output with a small example. Identify any changes made with AI assistance. Follow the relevant assignment's rules when using sample code in assessed work.

The [labs folder](../07_Labs/README.md) contains the structure for complete guided exercises. The [resource library](../01_Resources/README.md) contains downloaded reference code and notebooks.

## Recurring mHealth Cases

The [eight-module examples](mHealth/recurring_examples/README.md) include complete Python, aggregate outputs, a data-quality assessment, nutrition-screening sensitivity, and meaningful counterexample checks. The same code is embedded in the lecture notes.

Additional executed examples cover fixed-cohort reporting, recency/frequency, logging-gap survival, text topics, CUPED, basket associations, and checks on generated numerical claims. A separate synthetic price-instrument simulation illustrates endogeneity and exclusion. See the [resource-to-example map](../06_Lecture_Notes/RESOURCE_INTEGRATION.md) for source attribution, module sections, and the distinction between executed course code and downloaded reference notebooks.

## McDonald's Ice-Cream Availability

The [McBroken examples](McBroken/README.md) use the supplied restaurant-status data for measurement and cleaning in M2, comparison-group selection in M6, and forecasts on later dates in M7. Five executed Python programs, aggregate teaching tables, source hashes, and counterexample tests support the cases. The outcome is recorded order unavailability; the examples keep missing observations, irregular time gaps, address-key changes, and causal interpretation explicit.

## Generative-AI Demand

The [GenAI demand cases](GenAI_Demand/README.md) cover public-signal measurement in M2, subscription retention and acquisition in M4, and price-model verification in M8. Three executed Python programs use the supplied public pageview capture and a separate synthetic subscription panel. Fixed-cohort comparisons, missing-date checks, event definitions, and an exact binary-logit benchmark support the interpretation. Eight counterexample tests, full Python in the notes, three Illinois-color TikZ figures, and source hashes accompany the cases.

## Earnings-Call Pricing Communication

The [earnings-call case](Earnings_Calls/README.md) uses supplied structured metadata for missing-text assessment in M2, text measurement and interpretation in M5, descriptive event comparisons in M6, and pricing evidence in M8. Four complete Python programs, nine counterexample tests, source hashes, and three TikZ figures support the case. Seven source-linked paraphrases distinguish price displays, business advertising, intentions, infrastructure, and claims about pricing use. Full transcript excerpts remain in the original local bundle.

## AI Workflow Evaluation and Economics

The [AI workflow examples](AI_Workflows/README.md) compare model and library contributions, repeated selection on development accuracy, reusable-code costs, and buyer/seller price bounds. Three executed programs use only Python's standard library and synthetic inputs. Complete code appears in M6 §6.19, M7 §7.20, and M8 §8.17, with connections in M1, M4, and M5. Five small-case checks and four TikZ figures accompany the calculations. The examples require no model account and establish no provider performance, observed labor savings, or customer demand.

## Consumer Agency Literature and University Affiliations

The [journal-review example](Consumer_Agency_Literature/README.md) includes 144 original managerial summaries and mechanism codes, a DOI census, access-gap assessment, reproducible Jaccard clustering, and sensitivity checks. The [affiliation analysis](Consumer_Agency_Literature/AFFILIATIONS.md) groups universities through shared publications and compares fractional research profiles. The inputs are actual bibliographic metadata and preliminary review annotations. Full code appears in M2 §2.20, M4 §4.17, and M5 §5.17; causal and policy interpretations appear in M6 §6.20, M7 §7.21, and M8 §8.19.

## LLM Revalidation

[LLM Revalidation](LLM_Revalidation/README.md) contains a licensed fifty-claim research snapshot, independent descriptive calculations, and constructed comparisons of model upgrades and judge changes. Three standard-library programs, complete case-level outputs, a data dictionary, and four small-case tests accompany the full code in the notes.

## Marketing Dialectics

[Renewal and Customer Intent](Marketing_Dialectics/README.md) constructs two populations with the same billing rate and different unwanted-renewal shares. The standard-library program preserves population denominators and unknown intent. Complete code appears in Chapter 9; the comparison is synthetic and descriptive.

## AI Experimentation and Pricing

[Exact synthetic pricing comparisons](AI_Experimentation_and_Pricing/README.md) distinguish profit, aggregate surplus, and customer incidence. A separate calculation checks rounded published means, with source and version records.

## Statistical Graphics

[Paired customer changes and ranking versus calibration](Statistical_Graphics/README.md) use two original synthetic datasets, complete Python, aggregate tables, and six small-case tests. M2 §2.22 and M7 §7.23 reproduce the programs in full.

## Conformal Prediction

[Demand intervals and complaint-label sets](Conformal_Prediction/README.md) use fixed synthetic records, a shared finite-sample rank function, and complete standard-library Python. Six checks verify boundary ranks, ties, segment denominators, paired demand changes, and sets. Full code appears in M7 §§7.24–7.25, with demand-shift interpretation in M8 §8.21.

## AI Evidence and Evaluation

[Source selection and grader evaluation](AI_Evidence_and_Evaluation/README.md) use original fictional excerpts, stipulated answers, and disclosed reference judgments. Two complete programs and six independent checks preserve paired questions and full scoring denominators. No model performance is measured. M5 §§5.19–5.20 contain the full source.

## Clustering Optimization

[Clustering optimization](Clustering_Optimization/README.md) supplies exact scalar calculations and 27 CPU fits on fixed synthetic vectors. Complete Python, pinned requirements, final centroid arrays, label vectors, aggregate outputs, and five tests support M4 §§4.18–4.20. No o-means or GPU benchmark was executed.

## Dose-Response Curves

[Discount-response examples](Dose_Response/README.md) provide three complete synthetic programs: cross-fitted adjustment with 200 repeated-sample evaluations, randomized-store partial pooling, and a known-function comparison of objectives. Seven numerical tests, saved arrays, a data dictionary, and an agent guide accompany M6 §§6.22–6.27 and M8 §8.22.

## Retail Accessibility

[Retail accessibility](Retail_Accessibility/README.md) provides three complete programs, synthetic and observed inputs, eight independent tests, result hashes, and four editable figures. The observed case uses four restaurant records and a frozen OpenStreetMap extract; the synthetic case supplies population weights and service objectives. Full Python appears in M2 §2.23 and M5 §§5.21–5.22. [Optional practice](../07_Labs/Retail_Accessibility/README.md) extends the comparison.

## Anomaly Detection and Diagnosis

[The retail monitoring example](Anomaly_Diagnosis/README.md) supplies 4,320 synthetic store-minutes, training and validation references, two detection rules, incident timing, variable rankings, and evidence packets. A separate exact comparison examines permissive interval scoring and future-information leakage. Two full programs and eight independent checks support M7 §§7.29–7.30. No upstream benchmark or LLM was executed.

## Inference Efficiency and Customer Service

[Two original programs](Inference_Efficiency/README.md) compare progress per verification pass with total throughput and distinguish reference-token agreement, generated answers, and correct automatic resolutions. Twelve requests per decoding split and twelve paired service requests are synthetic. Nine independent checks cover termination, costs, selection, and failures. Complete Python is printed in M7 §§7.31–7.32.

## Training Mixtures and Conditional Service Outcomes

[Training Data Mixtures](Training_Data_Mixtures/README.md) contains three executed standard-library programs. They solve a two-feature ridge model, construct 1,000 paired synthetic service requests, and recompute selected published checkpoint and prompt-condition results. Ten checks verify independent calculations, source hashes, pairing, missing-response denominators, and resumed epoch logs. Full Python appears in M7 §§7.33–7.35; the dictionary and agent guide identify the distinct evidence supplied by each program.

## Synthetic Consumer Research

[Synthetic Consumers](Synthetic_Consumers/README.md) provides two executed standard-library programs, fixed invented inputs, ten independent checks, and two editable TikZ figures. The measurement example preserves responses, repeats, and persona weights; the screening example separates distribution fit, ranking, and shortlist errors. Full Python appears in M4 §4.23 and M5 §5.23, with input definitions and source attribution.

## Reproducible Recommendations

[Reproducible Product Recommendations](Reproducible_Recommendations/README.md) recomputes the synthetic-consumer tables, compares persona and response weights, and generates a report linked to its numerical evidence. Six independent checks cover reference arithmetic, missing values, stale tables, and execution after a folder move. The [optional lab](../07_Labs/Reproducible_Recommendations/README.md) separates interpretation and export checks from calculation.

## Auxiliary Data and Research Budgets

[Human and Synthetic Evidence](Auxiliary_Data/README.md) contains two executed standard-library programs, four invented product profiles, analytic precision and bias calculations, and six independent checks. Three editable figures distinguish preserved feature contrasts, conditional cost savings, and persistent coefficient bias. Full Python appears in M4 §4.24 and M7 §7.37, with definitions and a separate source review.

## Graph Coarsening

[Two standard-library programs](Graph_Coarsening/README.md) reproduce a four-zone revenue/access comparison and separate label-evaluation examples. Synthetic inputs, definitions, saved JSON/CSV outputs, provenance, and nine independent checks accompany complete Python in M5 §5.24 and M7 §7.38.

## Definitions and Representation Quality

[Cancellation evidence](../03_Data_and_Code/Ontology_and_Evidence/README.md) connects M1 §1.16 and M2 §2.25 to event definitions, validation, unknown states, and a fixed reporting cutoff. [Representation evaluation](../03_Data_and_Code/Representation_Evaluation/README.md) connects M7 §§7.39–7.40 to variance-weighted reconstruction, review recall, and nonunique features. Three complete Python programs, fourteen independent tests, and three editable figures support the synthetic cases. M4 §4.25, M5 §5.25, and M9 §9.19 connect segment interpretation, attributed claims, and permission evidence. Sessions 1, 2, 11, and 14 include ten additional slides within the existing meeting times.

## Agent Workflow Evaluation

[The workflow package](Agent_Workflows/README.md) provides compact mHealth task inputs, source reconstruction, reference calculation, a CSV grader, eight independent tests, and a hypothetical cost comparison. The information-by-feedback protocol supplies no measured model-performance results.

## Representation Alignment

[Changing text representations in mHealth](Representation_Alignment/README.md) includes a 9,000-description input, a source reconstruction program, a synthetic rotation, and a local word-versus-character comparison. Complete Python appears in M5 and M7. Nine independent tests, saved predictions, and category-specific denominators support the calculations; no model API is used.

## Pricing Systems and Customer Choice

[Pricing Competition](Pricing_Competition/README.md) contains a synthetic two-restaurant market, exact rational calculations, cell and policy tables, an editable welfare figure, and nine independent checks. The program varies demand information and pricing objectives separately. Full code appears in M4 §4.26; M8 and M9 connect the calculation to the Wendy's case and ethical reasoning.

## Digital Usage and Customer Access

[Digital Usage](Digital_Usage/README.md) contains 28,561 published geographic records, compact public Census extracts, five complete teaching programs, eleven independent checks, and four editable figures. The examples assess identifiers and income boundaries, compare adjusted projections, and evaluate clustering sensitivity. Original device microdata and analysis code are unavailable.

## Statistical Inference

[Two original programs](Statistical_Inference/README.md) reproduce paired mHealth logging and measure false-positive rates in a synthetic store-randomized experiment. Complete code appears in M3 §3.18 and M6 §6.30. Ten independent checks and two editable figures accompany the results; no model endpoint is used.

## Coding Workflows and Hidden Errors

[Agent workflow examples](Agent_Workflows/README.md) now include published aggregate reconstruction, eight constructed coding cases on each mHealth task, and a hypothetical decision-loss comparison. Three complete Python programs and two TikZ figures connect M1, M3, M6, M7, and M8; no new model calls are included.
