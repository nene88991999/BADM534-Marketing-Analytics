# Text, Social Media, and Network Analysis

Updated October 23, 2026. 9 curated resources. [Master Guide](../README.md).

Use a transparent baseline and a small manually labeled evaluation set before adding embeddings or LLMs. Networks are an optional extension from the syllabus introduction; the dated schedule emphasizes text analysis.

## Reading Guide

| ID | Resource | Priority | Format |
| --- | --- | --- | --- |
| X01 | [Natural Language Processing with Python](https://www.nltk.org/book/) | Core | Open web book |
| X02 | [scikit-learn: Text Feature Extraction](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction) | Core | Guide |
| X03 | [VADER Sentiment Analysis](https://github.com/cjhutto/vaderSentiment) | Core | Code and research repository |
| X04 | [spaCy 101](https://spacy.io/usage/spacy-101) | Reference | Guide |
| X05 | [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/en/chapter1/1) | Optional | Text course |
| X06 | [Sentence Transformers Quickstart](https://sbert.net/docs/quickstart.html) | Optional | Guide |
| X07 | [BERTopic Documentation](https://maartengr.github.io/BERTopic/) | Optional | Guide |
| X08 | [NetworkX Tutorial](https://networkx.org/documentation/stable/tutorial.html) | Reference | Guide |
| X09 | [Supervised Machine Learning for Text Analysis in R](https://smltar.com/) | Reference | Open web book |

Core identifies candidates for the eventual required readings. Reference material supports exercises and troubleshooting. Optional material supports extensions. Instructor material informs teaching and assessment; these labels are recommendations, not a finalized syllabus.

## Annotated Resources

### X01. Natural Language Processing with Python

**Source:** Steven Bird, Ewan Klein, and Edward Loper. [Open Resource](https://www.nltk.org/book/). **Priority:** Core. **Syllabus:** M5.

Text representation, tokenization, classification, and linguistic structure.

**Teaching Use:** Introduce a transparent text-processing baseline before modern language models.

**Conditions and Adaptation:** Some examples are older; verify current Python and NLTK behavior.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### X02. scikit-learn: Text Feature Extraction

**Source:** scikit-learn contributors. [Open Resource](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction). **Priority:** Core. **Syllabus:** M5.

Bag of words, n-grams, TF-IDF, and feature representations.

**Teaching Use:** Build a review classifier with vectorization learned inside the training pipeline.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### X03. VADER Sentiment Analysis

**Source:** C. J. Hutto and collaborators. [Open Resource](https://github.com/cjhutto/vaderSentiment). **Priority:** Core. **Syllabus:** M5.

A lexicon and rule-based sentiment baseline for social text.

**Teaching Use:** Manually label a small sample of reviews and examine disagreements with VADER.

**Conditions and Adaptation:** Sarcasm, domain vocabulary, and multilingual content require separate validation.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### X04. spaCy 101

**Source:** Explosion and spaCy contributors. [Open Resource](https://spacy.io/usage/spacy-101). **Priority:** Reference. **Syllabus:** M5.

Tokenization, linguistic annotation, entities, and text pipelines.

**Teaching Use:** Extract product or organization mentions and evaluate errors on manually checked examples.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### X05. Hugging Face LLM Course

**Source:** Hugging Face. [Open Resource](https://huggingface.co/learn/llm-course/en/chapter1/1). **Priority:** Optional. **Syllabus:** M5.

Transformers, language models, datasets, and evaluation.

**Teaching Use:** Select the text sections on pipelines and text classification.

**Conditions and Adaptation:** Full course is more advanced than an introductory marketing analytics module.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### X06. Sentence Transformers Quickstart

**Source:** Sentence Transformers contributors. [Open Resource](https://sbert.net/docs/quickstart.html). **Priority:** Optional. **Syllabus:** M5.

Sentence embeddings and semantic similarity.

**Teaching Use:** Cluster product reviews by semantic similarity and manually inspect the resulting themes.

**Conditions and Adaptation:** Model downloads and compute requirements may be unsuitable for a browser-only exercise.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### X07. BERTopic Documentation

**Source:** Maarten Grootendorst and contributors. [Open Resource](https://maartengr.github.io/BERTopic/). **Priority:** Optional. **Syllabus:** M5.

Topic modeling using embeddings, clustering, and term representations.

**Teaching Use:** Compare generated topic labels with representative reviews and a simpler TF-IDF baseline.

**Conditions and Adaptation:** Topic stability and interpretation need assessment; topics are not established customer segments.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### X08. NetworkX Tutorial

**Source:** NetworkX contributors. [Open Resource](https://networkx.org/documentation/stable/tutorial.html). **Priority:** Reference. **Syllabus:** M5.

Networks, nodes, edges, graph construction, and basic calculations.

**Teaching Use:** Explore a small customer-referral or product co-purchase network.

**Conditions and Adaptation:** A network association alone does not establish peer influence.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### X09. Supervised Machine Learning for Text Analysis in R

**Source:** Emil Hvitfeldt and Julia Silge. [Open Resource](https://smltar.com/). **Priority:** Reference. **Syllabus:** M5.

Text preprocessing, representation, model evaluation, and interpretation.

**Teaching Use:** Use explanations of leakage and text evaluation when designing Python labs.

**Conditions and Adaptation:** R examples are supplementary; the main course remains Python.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.
