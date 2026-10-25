# M7 · Predictive Models, AI and Machine Learning

55 resources (22 core). Built 2026-10-25 from `00_Index/_data/`; edit the YAML there and rerun `00_Index/_build/build_catalog.py` rather than editing this file.

Priority: **core** = likely to assign or build on; **recommended** = strong supplement; **optional** = background or niche. *Access* tells you whether students can open it without a login.

## Contents

- [Core ML for business students](#core-ml-for-business-students) (11)
- [Prediction vs. causation](#prediction-vs-causation) (3)
- [Marketing prediction problems](#marketing-prediction-problems) (13)
- [Recommender system design: research evidence](#recommender-system-design-research-evidence) (16)
- [Data leakage and AI-written pipelines](#data-leakage-and-ai-written-pipelines) (4)
- [LLMs as simulated consumers](#llms-as-simulated-consumers) (2)
- [Python for marketing analytics: notebooks and code](#python-for-marketing-analytics-notebooks-and-code) (6)

## Core ML for business students

- [core] **[scikit-learn User Guide 3.1: Cross-validation, evaluating estimator performance](https://scikit-learn.org/stable/modules/cross_validation.html)** (2026) — scikit-learn developers. *scikit-learn 1.9.1 documentation*
  `documentation` · `intermediate` · `access: open` · `BSD-3-Clause (scikit-learn)`
  The canonical reference for cross_val_score and cross_validate, K-fold, stratified, grouped (GroupKFold) and time-series (TimeSeriesSplit) splitters, and permutation tests.
  *Use in wiki:* Link from the M7 'how to evaluate a churn model' page, and use GroupKFold (customers) and TimeSeriesSplit (forecasting) as marketing-relevant splitting examples.
  Tools: scikit-learn
  *Note:* The full User Guide index is at scikit-learn.org/stable/user_guide.html (also verified). The license is scikit-learn's well-known BSD-3. I did not re-check it in this session.

- [core] **[SHAP documentation: 'An introduction to explainable AI with Shapley values'](https://shap.readthedocs.io/en/latest/example_notebooks/overviews/An%20introduction%20to%20explainable%20AI%20with%20Shapley%20values.html)** (2026) — Lundberg, S. and SHAP contributors. *shap.readthedocs.io*
  `documentation` · `intermediate` · `access: open` · `MIT`
  The official SHAP intro notebook. It builds from linear models to tree ensembles and explains global and local feature attributions with beeswarm, waterfall and dependence plots.
  *Use in wiki:* Use it for the 'why is this customer predicted to churn?' segment. Students can produce SHAP plots for their XGBoost model and write a manager-facing interpretation.
  Tools: shap, xgboost, scikit-learn
  *Note:* The underlying paper is Lundberg & Lee (2017), 'A Unified Approach to Interpreting Model Predictions', arXiv 1705.07874 (fetched; NIPS venue not shown on arXiv). The repo license (MIT) and notebooks folder were confirmed by fetch. The notebooks folder may be large, so download it selectively.

- [core] **[XGBoost Documentation (incl. 'Introduction to Boosted Trees' and scikit-learn interface)](https://xgboost.readthedocs.io/en/stable/)** (2026) — XGBoost developers (DMLC). *xgboost.readthedocs.io (v3.4.2)*
  `documentation` · `intermediate` · `access: open` · `Apache-2.0`
  Official docs for XGBoost, with a get-started page, a Python intro, the scikit-learn estimator interface, and a well-written conceptual tutorial on boosted trees (tutorials/model.html).
  *Use in wiki:* Assign 'Introduction to Boosted Trees' for intuition, then have students swap XGBClassifier into their sklearn churn pipeline.
  Tools: xgboost, scikit-learn
  *Note:* The Apache-2.0 license was confirmed on github.com/dmlc/xgboost.

- [core] **[Machine learning in Python with scikit-learn (Inria MOOC)](https://inria.github.io/scikit-learn-mooc)** (2024) — Inria / scikit-learn core developers. *FUN MOOC and GitHub (Jupyter Book)*
  `course` · `intro` · `access: open` · `CC-BY-4.0`
  A free MOOC by scikit-learn maintainers covering predictive modeling pipelines, overfitting and underfitting, hyperparameter tuning, linear models, trees, ensembles and evaluation, with runnable notebooks and quizzes.
  *Use in wiki:* Self-paced backup for students without an ML background. Embed specific notebooks (for example 'ensemble' or 'evaluation') as pre-class work.
  [Open-access copy](https://www.fun-mooc.fr/en/courses/machine-learning-python-scikit-learn/) · Tools: scikit-learn, pandas · Local copy: `07_M7_Predictive_Models_ML_and_AI/repos/INRIA__scikit-learn-mooc`
  *Note:* The CC-BY license is stated in the repo README. The year is approximate because the repo is continuously updated.

- [core] **[ISLP_labs: Python lab notebooks for ISLP](https://github.com/intro-stat-learning/ISLP_labs)** (2023) — intro-stat-learning (ISLP authors and contributors). *GitHub*
  `notebook` · `intermediate` · `access: open` · `BSD-2-Clause`
  Twelve Jupyter notebooks, one per ISLP chapter (Ch02 to Ch13: linreg, classification, resample, baggboost, deeplearning, unsup and so on), with small datasets and a requirements.txt pinned at tag v2.2.2.
  *Use in wiki:* Embed or fork the classification, resampling and baggboost notebooks as Colab in-class coding activities. Students can also ask an AI assistant to explain or extend a lab cell.
  Tools: ISLP, scikit-learn, statsmodels, torch · Local copy: `07_M7_Predictive_Models_ML_and_AI/repos/intro-stat-learning__ISLP_labs`
  *Note:* Labs are versioned (v2.2.2). Pin that tag so the notebooks match the requirements file.

- [recommended] **[AutoGluon Tabular: Quick Start](https://auto.gluon.ai/stable/tutorials/tabular/tabular-quick-start.html)** (2026) — AutoGluon team (Amazon). *auto.gluon.ai (v1.6.1)*
  `tutorial` · `intro` · `access: open` · `Apache-2.0` · `AI angle`
  Three lines of code (TabularPredictor.fit) train and stack many models on a tabular dataset. It comes with a ready Colab notebook.
  *Use in wiki:* Benchmark exercise: compare AutoGluon against the student's hand-tuned XGBoost on the same holdout, then discuss what AutoML can't do (framing the problem, leakage, the business metric).
  [Open-access copy](https://colab.research.google.com/github/autogluon/autogluon/blob/master/docs/tutorials/tabular/tabular-quick-start.ipynb) · Tools: autogluon · Local copy: `07_M7_Predictive_Models_ML_and_AI/repos/autogluon__autogluon`
  *Note:* The repo README also lists the MLZero multi-agent AutoML paper (arXiv 2505.13941) and the TabArena benchmark (arXiv 2506.16791), both NeurIPS 2025.

- [recommended] **[LightGBM Documentation (Python quick start)](https://lightgbm.readthedocs.io/en/stable/)** (2026) — Microsoft / LightGBM developers. *lightgbm.readthedocs.io (v4.7.0)*
  `documentation` · `intermediate` · `access: open` · `MIT`
  Docs for LightGBM, a fast, memory-efficient gradient-boosting library that is a common Kaggle and industry default for tabular prediction. Includes a Python-Intro quick start.
  *Use in wiki:* Present it as the alternative to XGBoost, and have students compare speed and AUC on the same churn data with cross-validation.
  Tools: lightgbm, scikit-learn
  *Note:* MIT license confirmed on github.com/microsoft/LightGBM. That page now points to a lightgbm-org/LightGBM location, so the repo may have moved organizations.

- [recommended] **[Interpretable Machine Learning: A Guide for Making Black Box Models Explainable (3rd ed.)](https://christophm.github.io/interpretable-ml-book/)** (2025) — Molnar, C. *christophm.github.io (free online book)*
  `book` · `intermediate` · `access: open` · `CC BY-NC-SA 4.0`
  A free book on interpretability methods: permutation feature importance, partial dependence, Shapley values and SHAP, and their pitfalls.
  *Use in wiki:* Background reading behind the SHAP lab, especially the chapters on PDP, permutation importance and SHAP limitations.
  *Note:* The page says 3rd edition but shows no year, so 2025 is approximate. Examples appear to use R, so pair it with the SHAP Python docs.

- [recommended] **[Machine Learning Crash Course (refreshed edition)](https://developers.google.com/machine-learning/crash-course)** (2024) — Google for Developers. *developers.google.com*
  `course` · `intro` · `access: open` · `AI angle`
  A fast-paced, visual intro to ML: linear and logistic regression, classification metrics (thresholds, confusion matrix, AUC), data prep, overfitting, neural nets, embeddings, an intro to LLMs, and new AutoML and ML-fairness modules.
  *Use in wiki:* Link the classification-metrics and AutoML modules (about 30 min) as pre-reading. The interactive visuals suit non-CS students.
  Tools: Keras, Colab
  *Note:* The AutoML module is at developers.google.com/machine-learning/crash-course/automl (verified; about 30 minutes, covers benefits and limitations). The 2024 refresh date comes from a Google blog result in search, not from the course page itself.

- [recommended] **[Data Science for Business: What You Need to Know about Data Mining and Data-Analytic Thinking](https://oreilly.com/library/view/data-science-for/9781449374273)** (2013) — Provost, F.; Fawcett, T. *O'Reilly Media*
  `book` · `intro` · `access: library`
  Widely used business-school text on data-analytic thinking: framing problems as classification, regression or ranking; overfitting and holdout evaluation; expected-value framing of model decisions; churn and targeting examples.
  *Use in wiki:* Conceptual companion to the hands-on ML material; its expected-value framework fits churn and targeting exercises.
  *Note:* Also on the MBA 542 Module 8 reading list. The O'Reilly link may need institutional access.

- [optional] **[TabPFN: Accurate predictions on small data with a tabular foundation model](https://github.com/PriorLabs/TabPFN)** (2025) — Hollmann, N.; et al. (Prior Labs / University of Freiburg). *Nature (2025); GitHub*
  `package` · `intermediate` · `access: open` · `Apache-2.0 (code); model weights under separate, partly non-commercial licenses` · `AI angle`
  A pretrained transformer that does classification and regression on small tabular datasets in one forward pass, with no tuning, through a scikit-learn-style API. It is often competitive with tuned boosting.
  *Use in wiki:* Shows where 'foundation models' are heading for tabular marketing data. Students drop TabPFNClassifier into their churn pipeline and compare it with XGBoost.
  DOI [10.1038/s41586-024-08328-6](https://doi.org/10.1038/s41586-024-08328-6) · [Open-access copy](https://colab.research.google.com/github/PriorLabs/TabPFN/blob/main/examples/notebooks/TabPFN_Demo_Local.ipynb) · Tools: tabpfn, torch, scikit-learn
  *Note:* The Nature page fetch failed; the DOI and title come from the GitHub README. TabPFN-2.5 and later weights are non-commercial (fine for class use). It needs a GPU for larger data.

## Prediction vs. causation

- [core] **[Machine Learning: An Applied Econometric Approach](https://www.aeaweb.org/articles?id=10.1257/jep.31.2.87)** (2017) — Mullainathan, S.; Spiess, J. *Journal of Economic Perspectives 31(2): 87-106*
  `paper` · `intermediate` · `access: open`
  An accessible explanation of how supervised ML differs from econometrics: it is good at prediction (y-hat) but not at recovering parameters (beta-hat), illustrated with house-price prediction and regularization.
  *Use in wiki:* The opening reading for M7, connecting M3 (regression) and M6 (causal) to prediction.
  DOI [10.1257/jep.31.2.87](https://doi.org/10.1257/jep.31.2.87)
  *Note:* JEP offers a free PDF. Replication data is on openICPSR (project 113993, seen in search).

- [core] **[Prediction Policy Problems](https://www.aeaweb.org/articles?id=10.1257/aer.p20151023)** (2015) — Kleinberg, J.; Ludwig, J.; Mullainathan, S.; Obermeyer, Z. *American Economic Review 105(5): 491-95 (Papers & Proceedings)*
  `paper` · `intro` · `access: open`
  A short piece separating 'umbrella' problems, where only a prediction is needed, from 'rain dance' problems, where the causal effect matters.
  *Use in wiki:* A five-page reading for an in-class exercise: classify marketing decisions (churn targeting, ad budget, pricing) as prediction or causal problems.
  DOI [10.1257/aer.p20151023](https://doi.org/10.1257/aer.p20151023) · [Open-access copy](https://harris.uchicago.edu/files/inline-files/AER%20policy%20prediction%20problems%20may%202015.pdf)
  *Note:* The oa_url PDF came from search results and was not fetched.

- [recommended] **[Machine learning and AI in marketing: Connecting computing power to human insights](https://ideas.repec.org/a/eee/ijrema/v37y2020i3p481-504.html)** (2020) — Ma, L.; Sun, B. *International Journal of Research in Marketing 37(3): 481-504*
  `paper` · `advanced` · `access: open`
  A review of ML methods (supervised, unsupervised, deep learning, reinforcement learning) for marketing problems, including text, image and behavioral data, and how they complement theory-driven models.
  *Use in wiki:* Instructor background, plus an optional reading for students who want a map of ML applications in marketing research.
  DOI [10.1016/j.ijresmar.2020.04.005](https://doi.org/10.1016/j.ijresmar.2020.04.005) · [Open-access copy](https://english.ckgsb.edu.cn/faculty/sun-baohong/ma_sun_2020/)
  *Note:* The CKGSB page hosts the extracted full text of the paper.

## Marketing prediction problems

- [core] **[Forecasting: Principles and Practice, the Pythonic Way](https://otexts.com/fpppy/)** (2026) — Hyndman, R. J.; Athanasopoulos, G.; Garza, A.; Challu, C.; Mergenthaler, M.; Olivares, K. G. *OTexts (free online)*
  `book` · `intermediate` · `access: open`
  The Python edition of Hyndman and Athanasopoulos's forecasting textbook, built on Nixtla's open-source 'nixtlaverse' libraries. It is free online.
  *Use in wiki:* Assigned reading for the forecasting week (benchmarks, ETS, ARIMA, evaluation), with code that matches the statsforecast lab.
  Tools: statsforecast, mlforecast, pandas
  *Note:* Preface dated May 2026. No license is stated (only a copyright symbol), so link to it rather than copy it.

- [core] **[StatsForecast: fast forecasting with statistical and econometric models](https://github.com/Nixtla/statsforecast)** (2026) — Nixtla. *GitHub / nixtlaverse.nixtla.io*
  `package` · `intermediate` · `access: open` · `Apache-2.0`
  Fast AutoARIMA, AutoETS, Theta, MSTL, Croston-type intermittent-demand models and baselines for many series at once, with built-in time-series cross-validation.
  *Use in wiki:* Main tool for the demand-forecasting lab: forecast SKU-store sales with AutoETS vs seasonal naive and evaluate with rolling-origin CV.
  [Open-access copy](https://nixtlaverse.nixtla.io/statsforecast) · Tools: statsforecast, pandas
  *Note:* The 'nbs' folder probably holds the source notebooks, but the page does not say so. The docs quick guide is at nixtlaverse.nixtla.io/statsforecast/docs/getting-started/getting_started_short.html.

- [core] **[Netflix Recommendations: Beyond the 5 stars (Part 1)](https://netflixtechblog.com/netflix-recommendations-beyond-the-5-stars-part-1-55838468f429)** (2012) — Amatriain, X.; Basilico, J. *Netflix Technology Blog*
  `blog` · `intro` · `access: open`
  Netflix's own account of the Netflix Prize. SVD and RBM from the Progress Prize went into production, but the winning ensemble was never deployed because the accuracy gains did not justify the engineering cost, and the business goal shifted from RMSE to engagement and retention.
  *Use in wiki:* Case discussion: offline metric vs business objective. It also pairs with privacy (M8), since the Prize sequel was cancelled after a lawsuit and FTC concerns.
  *Note:* For history: en.wikipedia.org/wiki/Netflix_Prize (fetched) covers the 2006-2009 timeline, the $1M prize to BellKor's Pragmatic Chaos, the Narayanan-Shmatikov de-anonymization, the 2009 lawsuit and the 2010 cancellation of the sequel.

- [core] **[Bagging and Boosting Classification Trees to Predict Churn](https://journals.sagepub.com/doi/10.1509/jmkr.43.2.276)** (2006) — Lemmens, A.; Croux, C. *Journal of Marketing Research 43(2): 276-286*
  `paper` · `intermediate` · `access: library`
  A classic marketing paper showing that ensemble tree methods (bagging, stochastic gradient boosting) beat logistic regression for churn prediction, and discussing how to handle oversampled (balanced) training data.
  *Use in wiki:* Pair it with the XGBoost lab. It is an early marketing-journal case for boosting, and its correction for balanced sampling is a useful discussion point.
  DOI [10.1509/jmkr.43.2.276](https://doi.org/10.1509/jmkr.43.2.276) · [Open-access copy](https://repository.tilburguniversity.edu/items/cc4ad18d-93b2-4bc0-a6e7-8b53be6603d6)
  *Note:* The Tilburg repository record lists a PDF (lemmens_bagging.pdf), but open access was not confirmed.

- [core] **[Defection Detection: Measuring and Understanding the Predictive Accuracy of Customer Churn Models](https://journals.sagepub.com/doi/10.1509/jmkr.43.2.204)** (2006) — Neslin, S. A.; Gupta, S.; Kamakura, W.; Lu, J.; Mason, C. H. *Journal of Marketing Research 43(2): 204-211*
  `paper` · `intermediate` · `access: library`
  Reports a churn-modeling tournament (Teradata Center at Duke) in which many teams modeled the same telecom data. It shows that method choice matters for predictive accuracy and that accuracy translates into substantial retention profit.
  *Use in wiki:* Academic anchor for the churn unit. Use the tournament framing to motivate holdout evaluation (top-decile lift, Gini) on students' own churn models.
  DOI [10.1509/jmkr.43.2.204](https://doi.org/10.1509/jmkr.43.2.204)
  *Note:* The tournament detail (Teradata Center at Duke) is from background knowledge and was not verified; the fetched page confirmed only the title, authors, volume and pages. IAOR lists the authors in a different order.

- [recommended] **[Surprise: a Python scikit for recommender systems](https://github.com/NicolasHug/Surprise)** (2019) — Hug, N. *GitHub / surprise.readthedocs.io*
  `package` · `intro` · `access: open` · `BSD-3-Clause`
  A scikit-style library for explicit-rating recommenders (SVD and other matrix factorization, kNN baselines) with built-in MovieLens and Jester data and cross-validation helpers.
  *Use in wiki:* Quick in-class lab: replicate a Netflix-Prize-style SVD on MovieLens 100k in about 20 lines.
  [Open-access copy](https://surprise.readthedocs.io/en/stable/index.html) · Tools: scikit-surprise · Local copy: `07_M7_Predictive_Models_ML_and_AI/repos/NicolasHug__Surprise`
  *Note:* Maintenance-only since v1.1.0 (2019), with no new features. Check NumPy 2 compatibility in Colab before class. For implicit feedback (clicks, purchases), use 'implicit' (github.com/benfred/implicit, MIT; ALS, BPR; verified).

- [recommended] **[In Pursuit of Enhanced Customer Retention Management: Review, Key Issues, and Future Directions](https://ideas.repec.org/a/spr/custns/v5y2018i1d10.1007_s40547-017-0080-0.html)** (2018) — Ascarza, E.; Neslin, S. A.; Netzer, O.; Anderson, Z.; Fader, P. S.; Gupta, S.; Hardie, B. G. S.; Lemmens, A.; Libai, B.; Neal, D.; Provost, F.; Schrift, R. *Customer Needs and Solutions 5(1): 65-81*
  `paper` · `intermediate` · `access: open`
  A review from a Choice Symposium on retention management. It argues for moving from 'who will churn?' to 'whom should we target and with what?', covering churn prediction, targeting, interventions and CLV links.
  *Use in wiki:* Framing reading for the churn module. It connects M4 (CLV) to M7 (prediction) and M6 (targeting experiments).
  DOI [10.1007/s40547-017-0080-0](https://doi.org/10.1007/s40547-017-0080-0) · [Open-access copy](https://lbsresearch.london.edu/id/eprint/915)
  *Note:* The LBS eprint record appeared in search results; I did not fetch it to confirm the full text.

- [recommended] **[Prophet: Forecasting at scale](https://facebook.github.io/prophet/)** (2017) — Meta (Facebook) Core Data Science; Taylor, S. J.; Letham, B. *facebook.github.io/prophet*
  `package` · `intro` · `access: open`
  An additive trend, seasonality and holiday forecasting procedure for R and Python, popular in marketing and business teams for daily data with promotions and holidays.
  *Use in wiki:* Easy first forecasting demo (quick start in Colab), then contrast it with statsforecast baselines to show that Prophet is not always the most accurate.
  Tools: prophet
  *Note:* The site links a PeerJ preprint (peerj.com/preprints/3190), but that fetch failed, so the authors and the journal version (American Statistician 2018) are unverified. The site has a '2023 Update' on Prophet's future (not read). The license was not stated on the page.

- [recommended] **[Know What Your Customers Want Before They Do](https://hbr.org/2011/12/know-what-your-customers-want-before-they-do)** (2011) — Davenport, T. H.; DalleMule, L.; Lucker, J. *Harvard Business Review (December 2011)*
  `paper` · `intro` · `access: library`
  A managerial article on 'next best offer' (NBO) analytics. It gives a four-step framework (define objectives, gather data, analyze and execute, learn and evolve) with Tesco, Zappos, Microsoft and Walmart examples.
  *Use in wiki:* Short practitioner reading that frames response, propensity and recommender models as one NBO decision system.

- [optional] **[Recommenders: Best Practices on Recommendation Systems](https://github.com/recommenders-team/recommenders)** (2026) — Recommenders team (Linux Foundation AI & Data; originally Microsoft). *GitHub*
  `notebook` · `advanced` · `access: open` · `MIT`
  A large collection of notebooks and utilities for about 33 recommender algorithms (ALS, BPR, SAR, NCF, LightGCN, SASRec, content-based and others), with data prep, offline evaluation and tuning.
  *Use in wiki:* Source of quick-start notebooks for team projects that want a recommender, and instructor reference for evaluation metrics (precision@k, NDCG).
  Tools: recommenders, pyspark, lightgbm · Local copy: `07_M7_Predictive_Models_ML_and_AI/repos/recommenders-team__recommenders`

- [optional] **[Reducing Recommender System Biases: An Investigation of Rating Display Designs](https://misq.org/reeducing-recommender-system-biases-an-investigation-of-rating-display-designs.html)** (2019) — Adomavicius, G.; Bockstedt, J. C.; Curley, S. P.; Zhang, J. *MIS Quarterly 43(4), 1321–1341*
  `paper` · `advanced` · `access: library`
  Experiments show that displayed recommendation ratings anchor consumers' own ratings, and test display designs that reduce the bias. Recommenders thereby shape the very data they are later trained on.
  *Use in wiki:* Discussion reading on feedback loops between recommendation and measurement; ties M7 to M6.
  [Open-access copy](https://papers.ssrn.com/abstract=3346686)
  *Note:* Also on the MBA 542 Module 5 reading list. The MISQ URL contains a typo ('reeducing') on the publisher's own site.

- [optional] **[Evaluating Recommendation Systems](https://www.microsoft.com/en-us/research/publication/evaluating-recommender-systems/)** (2011) — Shani, G.; Gunawardana, A. *Recommender Systems Handbook (Springer), pp. 257–297*
  `book-chapter` · `intermediate` · `access: open`
  Standard reference on offline, user-study and online evaluation of recommenders, covering accuracy plus coverage, novelty, diversity, serendipity and trust.
  *Use in wiki:* Reference for an M7 exercise that moves beyond accuracy, such as diversity-aware re-ranking on the MBA 542 Netflix viewing data.
  *Note:* Also on the MBA 542 Module 5 reading list. Check that the Microsoft Research page links a PDF.

- [optional] **[SMOTE: Synthetic Minority Over-sampling Technique](https://jair.org/index.php/jair/article/view/10302)** (2002) — Chawla, N. V.; Bowyer, K. W.; Hall, L. O.; Kegelmeyer, W. P. *Journal of Artificial Intelligence Research 16, 321–357*
  `paper` · `intermediate` · `access: open` · `AI angle`
  Introduces oversampling of rare classes by interpolating synthetic minority examples, a standard tool for churn and response models where positives are rare.
  *Use in wiki:* Background for an imbalanced-churn exercise. Also a good AI-coding check: oversampling before the train/test split leaks information, and AI-written pipelines often make that mistake.
  [Open-access copy](https://arxiv.org/pdf/1106.1813) · Tools: imbalanced-learn, scikit-learn
  *Note:* Also on the MBA 542 Module 8 reading list. In practice, class weights or threshold tuning often work as well as SMOTE.

## Recommender system design: research evidence

- [core] **[The Value of Personalized Recommendations: Evidence from Netflix](https://www.ifo.de/en/cesifo/publications/2026/working-paper/value-personalized-recommendations-evidence-netflix)** (2026) — Zielnicki, K.; Aridor, G.; Bibaut, A.; Tran, A.; Chou, W.; Kallus, N. *Working paper, June 9, 2026; CESifo working paper (2026)*
  `paper` · `advanced` · `access: open`
  Uses Netflix viewership and recommendation exposure to estimate a discrete-choice model under conditional exogeneity of exposure. A randomized perturbation supplies diversion evidence for model validation. Model-based replacement with matrix factorization or popularity-based recommendation lowers engagement by about 4% or 12%, respectively.
  *Use in wiki:* The 'why firms invest in recommenders' anchor for M7. It pairs naturally with the MBA 542 synthetic Netflix viewing data.
  Local copy: `../Instructor_Private/01_Resources/07_M7_Recommender_Systems/Readings/ZielnickiAridorBibautTranChouKallus_WorkingPaper2025.pdf (Dropbox only; excluded from Git)`
  *Note:* The supplied PDF is dated June 9, 2026, despite 2025 in its filename. Results are model-based engagement counterfactuals, not direct experimental effects of full replacement or measures of consumer welfare. Abstract and identification discussion checked locally.

- [core] **[Consumption Variety in Food Recommendation](https://www.journals.uchicago.edu/doi/10.1086/720453)** (2022) — Nielsen, D. E.; Yang, N.; Dubé, L.; Knäuper, B.; Ling, Y.; Nie, J.-Y. *Journal of the Association for Consumer Research 7(4)*
  `paper` · `intermediate` · `access: library` · `© 2022 Association for Consumer Research; all rights reserved`
  Relates food-consumption variety to recorded calorie and food-composition changes in app logs, then conditions the FOODVAR sequential recommender on a variety-change indicator. Offline comparisons assess hit rate and NDCG; the study does not randomize users to a variety intervention.
  *Use in wiki:* Instructor's own paper. It moves from a descriptive regression (M3) to a design change in the recommender (M7), the full analytics-to-action arc the course teaches. Use it to motivate multi-objective re-ranking and evaluation beyond accuracy.
  DOI [10.1086/720453](https://doi.org/10.1086/720453) · Local copy: `../Instructor_Private/01_Resources/07_M7_Recommender_Systems/Yang_research/NYDKLN_JACR_2022.pdf (Dropbox only; excluded from Git)`
  *Note:* Also on the MBA 542 Module 5 reading list. Empirical analysis, FOODVAR sections, and Tables 3–5 checked locally. Evaluation uses 30 history days, seven validation days, and a final test day. The M8 category-bonus calculation is a separate synthetic illustration.

- [core] **[Following Good Examples: Health Goal-Oriented Food Recommendation based on Behavior Data](https://dl.acm.org/doi/10.1145/3485447.3514193)** (2022) — Ling, Y.; Nie, J.-Y.; Nielsen, D.; Knäuper, B.; Yang, N.; Dubé, L. *Proceedings of the ACM Web Conference 2022 (WWW '22)*
  `paper` · `intermediate` · `access: library` · `© 2022 ACM (publisher copyright)`
  Develops a sequential food recommender combining general, BMI-specific, and goal-specific models learned from food logs. Evaluation compares held-out foods in periods associated with the intended weight outcome; it does not estimate the causal effect of deploying recommendations on weight.
  *Use in wiki:* Instructor's own paper and the anchor case for the recommender unit: accuracy versus goal attainment, blending objectives, and an M6 caution that learning from 'successful' users builds selection into the training data. A good AI-assisted coding exercise is a goal-aware re-ranker on the synthetic viewing or grocery data.
  DOI [10.1145/3485447.3514193](https://doi.org/10.1145/3485447.3514193) · Local copy: `../Instructor_Private/01_Resources/07_M7_Recommender_Systems/Yang_research/LNNKYD_WWW_2022.pdf (Dropbox only; excluded from Git)`
  *Note:* Also on the MBA 542 Module 5 reading list. Local Sections 3.2 and 5 checked: selected active users, last-basket testing, and offline outcome-conditioned evaluation. M7 Section 7.12 distinguishes retrospective outcomes from inputs available at recommendation time.

- [core] **[The Economics of Recommender Systems: Evidence from a Field Experiment on MovieLens](https://www.econstor.eu/handle/10419/271773)** (2022) — Aridor, G.; Gonçalves, D.; Kluver, D.; Kong, R.; Konstan, J. A. *CESifo Working Paper 10129, November 2022*
  `paper` · `intermediate` · `access: open`
  A MovieLens field experiment distinguishes recommendation from exposure-only conditions and elicits beliefs. Evidence supports an informational role beyond exposing an item, with implications for consumption and information acquisition.
  *Use in wiki:* Bridges M6 and M7: a clean randomized evaluation of a recommender, the right comparison for any offline accuracy metric.
  Local copy: `../Instructor_Private/01_Resources/07_M7_Recommender_Systems/Readings/AridorGoncalvesKluverKongKonstan_WorkingPaper2022.pdf (Dropbox only; excluded from Git)`
  *Note:* Cites the supplied November 2022 version. A later retitled version is at https://arxiv.org/abs/2211.14219 . The intervention design and belief-elicitation discussion were checked locally.

- [core] **[How Algorithmic Confounding in Recommendation Systems Increases Homogeneity and Decreases Utility](https://www.arxiv.org/abs/1710.11214)** (2018) — Chaney, A. J. B.; Stewart, B. M.; Engelhardt, B. E. *ACM RecSys 2018*
  `paper` · `intermediate` · `access: open`
  Simulates recommender retraining on behavior shaped by prior recommendations. Under the modeled updating and preference processes, feedback can homogenize consumption without improving utility. The results concern a simulation mechanism, not a universal field estimate.
  *Use in wiki:* Key M6 + M7 idea for analysts: platform data reflect past recommendations, so naive models learn the algorithm's own footprint. A simulation students can reproduce with AI help.
  Local copy: `../Instructor_Private/01_Resources/07_M7_Recommender_Systems/Readings/ChaneyStewartEngelhardt_ACMRecSys2018.pdf (Dropbox only; excluded from Git)`

- [recommended] **[Can Explanations Improve Recommendations? Evidence from Prediction-Informed Explanations](https://arxiv.org/abs/2502.16759v3)** (2026) — Wang, Y.; Li, P.; Chen, M. *arXiv 2502.16759v3 (May 1, 2026; first posted February 2025)*
  `paper` · `advanced` · `access: open` · `AI angle`
  RecPIE alternates prediction-informed explanation generation and explanation-informed recommendation. The paper reports gains in offline point-of-interest ranking and a separate human evaluation of explanations. These evaluations do not establish a deployed effect on customer welfare.
  *Use in wiki:* Source paper for the RecPIE teaching artifact built for MBA 542 (accuracy-only vs. explainability-only vs. RecPIE modes). It could be reused directly on the M7 wiki page.
  *Note:* Version and authors checked against arXiv v3. A related NeurIPS 2025 version has a different subtitle; cite the specific version used.

- [recommended] **[Engagement, User Satisfaction, and the Amplification of Divisive Content on Social Media](https://pmc.ncbi.nlm.nih.gov/articles/PMC11894805/)** (2025) — Milli, S.; Carroll, M.; Wang, Y.; Pandey, S.; Zhao, S.; Dragan, A. D. *PNAS Nexus*
  `paper` · `intermediate` · `access: open`
  A preregistered Twitter audit with 806 users compares engagement-ranked posts with a reverse-chronological baseline and collects item-level stated preferences. Engagement ranking amplifies emotionally charged and out-group-hostile content; users do not prefer the selected political posts on the stated-preference measure.
  *Use in wiki:* Concrete evidence that the optimization target matters. A good M8 discussion piece on stated versus revealed preferences.
  DOI [10.1093/pnasnexus/pgaf062](https://doi.org/10.1093/pnasnexus/pgaf062) · Local copy: `../Instructor_Private/01_Resources/07_M7_Recommender_Systems/Readings/MilliCarrollPandeyWangDragan_PNASNexus2025.pdf (Dropbox only; excluded from Git)`
  *Note:* Corrected author order and restored Sebastian Zhao using the published article. This is an algorithmic audit, not assignment to long-term use of alternative feeds. Local PDF is a December 2024 preprint; linked publication is March 2025.

- [recommended] **[Short-term Exposure to Filter-Bubble Recommendation Systems Has Limited Polarization Effects: Naturalistic Experiments on YouTube](https://doi.org/10.1073/pnas.2318127122)** (2025) — Liu, N.; Hu, X. E.; Savas, Y.; Baum, M. A.; Berinsky, A. J.; Chaney, A. J. B.; Lucas, C.; Mariman, R.; de Benedictis-Kessner, J.; Guess, A. M.; Knox, D.; Stewart, B. M. *PNAS 122(8), e2318127122 (2025)*
  `paper` · `intermediate` · `access: open`
  Four experiments with nearly 9,000 participants manipulate recommendations on a YouTube-like interface and find limited short-term polarization effects in the studied settings. Exposure duration and attitude outcomes differ from audits of ranked content.
  *Use in wiki:* Counterweight to the filter-bubble narrative. Pair it with Milli et al. to show that evidence on recommender harms is mixed and depends on design.
  DOI [10.1073/pnas.2318127122](https://doi.org/10.1073/pnas.2318127122)
  *Note:* Full authors verified against PNAS and PubMed; Tucker is not an author. The legacy catalog ID is retained for stable references. Linked primary publication; no local PDF in this course folder.

- [recommended] **[Beyond Persuasion: Towards Conversational Recommender System with Credible Explanations](https://aclanthology.org/2024.findings-emnlp.247/)** (2024) — Qin, P.; Huang, C.; Deng, Y.; Lei, W.; Chua, T.-S. *Findings of EMNLP 2024*
  `paper` · `advanced` · `access: open` · `AI angle`
  Shows that LLM-based conversational recommenders can persuade users with explanations that are not credible, and proposes a method that keeps explanations persuasive but grounded in true item facts.
  *Use in wiki:* Counterpoint to RecPIE: LLM explanations can improve recommendations, but they can also mislead. Good for a class debate on AI shopping assistants (M8).
  DOI [10.18653/v1/2024.findings-emnlp.247](https://doi.org/10.18653/v1/2024.findings-emnlp.247) · Local copy: `../Instructor_Private/01_Resources/07_M7_Recommender_Systems/Readings/QinHuangDengLeiChua_EMNLP2024.pdf (Dropbox only; excluded from Git)`
  *Note:* Authors, venue, and pages verified against ACL Anthology and supplied PDF. PC-CRS evaluates credibility and persuasion separately; M7 connects the distinction to attribute-level factual checks.

- [recommended] **[The Challenge of Understanding What Users Want: Inconsistent Preferences and Engagement Optimization](https://arxiv.org/abs/2202.11776v1)** (2024) — Kleinberg, J.; Mullainathan, S.; Raghavan, M. *Management Science*
  `paper` · `advanced` · `access: open`
  Models users whose impulsive choices differ from their considered preferences and shows how optimizing a platform for engagement can serve the impulses at the expense of what users actually value.
  *Use in wiki:* Conceptual reading for the 'what should the recommender optimize?' discussion; pairs with the instructor's goal-oriented food recommendation paper.
  Local copy: `../Instructor_Private/01_Resources/07_M7_Recommender_Systems/Readings/KleinbergMullainathanRaghavan_ManagementScience2024.pdf (Dropbox only; excluded from Git)`
  *Note:* Venue from the local file name; the link is the arXiv version.

- [recommended] **[What are you optimizing for? Aligning Recommender Systems with Human Values](https://arxiv.org/abs/2107.10939v1)** (2021) — Stray, J.; Vendrov, I.; Nixon, J.; Adler, S.; Hadfield-Menell, D. *Working paper, arXiv 2107.10939v1 (July 2021)*
  `paper` · `intro` · `access: open`
  Accessible survey of how platforms have tried to make recommenders serve values beyond engagement (well-being, diversity, user control) and what metrics and data that requires.
  *Use in wiki:* Readable framing for the multi-objective design theme that runs through the MBA 542 recommender module and the instructor's food-recommendation papers.
  Local copy: `../Instructor_Private/01_Resources/07_M7_Recommender_Systems/Readings/StrayVendrovNixonAdlerHadfield-Menell_WorkingPaper2021.pdf (Dropbox only; excluded from Git)`
  *Note:* Local v1 text and author list checked. The catalog does not rely on the previously unconfirmed workshop attribution.

- [recommended] **[Recommendations as Treatments: Debiasing Learning and Evaluation](https://proceedings.mlr.press/v48/schnabel16.html)** (2016) — Schnabel, T.; Swaminathan, A.; Singh, A.; Chandak, N.; Joachims, T. *ICML 2016 (PMLR 48)*
  `paper` · `advanced` · `access: open`
  Treats recommendation and rating exposure as a treatment assignment problem and uses propensity weighting to correct the selection bias in observed ratings, for both evaluating and training recommenders.
  *Use in wiki:* Shows students that causal-inference tools from M6 (propensity scores, inverse weighting) apply directly to recommender evaluation.
  Local copy: `../Instructor_Private/01_Resources/07_M7_Recommender_Systems/Readings/SchnabelSwaminathanSinghChandakJoachims_ICML2016.pdf (Dropbox only; excluded from Git)`

- [optional] **[Unintended Consequences of Recommender System Interventions: Evidence from a Field Experiment](https://arxiv.org/abs/2606.08265v1)** (2026) — Luo, S.; Yao, S.; Zhang, D. J. *Working paper, arXiv 2606.08265v1 (June 2026)*
  `paper` · `advanced` · `access: open`
  Studies a temporary ranking boost for celebrity sleep-reminder videos in a randomized platform campaign. The analyzed active-user panel shows increased late-night and overall usage, with persistence after the campaign. The authors relate persistence to training signals and policy updates generated by the intervention.
  *Use in wiki:* Recent example for the M6/M7 discussion of spillovers and unintended outcomes in platform experiments.
  Local copy: `../Instructor_Private/01_Resources/07_M7_Recommender_Systems/Readings/LuoYaoZhang_WorkingPaper2026.pdf (Dropbox only; excluded from Git)`
  *Note:* Local Sections 4.2–4.3 and Table 6 checked. The analyzed panel contains 200,000 users active on the first experiment day. Reported 14.75% and 2.18% figures are relative assignment effects on usage. Mechanism attribution and sample inclusion require separate attention.

- [optional] **[Steering via Algorithmic Recommendations](https://doi.org/10.1111/1756-2171.12481)** (2024) — Chen, N.; Tsai, H.-T. *The RAND Journal of Economics 55(4), 501–518 (2024)*
  `paper` · `advanced` · `access: library`
  Empirical study of Amazon self-preferencing using product recommendation records and within-product variation from Amazon stockouts. Seller identity affects receipt of Frequently Bought Together recommendations, with controls and falsification checks addressing alternative explanations.
  *Use in wiki:* Case on platform incentives and observational identification in M6/M8. Explain the stockout comparison, accompanying price and availability changes, and the distinction between platform return and customer value.
  DOI [10.1111/1756-2171.12481](https://doi.org/10.1111/1756-2171.12481) · Local copy: `../Instructor_Private/01_Resources/07_M7_Recommender_Systems/Readings/ChenTsai_WorkingPaper2021.pdf (Dropbox only; excluded from Git)`
  *Note:* Corrected the earlier theory-only description. Publisher metadata verifies the 2024 article; the supplied local working paper is dated December 2020 despite 2021 in its filename.

- [optional] **[Understanding or Manipulation: Rethinking Online Performance Gains of Modern Recommender Systems](https://arxiv.org/abs/2210.05662v2)** (2023) — Zhu, Z.; Qin, R.; Huang, J.; Dai, X.; Yu, Y. [Yang]; Yu, Y. [Yong]; Zhang, W. *arXiv 2210.05662v2 (December 2023); related ACM Transactions on Information Systems article*
  `paper` · `advanced` · `access: open` · `CC BY-NC-ND 4.0 (arXiv version)`
  Develops a benchmark for distinguishing matching to initial preferences from preference shifts induced by recommendations. Experiments use synthetic and real-world datasets within that framework; click gains alone need not imply better matching to initial preferences.
  *Use in wiki:* A sharp caution for interpreting recommender A/B tests in M6: winning an experiment and serving users are not the same thing.
  DOI [10.1145/3637869](https://doi.org/10.1145/3637869) · Local copy: `../Instructor_Private/01_Resources/07_M7_Recommender_Systems/Readings/ZhuQinHuangDai_ACMTOIS2022.pdf (Dropbox only; excluded from Git)`
  *Note:* Seven-author list and December 2023 version checked against supplied PDF and arXiv. Local filename contains 2022, the first arXiv submission year. Benchmark experiments are not a general field estimate of manipulation.

- [optional] **[Is Seeing Believing? How Recommender Interfaces Affect Users' Opinions](https://experts.umn.edu/en/publications/is-seeing-believing-how-recommender-interfaces-affect-users-opini/)** (2003) — Cosley, D.; Lam, S. K.; Albert, I.; Konstan, J. A.; Riedl, J. *ACM CHI 2003*
  `paper` · `intro` · `access: library`
  Classic experiment in which showing users (sometimes manipulated) predicted ratings pulls their own re-ratings toward the displayed value: recommender interfaces anchor opinions.
  *Use in wiki:* Short classic that pairs with Adomavicius et al. (2019) in this folder; useful for discussing how recommenders contaminate the ratings they learn from.
  Local copy: `../Instructor_Private/01_Resources/07_M7_Recommender_Systems/Readings/CosleyLamAlbertKonstanRiedl_ACMSIGCHI2003.pdf (Dropbox only; excluded from Git)`

## Data leakage and AI-written pipelines

- [core] **[scikit-learn User Guide 12: Common pitfalls and recommended practices](https://scikit-learn.org/stable/common_pitfalls.html)** (2026) — scikit-learn developers. *scikit-learn 1.9.1 documentation*
  `documentation` · `intro` · `access: open` · `AI angle`
  Short worked examples of inconsistent preprocessing, data leakage (for example feature selection on the full data inflates accuracy from 0.5 to about 0.76 on pure noise) and random_state control, with Pipeline as the fix.
  *Use in wiki:* Required reading before students let an AI assistant write an ML pipeline. Use it as an audit checklist: 'find the leakage in this AI-generated notebook'.
  Tools: scikit-learn
  *Note:* These are exactly the bugs LLM-written notebooks often contain: fit_transform before the train/test split, and feature selection on the full data.

- [core] **[Leakage and the Reproducibility Crisis in ML-based Science](https://reproducible.cs.princeton.edu/)** (2023) — Kapoor, S.; Narayanan, A. *Patterns (Cell Press), 2023; arXiv 2207.07048*
  `paper` · `intermediate` · `access: open` · `AI angle`
  Documents leakage errors in hundreds of ML-based papers across many fields, gives an eight-type leakage taxonomy, and proposes 'model info sheets' to rule leakage out.
  *Use in wiki:* Use the taxonomy and model info sheet as a required appendix in student project write-ups, especially when AI wrote the pipeline.
  [Open-access copy](https://arxiv.org/abs/2207.07048)
  *Note:* The project page links the Patterns 2023 paper and keeps a table (updated May 2024) of 41 papers across 30 fields that document leakage errors, which together affect 648 papers.

- [recommended] **[MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering](https://arxiv.org/abs/2410.07095)** (2024) — Chan, J. S.; Chowdhury, N.; Jaffe, O.; Aung, J.; Sherburn, D.; et al. (OpenAI). *arXiv 2410.07095 (v6, February 2025)*
  `paper` · `advanced` · `access: open` · `MIT (code)` · `AI angle`
  A benchmark of 75 Kaggle competitions for AI agents. o1-preview with AIDE scaffolding reached medal level in 16.9% of competitions at release, and agents on the repo's paused leaderboard now score above 60%.
  *Use in wiki:* Discussion of how far 'AI does the ML for you' has come. Show the leaderboard and the rule-violation and plagiarism detectors as evidence of how agents can cheat.
  [Open-access copy](https://github.com/openai/mle-bench)
  *Note:* The full dataset is about 3.3 TB and the Lite split about 158 GB, so do not download it; use it for discussion only. The AIDE agent is at github.com/WecoAI/aideml (MIT; verified).

- [optional] **[Data Leakage in Notebooks: Static Detection and Better Processes](https://arxiv.org/abs/2209.03345)** (2022) — Yang, C.; Brower-Sinning, R. A.; Lewis, G. A.; Kästner, C. *arXiv 2209.03345 (cs.SE)*
  `paper` · `intermediate` · `access: open` · `AI angle`
  A static-analysis tool that detects common train/test leakage patterns in data-science notebooks. Leakage turns out to be widespread across more than 100,000 public notebooks, and the paper discusses processes to prevent it.
  *Use in wiki:* Evidence that leakage is the default failure in notebook code, which is also what LLMs learn from. Motivates the course rule: always split first and use a Pipeline.
  *Note:* arXiv lists no journal reference. I believe it appeared at ASE 2022, but that venue is unverified.

## LLMs as simulated consumers

- [core] **[Using large language models to generate silicon samples in consumer and marketing research: Challenges, opportunities, and guidelines](https://business.columbia.edu/faculty/research/using-large-language-models-generate-silicon-samples-consumer-and-marketing)** (2024) — Sarstedt, M.; Adler, S. J.; Rau, L.; Schmitt, B. *Psychology & Marketing 41(6): 1254-1270*
  `paper` · `intro` · `access: open` · `AI angle`
  A marketing-specific review of when LLM 'silicon samples' agree with human respondents, with practical guidelines on where they are useful (pilots, item generation) and where they are not (final estimates).
  *Use in wiki:* Assigned reading and checklist for any team that wants to use LLM respondents in its project.
  DOI [10.1002/mar.21982](https://doi.org/10.1002/mar.21982) · [Open-access copy](https://epub.ub.uni-muenchen.de/116232/)
  *Note:* The LMU ePub record links a PDF but states no license. That record lists three authors, while the Columbia page lists all four.

- [core] **[Out of One, Many: Using Language Models to Simulate Human Samples](https://www.cambridge.org/core/product/035D7C8A55B237942FB6DBAD7CAA4E49)** (2023) — Argyle, L. P.; Busby, E. C.; Fulda, N.; Gubler, J. R.; Rytting, C.; Wingate, D. *Political Analysis 31(3): 337-351*
  `paper` · `intermediate` · `access: open` · `AI angle`
  Introduces 'silicon samples': GPT-3 conditioned on demographic backstories reproduces subgroup response patterns from US political surveys ('algorithmic fidelity').
  *Use in wiki:* Foundational reading for the 'LLMs as simulated consumers' session. Students can run a small persona-prompting replication in Colab.
  DOI [10.1017/pan.2023.2](https://doi.org/10.1017/pan.2023.2) · [Open-access copy](https://arxiv.org/pdf/2209.06899) · Tools: openai, anthropic
  *Note:* The volume, issue and pages come from the IDEAS URL seen in search. The DOI appears on the Cambridge page as the supplementary-material DOI. Replication data is at doi 10.7910/DVN/JPV20K.

## Python for marketing analytics: notebooks and code

- [core] **[mlxtend user guide: apriori, FP-growth, FP-max, H-mine and association_rules notebooks](https://github.com/rasbt/mlxtend)** (2026) — Raschka, S. *GitHub (rasbt/mlxtend); docs at rasbt.github.io/mlxtend*
  `notebook` · `intro` · `access: open` · `BSD-3-Clause`
  The standard Python market-basket workflow: one-hot transaction encoding, frequent itemsets (apriori, fpgrowth), and association rules with support, confidence, lift, leverage and conviction.
  *Use in wiki:* In-class coding activity on the UCI Online Retail data (already in the library): students reproduce the mlxtend examples on real baskets and interpret lift for cross-selling.
  Tools: mlxtend, pandas · Local copy: `04_M4_Conjoint_Segmentation_CLV/repos/rasbt__mlxtend`
  *Note:* Last commit 2026-09-29. The current association_rules notebook passes a num_itemsets argument (association_rules(..., num_itemsets=len(df.index))) that older tutorials and many AI-generated snippets omit, so version mismatches are a likely, teachable failure mode for AI assistants.

- [recommended] **[implicit: fast collaborative filtering for implicit feedback (Last.fm tutorial notebook)](https://github.com/benfred/implicit)** (2026) — Frederickson, B. *GitHub (benfred/implicit)*
  `package` · `intermediate` · `access: open` · `MIT`
  Widely used ALS, BPR and logistic-MF recommender package for clicks, plays and purchases (implicit feedback). The examples include a Last.fm tutorial notebook and MovieLens and Last.fm scripts.
  *Use in wiki:* Short lab on 'customers who bought X' recommendations from purchase logs. It complements the broader recommenders-team/recommenders library already in the library.
  Tools: implicit, scipy · Local copy: `07_M7_Predictive_Models_ML_and_AI/repos/benfred__implicit`
  *Note:* Last commit 2026-05-08.

- [recommended] **[lifelines example notebooks: Customer Churn, SaaS churn with piecewise models, time-lagged conversion rates](https://github.com/CamDavidsonPilon/lifelines)** (2026) — Davidson-Pilon, C. and contributors. *GitHub (CamDavidsonPilon/lifelines)*
  `notebook` · `intermediate` · `access: open` · `MIT`
  Survival-analysis notebooks on marketing questions: survival models for customer churn, piecewise-exponential SaaS churn, and modeling delayed (time-lagged) conversions.
  *Use in wiki:* Shows 'time to churn' as an alternative to binary churn classifiers, and links naturally to CLV in M4.
  Tools: lifelines, pandas · Local copy: `07_M7_Predictive_Models_ML_and_AI/repos/CamDavidsonPilon__lifelines`
  *Note:* lifelines last commit 2026-03-06. It is the maintained sibling of the archived `lifetimes` package. Check whether each notebook's data URL still resolves.

- [recommended] **[Fighting Churn with Data (companion code)](https://github.com/carl24k/fight-churn)** (2020) — Gold, C. *Manning (December 2020)*
  `notebook` · `intermediate` · `access: open` · `MIT`
  Python package and listings for a book on subscription churn: defining churn and retention rates, behavioral metrics from event data, cohort comparisons, churn forecasting and segmentation by behavior. Includes ChurnSim, a simulator that generates realistic customer event data.
  *Use in wiki:* Instructor background for retention-metric definitions in M2/M4. ChurnSim can generate a private dataset for the team project.
  Tools: pandas, postgresql, scikit-learn, shap · Local copy: `07_M7_Predictive_Models_ML_and_AI/repos/carl24k__fight-churn`
  *Note:* Needs PostgreSQL, which is heavier than Colab-only workflows. The newer crm5 simulation takes about an hour and produces about 30 GB in Postgres. Supports Python 3.9–3.12. Last push 2025-08.

- [optional] **[Analytics componentized patterns: BQML propensity-to-purchase, GA4 churn propensity, clustering and LTV notebooks](https://github.com/GoogleCloudPlatform/analytics-componentized-patterns)** (2026) — Google Cloud. *GitHub (GoogleCloudPlatform/analytics-componentized-patterns)*
  `notebook` · `intermediate` · `access: open` · `Apache-2.0`
  Notebooks that build propensity-to-purchase on Google Analytics sample data, churn propensity on GA4 gaming data, k-means segmentation, and AutoML LTV with lookalike activation, all inside BigQuery ML.
  *Use in wiki:* Shows students the SQL-first (BQML) route to propensity and segmentation models, a useful contrast to scikit-learn workflows.
  Tools: bigquery-ml, kubeflow-pipelines, vertex-ai
  *Note:* Needs a GCP project, though BigQuery sandbox or free tier can cover the SQL parts. Some notebooks use older KFP and AI Platform APIs, so treat them as patterns rather than turnkey labs. Repo last commit 2026-05-11; individual notebook dates were not checked.

- [optional] **[LightFM: hybrid recommendation with user and item features (quickstart, MovieLens, WARP loss notebooks)](https://github.com/lyst/lightfm)** (2023) — Lyst (Kula, M.). *GitHub (lyst/lightfm)*
  `package` · `intermediate` · `access: open` · `Apache-2.0`
  Hybrid matrix factorization that uses item and user metadata, which helps with cold-start products. Example notebooks cover the quickstart, MovieLens, learning schedules, WARP loss, and a StackExchange hybrid model.
  *Use in wiki:* Optional: shows how product attributes enter a recommender. Pair it with the cold-start discussion in M7.
  Tools: lightfm
  *Note:* STALE: last commit 2023-04-30 and no recent releases. It is a C-extension build, so test the pip install on current Colab and Python before assigning.

## AI-assisted coding angle for this module

Resources in this folder that show the method done with AI help, LLM versions of the method, or documented failure modes of AI-written analysis:

- [scikit-learn User Guide 12: Common pitfalls and recommended practices](https://scikit-learn.org/stable/common_pitfalls.html)
- [Using large language models to generate silicon samples in consumer and marketing research: Challenges, opportunities, and guidelines](https://business.columbia.edu/faculty/research/using-large-language-models-generate-silicon-samples-consumer-and-marketing)
- [Leakage and the Reproducibility Crisis in ML-based Science](https://reproducible.cs.princeton.edu/)
- [Out of One, Many: Using Language Models to Simulate Human Samples](https://www.cambridge.org/core/product/035D7C8A55B237942FB6DBAD7CAA4E49)
- [AutoGluon Tabular: Quick Start](https://auto.gluon.ai/stable/tutorials/tabular/tabular-quick-start.html)
- [Can Explanations Improve Recommendations? Evidence from Prediction-Informed Explanations](https://arxiv.org/abs/2502.16759v3)
- [Beyond Persuasion: Towards Conversational Recommender System with Credible Explanations](https://aclanthology.org/2024.findings-emnlp.247/)
- [Machine Learning Crash Course (refreshed edition)](https://developers.google.com/machine-learning/crash-course)
- [MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering](https://arxiv.org/abs/2410.07095)
- [TabPFN: Accurate predictions on small data with a tabular foundation model](https://github.com/PriorLabs/TabPFN)
- [Data Leakage in Notebooks: Static Detection and Better Processes](https://arxiv.org/abs/2209.03345)
- [SMOTE: Synthetic Minority Over-sampling Technique](https://jair.org/index.php/jair/article/view/10302)

## Also relevant (catalogued in other folders)

- **`01_M1_Marketing_Analytics_and_Python`**: [A Strategic Framework for Artificial Intelligence in Marketing](https://link.springer.com/article/10.1007/s11747-020-00749-9); [Applying Data Analytics in Marketing](https://www.coursera.org/learn/applying-data-analytics-business-in-marketing); [Marketing Analytics Jumpstart (Google Cloud)](https://github.com/GoogleCloudPlatform/marketing-analytics-jumpstart)
- **`03_M3_Regression`**: [PyBLP tutorial notebooks (logit and nested logit, Nevo cereal, BLP autos, Petrin micro moments, post-estimation, simulation)](https://github.com/jeffgortmaker/pyblp); [Mixtape Sessions: Demand Estimation (BLP workshop with PyBLP exercises and solutions)](https://github.com/Mixtape-Sessions/Demand-Estimation)
- **`04_M4_Conjoint_Segmentation_CLV`**: [Juan Orduz website projects: Bayesian marketing-analytics notebooks](https://github.com/juanitorduz/website_projects); [AI-Human Hybrids for Marketing Research: Leveraging Large Language Models (LLMs) as Collaborators](https://journals.sagepub.com/doi/10.1177/00222429241276529); [TensorHouse: reference notebooks for marketing, promotions and pricing (successor to Introduction to Algorithmic Marketing examples)](https://github.com/ikatsov/tensor-house); [The Challenge of Using LLMs to Simulate Human Behavior: A Causal Inference Perspective](https://arxiv.org/abs/2312.15524); [Using LLMs for Market Research](https://papers.ssrn.com/abstract=4395751); [scikit-learn User Guide: Clustering, and Gaussian Mixture Models](https://scikit-learn.org/stable/modules/clustering.html); [Crystalvalue: predictive customer lifetime value (pLTV) on Google Cloud Vertex AI](https://github.com/google-marketing-solutions/crystalvalue); [lifetime_value: Customer LTV prediction with zero-inflated lognormal loss (notebooks)](https://github.com/google/lifetime_value); [Choice-Learn: discrete choice modeling with large datasets](https://github.com/artefactory/choice-learn)
- **`05_M5_Text_and_Social_Media_Analytics`**: [OpenAI Cookbook: embedding and classification notebooks on Amazon fine-food reviews, plus structured outputs and synthetic data](https://github.com/openai/openai-cookbook); [Transformers Pipelines documentation (text-classification, zero-shot-classification)](https://huggingface.co/docs/transformers/main_classes/pipelines); [Working With Text Data (scikit-learn tutorial)](https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html); [Frontiers: Determining the Validity of Large Language Models for Automated Perceptual Analysis](https://doi.org/10.1287/mksc.2023.0454); [Hands-On Large Language Models (official code repository)](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models); [More than a Feeling: Accuracy and Application of Sentiment Analysis](https://www.sciencedirect.com/science/article/pii/S0167811622000477); [Sentence Transformers (SBERT) documentation](https://sbert.net/); [Comparing automated text classification methods](https://doi.org/10.1016/j.ijresmar.2018.09.009); [Identifying Customer Needs from User-Generated Content](https://doi.org/10.1287/mksc.2018.1123); [SetFit notebooks: few-shot and zero-shot text classification with sentence transformers](https://github.com/huggingface/setfit)
- **`06_M6_Causal_Inference_and_Experiments`**: [CausalML: uplift modeling and causal inference with ML (Uber)](https://github.com/uber/causalml); [Causal Inference in Python: Applying Causal Inference in the Tech Industry](https://www.oreilly.com/library/view/causal-inference-in/9781098140243/); [Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus?](https://www.nber.org/papers/w31122); [Retention Futility: Targeting High-Risk Customers Might Be Ineffective](https://journals.sagepub.com/doi/10.1509/jmr.16.0163); [MineThatData E-Mail Analytics and Data Mining Challenge (Hillstrom dataset)](https://blog.minethatdata.com/2008/03/minethatdata-e-mail-analytics-and-data.html); [scikit-uplift (sklift): uplift modeling in scikit-learn style](https://github.com/maks-sh/scikit-uplift); [AI-Assisted Statistics for Data Scientists: 50+ Essential Concepts Using R and Python, 3rd ed. (code)](https://github.com/gedeck/ai-assisted-statistics-for-data-scientists); [Matteo Courthoud's causal data science blog notebooks](https://github.com/matteocourthoud/Blog-Posts); [Heterogeneous Treatment Effects and Optimal Targeting Policy Evaluation](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3111957); [EconML: heterogeneous treatment effect estimation with ML (PyWhy)](https://github.com/py-why/EconML); [Fractional Uplift: uplift modelling with complex or constrained metrics](https://github.com/google-marketing-solutions/fractional_uplift); [Orbit: Bayesian time-series forecasting and KTR time-varying regression (Uber)](https://github.com/uber/orbit); [Effective-Uplift-Modeling (PyData London 2024 / SciPy 2024 talk materials)](https://github.com/takechanman1228/Effective-Uplift-Modeling); [DoubleML: an object-oriented implementation of double machine learning in Python](https://JMLR.org/papers/v23/21-0862.html)
- **`10_AI_Coding_Concepts_and_Evidence`**: [Andrej Karpathy: Software Is Changing (Again)](https://www.youtube.com/watch?v=LCEmiRjPEtQ); [Who is using AI to code? Global diffusion and impact of generative AI](https://arxiv.org/abs/2506.08945); [DSBench: How Far Are Data Science Agents from Becoming Data Science Experts?](https://arxiv.org/abs/2409.07703); [Benchmarking Data Science Agents (DSEval)](https://arxiv.org/abs/2402.17168); [DA-Code: Agent Data Science Code Generation Benchmark for Large Language Models](https://arxiv.org/abs/2410.07331); [DS-1000: A Natural and Reliable Benchmark for Data Science Code Generation](https://arxiv.org/abs/2211.11501)
- **`11_AI_Coding_Tools_and_Workflows`**: [Data Science Agent in Colab: The future of data analysis with Gemini](https://developers.googleblog.com/en/data-science-agent-in-colab-with-gemini/); [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/); [Claude Cookbooks (anthropics/claude-cookbooks)](https://github.com/anthropics/claude-cookbooks); [Generative AI for Beginners (21 lessons)](https://github.com/microsoft/generative-ai-for-beginners)
- **`20_Datasets`**: [Amazon Reviews 2023 (Amazon Reviews'23)](https://amazon-reviews-2023.github.io/); [MovieLens datasets (ml-latest-small, ml-32m)](https://grouplens.org/datasets/movielens/); [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce); [Google Analytics 4 sample ecommerce dataset (Google Merchandise Store) in BigQuery](https://developers.google.com/analytics/bigquery/web-ecommerce-demo-dataset); [Bank Marketing](https://archive.ics.uci.edu/dataset/222/bank+marketing); [Kevin Hillstrom MineThatData E-Mail Analytics Challenge dataset](https://www.uplift-modeling.com/en/latest/api/datasets/fetch_hillstrom.html); [Telco Customer Churn (IBM sample data)](https://github.com/IBM/telco-customer-churn-on-icp4d); [Stanford Large Network Dataset Collection (SNAP)](https://snap.stanford.edu/data/); [Yelp Open Dataset](https://business.yelp.com/data/resources/open-dataset/); [Online Shoppers Purchasing Intention Dataset](https://archive.ics.uci.edu/dataset/468/online+shoppers+purchasing+intention+dataset); [Criteo Uplift Prediction Dataset (v2.1)](https://ailab.criteo.com/?p=859); [The Instacart Online Grocery Shopping Dataset 2017](https://tech.instacart.com/3-million-instacart-orders-open-sourced-d40d29ead6f2); [Hugging Face Datasets Hub](https://huggingface.co/datasets); [Kaggle Datasets](https://www.kaggle.com/datasets); [dmba: utilities and datasets for Machine Learning (Data Mining) for Business Analytics, Python editions](https://github.com/gedeck/dmba); [CTR prediction benchmarks: Avazu (Kaggle) and Criteo 1TB Click Logs](https://www.kaggle.com/c/avazu-ctr-prediction); [H&M Personalized Fashion Recommendations (Kaggle competition data)](https://www.kaggle.com/competitions/h-and-m-personalized-fashion-recommendations); [Open Bandit Dataset and Open Bandit Pipeline](https://github.com/st-tech/zr-obp)
- **`21_Open_Textbooks_and_Courses`**: [An Introduction to Statistical Learning with Applications in Python (ISLP)](https://www.statlearning.com/); [Causal Inference for the Brave and True](https://matheusfacure.github.io/python-causality-handbook/landing-page.html); [Python for Marketing Research and Analytics](https://python-marketing-research.github.io/); [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/); [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1); [Marketing Analytics and Data Science: Tools and Models (supplementary code)](https://link.springer.com/book/9783032111296); [Speech and Language Processing, 3rd ed. draft](https://web.stanford.edu/~jurafsky/slp3/); [Applied Marketing Analytics Using Python](https://collegepublishing.sagepub.com/products/applied-marketing-analytics-using-python-1-288563); [Data 100 Course Notes: Principles and Techniques of Data Science](https://ds100.org/course-notes/); [Applied Causal Inference Powered by ML and AI](https://causalml-book.org/); [Machine Learning and Generative AI for Marketing (companion code)](https://github.com/PacktPublishing/Machine-Learning-and-Generative-AI-for-Marketing); [Data Science for Marketing Analytics, Second Edition (companion code)](https://github.com/PacktPublishing/Data-Science-for-Marketing-Analytics-Second-Edition); [Dealing with Data (NYU teaching notebooks)](https://github.com/ipeirotis/dealing_with_data); [Kaggle Learn micro-courses](https://www.kaggle.com/learn); [QuantEcon DataScience: Introduction to Economic Modeling and Data Science](https://datascience.quantecon.org/); [Practical Deep Learning for Coders](https://course.fast.ai/); [Data Science for Marketing Analytics (first edition, companion code)](https://github.com/TrainingByPackt/Data-Science-for-Marketing-Analytics); [Business Data Science: code and examples](https://github.com/TaddyLab/BDS); [Hands-On Data Science for Marketing (code repository)](https://github.com/PacktPublishing/Hands-On-Data-Science-for-Marketing); [pyrsm and Radiant: business-analytics teaching tools from UCSD Rady](https://pypi.org/project/pyrsm/)
- **`22_Wiki_Design_and_Hosting`**: [Packages built in Pyodide](https://pyodide.org/en/stable/usage/packages-in-pyodide.html); [MLU-Explain](https://mlu-explain.github.io/); [Distill Hiatus](https://distill.pub/2021/distill-hiatus/)
