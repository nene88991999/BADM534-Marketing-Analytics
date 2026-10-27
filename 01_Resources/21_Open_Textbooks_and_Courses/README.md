# Open Textbooks and Courses (cross-module)

42 resources (13 core). Built 2026-10-26 from `00_Index/_data/`; edit the YAML there and rerun `00_Index/_build/build_catalog.py` rather than editing this file.

Priority: **core** = likely to assign or build on; **recommended** = strong supplement; **optional** = background or niche. *Access* tells you whether students can open it without a login.

## Contents

- [Python and data science foundations](#python-and-data-science-foundations) (13)
- [Python for economists and econometrics](#python-for-economists-and-econometrics) (3)
- [Marketing analytics books and peer courses](#marketing-analytics-books-and-peer-courses) (9)
- [Causal inference](#causal-inference) (3)
- [Machine learning, NLP and visualization](#machine-learning-nlp-and-visualization) (5)
- [Python for marketing analytics: notebooks and code](#python-for-marketing-analytics-notebooks-and-code) (9)

## Python and data science foundations

- [core] **[The Missing Semester of Your CS Education](https://missing.csail.mit.edu/)** (2026) — MIT CSAIL (Missing Semester instructors). *MIT*
  `course` · `intro` · `access: open` · `CC BY-NC-SA` · `AI angle`
  MIT's short course on the shell, command-line environment, Git, development tools, debugging, packaging and code quality. The January 2026 edition adds an 'Agentic Coding' lecture and folds AI tools into every lecture.
  *Use in wiki:* Assign the Git and Agentic Coding lectures before the team project; a model for teaching AI coding tools alongside fundamentals.
  Tools: git, shell

- [core] **[AI Python for Beginners](https://www.deeplearning.ai/short-courses/ai-python-for-beginners/)** (2024) — Ng, A. (DeepLearning.AI). *DeepLearning.AI*
  `course` · `intro` · `access: free-registration` · `AI angle`
  11.5-hour beginner course on Python basics, files and CSVs, matplotlib, web scraping, packages and APIs. A built-in AI assistant helps learners write, test and debug code.
  *Use in wiki:* Pre-course onboarding for students new to Python that introduces AI-assisted coding from day one.
  Tools: python, matplotlib, beautifulsoup
  *Note:* Free during the platform beta; a certificate requires a PRO membership.

- [core] **[Python for Data Analysis, 3rd Edition (Open Access)](https://wesmckinney.com/book/)** (2022) — McKinney, W. *O'Reilly Media; wesmckinney.com*
  `book` · `intro` · `access: open` · `Online text free to read, not to be copied; code examples MIT`
  The pandas creator's guide to data wrangling with pandas, NumPy and Jupyter. The full 3rd edition is free to read online.
  *Use in wiki:* Assigned reading for M1-M2 (pandas basics, groupby, time series). Link to chapters from the wiki rather than copying text.
  Tools: pandas, numpy, matplotlib

- [core] **[Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)** (2016) — VanderPlas, J. *O'Reilly Media; GitHub*
  `book` · `intro` · `access: open` · `Text CC BY-NC-ND 3.0; code MIT`
  The full book as Jupyter notebooks, covering IPython, NumPy, pandas, Matplotlib and scikit-learn (including k-means and Gaussian mixture clustering).
  *Use in wiki:* Embed or launch notebooks for M4 clustering and M7 scikit-learn workflows.
  Tools: numpy, pandas, matplotlib, scikit-learn · Local copy: `21_Open_Textbooks_and_Courses/repos/jakevdp__PythonDataScienceHandbook`
  *Note:* The repo also has notebooks_v1 and notebooks_v2 folders (v2 presumably matches the 2nd edition; not confirmed). Edition years were not verified.

- [core] **[Think Python, 3rd Edition](https://allendowney.github.io/ThinkPython/)** — Downey, A. B. *Green Tea Press / O'Reilly*
  `book` · `intro` · `access: open` · `CC BY-NC-SA 4.0` · `AI angle`
  Beginner Python textbook with every chapter (1-19) as a Colab notebook. Each chapter ends with suggestions for using ChatGPT and Colab AI to learn more and get help with exercises.
  *Use in wiki:* M1 primer for non-programmers. Its end-of-chapter AI-assistant prompts model a 'learn with AI, verify yourself' habit.
  Tools: python, colab

- [recommended] **[Data 100 Course Notes: Principles and Techniques of Data Science](https://ds100.org/course-notes/)** (2025) — UC Berkeley Data 100 course staff. *UC Berkeley (ds100.org)*
  `course` · `intermediate` · `access: open` · `BSD-3-Clause`
  Fall 2025 notes on pandas EDA, regex, visualization, sampling, linear models, gradient descent, feature engineering, cross-validation and regularization, the bootstrap, logistic regression, clustering and PCA.
  *Use in wiki:* Concise readings to pair with modules; the regex and feature-engineering notes fit M5 and M7.
  Tools: pandas, scikit-learn, seaborn

- [recommended] **[Computational and Inferential Thinking: The Foundations of Data Science, 2nd ed. (Berkeley Data 8)](https://inferentialthinking.com/)** — Adhikari, A.; DeNero, J.; Wagner, D. *UC Berkeley*
  `book` · `intro` · `access: open` · `CC BY-NC-ND 4.0`
  Data 8 textbook covering causality and experiments, Python tables and visualization, sampling, hypothesis testing, comparing two samples (A/B tests), estimation, regression inference and classification.
  *Use in wiki:* A gentle, simulation-based treatment of A/B testing and permutation tests for non-CS students in M6.
  Tools: python, datascience
  *Note:* Uses Berkeley's own 'datascience' Tables library rather than pandas; translate examples for consistency.

- [recommended] **[Data Science DISCOVERY (University of Illinois)](https://discovery.cs.illinois.edu/)** — Fagen-Ulmschneider, W.; Flanagan, K. *University of Illinois Urbana-Champaign*
  `course` · `intro` · `access: open`
  Free Illinois resource (the basis of STAT/CS/IS 107) covering Python data science basics, EDA, simulation and distributions, probability, regression and clustering, and hypothesis testing.
  *Use in wiki:* A campus-made intro some students may already know; link it for refreshers and to connect with UIUC data science offerings.
  Tools: pandas, python
  *Note:* License not stated.

- [recommended] **[Kaggle Learn micro-courses](https://www.kaggle.com/learn)** — Kaggle. *Kaggle*
  `course` · `intro` · `access: free-registration`
  Free, short, hands-on courses that run in Kaggle notebooks, covering Python, data viz, pandas, machine learning and more.
  *Use in wiki:* Pre-course or remedial assignments (e.g. Python, Pandas, Intro to ML) for students to finish before in-class labs.
  Tools: pandas, scikit-learn
  *Note:* The page is JS-rendered, so the full course list and certificate details were not retrieved. The Pandas course was verified at https://www.kaggle.com/learn/pandas .

- [recommended] **[Python for Everybody (PY4E)](https://www.py4e.com/)** — Severance, C. R. *py4e.com*
  `course` · `intro` · `access: open` · `CC BY 4.0`
  Free, openly licensed beginner Python course with a book, lectures and autograded assignments, built for reuse by other instructors (Common Cartridge export, LTI).
  *Use in wiki:* Remedial Python track for students with no programming background. CC BY allows remixing into the wiki.
  Tools: python

- [recommended] **[Think Stats, 3rd Edition](https://allendowney.github.io/ThinkStats/)** — Downey, A. B. *Green Tea Press / O'Reilly*
  `book` · `intro` · `access: open` · `Creative Commons, attribution and non-commercial (book); repo MIT`
  Notebook-first intro to exploratory data analysis, distributions, hypothesis testing and regression in Python. Chapters 1-14 each open in Colab.
  *Use in wiki:* Statistics refresher for students weak on inference before M3 and M6; chapters can be linked as Colab notebooks.
  Tools: pandas, statsmodels · Local copy: `21_Open_Textbooks_and_Courses/repos/AllenDowney__ThinkStats`
  *Note:* The page footer says (c) 2023; the 3rd-edition publication year was not confirmed.

- [optional] **[Modern Statistics: A Computer-Based Approach with Python](https://github.com/gedeck/mistat-code-solutions)** (2022) — Kenett, R.; Zacks, S.; Gedeck, P. *Springer*
  `book` · `intermediate` · `access: library`
  Springer textbook on statistics with Python, with the companion mistat package (MIT) and a public repository of code and exercise solutions.
  *Use in wiki:* Optional statistics reference with worked Python solutions; its industrial-statistics flavor makes it a secondary pick behind ISLP and Think Stats.
  Tools: mistat, statsmodels, pandas
  *Note:* mistat on PyPI (MIT): https://pypi.org/project/mistat/ . The repository's license is not visible. A companion volume, Industrial Statistics, came out in 2023. Likely available through UIUC SpringerLink (not checked).

- [optional] **[Data Science for Economists (EC 607 lecture notes)](https://github.com/uo-ec607/lectures)** — McDermott, G. *University of Oregon; GitHub*
  `course` · `intermediate` · `access: open` · `MIT`
  PhD lecture notes on Git/GitHub, the shell, R, tidyverse/data.table wrangling, web scraping and APIs, regression, spatial analysis, parallel computing, Docker, cloud computing, databases and Spark.
  *Use in wiki:* Borrow the Git/GitHub and shell lectures for the GitHub-based project workflow. The rest is R-based, so use it selectively.
  Tools: R, git

## Python for economists and econometrics

- [core] **[Coding for Economists](https://aeturrell.github.io/coding-for-economists/)** — Turrell, A. *GitHub Pages*
  `book` · `intro` · `access: open` · `MIT`
  Python book for economists covering reproducible workflow (Quarto, version control), data handling, visualization (matplotlib, seaborn, lets-plot, plotnine), regression and diagnostics, causal inference, text/regex/NLP, ML and time series.
  *Use in wiki:* Reference for workflow, regression and causal chapters. The MIT license lets you adapt pages directly into the wiki.
  Tools: pandas, statsmodels, pyfixest, seaborn · Local copy: `21_Open_Textbooks_and_Courses/repos/aeturrell__coding-for-economists`

- [recommended] **[QuantEcon DataScience: Introduction to Economic Modeling and Data Science](https://datascience.quantecon.org/)** — Coleman, C.; Lyon, S.; Perla, J. *QuantEcon*
  `course` · `intro` · `access: open` · `CC BY-SA 4.0`
  A Python course running from basics through pandas, visualization, regression and classification to applications (ML in economics, networks, text analysis, heterogeneous effects), with one-click Colab launch.
  *Use in wiki:* Ready-made notebooks to adapt (CC BY-SA permits remixing with attribution and share-alike) for M1-M3 and the M5 text and network applications.
  Tools: pandas, matplotlib, scikit-learn, statsmodels
  *Note:* Other QuantEcon series (https://quantecon.org/lectures/) are more macro- and theory-oriented: Python Programming for Economics and Finance (https://python-programming.quantecon.org/), A First Course in Quantitative Economics with Python (https://intro.quantecon.org/), and Intermediate (https://python.quantecon.org/).

- [optional] **[Introduction to Python for Econometrics, Statistics and Numerical Analysis](https://www.kevinsheppard.com/teaching/python/notes/)** (2021) — Sheppard, K. *kevinsheppard.com (University of Oxford)*
  `book` · `intermediate` · `access: open` · `CC BY-NC-ND 4.0 (text); NCSA (code)`
  Free PDF notes taking beginners through Python, NumPy, SciPy, matplotlib and pandas, with econometric examples (GJR-GARCH, Fama-MacBeth, GMM).
  *Use in wiki:* Instructor reference and optional reading for students who want rigorous numerical Python. It is finance-econometrics oriented.
  Tools: numpy, scipy, pandas
  *Note:* Edition labeling on the page is inconsistent (4th edition 2021 vs 'fifth edition'). Mini-course: https://www.kevinsheppard.com/teaching/python/course/

## Marketing analytics books and peer courses

- [core] **[Python for Marketing Research and Analytics](https://python-marketing-research.github.io/)** (2020) — Schwarz, J. S.; Chapman, C.; Feit, E. M. *Springer*
  `book` · `intro` · `access: library` · `Code repository Apache-2.0`
  The Python edition of Chapman and Feit's marketing-research text. All analyses are Colab notebooks with chapter data files and a pip-installable helper package.
  *Use in wiki:* Closest-fit textbook for the course. Embed its Colab notebooks and data for M2-M4 activities; the code is Apache-2.0, so it can be adapted.
  DOI [10.1007/978-3-030-49720-0](https://doi.org/10.1007/978-3-030-49720-0) · Tools: pandas, statsmodels, scikit-learn, colab · Local copy: `21_Open_Textbooks_and_Courses/repos/python-marketing-research__python-marketing-research-1ed`
  *Note:* Springer page: https://link.springer.com/book/10.1007/978-3-030-49720-0 (likely in UIUC's SpringerLink holdings; not checked). The chapter list was not verified; topics are expected to mirror the R edition (regression, segmentation, choice modeling).

- [recommended] **[Ad response tutorial: last-click attribution, experiments, MMM and attribution models](https://github.com/eleafeit/ad_response_tutorial)** — Feit, E. M. *GitHub*
  `tutorial` · `intermediate` · `access: open`
  Workshop materials (R code, LaTeX slides, handout) that apply last-click attribution, experiments, marketing-mix models and attribution models to the same synthetic advertising data, including the data preparation.
  *Use in wiki:* Template for an M6/M8 activity: students port the R analysis to Python with AI help and compare the estimates across methods.
  Tools: R
  *Note:* No license file was seen, so link to it rather than copying.

- [recommended] **[Dealing with Data (NYU teaching notebooks)](https://github.com/ipeirotis/dealing_with_data)** — Ipeirotis, P. *NYU; GitHub*
  `syllabus` · `intro` · `access: open` · `CC BY-NC 4.0 outside NYU`
  Notebooks from NYU classes that teach programming for data science to non-CS majors through live examples: pandas, web APIs, regex, scraping, time series, maps, text mining/NLP, visualization, network analysis, crowdsourcing and predictive modeling.
  *Use in wiki:* A model for teaching non-CS business students. Borrow the text-mining and network notebooks for M5, with attribution and non-commercial use.
  Tools: pandas, jupyter, mysql

- [optional] **[Business Data Science: code and examples](https://github.com/TaddyLab/BDS)** — Taddy, M. *GitHub (TaddyLab)*
  `book` · `intermediate` · `access: paid`
  R scripts, data (examples/) and notebooks accompanying the book Business Data Science.
  *Use in wiki:* Instructor reference for business-framed regression, regularization and causal examples; the datasets in examples/ can be reused in Python.
  Tools: R
  *Note:* No license is shown. The publisher (McGraw Hill, 2019) and the book's origin in Taddy's Chicago Booth course are from memory; verify.

- [optional] **[Customer Analytics (Wharton, Coursera)](https://www.coursera.org/learn/wharton-customer-analytics)** — Bradlow, E.; Fader, P.; Iyengar, R.; et al. *Coursera (University of Pennsylvania)*
  `course` · `intro` · `access: freemium`
  Introductory course in Wharton's Business Analytics Specialization on descriptive, predictive (CLV, customer-based corporate valuation) and prescriptive customer analytics, with examples from Amazon, Google and Starbucks.
  *Use in wiki:* Optional video background on CLV and customer-centric valuation for M4. It is not Python-based.

- [optional] **[Darden Business Publishing (cases, simulations, course packs)](https://store.darden.virginia.edu/)** — University of Virginia Darden School of Business. *Darden Business Publishing*
  `case` · `intermediate` · `access: paid`
  Store for cases, technical notes, exercises and simulations (including a digital-marketing attribution simulation), with a course-pack builder and free educator resources.
  *Use in wiki:* Source of paid marketing-analytics cases with data, if the budget allows a per-student fee.
  *Note:* Venkatesan, Farris & Wilcox's book of Darden marketing-analytics cases with data sets ('Cutting-Edge Marketing Analytics') could not be verified because the publisher pages failed to load. Harvard Business Publishing Education (https://hbsp.harvard.edu/cases/) loads only with JavaScript, so its data cases were not checked.

- [optional] **[Hands-On Data Science for Marketing (code repository)](https://github.com/PacktPublishing/Hands-On-Data-Science-for-Marketing)** — Hwang, Y. H. *Packt Publishing*
  `book` · `intro` · `access: paid` · `MIT (code)`
  MIT-licensed code for a 12-chapter Packt book that works marketing use cases in parallel Python and R.
  *Use in wiki:* Source of short marketing-specific Python examples to adapt into in-class activities. The book itself is paid.
  Tools: pandas, scikit-learn, R · Local copy: `21_Open_Textbooks_and_Courses/repos/PacktPublishing__Hands-On-Data-Science-for-Marketing`
  *Note:* Chapter topics (recalled as KPIs, engagement, CLV, segmentation, churn, A/B testing) and the publication year were not verified; it requires Python >= 3.6, so expect some version drift.

- [optional] **[Marketing Science Institute library (free working papers)](https://www.msi.org/library/)** — Marketing Science Institute. *MSI*
  `website` · `intermediate` · `access: open`
  MSI offers free access to its working papers, plus webinars in which academics and practitioners present current marketing research. Some content is members-only.
  *Use in wiki:* Source of current-topics readings for M8. No dedicated teaching-resource section was found.
  *Note:* AMA teaching resources could not be verified (the target page did not load).

- [optional] **[pyrsm and Radiant: business-analytics teaching tools from UCSD Rady](https://pypi.org/project/pyrsm/)** — Nijs, V. *PyPI; Rady School of Management, UC San Diego*
  `package` · `intro` · `access: open` · `AGPL-3.0 (pyrsm); Radiant AGPLv3 with CC-licensed docs`
  pyrsm is the Python package used in Rady's MSBA for basic tests, linear/logistic regression, ML models and EDA. Its R sibling Radiant is a browser-based Shiny app with conjoint, brand maps, clustering, collaborative filtering and experimental-design modules.
  *Use in wiki:* Shows how a peer MSBA program wraps model output for business students. The Radiant docs show marketing-analytics workflows (conjoint, perceptual maps).
  Tools: pyrsm, statsmodels, R, shiny
  *Note:* Radiant docs: https://radiant-rstats.github.io/docs/ . AGPL matters if modified code is redistributed.

## Causal inference

- [core] **[Causal Inference for the Brave and True](https://matheusfacure.github.io/python-causality-handbook/landing-page.html)** (2022) — Facure Alves, M. *GitHub Pages*
  `book` · `intermediate` · `access: open` · `MIT (repository)`
  Free Python book on potential outcomes, causal graphs, randomized experiments, IV, matching and propensity scores, DiD, synthetic control, RD and heterogeneous effects/meta-learners, with tech-industry applications.
  *Use in wiki:* Core M6 reading. Its notebooks and data can be embedded or adapted.
  Tools: pandas, statsmodels, scikit-learn · Local copy: `06_M6_Causal_Inference_and_Experiments/repos/matheusfacure__python-causality-handbook`

- [core] **[The Effect: An Introduction to Research Design and Causality](https://theeffectbook.net/)** (2021) — Huntington-Klein, N. *Chapman & Hall/CRC (free online edition)*
  `book` · `intro` · `access: open`
  Free online textbook on causal research design (causal diagrams, controls, matching, DiD, IV, RD and more), with code examples in R, Stata and Python.
  *Use in wiki:* Accessible M6 conceptual reading. Pair it with the causaldata package so students run the examples in Colab.
  Tools: causaldata, statsmodels
  *Note:* The author plans to keep the web version free. Cunningham's 'Causal Inference: The Mixtape' (online 2nd edition, https://mixtape.scunning.com/, R and Stata) is a companion option.

- [recommended] **[Applied Causal Inference Powered by ML and AI](https://causalml-book.org/)** (2024) — Chernozhukov, V.; Hansen, C.; Kallus, N.; Spindler, M.; Syrgkanis, V. *causalml-book.org*
  `book` · `advanced` · `access: open`
  Free graduate-level textbook on double/debiased machine learning and causal ML for treatment effects, with Python and R labs.
  *Use in wiki:* Instructor anchor and optional reading for students using ML for causal estimation (DML, heterogeneous effects).
  [Open-access copy](https://arxiv.org/pdf/2403.02467) · Tools: doubleml, econml, scikit-learn
  *Note:* The landing page does not state a year or license, and the lab notebook links are not on that page.

## Machine learning, NLP and visualization

- [core] **[An Introduction to Statistical Learning with Applications in Python (ISLP)](https://www.statlearning.com/)** (2023) — James, G.; Witten, D.; Hastie, T.; Tibshirani, R.; Taylor, J. *Springer*
  `book` · `intermediate` · `access: open` · `Labs repo: BSD-2-Clause`
  The standard intro to regression, classification, resampling, regularization, trees, SVMs, deep learning and unsupervised learning, now with Python labs. The PDF is a free download.
  *Use in wiki:* Core reading for M3 (regression) and M7 (prediction); the ISLP labs can be assigned as runnable notebooks.
  DOI [10.1007/978-3-031-38747-0](https://doi.org/10.1007/978-3-031-38747-0) · [Open-access copy](https://hastie.su.domains/ISLP/ISLP_website.pdf.download.html) · Tools: ISLP, statsmodels, scikit-learn · Local copy: `07_M7_Predictive_Models_ML_and_AI/repos/intro-stat-learning__ISLP_labs`
  *Note:* Labs repo v2.2.2 targets Python 3.12. Its README mentions Codespaces and uv, not Colab.

- [core] **[Fundamentals of Data Visualization](https://clauswilke.com/dataviz/)** (2019) — Wilke, C. O. *O'Reilly Media (free online)*
  `book` · `intro` · `access: open` · `CC BY-NC-ND 4.0`
  Free online guide to choosing and designing figures: aesthetics, color, amounts, distributions, proportions, associations, time series, uncertainty, figure design and telling a story with figures.
  *Use in wiki:* M2 reading on chart choice and design, paired with the Pyramid Principle for communicating results. The text is software-agnostic.

- [recommended] **[Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1)** (2026) — Hugging Face. *Hugging Face*
  `course` · `intermediate` · `access: open` · `Apache 2.0` · `AI angle`
  Free course on transformers and LLMs: pretrained models, fine-tuning, the Datasets and Tokenizers libraries, classic NLP tasks, demos, dataset curation, LLM fine-tuning and reasoning models.
  *Use in wiki:* Chapters 1-2 and the Datasets chapter support M5 sentiment and text classification with pretrained models in Colab.
  Tools: transformers, datasets, tokenizers

- [recommended] **[Speech and Language Processing, 3rd ed. draft](https://web.stanford.edu/~jurafsky/slp3/)** (2026) — Jurafsky, D.; Martin, J. H. *Stanford University (draft)*
  `book` · `advanced` · `access: open` · `AI angle`
  Free draft (Aug 19, 2026 release) of the standard NLP textbook. It now opens with a volume on large language models (transformers, pretraining, post-training) and includes chapters on embeddings and on sentiment and affect lexicons.
  *Use in wiki:* Instructor background, plus selective student readings on embeddings and sentiment lexicons for M5.

- [optional] **[Practical Deep Learning for Coders](https://course.fast.ai/)** (2022) — fast.ai. *fast.ai*
  `course` · `intermediate` · `access: open`
  Free top-down deep learning course (Part 1, 2022 edition) covering vision, NLP, tabular data, collaborative filtering, random forests and deployment with PyTorch, fastai and Hugging Face. Runs on Kaggle Notebooks.
  *Use in wiki:* Optional extension for students who want deep-learning or recommender depth in M7 projects.
  Tools: fastai, pytorch, transformers

## Python for marketing analytics: notebooks and code

- [core] **[Marketing Science in Python: A Practitioner's Guide (companion code)](https://github.com/takechanman1228/marketing-science-in-python)** (2026) — Takeda, H. *Self-published book; site marketing-science-in-python.com*
  `notebook` · `intermediate` · `access: open` · `MIT (code and notebooks); book text all rights reserved` · `AI angle`
  14 recent notebooks: A/B tests, quasi-experiments, CausalImpact, meta-learners and uplift (Part 3); traditional and embedding-based segmentation plus CLV with PyMC-Marketing (Part 4); price elasticity, assortment optimization and forecasting (Part 5); Meridian MMM and geo experiments (Part 6). Includes small synthetic datasets and Colab badges.
  *Use in wiki:* Use sec5.1_price_elasticity for M3, sec4.1 and sec4.2 (segmentation, CLV) for M4, and the Part 3 notebooks for M6. All are current-API examples worth embedding.
  Tools: pandas, pymc-marketing, google-meridian, causalml, lightgbm, statsmodels · Local copy: `21_Open_Textbooks_and_Courses/repos/takechanman1228__marketing-science-in-python`
  *Note:* Public course mirror retains explicitly licensed Python and notebooks; other downloaded prose, data, figures, and configuration remain Dropbox-only. LICENSE-CODE explicitly covers notebooks. Do not copy the book manuscript, which lives elsewhere. Larger public datasets (Dunnhumby, Online Retail II, MineThatData) are not redistributed; data/raw/README.md explains how to get them. ai_angle refers to the embedding-based ('semantic') segmentation notebook. The author gave related PyData NYC 2023, PyData London 2024 and SciPy 2024 talks.

- [core] **[Data Analytics for Marketing: A practical guide to analyzing marketing data using Python (companion code)](https://github.com/PacktPublishing/Data-Analytics-for-Marketing)** (2024) — Diaz-Bérrio, G. *Packt (May 2024)*
  `notebook` · `intermediate` · `access: open` · `MIT`
  Notebooks for a 2024 Packt book: data extraction and EDA with pandas, Streamlit presentation (ch3), econometrics and causal inference with statsmodels/PyMC (ch4), forecasting, segmentation and RFM (ch7), CLV with PyMC-Marketing (ch8), survey analysis (ch9), conjoint with statsmodels (ch10), multi-touch attribution (ch11), MMM (ch12) and Bayesian experiments (ch13).
  *Use in wiki:* Closest single match to the M1–M4 module spine; embed the ch7 RFM, ch8 CLV and ch10 conjoint notebooks as in-class coding activities.
  Tools: pandas, statsmodels, pymc, pymc-marketing, statsforecast, streamlit · Local copy: `21_Open_Textbooks_and_Courses/repos/PacktPublishing__Data-Analytics-for-Marketing`
  *Note:* No Chapter01 folder. Chapter11 (attribution) is left out because its 'attribution data markov chain.csv' is 44 MB; add it only if needed. The README pins PyMC-Marketing 0.3.1 and PyMC 5.11; PyMC-Marketing's CLV/MMM API has changed a lot since then, so expect to update the ch8 and ch12 calls (a good AI-assisted debugging exercise). The author also runs a paid 'MMM with Claude Code' workshop (see maven-mmm-with-claude-code).

- [recommended] **[Marketing Analytics and Data Science: Tools and Models (supplementary code)](https://link.springer.com/book/9783032111296)** (2026) — Dong, X. *Palgrave Macmillan*
  `notebook` · `intro` · `access: library` · `MIT (repo)` · `AI angle`
  Chapter notebooks and CSVs from a 2026 textbook by a marketing professor: coding basics, data sources, MMM, segmentation (with a 2 MB customer-purchase dataset), two targeting chapters (bank marketing), forecasting, Bayes, Thompson sampling, causal inference, and an AI chapter with a Gemini example notebook. Several chapters include homework solution notebooks.
  *Use in wiki:* Ready-made homework sets with solutions. The ch5 segmentation and ch4 MMM notebooks fit M4/M8, and the Gemini notebook is an AI-assisted example.
  Tools: pandas, scikit-learn, statsmodels, google-gemini · Local copy: `21_Open_Textbooks_and_Courses/repos/sn-code-inside__marketing-analytics-and-data-science`
  *Note:* Small and new (4 stars, pushed 2026-02). Folder names contain spaces (e.g., 'Chapter 05 - Segmentation'). The book is likely available through SpringerLink at UIUC. Homework solutions are public, so don't reuse them verbatim as graded work.

- [recommended] **[Applied Marketing Analytics Using Python](https://collegepublishing.sagepub.com/products/applied-marketing-analytics-using-python-1-288563)** (2025) — Yildirim, G.; Kübler, R. V. *SAGE Publications (March 2025)*
  `book` · `intermediate` · `access: paid`
  Python textbook by Imperial and ESSEC marketing faculty: segmentation, marketing mix modelling, attribution, user-generated data, customer mindset metrics, text mining, churn classification, demand forecasting, image analytics and data-project management. Comes with student notebooks/datasets and lecturer slides, teaching guide and testbank.
  *Use in wiki:* Candidate adopted textbook. Its companion site (study.sagepub.com/yildirimpython) offers instructor slides and testbank.
  Tools: pandas, scikit-learn, statsmodels
  *Note:* No GitHub repo, and the resource terms aren't stated, so link only. Student resources go through edge.sagepub.com and may need login. LMU Munich's Summer 2025 Python Marketing Analytics syllabus covers a very similar topic list.

- [recommended] **[Machine Learning and Generative AI for Marketing (companion code)](https://github.com/PacktPublishing/Machine-Learning-and-Generative-AI-for-Marketing)** (2024) — Hwang, Y. H.; Burtch, N. C. *Packt (August 2024)*
  `notebook` · `intermediate` · `access: open` · `MIT` · `AI angle`
  One notebook per chapter: marketing KPIs, drivers of marketing success, seasonality, sentiment analysis, predictive analytics and A/B testing, recommendations, ML segmentation, then generative-AI chapters on zero-shot content creation, few-shot/transfer learning, RAG for micro-targeting, and AI ethics and governance. Colab/Kaggle links in the README.
  *Use in wiki:* Bridge between classic marketing analytics and GenAI. Ch2 (KPIs) suits M1/M2, ch6 (A/B testing) M6, and ch9–11 the M8 current-topics week.
  Tools: pandas, scikit-learn, transformers, langchain · Local copy: `21_Open_Textbooks_and_Courses/repos/PacktPublishing__Machine-Learning-and-Generative-AI-for-Marketing`
  *Note:* Full repo is 183 MB. Left out: ch.7 and ch.8 (recommendations, segmentation), each with a 44 MB data.csv (the same file), and ch.11 (RAG), with a 77 MB 2019-Dec.csv.zip. Pull one copy of ch.8 if the segmentation notebook is wanted. The README doesn't name the LLM libraries; the tools list is a guess from chapter titles, so check before relying on it. Last pushed 2024-09; GenAI API calls may have drifted.

- [recommended] **[Data Science for Marketing Analytics, Second Edition (companion code)](https://github.com/PacktPublishing/Data-Science-for-Marketing-Analytics-Second-Edition)** (2021) — Baig, M. R.; Govindan, G.; Shrimali, V. R. *Packt (September 2021)*
  `notebook` · `intro` · `access: open` · `MIT`
  Exercise and activity notebooks for 9 chapters: data preparation and cleaning, EDA and visualization, unsupervised segmentation and choosing a segmentation approach, predicting customer revenue with linear regression, evaluating regression models, churn prediction, tuning classifiers and multiclass classification.
  *Use in wiki:* Step-by-step exercise format suits in-class coding for non-CS students. Ch3–4 (segmentation) map to M4 and ch5–6 to M3.
  Tools: pandas, matplotlib, seaborn, scikit-learn · Local copy: `21_Open_Textbooks_and_Courses/repos/PacktPublishing__Data-Science-for-Marketing-Analytics-Second-Edition`
  *Note:* Chapter05 (linear regression, the M3 chapter) is 70 MB because Datasets/ holds two identical 36 MB retail_transactions CSVs. Fetch only its notebooks and one copy of the CSV if needed. The Chapter08/09 sizes were not visible (tree listing truncated), so approx_mb is an estimate. The code dates from 2021 (pandas 1.x and older scikit-learn), so expect small API fixes. PacktPublishing/Data-Science-for-Marketing-Analytics and the '...Workshop' repo both redirect here.

- [optional] **[Data Science for Marketing Analytics (first edition, companion code)](https://github.com/TrainingByPackt/Data-Science-for-Marketing-Analytics)** (2019) — Blanchard, T.; Behera, D.; Bhatnagar, P. *Packt (March 2019)*
  `notebook` · `intro` · `access: open` · `MIT`
  Nine lesson folders: pandas and Matplotlib data handling, hierarchical and k-means segmentation, predicting CLV with linear regression, regression evaluation, customer-choice classification, churn models and marketing dashboards.
  *Use in wiki:* Backup exercise bank. The CLV-by-regression lesson contrasts usefully with probabilistic BTYD models in M4.
  Tools: pandas, matplotlib, scikit-learn
  *Note:* Last pushed 2019-05-27, so stale: expect pandas/scikit-learn deprecations. The git pack is 20 MB; working-tree size is estimated. Prefer the 2nd edition and keep this one only for extra exercises.

- [optional] **[R_to_Python_marketing_analysis: Python translation of R for Marketing Research and Analytics](https://github.com/Charlotte2110/R_to_Python_marketing_analysis)** (2018) — Charlotte2110 (GitHub). *GitHub*
  `notebook` · `intro` · `access: open`
  Seven notebooks translating chapters 3–9 of Chapman & Feit's R book (describing data, relationships, comparing groups, regression and linear models, amusement-park satisfaction drivers) with the book's CSVs.
  *Use in wiki:* Reference only; the official Python edition (already in the library) supersedes it.
  Tools: pandas, statsmodels
  *Note:* No LICENSE file, so link only. Two commits; date unknown (search result showed a 2018 push). This was the only other Python port of the Chapman & Feit book found.

- [optional] **[Marketing Data Science: Modeling Techniques in Predictive Analytics with R and Python (code downloads)](https://www.informit.com/promotions/marketing-data-science-modeling-techniques-in-predictive-141181)** (2015) — Miller, T. W. *Pearson FT Press / InformIT*
  `book` · `intermediate` · `access: open`
  Per-chapter ZIP downloads of R and Python code and data: conjoint for mobile services, commuter choice, targeting and retention, segmentation, MDS/positioning, market basket, HB market simulation, network models.
  *Use in wiki:* Instructor-only mine of classic marketing case datasets (e.g., conjoint, Dodgers promotion data); not for direct student use (Python 2 era).
  Tools: R, python
  *Note:* Not on GitHub, and the page says all rights reserved (including text and data mining), so link only. The code is about 10 years old. No GitHub mirror with a license was found.
