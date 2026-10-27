# Datasets for Exercises and Projects

38 resources (13 core). Built 2026-10-26 from `00_Index/_data/`; edit the YAML there and rerun `00_Index/_build/build_catalog.py` rather than editing this file.

Priority: **core** = likely to assign or build on; **recommended** = strong supplement; **optional** = background or niche. *Access* tells you whether students can open it without a login.

## Contents

- [AI models and releases](#ai-models-and-releases) (1)
- [Transactions, RFM and CLV](#transactions-rfm-and-clv) (7)
- [Experiments, uplift and causal inference](#experiments-uplift-and-causal-inference) (6)
- [Pricing, choice and conjoint](#pricing-choice-and-conjoint) (5)
- [Prediction: churn, response, CTR, recommendations](#prediction-churn-response-ctr-recommendations) (5)
- [Marketing mix modeling](#marketing-mix-modeling) (2)
- [Text, reviews, social and networks](#text-reviews-social-and-networks) (6)
- [Aggregators and package datasets](#aggregators-and-package-datasets) (5)
- [Python for marketing analytics: notebooks and code](#python-for-marketing-analytics-notebooks-and-code) (1)

## AI models and releases

- [recommended] **[Epoch AI: Notable AI Models (data hub)](https://epoch.ai/data/notable-ai-models)** (2026) — Epoch AI
  `dataset` · `intro` · `access: open` · `CC BY 4.0` · `AI angle`
  Table of 3,600+ machine-learning models since 1950 with publication date, organization, country, domain, training compute, parameters, dataset size, cost estimates and accessibility; CSV downloads at epoch.ai/data/notable_ai_models.csv and related files.
  *Use in wiki:* Candidate event-date source for M6/M8. Check each model record, linked announcement, and access timing before constructing event windows. No local Epoch table was supplied in the GenAI bundle.

## Transactions, RFM and CLV

- [core] **[Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)** (2021) — Olist. *Kaggle*
  `dataset` · `intermediate` · `access: free-registration` · `CC BY-NC-SA 4.0`
  About 100,000 orders from the Brazilian marketplace Olist, in relational tables covering customers, sellers, products, payments, delivery and review scores/text. About 126 MB.
  *Use in wiki:* Strong team-project dataset: practice joins, analyze delivery delay against review score, use the Portuguese review text in M5 (a good LLM-translation exercise), and model repeat purchase in M7.
  Tools: pandas, duckdb
  *Note:* The license, size and 'last updated 2021-10-01' come from the Kaggle API. The companion 'Marketing Funnel by Olist' dataset (Kaggle ref olistbr/marketing-funnel-olist) has about 8k marketing-qualified leads from Jun 2017 to Jun 2018, 875 KB, CC BY-NC-SA 4.0, and joins to orders via seller_id.

- [core] **[Google Analytics 4 sample ecommerce dataset (Google Merchandise Store) in BigQuery](https://developers.google.com/analytics/bigquery/web-ecommerce-demo-dataset)** (2021) — Google. *BigQuery public datasets*
  `dataset` · `intermediate` · `access: free-registration` · `Docs CC BY 4.0; code samples Apache 2.0; dataset under Google terms`
  Obfuscated GA4 event export from the Google Merchandise Store, covering Nov 1, 2020 to Jan 31, 2021. Query it as bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*; it runs within the BigQuery Sandbox or free tier.
  *Use in wiki:* Web-analytics lab: SQL from Colab for funnels, sessions, traffic sources and purchase conversion. It is a natural place for AI-assisted SQL writing, with students checking the generated queries against the schema.
  Tools: BigQuery, google-cloud-bigquery, SQL
  *Note:* Contains placeholder values (<Other>, NULL, empty strings) and has limited internal consistency. The older Universal Analytics sample (bigquery-public-data.google_analytics_sample.ga_sessions_*, session-level, obfuscated GA360 data around Aug 2016 to Aug 2017) is documented at https://support.google.com/analytics/answer/7586738 .

- [core] **[Online Retail II](https://archive.ics.uci.edu/dataset/502/online+retail+ii)** (2012) — Chen, D. *UCI Machine Learning Repository*
  `dataset` · `intro` · `access: open` · `CC BY 4.0`
  1,067,371 invoice lines from a UK online retailer, Dec 2009 to Dec 2011, in a single 43.5 MB xlsx file (invoice, stock code, quantity, price, customer ID, country).
  *Use in wiki:* Default dataset for M2 cleaning and visualization and for M4 RFM segmentation and CLV exercises. It is small enough for Colab.
  DOI [10.24432/C5CG6D](https://doi.org/10.24432/C5CG6D) · Tools: pandas, openpyxl
  *Note:* The original Online Retail (I) has 541,909 rows (Dec 2010 to Dec 2011), 22.6 MB, CC BY 4.0, DOI 10.24432/C5BW33, at https://archive.ics.uci.edu/dataset/352/online+retail . Expect cancellations/returns and missing customer IDs to clean; check these on load.

- [core] **[CDNOW and other BTYD datasets (Bruce Hardie)](https://www.brucehardie.com/datasets/)** — Hardie, B. *brucehardie.com*
  `dataset` · `intermediate` · `access: open`
  Small classic datasets for probability models of customer behavior: CDNOW (full, 424 KB zip, and a 1/10 sample), 'Kiwi Bubbles' test-market panel data, cumulative trial data for 19 new products, and a 1995-cohort donation-incidence dataset.
  *Use in wiki:* M4 CLV exercise: fit BG/NBD and Gamma-Gamma on CDNOW (2,357 customers, 78 weeks), then compare against RFM heuristics.
  Tools: pymc-marketing, pandas
  *Note:* No terms of use are stated. A ready CSV used by PyMC-Marketing: https://raw.githubusercontent.com/pymc-labs/pymc-marketing/main/data/cdnow_transactions.csv

- [core] **[dunnhumby Source Files: The Complete Journey, Breakfast at the Frat, Carbo-Loading, Let's Get Sort-of-Real](https://www.dunnhumby.com/source-files/)** — dunnhumby. *dunnhumby*
  `dataset` · `intermediate` · `access: open`
  Free retail datasets. The Complete Journey has two years of all-category transactions for 2,500 frequent-shopper households, with demographics and direct-marketing campaign history. Breakfast at the Frat has 156 weeks of store-week sales, prices and promotions for four categories. Carbo-Loading has household transactions in pasta, sauce, syrup and pancake mix. Let's Get Sort-of-Real is a large simulated set (4.3 GB full, with smaller samples).
  *Use in wiki:* Use The Complete Journey for campaign-response and CLV projects, and Breakfast at the Frat for M3 price/promotion regression and elasticity exercises.
  Tools: pandas
  *Note:* Direct downloads, with no registration requirement visible. The license is on a linked Terms and Conditions page that was not reviewed. A Kaggle mirror of The Complete Journey (ref frtgnn/dunnhumby-the-complete-journey, 847 MB, listed under ODbL) also exists. Separately, 84.51 released a different 'Complete Journey' (801 households, one year, about 1.47M transactions) as the pip-installable completejourney_py (MIT code, Parquet): https://github.com/cunningjames/completejourney_py . Its README describes that data as simulated and for educational use only, which makes it the easiest Colab option. Not confirmed whether downloads require a sign-up; the page's download buttons are script-driven.

- [recommended] **[Online Shoppers Purchasing Intention Dataset](https://archive.ics.uci.edu/dataset/468/online+shoppers+purchasing+intention+dataset)** (2019) — Sakar, C.; Kastro, Y. *UCI Machine Learning Repository*
  `dataset` · `intro` · `access: open` · `CC BY 4.0`
  12,330 e-commerce sessions with 17 session-level clickstream features and a purchase label (1 MB CSV).
  *Use in wiki:* Quick in-class classification lab with class imbalance; it complements GA4 with a tidy, flat table.
  DOI [10.24432/C5F88Q](https://doi.org/10.24432/C5F88Q) · Tools: pandas, scikit-learn
  *Note:* Paper: Sakar, Polat, Katircioglu & Kastro (2019), Neural Computing & Applications. The year shown is the paper's.

- [recommended] **[The Instacart Online Grocery Shopping Dataset 2017](https://tech.instacart.com/3-million-instacart-orders-open-sourced-d40d29ead6f2)** (2017) — Instacart. *Instacart tech blog*
  `dataset` · `intermediate` · `access: free-registration` · `Provided as-is for non-commercial use, subject to Instacart Terms (per release post)`
  Over 3 million grocery orders from more than 200,000 users, with 4 to 100 orders each, including order sequence, timing and product/aisle/department.
  *Use in wiki:* Use for market-basket (association-rule) analysis, reorder prediction and product-embedding exercises.
  Tools: pandas, mlxtend
  *Note:* The post links to https://www.instacart.com/datasets/grocery-shopping-2017 for download (not tested; the original S3 hosting may be gone). A Kaggle mirror (ref psparks/instacart-market-basket-analysis, 713 MB) is labeled CC0 by its uploader. That conflicts with Instacart's non-commercial terms, so follow Instacart's terms.

## Experiments, uplift and causal inference

- [core] **[The Upworthy Research Archive](https://upworthy.natematias.com/)** (2021) — Matias, J. N.; Munger, K.; Aubin Le Quere, M.; Ebersole, C. *Scientific Data (data descriptor); Cornell University*
  `dataset` · `intermediate` · `access: open` · `CC BY 4.0`
  Headline A/B tests Upworthy ran from Jan 2013 to Apr 2015: 32,487 experiments in total, including a 4,873-experiment exploratory set released for analysis and teaching.
  *Use in wiki:* Real field experiments for M6 (multiple arms, effect sizes, multiple testing) and M5 (which headline text features drive clicks, including LLM-coded features).
  DOI [10.1038/s41597-021-00934-7](https://doi.org/10.1038/s41597-021-00934-7) · Tools: pandas, statsmodels
  *Note:* Download from OSF at https://osf.io/jd64p/ . The site links a June 2024 update on the reliability of platform A/B-test archives; read it before analysis.

- [core] **[Kevin Hillstrom MineThatData E-Mail Analytics Challenge dataset](https://www.uplift-modeling.com/en/latest/api/datasets/fetch_hillstrom.html)** (2008) — Hillstrom, K. *MineThatData; loader in scikit-uplift*
  `dataset` · `intro` · `access: open`
  64,000 recent customers randomly split into a Men's e-mail, a Women's e-mail or no e-mail, with two-week visit, conversion and spend outcomes (about 5 MB CSV).
  *Use in wiki:* Flagship M6 experiment dataset: estimate effects by arm, explore heterogeneous effects and build uplift targeting policies. sklift.datasets.fetch_hillstrom() loads it in one line.
  Tools: scikit-uplift, pandas, statsmodels
  *Note:* The original 2008 post is on blog.minethatdata.com; a direct file URL was not verified. scikit-uplift also has loaders for the Criteo, X5 RetailHero, Lenta and MegaFon uplift datasets: https://www.uplift-modeling.com/en/latest/api/datasets/index.html

- [recommended] **[causaldata (Python, R and Stata package)](https://pypi.org/project/causaldata/)** (2024) — Huntington-Klein, N. *PyPI / CRAN / SSC*
  `package` · `intro` · `access: open` · `MIT`
  Packages the example datasets from The Effect (Huntington-Klein) and Causal Inference: The Mixtape (Cunningham) for pip, CRAN and Stata (Python v0.1.5, Nov 2024).
  *Use in wiki:* Load textbook causal-inference datasets in one line to reproduce book examples (DiD, IV, RD, matching) in Colab.
  Tools: causaldata, pandas, statsmodels
  *Note:* R: https://cran.r-project.org/web/packages/causaldata/index.html . The PyPI page does not list the datasets. Cunningham's Mixtape (online 2nd ed. at https://mixtape.scunning.com/) uses R and Stata, so this package is the Python route to its data.

- [recommended] **[Criteo Uplift Prediction Dataset (v2.1)](https://ailab.criteo.com/?p=859)** (2018) — Diemert, E.; Betlei, A.; Renaudin, C.; Amini, M.-R. *Criteo AI Lab; AdKDD & TargetAd Workshop at KDD 2018*
  `dataset` · `advanced` · `access: open` · `CC BY-NC-SA 4.0`
  13,979,592 users from randomized ad incrementality tests (v2.1, 297 MB compressed). It has 12 anonymized features, a treatment flag, an exposure flag and visit/conversion labels; the treatment ratio is 0.85.
  *Use in wiki:* Advanced uplift exercise, plus a lesson on noncompliance (assigned treatment vs actual exposure). Subsample it for Colab.
  [Open-access copy](https://lig-aptikal.imag.fr/~amini/Publis/large-scale-benchmark.pdf) · Tools: scikit-uplift, causalml, pandas
  *Note:* Use v2.1. The original 25.3M-row release had a leak that inflated uplift. oa_url is the benchmark paper PDF (seen in search).

- [optional] **[Criteo Attribution Modeling for Bidding Dataset](https://ailab.criteo.com/?p=649)** (2017) — Diemert, E.; Meynet, J.; Lefortier, D.; Galland, P. *Criteo AI Lab; AdKDD & TargetAd Workshop at KDD 2017*
  `dataset` · `advanced` · `access: open` · `CC BY-NC-SA 4.0`
  A 30-day sample of Criteo traffic: 16.5M impressions, 45K conversions and 700 campaigns, with clicks, conversions, attribution flags and cost (623 MB compressed). Ships with a reproduction notebook.
  *Use in wiki:* Instructor demo for M6/M8 on last-click vs model-based attribution. Too large for routine student download.
  [Open-access copy](https://arxiv.org/abs/1707.06409v2) · Tools: pandas, scikit-learn

- [optional] **[Open Bandit Dataset and Open Bandit Pipeline](https://github.com/st-tech/zr-obp)** — ZOZO, Inc. (st-tech). *GitHub*
  `dataset` · `advanced` · `access: open` · `Code Apache 2.0; data license not stated (full data for research use)`
  Logged recommendation data from a 7-day experiment on the ZOZOTOWN fashion e-commerce site, where uniform-random and Bernoulli Thompson Sampling policies served items. Comes with the obp Python library for off-policy evaluation.
  *Use in wiki:* M8 demo on bandits and on evaluating a new recommendation policy from logged data. A small sample ships in the repo.
  Tools: obp
  *Note:* The README says the small version is in obd/; the folder listing itself was blocked. The full data is at research.zozo.com.

## Pricing, choice and conjoint

- [core] **[R for Marketing Research and Analytics: companion data, code and slides](https://r-marketing.r-forge.r-project.org/)** (2019) — Chapman, C.; Feit, E. M. *r-marketing.r-forge.r-project.org (Springer book companion)*
  `dataset` · `intro` · `access: open`
  Companion site with updated R code, data files (mostly simulated), classroom slides, exercises and errata. Includes the Chapter 13 choice-based conjoint data (seats, cargo, engine, price; 3,000 choice tasks) and survey/segmentation data.
  *Use in wiki:* Ready-made conjoint, segmentation and satisfaction-survey datasets (plain CSVs readable from Python) for M4 in-class activities.
  Tools: R, pandas
  *Note:* Data index: http://r-marketing.r-forge.r-project.org/data.html (2nd-edition files are a superset of the 1st). The Chapter 13 instructor page: https://r-marketing.r-forge.r-project.org/Instructor/Chapter13/Chapter13-ChapmanFeit.html . Some loads use goo.gl short links, which may break; use the data folder instead.

- [recommended] **[Dominick's Finer Foods scanner data](https://www.chicagobooth.edu/research/kilts/research-data/dominicks)** — Kilts Center for Marketing, Chicago Booth. *Kilts Center for Marketing, University of Chicago Booth*
  `dataset` · `intermediate` · `access: open` · `Academic research use only; acknowledge the Kilts Center`
  Weekly store-level UPC sales, price, profit margin and deal codes for 29 categories (3,500+ UPCs) from about 100 Chicago-area stores, 1989 to 1994, plus daily customer counts and store demographics. CSV, SAS and Stata.
  *Use in wiki:* Price-elasticity and promotion regressions in M3 using one category's movement file (e.g. soft drinks or cereals).
  Tools: pandas, statsmodels
  *Note:* Free direct download. The terms say 'for academic research purposes only' and do not address teaching; confirm classroom use with marketingdata@chicagobooth.edu. The page gives inconsistent coverage lengths ('seven years', 'nine years'). Use the truncated PRICE/PROFIT variables in the CSVs.

- [recommended] **[Train and ModeCanada choice datasets (R package mlogit)](https://cran.csiro.au/web/packages/mlogit/vignettes/c2.formula.data.html)** — mlogit package (CRAN). *CRAN vignette*
  `dataset` · `intermediate` · `access: open`
  Train is a Dutch stated-preference survey: respondents chose between two train trips differing in price, time, number of changes and comfort (up to 16 tasks each, wide format). ModeCanada records mode choice among train, air, bus and car in the Ontario-Quebec corridor (long format; 2,779 situations with all four modes available).
  *Use in wiki:* Conjoint-style multinomial/mixed logit and willingness-to-pay exercises (Train mimics a two-alternative conjoint).
  Tools: R, mlogit, xlogit
  *Note:* Python option: xlogit (pip install xlogit; GPU-accelerated mixed logit, MNL, WTP space) uses an electricity-supplier choice dataset (electricity_long.csv) in its quick start: https://xlogit.readthedocs.io/en/latest/ . AER datasets were not checked.

- [optional] **[bayesm package datasets (Rossi)](https://www.chicagobooth.edu/research/kilts/research-data/bayesm)** — Rossi, P. *CRAN; Kilts Center listing*
  `package` · `advanced` · `access: open` · `GPL-2 | GPL-3 (package, per CRAN)`
  R package for Bayesian marketing models (v3.0-2 on CRAN) that bundles classic marketing data: Bank (credit-card conjoint), Margarine (scanner panel), Cheese (account-level sales and marketing mix), Scotch, Detailing and CustomerSat.
  *Use in wiki:* Hierarchical Bayes conjoint (Bank) and brand-choice (Margarine) examples; an instructor anchor and optional student extension.
  Tools: R, bayesm
  *Note:* CRAN: https://cran.r-project.org/web/packages/bayesm/index.html

- [optional] **[NielsenIQ Retail Scanner and Consumer Panel data (Kilts Center)](https://www.chicagobooth.edu/research/kilts/research-data/nielseniq)** — Kilts Center for Marketing, Chicago Booth; NielsenIQ. *Kilts Center for Marketing*
  `dataset` · `advanced` · `access: library`
  Consumer Panel (household purchases from 2004, about 40-60K active panelists) and Retail Scanner (weekly store-level price and volume from 2006, 90+ chains, 35-50K stores), available through an institutional subscription.
  *Use in wiki:* Instructor-only background or a faculty/PhD research resource. Not usable for master's team projects under UIUC's eligibility rules.
  *Note:* UIUC has a contract (Consumer Panel, Retail Scanner, PanelView surveys) through DSRS: https://dsrs.illinois.edu/datahub/nielsen . Authorized users are tenured and tenure-track faculty, PhD students and postdocs, on campus, for scholarly use only. Master's students are not listed and classroom use is not addressed.

## Prediction: churn, response, CTR, recommendations

- [core] **[MovieLens datasets (ml-latest-small, ml-32m)](https://grouplens.org/datasets/movielens/)** (2024) — GroupLens Research (Harper, F. M.; Konstan, J. A.). *GroupLens, University of Minnesota*
  `dataset` · `intro` · `access: open` · `GroupLens usage license in each README (research-use conditions)`
  Movie ratings. ml-latest-small has 100,836 ratings from 610 users on 9,742 movies (1 MB). ml-32m has 32M ratings from 200,948 users on 87,585 movies (239 MB, released May 2024).
  *Use in wiki:* Collaborative-filtering and recommender-evaluation lab in M7; ml-latest-small fits easily in Colab.
  DOI [10.1145/2827872](https://doi.org/10.1145/2827872) · Tools: pandas, scikit-learn, surprise
  *Note:* The DOI is the dataset paper: Harper & Konstan (2015), ACM TiiS 5(4). The README calls ml-latest-small a changing development set that is not appropriate for reported research results; check the license conditions before redistributing. 32M page: https://grouplens.org/datasets/movielens/32m/

- [core] **[Bank Marketing](https://archive.ics.uci.edu/dataset/222/bank+marketing)** (2014) — Moro, S.; Rita, P.; Cortez, P. *UCI Machine Learning Repository*
  `dataset` · `intro` · `access: open` · `CC BY 4.0`
  45,211 records from a Portuguese bank's phone-based direct-marketing campaigns, with client attributes, contact history and whether the client subscribed to a term deposit. Under 1 MB zipped.
  *Use in wiki:* Response-model exercise: logistic regression against gradient boosting, lift/gain charts and campaign targeting.
  DOI [10.24432/C5K306](https://doi.org/10.24432/C5K306) · Tools: pandas, scikit-learn, statsmodels
  *Note:* Associated paper: Moro, Cortez & Rita (2014), 'A data-driven approach to predict the success of bank telemarketing', Decision Support Systems. The year shown is the paper's. Call duration is a common leakage teaching point; confirm in the UCI variable notes.

- [core] **[Telco Customer Churn (IBM sample data)](https://github.com/IBM/telco-customer-churn-on-icp4d)** — IBM. *IBM GitHub code pattern*
  `dataset` · `intro` · `access: open` · `Apache-2.0 (repository)`
  IBM's sample telecom customer table with demographics, services, charges and a churn flag. It is the standard churn-classification teaching dataset (about 1 MB CSV).
  *Use in wiki:* Use for logistic regression and tree-based churn models in M3/M7, plus retention targeting and the link to CLV.
  Tools: pandas, scikit-learn, statsmodels · Local copy: `20_Datasets/repos/IBM__telco-customer-churn-on-icp4d`
  *Note:* Also on Kaggle (ref blastchar/telco-customer-churn, 977,501 bytes, license listed as 'Data files (c) Original Authors'). IBM Cognos docs describe an extended five-file version with CLTV and churn-score fields: https://www.ibm.com/docs/SSEP7J_11.1.0/com.ibm.swg.ba.cognos.ig_smples.doc/c_telco_dm_sam.html

- [optional] **[CTR prediction benchmarks: Avazu (Kaggle) and Criteo 1TB Click Logs](https://www.kaggle.com/c/avazu-ctr-prediction)** — Avazu; Criteo AI Lab. *Kaggle; Criteo AI Lab*
  `dataset` · `advanced` · `access: free-registration` · `Avazu: Kaggle competition rules; Criteo Click Logs on Hugging Face: CC BY-NC-SA 4.0`
  Two standard ad click-through datasets. Avazu is the Kaggle competition to predict whether a mobile ad is clicked. Criteo 1TB Click Logs covers 24 days with 13 integer and 26 hashed categorical features and is a larger version of the Kaggle Display Advertising Challenge data.
  *Use in wiki:* Instructor-prepared subsamples for M7 classification with high-cardinality categoricals (hashing, target encoding, calibration). Too large for raw student download.
  Tools: pandas, lightgbm, scikit-learn
  *Note:* Criteo 1TB: https://ailab.criteo.com/download-criteo-1tb-click-logs-dataset/ ; Hugging Face mirror: https://huggingface.co/datasets/criteo/CriteoClickLogs ; Display Advertising Challenge: https://www.kaggle.com/c/criteo-display-ad-challenge . Avazu row counts and file sizes were not visible (page is JS-rendered).

- [optional] **[H&M Personalized Fashion Recommendations (Kaggle competition data)](https://www.kaggle.com/competitions/h-and-m-personalized-fashion-recommendations)** — H&M Group; Kaggle. *Kaggle*
  `dataset` · `advanced` · `access: free-registration`
  Kaggle competition data for building product recommendations from customers' previous purchases.
  *Use in wiki:* Optional advanced team-project dataset for recommender systems. Give students a pre-sampled slice.
  Tools: pandas, lightgbm
  *Note:* Only the competition metadata could be fetched; the Data and Rules tabs did not load. The data is known to include article metadata, customers, transactions and product images and to run to many GB, but file sizes and the license were not verified. Students must accept the competition rules to download.

## Marketing mix modeling

- [core] **[PyMC-Marketing example data: synthetic MMM and CDNOW CLV](https://www.pymc-marketing.io/en/stable/notebooks/mmm/mmm_example.html)** — PyMC Labs. *PyMC-Marketing docs*
  `notebook` · `intermediate` · `access: open` · `Apache-2.0` · `AI angle`
  The MMM example notebook builds a synthetic dataset step by step (179 weeks, two channels, events, trend, adstock and saturation) and then recovers the parameters. The repo's data/ folder provides mmm_example.csv and cdnow_transactions.csv for the MMM and CLV quickstarts.
  *Use in wiki:* Shows the data-generating process before fitting, which suits 'can the AI-written model recover the known truth?' exercises. Use CDNOW for BG/NBD plus Gamma-Gamma CLV in M4.
  Tools: pymc-marketing, PyMC, ArviZ · Local copy: `20_Datasets/repos/pymc-labs__pymc-marketing-data`
  *Note:* The repo ships an LLM coding-assistant skill for MMM workflows (skills/mmm-modeling/SKILL.md), listed at https://tessl.io/registry/skills/github/pymc-labs/pymc-marketing/mmm-modeling . It warns about mistakes such as flat priors on saturation. The data/ folder contents are inferred from quickstart code because the listing was blocked.

- [recommended] **[Google Meridian simulated geo-level MMM data (geo_all_channels)](https://developers.google.com/meridian/docs/user-guide/load-geo-data-with-organic-and-non-media)** — Google (Meridian). *Meridian developer docs / GitHub*
  `dataset` · `intermediate` · `access: open` · `Apache-2.0 (repository)`
  Simulated geo-by-week MMM data in CSV, XLSX and xarray-pickle formats. It has five paid channels (impressions and spend), one organic channel, a promo treatment, controls (GQV, competitor sales), population, conversions and revenue per conversion.
  *Use in wiki:* Geo-level Bayesian MMM demo in Colab using Meridian's Getting Started notebook, contrasted with Robyn and PyMC-Marketing.
  Tools: meridian, tensorflow-probability · Local copy: `20_Datasets/repos/google__meridian-simulated-data`
  *Note:* The repo also has demo/ Colab notebooks (e.g. demo/Meridian_Full_Funnel.ipynb) and top-level .agents and skills folders, whose contents were not inspected (listing blocked). The number of geos and weeks was not stated on the page.

## Text, reviews, social and networks

- [core] **[Amazon Reviews 2023 (Amazon Reviews'23)](https://amazon-reviews-2023.github.io/)** (2024) — Hou, Y.; Li, J.; He, Z.; Yan, A.; Chen, X.; McAuley, J. *McAuley Lab, UC San Diego; arXiv:2403.03952*
  `dataset` · `intermediate` · `access: open` · `AI angle`
  571.54M reviews from 54.51M users on 48.19M items in 33 categories (May 1996 to Sep 2023). Includes ratings, text, helpful votes, images, item metadata (price, descriptions) and bought-together links.
  *Use in wiki:* Have students pick a small category (Subscription_Boxes about 16K ratings, Magazine_Subscriptions about 71K, Gift_Cards about 152K) for sentiment, topic modeling, LLM review summarization and recommender exercises.
  Tools: datasets, pandas, transformers
  *Note:* Load from Hugging Face, e.g. load_dataset('McAuley-Lab/Amazon-Reviews-2023', 'raw_review_All_Beauty', trust_remote_code=True); see https://huggingface.co/datasets/McAuley-Lab/Amazon-Reviews-2023 . The full corpus is about 750 GB, so never download all of it. No license is stated; treat it as research/teaching use. The companion paper ('Bridging Language and Items for Retrieval and Recommendation') covers LLM-era retrieval and recommendation.

- [recommended] **[Stanford Large Network Dataset Collection (SNAP)](https://snap.stanford.edu/data/)** (2026) — Stanford Network Analysis Project (SNAP). *Stanford University*
  `dataset` · `intermediate` · `access: open` · `No license stated; citation requested`
  Graph datasets including social networks, Amazon co-purchasing graphs with product metadata and reviews (about 548K products), review corpora (BeerAdvocate, RateBeer, Amazon fine foods), Twitter diffusion (higgs-twitter) and Epinions trust networks.
  *Use in wiki:* M5 network-analysis lab with networkx: co-purchase centrality, community detection and diffusion.
  Tools: networkx, pandas

- [recommended] **[Yelp Open Dataset](https://business.yelp.com/data/resources/open-dataset/)** (2026) — Yelp. *Yelp*
  `dataset` · `intermediate` · `access: open` · `Yelp dataset terms (described as for educational use; full terms not reviewed)`
  A subset of Yelp data for educational use: 150,346 businesses, 6,990,280 reviews and 200,100 photos across 11 metro areas, plus check-ins and business attributes (JSON, 4.35 GB compressed).
  *Use in wiki:* Team projects on review text, drivers of star ratings and local-business analytics. Give students a pre-filtered city or category subset.
  Tools: pandas, duckdb
  *Note:* For a ready-made sentiment benchmark, use Yelp/yelp_review_full on Hugging Face: 700K reviews (650K train/50K test) labeled 1 to 5 stars, 323 MB, license 'other' under the Yelp agreement: https://huggingface.co/datasets/Yelp/yelp_review_full

- [recommended] **[TweetEval](https://huggingface.co/datasets/cardiffnlp/tweet_eval)** (2020) — Barbieri, F.; Camacho-Collados, J.; Espinosa-Anke, L.; Neves, L. *Findings of EMNLP 2020; Hugging Face (cardiffnlp)*
  `dataset` · `intro` · `access: open` · `Varies by subset (sentiment CC BY 3.0; others undefined); Twitter terms apply`
  Seven tweet classification tasks (sentiment, emotion, irony, hate, offensive, emoji, stance) across 11 subsets, about 200K rows (14.2 MB) with fixed splits.
  *Use in wiki:* Social-media text lab: compare a lexicon method, a pretrained transformer and zero-shot LLM labels on short, informal text.
  Tools: datasets, transformers, vaderSentiment
  *Note:* Paper: arXiv:2010.12421.

- [recommended] **[Bluesky developer docs and Jetstream](https://docs.bsky.app/)** — Bluesky PBC. *docs.bsky.app*
  `documentation` · `intermediate` · `access: open`
  Docs for the open AT Protocol HTTP API and SDKs (official TypeScript and Go; community Python and Dart). Jetstream is a lightweight JSON stream of public network events, filterable by collection or account.
  *Use in wiki:* The most practical open source of live social-media text for M5, via the Python SDK. Use Jetstream for prototypes; Bluesky says it is not the right tool for research-grade archives.
  Tools: atproto, websockets
  *Note:* Jetstream post: https://docs.bsky.app/blog/jetstream (public instances; events are not signed). Authentication and terms are not on the landing page; review Bluesky's developer guidelines and ethics/IRB considerations before collecting user posts.

- [recommended] **[Reddit Data API and Reddit for Researchers access rules](https://support.reddithelp.com/hc/en-us/articles/14945211791892-Developer-Platform-Accessing-Reddit-Data)** — Reddit. *Reddit Help Center*
  `documentation` · `intro` · `access: application`
  Reddit's policy: the Data API is rate-limited and bulk export is restricted. Academic research must go through the Reddit for Researchers program, and content may not be used for model training without Reddit's consent.
  *Use in wiki:* Required policy reading for M5 social-media analysis. It explains why students should not scrape Reddit or use the API for research projects, and how research access works.
  *Note:* Reddit for Researchers eligibility is not listed; applications go through a support ticket. Requests from hosted-service IP ranges, likely including cloud notebooks, need OAuth or a login. Checked 2026-10-23: access needs an application and approval (Data API app review, or Reddit for Researchers); it is not self-serve sign-up. Don't plan student projects on Reddit data without lead time.

## Aggregators and package datasets

- [recommended] **[Hugging Face Datasets Hub](https://huggingface.co/datasets)** — Hugging Face. *Hugging Face*
  `website` · `intro` · `access: open`
  Over 1.1 million datasets (as of this check), loadable with the datasets library; the main source for text, review and sentiment data.
  *Use in wiki:* Default source for M5 text datasets; teach load_dataset() and reading dataset cards for license and provenance.
  Tools: datasets

- [recommended] **[Kaggle Datasets](https://www.kaggle.com/datasets)** — Kaggle (Google). *Kaggle*
  `website` · `intro` · `access: free-registration`
  Hundreds of thousands of community-uploaded datasets with notebooks; each dataset lists its own license.
  *Use in wiki:* Discovery source for team-project data. Require students to record the license and provenance, since mirrors often mislabel licenses (see the Instacart CC0 mirror).
  *Note:* The Kaggle API (kaggle datasets download) works from Colab with an API token.

- [recommended] **[statsmodels example datasets and Rdatasets (get_rdataset)](https://www.statsmodels.org/stable/datasets/index.html)** — statsmodels developers; Arel-Bundock, V. (Rdatasets). *statsmodels documentation*
  `dataset` · `intro` · `access: open` · `Rdatasets code GPL-3; data licenses uncertain per maintainer`
  statsmodels bundles 28 datasets (e.g. modechoice travel choice, grunfeld, fair, randhie), and sm.datasets.get_rdataset() pulls any of the 3,648 CRAN datasets in Rdatasets into pandas.
  *Use in wiki:* Zero-setup data for M3 regression drills in Colab. get_rdataset lets Python students use classic R textbook data without installing R.
  Tools: statsmodels, pandas
  *Note:* Rdatasets index: https://vincentarelbundock.github.io/Rdatasets/

- [recommended] **[TidyTuesday weekly datasets](https://github.com/rfordatascience/tidytuesday)** — Data Science Learning Community. *GitHub*
  `dataset` · `intro` · `access: open` · `CC0-1.0`
  A new real-world dataset each week, organized by year and date (2018 to 2026) with a readme and source article for each; Python users join with #PydyTuesday.
  *Use in wiki:* Weekly M2 viz warm-ups or a 'pick any TidyTuesday dataset' option for a short assignment; CC0 allows hosting copies on the wiki.
  Tools: pandas, seaborn, plotnine
  *Note:* Python resources: github.com/posit-dev/python-tidytuesday-challenge (linked from the README). Download only the selected weeks; the full repo is large.

- [optional] **[Google Dataset Search](https://datasetsearch.research.google.com/)** — Google. *Google Research*
  `tool` · `intro` · `access: open`
  Search engine over datasets described with schema.org metadata across repositories; supports site: filters (e.g. site:huggingface.co).
  *Use in wiki:* Teach students how to find and vet data for team projects.
  *Note:* data.world's open community, often listed with these aggregators, was retired on July 13, 2026 (its datasets are no longer downloadable), so it is omitted.

## Python for marketing analytics: notebooks and code

- [optional] **[dmba: utilities and datasets for Machine Learning (Data Mining) for Business Analytics, Python editions](https://github.com/gedeck/dmba)** (2025) — Gedeck, P. (package); book by Shmueli, G.; Bruce, P. C.; Gedeck, P.; Patel, N. R. *Wiley (2nd Python ed., May 2025)*
  `dataset` · `intro` · `access: open` · `MIT`
  pip-installable helper package (dmba) with the book's teaching datasets bundled as CSV/GZ: e.g., Universal Bank, Toyota Corolla, laptop sales, farm ads, AutoAndElectronics text. It also has plotting and model-evaluation helpers (lift/gains charts, regression summaries).
  *Use in wiki:* Source of small, documented business datasets for M3/M7 exercises; dmba.liftChart and gainsChart help teach targeting.
  Tools: dmba, pandas, scikit-learn
  *Note:* Chapter notebooks are not in this repo (the README points to dataminingbook.com). The repo describes itself as for 'Data Mining for Business Analytics ... in Python'; the 2nd Python edition is titled 'Machine Learning for Business Analytics' (Wiley, May 2025, per the Wiley-VCH page). Last pushed 2024-04. Dataset licensing follows the repo's MIT license; original sources vary.
