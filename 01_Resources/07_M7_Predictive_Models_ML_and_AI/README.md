# M7 · Predictive Models, AI and Machine Learning

29 resources (16 core). Built 2026-10-23 from `00_Index/_data/`; edit the YAML there and rerun `00_Index/_build/build_catalog.py` rather than editing this file.

Priority: **core** = likely to assign or build on; **recommended** = strong supplement; **optional** = background or niche. *Access* tells you whether students can open it without a login.

## Contents

- [Core ML for business students](#core-ml-for-business-students) (10)
- [Prediction vs. causation](#prediction-vs-causation) (3)
- [Marketing prediction problems](#marketing-prediction-problems) (10)
- [Data leakage and AI-written pipelines](#data-leakage-and-ai-written-pipelines) (4)
- [LLMs as simulated consumers](#llms-as-simulated-consumers) (2)

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
  [Open-access copy](https://surprise.readthedocs.io/en/stable/index.html) · Tools: scikit-surprise
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

## AI-assisted coding angle for this module

Resources in this folder that show the method done with AI help, LLM versions of the method, or documented failure modes of AI-written analysis:

- [scikit-learn User Guide 12: Common pitfalls and recommended practices](https://scikit-learn.org/stable/common_pitfalls.html)
- [Using large language models to generate silicon samples in consumer and marketing research: Challenges, opportunities, and guidelines](https://business.columbia.edu/faculty/research/using-large-language-models-generate-silicon-samples-consumer-and-marketing)
- [Leakage and the Reproducibility Crisis in ML-based Science](https://reproducible.cs.princeton.edu/)
- [Out of One, Many: Using Language Models to Simulate Human Samples](https://www.cambridge.org/core/product/035D7C8A55B237942FB6DBAD7CAA4E49)
- [AutoGluon Tabular: Quick Start](https://auto.gluon.ai/stable/tutorials/tabular/tabular-quick-start.html)
- [Machine Learning Crash Course (refreshed edition)](https://developers.google.com/machine-learning/crash-course)
- [MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering](https://arxiv.org/abs/2410.07095)
- [TabPFN: Accurate predictions on small data with a tabular foundation model](https://github.com/PriorLabs/TabPFN)
- [Data Leakage in Notebooks: Static Detection and Better Processes](https://arxiv.org/abs/2209.03345)

## Also relevant (catalogued in other folders)

- **`01_M1_Marketing_Analytics_and_Python`**: [A Strategic Framework for Artificial Intelligence in Marketing](https://link.springer.com/article/10.1007/s11747-020-00749-9); [Applying Data Analytics in Marketing](https://www.coursera.org/learn/applying-data-analytics-business-in-marketing)
- **`04_M4_Conjoint_Segmentation_CLV`**: [AI-Human Hybrids for Marketing Research: Leveraging Large Language Models (LLMs) as Collaborators](https://journals.sagepub.com/doi/10.1177/00222429241276529); [The Challenge of Using LLMs to Simulate Human Behavior: A Causal Inference Perspective](https://arxiv.org/abs/2312.15524); [Using LLMs for Market Research](https://papers.ssrn.com/abstract=4395751); [scikit-learn User Guide: Clustering, and Gaussian Mixture Models](https://scikit-learn.org/stable/modules/clustering.html); [Choice-Learn: discrete choice modeling with large datasets](https://github.com/artefactory/choice-learn)
- **`05_M5_Text_and_Social_Media_Analytics`**: [Transformers Pipelines documentation (text-classification, zero-shot-classification)](https://huggingface.co/docs/transformers/main_classes/pipelines); [Working With Text Data (scikit-learn tutorial)](https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html); [Frontiers: Determining the Validity of Large Language Models for Automated Perceptual Analysis](https://doi.org/10.1287/mksc.2023.0454); [Hands-On Large Language Models (official code repository)](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models); [More than a Feeling: Accuracy and Application of Sentiment Analysis](https://www.sciencedirect.com/science/article/pii/S0167811622000477); [Sentence Transformers (SBERT) documentation](https://sbert.net/); [Comparing automated text classification methods](https://doi.org/10.1016/j.ijresmar.2018.09.009); [Identifying Customer Needs from User-Generated Content](https://doi.org/10.1287/mksc.2018.1123)
- **`06_M6_Causal_Inference_and_Experiments`**: [CausalML: uplift modeling and causal inference with ML (Uber)](https://github.com/uber/causalml); [Causal Inference in Python: Applying Causal Inference in the Tech Industry](https://www.oreilly.com/library/view/causal-inference-in/9781098140243/); [Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus?](https://www.nber.org/papers/w31122); [Retention Futility: Targeting High-Risk Customers Might Be Ineffective](https://journals.sagepub.com/doi/10.1509/jmr.16.0163); [MineThatData E-Mail Analytics and Data Mining Challenge (Hillstrom dataset)](https://blog.minethatdata.com/2008/03/minethatdata-e-mail-analytics-and-data.html); [scikit-uplift (sklift): uplift modeling in scikit-learn style](https://github.com/maks-sh/scikit-uplift); [Heterogeneous Treatment Effects and Optimal Targeting Policy Evaluation](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3111957); [EconML: heterogeneous treatment effect estimation with ML (PyWhy)](https://github.com/py-why/EconML); [DoubleML: an object-oriented implementation of double machine learning in Python](https://JMLR.org/papers/v23/21-0862.html)
- **`10_AI_Coding_Concepts_and_Evidence`**: [Andrej Karpathy: Software Is Changing (Again)](https://www.youtube.com/watch?v=LCEmiRjPEtQ); [Who is using AI to code? Global diffusion and impact of generative AI](https://arxiv.org/abs/2506.08945); [DSBench: How Far Are Data Science Agents from Becoming Data Science Experts?](https://arxiv.org/abs/2409.07703); [Benchmarking Data Science Agents (DSEval)](https://arxiv.org/abs/2402.17168); [DA-Code: Agent Data Science Code Generation Benchmark for Large Language Models](https://arxiv.org/abs/2410.07331); [DS-1000: A Natural and Reliable Benchmark for Data Science Code Generation](https://arxiv.org/abs/2211.11501)
- **`11_AI_Coding_Tools_and_Workflows`**: [Data Science Agent in Colab: The future of data analysis with Gemini](https://developers.googleblog.com/en/data-science-agent-in-colab-with-gemini/); [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/); [Claude Cookbooks (anthropics/claude-cookbooks)](https://github.com/anthropics/claude-cookbooks); [Generative AI for Beginners (21 lessons)](https://github.com/microsoft/generative-ai-for-beginners)
- **`20_Datasets`**: [Amazon Reviews 2023 (Amazon Reviews'23)](https://amazon-reviews-2023.github.io/); [MovieLens datasets (ml-latest-small, ml-32m)](https://grouplens.org/datasets/movielens/); [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce); [Google Analytics 4 sample ecommerce dataset (Google Merchandise Store) in BigQuery](https://developers.google.com/analytics/bigquery/web-ecommerce-demo-dataset); [Bank Marketing](https://archive.ics.uci.edu/dataset/222/bank+marketing); [Kevin Hillstrom MineThatData E-Mail Analytics Challenge dataset](https://www.uplift-modeling.com/en/latest/api/datasets/fetch_hillstrom.html); [Telco Customer Churn (IBM sample data)](https://github.com/IBM/telco-customer-churn-on-icp4d); [Stanford Large Network Dataset Collection (SNAP)](https://snap.stanford.edu/data/); [Yelp Open Dataset](https://business.yelp.com/data/resources/open-dataset/); [Online Shoppers Purchasing Intention Dataset](https://archive.ics.uci.edu/dataset/468/online+shoppers+purchasing+intention+dataset); [Criteo Uplift Prediction Dataset (v2.1)](https://ailab.criteo.com/?p=859); [The Instacart Online Grocery Shopping Dataset 2017](https://tech.instacart.com/3-million-instacart-orders-open-sourced-d40d29ead6f2); [Hugging Face Datasets Hub](https://huggingface.co/datasets); [Kaggle Datasets](https://www.kaggle.com/datasets); [CTR prediction benchmarks: Avazu (Kaggle) and Criteo 1TB Click Logs](https://www.kaggle.com/c/avazu-ctr-prediction); [H&M Personalized Fashion Recommendations (Kaggle competition data)](https://www.kaggle.com/competitions/h-and-m-personalized-fashion-recommendations); [Open Bandit Dataset and Open Bandit Pipeline](https://github.com/st-tech/zr-obp)
- **`21_Open_Textbooks_and_Courses`**: [An Introduction to Statistical Learning with Applications in Python (ISLP)](https://www.statlearning.com/); [Causal Inference for the Brave and True](https://matheusfacure.github.io/python-causality-handbook/landing-page.html); [Python for Marketing Research and Analytics](https://python-marketing-research.github.io/); [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/); [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1); [Speech and Language Processing, 3rd ed. draft](https://web.stanford.edu/~jurafsky/slp3/); [Data 100 Course Notes: Principles and Techniques of Data Science](https://ds100.org/course-notes/); [Applied Causal Inference Powered by ML and AI](https://causalml-book.org/); [Dealing with Data (NYU teaching notebooks)](https://github.com/ipeirotis/dealing_with_data); [Kaggle Learn micro-courses](https://www.kaggle.com/learn); [QuantEcon DataScience: Introduction to Economic Modeling and Data Science](https://datascience.quantecon.org/); [Practical Deep Learning for Coders](https://course.fast.ai/); [Business Data Science: code and examples](https://github.com/TaddyLab/BDS); [Hands-On Data Science for Marketing (code repository)](https://github.com/PacktPublishing/Hands-On-Data-Science-for-Marketing); [pyrsm and Radiant: business-analytics teaching tools from UCSD Rady](https://pypi.org/project/pyrsm/)
- **`22_Wiki_Design_and_Hosting`**: [Packages built in Pyodide](https://pyodide.org/en/stable/usage/packages-in-pyodide.html); [MLU-Explain](https://mlu-explain.github.io/); [Distill Hiatus](https://distill.pub/2021/distill-hiatus/)
