# M5 · Content Analysis, Text and Social Media

59 resources (18 core). Built 2026-10-23 from `00_Index/_data/`; edit the YAML there and rerun `00_Index/_build/build_catalog.py` rather than editing this file.

Priority: **core** = likely to assign or build on; **recommended** = strong supplement; **optional** = background or niche. *Access* tells you whether students can open it without a login.

## Contents

- [Text analysis in marketing: anchor papers](#text-analysis-in-marketing-anchor-papers) (15)
- [Python NLP toolkit](#python-nlp-toolkit) (10)
- [LLMs as annotators: methods and validation](#llms-as-annotators-methods-and-validation) (8)
- [Failure modes of LLM text analysis](#failure-modes-of-llm-text-analysis) (2)
- [Classifying text at scale with LLM APIs](#classifying-text-at-scale-with-llm-apis) (3)
- [Social media and reviews](#social-media-and-reviews) (11)
- [Network analysis and diffusion](#network-analysis-and-diffusion) (5)
- [Python for marketing analytics: notebooks and code](#python-for-marketing-analytics-notebooks-and-code) (5)

## Text analysis in marketing: anchor papers

- [core] **[Using natural language processing to analyse text data in behavioural science](https://www.nature.com/articles/s44159-024-00392-z)** (2025) — Feuerriegel, S.; Maarouf, A.; Bär, D.; Geißler, D.; Schweisthal, J.; Pröllochs, N.; Robertson, C. E.; Rathje, S.; Hartmann, J.; Mohammad, S. M.; Netzer, O.; Siegel, A. A.; Plank, B.; Van Bavel, J. J. *Nature Reviews Psychology*
  `paper` · `intermediate` · `access: open` · `AI angle`
  Review of the NLP pipeline for behavioral research, from dictionaries through supervised ML to LLMs. Discusses interpretability versus accuracy and gives recommendations for rigor and reproducibility.
  *Use in wiki:* Core modern overview reading that updates Berger et al. (2020) for the LLM era. Its pipeline figure can serve as the M5 roadmap.
  DOI [10.1038/s44159-024-00392-z](https://doi.org/10.1038/s44159-024-00392-z) · [Open-access copy](https://business.columbia.edu/sites/default/files-efs/citation_file_upload/NLP_paper.pdf)
  *Note:* Published online 4 Feb 2025; volume and pages not verified. Co-authors include marketing scholars Hartmann and Netzer. The open-access PDF is on the Columbia Business School site (seen in search).

- [core] **[Frontiers: Determining the Validity of Large Language Models for Automated Perceptual Analysis](https://doi.org/10.1287/mksc.2023.0454)** (2024) — Li, P.; Castelo, N.; Katona, Z.; Sarvary, M. *Marketing Science 43(2), 254-266*
  `paper` · `intermediate` · `access: library` · `AI angle`
  Tests whether LLM responses can stand in for survey respondents in perceptual mapping. LLM-based brand similarity and attribute ratings agree with human data over 75% of the time.
  *Use in wiki:* Bridge between M4 (perceptual maps) and M5: students ask an LLM for brand-similarity judgments and compare the result with a map built from review co-mentions.
  DOI [10.1287/mksc.2023.0454](https://doi.org/10.1287/mksc.2023.0454) · Tools: OpenAI API
  *Note:* Metadata from IDEAS/RePEc. INFORMS press release: https://www.informs.org/News-Room/INFORMS-Releases/News-Releases/Can-Large-Language-Models-Replace-Human-Participants-in-Some-Future-Market-Research (seen in search).

- [core] **[Sentiment Analysis in the Age of Generative AI](https://link.springer.com/doi/10.1007/s40547-024-00143-4)** (2024) — Krugmann, J. O.; Hartmann, J. *Customer Needs and Solutions 11, article 3*
  `paper` · `intro` · `access: open` · `AI angle`
  Compares zero-shot GPT-3.5, GPT-4 and Llama 2 with established transfer-learning sentiment models on marketing text. The LLMs often match or beat them, accuracy depends on data source and text features, and Llama 2 gives the most useful explanations.
  *Use in wiki:* Core, accessible reading for the 'LLM as sentiment classifier' lab. Students replicate a mini version (VADER vs. SiEBERT vs. an LLM API) on 200 hand-labeled reviews.
  DOI [10.1007/s40547-024-00143-4](https://doi.org/10.1007/s40547-024-00143-4) · Tools: OpenAI API, Llama, transformers
  *Note:* Open access; authors hold copyright.

- [core] **[More than a Feeling: Accuracy and Application of Sentiment Analysis](https://www.sciencedirect.com/science/article/pii/S0167811622000477)** (2023) — Hartmann, J.; Heitmann, M.; Siebert, C.; Schamp, C. *International Journal of Research in Marketing 40(1), 75-87*
  `paper` · `intermediate` · `access: library`
  Shows that sentiment-method accuracy varies widely and that inaccurate sentiment scores can bias downstream marketing conclusions. Transfer learning (fine-tuned RoBERTa) performs best, and the authors release SiEBERT, a ready-to-use model.
  *Use in wiki:* Core reading for sentiment. The released SiEBERT model fits in a 3-line Colab demo, so students can compare it with VADER on the same reviews.
  DOI [10.1016/j.ijresmar.2022.05.005](https://doi.org/10.1016/j.ijresmar.2022.05.005) · Tools: transformers, SiEBERT
  *Note:* Model card: https://huggingface.co/siebert/sentiment-roberta-large-english (binary pos/neg; trained/evaluated on 15 datasets; license not stated on card). Usage: pipeline('sentiment-analysis', model='siebert/sentiment-roberta-large-english'). ScienceDirect blocked fetching, so the article's open-access status is unverified. Metadata confirmed on IDEAS and Univ. Hamburg page.

- [core] **[Uniting the Tribes: Using Text for Marketing Insight](https://doi.org/10.1177/0022242919873106)** (2020) — Berger, J.; Humphreys, A.; Ludwig, S.; Moe, W. W.; Netzer, O.; Schweidel, D. A. *Journal of Marketing 84(1), 1-25*
  `paper` · `intro` · `access: open`
  Framework paper on how marketers can extract insight from text: text as a reflection of producers versus an influence on audiences, plus a tour of methods from dictionaries to topic models and embeddings.
  *Use in wiki:* Assigned opening reading for M5. Its 'what text reflects vs. what text affects' framing can organize the module page.
  DOI [10.1177/0022242919873106](https://doi.org/10.1177/0022242919873106) · [Open-access copy](https://business.columbia.edu/sites/default/files-efs/pubfiles/26260/uniting%20the%20tribes.pdf) · Tools: LIWC, topic models, word embeddings
  *Note:* Citation and DOI confirmed on the AMA press release page. The open PDF is on Columbia's site. Won the 2025 Sheth Foundation/JM Award (per an AMA press-release title seen in search).

- [core] **[What Makes Online Content Viral?](https://doi.org/10.1509/jmr.10.0353)** (2012) — Berger, J.; Milkman, K. L. *Journal of Marketing Research 49(2), 192–205*
  `paper` · `intermediate` · `access: library`
  Codes about 7,000 New York Times articles for emotion with automated sentiment tools and human raters, then models which ones reach the most-emailed list. High-arousal emotions (awe, anger, anxiety) drive sharing more than positivity alone.
  *Use in wiki:* Classic M5 example of turning text into variables and regressing an outcome on them. Students can replicate the logic with LLM-coded emotions on the MBA 542 Substack dataset.
  DOI [10.1509/jmr.10.0353](https://doi.org/10.1509/jmr.10.0353) · [Open-access copy](https://faculty.wharton.upenn.edu/wp-content/uploads/2011/11/Virality.pdf) · Tools: VADER, statsmodels
  *Note:* Also on the MBA 542 Module 2 reading list.

- [recommended] **[Text as Data: A New Framework for Machine Learning and the Social Sciences](https://press.princeton.edu/books/paperback/9780691207551/text-as-data)** (2022) — Grimmer, J.; Roberts, M. E.; Stewart, B. M. *Princeton University Press*
  `book` · `intermediate` · `access: library`
  Research-design-first textbook organized around representation, discovery, measurement, prediction and causal inference with text.
  *Use in wiki:* Instructor backbone for structuring M5 (discovery vs. measurement vs. prediction). Assign selected chapters, e.g., on validation, through the library.
  *Note:* Paid ($49.95 paperback; ebook formats). No free full text was verified, so check the UIUC library for e-book access.

- [recommended] **[Happiness Begets Money: Emotion and Engagement in Live Streaming](https://journals.sagepub.com/doi/10.1177/00222437211002477)** (2021) — Lin, Y.; Yao, D.; Chen, X. *Journal of Marketing Research 58(3), 417–438*
  `paper` · `advanced` · `access: library`
  Uses deep-learning facial-emotion detection on live-stream video to show that broadcaster happiness raises viewer engagement and tipping.
  *Use in wiki:* Shows content analysis extending beyond text to video and emotion signals; a good 'where this is heading' reading for M5.
  DOI [10.1177/00222437211002477](https://doi.org/10.1177/00222437211002477)
  *Note:* Also on the MBA 542 Module 3 reading list.

- [recommended] **[Visual Listening In: Extracting Brand Image Portrayed on Social Media](https://pubsonline.informs.org/doi/fpi/10.1287/mksc.2020.1226)** (2020) — Liu, L.; Dzyabura, D.; Mizik, N. *Marketing Science 39(4), 669–686*
  `paper` · `advanced` · `access: library`
  Trains image classifiers on consumer-posted Instagram photos to measure how brands are portrayed on attributes such as glamorous or rugged, and validates the measures against survey-based brand perceptions.
  *Use in wiki:* Anchor for extending M5 content analysis from text to images; pairs with today's multimodal LLMs as a cheaper labelling route.
  DOI [10.1287/mksc.2020.1226](https://doi.org/10.1287/mksc.2020.1226) · [Open-access copy](https://www.nes.ru/files/Preprints-resh/WP258.pdf)
  *Note:* Also on the MBA 542 Module 6 (visual listening) reading list. The open-access link is a working-paper version.

- [recommended] **[Comparing automated text classification methods](https://doi.org/10.1016/j.ijresmar.2018.09.009)** (2019) — Hartmann, J.; Huppertz, J.; Schamp, C.; Heitmann, M. *International Journal of Research in Marketing 36(1), 20-38*
  `paper` · `intermediate` · `access: open` · `CC BY-NC-ND (publisher version, per University of Groningen repository)`
  Benchmarks lexicon methods against machine-learning classifiers (random forests, SVM, naive Bayes, neural nets and others) across dozens of social media and review datasets, and gives guidance on which to use when.
  *Use in wiki:* Reading behind a 'dictionary vs. ML classifier' in-class comparison. Students can rerun a mini version with scikit-learn on Yelp or Amazon reviews.
  DOI [10.1016/j.ijresmar.2018.09.009](https://doi.org/10.1016/j.ijresmar.2018.09.009) · [Open-access copy](https://research.rug.nl/files/202561216/1_s2.0_S0167811618300545_main.pdf) · Tools: scikit-learn
  *Note:* Pre-LLM benchmark. Pair it with Hartmann et al. (2023) and Krugmann & Hartmann (2024) to show how the ranking of methods changed.

- [recommended] **[Identifying Customer Needs from User-Generated Content](https://doi.org/10.1287/mksc.2018.1123)** (2019) — Timoshenko, A.; Hauser, J. R. *Marketing Science 38(1)*
  `paper` · `intermediate` · `access: open` · `CC BY-NC-SA 4.0 (author's final manuscript on MIT DSpace)`
  Uses a CNN to filter non-informative review sentences and embeddings to cluster the rest, so human analysts can find customer needs in Amazon reviews more efficiently. UGC proves at least as rich a source of needs as interviews.
  *Use in wiki:* Case example on human-machine workflows. A natural team-project template: filter reviews with embeddings or an LLM, then have humans code needs.
  DOI [10.1287/mksc.2018.1123](https://doi.org/10.1287/mksc.2018.1123) · [Open-access copy](https://dspace.mit.edu/handle/1721.1/124203) · Tools: word embeddings, CNN
  *Note:* Plain-language summary for students: https://insight.kellogg.northwestern.edu/article/how-companies-can-mine-online-reviews-for-product-development-gold (seen in search). An updated LLM version of this workflow would make a good team project.

- [recommended] **[Automated Text Analysis for Consumer Research](https://doi.org/10.1093/jcr/ucx104)** (2018) — Humphreys, A.; Wang, R. J.-H. *Journal of Consumer Research 44(6), 1274-1306*
  `paper` · `intermediate` · `access: library`
  A step-by-step methodological guide to dictionary-based and other automated text analysis for consumer research: building constructs, operationalizing them, and checking validity.
  *Use in wiki:* Background reading on construct validity for dictionary methods. Its stages (question, data, construct, operationalization, validation) can be reused as a checklist for team projects.
  DOI [10.1093/jcr/ucx104](https://doi.org/10.1093/jcr/ucx104) · Tools: LIWC
  *Note:* Metadata from IDEAS/RePEc. Full text is subscriber-only, so use UIUC library access. LIWC-22, the commercial dictionary tool used in much of this work, is at https://www.liwc.app/ (paid; Python/R integration mentioned).

- [recommended] **[Mining Marketing Meaning from Online Chatter: Strategic Brand Analysis of Big Data Using Latent Dirichlet Allocation](https://doi.org/10.1509/jmr.12.0106)** (2014) — Tirunillai, S.; Tellis, G. J. *Journal of Marketing Research 51(4), 463-479*
  `paper` · `intermediate` · `access: library`
  Applies LDA to product reviews to extract quality dimensions and their valence, and tracks brand positions on those dimensions over time.
  *Use in wiki:* Anchor reading for the topic-modeling lesson. Students run gensim LDA or BERTopic on Amazon Reviews 2023 and compare their output with the paper's quality dimensions.
  DOI [10.1509/jmr.12.0106](https://doi.org/10.1509/jmr.12.0106) · Tools: gensim
  *Note:* DOI metadata confirmed via Crossref.

- [recommended] **[Mine Your Own Business: Market-Structure Surveillance Through Text Mining](https://doi.org/10.1287/mksc.1120.0713)** (2012) — Netzer, O.; Feldman, R.; Goldenberg, J.; Fresko, M. *Marketing Science 31(3), 521-543*
  `paper` · `advanced` · `access: library`
  Mines forum posts for brand co-mentions to build perceptual and market-structure maps, then compares them with survey and sales-based maps.
  *Use in wiki:* Case example linking text to M4 perceptual mapping. Students can replicate a simple brand co-occurrence network from Reddit or review text.
  DOI [10.1287/mksc.1120.0713](https://doi.org/10.1287/mksc.1120.0713) · Tools: NetworkX
  *Note:* Metadata from IDEAS/RePEc. A natural bridge to the network-analysis part of M5 (co-mention networks).

- [optional] **[Text as Data](https://doi.org/10.1257/jel.20181020)** (2019) — Gentzkow, M.; Kelly, B.; Taddy, M. *Journal of Economic Literature 57(3), 535-574*
  `paper` · `advanced` · `access: library`
  Economics survey of representing text numerically (document-term matrices), dictionary methods, penalized regression, topic models and word embeddings, with applications.
  *Use in wiki:* Instructor-only background for the 'text to numbers' lecture. Optional reading for students who want more depth.
  DOI [10.1257/jel.20181020](https://doi.org/10.1257/jel.20181020)
  *Note:* DOI metadata confirmed via Crossref. Predates LLMs. For a more recent econ survey see Ash & Hansen (2023), 'Text Algorithms in Economics', Annual Review of Economics 15:659-688, doi 10.1146/annurev-economics-082222-074352 (Crossref-verified).

## Python NLP toolkit

- [core] **[Transformers Pipelines documentation (text-classification, zero-shot-classification)](https://huggingface.co/docs/transformers/main_classes/pipelines)** (2026) — Hugging Face. *Hugging Face Transformers docs*
  `documentation` · `intro` · `access: open`
  Reference for pipeline(), the one-line way to run pretrained models for sentiment, text classification, zero-shot classification and more, with batching and GPU options.
  *Use in wiki:* Code reference for the sentiment lab. Students run pipeline('sentiment-analysis', model=...) on reviews and tweets in Colab.
  Tools: transformers
  *Note:* Good social-media model: https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest (RoBERTa trained on about 124M tweets and fine-tuned on TweetEval; neg/neu/pos labels; CC-BY-4.0; fetched). For few-label fine-tuning see SetFit (Apache-2.0): https://github.com/huggingface/setfit (fetched).

- [core] **[Working With Text Data (scikit-learn tutorial)](https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html)** (2026) — scikit-learn developers. *scikit-learn documentation*
  `tutorial` · `intro` · `access: open`
  Official tutorial on bag-of-words with CountVectorizer, TF-IDF weighting, naive Bayes and linear SVM in a Pipeline, evaluation with classification reports and confusion matrices, and grid search, using 20 Newsgroups.
  *Use in wiki:* Template for the in-class TF-IDF classifier activity. Students swap 20 Newsgroups for Yelp star ratings and use an AI assistant to adapt the code.
  Tools: scikit-learn
  *Note:* Living documentation; the year is the current docs version. Its exercises include movie-review sentiment and language identification.

- [core] **[Hands-On Large Language Models (official code repository)](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models)** (2024) — Alammar, J.; Grootendorst, M. *GitHub (companion to O'Reilly book)*
  `notebook` · `intermediate` · `access: open` · `Apache-2.0` · `AI angle`
  Colab-ready notebooks for the book's 12 chapters, including Ch. 4 Text Classification (pretrained, embedding-based and generative/prompted approaches), Ch. 5 Text Clustering and Topic Modeling (BERTopic), and Ch. 6 Prompt Engineering.
  *Use in wiki:* Embed or adapt Ch. 4-6 notebooks as M5 labs. They run on a free Colab T4 GPU and directly compare classic, embedding and LLM classifiers.
  Tools: transformers, sentence-transformers, bertopic, openai · Local copy: `05_M5_Text_and_Social_Media_Analytics/repos/HandsOnLLM__Hands-On-Large-Language-Models`
  *Note:* The book itself is paid (O'Reilly); the notebooks are free. Chapter folder names were not verified, so keep chapters 4-6. Year is approximate (book published 2024). Alternative: 'NLP with Transformers' notebooks (Apache-2.0), https://github.com/nlp-with-transformers/notebooks (fetched; some chapters no longer maintained).

- [core] **[BERTopic: Neural topic modeling with a class-based TF-IDF procedure](https://maartengr.github.io/BERTopic/index.html)** (2022) — Grootendorst, M. *Docs site + arXiv:2203.05794*
  `package` · `intermediate` · `access: open` · `MIT (per GitHub README badge)` · `AI angle`
  Modular topic modeling: sentence-transformer embeddings, UMAP, HDBSCAN, then c-TF-IDF topic descriptions. Supports dynamic and semi-supervised topics and LLM-generated topic labels, e.g., via OpenAI models.
  *Use in wiki:* Main topic-modeling tool for the course. The README's Colab 'Best Practices' notebook can be embedded as a starting lab, and the LLM labeling step shows the AI angle.
  Tools: bertopic, sentence-transformers, umap-learn, hdbscan
  *Note:* GitHub: https://github.com/MaartenGr/BERTopic (README links about 9 Colab notebooks, including LLM-based ones). The README license badge points to a different repo, so confirm the LICENSE file before redistributing.

- [core] **[VADER: A Parsimonious Rule-Based Model for Sentiment Analysis of Social Media Text (vaderSentiment)](https://github.com/cjhutto/vaderSentiment)** (2014) — Hutto, C. J.; Gilbert, E. *ICWSM 8(1), 216-225; GitHub*
  `package` · `intro` · `access: open` · `MIT`
  Lexicon- and rule-based sentiment scorer tuned for social media. It handles negation, intensifiers, punctuation, capitalization, emoticons and slang, and returns compound and pos/neu/neg scores.
  *Use in wiki:* First hands-on sentiment demo in Colab (pip install vaderSentiment). Serves as the baseline that transformer and LLM classifiers are compared against.
  DOI [10.1609/icwsm.v8i1.14550](https://doi.org/10.1609/icwsm.v8i1.14550) · Tools: vaderSentiment, nltk
  *Note:* The paper DOI was confirmed via Crossref. The repo includes the lexicon and the evaluation datasets.

- [recommended] **[LDA Model tutorial (Gensim)](https://radimrehurek.com/gensim/auto_examples/tutorials/run_lda.html)** (2026) — Řehůřek, R. and Gensim contributors. *Gensim documentation*
  `tutorial` · `intermediate` · `access: open` · `LGPL-2.1 (Gensim library, per GitHub)`
  End-to-end LDA on a 1,740-paper NIPS corpus: tokenizing, lemmatizing, bigrams, dictionary filtering, training, and UMass topic coherence.
  *Use in wiki:* Classic topic-model lab, paired with Tirunillai & Tellis (2014). Contrast it with BERTopic on the same review corpus.
  Tools: gensim, nltk
  *Note:* Gensim is in 'stable maintenance mode' (bug and doc fixes only), per its GitHub README: https://github.com/piskvorky/gensim.

- [recommended] **[Sentence Transformers (SBERT) documentation](https://sbert.net/)** (2026) — UKP Lab (TU Darmstadt); maintained by Aarsen, T. (Hugging Face). *sbert.net*
  `documentation` · `intermediate` · `access: open` · `Apache-2.0`
  Library and docs for computing sentence embeddings and rerankers. Covers semantic search, clustering, paraphrase mining and fine-tuning.
  *Use in wiki:* Use for an 'embeddings + k-means' lab that links M4 segmentation to text, e.g., clustering review sentences into customer-need themes.
  Tools: sentence-transformers
  *Note:* GitHub: https://github.com/huggingface/sentence-transformers (Apache-2.0).

- [recommended] **[Introduction to Cultural Analytics & Python](https://melaniewalsh.github.io/Intro-Cultural-Analytics/welcome.html)** (2021) — Walsh, M. *Jupyter Book (online)*
  `book` · `intro` · `access: open` · `CC BY-NC-SA 4.0 (book); GPL-3.0 (repo)`
  Open online textbook teaching Python to humanities and social science students with song lyrics, news, tweets and Reddit. Covers TF-IDF, sentiment, topic modeling, NER and POS tagging.
  *Use in wiki:* Gentle, non-CS-friendly chapters to link from the wiki. A good model for the wiki's own Jupyter Book-style design.
  Tools: pandas, scikit-learn, tomotopy
  *Note:* Year is approximate. Pages launch in Binder (Colab not mentioned). Some Twitter-collection chapters predate the X API changes. R alternative: Silge & Robinson, 'Text Mining with R: A Tidy Approach', https://www.tidytextmining.com/ (CC BY-NC-SA 3.0 US; fetched). Free course materials from ETH: Elliott Ash's 'NLP for Law and Social Science' repos, e.g. https://github.com/elliottash/nlp_lss_2023 (GPL-3.0; fetched).

- [recommended] **[Advanced NLP with spaCy (free online course)](https://course.spacy.io/en/)** (2020) — Montani, I. (Explosion). *course.spacy.io*
  `course` · `intermediate` · `access: open`
  Free interactive four-chapter course: finding words, phrases, names and concepts; large-scale data analysis; processing pipelines; and training a neural network model.
  *Use in wiki:* Self-paced lab for named-entity recognition (e.g., extracting brands and products from reviews). Link chapter 1-2 as optional homework.
  Tools: spacy
  *Note:* Year approximate, not stated on page. Source: https://github.com/ines/spacy-course (license not checked, so no download). For LLM-backed spaCy components see spacy-llm (MIT, marked experimental): https://github.com/explosion/spacy-llm (fetched).

- [recommended] **[Natural Language Processing with Python: Analyzing Text with the Natural Language Toolkit](https://www.nltk.org/book/)** (2009) — Bird, S.; Klein, E.; Loper, E. *nltk.org (online edition updated for Python 3 / NLTK 3)*
  `book` · `intro` · `access: open` · `CC BY-NC-ND 3.0 US`
  The free online NLTK book: tokenization, corpora, word frequencies, tagging, text classification and more, in 12 chapters.
  *Use in wiki:* Reference reading for the preprocessing lesson (chapters 1-3). Link specific sections rather than assigning the whole book.
  Tools: nltk
  *Note:* The original O'Reilly edition is from 2009 and the online edition was updated for Python 3. Some content is dated, but it remains the canonical NLTK reference. NLTK also bundles VADER (nltk.sentiment.vader).

## LLMs as annotators: methods and validation

- [core] **[Best Practices for Text Annotation with Large Language Models](https://sociologica.unibo.it/article/view/19461)** (2024) — Törnberg, P. *Sociologica 18(2), 67-85*
  `paper` · `intro` · `access: open` · `CC BY 4.0` · `AI angle`
  Practical guidelines for LLM-based text annotation: model choice, prompt design and iteration, stability testing, validation against human labels, transparency, and ethics.
  *Use in wiki:* Basis for an 'LLM annotation checklist' callout on the wiki and for the grading rubric of LLM-coded variables in team projects.
  DOI [10.6092/issn.1971-8853/19461](https://doi.org/10.6092/issn.1971-8853/19461) · [Open-access copy](https://www.arxiv.org/pdf/2402.05129)
  *Note:* Openly licensed, so short excerpts can be quoted on the wiki with attribution.

- [core] **[Classification with Claude: Insurance Support Ticket Classifier (Claude Cookbook)](https://platform.claude.com/cookbook/capabilities-classification-guide)** (2024) — Doyle, G. (Anthropic). *Claude Cookbook*
  `notebook` · `intermediate` · `access: open` · `MIT (claude-cookbooks repo)` · `AI angle`
  Worked notebook comparing simple prompting (74%), retrieval of similar labeled examples (94%) and retrieval plus chain of thought (97%) on a 10-category text classifier. Includes a scikit-learn classification report and confusion matrix, and Promptfoo tests across temperatures.
  *Use in wiki:* Template for the M5 'LLM classifier' lab. Students swap in their own label set (e.g., complaint types in reviews), keep the evaluation harness, and report accuracy against human labels.
  Tools: anthropic, scikit-learn, voyageai, promptfoo · Local copy: `05_M5_Text_and_Social_Media_Analytics/repos/anthropics__claude-cookbooks`
  *Note:* Uses synthetic data (68 train / 68 test tickets). Requires API keys, so set a classroom budget. Companion guide on when to use an LLM vs. traditional ML and on known failure modes (implicit requests, emotion overriding intent, multi-issue texts): https://platform.claude.com/docs/en/about-claude/use-case-guides/ticket-routing (fetched).

- [core] **[ChatGPT outperforms crowd workers for text-annotation tasks](https://doi.org/10.1073/pnas.2305016120)** (2023) — Gilardi, F.; Alizadeh, M.; Kubli, M. *PNAS 120(30)*
  `paper` · `intro` · `access: open` · `CC BY 4.0` · `AI angle`
  On 2,382 tweets, zero-shot ChatGPT beat MTurk crowd workers on four of five annotation tasks, had higher intercoder agreement than crowd workers and trained annotators, and cost under a third of a cent per annotation (about 20 times cheaper).
  *Use in wiki:* Short core reading that motivates LLM labeling. Pair it with Reiss (2023) and Baumann et al. (2025) for the cautionary side.
  DOI [10.1073/pnas.2305016120](https://doi.org/10.1073/pnas.2305016120) · [Open-access copy](https://pmc.ncbi.nlm.nih.gov/articles/PMC10372638) · Tools: OpenAI API
  *Note:* DOI and license confirmed via Crossref. arXiv version: https://arxiv.org/abs/2303.15056. Results are for ChatGPT as of early 2023, so newer models differ.

- [recommended] **[Structured Outputs guide](https://developers.openai.com/api/docs/guides/structured-outputs)** (2026) — OpenAI. *OpenAI API docs*
  `documentation` · `intermediate` · `access: paid` · `AI angle`
  Makes model outputs conform to a supplied JSON Schema (strict mode), with Pydantic models in the Python SDK. Enum fields restrict outputs to a fixed label set, so the model cannot invent categories.
  *Use in wiki:* Teach 'labels as a schema': define a Pydantic class with an enum sentiment, a list of aspects and a confidence field, so LLM classification outputs load straight into pandas.
  Tools: openai, pydantic
  *Note:* Anthropic and Gemini offer comparable structured-output features (not separately verified here). Schema enforcement fixes formatting but not validity, so a human-labeled check is still needed.

- [recommended] **[Large Language Models: An Applied Econometric Framework](https://nber.org/papers/w33344)** (2025) — Ludwig, J.; Mullainathan, S.; Rambachan, A. *NBER Working Paper 33344 (rev. Dec 2025)*
  `paper` · `advanced` · `access: open` · `AI angle`
  Distinguishes prediction uses of LLMs, which need no training leakage, from estimation or measurement uses. For measurement, valid inference requires a small validation sample, because otherwise arbitrary choices such as the model or prompt can change results a lot.
  *Use in wiki:* Instructor anchor for the module's validation rule: every LLM-coded variable needs a human-labeled validation subsample. Assign a simplified slide version to students.
  DOI [10.3386/w33344](https://doi.org/10.3386/w33344) · [Open-access copy](https://arxiv.org/abs/2412.07031v3)
  *Note:* The NBER page is open. Was presented at the NBER SI 2026 ML session (conference PDF seen in search).

- [recommended] **[To Err Is Human; To Annotate, SILICON? Toward Robust Reproducibility in LLM Annotation](https://arxiv.org/abs/2412.14461)** (2024) — Cheng, X.; Mayya, R.; Sedoc, J. *arXiv:2412.14461 (v4, May 2026)*
  `paper` · `intermediate` · `access: open` · `AI angle`
  Shows how LLM-based annotation becomes irreproducible when proprietary models are retired, and proposes the SILICON workflow: decompose measurement error, choose open-weight backup models, and route low-confidence labels to auxiliary models.
  *Use in wiki:* Reading for the 'non-reproducibility' failure mode. Supports a course rule that teams log the model version, prompt, temperature and date, and keep an open-weight fallback.
  *Note:* Preprint by business-school (NYU Stern) authors; no journal ref listed.

- [optional] **[Correcting Toward the Wrong Target: LLM-Annotated Regressors Under Noisy Human Benchmarks](https://scholar.smu.edu/business_marketing_research/63)** (2025) — Overgoor, G.; Knight, S.; Bart, Y. *SMU Cox Marketing working paper / SSRN*
  `paper` · `advanced` · `access: open` · `AI angle`
  Argues that validating LLM labels against noisy human labels can mislead, because corrections pull estimates toward an attenuated target. Uses about 10k TV ads and proposes a diagnostic plus an IV estimator that uses a second human rater.
  *Use in wiki:* Instructor background and an advanced reading that links M3 measurement error to LLM labeling. Shows why human 'gold' labels are not automatically gold.
  DOI [10.2139/ssrn.5494548](https://doi.org/10.2139/ssrn.5494548) · [Open-access copy](https://papers.ssrn.com/ab_id=5494548)
  *Note:* Working paper (Sept 2025); journal publication not confirmed.

- [optional] **[Using Imperfect Surrogates for Downstream Inference: Design-based Supervised Learning for Social Science Applications of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2023/hash/d862f7f5445255090de13b825b880d59-Abstract.html)** (2023) — Egami, N.; Hinck, M.; Stewart, B. M.; Wei, H. *NeurIPS 36 (2023)*
  `paper` · `advanced` · `access: open` · `CC BY 4.0 (arXiv version)` · `AI angle`
  Shows that plugging LLM labels straight into regressions can bias estimates and confidence intervals even at 80-90% accuracy. Proposes DSL, a doubly robust estimator that combines surrogate labels with a random gold-standard subsample.
  *Use in wiki:* Instructor background and an advanced optional reading on why and how to correct regressions that use LLM-coded variables.
  [Open-access copy](https://arxiv.org/html/2306.04746v3)
  *Note:* Related: Angelopoulos et al. (2023), 'Prediction-powered inference', Science 382(6671):669-674, doi 10.1126/science.adi6000 (Crossref-verified). The authors' DSL software was not verified here.

## Failure modes of LLM text analysis

- [recommended] **[Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs for Text Annotation](https://arxiv.org/abs/2509.08825v2)** (2025) — Baumann, J.; Röttger, P.; Urman, A.; Wendsjö, A.; Plaza-del-Arco, F. M.; Gruber, J. B.; Hovy, D. *arXiv:2509.08825*
  `paper` · `intermediate` · `access: open` · `AI angle`
  Across many replicated hypotheses, about 31% of tests using state-of-the-art LLM annotations reached incorrect conclusions, and the risk is highest near significance thresholds. Human annotations were the best safeguard of the 21 mitigations tested.
  *Use in wiki:* Key cautionary reading. It links naturally to M6 on p-hacking: changing models or prompts until results look significant is a form of p-hacking.
  *Note:* Preprint (v2, Oct 2025); no journal ref yet.

- [recommended] **[Testing the Reliability of ChatGPT for Text Annotation and Classification: A Cautionary Remark](https://arxiv.org/abs/2304.11085)** (2023) — Reiss, M. V. *arXiv:2304.11085*
  `paper` · `intro` · `access: open` · `AI angle`
  Repeated runs and small prompt or setting changes produce inconsistent ChatGPT classifications, so unsupervised use without validation against human labels is not advisable.
  *Use in wiki:* Motivates an in-class exercise: rerun the same LLM classification with 3 prompt wordings and 2 temperatures and measure agreement (Krippendorff's alpha).
  *Note:* See also Atreja et al. (2024), 'Prompt Design Matters for Computational Social Science Tasks but in Unpredictable Ways', https://arxiv.org/abs/2406.11980 (likely ICWSM 2025; fetched), and Pangakis et al. (2023), 'Automated Annotation with Generative AI Requires Validation', https://arxiv.org/abs/2306.00176 (fetched).

## Classifying text at scale with LLM APIs

- [recommended] **[Batch processing (Message Batches API)](https://platform.claude.com/docs/en/build-with-claude/batch-processing)** (2026) — Anthropic. *Claude Developer Platform docs*
  `documentation` · `intermediate` · `access: paid` · `AI angle`
  Asynchronous batches at 50% of standard price. Most finish within an hour and expire at 24 hours; limits are 100,000 requests or 256 MB; prompt-caching discounts stack. Includes a full Python example.
  *Use in wiki:* Code reference for the batch-labeling step. Its tips (match by custom_id, validate request shape first, cache the shared instruction prompt) belong in the wiki's LLM-annotation checklist.
  Tools: anthropic
  *Note:* docs.anthropic.com URLs now redirect to platform.claude.com. Results are retained 29 days. Prices are on the page and change over time, so check them before setting a class budget.

- [recommended] **[Gemini API Batch Mode](https://ai.google.dev/gemini-api/docs/batch-mode)** (2026) — Google. *Google AI for Developers*
  `documentation` · `intermediate` · `access: freemium` · `AI angle`
  Batch jobs at 50% of standard price with a 24-hour target (expiring after 48 hours). Requests go inline (under 20 MB) or as a JSONL file (up to 2 GB) with keys, and the page includes a Python example using the google-genai SDK.
  *Use in wiki:* Low-cost option for students. The Gemini free tier (via Google AI Studio) lets them prototype classification prompts without a credit card before scaling.
  Tools: google-genai
  *Note:* Pricing page, https://ai.google.dev/gemini-api/docs/pricing (fetched Oct 2026): a free tier exists for some Flash/Flash-Lite models, but free-tier content is used to improve Google products. Students must not send confidential or personal data on the free tier.

- [recommended] **[OpenAI Batch API guide](https://developers.openai.com/api/docs/guides/batch)** (2026) — OpenAI. *OpenAI API docs*
  `documentation` · `intermediate` · `access: paid` · `AI angle`
  Asynchronous bulk requests at 50% lower cost with a 24-hour completion window. Input is a JSONL file (up to 50,000 requests, 200 MB) with custom_id for matching outputs, and it uses a separate rate-limit pool.
  *Use in wiki:* Reference for scaling a validated prompt from 200 to 50,000 reviews cheaply. Teach the pattern: pilot synchronously, validate, then batch.
  Tools: openai
  *Note:* platform.openai.com/docs/guides/batch now redirects here. Output order may differ from input, so match on custom_id. Output files are deleted after 30 days.

## Social media and reviews

- [core] **[Bluesky API Directory: public endpoints (no authentication)](https://docs.bsky.app/docs/advanced-guides/api-directory)** (2026) — Bluesky PBC. *docs.bsky.app*
  `documentation` · `intro` · `access: open`
  Many Bluesky (AT Protocol) endpoints are public and need no authentication via public.api.bsky.app. Bluesky also offers a JSON 'Jetstream' firehose, making it one of the most open major platforms for classroom data collection.
  *Use in wiki:* Default platform for live social-media labs: students collect posts on a brand or hashtag with the Python SDK, then run sentiment, topic and reply-network analyses.
  Tools: atproto, websockets
  *Note:* Jetstream announcement (Oct 2024; not a formally stable API): https://docs.bsky.app/blog/jetstream. Community Python SDK: https://atproto.blue/en/latest/ (pip install atproto). Main docs: https://docs.bsky.app/. All fetched. Remind students of ethics: public posts are not consent for redistribution.

- [recommended] **[Reddit Data API Wiki](https://support.reddithelp.com/hc/en-us/articles/16160319875092-Reddit-Data-API-Wiki)** (2026) — Reddit, Inc. *Reddit Help*
  `documentation` · `intro` · `access: application`
  Official rules for the Reddit Data API: OAuth required (unauthenticated traffic is blocked), 100 queries per minute per OAuth client on the free tier, a descriptive User-Agent, and the Responsible Builder Policy and Data API Terms.
  *Use in wiki:* Setup guide for a Reddit-comments lab with PRAW. Students register a script app, then pull a subreddit's posts for sentiment and topic analysis.
  Tools: praw
  *Note:* Page updated May 11, 2026. Python wrapper: PRAW 8.0.3 docs, https://praw.readthedocs.io/en/stable/. Checked 2026-10-23: even non-commercial Data API use is limited to approved developers after a request and app review, so plan for lead time or use Bluesky's open API for class labs.

- [recommended] **[X API pricing (pay-per-usage)](https://docs.x.com/x-api/getting-started/pricing)** (2026) — X Corp. *docs.x.com*
  `documentation` · `intro` · `access: paid`
  Current X API docs describe only prepaid, pay-per-usage credits: about $0.005 per post read and $0.010 per user read, capped at 3M post reads per month (Enterprise above that), with 24-hour deduplication.
  *Use in wiki:* Use in a 'data access reality check' callout: a 10,000-tweet student project costs real money, which is why course labs use Bluesky, Reddit or archived datasets.
  *Note:* Fetched Oct 2026. The intro page (https://docs.x.com/x-api/introduction) says 'No subscriptions—pay only for what you use' and does not describe a free research tier. Prices may change.

- [recommended] **[YouTube Data API v3: Getting Started (and quota costs)](https://developers.google.com/youtube/v3/getting-started)** (2026) — Google. *Google for Developers*
  `documentation` · `intro` · `access: free-registration` · `Docs CC BY 4.0; code samples Apache 2.0`
  How to get an API key and use the YouTube Data API. The default quota is 10,000 units per day; most list calls such as commentThreads.list and videos.list cost 1 unit, and search.list has its own 100-calls-per-day cap.
  *Use in wiki:* Easy free source for a comments-sentiment or influencer-video lab. Students pull comments on a brand's or creator's videos and classify them.
  Tools: google-api-python-client
  *Note:* Quota table: https://developers.google.com/youtube/v3/determine_quota_cost (fetched Oct 2026; quotas reset at midnight Pacific). Scaled academic access: YouTube Researcher Program, https://research.youtube/ (fetched).

- [recommended] **[Influencer Marketing Effectiveness](https://doi.org/10.1177/00222429221102889)** (2022) — Leung, F. F.; Gu, F. F.; Li, Y.; Zhang, J. Z.; Palmatier, R. W. *Journal of Marketing 86(6), 93-115*
  `paper` · `intermediate` · `access: library`
  Empirical study of what drives influencer marketing effectiveness, covering influencer, content, follower and brand factors and how they shape engagement.
  *Use in wiki:* Anchor reading for the influencer subsection. Students operationalize its content factors using text and LLM coding of influencer posts or YouTube videos.
  DOI [10.1177/00222429221102889](https://doi.org/10.1177/00222429221102889)
  *Note:* DOI metadata confirmed via Crossref; the summary is generic because the abstract was not fetched. Also see Hughes, Swaminathan & Brooks (2019, JM 83(5):78-96), doi 10.1177/0022242919854374 (Crossref-verified). FTC influencer disclosure guidance: https://www.ftc.gov/business-guidance/resources/disclosures-101-social-media-influencers (fetched).

- [recommended] **[Online Influencer Marketing](https://ideas.repec.org/a/spr/joamsc/v50y2022i2d10.1007_s11747-021-00829-4.html)** (2022) — Leung, F. F.; Gu, F. F.; Palmatier, R. W. *Journal of the Academy of Marketing Science 50(2), 226–251*
  `paper` · `intermediate` · `access: library`
  Integrative review and framework for influencer marketing: influencer, follower, content and brand factors and how they drive engagement and sales. Won the 2022 JAMS Sheth Foundation Best Paper Award.
  *Use in wiki:* Framework reading for influencer analytics; pairs with the MBA 542 TikTok transcript exercise, in which an LLM scores expertise and authenticity cues.
  DOI [10.1007/s11747-021-00829-4](https://doi.org/10.1007/s11747-021-00829-4) · [Open-access copy](https://ira.lib.polyu.edu.hk/bitstream/10397/94874/1/Leung_Online_Influencer_Marketing.pdf)
  *Note:* Also on the MBA 542 Module 3 reading list. Distinct from the Leung et al. (2022) Journal of Marketing paper on influencer marketing effectiveness, which is also in this catalog.

- [recommended] **[The Market for Fake Reviews](https://doi.org/10.1287/mksc.2022.1353)** (2022) — He, S.; Hollenbeck, B.; Proserpio, D. *Marketing Science 41(5), 896-921*
  `paper` · `intermediate` · `access: library`
  Documents the online market for buying fake Amazon reviews (organized via Facebook groups) and its effects on ratings, sales and product outcomes.
  *Use in wiki:* Case for discussing review-data validity before running sentiment on reviews. Pairs with the FTC's 2024 fake-review rule.
  DOI [10.1287/mksc.2022.1353](https://doi.org/10.1287/mksc.2022.1353)
  *Note:* DOI metadata confirmed via Crossref; summary is from general knowledge of the paper. Also see Luca & Zervas (2016), 'Fake It Till You Make It', Management Science 62(12):3412-3427, doi 10.1287/mnsc.2015.2304 (Crossref-verified).

- [recommended] **[The Effect of Word of Mouth on Sales: Online Book Reviews](https://doi.org/10.1509/jmkr.43.3.345)** (2006) — Chevalier, J. A.; Mayzlin, D. *Journal of Marketing Research 43(3), 345-354*
  `paper` · `intermediate` · `access: library`
  Classic differences-in-differences comparison of Amazon and Barnes & Noble reviews, showing that review ratings affect relative book sales and that negative reviews weigh more.
  *Use in wiki:* Classic case linking review text and ratings to sales. A good bridge to M6 identification logic.
  DOI [10.1509/jmkr.43.3.345](https://doi.org/10.1509/jmkr.43.3.345)
  *Note:* DOI metadata confirmed via Crossref.

- [optional] **[Meta Content Library and Content Library API](https://developers.facebook.com/docs/content-library-and-api/)** (2026) — Meta. *Meta for Developers*
  `documentation` · `intermediate` · `access: free-registration`
  Controlled-access research archive of public Facebook and Instagram content (posts, Pages, comments, groups, events and more), with a web UI and an API. Analysis runs in Meta's Secure Research Environment (Python/R JupyterHub) or an approved cleanroom.
  *Use in wiki:* Instructor-facing context on post-CrowdTangle research access. Too heavy for a semester project, but useful in a lecture on who can see platform data.
  *Note:* Requires an approved application (via ICPSR or CASD) and agreement to Meta's research terms. The ICPSR page failed to load, so fees and eligibility are not verified. Compute in the SRE is stated as free. Related: TikTok Research API for academic researchers in the US, EEA, UK, Switzerland and Canada (applications take about 4 weeks), https://developers.tiktok.com/products/research-api/ (fetched).

- [optional] **[Federal Trade Commission Announces Final Rule Banning Fake Reviews and Testimonials](https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials)** (2024) — U.S. Federal Trade Commission. *FTC press release (Aug 14, 2024)*
  `report` · `intro` · `access: open` · `AI angle`
  Final rule banning fake reviews, including AI-generated ones, insider reviews, review suppression, incentives conditioned on sentiment, and buying or selling fake social media indicators such as bot followers and views.
  *Use in wiki:* Short case for an M5/M8 discussion: generative AI makes fake reviews cheap, so what does that mean for review analytics and detection?
  *Note:* Takes effect 60 days after Federal Register publication.

- [optional] **[Word of Mouth and Interpersonal Communication: A Review and Directions for Future Research](https://myscp.onlinelibrary.wiley.com/doi/abs/10.1016/j.jcps.2014.05.002)** (2014) — Berger, J. *Journal of Consumer Psychology 24(4), 586–607*
  `paper` · `intermediate` · `access: library`
  Review of why people share word of mouth (impression management, emotion regulation, information acquisition, social bonding, persuasion) and how sharing shapes the sender and receiver.
  *Use in wiki:* Background reading for the social-media analytics part of M5.
  DOI [10.1016/j.jcps.2014.05.002](https://doi.org/10.1016/j.jcps.2014.05.002)
  *Note:* Also on the MBA 542 Module 2 reading list.

## Network analysis and diffusion

- [core] **[NetworkX Tutorial](https://networkx.org/documentation/stable/tutorial.html)** (2026) — NetworkX Developers. *NetworkX documentation (v3.7)*
  `tutorial` · `intro` · `access: open`
  Official hands-on tutorial: creating graphs, nodes and edges with attributes, directed and multigraphs, generators, file I/O, basic analysis (components, degree, clustering, shortest paths) and drawing.
  *Use in wiki:* Code reference for the network lab: build a retweet or reply network from Bluesky, or a brand co-mention network from reviews, then compute degree and betweenness centrality.
  Tools: networkx, matplotlib
  *Note:* Community notebooks at NX-Guides, https://networkx.org/nx-guides/ (fetched), include a 'Facebook network analysis' exploratory notebook (Binder-ready) suitable as a ready-made in-class exercise. NetworkX is BSD-licensed per general knowledge; the license was not stated on the fetched page.

- [core] **[Seeding Strategies for Viral Marketing: An Empirical Comparison](https://doi.org/10.1509/jm.10.0088)** (2011) — Hinz, O.; Skiera, B.; Barrot, C.; Becker, J. U. *Journal of Marketing 75(6), 55-71*
  `paper` · `intermediate` · `access: library`
  Compares seeding strategies (high-degree hubs, bridges, random) with field experiments and real referral data. Seeding well-connected people can far outperform random seeding.
  *Use in wiki:* Core marketing reading for the network subsection. Students simulate hub vs. random seeding on a SNAP network in NetworkX and compare reach.
  DOI [10.1509/jm.10.0088](https://doi.org/10.1509/jm.10.0088)
  *Note:* DOI metadata confirmed via Crossref; summary is from general knowledge of the paper. Related: Goldenberg, Han, Lehmann & Hong (2009), 'The Role of Hubs in the Adoption Process', JM 73(2):1-13, doi 10.1509/jmkg.73.2.1; Trusov, Bucklin & Pauwels (2009), 'Effects of WOM versus Traditional Marketing', JM 73(5):90-102, doi 10.1509/jmkg.73.5.90; Katona, Zubcsek & Sarvary (2011), JMR 48(3):425-443, doi 10.1509/jmkr.48.3.425. All Crossref-verified.

- [recommended] **[Network Analysis Made Simple](https://ericmjl.github.io/Network-Analysis-Made-Simple/)** (2026) — Ma, E.; Seth, M. *Web book + GitHub*
  `notebook` · `intro` · `access: open` · `MIT (repo)`
  Jupyter-notebook course on NetworkX: graph basics, visualization, hubs and paths, structures, bipartite graphs, and case studies (Game of Thrones, airports).
  *Use in wiki:* Adapt the hubs/centrality and bipartite (customer-product) notebooks as M5 labs. Bipartite graphs link to recommendation in M7.
  Tools: networkx, nxviz · Local copy: `05_M5_Text_and_Social_Media_Analytics/repos/ericmjl__Network-Analysis-Made-Simple`
  *Note:* Binder supported; Colab not mentioned. The ebook (PDF/EPUB) on LeanPub is paid, but the notebooks are free. Year reflects the live site.

- [recommended] **[Identifying Influential and Susceptible Members of Social Networks](https://doi.org/10.1126/science.1215842)** (2012) — Aral, S.; Walker, D. *Science 337(6092), 337-341*
  `paper` · `intermediate` · `access: library`
  Randomized experiment on Facebook (product adoption via an app) estimating who is influential and who is susceptible to influence, by demographics.
  *Use in wiki:* Case example for 'influencers are not just high-degree nodes'. Bridges to M6 on why experiments are needed to separate influence from homophily.
  DOI [10.1126/science.1215842](https://doi.org/10.1126/science.1215842)
  *Note:* DOI metadata confirmed via Crossref; summary is from general knowledge of the paper. Other Aral work: Aral, Muchnik & Sundararajan (2009), 'Distinguishing influence-based contagion from homophily-driven diffusion in dynamic networks', PNAS 106(51):21544-21549, doi 10.1073/pnas.0908800106; Aral & Dhillon (2018), 'Social influence maximization under empirical influence models', Nature Human Behaviour 2(6):375-382, doi 10.1038/s41562-018-0346-z. Both Crossref-verified.

- [recommended] **[Networks, Crowds, and Markets: Reasoning About a Highly Connected World](https://www.cs.cornell.edu/home/kleinber/networks-book/)** (2010) — Easley, D.; Kleinberg, J. *Cambridge University Press (free pre-publication draft)*
  `book` · `intro` · `access: open`
  Introductory, no-prerequisite text that combines economics, sociology and computing. Ch. 16 (information cascades) and Ch. 19 (cascading behavior in networks, thresholds, weak ties) fit WOM and seeding.
  *Use in wiki:* Assign Ch. 19 as conceptual reading before the seeding/influencer lecture. Its threshold models can be simulated in NetworkX.
  *Note:* A complete pre-publication draft PDF is free on the page. Alternative: Barabási, 'Network Science', http://networksciencebook.com/ (online; license and access terms not confirmed by fetch).

## Python for marketing analytics: notebooks and code

- [core] **[OpenAI Cookbook: embedding and classification notebooks on Amazon fine-food reviews, plus structured outputs and synthetic data](https://github.com/openai/openai-cookbook)** (2026) — OpenAI. *GitHub (openai/openai-cookbook)*
  `notebook` · `intermediate` · `access: open` · `MIT` · `AI angle`
  Runnable notebooks on a 1k-review Amazon fine-food dataset: getting embeddings, zero-shot sentiment classification with embeddings, supervised classification on embeddings, clustering with GPT-written cluster labels, 2-D visualization, and user and product embeddings. Also an intro to Structured Outputs and LLM synthetic data generation (SDG1).
  *Use in wiki:* M5 LLM lab: students embed reviews, classify sentiment zero-shot, cluster complaints and let an LLM name the clusters, then check the labels against star ratings.
  Tools: openai, pandas, scikit-learn, plotly · Local copy: `05_M5_Text_and_Social_Media_Analytics/repos/openai__openai-cookbook`
  *Note:* Repo is huge (3,700+ files), so use only these sparse paths. examples/data/fine_food_reviews_with_embeddings_1k.csv (35 MB) is excluded: students regenerate it with Get_embeddings_from_dataset, which needs an API key and incurs a small API cost, or swap in a free embedding model. Older notebooks use older embedding model names. Last commit 2026-10-21.

- [recommended] **[BERTopic documentation: best practices, LLM-based topic representation, zero-shot topics, topics over time and per class](https://github.com/MaartenGr/BERTopic)** (2026) — Grootendorst, M. *GitHub (MaartenGr/BERTopic)*
  `documentation` · `intermediate` · `access: open` · `MIT` · `AI angle`
  Markdown sources of the BERTopic guide. Covers the embed-reduce-cluster-c-TF-IDF pipeline, LLM-generated topic labels (OpenAI, Llama, etc.), zero-shot and guided topics, and dynamic topics by date or by class (e.g. brand or rating).
  *Use in wiki:* Reference for review- and social-media topic modeling labs. 'Topics per class' and 'topics over time' map directly onto brand comparisons and campaign tracking.
  Tools: bertopic, sentence-transformers, umap-learn, hdbscan · Local copy: `05_M5_Text_and_Social_Media_Analytics/repos/MaartenGr__BERTopic`
  *Note:* Last commit 2026-08-27. The repo has no .ipynb files; the README's Colab links point to Google Drive, which is not downloadable. Hands-On LLMs (already in the library) has a BERTopic chapter with runnable notebooks.

- [recommended] **[Blueprints for Text Analytics Using Python: companion notebooks](https://github.com/blueprints-for-text-analytics-python/blueprints-text)** (2026) — Albrecht, J.; Ramachandran, S.; Winkler, C. *GitHub (blueprints-for-text-analytics-python/blueprints-text); O'Reilly 2020*
  `book` · `intermediate` · `access: open` · `Apache-2.0`
  One notebook per chapter: first insights and word frequencies, text preparation, classification, topic modeling and clustering, embeddings, and sentiment analysis of Amazon product reviews (lexicon, ML and transformer approaches).
  *Use in wiki:* Backbone notebooks for M5's classical-NLP half (before LLMs). Chapter 11 sentiment on product reviews is directly about marketing.
  Tools: pandas, spacy, scikit-learn, gensim, textacy, transformers · Local copy: `05_M5_Text_and_Social_Media_Analytics/repos/blueprints-for-text-analytics-python__blueprints-text`
  *Note:* oreil.ly/btap-code redirects here. Last commit 2026-05-28. The book used spaCy 2.3 and gensim 3.8, so some cells need updates for spaCy 3, gensim 4 and textacy. The data/ folder (about 130 MB) is excluded. data/amazon-product-reviews/reviews_5_balanced.json.gz (16.6 MB) is needed for ch11, but redistribution terms for the Amazon review data are unclear, so fetch it at runtime rather than mirror it.

- [optional] **[Scikit-LLM: LLM zero-shot classification inside scikit-learn](https://github.com/BeastByteAI/scikit-llm)** (2026) — BeastByteAI. *GitHub (BeastByteAI/scikit-llm); docs skllm.beastbyte.ai*
  `package` · `intro` · `access: open` · `MIT` · `AI angle`
  Wraps GPT-style models as scikit-learn estimators (fit/predict) for zero-shot text classification, so LLM labeling slots into familiar pipelines and evaluation code.
  *Use in wiki:* Low-friction way for non-CS students to compare LLM zero-shot labels against a TF-IDF and logistic-regression baseline on review data, with standard metrics.
  [Open-access copy](https://skllm.beastbyte.ai) · Tools: scikit-llm, scikit-learn, openai
  *Note:* LINK ONLY by choice: MIT-licensed, but the repo is library code with no notebooks, so pip install it instead. Last commit 2026-01-21. The README still has stale links to iryna-kondr/ repos (the old owner).

- [optional] **[SetFit notebooks: few-shot and zero-shot text classification with sentence transformers](https://github.com/huggingface/setfit)** (2026) — Hugging Face. *GitHub (huggingface/setfit)*
  `notebook` · `intermediate` · `access: open` · `Apache-2.0`
  Train an accurate text classifier from 8 to 64 labeled examples per class, or from label names alone (zero-shot), without prompting a large LLM.
  *Use in wiki:* Cheap, private alternative to LLM-API labeling of reviews or tickets. Students compare SetFit with zero-shot LLM labels on the same marketing texts.
  Tools: setfit, sentence-transformers, datasets
  *Note:* Last commit 2026-10-06. The notebooks pull models and datasets from the Hugging Face Hub at runtime, which works on Colab but not on the GitHub-only download machine.

## AI-assisted coding angle for this module

Resources in this folder that show the method done with AI help, LLM versions of the method, or documented failure modes of AI-written analysis:

- [OpenAI Cookbook: embedding and classification notebooks on Amazon fine-food reviews, plus structured outputs and synthetic data](https://github.com/openai/openai-cookbook)
- [Using natural language processing to analyse text data in behavioural science](https://www.nature.com/articles/s44159-024-00392-z)
- [Best Practices for Text Annotation with Large Language Models](https://sociologica.unibo.it/article/view/19461)
- [Classification with Claude: Insurance Support Ticket Classifier (Claude Cookbook)](https://platform.claude.com/cookbook/capabilities-classification-guide)
- [Frontiers: Determining the Validity of Large Language Models for Automated Perceptual Analysis](https://doi.org/10.1287/mksc.2023.0454)
- [Hands-On Large Language Models (official code repository)](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models)
- [Sentiment Analysis in the Age of Generative AI](https://link.springer.com/doi/10.1007/s40547-024-00143-4)
- [ChatGPT outperforms crowd workers for text-annotation tasks](https://doi.org/10.1073/pnas.2305016120)
- [BERTopic: Neural topic modeling with a class-based TF-IDF procedure](https://maartengr.github.io/BERTopic/index.html)
- [Batch processing (Message Batches API)](https://platform.claude.com/docs/en/build-with-claude/batch-processing)
- [BERTopic documentation: best practices, LLM-based topic representation, zero-shot topics, topics over time and per class](https://github.com/MaartenGr/BERTopic)
- [Gemini API Batch Mode](https://ai.google.dev/gemini-api/docs/batch-mode)
- [OpenAI Batch API guide](https://developers.openai.com/api/docs/guides/batch)
- [Structured Outputs guide](https://developers.openai.com/api/docs/guides/structured-outputs)
- [Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs for Text Annotation](https://arxiv.org/abs/2509.08825v2)
- [Large Language Models: An Applied Econometric Framework](https://nber.org/papers/w33344)
- [To Err Is Human; To Annotate, SILICON? Toward Robust Reproducibility in LLM Annotation](https://arxiv.org/abs/2412.14461)
- [Testing the Reliability of ChatGPT for Text Annotation and Classification: A Cautionary Remark](https://arxiv.org/abs/2304.11085)
- [Scikit-LLM: LLM zero-shot classification inside scikit-learn](https://github.com/BeastByteAI/scikit-llm)
- [Correcting Toward the Wrong Target: LLM-Annotated Regressors Under Noisy Human Benchmarks](https://scholar.smu.edu/business_marketing_research/63)
- [Federal Trade Commission Announces Final Rule Banning Fake Reviews and Testimonials](https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials)
- [Using Imperfect Surrogates for Downstream Inference: Design-based Supervised Learning for Social Science Applications of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2023/hash/d862f7f5445255090de13b825b880d59-Abstract.html)

## Also relevant (catalogued in other folders)

- **`01_M1_Marketing_Analytics_and_Python`**: [Applying Data Analytics in Marketing](https://www.coursera.org/learn/applying-data-analytics-business-in-marketing); [Principles of Marketing Engineering and Analytics (3rd ed.)](https://faculty.essec.edu/research/3268-principles-of-marketing-engineering-and-analytics-3rd-edition)
- **`04_M4_Conjoint_Segmentation_CLV`**: [AI-Human Hybrids for Marketing Research: Leveraging Large Language Models (LLMs) as Collaborators](https://journals.sagepub.com/doi/10.1177/00222429241276529); [TensorHouse: reference notebooks for marketing, promotions and pricing (successor to Introduction to Algorithmic Marketing examples)](https://github.com/ikatsov/tensor-house)
- **`07_M7_Predictive_Models_ML_and_AI`**: [Machine learning and AI in marketing: Connecting computing power to human insights](https://ideas.repec.org/a/eee/ijrema/v37y2020i3p481-504.html)
- **`08_M8_Current_Topics_in_Marketing`**: [Gemini API Cookbook: Market a Jet Backpack, JSON sentiment and classification, embeddings classification and clustering](https://github.com/google-gemini/cookbook); [2025 Creator Economy Ad Spend & Strategy Report](https://www.iab.com/insights/2025-creator-economy-ad-spend-strategy-report/); [GEO: Generative Engine Optimization](https://arxiv.org/abs/2311.09735); [Google Cloud generative-ai repo: creative content generation, product attribute extraction, multimodal sentiment, AI-assisted data science](https://github.com/GoogleCloudPlatform/generative-ai); [Frontiers: Supporting Content Marketing with Natural Language Generation](https://ideas.repec.org/a/inm/ormksc/v41y2022i3p441-452.html)
- **`10_AI_Coding_Concepts_and_Evidence`**: [Anthropic Economic Index: AI's impact on software development](https://www.anthropic.com/research/impact-software-development)
- **`11_AI_Coding_Tools_and_Workflows`**: [Claude Cookbooks (anthropics/claude-cookbooks)](https://github.com/anthropics/claude-cookbooks); [Generative AI for Beginners (21 lessons)](https://github.com/microsoft/generative-ai-for-beginners)
- **`12_AI_Coding_Pedagogy_and_Policy`**: [Anthropic Education Report: How University Students Use Claude](https://www.anthropic.com/news/anthropic-education-report-how-university-students-use-claude)
- **`20_Datasets`**: [Amazon Reviews 2023 (Amazon Reviews'23)](https://amazon-reviews-2023.github.io/); [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce); [The Upworthy Research Archive](https://upworthy.natematias.com/); [Stanford Large Network Dataset Collection (SNAP)](https://snap.stanford.edu/data/); [Yelp Open Dataset](https://business.yelp.com/data/resources/open-dataset/); [TweetEval](https://huggingface.co/datasets/cardiffnlp/tweet_eval); [Bluesky developer docs and Jetstream](https://docs.bsky.app/); [Hugging Face Datasets Hub](https://huggingface.co/datasets); [Reddit Data API and Reddit for Researchers access rules](https://support.reddithelp.com/hc/en-us/articles/14945211791892-Developer-Platform-Accessing-Reddit-Data)
- **`21_Open_Textbooks_and_Courses`**: [Coding for Economists](https://aeturrell.github.io/coding-for-economists/); [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1); [Speech and Language Processing, 3rd ed. draft](https://web.stanford.edu/~jurafsky/slp3/); [Applied Marketing Analytics Using Python](https://collegepublishing.sagepub.com/products/applied-marketing-analytics-using-python-1-288563); [Data 100 Course Notes: Principles and Techniques of Data Science](https://ds100.org/course-notes/); [Machine Learning and Generative AI for Marketing (companion code)](https://github.com/PacktPublishing/Machine-Learning-and-Generative-AI-for-Marketing); [Dealing with Data (NYU teaching notebooks)](https://github.com/ipeirotis/dealing_with_data); [QuantEcon DataScience: Introduction to Economic Modeling and Data Science](https://datascience.quantecon.org/); [Practical Deep Learning for Coders](https://course.fast.ai/); [Marketing Data Science: Modeling Techniques in Predictive Analytics with R and Python (code downloads)](https://www.informit.com/promotions/marketing-data-science-modeling-techniques-in-predictive-141181)
