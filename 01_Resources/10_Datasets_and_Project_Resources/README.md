# Datasets and Project Resources

Updated October 23, 2026. 9 curated resources. [Master Guide](../README.md).

The five UCI archives and extracted contents are saved locally. Larger, restricted, or registration-dependent sources remain linked. Matching a dataset to a method requires checking its unit, timing, outcome, and data-generating process.

## Reading Guide

| ID | Resource | Priority | Format |
| --- | --- | --- | --- |
| D01 | [UCI Online Retail](https://archive.ics.uci.edu/dataset/352/online+retail) | Core | Dataset |
| D02 | [UCI Bank Marketing](https://archive.ics.uci.edu/dataset/222/bank+marketing) | Core | Dataset |
| D03 | [UCI Online Shoppers Purchasing Intention](https://archive.ics.uci.edu/dataset/468/online+shoppers+purchasing+intention+dataset) | Core | Dataset |
| D04 | [UCI Sentiment Labelled Sentences](https://archive.ics.uci.edu/dataset/331/sentiment+labelled+sentences) | Core | Dataset |
| D05 | [MovieLens Datasets](https://lenskit.grouplens.org/datasets/movielens/) | Optional | Dataset collection |
| D06 | [Criteo Uplift Prediction Dataset](https://ailab.criteo.com/criteo-uplift-prediction-dataset/) | Optional | Dataset |
| D07 | [Amazon Reviews 2023](https://amazon-reviews-2023.github.io/) | Optional | Dataset collection |
| D08 | [dunnhumby Source Files](https://www.dunnhumby.com/source-files/) | Optional | Dataset portal |
| D09 | [UCI Wholesale Customers](https://archive.ics.uci.edu/dataset/292/wholesale+customers) | Core | Dataset |

Core identifies candidates for the eventual required readings. Reference material supports exercises and troubleshooting. Optional material supports extensions. Instructor material informs teaching and assessment; these labels are recommendations, not a finalized syllabus.

## Annotated Resources

### D01. UCI Online Retail

**Source:** Daqing Chen / UCI. [Open Resource](https://archive.ics.uci.edu/dataset/352/online+retail). **Priority:** Core. **Syllabus:** M2; M4; M7.

Invoice-line transactions for customer and retail analysis.

**Teaching Use:** Support cleaning, revenue visualization, RFM segmentation, repeat purchasing, and time splits.

**Conditions and Adaptation:** Cancellations, missing customer identifiers, and nonpositive quantities/prices need explicit rules. Observational data.

**Access and Reuse:** Public web resource; linked services may require an account or payment. CC BY 4.0 on UCI landing page; retain creator and DOI attribution.

**Local Files:**

- [Data/D01/online_retail.zip](Data/D01/online_retail.zip)
- [Data/D01/Extracted/Online Retail.xlsx](Data/D01/Extracted/Online%20Retail.xlsx)

**Verification:** Source URL retrieved successfully on October 23, 2026.

### D02. UCI Bank Marketing

**Source:** Sérgio Moro, Paulo Rita, and Paulo Cortez / UCI. [Open Resource](https://archive.ics.uci.edu/dataset/222/bank+marketing). **Priority:** Core. **Syllabus:** M3; M7.

Direct-marketing campaign records and subscription outcome.

**Teaching Use:** Compare logistic and tree-based response prediction with cost-sensitive thresholds.

**Conditions and Adaptation:** Call duration is unavailable before a call; exclude it for pre-call targeting. Campaign data do not identify the causal effect of contact.

**Access and Reuse:** Public web resource; linked services may require an account or payment. CC BY 4.0 on UCI landing page; retain source citation.

**Local Files:**

- [Data/D02/bank_marketing.zip](Data/D02/bank_marketing.zip)
- [Data/D02/Extracted/bank.zip](Data/D02/Extracted/bank.zip)
- [Data/D02/Extracted/bank/bank-full.csv](Data/D02/Extracted/bank/bank-full.csv)
- [Data/D02/Extracted/bank/bank-names.txt](Data/D02/Extracted/bank/bank-names.txt)
- [Data/D02/Extracted/bank/bank.csv](Data/D02/Extracted/bank/bank.csv)
- [Data/D02/Extracted/bank-additional.zip](Data/D02/Extracted/bank-additional.zip)
- [Data/D02/Extracted/bank-additional/bank-additional/.Rhistory](Data/D02/Extracted/bank-additional/bank-additional/.Rhistory)
- [Data/D02/Extracted/bank-additional/bank-additional/bank-additional-full.csv](Data/D02/Extracted/bank-additional/bank-additional/bank-additional-full.csv)
- [Data/D02/Extracted/bank-additional/bank-additional/bank-additional-names.txt](Data/D02/Extracted/bank-additional/bank-additional/bank-additional-names.txt)
- [Data/D02/Extracted/bank-additional/bank-additional/bank-additional.csv](Data/D02/Extracted/bank-additional/bank-additional/bank-additional.csv)

**Verification:** Source URL retrieved successfully on October 23, 2026.

### D03. UCI Online Shoppers Purchasing Intention

**Source:** C. Sakar and Yomi Kastro / UCI. [Open Resource](https://archive.ics.uci.edu/dataset/468/online+shoppers+purchasing+intention+dataset). **Priority:** Core. **Syllabus:** M2; M7.

Web-session features and purchase outcome.

**Teaching Use:** Predict conversion with an explicit point in the session when the prediction would be made.

**Conditions and Adaptation:** Some features are only known late in a session; availability must match the intended decision.

**Access and Reuse:** Public web resource; linked services may require an account or payment. CC BY 4.0 on UCI landing page; retain source citation.

**Local Files:**

- [Data/D03/online_shoppers_purchasing_intention_dataset.zip](Data/D03/online_shoppers_purchasing_intention_dataset.zip)
- [Data/D03/Extracted/online_shoppers_intention.csv](Data/D03/Extracted/online_shoppers_intention.csv)

**Verification:** Source URL retrieved successfully on October 23, 2026.

### D04. UCI Sentiment Labelled Sentences

**Source:** Dimitrios Kotzias / UCI. [Open Resource](https://archive.ics.uci.edu/dataset/331/sentiment+labelled+sentences). **Priority:** Core. **Syllabus:** M5; M7.

Small labeled sentences from product, restaurant, and movie reviews.

**Teaching Use:** Compare a lexicon baseline, TF-IDF classifier, and optional LLM labels.

**Conditions and Adaptation:** Small balanced benchmark; evaluate domain transfer separately from random splits.

**Access and Reuse:** Public web resource; linked services may require an account or payment. CC BY 4.0 on UCI landing page; retain source citation and original attribution.

**Local Files:**

- [Data/D04/sentiment_labelled_sentences.zip](Data/D04/sentiment_labelled_sentences.zip)
- [Data/D04/Extracted/sentiment labelled sentences/amazon_cells_labelled.txt](Data/D04/Extracted/sentiment%20labelled%20sentences/amazon_cells_labelled.txt)
- [Data/D04/Extracted/sentiment labelled sentences/imdb_labelled.txt](Data/D04/Extracted/sentiment%20labelled%20sentences/imdb_labelled.txt)
- [Data/D04/Extracted/sentiment labelled sentences/readme.txt](Data/D04/Extracted/sentiment%20labelled%20sentences/readme.txt)
- [Data/D04/Extracted/sentiment labelled sentences/yelp_labelled.txt](Data/D04/Extracted/sentiment%20labelled%20sentences/yelp_labelled.txt)

**Verification:** Source URL retrieved successfully on October 23, 2026.

### D05. MovieLens Datasets

**Source:** GroupLens Research. [Open Resource](https://lenskit.grouplens.org/datasets/movielens/). **Priority:** Optional. **Syllabus:** M8.

Ratings and movie metadata for recommendation exercises.

**Teaching Use:** Use the small dataset for ranking and recommendation evaluation.

**Conditions and Adaptation:** Dataset has specific research-use terms and redistribution conditions; link students to original download.

**Access and Reuse:** Search-indexed official GroupLens page; direct retrieval timed out. Dataset use is subject to the linked README terms. Custom GroupLens terms; public redistribution not cleared.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Direct retrieval incomplete: <urlopen error timed out>. Retained as an optional/reference lead; check access before assigning.

### D06. Criteo Uplift Prediction Dataset

**Source:** Criteo AI Lab. [Open Resource](https://ailab.criteo.com/criteo-uplift-prediction-dataset/). **Priority:** Optional. **Syllabus:** M6; M7; M8.

Advertising incrementality-test data for uplift modeling.

**Teaching Use:** Compare purchase propensity and incremental response for a targeting extension.

**Conditions and Adaptation:** Large dataset; nonuniform subsampling prevents recovery of original incrementality levels. Do not report original campaign ROI.

**Access and Reuse:** Public web resource; linked services may require an account or payment. CC BY-NC-SA 4.0 terms on source page; no bulk download in this collection.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### D07. Amazon Reviews 2023

**Source:** McAuley Lab, UC San Diego. [Open Resource](https://amazon-reviews-2023.github.io/). **Priority:** Optional. **Syllabus:** M5; M8.

Large review and product-metadata collection.

**Teaching Use:** Select a documented small subset for an advanced text or recommendation project.

**Conditions and Adaptation:** Large downloads, user-generated text, and source terms require review before use or redistribution.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### D08. dunnhumby Source Files

**Source:** dunnhumby. [Open Resource](https://www.dunnhumby.com/source-files/). **Priority:** Optional. **Syllabus:** M2; M4; M8.

Retail research data and accompanying documentation.

**Teaching Use:** Consider as an advanced household purchase or promotion-analysis project source.

**Conditions and Adaptation:** Access conditions and file availability must be checked; no registration or agreement was submitted.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### D09. UCI Wholesale Customers

**Source:** Margarida Cardoso / UCI. [Open Resource](https://archive.ics.uci.edu/dataset/292/wholesale+customers). **Priority:** Core. **Syllabus:** M2; M4.

Customer spending across wholesale product categories.

**Teaching Use:** Build a small segmentation exercise suitable for lightweight computation.

**Conditions and Adaptation:** No transaction sequence or retention outcome; unsuitable for direct lifetime-value estimation.

**Access and Reuse:** Public web resource; linked services may require an account or payment. CC BY 4.0 on UCI landing page; retain source citation.

**Local Files:**

- [Data/D09/wholesale_customers.zip](Data/D09/wholesale_customers.zip)
- [Data/D09/Extracted/Wholesale customers data.csv](Data/D09/Extracted/Wholesale%20customers%20data.csv)

**Verification:** Source URL retrieved successfully on October 23, 2026.

## Dataset Selection

- [Dataset Guide and Project Options](Dataset_Guide/README.md)
