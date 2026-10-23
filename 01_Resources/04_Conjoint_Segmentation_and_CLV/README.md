# Conjoint, Segmentation, and Customer Lifetime Value

Updated October 23, 2026. 12 curated resources. [Master Guide](../README.md).

Keep the three decisions distinct: product configuration and pricing; useful customer segments; and future customer value. Basic RFM and clustering can precede probabilistic CLV. Bayesian choice and CLV examples are advanced extensions.

## Reading Guide

| ID | Resource | Priority | Format |
| --- | --- | --- | --- |
| C01 | [Academic Teaching Resources for Conjoint Analysis](https://sawtoothsoftware.com/academics/teaching-resources) | Core | Teaching collection |
| C02 | [Discrete Choice Methods with Simulation, Second Edition](https://eml.berkeley.edu/books/choice2.html) | Reference | Author-hosted textbook |
| C03 | [PyMC-Marketing: Multinomial Logit](https://www.pymc-marketing.io/en/latest/notebooks/customer_choice/mnl_logit.html) | Optional | Guide |
| C04 | [Market Segmentation Analysis: Understanding It, Doing It, and Making It Useful](https://link.springer.com/book/10.1007/978-981-10-8818-6) | Core | Open textbook |
| C05 | [scikit-learn: Clustering](https://scikit-learn.org/stable/modules/clustering.html) | Core | Guide |
| C06 | [Selecting the Number of Clusters with Silhouette Analysis](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_silhouette_analysis.html) | Core | Guide |
| C07 | [PyMC-Marketing: CLV Quickstart](https://www.pymc-marketing.io/en/latest/notebooks/clv/clv_quickstart.html) | Core | Guide |
| C08 | [PyMC-Marketing: Gamma-Gamma Model](https://www.pymc-marketing.io/en/latest/notebooks/clv/gamma_gamma.html) | Reference | Guide |
| C09 | [Bruce Hardie: Research Notes](https://www.brucehardie.com/notes/) | Reference | Author research collection |
| C10 | [lifetimes Repository](https://github.com/CamDavidsonPilon/lifetimes) | Optional | Archived code repository |
| C11 | [Counting Your Customers the Easy Way: An Alternative to the Pareto/NBD Model](https://www.brucehardie.com/papers/018/) | Reference | Research paper |
| C12 | [Interpreting the Results of Conjoint Analysis](https://content.sawtoothsoftware.com/assets/3501e79f-3a9f-4d99-a0f5-1522525e7f3f) | Core | Research paper |

Core identifies candidates for the eventual required readings. Reference material supports exercises and troubleshooting. Optional material supports extensions. Instructor material informs teaching and assessment; these labels are recommendations, not a finalized syllabus.

## Annotated Resources

### C01. Academic Teaching Resources for Conjoint Analysis

**Source:** Sawtooth Software. [Open Resource](https://sawtoothsoftware.com/academics/teaching-resources). **Priority:** Core. **Syllabus:** M4.

Structured conjoint curricula, readings, examples, and exercises.

**Teaching Use:** Use the text-based introductory materials to frame product-design and pricing decisions.

**Conditions and Adaptation:** Some resources include videos or vendor software; select readings and exercises.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### C02. Discrete Choice Methods with Simulation, Second Edition

**Source:** Kenneth Train. [Open Resource](https://eml.berkeley.edu/books/choice2.html). **Priority:** Reference. **Syllabus:** M4.

Utility, logit models, heterogeneity, and simulation.

**Teaching Use:** Use chapters 2-3 to clarify the interpretation and limitations of choice probabilities.

**Conditions and Adaptation:** Technical reading for instructor or advanced students; electronic edition is restricted to personal research and study.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Personal research and study only per author site; link rather than republish.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### C03. PyMC-Marketing: Multinomial Logit

**Source:** PyMC Labs and contributors. [Open Resource](https://www.pymc-marketing.io/en/latest/notebooks/customer_choice/mnl_logit.html). **Priority:** Optional. **Syllabus:** M4.

Python implementation of product-choice models.

**Teaching Use:** Build a small product-choice exercise and compare predicted shares when an attribute changes.

**Conditions and Adaptation:** Bayesian estimation is an extension; begin with utility and choice probabilities.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Downloaded repository LICENSE: Apache-2.0. Retain attribution and notices; check separate dataset and third-party content terms.

**Local Files:**

- [Source_Notebooks/Choice/LICENSE](Source_Notebooks/Choice/LICENSE)
- [Source_Notebooks/Choice/docs/source/notebooks/customer_choice/mnl_logit.ipynb](Source_Notebooks/Choice/docs/source/notebooks/customer_choice/mnl_logit.ipynb)
- [Source_Notebooks/Choice/data/choice_wide_heating.csv](Source_Notebooks/Choice/data/choice_wide_heating.csv)
- [Source_Notebooks/Choice/data/choice_crackers.csv](Source_Notebooks/Choice/data/choice_crackers.csv)

**Verification:** Source URL retrieved successfully on October 23, 2026.

### C04. Market Segmentation Analysis: Understanding It, Doing It, and Making It Useful

**Source:** Sara Dolnicar, Bettina Grün, and Friedrich Leisch. [Open Resource](https://link.springer.com/book/10.1007/978-981-10-8818-6). **Priority:** Core. **Syllabus:** M4.

Selecting segmentation variables, assessing solutions, and managerial implementation.

**Teaching Use:** Require students to explain why segments would support a feasible marketing decision.

**Conditions and Adaptation:** Examples use R; translate selected exercises into Python with checked results.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Book published CC BY 4.0; retain attribution and check individual third-party content.

**Local Files:**

- [Books/Dolnicar_Grun_Leisch_Springer2018.pdf](Books/Dolnicar_Grun_Leisch_Springer2018.pdf)

**Verification:** Source URL retrieved successfully on October 23, 2026.

### C05. scikit-learn: Clustering

**Source:** scikit-learn contributors. [Open Resource](https://scikit-learn.org/stable/modules/clustering.html). **Priority:** Core. **Syllabus:** M4.

Clustering methods and their assumptions.

**Teaching Use:** Compare scaled and unscaled customer segmentation and interpret the differences.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### C06. Selecting the Number of Clusters with Silhouette Analysis

**Source:** scikit-learn contributors. [Open Resource](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_silhouette_analysis.html). **Priority:** Core. **Syllabus:** M4.

Silhouette plots and alternative cluster counts.

**Teaching Use:** Assess numerical separation alongside stability and managerial usefulness.

**Conditions and Adaptation:** A favorable silhouette score does not establish an economically useful segmentation.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### C07. PyMC-Marketing: CLV Quickstart

**Source:** PyMC Labs and contributors. [Open Resource](https://www.pymc-marketing.io/en/latest/notebooks/clv/clv_quickstart.html). **Priority:** Core. **Syllabus:** M4.

Customer purchase histories, repeat purchasing, and model-based CLV.

**Teaching Use:** Compare a simple RFM baseline with predictions based on frequency, recency, and observation time.

**Conditions and Adaptation:** State contractual versus noncontractual setting and the observation and prediction horizons. Upstream notebook reads a remote main-branch CSV; a pinned local copy is included.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Downloaded repository LICENSE: Apache-2.0. Retain attribution and notices; check separate dataset and third-party content terms.

**Local Files:**

- [Source_Notebooks/CLV/LICENSE](Source_Notebooks/CLV/LICENSE)
- [Source_Notebooks/CLV/docs/source/notebooks/clv/clv_quickstart.ipynb](Source_Notebooks/CLV/docs/source/notebooks/clv/clv_quickstart.ipynb)
- [Source_Notebooks/CLV/data/clv_quickstart.csv](Source_Notebooks/CLV/data/clv_quickstart.csv)
- [Source_Notebooks/CLV/data/cdnow_transactions.csv](Source_Notebooks/CLV/data/cdnow_transactions.csv)

**Verification:** Source URL retrieved successfully on October 23, 2026.

### C08. PyMC-Marketing: Gamma-Gamma Model

**Source:** PyMC Labs and contributors. [Open Resource](https://www.pymc-marketing.io/en/latest/notebooks/clv/gamma_gamma.html). **Priority:** Reference. **Syllabus:** M4.

Modeling customer monetary value for CLV calculations.

**Teaching Use:** Examine whether monetary-value and purchase-frequency assumptions suit the chosen dataset.

**Conditions and Adaptation:** Revenue predictions require margins, discounting, and costs before becoming profit-based CLV. Upstream notebook reads a remote main-branch CSV; a pinned local copy is included.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Downloaded repository LICENSE: Apache-2.0. Retain attribution and notices; check separate dataset and third-party content terms.

**Local Files:**

- [Source_Notebooks/Monetary_Value/LICENSE](Source_Notebooks/Monetary_Value/LICENSE)
- [Source_Notebooks/Monetary_Value/docs/source/notebooks/clv/gamma_gamma.ipynb](Source_Notebooks/Monetary_Value/docs/source/notebooks/clv/gamma_gamma.ipynb)
- [Source_Notebooks/Monetary_Value/data/cdnow_transactions.csv](Source_Notebooks/Monetary_Value/data/cdnow_transactions.csv)
- [Source_Notebooks/Monetary_Value/data/clv_quickstart.csv](Source_Notebooks/Monetary_Value/data/clv_quickstart.csv)

**Verification:** Source URL retrieved successfully on October 23, 2026.

### C09. Bruce Hardie: Research Notes

**Source:** Bruce G. S. Hardie and coauthors. [Open Resource](https://www.brucehardie.com/notes/). **Priority:** Reference. **Syllabus:** M4.

Technical notes on customer-base analysis, retention, and lifetime value.

**Teaching Use:** Use the relevant note to explain model assumptions behind package outputs.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### C10. lifetimes Repository

**Source:** Cam Davidson-Pilon and contributors. [Open Resource](https://github.com/CamDavidsonPilon/lifetimes). **Priority:** Optional. **Syllabus:** M4.

Widely used historical Python implementation of customer-base models.

**Teaching Use:** Use for understanding legacy CLV examples and migration comparisons.

**Conditions and Adaptation:** Archived project; prefer maintained PyMC-Marketing examples for new teaching code.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### C11. Counting Your Customers the Easy Way: An Alternative to the Pareto/NBD Model

**Source:** Peter S. Fader, Bruce G. S. Hardie, and Ka Lok Lee. [Open Resource](https://www.brucehardie.com/papers/018/). **Priority:** Reference. **Syllabus:** M4.

The behavioral foundation of the BG/NBD model.

**Teaching Use:** Explain how purchase and dropout assumptions produce repeat-purchase predictions.

**Conditions and Adaptation:** Use the paper to interpret the model; parameter estimates are conditional on its assumptions.

**Access and Reuse:** Public landing page; consult linked full-text availability. Link to source; public redistribution not cleared.

**Local Files:**

- [Papers/Fader_Hardie_Lee_MarketingScience2005.pdf](Papers/Fader_Hardie_Lee_MarketingScience2005.pdf)

**Verification:** Source URL retrieved successfully on October 23, 2026.

### C12. Interpreting the Results of Conjoint Analysis

**Source:** Bryan Orme / Sawtooth Software. [Open Resource](https://content.sawtoothsoftware.com/assets/3501e79f-3a9f-4d99-a0f5-1522525e7f3f). **Priority:** Core. **Syllabus:** M4.

Part-worth utilities, attribute importance, and market simulations.

**Teaching Use:** Translate conjoint output into product comparisons and state the simulated competitive set.

**Conditions and Adaptation:** Preference shares depend on the modeled choice set and are not automatically observed market shares.

**Access and Reuse:** Public landing page; consult linked full-text availability. Link to source; public redistribution not cleared.

**Local Files:**

- [Papers/Orme_ResearchPublishers2019.pdf](Papers/Orme_ResearchPublishers2019.pdf)

**Verification:** Source URL retrieved successfully on October 23, 2026.
