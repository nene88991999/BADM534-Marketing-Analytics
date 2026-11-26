# Marketing Analytics Resource Library

Collected October 23, 2026 for Nathan Yang's planned version of **Marketing Analytics**. The collection follows Unnati Narang's eight-module Spring 2026 syllabus and adds resources for AI-assisted coding throughout the course. The Spring 2027 syllabus is available; wiki design and implementation remain pending.

## Start Here

The initial collection contained **117 annotated resources across 12 topic folders**, **14 PDFs**, **24 source notebooks**, **5 UCI dataset archives with extracted files**, and companion data, Python functions, and licenses. The 84 downloaded source files occupy approximately 82.5 MB before archive extraction. Web resources also have Finder bookmarks in each folder's `Links` directory.

1. Read the [Syllabus Coverage and Teaching Priorities](00_Course_Map_and_Teaching/Planning_Notes/README.md).
2. Review the [AI Coding and Assessment Notes](09_AI_Assisted_Coding/Teaching_Notes/README.md).
3. Choose starting data from the [Dataset Guide](10_Datasets_and_Project_Resources/Dataset_Guide/README.md).
4. Use the topic guides below to select short readings and source examples.
5. Consult the [Hosting and Interactivity Notes](11_GitHub_HTML_and_Interactive_Teaching/Design_Notes/README.md) when beginning wiki design.

## Topic Folders

| Folder | Coverage | Resources |
| --- | --- | ---: |
| [Course Map and Teaching](00_Course_Map_and_Teaching/README.md) | Across modules | 6 |
| [Python, Data, and Reproducibility](01_Python_Data_and_Reproducibility/README.md) | M1 | 10 |
| [Customer Data and Visualization](02_Customer_Data_and_Visualization/README.md) | M2 | 8 |
| [Regression and Statistical Foundations](03_Regression_and_Statistical_Foundations/README.md) | M3 | 7 |
| [Conjoint, Segmentation, and Customer Lifetime Value](04_Conjoint_Segmentation_and_CLV/README.md) | M4 | 12 |
| [Text, Social Media, and Network Analysis](05_Text_Social_and_Network_Analysis/README.md) | M5 | 9 |
| [Causal Inference and Experiments](06_Causal_Inference_and_Experiments/README.md) | M6 | 9 |
| [Prediction and Machine Learning](07_Prediction_and_Machine_Learning/README.md) | M7 | 10 |
| [Current Topics in Marketing](08_Current_Topics_in_Marketing/README.md) | M8 | 9 |
| [AI-Assisted Coding](09_AI_Assisted_Coding/README.md) | Across modules | 18 |
| [Datasets and Project Resources](10_Datasets_and_Project_Resources/README.md) | Across modules | 9 |
| [GitHub, HTML, and Interactive Teaching](11_GitHub_HTML_and_Interactive_Teaching/README.md) | Across modules | 10 |

## A Focused Starting Set

A manageable starting set is the Python marketing research notebooks (P10), pandas tutorials (P03), Wilke's visualization book (V01), ISLP and its labs (R01-R02), Sawtooth's conjoint readings (C01/C12), the segmentation book (C04), PyMC-Marketing CLV (C07), scikit-learn text features (X02), Facure's causal handbook (E01), the experimental-design paper (E06), scikit-learn pitfalls and evaluation (M02/M04), and one coding-assistant guide (AI01, AI03, or AI04). Use the seven coding studies AI09-AI14 and AI17 primarily for instructor preparation.

The eight modules already cover a substantial semester. Treat advanced Bayesian estimation, uplift, embeddings, recommendations, and full marketing mix modeling as alternatives for extensions or projects. Python remains the default; R sources provide conceptual or instructor references.

## How the Collection Was Selected

The search combined the syllabus topics with marketing decisions, teaching materials, datasets, Python implementations, AI coding practices, and static HTML execution. Sources favor authors, publishers, university projects, official package documentation, and original research. Text, notebooks, and exercises are preferred; videos are not required. An author repository is counted once even when multiple companion files are saved. A book and its separate code repository can have distinct records because they have different uses and licenses.

This is a broad curated foundation, not an exhaustive inventory of everything online. Each entry records the source, teaching use, priority, cautions, access/reuse notes, and available local files. General search results, unverified mirrors, bulk review dumps, and commercial registrations were not copied into the library.

## Verification and Access

All 117 source URLs were checked. 115 returned successful responses. Two useful reference leads have incomplete direct access: T06 (DecisionPro, HTTP 403) and D05 (GroupLens, timeout); both were found through official indexed pages. They are marked in their guides and are not required for the core collection. Successful retrieval confirms availability at collection time, not permanent access or technical suitability.

Downloaded PDFs were parsed; ZIP archives passed CRC checks; notebooks were checked as notebook JSON; file hashes and exact source URLs are recorded. Selected GitHub files use commit-pinned download URLs. **Source notebooks have not been executed or converted into assignments.** Their dependencies, remote assets, outputs, and data-loading paths require adaptation and execution checks during lesson development.

## Public Wiki Reuse

Keep the instructor resource library separate from the eventual public site. Publicly readable material does not automatically permit copying to GitHub. In particular, the Python for Data Analysis web text restricts copying, Train's electronic book restricts use to personal research and study, and the Kohavi paper explicitly prohibits redistribution. Link to those sources. Retain license notices for repository code and cite datasets. Open-license materials still require attribution and attention to third-party exceptions.

The historical syllabus remains an internal instructor reference in Dropbox and is excluded from Git publication. Its topic coverage and the differences between its two AI-use passages are summarized in the course map.

## Additional Material in the Shared Folder

A [separate index](00_Index/README.md) and additional module folders appeared during collection. They are preserved and have not been merged into this catalog. The counts and verification results above refer to the 117 entries in `RESOURCE_CATALOG.json` and the 12 linked topic folders.

## Files for Maintenance

[RESOURCE_CATALOG.json](RESOURCE_CATALOG.json) is the portable structured catalog for later filtering or import into the wiki. [_maintenance/README.md](_maintenance/README.md) explains source provenance, download and extraction manifests, link checks, and how to rebuild these guides. Review live AI documentation and package behavior again before the teaching term.

## Nutrition and Dietary Data Quality

The [nutrition methods collection](12_Nutrition_and_Dietary_Data_Quality/README.md) adds 14 cataloged sources on food records, usual intake, outliers, energy adjustment, reporting plausibility, and documented dietary reliability. Eleven government resources and two methods PDFs were downloaded. The copyrighted Black PDF remains in the instructor Dropbox folder; the public collection contains its summary and source links. The original Goldberg paper is linked from its abstract. These resources support the mHealth assessment and screening examples in M1–M3.

## Marketing Dialectics

[The categorized collection](15_Marketing_Dialectics/README.md) contains Kantian primary texts and scholarship, marketing ethics and evidence, industry cases, Hume and Smith on self-interest, and Confucian readings. The catalog identifies 41 source records, 35 downloaded files, versions, rights, reading scope, and nine full-work access gaps.

## AI Experimentation and Pricing

[Research and primary policy sources](16_AI_Experimentation_and_Pricing/README.md) support a Kantian case on AI-assisted A/B testing, personalized prices, commercial objectives, and customer consequences.

## PyStatlas Statistical Graphics

[A catalog of 61 examples and a module-specific guide](17_PyStatlas_Statistical_Graphics/README.md) support chart selection, interpretation, AI-assisted coding, and future static-wiki design. The source record distinguishes nine full script readings from metadata cataloguing.

## Conformal Prediction

[A focused guide and versioned notebook catalog](18_Conformal_Prediction/README.md) support demand intervals, segment coverage, complaint-label sets, and temporal revalidation. The course adaptations use original synthetic records and verified standard-library Python.

## AI Practice and Evaluation

[Selected Stanford CS193T activities](19_AI_Practice_and_Evaluation/README.md) motivate original exercises on source selection, evaluator reliability, and independent verification. The source record links public materials without republishing them. Full course Python, synthetic cases, and a practice lab accompany the notes.

## Clustering Optimization

[The clustering collection](23_Clustering_Optimization/README.md) preserves the e-means paper, pinned implementation documentation and licenses, o-means benchmark scope, and a catalog of six primary resources. Original executed CPU examples support the M4 extension; GPU methods remain advanced reading.

## Dose-Response Curves

[The dose-response collection](24_Dose_Response/README.md) links eight methodological and implementation resources, including nonlinear DML, doubly robust curves, hierarchical standardization, and continuous-DiD assumptions. The pinned MIT documentation preserves attribution; original executed course programs supply the examples.

## Spatial Networks and Retail Access

[The spatial-network collection](25_Spatial_Networks/README.md) records the city2graph review, pinned reference files, source licenses, and connections to retail access. [Original executed course programs](../03_Data_and_Code/Retail_Accessibility/README.md) separate graph reachability, map footprints, recorded restaurant availability, and customer behavior. The collection has its own `spatial-networks` catalog namespace.

## Anomaly Detection and Marketing Diagnosis

[The SHAD collection](26_Anomaly_Detection_and_Diagnosis/README.md) separates detecting an unusual pattern, locating implicated variables, interpreting an event, and choosing a response. It preserves the paper and selected repository files, with a source review covering timing, missingness, labels, and evaluation rules. Proposed retail, restaurant-availability, and mHealth applications connect to M2, M5, M7, M8, and M9. M7 §§7.29–7.30 now include [original executed Python and synthetic cases](../03_Data_and_Code/Anomaly_Diagnosis/README.md), with optional ungraded practice. Other module connections remain suggestions. The collection uses the `anomaly-diagnosis` catalog namespace.

## AI Inference Efficiency

[AI inference efficiency](27_AI_Inference_Efficiency/README.md) connects multi-token prediction to computational cost, component compatibility, and the unit of evaluation. The collection preserves the paper and nine pinned repository files, with a detailed source review and the implemented M7 §§7.31–7.32 comparison. The resource catalog uses the `inference-efficiency` namespace; model training and inference were not executed.

## Training Data Mixtures and Conditional Behavior

[The training-data collection](28_Training_Data_Mixtures/README.md) connects interactions between data sources to confounded features, regularization, conditional model evaluation, and evaluator validity. It preserves the paper and selected pinned repository files, with independently recomputed published aggregates. M7 §§7.33–7.35 contain [three executed course programs](../03_Data_and_Code/Training_Data_Mixtures/README.md), two TikZ figures, and a Session 11 comparison linked to M2, M3, M8, and M9. The collection uses the `training-data-mixtures` catalog namespace. No upstream model training or inference was executed.

## Synthetic Consumer Research

[The paper and pinned implementation review](29_Synthetic_Consumer_Research/README.md) connect product concept screening in M4 to text measurement in M5 and validation in M7. The guide distinguishes correlation attainment, response-distribution fit, and human purchasing outcomes, with six source-review arithmetic checks, two implemented course programs, ten independent course checks, and optional ungraded practice.

## Research Writing and AI-Assisted Coding

[The Suzuri review](30_Research_Writing_and_Coding/README.md) connects readable project files, source evidence, executable code, and independent checks. Nine pinned reference files support the assessment of export behavior, citation attachments, typesetting, and opt-in GitHub synchronization. An optional M1/M8 exercise and future wiki practices are proposed; no editor installation or new course requirement is introduced.

## Auxiliary Data and Bias Geometry

[The auxiliary-data collection](31_Auxiliary_Data_and_Bias_Geometry/README.md) connects M4 §4.24 research budgets to M7 §7.37 omitted-bias evaluation, with links in M3 and M6. Two complete programs, six independent checks, three TikZ figures, and optional ungraded practice separate feature comparisons from price bias and calculate cost at a common accuracy target. The paper's 74% and 32% savings remain attributed retrospective model calculations. The collection uses the `auxiliary-bias` catalog namespace.

## Graph Coarsening

[The GraCo review](32_Graph_Coarsening/README.md) examines network compression, aggregation weights, metric-dependent rankings, population restrictions, and label use. The collection preserves the CC BY paper and 21 pinned source files with their licenses, plus seven original arithmetic checks. [The implemented M5/M7 case](../03_Data_and_Code/Graph_Coarsening/README.md) adds two executed programs, nine independent checks, and optional practice. The source toolkit and GNN training remain unexecuted. The catalog namespace is `graph-coarsening`.

## Ontologies and Knowledge Representation

[The ontology review](33_Ontologies_and_Knowledge_Representation/README.md) connects explicit definitions and reasoning traces to data contracts, missing observations, attributed claims, and customer permissions. The implemented cancellation-record exercise appears in M1 §1.16 and M2 §2.25, with M5 §5.25 and M9 §9.19 connections, complete Python, and optional practice. The hosted revenue-definition case was checked; unlicensed application source is linked rather than copied. The catalog namespace is `ontology-representation`.

## Representation Evaluation

[The sparse-autoencoder review](34_Representation_Evaluation/README.md) connects aggregate reconstruction, feature stability, and decision-specific evaluation to M7, with M2/M4/M5/M9 applications. Thirteen licensed source files and saved-result tables accompany eight original source-review checks. The implemented M7 §§7.39–7.40 examples add two complete programs, six independent tests, and optional practice. Source models remain unexecuted. The catalog namespace is `representation-evaluation`.

## Agent Workflow Evaluation

[The survey and source review](35_Agent_Workflow_Evaluation/README.md) connect execution environments, context, tools, checks, and authority to an original mHealth coding exercise. The licensed paper is archived with attribution and a pinned source hash. The companion catalog is linked; no upstream code was executed.

## Representation Alignment

[Representation alignment](36_Representation_Alignment/README.md) connects Plato's Key and related research to original coordinate calculations and an executed mHealth text-classification comparison. The guide records source scope, rights, and the separation between internal neural states and locally fitted lexical features.

## Pricing Systems and Customer Choice

[The pricing-systems library](37_Pricing_Systems_and_Competition/README.md) contains six source records linking the Wendy's complaint, reporting, company statements, pricing research, and an agency argument. The source review preserves dates, jurisdiction, claim scope, and access limits. Three PDF reference copies remain in Dropbox only. Original course annotations, the synthetic model, and public links accompany M4, M8, and M9.

## Digital Usage and Inclusion

The [digital-usage library](38_Digital_Usage_and_Inclusion/README.md) archives the licensed article and supplement, pins the public release, and documents Census sources. Original calculations distinguish geographic activity from individual ability, reproduce the source example under two log conventions, and examine assistance and access.

## Statistical Inference and AI-Assisted Analysis

The [Fisher-R1 source collection](39_Statistical_Inference_and_AI/README.md) archives the licensed paper and a benchmark question, documents the inspected repository, and distinguishes answer agreement from statistical calibration. Original mHealth and store-randomization examples connect M1, M3, M6, and M9.

## Econometric Coding Workflows

[The coding-workflow collection](40_Econometric_Coding_Workflows/README.md) connects the November 2026 Galiani, López, and Sosa study to execution feedback, silent errors, prompt-effect scales, and costs. Three small CC0 aggregate tables support original Python exercises. The paper and complete replication release remain linked with their versions and rights.

## Statistical Claims, Household Burdens, and Agency

The [statistical-claims examples](41_Statistical_Claims_and_Decisions/README.md) connect repeated p-values, economic thresholds, equivalence, and a recurring data-center electricity case. M2 §2.28, M3 §3.19, M6 §§6.32–6.33, M8 §8.31, and M9 §§9.25–9.26 examine reported tables, measurement, causal interpretation, public reassurance, ontology, and household authority. Four complete Python programs and five original TikZ figures support the comparisons. Guided practice is optional and ungraded.
