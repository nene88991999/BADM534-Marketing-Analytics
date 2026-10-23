# Resources Integrated Into Lecture Notes

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

The [Markdown modules](README.md) include the complete program text beside each case. The compiled notes have 41 TikZ figures using the Illinois palette, including six figures added with these cases. Numerical outputs and the environment record are available in [mHealth results](../03_Data_and_Code/mHealth/recurring_examples/results/) and the [synthetic IV result](../03_Data_and_Code/Lecture_Examples/price_iv_results.json).

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

Run the programs through the commands in the [mHealth example README](../03_Data_and_Code/mHealth/recurring_examples/README.md) and [synthetic example README](../03_Data_and_Code/Lecture_Examples/README.md). `test_extension_logic.py` checks seven independent small cases, including a censored risk set with tied times, a confirmed gap followed by a return, future-information exclusion, a denominator mismatch, and a coefficient that increases adjusted variance. `scripts/check_lecture_code.py` verifies all 32 embedded source blocks against their matching files.

The mHealth programs use the existing 370-user teaching cohort and impose case-specific eligibility rules before reporting results. Their outputs are aggregate. The price simulation is explicitly synthetic. Schema-valid false claims are constructed teaching examples, not measured errors from an LLM. Historical variance reduction is a planning comparison, and basket lift is a descriptive association.

Original source licenses are retained. Takeda's `LICENSE-CODE` explicitly permits Python and notebook reuse; its separate `LICENSE` reserves rights to non-code content. The public mirror includes the licensed source and license/provenance files. Other downloaded prose, data, configuration, and HTML remain in Dropbox through `.gitignore`, with upstream links. The source review record distinguishes downloaded snapshots from course-tested programs.

## Data Visualization Additions

`DATAVIZ.yaml` adds 17 source entries, of which one overlaps with the existing catalog. The additional catalog now contains 629 entries, compared with 613 before these additions. Nine new repository snapshots supply local references. The [visualization review](../01_Resources/00_Index/dataviz_resource_review_2026-10-23.json) identifies the inspected sources, catalog aliases, licenses, and incorporation decisions.

| Notes | Source References | Incorporation |
| --- | --- | --- |
| M2, 2.14 | Financial Times Visual Vocabulary; seaborn distribution and palette tutorials | Managerial question before chart choice; fixed versus conditional denominators; exact ECDFs; ties, endpoint masses, scales, and redundant visual encodings. |
| M2, 2.15 | Altair tutorial and current widget/export documentation | Aggregate-data month selector, fixed scales, explicit counts, an accessible HTML table, and a static-hosting example. |
| M3, 3.6.1 | seaborn error-bar tutorial | Distribution spread versus uncertainty; complete-user resampling; a paired interval compared with an incorrect independent-day calculation. |
| M8, 8.12 | VisEval | Executability, fidelity to the analytical question, and readability; four constructed chart mistakes and an independent numerical audit. |

`visualization.py`, `visualization_charts.py`, and `chart_audit.py` were written for the course and executed locally. Their full code is embedded in the notes. Three generated TikZ figures use the Illinois palette. Five independent small-data tests supplement the numerical checks. [Chart data and replication instructions](../03_Data_and_Code/mHealth/recurring_examples/results/VISUALIZATION.md) describe the output and browser-validation scope.

FlowingData, its commercial book, the unlicensed storytelling recreation, Data to Viz, Datawrapper, Munzner, and PyNarrative remain optional linked references. No paid material was copied. Bokeh and HoloViz remain alternative implementation references, with their notebooks unexecuted. Matplotlib cheat sheets and Rougier's code remain figure-construction references. Rougier's `LICENSE.txt` separately grants BSD-2-Clause terms to code and CC BY-NC-SA 4.0 terms to book material; the catalog and generated provenance label have been corrected to preserve that distinction.
