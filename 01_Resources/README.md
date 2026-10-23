# Marketing Analytics Resource Library

Collected October 23, 2026 for Nathan Yang's planned version of **Marketing Analytics**. The collection follows Unnati Narang's eight-module Spring 2026 syllabus and adds resources for AI-assisted coding throughout the course. The wiki and new syllabus have not been built.

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

The [nutrition methods collection](12_Nutrition_and_Dietary_Data_Quality/README.md) adds 14 cataloged sources on food records, usual intake, outliers, energy adjustment, reporting plausibility, and documented dietary reliability. Eleven government resources and two methods PDFs were downloaded. The copyrighted Black PDF remains in the instructor Dropbox folder; the public collection contains its summary and source links. The original Goldberg paper is linked from its abstract. These resources support the mHealth audit and screening examples in M1–M3.
