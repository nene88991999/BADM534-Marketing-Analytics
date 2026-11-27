# Resources Integrated into Lecture Notes

The October 23 additions contain 77 source entries across `PY_BOOKS_COURSES.yaml` and `PY_METHODS_INDUSTRY.yaml`. These entries overlap with each other and the existing collection. After catalog reconciliation, the additional catalog grows from 546 to 613 entries. The 35 new local repository snapshots occupy approximately 221 MB before Git compression. These counts describe different objects and must not be added together.

The review used the catalog metadata and repository indexes to select relevant material, then inspected the specific source files listed in the [review record](../01_Resources/00_Index/python_resource_review_2026-10-23.json). It does not represent a line-by-line review of every downloaded file. Original snapshot commits, licenses, and source links remain in each `SOURCE.md`. Downloaded notebooks were not executed. The eight course programs below were written for the lecture examples and executed locally; they do not import downloaded repository code or call external AI services.

## Integrated Cases

Resource IDs in this table use the **additional** catalog namespace, including source aliases recorded in the YAML and `local_copies.json`. Search the catalog by title or URL when a duplicate has been merged into another ID.

| Notes | Case | Source IDs | Executed Program | Integration |
| --- | --- | --- | --- | --- |
| M1, 1.10 | Fixed-Cohort Business Review | claude-ecom-business-review-skill | [reporting.py](../03_Data_and_Code/mHealth/recurring_examples/reporting.py) | 340 eligible users; May/June denominators; source checksum and counting identity. |
| M2, 2.13 | Recency and Frequency | correia-rfm-analysis | [recency.py](../03_Data_and_Code/mHealth/recurring_examples/recency.py) | June snapshot and July logging; zero-log users retained; no invented monetary variable. |
| M3, 3.12 | Price Endogeneity and Instruments | pyblp-tutorials | [price_iv.py](../03_Data_and_Code/Lecture_Examples/price_iv.py) | Synthetic markets; OLS, valid IV, and a direct-effect violation; robust uncertainty. |
| M4, 4.13 | Logging-Gap Survival | lifelines-churn-notebooks | [logging_gaps.py](../03_Data_and_Code/mHealth/recurring_examples/logging_gaps.py) | Confirmed gap timing, administrative censoring, explicit risk sets, 14/28-day sensitivity. |
| M5, 5.12 | Topic Models and Measurement | blueprints-text-analytics; bertopic-docs-llm-representations | [topics.py](../03_Data_and_Code/mHealth/recurring_examples/topics.py) | Frozen TF-IDF/NMF; component scaling; future vocabulary coverage; two weighting schemes. |
| M6, 6.15 | CUPED and Precision | feedx-shopping-feed-experiments | [cuped.py](../03_Data_and_Code/mHealth/recurring_examples/cuped.py) | Prior-period coefficient; historical variance; sharp-null simulation and an analytical variance check. |
| M7, 7.17 | Basket Associations | mlxtend-frequent-patterns | [association_rules.py](../03_Data_and_Code/mHealth/recurring_examples/association_rules.py) | Support, confidence, lift, training-only selection, future baskets, user bootstrap. |
| M8, 8.11 | Evidence Checks for Generated Claims | copycat-ad-copy-generation; pymc-labs-semantic-similarity-rating; claude-ecom-business-review-skill | [claim_checks.py](../03_Data_and_Code/mHealth/recurring_examples/claim_checks.py) | Constructed false claims; numerical and interpretation checks; synthetic-consumer validity discussion. |

The [Markdown modules](README.md) include the complete program text beside each case. The compiled notes have 47 TikZ figures using the Illinois palette, including six figures added with these cases. Numerical outputs and the environment record are available in [mHealth results](../03_Data_and_Code/mHealth/recurring_examples/results/) and the [synthetic IV result](../03_Data_and_Code/Lecture_Examples/price_iv_results.json).

## Other Uses of the Added Resources

| Resource Group | Course Use | Execution Status and Conditions |
| --- | --- | --- |
| Packt marketing books, Dong's textbook notebooks, Takeda's practitioner code, TensorHouse | Alternate examples across M1–M8; compare data definitions, estimands, and output units with the verified course cases. | Reference material. Package versions, chapter-specific data rights, and saved output need checking before adaptation. Public solutions should not be reused as undisclosed graded assessments. |
| pandas exercises and ecommerce tools | M1–M2 practice with filtering, aggregation, joins, and customer tables. | Reference material. The fixed-cohort course example supplies an executed baseline. |
| pyrsm conjoint and choice notebooks | M4 preference elicitation, willingness to pay, and choice-task construction; distinguish respondent/task IDs from a task number reused by different respondents. | Selected notebooks inspected, not executed. Preserve AGPL terms when adapting source. |
| AI-Assisted Statistics, Behavioral Data Analysis, Bayesian decision notebooks | M3/M6 inference, clustered assignment, bootstrap logic, and expected-loss decisions. | Reference material; the course IV simulation and CUPED comparison use their own stated data-generating or assignment assumptions. |
| FeedX, Spotify Confidence, Meridian GeoX, Orduz's experiment examples | M6 experiment units, prior-period adjustment, monitoring, geo experiments, and power. | FeedX adjustment source inspected; other reference workflows not executed. Sequential monitoring and geography require design-specific validation. |
| Robyn, media-mix notebooks, attribution packages, Awesome Marketing Science | M8 allocation, carryover, saturation, calibration, and the distinction between attribution and incrementality. | Reference material. Dataset-specific identification and calibration evidence remain necessary. |
| Crystalvalue, lifetime-value and churn examples | M4/M7 forecasting retention and commercial value with documented timing and costs. | Reference material. mHealth logging gaps have no observed subscription-cancellation or monetary-value outcome. |
| implicit and Surprise | M7 contrast implicit occurrences with explicit ratings; retain the course's chronological and candidate-set evaluation. | Reference material; no fitted collaborative-filtering model is claimed. |
| Text blueprints, BERTopic, embeddings cookbooks | M5 representation, topic descriptions, label evaluation, and future-text coverage. | Local NMF course program executed; downloaded embedding/LLM notebooks not executed. |
| Copycat, Gemini and Google Cloud marketing notebooks, semantic-similarity rating | M8 generated copy, structured extraction, synthetic respondents, and validation against consumer outcomes. | Selected documentation inspected; no model credentials, cloud deployment, external calls, or consumer-panel validation performed. |
| Linked courses, paid workshops, gated books, and datasets requiring registration | Instructor references and routes to further reading. | Link-only or reference resources; catalog access labels do not imply enrollment, purchases, or course execution. |

## Replication and Publication

Run the programs through the commands in the [mHealth example README](../03_Data_and_Code/mHealth/recurring_examples/README.md) and [synthetic example README](../03_Data_and_Code/Lecture_Examples/README.md). `test_extension_logic.py` checks seven independent small cases, including a censored risk set with tied times, a confirmed gap followed by a return, future-information exclusion, a denominator mismatch, and a coefficient that increases adjusted variance. `scripts/check_lecture_code.py` verifies all 40 embedded source blocks against their matching files.

The mHealth programs use the existing 370-user teaching cohort and impose case-specific eligibility rules before reporting results. Their outputs are aggregate. The price simulation is explicitly synthetic. Schema-valid false claims are constructed teaching examples, not measured errors from an LLM. Historical variance reduction is a planning comparison, and basket lift is a descriptive association.

Original source licenses are retained. Takeda's `LICENSE-CODE` explicitly permits Python and notebook reuse; its separate `LICENSE` reserves rights to non-code content. The public mirror includes the licensed source and license/provenance files. Other downloaded prose, data, configuration, and HTML remain in Dropbox through `.gitignore`, with upstream links. The source review record distinguishes downloaded snapshots from course-tested programs.

## Data Visualization Additions

`DATAVIZ.yaml` adds 17 source entries, of which one overlaps with the existing catalog. After the visualization additions, the additional catalog contained 629 entries, compared with 613 beforehand. Nine new repository snapshots supply local references. The [visualization review](../01_Resources/00_Index/dataviz_resource_review_2026-10-23.json) identifies the inspected sources, catalog aliases, licenses, and incorporation decisions.

| Notes | Source References | Incorporation |
| --- | --- | --- |
| M2, 2.14 | Financial Times Visual Vocabulary; seaborn distribution and palette tutorials | Managerial question before chart choice; fixed versus conditional denominators; exact ECDFs; ties, endpoint masses, scales, and redundant visual encodings. |
| M2, 2.15 | Altair tutorial and current widget/export documentation | Aggregate-data month selector, fixed scales, explicit counts, an accessible HTML table, and a static-hosting example. |
| M3, 3.6.1 | seaborn error-bar tutorial | Distribution spread versus uncertainty; complete-user resampling; a paired interval compared with an incorrect independent-day calculation. |
| M8, 8.12 | VisEval | Executability, fidelity to the analytical question, and readability; four constructed chart mistakes and an independent numerical assessment. |

`visualization.py`, `visualization_charts.py`, and `chart_assessment.py` were written for the course and executed locally. Their full code is embedded in the notes. Three generated TikZ figures use the Illinois palette. Five independent small-data tests supplement the numerical checks. [Chart data and replication instructions](../03_Data_and_Code/mHealth/recurring_examples/results/VISUALIZATION.md) describe the output and browser-validation scope.

FlowingData, its commercial book, the unlicensed storytelling recreation, Data to Viz, Datawrapper, Munzner, and PyNarrative remain optional linked references. No paid material was copied. Bokeh and HoloViz remain alternative implementation references, with their notebooks unexecuted. Matplotlib cheat sheets and Rougier's code remain figure-construction references. Rougier's `LICENSE.txt` separately grants BSD-2-Clause terms to code and CC BY-NC-SA 4.0 terms to book material; the catalog and generated provenance label have been corrected to preserve that distinction.

## McBroken Resources and Executed Cases

The supplied [McBroken bundle](../01_Resources/02_M2_Customer_Data_and_Visualization/mcbroken_api_lab/README.md) includes source retrieval scripts, a notebook with saved outputs, a US store panel, and daily/weekly aggregates. The [course adaptation review](../01_Resources/02_M2_Customer_Data_and_Visualization/mcbroken_api_lab/COURSE_ADAPTATION.md) records the inspected source logic, policy-date correction, measurement issues, and verification scope.

| Resource | Course Application | Verified Output |
| --- | --- | --- |
| Supplied snapshot and panel extraction | M2 §2.16: API type handling, source assessment, coverage, address keys, exact calendar joins | `api_checks.py`, `prepare.py`, `coverage.py`; national counts and dimension totals reconcile |
| Weekly country series and the Copyright Office's 2024 final rule | M6 §6.16: common-week policy contrasts and comparison-country sensitivity | `policy.py`; descriptive USA–Canada and USA–UK contrasts with implementation week omitted |
| US store panel and snapshot manifest | M7 §7.18: time-separated forecasts, Brier scores, calibration, missing future labels | `predict.py`; later-date evaluation and eligible-origin denominator |

The five original teaching programs use the local data and appear in full in the notes. Their [README](../03_Data_and_Code/McBroken/README.md), [data dictionary](../03_Data_and_Code/McBroken/DATA_DICTIONARY.md), [manifest](../03_Data_and_Code/McBroken/manifest.json), and [result descriptions](../03_Data_and_Code/McBroken/results/README.md) provide replication and interpretation details. Three additional TikZ figures use the Illinois palette. The supplied network collector and notebook were inspected as references; the adaptation does not claim to have rerun their complete historical retrieval. The original bundle is preserved with attribution, and no scheduled collection was activated.

## Generative-AI Demand Resources

The October 26 addition contains ten entries in `GENAI_DEMAND.yaml`, increasing the additional catalog from 634 to 644 resources. The [review record](../01_Resources/00_Index/genai_demand_resource_review_2026-10-26.json) and [adaptation review](../01_Resources/08_M8_Current_Topics_in_Marketing/genai_demand_lab/COURSE_ADAPTATION.md) distinguish inspected source files, verified external definitions, executed adaptations, and optional extensions.

| Notes | Resource and Question | Executed Adaptation |
| --- | --- | --- |
| M2 §2.17 | Public signals and Wikimedia title-level counts | `measurement.py`: complete calendars, duplicate/conflict checks, selected-title aggregation, and independent monthly totals |
| M4 §4.14 | Supplied synthetic subscription panel and its generator | `retention.py`: full-population adoption, fixed-cohort provider/category outcomes, endpoint versus continuous retention, four acquisition-event categories |
| M8 §8.13 | Egan et al. and Fradkin abstracts; supplied price-regression example | `demand.py`: stock/flow projections, price support and rank checks, independent residualized slope, and exact binary-logit benchmark |

Three complete Python blocks and three original TikZ figures accompany the cases. The [course README](../03_Data_and_Code/GenAI_Demand/README.md), [data dictionary](../03_Data_and_Code/GenAI_Demand/DATA_DICTIONARY.md), [agent guide](../03_Data_and_Code/GenAI_Demand/AGENTS.md), and aggregate results support replication. Eight hand-checkable counterexample tests passed. The original notebook, network collectors, and complete panel simulator were inspected but not rerun. No model API calls or scheduled retrievals occurred.

The supplied notebook's flow regression does not establish recovery of the dynamic simulator's utility price coefficient. Its original retention curves also compare different starting cohorts, and its new-provider measure includes first adoption, reentry, and additions. The course cases correct these interpretations. Catalog summaries now point to the executed adaptation and retain the distinction between public snapshots and simulated consumers. Apple, Ramp, Epoch, Wayback, and Cloudflare remain useful measurement or collection extensions with their stated verification limits.

## Ethics and Regulation

New conceptual material informs data boundaries, sample restrictions, claim support, retention, review provenance, experimentation, delivery, and adaptive objectives across M1–M8. The [integration guide](ETHICS_AND_REGULATION.md) maps the numbered note sections and session decks. Public legal propositions are checked against FTC and DOJ sources, with sector and procedural status retained.

The new [retention calculation](../03_Data_and_Code/Lecture_Examples/retention_welfare.py) uses imposed probabilities and monetary stakes. Its CSV independently reconciles with a 100-customer calculation and supplies the new TikZ figure. It is an analytical illustration, not an estimate of customer responses. The [session examples](../03_Data_and_Code/Lecture_Examples/session_examples.py) reproduce the small projected calculations.

## Earnings-Call Pricing Communication

The newly supplied `pricing_risk_earnings_calls` bundle contributes 2,326 call records, 971 match records, a firm roster, a dictionary, collectors, and interpretation notes. The [course adaptation](../03_Data_and_Code/Earnings_Calls/README.md) retains factual metadata and adds seven source-linked paraphrases. It preserves the raw bundle locally and records original and exported hashes. The supplied collectors and starter analysis were inspected, not executed.

| Notes and Session | Integration | Executed Program |
| --- | --- | --- |
| M2 §2.19; S02 | Missing transcript versus observed zero; roster retention; selection into retrieved calls | `assessment.py` |
| M5 §5.14; S07 | Role exposure, quarterly support, substantive coding, and synthetic contrasts | `disclosure.py`, `construct_checks.py` |
| M6 §6.18; S10 | Common firms, alternative windows, occurrence counts, and call incidence | `event_windows.py` |
| M8 §8.16; S14 | Price rules, customer outcomes, and regulatory evidence | Interpretation table and M5 programs |

All four programs and nine counterexample tests passed. Full code is embedded in the notes, and three generated TikZ figures reconcile to output tables. Dictionary precision, population adoption, causal event effects, and firm risk probabilities are not established by these data. Wendy's dated clarification and the FTC staff research document were checked as primary sources; other supplied event-list legal claims are not incorporated.

## AI Workflow Evaluation and Economics

| Notes | Course Application | Program or Example |
| --- | --- | --- |
| M1 §1.12 | Code errors, missing information, and the analytical target | mHealth aggregation and coupon evidence |
| M4 §4.16 | Buyer burden and the outside option | Customer participation at a common horizon |
| M5 §5.15 | Prompt revision and document dependence | Earnings-call evaluation on unseen firms or later periods |
| M6 §6.19 | Separate model and library contributions | `AI_Workflows/factorial.py` |
| M7 §7.20 | Selection among equally uninformative candidates | `AI_Workflows/repeated_selection.py` |
| M8 §§8.17–8.18 | Reuse economics, price bounds, and selective upgrades | `AI_Workflows/investment.py` and task-specific revalidation |

The [original teaching examples](../03_Data_and_Code/AI_Workflows/README.md) contain three executed Python programs, five exact small-case checks, aggregate CSV/JSON outputs, and an agent guide. Four TikZ figures reconcile to those outputs. All numerical inputs are synthetic. The selection simulation has an independent analytical benchmark, and the factorial and investment programs check contrasts and monetary balances directly. No model service was called. Sessions 01, 05, 07, 09, 11, and 14 incorporate the cases within the existing meeting allocations.

## Consumer Agency and University Affiliation Networks

The [recent journal review](../01_Resources/13_Consumer_Agency_and_Recent_Research/README.md) provides source-specific managerial implications and separates reported choice concerns from inferred dual use. `assess_coverage.py` in M2 §2.20 preserves missing evidence. `cluster.py` in M4 §4.17 compares Jaccard clusters, alternative samples, distances, and feature perturbations. `affiliation_clusters.py` in M5 §5.17 groups higher-education institutions by shared-publication links and uses fractional allocations for research profiles. The three programs and their [outputs](../03_Data_and_Code/Consumer_Agency_Literature/README.md) are public and executable without the local PDFs.

M5 §5.16 distinguishes text classification from construct validity. M6 §6.20 evaluates purchases, returns, and effective exit; M7 §7.21 preserves model-dependent welfare interpretation; M8 §8.19 connects those mechanisms to the [verified cancellation-policy record](../01_Resources/13_Consumer_Agency_and_Recent_Research/Policy/README.md).

## LLM Findings and Revalidation

The [Queen and Zou snapshot and six related papers](../01_Resources/14_LLM_Evidence_and_Revalidation/README.md) motivate versioned evidence in M1 §1.13, censoring in M2 §2.21, changing judges in M5 §5.18, paired regressions in M7 §7.22, and exposure in M8 §8.18.1. `summarize_snapshot.py` reads licensed released tables; `evaluate_judges.py` and `evaluate_upgrade.py` use entirely constructed inputs. [All three programs](../03_Data_and_Code/LLM_Revalidation/README.md) appear verbatim in the notes. The aggregate counts reconcile to the source files; this does not reproduce the underlying model calls or fitted trends.

## Marketing Dialectics

M9 links Kantian dialectic and ethics with institutional scrutiny of private interests (Hume, 1741; Smith, 1776) and Confucian accounts of righteousness, trust, roles, and cultivation. The [41-entry library](../01_Resources/15_Marketing_Dialectics/README.md) separates original texts, adaptations, scholarly interpretation, research, and institutional cases. The new [renewal example](../03_Data_and_Code/Marketing_Dialectics/README.md) has complete source in §9.5; six diagrams clarify claims, premises, denominators, goals, scope, and burdens of justification. Session 14 and the syllabus include the chapter within existing meeting time.

## AI Experimentation, Pricing, and Ethical Judgment

[Four research contributions and primary policy sources](../01_Resources/16_AI_Experimentation_and_Pricing/README.md) inform M6 §6.21, M8 §8.20, and M9 §§9.14–9.18. [The executed pricing example](../03_Data_and_Code/AI_Experimentation_and_Pricing/README.md) solves an original imposed population exactly, contrasts distributional and aggregate outcomes, and separately checks arithmetic from published summaries. It does not reproduce the papers' experiments or estimate ethical legitimacy. Two new TikZ figures show incidence and the role of justified restrictions.

## PyStatlas Statistical Graphics

Thierry Warin’s [PyStatlas](https://warint.github.io/pystatlas/) informs M2 §2.22 and M7 §7.23. Original synthetic examples preserve customer pairs and distinguish ranking from probability accuracy. [The resource guide](../01_Resources/17_PyStatlas_Statistical_Graphics/README.md) maps the 12 families to course questions and records code-reading scope. [Executed programs and tests](../03_Data_and_Code/Statistical_Graphics/README.md) supply the aggregate tables used by two new TikZ figures. Sessions 3 and 11 carry the corresponding discussion.

## Conformal Prediction

[The source review](../01_Resources/18_Conformal_Prediction/SOURCE_REVIEW.md) informs finite-sample calibration in M7 §7.24, complaint-label sets in §7.25, and changed-demand evaluation in M8 §8.21. [Original course programs](../03_Data_and_Code/Conformal_Prediction/README.md) construct all inputs, preserve every evaluation record, and provide the tables for two TikZ figures. Sessions 11 and 13 contain the corresponding discussion. Source inspection is recorded separately from executed course code; no upstream notebook was run.

## Thinking with AI: Source Selection and Evaluation

[Stanford CS193T activity ideas](../01_Resources/19_AI_Practice_and_Evaluation/README.md) support the original source-selection and grader comparisons in M5 §§5.19–5.20. M1 §1.14 and M7 §7.26 connect specifications, independent explanation, evaluation coverage, and asymmetric loss. Two programs, six checks, and two TikZ diagrams use entirely synthetic inputs. [The practice lab](../07_Labs/AI_Evidence_and_Evaluation/README.md) supplies an optional protocol for collecting new responses. Sessions 7 and 11 include the comparisons.

## Clustering Optimization

[The e-means and o-means source review](../01_Resources/23_Clustering_Optimization/README.md) informs M4 §§4.18–4.20. The original scalar examples and fixed-data CPU comparison preserve common initial centers, an exhaustive final scorer, and explicit timing boundaries. Two figures show inconsistent labels and the measured cost/error comparison. Full Python and [optional practice](../07_Labs/Clustering_Optimization/README.md) accompany Session 6; M5 §5.3 and M7 §7.27 connect representation and evaluation. The reviewed GPU claims are distinct from the executed CPU results.

## Dose-Response Curves

The [dose-response sources](../01_Resources/24_Dose_Response/README.md), reviewed November 18, 2026, support M6 §§6.22–6.27 and the M8 objective calculation. The course's original NumPy examples evaluate four nuisance specifications over 200 simulated samples, a separate randomized-store pooling comparison, and three known-function objectives. Three editable figures show a zero linear projection slope, conditional overlap, and store-level shrinkage. Full code appears in the notes. Source package simulations and continuous-DiD implementations were not executed.

## Spatial Networks and Retail Alternatives

[The city2graph review](../01_Resources/25_Spatial_Networks/README.md) motivates original distance and geometry calculations in [Retail Accessibility](../03_Data_and_Code/Retail_Accessibility/README.md). M2 §2.23 covers map footprints; M4 §4.22 covers spatial representations; M5 §§5.21–5.22 contain full accessibility and observed-network programs; M7 §7.28 matches evaluation to deployment; M8 §8.23 compares restoration priorities; M9 §9.18.2 examines feasible alternatives and service conduct. Three original programs were executed with NetworkX. No upstream notebook, city2graph package, clustering fit, or GNN training was executed. The selected observed snapshot and later street extract retain separate dates and attribution.

## Anomaly Detection and Diagnosis

The [SHAD review](../01_Resources/26_Anomaly_Detection_and_Diagnosis/README.md) motivates M7 §§7.29–7.30. Original standard-library programs generate a fixed synthetic retail panel and exact timing/imputation comparisons. Eight independent checks verify population counts, information boundaries, tied-threshold conventions, confusion counts, interval arithmetic, packet contents, and the beneficial campaign. Two editable figures and six Session 11 slides preserve the distinction between observed symptoms and imposed causes. No original benchmark or LLM API was executed.

## AI Inference Efficiency

The [G-MTP paper and source review](../01_Resources/27_AI_Inference_Efficiency/README.md) motivate M7 §§7.31–7.32. [Two original standard-library programs](../03_Data_and_Code/Inference_Efficiency/README.md) generate synthetic decoding rounds and separately constructed teacher-forced predictions and free responses. Nine checks verify boundary cases, failed-request denominators, costs, and development selection. Two editable figures and four Session 11 slides connect computation to correct customer resolution. M1, M4, and M8 supply short conceptual links. Published figures remain attributed and configuration-specific. No upstream model, training code, benchmark, or external inference service was executed.

## Training Data Mixtures

The [Homeopathic Learning review](../01_Resources/28_Training_Data_Mixtures/README.md) motivates M7 §§7.33–7.35. [Three original standard-library programs](../03_Data_and_Code/Training_Data_Mixtures/README.md) distinguish an exact synthetic ridge calculation, imposed paired service outcomes, and recomputed published aggregates. Ten checks cover normal equations, penalty scaling, context denominators, pairing, and resumed epoch logs. Two editable TikZ figures and five Session 11 slides preserve source counts, score units, final and peak checkpoints, and the distinction between model behavior and company intent. M2, M3, M8, and M9 supply conceptual links. No upstream code, model training, or external inference service was executed.

## Synthetic Consumer Measurement and Concept Screening

[Maier and coauthors' paper and pinned repository](../01_Resources/29_Synthetic_Consumer_Research/README.md) support M4 §4.23, M5 §5.23, M7 §7.36, M8 §8.11, and M9 §9.18.4. The course adaptations use two original standard-library programs with invented panels and imposed similarities. The repository's private study data are unavailable, so no replication of human-response results is claimed. Reported correlation attainment retains its split-half denominator and the paper's same-survey anchor-selection qualification.

The [implemented examples](../03_Data_and_Code/Synthetic_Consumers/README.md) include explicit uninformative mappings, equal-persona aggregation, common concept rosters, undefined correlations, and tied shortlist boundaries. Ten independent checks and two editable figures support eight new slides across Sessions 5, 7, and 14. [Optional ungraded practice](../07_Labs/Synthetic_Consumers/README.md) develops sensitivity analysis and human validation.

## Auxiliary Data and Bias Geometry

[Jasin, Lin, and Zhang's working paper](../01_Resources/31_Auxiliary_Data_and_Bias_Geometry/SOURCE_REVIEW.md) supports M3 §3.16, M4 §4.24, M6 §6.28, and M7 §7.37. [Two original programs](../03_Data_and_Code/Auxiliary_Data/README.md) calculate means, optimal continuous precision, rounded allocations, and analytic MSE under an omitted bias feature. Six checks independently construct joint-regression normal equations, compare the allocation with a feasible numerical search, and assess the expanded bias dictionary. Three TikZ figures and nine slides across Sessions 4, 5, 9, and 11 retain the fixed coefficient loss and source assumptions. The paper's retrospective savings remain attributed and separate from the invented example; author code and survey microdata were not executed.

## Graph Coarsening and Information Restrictions

[The pinned GraCo review](../01_Resources/32_Graph_Coarsening/SOURCE_REVIEW.md) supports M5 §5.24 and M7 §7.38. [Original executed cases](../03_Data_and_Code/Graph_Coarsening/README.md) distinguish revenue preservation from access, original-node weights from group weights, and oracle label diagnostics from fitted prediction. Nine independent tests verify arithmetic and information-set comparisons. No upstream toolkit or GNN training was executed.

## Ontologies and Representation Evaluation

[The ontology review](../01_Resources/33_Ontologies_and_Knowledge_Representation/SOURCE_REVIEW.md) informs M1 §1.16 and M2 §2.25. The original cancellation case preserves requests, confirmations, unknown states, dated evidence, and row-level validation findings. Eight independent tests accompany complete Python and an editable diagram. M5 §5.25 preserves source-attributed claims; M9 §9.19 connects definitions to Kantian inference and Confucian role expectations.

[Delisle and Tan's paper and pinned repository](../01_Resources/34_Representation_Evaluation/SOURCE_REVIEW.md) inform M7 §§7.39–7.40. Two original programs and six tests examine reconstruction, coordinate scales, review recall, and nonunique exact decompositions. Two editable figures preserve the different denominators and dictionary-dependent removal errors. M4 §4.25 connects reproducibility with segment interpretation. These synthetic examples do not reproduce sparse-autoencoder training or estimate marketing effects. Third-party source notices remain intact.

## Agent Workflow Evaluation

[Agent Harness Engineering: A Survey](../01_Resources/35_Agent_Workflow_Evaluation/README.md), §§5, 8, 9, and 11, motivates original comparisons in M1 §1.17, M6 §6.29, M7 §7.41, M8 §8.26, and M9 §9.20. [Four executed programs](../03_Data_and_Code/Agent_Workflows/README.md) reconstruct compact mHealth tasks, calculate reference results, grade CSV outputs, and reproduce hypothetical costs. Eight independent tests include a SQLite comparison. The four-cell model experiment remains a protocol; no model performance is reported.

## Representation Alignment and Functional Evaluation

[The reviewed sources](../01_Resources/36_Representation_Alignment/SOURCE_REVIEW.md) motivate separate geometry and task comparisons. M5 §5.26 contains complete sample preparation; M7 §§7.42–7.43 contain complete alignment and classification programs; §7.44 defines a separate answer-evaluation protocol. The executed [mHealth comparison](../03_Data_and_Code/Representation_Alignment/README.md) uses 6,000 training, 1,500 validation, and 1,500 test descriptions. M8 §8.27 and M9 §9.21 connect cost and justification. The two figures use original synthetic cases. No upstream neural-model experiment or prompt experiment was executed.

## Pricing Systems and Customer Choice

[Six source records](../01_Resources/37_Pricing_Systems_and_Competition/README.md) motivate an original [pricing comparison](../03_Data_and_Code/Pricing_Competition/README.md). M4 §4.26 varies demand information and the pricing objective separately; M8 §8.28 distinguishes the complaint, company statements, and agency argument; M9 §9.22 develops the philosophical evaluation. Exact fractions, complete Python, nine checks, two editable figures, and Sessions 5 and 14 support the comparison. The calculation is separate from Harrington's vendor-design model and contains no actual Wendy's prices.

## Digital Usage and Customer Access

[Pereira and coauthors’ article and public release](../01_Resources/38_Digital_Usage_and_Inclusion/SOURCE_REVIEW.md) support M2 §§2.26–2.27, M3 §3.17, M4 §4.27, M7 §7.45, M8 §8.29, and M9 §9.23. Five complete source listings, eleven independent tests, four original TikZ figures, and ten slides across Sessions 2, 3, 4, 6, and 14 accompany the [executed geographic examples](../03_Data_and_Code/Digital_Usage/README.md). The course adds public Census estimates, preserves source counts and formula discrepancies, and separates descriptive evidence from service outcomes and ethical justification. No private telemetry pipeline was reproduced.

## Statistical Inference and AI-Assisted Analysis

The [Fisher-R1 review](../01_Resources/39_Statistical_Inference_and_AI/README.md) informs M1 §1.18, M3 §3.18, M6 §6.30, and M9 §9.24. The course implements two original Python programs, ten independent checks, and two editable TikZ figures. Observed logging uses the existing mHealth release; the store experiment imposes a known zero effect. The consumer-credit question supports philosophical discussion while its reference specification remains unverified. No upstream code or model evaluation is executed.

## Econometric Coding Workflows

[The source collection](../01_Resources/40_Econometric_Coding_Workflows/README.md) supports M1 §1.19, M3 §3.18, M6 §6.31, M7 §7.46, M8 §8.30, and M9 §9.24. The [original programs](../03_Data_and_Code/Agent_Workflows/README.md) reconstruct published denominators, expose deliberately constructed mHealth errors, and compare hypothetical review costs. The three data types remain distinct. Sessions 1, 4, 9, 11, and 14 use existing discussion blocks.

## Statistical Claims and the Ethics of Public Reassurance

The [resource and claim assessment](../01_Resources/41_Statistical_Claims_and_Decisions/README.md) connects Lakens’s inference guidance with the data-center electricity paper. M2 §2.28 distinguishes average prices, household incidence, and ownership categories. M3 §3.19 simulates repeated p-values; M6 §§6.32–6.33 compare detection with profit and reconstruct power, bounds, subgroup tests, sales mechanisms, and residual arithmetic. M8 §8.31 evaluates public communication. M9 §§9.25–9.26 develop equivalence, ontology, reasons, authority, Kantian duties, and Confucian trustworthiness. Four full Python listings and five editable Illinois-color figures accompany the notes. Sessions 4, 9, and 14 add eleven slides within existing allocations. The case distinguishes verified academic coverage from unverified company dissemination, demonstrated interpretation problems from replication questions, and possible harm from established consequences.

## Logical Assessment and Inverse Power

M6 §6.34 develops the inverse-power approach (Andrews, 1989) with specified alternatives, nuisance parameters, and directional sensitivity. M9 §9.27 reconstructs the electricity arguments through premises, counterexamples, measurement, extrapolation, and household authority. The [argument record](../01_Resources/41_Statistical_Claims_and_Decisions/ARGUMENT_ASSESSMENT.md) links claims to evidence and repairs. Two complete Python examples and two editable TikZ figures support the discussion. Sessions 9 and 14 use selected examples within existing meeting allocations; extended calculations remain optional ungraded practice.

## Project Pipelines and Household Expenditure

M2 §2.28.1 separates average revenue per MWh from household bills through a matched-denominator identity. M6 §6.35 adds requests, preparatory investment, cancellation, operating entry, and cost recovery to the treatment definition. Full synthetic Python and an editable TikZ diagram show how costs in a nominally untreated donor alter a comparison. M9 §9.27.6 identifies the missing institutional premises. The [source assessment](../01_Resources/41_Statistical_Claims_and_Decisions/INSTITUTIONAL_ASSESSMENT.md) records the Bloomberg report and primary operator, FERC, and EIA evidence.

## Reasons and Stakeholder Obligations

The supplemental contractualist and stakeholder collection supports M9 §§9.28–9.32, with recurring applications in M1 and M8. Source access and reading extent are recorded in [the guide](../01_Resources/15_Marketing_Dialectics/07_Stakeholders_and_Reasons/README.md). The figures and optional practice use hypothetical cancellation procedures. The electricity application distinguishes nearby residents, customers, cost incidence, and access to a hearing.

## Qualitative Evidence from Utility Disclosures

M5 §5.27 includes three attributed verbatim excerpt boxes, a TikZ evidence diagram, and complete retrieval and comparison programs. M6 §6.36 distinguishes institutional mechanisms from identification; M8 §8.31 and M9 §9.33 address reassurance and stakeholder reasons. Six selected documents and ten claim annotations preserve negative cases and source families. Five sources were downloaded; the remaining accounting passage was reviewed through the web reader. [Methods references](../01_Resources/42_Qualitative_Evidence/README.md) support directed content analysis, reflexivity, contextual comparison, and appropriate coding review.

## Pricing, Individual Reasons, and Antitrust Evidence

M4 §4.28, M6 §6.37, M8 §8.32, and M9 §§9.34–9.39 connect flexible demand models to welfare identification, experimental exposure, Kantian authority, Scanlonian justification, and U.S. antitrust proof. Five [executed programs](../03_Data_and_Code/AI_Experimentation_and_Pricing/README.md) reproduce exact synthetic comparisons and the rounded competitive payoff table (Dubé et al., 2017). Four editable TikZ figures explain the mechanisms. The [source assessment](../01_Resources/16_AI_Experimentation_and_Pricing/SCANLON_ASSESSMENT.md) and [legal guide](../01_Resources/16_AI_Experimentation_and_Pricing/ANTITRUST_AND_REASONS.md) preserve contrary findings, primary citations, and document status. Fourteen new checks pass; all 122 Python blocks match their standalone files.

## Questions, Logical Consequence, and Analytical Arguments

The [primary-source guide](../01_Resources/15_Marketing_Dialectics/08_Logic_and_Analytical_Arguments/README.md) connects question-based reasoning (Koralus and Mascarenhas, 2013), logical normativity (MacFarlane, 2004), inquisitive semantics (Ciardelli et al., 2018), and causal identification (Pearl, 2009) to the course's existing Scanlonian assessment. M1 §1.20, M4 §4.29, M6 §6.38, and M9 §9.40 distinguish question formulation, meaning, compatible models, identified effects, independent valuations, and justified action. Two original exact-fraction programs, ten independent checks, and three editable figures accompany the examples. The source guide records selected reading scope; private research notes remain outside the public course materials.

M1 and [M9 §9.41](../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md) place the worth of the objective, the phenomena–noumena distinction (Kant, 1781/1787), and the practical standing of affected people before optimization. Sessions 1 and 14 connect the limits of empirical representation to separate arguments about ends, authority, and obligations. A fourth editable diagram distinguishes further empirical inquiry from the noumenal limiting concept (Kant, 1781/1787) and practical justification.

[M9 §§9.41–9.43](../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md) distinguish acknowledged epistemic limits from unknown unknowns and assess interpretations through an ontological spectrum. Electricity reassurance, personalized pricing, and cancellation connect to limits of cognition (Kant, 1781/1787), observational justification (Sellars, 1956), critical realism (Bhaskar, 2007), intentionality (Husserl, 1970), and normative reasons (Scanlon, 2009). Publication selection toward tractable questions remains a hypothesis separate from verified evidence of selection by result strength. Session 14 uses selected cases within its existing discussion blocks; the extended comparisons are optional practice.

## AI-Augmented Learning and Independent Judgment

[The reviewed paper and later report](../01_Resources/43_AI_Augmented_Learning/README.md) motivate preserving an argument across prose, equations, diagrams, and code. M1 §1.21 develops that requirement; M2 §2.29 connects percentages and bills; M6 §6.39 uses a synthetic factorial comparison; M9 §9.44 examines learner authority. [Complete Python](../03_Data_and_Code/Learning_Design/README.md), two editable figures, and the [electricity pilot](../08_Wiki/pilot/README.md) support the examples. Usability and calculation checks do not establish an effect on student learning.

## Conflicts of Interest and Consumer Control

The [nine-source supplement](../01_Resources/15_Marketing_Dialectics/09_Conflicts_of_Interest/README.md) supports M1 §1.22, M7 §7.47, M8 §8.33, and M9 §§9.45–9.49. The [synthetic feed program](../03_Data_and_Code/Conflicts_of_Interest/README.md) uses original totals and no borrowed empirical coefficients. Sessions 1, 11, and 14 use selected discussion slides; [optional practice](../07_Labs/Conflicts_of_Interest/README.md) supplies the extended exercise.

## Bad Controls and Project Exposure

The [categorized collection](../01_Resources/44_Bad_Controls_and_Project_Exposure/README.md) connects M3 causal graphs to M6 panel identification and the phantom-project case. The examples separate a total effect from a conditioned coefficient and an operating-entry effect from the wider proposal population. M9 §9.50 asks which empirical premises justify reassurance to households. The 2020–2025 historical evidence supports particular scrutiny of later sample years; exact donor exposure requires project and payment records.

## Data, Truth, and Norms

The [collection](../01_Resources/45_Data_Truth_and_Norms/README.md) develops an explicit analogy from created artifacts (Thomasson, 1999, 2014) while preserving the distinction between datasets and represented people. Accounts of data, inductive risk, critical interaction, and undone science connect institutional production to evidence and public justification (Leonelli, 2015; Bogen and Woodward, 1988; Douglas, 2000; Longino, 2004; Frickel et al., 2010). M2 §§2.30–2.31 and M9 §§9.51–9.54 develop the conceptual and synthetic examples. M6 §6.43 uses EIA and specific institutional documents to correct a universal noncollection claim and identify the unresolved linkage and counterfactual requirements.

## Measurement and Evidentiary Standards

The [historical readings](../01_Resources/46_Measurement_and_Disciplinary_History/README.md) support M1 §1.23 and M9 §9.55. The [evidence-standards collection](../01_Resources/47_Evidence_Standards_and_Error_Costs/README.md) supports M2 §2.32, M3 §3.22, M4 §4.30, M5 §5.28, M6 §§6.44–6.45, M7 §7.48, M8 §8.34, and M9 §§9.56–9.59. The integration distinguishes historical evidence, model restrictions, a philosophical institutional critique, exact synthetic calculation, and legal requirements. It preserves contrary evidence about identification, markup direction, theory at Cowles, and continuing societal marketing research. Complete Python, three editable figures, selected slides in ten sessions, and [optional practice](../07_Labs/Evidence_Standards/README.md) accompany the discussion.
