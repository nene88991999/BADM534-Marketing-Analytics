# M3 · Regression Analysis: A Review

24 resources (7 core). Built 2026-10-26 from `00_Index/_data/`; edit the YAML there and rerun `00_Index/_build/build_catalog.py` rather than editing this file.

Priority: **core** = likely to assign or build on; **recommended** = strong supplement; **optional** = background or niche. *Access* tells you whether students can open it without a login.

## Contents

- [OLS refreshers and Python implementation](#ols-refreshers-and-python-implementation) (5)
- [Standard errors and fixed effects](#standard-errors-and-fixed-effects) (5)
- [Marketing applications: elasticities and response models](#marketing-applications-elasticities-and-response-models) (7)
- [AI pitfalls in regression analysis](#ai-pitfalls-in-regression-analysis) (4)
- [Python for marketing analytics: notebooks and code](#python-for-marketing-analytics-notebooks-and-code) (3)

## OLS refreshers and Python implementation

- [core] **[The Effect: An Introduction to Research Design and Causality, Chapter 13: Regression](https://theeffectbook.net/ch-StatisticalAdjustment.html)** (2021) — Huntington-Klein, N. *Chapman & Hall/CRC (free web edition at theeffectbook.net)*
  `book-chapter` · `intro` · `access: open`
  Non-technical regression chapter: error terms and exogeneity, how to read a regression table, binary and categorical predictors, polynomials and log transforms, interactions, and a section titled 'Your Standard Errors Are Probably Wrong'. It has code in R, Stata and Python (statsmodels formula API plus stargazer).
  *Use in wiki:* Core reading for the M3 review. The Python snippets can seed a first Colab warm-up that students then extend with an AI assistant.
  Tools: statsmodels, stargazer
  *Note:* The site says the web version 'will continue to be free'. No license is stated for the text. Print edition is from CRC Press (2021).

- [core] **[Coding for Economists: Regression](https://aeturrell.github.io/coding-for-economists/econmt-regression.html)** — Turrell, A. *Coding for Economists (online book)*
  `book-chapter` · `intro` · `access: open` · `MIT (book)`
  Practical Python regression chapter built mainly on pyfixest. It covers HC robust and one- and two-way clustered SEs, categorical and high-dimensional fixed effects, interactions and polynomials, log and asinh transforms, and IV, with statsmodels shown for comparison.
  *Use in wiki:* Best single 'how do I do X in Python' reference for M3. Assign it as the syntax companion to The Effect.
  Tools: pyfixest, statsmodels, linearmodels, lets-plot
  *Note:* The page states the book is under an MIT license. The GitHub source repo was not checked.

- [recommended] **[Causal Inference: The Mixtape, Chapter 2: Probability and Regression Review](https://mixtape.scunning.com/02-probability_and_regression)** (2021) — Cunningham, S. *mixtape.scunning.com (online edition)*
  `book-chapter` · `intermediate` · `access: open`
  Review of probability, expectation and variance, the population regression model, OLS estimation and goodness of fit, the law of iterated expectations, CEF properties and the regression anatomy theorem. It includes Python code blocks (numpy, pandas, statsmodels, plotnine) alongside R and Stata.
  *Use in wiki:* Optional deeper reading for students who want the 'why' behind OLS. The regression-anatomy Python example works as an in-class demo.
  Tools: statsmodels, pandas, plotnine
  *Note:* The online site is labeled the in-progress second edition and does not state access terms, but it is openly readable. The publisher (Yale University Press, 2021) is from recollection, not shown on the page.

- [recommended] **[Regression and Other Stories](https://avehtari.github.io/ROS-Examples/)** (2020) — Gelman, A.; Hill, J.; Vehtari, A. *Cambridge University Press*
  `book` · `intermediate` · `access: open` · `PDF free to view and download for personal use only (no redistribution or derivatives). The code repo states no license.`
  Applied regression textbook with a free official PDF and R code and data for every example. It covers linear regression, transformations, interactions, logistic regression and causal inference.
  *Use in wiki:* Link specific chapters (log transforms, interactions, and the predictive checks used as diagnostics) as optional reading. A good exercise is to have an AI assistant port an R example to Python and then check the port against the book's output.
  [Open-access copy](https://users.aalto.fi/~ave/ROS.pdf) · Tools: R, rstanarm
  *Note:* Use the official site, which carries the latest corrections. Don't mirror the PDF or the code, because the license allows personal use only and the code has no license.

- [recommended] **[Linear Regression in Python (QuantEcon lecture)](https://python.quantecon.org/ols.html)** (2017) — QuantEcon (Sargent, T. J.; Stachurski, J., series editors). *QuantEcon: Intermediate Quantitative Economics with Python*
  `tutorial` · `intermediate` · `access: open`
  Worked lecture on the Acemoglu-Johnson-Robinson data: simple and multivariate OLS with statsmodels, omitted variable bias, side-by-side tables with summary_col, and 2SLS with linearmodels IV2SLS. It also explains why manual two-stage regression gives wrong standard errors.
  *Use in wiki:* Short model notebook for regression syntax and tables. The default 'nonrobust' standard errors make it a good prompt for the robust-SE discussion.
  Tools: statsmodels, linearmodels, pandas
  *Note:* Robust standard errors are not covered, and the output shows 'nonrobust' covariance. A copy also appears at https://stats.quantecon.org/ols.html (seen in search). The year comes from a 2017 QuantEcon announcement; the lecture is updated continuously.

## Standard errors and fixed effects

- [core] **[PyFixest: fast high-dimensional fixed-effects regression in Python (quickstart, tutorials, llms.txt and agent skill file)](https://pyfixest.org/getting-started.html)** (2025) — Fischer, A. and contributors (py-econometrics). *pyfixest.org / GitHub*
  `package` · `intermediate` · `access: open` · `MIT` · `AI angle`
  Python port of R's fixest. It offers feols, fepois, feglm and quantreg with multi-way fixed effects; iid, HC1-HC3, CRV1/CRV3, Newey-West and Driscoll-Kraay vcov; wild cluster bootstrap; DiD and event-study estimators; and etable regression tables. The docs site publishes llms.txt and a ready-made skill file meant to be saved as SKILL.md or Agent.md so LLM coding tools write correct PyFixest code.
  *Use in wiki:* Recommended regression package for the course. Have teams add the provided skill file (https://pyfixest.org/skills.llms.md) to their project repo before using Claude Code or Cursor, then require them to state and justify their vcov choice.
  Tools: pyfixest
  *Note:* Repo: https://github.com/py-econometrics/pyfixest (MIT). The skill page lists vcov options but does not say what the defaults are. Check the API docs before telling students the defaults; fixest-style packages often cluster by the first fixed effect when FEs are present. HC2 and HC3 are not supported with FEs or IV.

- [core] **[linearmodels: panel data, instrumental variables and system regression for Python](https://bashtage.github.io/linearmodels/)** — Sheppard, K. (bashtage). *GitHub / documentation site (v7.1)*
  `package` · `intermediate` · `access: open` · `NCSA`
  Adds estimators missing from statsmodels: PanelOLS (one- and two-way FE), RandomEffects, FirstDifferenceOLS, BetweenOLS, Fama-MacBeth, AbsorbingLS, IV2SLS/LIML/GMM, SUR and 3SLS, plus Hausman, Kleibergen-Paap and Pesaran CD diagnostics.
  *Use in wiki:* Alternative to pyfixest for panel examples. It is also what QuantEcon uses for IV.
  Tools: linearmodels
  *Note:* License (NCSA) taken from the GitHub repo page https://github.com/bashtage/linearmodels. The maintainer name is from recollection.

- [core] **[statsmodels OLSResults.get_robustcov_results: HC0-HC3, cluster, HAC and panel covariance options](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.OLSResults.get_robustcov_results.html)** — statsmodels developers. *statsmodels documentation*
  `documentation` · `intermediate` · `access: open`
  Reference for every cov_type in statsmodels: HC0-HC3, cluster (CRV1, with integer 'groups'), cluster-crv3, cluster-jk, HAC (maxlags), hac-groupsum (Driscoll-Kraay) and hac-panel.
  *Use in wiki:* Cheat sheet for an exercise. Students take AI-generated statsmodels code, which usually keeps the default nonrobust SEs, and re-estimate with HC3 and clustered SEs to see how the inference changes.
  Tools: statsmodels
  *Note:* In practice the same options are usually passed via fit(cov_type=..., cov_kwargs=...).

- [recommended] **[When Should You Adjust Standard Errors for Clustering?](https://www.nber.org/papers/w24003)** (2023) — Abadie, A.; Athey, S.; Imbens, G. W.; Wooldridge, J. M. *Quarterly Journal of Economics (NBER Working Paper 24003, 2017)*
  `paper` · `advanced` · `access: open`
  Argues that clustering is a design question. Clustered SEs are needed when sampling is two-stage or when treatment assignment is correlated within clusters, and the paper proposes less conservative estimators for intermediate cases.
  *Use in wiki:* Instructor background for the 'at what level should I cluster?' slide. Also gives students a rule to apply when an AI tool clusters 'by everything'.
  [Open-access copy](https://arxiv.org/abs/1710.02926v3)
  *Note:* QJE publication is suggested by search results; the volume, pages and DOI were not verified. The arXiv page was fetched.

- [recommended] **[A Practitioner's Guide to Cluster-Robust Inference](https://cameron.econ.ucdavis.edu/research/Cameron_Miller_JHR_2015_February.pdf)** (2015) — Cameron, A. C.; Miller, D. L. *Journal of Human Resources*
  `paper` · `advanced` · `access: open`
  Standard practitioner reference on cluster-robust SEs. It covers why default SEs overstate precision, FE with clustering, choosing the cluster level, two-way clustering, few-cluster corrections and the wild cluster bootstrap.
  *Use in wiki:* Instructor-only reference. Sections on few clusters and choosing clusters can back short wiki call-outs.
  *Note:* The journal and year come from the PDF filename (JHR 2015). Volume and pages were not checked.

## Marketing applications: elasticities and response models

- [core] **[Regression example: log transformation and additional predictors (beer sales, own- and cross-price elasticities)](https://people.duke.edu/~rnau/regex4.htm)** — Nau, R. (Duke Fuqua School of Business). *Statistical forecasting notes, Duke University*
  `tutorial` · `intro` · `access: open`
  Business-school worked example. A log-log regression of 18-pack beer sales on price gives an own-price elasticity of about -6.7, and adding other carton sizes' prices yields cross-price elasticities. It also explains reading log-unit errors as percentages.
  *Use in wiki:* Interpretation reference for the log-log and elasticity lesson. Students reproduce the example in statsmodels or pyfixest with AI help and check that they get the same coefficients.
  *Note:* The original uses Excel/RegressIt, not Python. The transformation details are on the linked 'part 3' page.

- [recommended] **[Meta-Analysis of Advertising Effectiveness: New Insights from Improved Bias Corrections](https://pure.eur.nl/en/publications/meta-analysis-of-advertising-effectiveness-new-insights-from-impr/)** (2026) — Korkames, J.; Stanley, T. D.; Stremersch, S. *International Journal of Research in Marketing 43(1), 131-151*
  `paper` · `advanced` · `access: open`
  Meta-analysis of 538 B2C own-brand advertising elasticities. Modern publication-bias corrections cut the mean effect more than fivefold (short-term about 0.0008, long-term about 0.03), in line with RCT evidence, and internet advertising shows the highest elasticity.
  *Use in wiki:* Use it with a log-log sales response regression to discuss why observational ad elasticities run high (endogeneity and publication bias).
  DOI [10.1016/j.ijresmar.2025.04.001](https://doi.org/10.1016/j.ijresmar.2025.04.001) · [Open-access copy](https://personal.eur.nl/stremersch/artikels/Korkames_Stanley_and_Stremersch_IJRM_2025_print.pdf)
  *Note:* The Erasmus repository offers the final PDF under the Dutch 'Article 25fa' (Taverne) provision. The classic benchmark is Sethuraman, Tellis & Briesch (2011): 872 estimates with a mean short-term elasticity of 0.12 (https://scholar.smu.edu/business_marketing_research/12; SSRN doi 10.2139/ssrn.1866002). Its repository title differs from the published JMR title 'How Well Does Advertising Work?'.

- [recommended] **[TV Advertising Effectiveness and Profitability: Generalizable Results from 288 Brands](https://papers.ssrn.com/abstract=3273476)** (2021) — Shapiro, B. T.; Hitsch, G. J.; Tuchman, A. E. *SSRN working paper (published in Econometrica)*
  `paper` · `advanced` · `access: open`
  Regression-based estimates of TV ad elasticities for 288 CPG brands. Elasticities are much smaller than prior literature, many are insignificant, and marginal ROI is negative for over 80% of brands.
  *Use in wiki:* Flagship case for 'advertising response as regression'. Students can read the Kellogg Insight summary (https://insight.kellogg.northwestern.edu/article/tv-advertising-is-usually-not-worth-it).
  DOI [10.2139/ssrn.3273476](https://doi.org/10.2139/ssrn.3273476)
  *Note:* Published in Econometrica (2021); the SSRN page does not name the journal. The study covers 288 brands. A related NBER paper, 'Generalizable and Robust TV Advertising Effects' (w27684), also exists.

- [recommended] **[Bayesian Methods for Media Mix Modeling with Carryover and Shape Effects](https://research.google/pubs/bayesian-methods-for-media-mix-modeling-with-carryover-and-shape-effects/)** (2017) — Jin, Y.; Wang, Y.; Sun, Y.; Chan, D.; Koehler, J. *Google Research*
  `report` · `intermediate` · `access: open`
  Foundational paper on modern MMM. A regression of sales on adstocked (carryover) and saturated (shape) media spend, estimated with Bayesian methods, showing that priors dominate in small samples and the optimal mix is highly uncertain.
  *Use in wiki:* Bridge from 'MMM is just a regression with transformed regressors' to modern Bayesian MMM tools.
  [Open-access copy](https://storage.googleapis.com/gweb-research2023-media/pubtools/3806.pdf)
  *Note:* Google's open-source follow-up is Meridian (https://github.com/google/meridian, Apache-2.0), with a getting-started Colab at https://developers.google.com/meridian/notebook/meridian-getting-started.

- [recommended] **[New Empirical Generalizations on the Determinants of Price Elasticity](https://repository.tilburguniversity.edu/items/813834f9-4626-45f8-ad0a-2920a545e089)** (2005) — Bijmolt, T. H. A.; van Heerde, H. J.; Pieters, R. *Journal of Marketing Research 42(2), 141-156*
  `paper` · `advanced` · `access: library`
  Meta-analysis of published price elasticities and of what drives their size (category, data type, model specification, estimation method).
  *Use in wiki:* Benchmark for sanity-checking student estimates. If a regression returns a price elasticity of +0.3 or -15, that is a red flag.
  *Note:* The landing page has metadata only, with no abstract or DOI. The often-quoted mean elasticity of about -2.6 is from recollection; check it in the paper before quoting.

- [recommended] **[PyMC-Marketing: Additive vs Log vs Log-Log MMMs (and the end-to-end MMM example)](https://www.pymc-marketing.io/en/stable/notebooks/mmm/mmm_multiplicative.html)** — PyMC Labs and PyMC-Marketing contributors. *PyMC-Marketing documentation*
  `notebook` · `intermediate` · `access: open` · `Apache-2.0` · `AI angle`
  Compares additive, log-link and log-log MMM specifications with adstock and saturation on synthetic weekly data. It explains when log-log channel coefficients can be read as elasticities and when they are semi-elasticities, then compares ROAS and budget plans against the known truth.
  *Use in wiki:* Connects M3's log-log interpretation to MMM. The repo also ships AI-agent folders (.claude, .cursor, skills/mmm-modeling) and links to MMM-GPT, so it can serve as a guided vibe-coding exercise.
  Tools: pymc-marketing, pymc
  *Note:* End-to-end example: https://www.pymc-marketing.io/en/stable/notebooks/mmm/mmm_example.html. The contents of the skills folder could not be inspected because GitHub blocked the fetch. The notebook path inside docs/source is presumed, so confirm it before mirroring.

- [optional] **[Market Response Models: Econometric and Time Series Analysis](https://link.springer.com/book/10.1007/b109775)** (2001) — Hanssens, D. M.; Parsons, L. J.; Schultz, R. L. *Springer (Kluwer), 2nd ed.*
  `book` · `advanced` · `access: library`
  Classic monograph on sales response functions: functional forms (linear, multiplicative/log-log, saturation), carryover, and econometric and time-series estimation of marketing-mix effects.
  *Use in wiki:* Instructor background for the 'sales response models' framing. Assign individual chapters through the UIUC library if needed.
  DOI [10.1007/b109775](https://doi.org/10.1007/b109775)
  *Note:* Edition and year (2nd ed., 2001) are from recollection; the Springer page was not fetched.

## AI pitfalls in regression analysis

- [recommended] **[StatLLM: A Dataset for Evaluating the Performance of Large Language Models in Statistical Analysis](https://arxiv.org/abs/2502.17657)** (2025) — Song, X.; Lee, L.; Xie, K.; Liu, X.; Deng, X.; Hong, Y. *arXiv:2502.17657*
  `paper` · `intermediate` · `access: open` · `AI angle`
  Open dataset of statistical-analysis tasks with verified reference SAS code, LLM-generated code (ChatGPT 3.5 and 4.0, Llama 3.1), and expert ratings of correctness, effectiveness, readability, executability and output accuracy.
  *Use in wiki:* Template for a course rubric to grade AI-written regression code on whether it runs, gives the right numbers and is read correctly.
  *Note:* The code evaluated is SAS, not Python. The value for the course is the evaluation design rather than the code.

- [recommended] **[Are Large Language Models Good Statisticians?](https://arxiv.org/abs/2406.07815)** (2024) — Zhu, Y.; Du, S.; Li, B.; Luo, Y.; Tang, N. *NeurIPS 2024 Datasets and Benchmarks Track (arXiv:2406.07815)*
  `paper` · `intermediate` · `access: open` · `AI angle`
  StatQA benchmark (11,623 examples) on choosing and applying hypothesis tests. GPT-4o reached only about 65%. LLMs mostly make applicability errors (using a method whose assumptions fail), whereas humans mostly confuse task types.
  *Use in wiki:* Supports a rule for the wiki: make the AI state each method's assumptions and check them on the data before trusting its test or regression.
  *Note:* Venue confirmed on the NeurIPS 2024 virtual site (poster, Datasets and Benchmarks Track).

- [recommended] **[Are LLMs Capable of Data-based Statistical and Causal Reasoning? Benchmarking Advanced Quantitative Reasoning with Data](https://arxiv.org/abs/2402.17644)** (2024) — Liu, X.; Wu, Z.; Wu, X.; Lu, P.; Chang, K.-W.; Feng, Y. *Findings of ACL 2024*
  `paper` · `intermediate` · `access: open` · `AI angle`
  QRData has 411 questions on real data sheets from textbooks, courses and papers. The best model (GPT-4) got 58%, and models were weakest on data analysis and on combining causal knowledge with the data.
  *Use in wiki:* Instructor background, and a source of realistic 'check the AI' questions for in-class activities.

- [recommended] **[The garden of forking paths: Why multiple comparisons can be a problem, even when there is no 'fishing expedition' or 'p-hacking' and the research hypothesis was posited ahead of time](https://sites.stat.columbia.edu/gelman/research/unpublished/p_hacking.pdf)** (2013) — Gelman, A.; Loken, E. *Working paper, Columbia University*
  `paper` · `intermediate` · `access: open`
  Shows that data-dependent analysis choices (exclusions, codings, subgroups, interactions) invalidate p-values even without deliberate fishing. Remedies include preregistration, replication and multilevel modeling.
  *Use in wiki:* Framing reading for 'vibe coding' risks. AI agents make it nearly free to try dozens of specifications, so students should log every specification an AI tool ran and report all of them.
  *Note:* The link redirects from stat.columbia.edu to sites.stat.columbia.edu; the final URL is used here.

## Python for marketing analytics: notebooks and code

- [core] **[PyBLP tutorial notebooks (logit and nested logit, Nevo cereal, BLP autos, Petrin micro moments, post-estimation, simulation)](https://github.com/jeffgortmaker/pyblp)** (2026) — Conlon, C.; Gortmaker, J. *GitHub (jeffgortmaker/pyblp); docs pyblp.readthedocs.io; paper RAND Journal of Economics 51(4), 2020*
  `notebook` · `advanced` · `access: open` · `MIT`
  Reference implementation of BLP random-coefficients logit demand. The tutorials go from plain and nested logit to Nevo's cereal and BLP's autos, then compute elasticities, diversion ratios, markups and merger or price-change counterfactuals.
  *Use in wiki:* The structural-demand anchor for the pricing topic: students estimate logit elasticities on the cereal data and run a price-cut counterfactual. It fits Nathan's structural IO perspective.
  [Open-access copy](https://pyblp.readthedocs.io/en/stable/tutorial.html) · Tools: pyblp, numpy, scipy, pandas · Local copy: `03_M3_Regression/repos/jeffgortmaker__pyblp`
  *Note:* Last commit 2026-10-14. The datasets ship inside the pyblp package (pyblp.data), so no extra download is needed. Cite Conlon and Gortmaker (2020), 'Best practices for differentiated products demand estimation with PyBLP', RAND Journal of Economics 51(4):1108-1161 (RePEc listing https://ideas.repec.org/a/bla/randje/v51y2020i4p1108-1161.html).

- [recommended] **[Mixtape Sessions: Demand Estimation (BLP workshop with PyBLP exercises and solutions)](https://github.com/Mixtape-Sessions/Demand-Estimation)** (2025) — Gortmaker, J. (with Pakes, A. on Day 1); Mixtape Sessions. *GitHub (Mixtape-Sessions/Demand-Estimation)*
  `course` · `advanced` · `access: open`
  Three-day workshop with slides, readings and three Python/PyBLP exercises (pure logit with a price-cut counterfactual, mixed logit, micro data), with solution notebooks and products and demographics CSVs.
  *Use in wiki:* Instructor template for a two-session pricing and demand unit. Link the exercise READMEs and Colab badges rather than mirroring them.
  Tools: pyblp, pandas
  *Note:* LINK ONLY: the repo has no LICENSE file, so it is all rights reserved. Do not mirror it. Last commit 2025-10-24. Day 1 is listed as 'by Ariel Pakes' in the README.

- [optional] **[Customer_Analytics: segmentation, RFM, and price/brand elasticity on FMCG loyalty-card data](https://github.com/sai-krishna-msk/Customer_Analytics)** (2020) — sai-krishna-msk (GitHub). *GitHub*
  `notebook` · `intermediate` · `access: open` · `MIT`
  Two notebooks: (1) PCA + k-means segmentation on demographics and RFM on purchases, (2) logistic purchase-probability models giving own-price, promotion and cross-brand price elasticities for chocolate bars (500 customers, 5 brands, 2 years).
  *Use in wiki:* Worked M3 example of elasticity from a logit purchase model; pair with Takeda sec5.1 for a log-log comparison.
  Tools: pandas, scikit-learn, statsmodels
  *Note:* Data provenance isn't stated (the structure resembles the 365 Data Science 'Customer Analytics in Python' course data). Confirm the source before redistributing the CSV. Last push 2020. Size estimated.

## AI-assisted coding angle for this module

Resources in this folder that show the method done with AI help, LLM versions of the method, or documented failure modes of AI-written analysis:

- [PyFixest: fast high-dimensional fixed-effects regression in Python (quickstart, tutorials, llms.txt and agent skill file)](https://pyfixest.org/getting-started.html)
- [StatLLM: A Dataset for Evaluating the Performance of Large Language Models in Statistical Analysis](https://arxiv.org/abs/2502.17657)
- [Are Large Language Models Good Statisticians?](https://arxiv.org/abs/2406.07815)
- [Are LLMs Capable of Data-based Statistical and Causal Reasoning? Benchmarking Advanced Quantitative Reasoning with Data](https://arxiv.org/abs/2402.17644)
- [PyMC-Marketing: Additive vs Log vs Log-Log MMMs (and the end-to-end MMM example)](https://www.pymc-marketing.io/en/stable/notebooks/mmm/mmm_multiplicative.html)

## Also relevant (catalogued in other folders)

- **`01_M1_Marketing_Analytics_and_Python`**: [Cutting-Edge Marketing Analytics: Real World Cases and Data Sets for Hands On Learning](https://www.oreilly.com/library/view/-/9780133552584/)
- **`02_M2_Customer_Data_and_Visualization`**: [seaborn user guide and tutorial](https://seaborn.pydata.org/tutorial.html)
- **`04_M4_Conjoint_Segmentation_CLV`**: [Juan Orduz website projects: Bayesian marketing-analytics notebooks](https://github.com/juanitorduz/website_projects); [pyrsm example notebooks (Rady School of Management business-analytics toolkit)](https://github.com/radiant-ai-hub/pyrsm); [TensorHouse: reference notebooks for marketing, promotions and pricing (successor to Introduction to Algorithmic Marketing examples)](https://github.com/ikatsov/tensor-house)
- **`05_M5_Text_and_Social_Media_Analytics`**: [What Makes Online Content Viral?](https://doi.org/10.1509/jmr.10.0353); [Large Language Models: An Applied Econometric Framework](https://nber.org/papers/w33344); [Correcting Toward the Wrong Target: LLM-Annotated Regressors Under Noisy Human Benchmarks](https://scholar.smu.edu/business_marketing_research/63); [Using Imperfect Surrogates for Downstream Inference: Design-based Supervised Learning for Social Science Applications of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2023/hash/d862f7f5445255090de13b825b880d59-Abstract.html)
- **`06_M6_Causal_Inference_and_Experiments`**: [Meridian: Google's open-source Bayesian marketing mix model](https://developers.google.com/meridian); [Improving the Sensitivity of Online Controlled Experiments by Utilizing Pre-Experiment Data (CUPED)](https://exp-platform.com/cuped/); [AI-Assisted Statistics for Data Scientists: 50+ Essential Concepts Using R and Python, 3rd ed. (code)](https://github.com/gedeck/ai-assisted-statistics-for-data-scientists); [Behavioral Data Analysis with R and Python (companion code)](https://github.com/BuissonFlorent/BehavioralDataAnalysis)
- **`07_M7_Predictive_Models_ML_and_AI`**: [ISLP_labs: Python lab notebooks for ISLP](https://github.com/intro-stat-learning/ISLP_labs); [Consumption Variety in Food Recommendation](https://www.journals.uchicago.edu/doi/10.1086/720453); [Machine Learning: An Applied Econometric Approach](https://www.aeaweb.org/articles?id=10.1257/jep.31.2.87)
- **`10_AI_Coding_Concepts_and_Evidence`**: [AI Agents for Economic Research: August 2025 Update](https://www.aeaweb.org/articles/materials/23826); [BLADE: Benchmarking Language Model Agents for Data-Driven Science](https://arxiv.org/abs/2408.09667); [How Do Analysts Understand and Verify AI-Assisted Data Analyses?](https://arxiv.org/abs/2309.10947); [Generative AI for Economic Research: Use Cases and Implications for Economists](https://www.aeaweb.org/articles?id=10.1257/jel.20231736); [Measuring AI Ability to Complete Long Software Tasks](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/); [DSBench: How Far Are Data Science Agents from Becoming Data Science Experts?](https://arxiv.org/abs/2409.07703)
- **`11_AI_Coding_Tools_and_Workflows`**: [Google Colab: AI-powered notebooks (Gemini in Colab)](https://developers.google.com/colab); [Data Science Agent in Colab: The future of data analysis with Gemini](https://developers.googleblog.com/en/data-science-agent-in-colab-with-gemini/); [pandera: statistical data testing for DataFrames](https://github.com/unionai-oss/pandera); [Posit Assistant in Positron (replaces Positron Assistant and Databot)](https://positron.posit.co/assistant.html); [Julius AI](https://julius.ai)
- **`20_Datasets`**: [R for Marketing Research and Analytics: companion data, code and slides](https://r-marketing.r-forge.r-project.org/); [Bank Marketing](https://archive.ics.uci.edu/dataset/222/bank+marketing); [dunnhumby Source Files: The Complete Journey, Breakfast at the Frat, Carbo-Loading, Let's Get Sort-of-Real](https://www.dunnhumby.com/source-files/); [Telco Customer Churn (IBM sample data)](https://github.com/IBM/telco-customer-churn-on-icp4d); [causaldata (Python, R and Stata package)](https://pypi.org/project/causaldata/); [Dominick's Finer Foods scanner data](https://www.chicagobooth.edu/research/kilts/research-data/dominicks); [statsmodels example datasets and Rdatasets (get_rdataset)](https://www.statsmodels.org/stable/datasets/index.html); [dmba: utilities and datasets for Machine Learning (Data Mining) for Business Analytics, Python editions](https://github.com/gedeck/dmba); [bayesm package datasets (Rossi)](https://www.chicagobooth.edu/research/kilts/research-data/bayesm); [NielsenIQ Retail Scanner and Consumer Panel data (Kilts Center)](https://www.chicagobooth.edu/research/kilts/research-data/nielseniq)
- **`21_Open_Textbooks_and_Courses`**: [Marketing Science in Python: A Practitioner's Guide (companion code)](https://github.com/takechanman1228/marketing-science-in-python); [Data Analytics for Marketing: A practical guide to analyzing marketing data using Python (companion code)](https://github.com/PacktPublishing/Data-Analytics-for-Marketing); [An Introduction to Statistical Learning with Applications in Python (ISLP)](https://www.statlearning.com/); [Causal Inference for the Brave and True](https://matheusfacure.github.io/python-causality-handbook/landing-page.html); [The Effect: An Introduction to Research Design and Causality](https://theeffectbook.net/); [Python for Marketing Research and Analytics](https://python-marketing-research.github.io/); [Coding for Economists](https://aeturrell.github.io/coding-for-economists/); [Data 100 Course Notes: Principles and Techniques of Data Science](https://ds100.org/course-notes/); [Data Science for Marketing Analytics, Second Edition (companion code)](https://github.com/PacktPublishing/Data-Science-for-Marketing-Analytics-Second-Edition); [Computational and Inferential Thinking: The Foundations of Data Science, 2nd ed. (Berkeley Data 8)](https://inferentialthinking.com/); [Data Science DISCOVERY (University of Illinois)](https://discovery.cs.illinois.edu/); [QuantEcon DataScience: Introduction to Economic Modeling and Data Science](https://datascience.quantecon.org/); [Think Stats, 3rd Edition](https://allendowney.github.io/ThinkStats/); [Modern Statistics: A Computer-Based Approach with Python](https://github.com/gedeck/mistat-code-solutions); [Introduction to Python for Econometrics, Statistics and Numerical Analysis](https://www.kevinsheppard.com/teaching/python/notes/); [Data Science for Marketing Analytics (first edition, companion code)](https://github.com/TrainingByPackt/Data-Science-for-Marketing-Analytics); [R_to_Python_marketing_analysis: Python translation of R for Marketing Research and Analytics](https://github.com/Charlotte2110/R_to_Python_marketing_analysis); [Business Data Science: code and examples](https://github.com/TaddyLab/BDS); [pyrsm and Radiant: business-analytics teaching tools from UCSD Rady](https://pypi.org/project/pyrsm/)
- **`22_Wiki_Design_and_Hosting`**: [Packages built in Pyodide](https://pyodide.org/en/stable/usage/packages-in-pyodide.html); [MLU-Explain](https://mlu-explain.github.io/); [Seeing Theory](https://seeing-theory.brown.edu/)
