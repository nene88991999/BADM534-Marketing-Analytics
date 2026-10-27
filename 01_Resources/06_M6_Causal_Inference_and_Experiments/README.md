# M6 · Causal Models and Experiments

73 resources (29 core). Built 2026-10-26 from `00_Index/_data/`; edit the YAML there and rerun `00_Index/_build/build_catalog.py` rather than editing this file.

Priority: **core** = likely to assign or build on; **recommended** = strong supplement; **optional** = background or niche. *Access* tells you whether students can open it without a login.

## Contents

- [Foundations](#foundations) (8)
- [A/B testing and online experiments](#ab-testing-and-online-experiments) (15)
- [Advertising measurement](#advertising-measurement) (7)
- [Quasi-experimental methods in Python](#quasi-experimental-methods-in-python) (9)
- [Marketing mix modeling](#marketing-mix-modeling) (3)
- [Heterogeneous effects, uplift and targeting](#heterogeneous-effects-uplift-and-targeting) (7)
- [LLMs and causal inference](#llms-and-causal-inference) (5)
- [Python for marketing analytics: notebooks and code](#python-for-marketing-analytics-notebooks-and-code) (19)

## Foundations

- [core] **[Causal Inference in Python: Applying Causal Inference in the Tech Industry](https://www.oreilly.com/library/view/causal-inference-in/9781098140243/)** (2023) — Facure, M. *O'Reilly Media*
  `book` · `intermediate` · `access: library`
  Written for managers, data scientists and business analysts. It measures the effects of marketing spend, discounts and pricing through A/B tests, regression, propensity scores, meta-learners, DiD, synthetic control, geo and switchback experiments, and noncompliance/IV.
  *Use in wiki:* The core business-facing text for M6. The geo/switchback chapter covers interference and marketplace settings, and its MIT-licensed code can be loaded straight into Colab.
  Tools: pandas, statsmodels, scikit-learn, lightgbm · Local copy: `06_M6_Causal_Inference_and_Experiments/repos/matheusfacure__causal-inference-in-python-code`
  *Note:* ISBN 9781098140243, 408 pages, July 2023. The O'Reilly page is paywalled. Students can probably reach it through O'Reilly Learning via the library; I haven't checked UIUC access.

- [core] **[Conducting Research in Marketing with Quasi-Experiments](https://journals.sagepub.com/doi/10.1177/00222429221082977)** (2022) — Goldfarb, A.; Tucker, C.; Wang, Y. *Journal of Marketing 86(3), 1-20*
  `paper` · `intermediate` · `access: library`
  A JM methods guide to quasi-experimental designs in marketing (DiD, synthetic control, RDD and related designs): when they are credible and how to probe their assumptions.
  *Use in wiki:* Assigned academic anchor for the quasi-experiments week. Its checklist of identification threats can feed a student project rubric.
  DOI [10.1177/00222429221082977](https://doi.org/10.1177/00222429221082977)
  *Note:* Metadata confirmed through the Crossref record for the DOI. The SAGE landing page blocked automated fetching. I didn't find an open-access copy.

- [core] **[Causal Inference: The Mixtape](https://mixtape.scunning.com/)** (2021) — Cunningham, S. *Yale University Press (free online edition)*
  `book` · `intermediate` · `access: open`
  A widely used, readable textbook on DAGs, potential outcomes, matching, IV, RDD, DiD and synthetic control. The free web edition runs alongside the print book.
  *Use in wiki:* Assign chapters as background reading per method, e.g. the DiD and synthetic control chapters before the pyfixest and pysyncon labs.
  Tools: R, Stata
  *Note:* The online edition says its code is in R and Stata, not Python. Its datasets reach Python through the causaldata package (see the-effect entry). The Yale UP publisher and 2021 date come from the print ISBN (9780300251685) in search results; the web page itself doesn't state them. Companion page: https://www.scunning.com/mixtape. The author also runs 'Scott's Mixtape Substack' (https://causalinf.substack.com/), which describes itself as covering how AI agents are changing empirical research. I couldn't confirm individual AI posts there.

- [core] **[Causal inference in economics and marketing](https://pmc.ncbi.nlm.nih.gov/articles/PMC4941501)** (2016) — Varian, H. R. *Proceedings of the National Academy of Sciences 113(27), 7310-7315*
  `paper` · `intro` · `access: open`
  Google's chief economist gives a short, non-technical tour of counterfactual thinking, experiments, IV, RDD, DiD and 'train-test-treat-compare' with predictive models, illustrated with advertising and marketing examples.
  *Use in wiki:* First assigned reading for M6. It frames 'what would have happened otherwise' for business students.
  DOI [10.1073/pnas.1510479113](https://doi.org/10.1073/pnas.1510479113) · [Open-access copy](https://people.ischool.berkeley.edu/~hal/Papers/cause-PNAS4.pdf)

- [core] **[DoWhy: causal inference with explicit modeling and testing of assumptions (PyWhy)](https://github.com/py-why/dowhy)** — PyWhy contributors (originally Microsoft Research). *GitHub / pywhy.org*
  `package` · `intermediate` · `access: open` · `MIT`
  A four-step workflow (model a DAG, identify, estimate, refute) with refutation tests and graphical causal models for attribution and root-cause analysis.
  *Use in wiki:* Teaches 'draw the DAG first'. Use the 'Estimating the Effect of a Member Rewards Program' and online-shop root-cause notebooks as marketing exercises.
  Tools: dowhy · Local copy: `06_M6_Causal_Inference_and_Experiments/repos/py-why__dowhy`
  *Note:* Example notebook index: https://www.pywhy.org/dowhy/main/example_notebooks/nb_index.html (includes member rewards, online shop root-cause, time-decay attribution, and hotel booking cancellations). No year given.

- [recommended] **[Mobile App Introduction and Online and Offline Purchases and Product Returns](https://pubsonline.informs.org/doi/10.1287/mksc.2019.1169)** (2019) — Narang, U.; Shankar, V. *Marketing Science 38(5), 756–772*
  `paper` · `advanced` · `access: library`
  Estimates how adopting a retailer's mobile app changes customers' online and offline purchases and product returns, using a quasi-experimental design that compares adopters with matched non-adopters.
  *Use in wiki:* A marketing quasi-experiment by the course's previous instructor; useful continuity for students and a clean worked example of difference-in-differences with matching.
  DOI [10.1287/mksc.2019.1169](https://doi.org/10.1287/mksc.2019.1169)
  *Note:* Also on the MBA 542 Module 1 reading list.

- [optional] **[McDonald's franchisees will now have an easier time repairing ice cream machines (US Copyright Office DMCA exemption for commercial food-preparation equipment)](https://www.nrn.com/quick-service/mcdonald-s-franchisees-will-now-have-an-easier-time-repairing-ice-cream-machines)** (2024) — Nation's Restaurant News. *Nation's Restaurant News, 28 Oct 2024*
  `report` · `intro` · `access: open`
  In late October 2024 the US Copyright Office granted an exemption, petitioned by iFixit and Public Knowledge and supported by the FTC and DOJ, allowing third parties to diagnose and repair retail-level commercial food-preparation equipment, including the Taylor soft-serve machines in McDonald's stores.
  *Use in wiki:* A natural event for a difference-in-differences exercise with the McBroken weekly country panel (USA versus Canada, UK and others). Students write the identifying assumption before plotting.
  *Note:* Decision reported 25 Oct 2024. Measurement in the McBroken series also changed over time, so the exercise is as much about threats to identification as about the estimate.

- [optional] **[Causal Inference: What If](https://miguelhernan.org/whatifbook)** (2020) — Hernán, M. A.; Robins, J. M. *Chapman & Hall/CRC (free online edition)*
  `book` · `advanced` · `access: open`
  The epidemiology-rooted standard reference on potential outcomes, confounding, selection bias, IP weighting, standardization and g-methods. The book and its code and data are free to download.
  *Use in wiki:* Instructor-only background on confounding and selection bias. Chapters 1-3 can serve as an optional deep-dive reading.
  [Open-access copy](https://www.hsph.harvard.edu/miguel-hernan/wp-content/uploads/sites/1268/2024/04/hernanrobins_WhatIf_26apr24.pdf) · Tools: Python, R, Stata, SAS
  *Note:* Python code for Part II (chapters 11-17) by James Fiedler: https://github.com/jrfiedler/causal_inference_python_code. That repo shows no license, so it isn't marked for download. The PDF link is the April 2024 version found in search.

## A/B testing and online experiments

- [core] **[Encouragement Designs and Instrumental Variables for A/B Testing](https://engineering.atspotify.com/2023/8/encouragement-designs-and-instrumental-variables-for-a-b-testing)** (2023) — Elbers, B. (Spotify). *Spotify Engineering*
  `blog` · `intermediate` · `access: open`
  Explains how to randomize a nudge (e.g., a banner) when the feature itself can't be withheld, and then use IV to estimate the complier effect. Covers monotonicity, exclusion and relevance, with practical trade-offs.
  *Use in wiki:* The best business-facing intro to IV for this audience. Pair with a linearmodels IV2SLS exercise on simulated nudge data.
  Tools: linearmodels

- [core] **[Decision Making at Netflix (Part 1 of the Netflix A/B testing series)](https://netflixtechblog.com/decision-making-at-netflix-33065fa06481)** (2021) — Tingley, M.; Zheng, W.; Ejdemyr, S.; Lane, S.; McFarland, C. (Netflix Technology Blog). *Netflix Technology Blog*
  `blog` · `intro` · `access: open`
  A multi-part, non-technical series on how Netflix uses A/B tests. Later parts cover hypotheses, primary/secondary/guardrail metrics, false positives and power.
  *Use in wiki:* Assign Parts 1-3 as the A/B testing primer before the first coding lab. The upside-down box art example works well in class.
  *Note:* Part 2 'What is an A/B Test?': https://netflixtechblog.com/what-is-an-a-b-test-b08cc1b57962 ; Part 3 'Interpreting A/B test results: false positives and statistical significance': https://netflixtechblog.com/interpreting-a-b-test-results-false-positives-and-statistical-significance-c1522d0db27a (URL taken from a syndicated copy of the post). A later part on false negatives and power exists, but I didn't verify its original URL.

- [core] **[Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing](https://experimentguide.com/)** (2020) — Kohavi, R.; Tang, D.; Xu, Y. *Cambridge University Press*
  `book` · `intermediate` · `access: library`
  The standard practitioner reference on online experiments from the Microsoft, Google and LinkedIn experimentation leaders: metrics/OEC, guardrails, SRM, trust checks, variance, interference and experimentation culture.
  *Use in wiki:* Core text for the A/B testing week. Assign the free Chapter 1 PDF from experimentguide.com and pull SRM and pitfall examples for exercises.
  *Note:* experimentguide.com offers a free Chapter 1 PDF (English plus translations), errata, an FAQ and a bibliography. Cambridge Core page: https://www.cambridge.org/core/books/trustworthy-online-controlled-experiments/D97B26382EB0EB2DC2019A7A7B518F59. Kohavi's interactive Maven courses are paid.

- [core] **[Diagnosing Sample Ratio Mismatch in Online Controlled Experiments: A Taxonomy and Rules of Thumb for Practitioners](https://exp-platform.com/Documents/2019_KDDFabijanGupchupFuptaOmhoverVermeerDmitriev.pdf)** (2019) — Fabijan, A.; Gupchup, J.; et al. (incl. Vermeer, L.; Dmitriev, P.). *KDD 2019*
  `paper` · `intermediate` · `access: open`
  Defines SRM (observed group sizes deviate from the designed split), shows how often it invalidates results, and gives a taxonomy of causes across assignment, execution, logging, analysis and interference.
  *Use in wiki:* Use with a Colab chi-square SRM check. Lukas Vermeer's SRM Checker site (https://lukasvermeer.nl/srm/) has a manual checker, a FAQ and the cause taxonomy.
  Tools: scipy
  *Note:* The full author list isn't shown in what I fetched; the abbreviated list follows the PDF filename. The SRM Checker Chrome extension has been retired, but the website, docs and manual check remain (MIT-licensed repo).

- [core] **[Improving the Sensitivity of Online Controlled Experiments by Utilizing Pre-Experiment Data (CUPED)](https://exp-platform.com/cuped/)** (2013) — Deng, A.; Xu, Y.; Kohavi, R.; Walker, T. *WSDM 2013*
  `paper` · `intermediate` · `access: open`
  The original CUPED paper, which reduces A/B test variance by regressing out pre-experiment covariates. It is now standard on most experimentation platforms.
  *Use in wiki:* Pair with a Colab exercise in which students implement CUPED as OLS with a pre-period covariate and compare confidence-interval widths, linking back to M3 regression.
  Tools: statsmodels, numpy
  *Note:* The page links a free PDF at exp-platform.com/Documents/2013-02-CUPED-ImprovingSensitivityOfControlledExperiments.pdf

- [core] **[Evan's Awesome A/B Tools: Sample Size Calculator](https://evanmiller.org/ab-testing/sample-size.html)** — Miller, E. *evanmiller.org*
  `tool` · `intro` · `access: open`
  A free web calculator for the sample size a conversion-rate A/B test needs, given baseline rate, minimum detectable effect, power and significance. It is part of a small suite of A/B tools.
  *Use in wiki:* In-class demo. Students check the calculator's answer against statsmodels code, possibly written with an AI assistant.
  *Note:* No year given; the tool has been around since the early 2010s.

- [core] **[How Not To Run an A/B Test](https://www.evanmiller.org/how-not-to-run-an-ab-test.html)** — Miller, E. *evanmiller.org*
  `blog` · `intro` · `access: open`
  The classic short explainer showing that repeatedly checking significance and stopping early inflates false positives. It recommends fixing the sample size in advance or using sequential methods.
  *Use in wiki:* Pre-reading for a peeking simulation exercise.
  *Note:* No year given; usually dated 2010.

- [recommended] **[Better Experiments with LLM Evals: A funnel, not a fork](https://engineering.atspotify.com/2026/5/better-experiments-with-llm-evals-a-funnel-not-a-fork)** (2026) — Ankargren, M.; Schultzberg, M. (Spotify). *Spotify Engineering*
  `blog` · `intermediate` · `access: open` · `AI angle`
  Argues that offline LLM evals (LLM-as-judge) should screen candidates and generate hypotheses, while A/B tests validate real user impact. LLM judges have to be calibrated against online results.
  *Use in wiki:* Current-practice reading on how A/B testing fits AI product development. It works as a discussion starter on why an LLM judge isn't a causal estimate.
  *Note:* The post reports that Spotify rolls back about 42% of launched experiments to prevent regressions in secondary metrics.

- [recommended] **[Statistical Challenges in Online Controlled Experiments: A Review of A/B Testing Methodology](https://doi.org/10.1080/00031305.2023.2257237)** (2024) — Larsen, N.; Stallrich, J.; Sengupta, S.; Deng, A.; Kohavi, R.; Stevens, N. T. *The American Statistician 78(2), 135-149*
  `paper` · `advanced` · `access: library`
  A review of open statistical problems in A/B testing: variance reduction, heterogeneous effects, sequential testing and peeking, interference and network/marketplace effects, and long-term effects.
  *Use in wiki:* Instructor background for the pitfalls lecture, especially the interference section.
  DOI [10.1080/00031305.2023.2257237](https://doi.org/10.1080/00031305.2023.2257237)
  *Note:* Published online Oct 2023. exp-platform.com links a supplement at https://bit.ly/ABTestingStatChallengesSupplement

- [recommended] **[statsmodels.stats.power: tt_ind_solve_power / NormalIndPower](https://www.statsmodels.org/v0.14.4/generated/statsmodels.stats.power.tt_ind_solve_power.html)** (2024) — statsmodels developers. *statsmodels documentation (v0.14.4)*
  `documentation` · `intro` · `access: open` · `BSD-3-Clause (statsmodels)`
  API reference for solving for sample size, power or effect size in two-sample t-tests and z-tests (proportions via effect sizes) in Python.
  *Use in wiki:* Reference for a power-analysis Colab cell. Students prompt an AI assistant for the code and then check its arguments (effect size in Cohen's d, not raw lift) against the docs.
  Tools: statsmodels
  *Note:* The BSD-3 license is statsmodels' standard license; this doc page doesn't state it. The version-pinned URL came from search, and the 'stable' docs path should also work.

- [recommended] **[Choosing a Sequential Testing Framework: Comparisons and Discussions](https://engineering.atspotify.com/2023/3/choosing-sequential-testing-framework-comparisons-and-discussions)** (2023) — Schultzberg, M.; Ankargren, S. (Spotify). *Spotify Engineering*
  `blog` · `intermediate` · `access: open`
  Compares group sequential tests, always-valid inference (mSPRT/GAVI), corrected-alpha and Bonferroni as fixes for the peeking problem, using Monte Carlo evidence on power.
  *Use in wiki:* Follow-up reading after a peeking simulation in Colab, where students see the false-positive rate inflate when they stop at the first p<0.05.
  *Note:* Related Spotify posts: 'Bringing Sequential Testing to Experiments with Longitudinal Data (Part 1): The Peeking Problem 2.0' (2023) and 'Risk-Aware Product Decisions in A/B Tests with Multiple Metrics' (2024), https://engineering.atspotify.com/2024/3/risk-aware-product-decisions-in-a-b-tests-with-multiple-metrics

- [recommended] **[ExP Platform: Kohavi et al. papers, talks and pitfalls on online controlled experiments](https://exp-platform.com/)** (2023) — Kohavi, R. et al. *exp-platform.com*
  `website` · `intermediate` · `access: open`
  Free PDFs of the classic Microsoft/Bing experimentation papers: Practical Guide (KDD 2007), Seven Pitfalls, Rules of Thumb, Puzzling Outcomes, A Dirty Dozen metric-interpretation pitfalls, continuous monitoring and trigger dilution.
  *Use in wiki:* Reading bank. Assign the KDD 2007 'Practical Guide' (HiPPO) as an intro piece and 'A Dirty Dozen' for metric-interpretation pitfalls.
  *Note:* Year marks roughly the latest listed item. Direct pages found on the hub: Practical Guide https://exp-platform.com/practical-guide/ ; Seven Pitfalls https://exp-platform.com/seven-pitfalls/ ; Rules of Thumb https://exp-platform.com/rules-of-thumb/ ; Dirty Dozen PDF https://exp-platform.com/Documents/2017-08%20KDDMetricInterpretationPitfalls.pdf

- [recommended] **[A/B Testing Intuition Busters: Common Misunderstandings in Online Controlled Experiments](https://exp-platform.com/abtestingintuitionbusters/)** (2022) — Kohavi, R.; Deng, A.; Vermeer, L. *KDD 2022*
  `paper` · `intermediate` · `access: open`
  Debunks common, intuitive but wrong beliefs about A/B tests that some tool vendors promote, such as misreadings of p-values and statistical power. It recommends platform designs that make the mistakes harder to commit.
  *Use in wiki:* Discussion reading. Students check whether an AI chatbot repeats any of the misconceptions, then correct it.

- [recommended] **[Deep Dive Into Variance Reduction](https://www.microsoft.com/en-us/research/articles/deep-dive-into-variance-reduction/)** (2022) — Cosgrove, L.; Townsend, J.; Litz, J. (Microsoft Experimentation Platform). *Microsoft Research, ExP articles*
  `blog` · `intermediate` · `access: open`
  Explains CUPED as a regression adjustment that leaves the estimator consistent, shows its equivalence to Lin's ANCOVA estimator, and introduces the 'effective traffic multiplier' 1/(1-R^2) with real Microsoft numbers.
  *Use in wiki:* A readable companion to the CUPED paper. The traffic-multiplier idea makes a good short quiz question.
  *Note:* The ExP articles index (https://www.microsoft.com/en-us/research/group/experimentation-platform-exp/articles/) also has 'A/B Interactions: A Call to Relax' (2023) and pieces on experimenting with GenAI features.

- [optional] **[Democratizing online controlled experiments at Booking.com](https://arxiv.org/abs/1710.08217)** (2017) — Kaufman, R. L.; Pitchforth, J.; Vermeer, L. *arXiv:1710.08217*
  `paper` · `intro` · `access: open`
  Describes how Booking.com built an experimentation culture and infrastructure in which anyone can run trustworthy A/B tests at scale, with safeguards and shared tooling.
  *Use in wiki:* A case example of experimentation culture, to pair with the Netflix series.
  [Open-access copy](https://arxiv.org/pdf/1710.08217)
  *Note:* Lukas Vermeer's publications page dates it July 2018. I couldn't find a separate Booking.com engineering blog post on CUPED or power.

## Advertising measurement

- [core] **[A Comparison of Approaches to Advertising Measurement: Evidence from Big Field Experiments at Facebook](https://www.kellogg.northwestern.edu/academics-research/research/detail/2019/a-comparison-of-approaches-to-advertising-measurement-evidence-from/)** (2019) — Gordon, B. R.; Zettelmeyer, F.; Bhargava, N.; Chapsky, D. *Marketing Science*
  `paper` · `intermediate` · `access: open`
  Benchmarks matching, regression adjustment and propensity-score methods against large Facebook RCTs. Observational methods often miss the experimental lift by large margins.
  *Use in wiki:* Assigned anchor. Students try to recover an RCT effect with observational methods on a dataset like Hillstrom and reflect on why it fails.
  DOI [10.1287/mksc.2018.1135](https://doi.org/10.1287/mksc.2018.1135) · [Open-access copy](https://www.kellogg.northwestern.edu/faculty/gordon_b/files/fb_comparison.pdf)
  *Note:* A non-technical Kellogg/Facebook white paper is also available: https://www.kellogg.northwestern.edu/faculty/gordon_b/files/kellogg_fb_whitepaper.pdf

- [core] **[Consumer Heterogeneity and Paid Search Effectiveness: A Large-Scale Field Experiment](https://doi.org/10.3982/ECTA12423)** (2015) — Blake, T.; Nosko, C.; Tadelis, S. *Econometrica 83(1), 155-174*
  `paper` · `intermediate` · `access: open`
  eBay switched off brand-keyword and non-brand search ads in randomized geographic tests and found much smaller returns than naive observational estimates suggested, especially among frequent, loyal users.
  *Use in wiki:* Headline case study for M6. Contrast the 'correlational ROI' story with the experimental one and discuss selection on intent.
  DOI [10.3982/ECTA12423](https://doi.org/10.3982/ECTA12423) · [Open-access copy](https://faculty.haas.berkeley.edu/stadelis/BNT_ECMA_rev.pdf)
  *Note:* NBER working paper version: https://www.nber.org/papers/w20171

- [core] **[The Unfavorable Economics of Measuring the Returns to Advertising](https://ideas.repec.org/a/oup/qjecon/v130y2015i4p1941-1973.html)** (2015) — Lewis, R. A.; Rao, J. M. *Quarterly Journal of Economics 130(4), 1941-1973*
  `paper` · `intermediate` · `access: library`
  Using a large set of field experiments, shows that individual-level sales are so noisy relative to ad effects that even huge experiments are badly underpowered to measure ad ROI.
  *Use in wiki:* Pair with the power calculators. Students compute the sample size needed to detect a realistic ad lift and see the 'unfavorable economics' for themselves.
  DOI [10.1093/qje/qjv023](https://doi.org/10.1093/qje/qjv023) · [Open-access copy](https://aeaweb.org/conference/2014/retrieve.php?pdfid=985)
  *Note:* The oa_url is an earlier AEA 2014 conference draft found in search, not the published version. The open-access link is the December 2013 working paper 'On the Near Impossibility of Measuring the Returns to Advertising', not the published QJE text (QJE 130(4), 1941–1973; DOI 10.1093/qje/qjv023).

- [recommended] **[GeoLift: geo-level lift measurement with synthetic control](https://github.com/facebookincubator/GeoLift)** (2026) — Meta Open Source (facebookincubator). *GitHub*
  `package` · `intermediate` · `access: open` · `MIT`
  An end-to-end R toolkit for geo experiments: market selection and power analysis, then lift estimation with (augmented) synthetic control, including multi-cell tests.
  *Use in wiki:* Explains how brands run geo holdouts. Demo the walkthrough vignette, or reproduce the GeoLift idea in Python with CausalPy.
  Tools: R, GeoLift
  *Note:* R only (R >= 4.0); no Python version. Site: https://facebookincubator.github.io/GeoLift/ . No year given.

- [recommended] **[Close Enough? A Large-Scale Exploration of Non-Experimental Approaches to Advertising Measurement](https://www.kellogg.northwestern.edu/academics-research/research/detail/2023/close-enough-a-large-scale-exploration-of-non-experimental/)** (2023) — Gordon, B. R.; Moakler, R.; Zettelmeyer, F. *Marketing Science*
  `paper` · `advanced` · `access: open`
  Uses a large set of Facebook RCTs to test whether double/debiased ML and rich user-level data let observational methods recover experimental ad effects. Mostly they don't, even with rich data.
  *Use in wiki:* Follow-up to Gordon et al. (2019) that shows ML doesn't solve confounding. Good for a debate on 'can AI replace experiments?'.
  DOI [10.1287/mksc.2022.1413](https://doi.org/10.1287/mksc.2022.1413) · [Open-access copy](https://arxiv.org/pdf/2201.07055)
  *Note:* Volume and issue not verified. Check the exact number of experiments against the abstract before quoting.

- [recommended] **[Ghost Ads: Improving the Economics of Measuring Online Ad Effectiveness](https://www.kellogg.northwestern.edu/faculty/research/detail/2017/ghost-ads-improving-the-economics-of-measuring-online-ad)** (2017) — Johnson, G. A.; Lewis, R. A.; Nubbemeyer, E. I. *Journal of Marketing Research 54(6), 867-884*
  `paper` · `intermediate` · `access: free-registration`
  Introduces 'ghost ads', which log the ads control users would have seen, to build an exposed-vs-would-have-been-exposed comparison. It is cheaper and more precise than PSA or intent-to-treat ad experiments.
  *Use in wiki:* Explains how platform lift studies (Meta/Google conversion lift) actually work, and links ITT vs. treatment-on-treated to the IV material.
  [Open-access copy](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2620078)
  *Note:* I didn't see a DOI. Won the 2022 AMA Weitz-Winer-O'Dell award, per AMA search results.

- [optional] **[Meridian GeoX: open-source geo experiments for incrementality and MMM calibration](https://developers.google.com/meridian/geox)** (2026) — Google. *Google for Developers*
  `tool` · `advanced` · `access: open`
  Google's geo-experiment tool (holdback, go-dark and heavy-up designs, multi-treatment) that turns experiment results into priors for Meridian MMM and recommends which channels to test.
  *Use in wiki:* Current-practice example of the 'experiment, then calibrate the MMM' loop. Its Colab notebooks can serve as an instructor demo.
  Tools: meridian-geox
  *Note:* Source: https://github.com/google/meridian-geox (license not verified). Notebooks: https://developers.google.com/meridian/geox/notebook . Year is when I found the 'now available' announcement; exact release date not verified. Google's older trimmed_match geo library (https://github.com/google/trimmed_match, Apache-2.0, research-only) covers matched-pair geo designs.

## Quasi-experimental methods in Python

- [core] **[CausalPy: causal inference for quasi-experiments in Python](https://github.com/pymc-labs/CausalPy)** (2025) — PyMC Labs. *GitHub / Read the Docs*
  `package` · `intermediate` · `access: open` · `Apache-2.0` · `AI angle`
  One API (Bayesian via PyMC, or scikit-learn) for synthetic control, GeoLift, DiD, staggered DiD, RDD, regression kink, interrupted time series, IV and IPW. It ships agent skills that teach AI coding assistants to use it.
  *Use in wiki:* The one-stop quasi-experiment toolkit for the wiki. Students can try its bundled AI-assistant skills (in Claude Code or Cursor) and critique the analyses they produce.
  Tools: CausalPy, PyMC, scikit-learn · Local copy: `06_M6_Causal_Inference_and_Experiments/repos/pymc-labs__CausalPy`
  *Note:* Docs: https://causalpy.readthedocs.io . Per the docs, the skills live in causalpy/skills/ and are distributed through Decision AI Hub (hub.decision.ai). Year approximate.

- [core] **[pysyncon: a Python module for the synthetic control method](https://github.com/sdfordham/pysyncon)** — Fordham, S. D. *GitHub*
  `package` · `intermediate` · `access: open` · `MIT`
  Implements classic, robust, augmented and penalized synthetic control with placebo tests and confidence intervals. Example notebooks reproduce Basque, Texas (from the Mixtape) and German reunification.
  *Use in wiki:* Synthetic control lab. Start from the Mixtape Texas notebook, then apply it to a brand or market-level marketing intervention.
  Tools: pysyncon · Local copy: `06_M6_Causal_Inference_and_Experiments/repos/sdfordham__pysyncon`
  *Note:* No year given.

- [core] **[TFP CausalImpact: Python port of Google's CausalImpact](https://github.com/google/tfp-causalimpact)** — Google. *GitHub / PyPI (tfp-causalimpact)*
  `package` · `intermediate` · `access: open` · `Apache-2.0`
  A Python/TensorFlow Probability implementation of CausalImpact. It estimates the effect of a marketing intervention on a time series against a Bayesian structural time-series counterfactual built from control series.
  *Use in wiki:* Demo for 'did the campaign lift sales?' with only aggregate time series. Includes a quick-start notebook.
  Tools: tfp-causalimpact, tensorflow-probability · Local copy: `06_M6_Causal_Inference_and_Experiments/repos/google__tfp-causalimpact`
  *Note:* Quick start is docs/quickstart.ipynb. Marked 'not an officially supported Google product'. The original R package (Apache-2.0) is at https://github.com/google/CausalImpact, with docs at https://google.github.io/CausalImpact/CausalImpact.html; its README points Python users to tfp-causalimpact. No year given.

- [recommended] **[rdrobust: robust bias-corrected inference for regression discontinuity (Python)](https://github.com/rdpackages/rdrobust)** (2026) — Calonico, S.; Cattaneo, M. D.; Farrell, M. H.; Masini, R.; Titiunik, R. *PyPI / GitHub (rdpackages)*
  `package` · `intermediate` · `access: open` · `GPL-3.0`
  The reference RDD implementation (`pip install rdrobust`), with local polynomial estimates, robust bias-corrected CIs, data-driven bandwidths and rdplot. Ships Python illustration scripts and the US Senate example data.
  *Use in wiki:* RDD lab, e.g. loyalty-tier thresholds or rating cutoffs. Compare an AI-written 'OLS with a cutoff dummy' against rdrobust.
  Tools: rdrobust
  *Note:* PyPI: https://pypi.org/project/rdrobust/ (v2.1.1, released 2026-10-07, GPL-3.0-only). The old rdpackages.github.io/rdrobust page now just says the project moved to GitHub.

- [recommended] **[Difference-in-Differences Designs: A Practitioner's Guide](https://arxiv.org/abs/2503.13323)** (2025) — Baker, A.; Callaway, B.; Cunningham, S.; Goodman-Bacon, A.; Sant'Anna, P. H. C. *arXiv:2503.13323 [econ.EM]*
  `paper` · `advanced` · `access: open`
  A framework for classifying DiD designs and estimators: covariates, weighting, multiple periods and staggered adoption. It explains why naive two-way fixed effects can mislead.
  *Use in wiki:* Instructor reference for the staggered-DiD lab. Students can use its checklist to audit DiD code an AI assistant writes.
  DOI [10.48550/arXiv.2503.13323](https://doi.org/10.48550/arXiv.2503.13323) · Tools: csdid, differences, pyfixest
  *Note:* The arXiv page lists no journal reference. The paper is widely reported as forthcoming or published in the Journal of Economic Literature, which I haven't verified.

- [recommended] **[How to Accurately Test Significance with Difference in Difference Models](https://engineering.atspotify.com/2023/9/how-to-accurately-test-significance-with-difference-in-difference-models)** (2023) — Doll, B.; Li, J.; Oztan, T. (Spotify). *Spotify Engineering*
  `blog` · `intermediate` · `access: open`
  Simulations show that naive DiD standard errors on serially correlated time series give over 30% false positives. Compares clustered SEs, averaging and permutation tests, and says when to use each.
  *Use in wiki:* A concrete check for AI-written DiD code. Students verify that the assistant clustered standard errors at the unit level, then rerun a placebo or permutation test.
  Tools: statsmodels, pyfixest

- [recommended] **[csdid: Callaway and Sant'Anna difference-in-differences for Python](https://github.com/d2cml-ai/csdid)** — d2cml-ai. *GitHub / PyPI*
  `package` · `advanced` · `access: open` · `MIT`
  A Python port of R's did package. It estimates group-time ATT(g,t) under staggered adoption (with doubly robust options) and aggregates to event-study, calendar or group effects, with plots.
  *Use in wiki:* Staggered-adoption lab on the mpdta minimum-wage example in the README. Students compare its results with naive TWFE from pyfixest.
  Tools: csdid, drdid
  *Note:* Needs the drdid library installed separately from GitHub. Docs: d2cml-ai.github.io/csdid/. No year given.

- [optional] **[differences: difference-in-differences estimation and inference for Python](https://github.com/bernardodionisi/differences)** — Dionisi, B. *GitHub*
  `package` · `advanced` · `access: open` · `GPL-3.0`
  Implements Callaway and Sant'Anna (2021) ATT(g,t) through an ATTgt class, plus Sant'Anna and Zhao (2020) DR-DiD, multi-valued treatments and triple differences.
  *Use in wiki:* An alternative to csdid for students who want a richer API. Use for cross-checking estimates.
  Tools: differences
  *Note:* Docs: https://bernardodionisi.github.io/differences/latest/ . The repo has few commits (58), so recent maintenance is unclear.

- [optional] **[SparseSC: Fit sparse synthetic control models in Python](https://github.com/microsoft/SparseSC)** — Microsoft (Quistorff, B. et al.). *GitHub*
  `package` · `advanced` · `access: open` · `MIT`
  An ML-enhanced synthetic control that penalizes feature and unit weights. It is useful when there are many donor units or many predictors.
  *Use in wiki:* Optional advanced alternative for project teams with many control markets.
  Tools: SparseSC
  *Note:* Docs: https://sparsesc.readthedocs.io/en/latest/ . Last commit date unclear and the repo is modestly active (about 90 stars). Background: Quistorff, Goldman and Thorpe (2020). No year given.

## Marketing mix modeling

- [core] **[Meridian: Google's open-source Bayesian marketing mix model](https://developers.google.com/meridian)** (2025) — Google. *GitHub / Google for Developers*
  `package` · `advanced` · `access: open` · `Apache-2.0`
  An in-house MMM framework with reach/frequency and search-volume features and ROI priors that can be calibrated with experiments. Comes with Colab notebooks.
  *Use in wiki:* Shows how MMM estimates are made 'causal' by calibrating to lift tests. Run the Getting Started Colab live.
  [Open-access copy](https://developers.google.com/meridian) · Tools: google-meridian, TensorFlow Probability · Local copy: `06_M6_Causal_Inference_and_Experiments/repos/google__meridian`
  *Note:* Getting started: https://developers.google.com/meridian/notebook/meridian-getting-started ; ROI priors and calibration guide: https://developers.google.com/meridian/docs/advanced-modeling/roi-priors-and-calibration . The repo citation lists v2.0.0; needs Python 3.11-3.13. The demo/ path is inferred from a Colab link to demo/Meridian_Full_Funnel.ipynb.

- [core] **[PyMC-Marketing: Bayesian MMM, CLV and choice models in Python](https://www.pymc-marketing.io/en/stable/)** (2025) — PyMC Labs. *GitHub / pymc-marketing.io*
  `package` · `intermediate` · `access: open` · `Apache-2.0` · `AI angle`
  A Python Bayesian MMM with adstock/saturation, a DAG-based causal identification guide, lift-test and ROAS calibration and budget optimization, plus CLV/BTYD models that also tie into M4.
  *Use in wiki:* Main Python MMM. Assign the notebook 'Mitigating Unobserved Confounders in MMMs with Lift Test Likelihoods' (https://www.pymc-marketing.io/en/stable/notebooks/mmm/mmm_roas.html), where an omitted confounder flips the channel ROAS ranking and lift tests fix it.
  [Open-access copy](https://www.pymc-marketing.io/en/stable/) · Tools: pymc-marketing, PyMC, ArviZ
  *Note:* AI angle: the README links MMM-GPT (https://mmm-gpt.com/), an AI assistant for marketing analytics built on PyMC-Marketing. The repo also contains skills/mmm-modeling, .claude and .cursor directories, but GitHub blocked fetching them, so their contents are unverified. Lift-test integration notebook: https://www.pymc-marketing.io/en/stable/notebooks/mmm/mmm_lift_test.html . Requires Python >= 3.12.

- [recommended] **[Robyn: Meta's open-source marketing mix modeling package](https://github.com/facebookexperimental/Robyn)** (2023) — Meta Marketing Science (facebookexperimental). *GitHub / CRAN*
  `package` · `advanced` · `access: open` · `MIT` · `AI angle`
  An automated MMM in R: ridge regression, evolutionary hyperparameter search, adstock/saturation, calibration to lift experiments and budget allocation. Has a beta Python API.
  *Use in wiki:* Compare with Meridian and PyMC-Marketing in a 'which MMM would you trust?' discussion, using the R demo script or the Python API notebook.
  [Open-access copy](https://facebookexperimental.github.io/Robyn/) · Tools: R, Robyn · Local copy: `06_M6_Causal_Inference_and_Experiments/repos/facebookexperimental__Robyn`
  *Note:* Year is the release of the Python API beta (Nov 2023). Site: https://facebookexperimental.github.io/Robyn/ . R demo: demo/demo.R. The Python API notebook is robyn_api/robyn_python_notebook.ipynb and needs R installed.

## Heterogeneous effects, uplift and targeting

- [core] **[CausalML: uplift modeling and causal inference with ML (Uber)](https://github.com/uber/causalml)** (2026) — Uber Technologies. *GitHub / Read the Docs*
  `package` · `intermediate` · `access: open` · `Apache-2.0`
  Uplift trees and forests, S/T/X/R/DR meta-learners, and Qini and uplift curves for estimating who to target with a marketing treatment from experimental data.
  *Use in wiki:* Main uplift lab package. Start with the meta-learner and uplift-tree example notebooks, then apply them to the Hillstrom data.
  [Open-access copy](https://causalml.readthedocs.io/en/latest/examples.html) · Tools: causalml, scikit-learn, xgboost · Local copy: `06_M6_Causal_Inference_and_Experiments/repos/uber__causalml`
  *Note:* Examples index: https://causalml.readthedocs.io/en/latest/examples.html (uplift trees, meta-learners, Qini curves with costly treatments, SHAP interpretation). No year given.

- [core] **[Retention Futility: Targeting High-Risk Customers Might Be Ineffective](https://journals.sagepub.com/doi/10.1509/jmr.16.0163)** (2018) — Ascarza, E. *Journal of Marketing Research 55(1), 80-98*
  `paper` · `intermediate` · `access: library`
  Field experiments show that targeting customers with the highest churn risk is not the same as targeting those most responsive to a retention offer. Uplift-based targeting beats risk-based targeting.
  *Use in wiki:* Key marketing anchor linking M7 prediction to M6 causal targeting. Pair with an uplift exercise on the Hillstrom data.
  DOI [10.1509/jmr.16.0163](https://doi.org/10.1509/jmr.16.0163)
  *Note:* Metadata confirmed through Crossref. I didn't verify an open-access copy.

- [core] **[MineThatData E-Mail Analytics and Data Mining Challenge (Hillstrom dataset)](https://blog.minethatdata.com/2008/03/minethatdata-e-mail-analytics-and-data.html)** (2008) — Hillstrom, K. (MineThatData). *MineThatData blog*
  `dataset` · `intro` · `access: open`
  64,000 customers randomized to a men's email, a women's email or no email, with two-week visit, conversion and spend outcomes plus recency, history and channel covariates.
  *Use in wiki:* Workhorse dataset for M6: A/B analysis, CUPED-style adjustment, power, heterogeneous effects and uplift targeting. It is about 5 MB and easy to load in Colab.
  Tools: sklift, pandas
  *Note:* The blog post links a direct CSV. scikit-uplift loads it with fetch_hillstrom() (https://www.uplift-modeling.com/en/latest/api/datasets/fetch_hillstrom.html). No explicit license; it was released publicly for the 2008 challenge.

- [core] **[scikit-uplift (sklift): uplift modeling in scikit-learn style](https://github.com/maks-sh/scikit-uplift)** — Shevchenko, M. et al. (maks-sh). *GitHub / uplift-modeling.com*
  `package` · `intro` · `access: open` · `MIT`
  Lightweight uplift models (solo, two-model, class transformation), uplift/Qini metrics and plots, and one-line loaders for Hillstrom, Criteo, X5, Lenta and Megafon uplift datasets.
  *Use in wiki:* Easiest uplift entry point for non-CS students. Use fetch_hillstrom() and the RetailHero tutorial notebook in Colab.
  Tools: sklift, scikit-learn · Local copy: `06_M6_Causal_Inference_and_Experiments/repos/maks-sh__scikit-uplift`
  *Note:* Tutorials: https://www.uplift-modeling.com/en/latest/tutorials.html . Author name inferred from the GitHub handle; not verified. No year given.

- [recommended] **[Heterogeneous Treatment Effects and Optimal Targeting Policy Evaluation](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3111957)** (2023) — Hitsch, G. J.; Misra, S.; Zhang, W. *SSRN working paper*
  `paper` · `advanced` · `access: free-registration`
  A framework for building and evaluating customer targeting policies from one randomized dataset using off-policy evaluation. In catalog mailing data, direct CATE methods (including their treatment effect projection) beat outcome-model methods on profit.
  *Use in wiki:* Instructor background and an advanced reading on why you evaluate targeting policies by profit, not by prediction accuracy.
  *Note:* The SSRN page (revised Nov 2023, first posted 2018) shows no journal. I believe a version appeared in Quantitative Marketing and Economics (2024) but haven't verified it.

- [recommended] **[EconML: heterogeneous treatment effect estimation with ML (PyWhy)](https://github.com/py-why/EconML)** — Microsoft Research ALICE / PyWhy contributors. *GitHub (py-why)*
  `package` · `advanced` · `access: open` · `MIT (some modules BSD-3-Clause from scikit-learn)`
  Estimates CATE with double ML, causal forests, meta-learners, orthogonal IV and dynamic DML, with interpretability and policy-learning tools. Built in Microsoft's ALICE project.
  *Use in wiki:* HTE and personalization lab: who responds to a coupon or email? The notebooks folder has worked examples to adapt in Colab.
  Tools: econml, scikit-learn, lightgbm · Local copy: `06_M6_Causal_Inference_and_Experiments/repos/py-why__EconML`
  *Note:* GitHub's robots rules blocked listing the notebooks folder, so I couldn't verify individual notebook names (e.g. the customer-scenario case studies). No year given.

- [optional] **[DoubleML: an object-oriented implementation of double machine learning in Python](https://JMLR.org/papers/v23/21-0862.html)** (2022) — Bach, P.; Chernozhukov, V.; Kurz, M. S.; Spindler, M. *Journal of Machine Learning Research 23(53), 1-6*
  `package` · `advanced` · `access: open` · `BSD-3-Clause`
  A scikit-learn-based DML package for partially linear, interactive and IV models. It is the companion software to the Chernozhukov et al. causal ML book.
  *Use in wiki:* Optional advanced lab: use ML for nuisance functions without biasing the treatment effect, e.g. the effect of promotions with many controls.
  Tools: doubleml, scikit-learn
  *Note:* Docs: https://docs.doubleml.org

## LLMs and causal inference

- [core] **[Causal Reasoning and Large Language Models: Opening a New Frontier for Causality](https://arxiv.org/abs/2305.00050)** (2023) — Kıcıman, E.; Ness, R.; Sharma, A.; Tan, C. *arXiv:2305.00050*
  `paper` · `intermediate` · `access: open` · `AI angle`
  GPT-4-class models do very well on text-based causal tasks (pairwise causal discovery, counterfactuals, necessary/sufficient causes) but show unpredictable failure modes. The authors suggest pairing LLMs, which supply domain knowledge and DAG drafting, with formal causal methods.
  *Use in wiki:* Frames the AI-assisted workflow for M6: let the LLM propose a DAG and confounders, then verify with data and refutation tests (see PyWhy-LLM).
  *Note:* By DoWhy contributors (Microsoft Research). Current version v3, Aug 2024.

- [core] **[Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus?](https://www.nber.org/papers/w31122)** (2023) — Horton, J. J.; Filippas, A.; Manning, B. S. *NBER Working Paper 31122*
  `paper` · `intermediate` · `access: open` · `AI angle`
  Treats LLMs as implicit computational models of humans ('Homo silicus') that can be given endowments and preferences and run through classic behavioral-economics experiments. Results are broadly similar to the originals.
  *Use in wiki:* Anchor for the debate 'can a simulated experiment replace a real A/B test?'. Students run a small LLM-simulated survey and compare it with real data.
  [Open-access copy](https://arxiv.org/abs/2301.07543v2)
  *Note:* Originally sole-authored by Horton (2023); the NBER page now lists three authors and a Feb 2026 revision.

- [recommended] **[Using Large Language Models to Simulate Multiple Humans and Replicate Human Subject Studies](https://arxiv.org/abs/2208.10264)** (2023) — Aher, G.; Arriaga, R. I.; Kalai, A. T. *arXiv:2208.10264*
  `paper` · `intermediate` · `access: open` · `AI angle`
  Proposes 'Turing Experiments' that simulate representative samples of participants. Replicates the Ultimatum Game, garden-path sentences and Milgram, but finds a 'hyper-accuracy distortion' in wisdom-of-crowds tasks for newer models.
  *Use in wiki:* Pair with Horton. The hyper-accuracy distortion is a concrete failure mode for simulated consumer panels.
  *Note:* First posted 2022; current v5 July 2023. Widely cited as ICML 2023, though the arXiv page lists no venue.

- [recommended] **[PyWhy-LLM: integrating LLM capabilities into causal analysis](https://github.com/py-why/pywhy-llm)** — PyWhy contributors. *GitHub (py-why)*
  `package` · `intermediate` · `access: open` · `MIT` · `AI angle`
  An experimental library that uses LLMs as a stand-in domain expert: it suggests confounders, edges and DAGs, proposes backdoor, mediator and IV sets, and critiques a given DAG with suggested negative controls.
  *Use in wiki:* Exercise: students let PyWhy-LLM (or a chat assistant) propose a DAG for a marketing question, then defend or reject each edge.
  Tools: pywhyllm, dowhy
  *Note:* Experimental; install with `pip install pywhyllm`. No published release shown. No year given.

- [optional] **[CLadder: Assessing Causal Reasoning in Language Models](https://arxiv.org/abs/2312.04350)** (2023) — Jin, Z.; Chen, Y.; Leeb, F.; Gresele, L.; Kamal, O.; Lyu, Z.; Blin, K.; Gonzalez Adauto, F.; Kleiman-Weiner, M.; Sachan, M.; Schölkopf, B. *arXiv:2312.04350*
  `paper` · `advanced` · `access: open` · `AI angle`
  A 10K-question benchmark of associational, interventional and counterfactual queries built from causal graphs. LLMs find formal causal inference rules hard, even with a custom CausalCoT prompt.
  *Use in wiki:* Counterpoint to Kıcıman et al.: LLMs talk causality fluently but stumble on formal rung-2/3 reasoning, so students should check identification themselves.
  *Note:* The arXiv page lists no venue; widely cited as NeurIPS 2023 (not verified). The companion 'Can Large Language Models Infer Causation from Correlation?' (Corr2Cause; Jin et al., arXiv:2306.05836, https://arxiv.org/abs/2306.05836) finds 17 LLMs near random at inferring causation from correlations.

## Python for marketing analytics: notebooks and code

- [core] **[FeedX: transparent, robust A/B experimentation for Shopping feeds](https://github.com/google-marketing-solutions/feedx)** (2026) — Google Marketing Solutions. *GitHub (google-marketing-solutions/feedx)*
  `notebook` · `intermediate` · `access: open` · `Apache-2.0` · `AI angle`
  Python package plus two Colabs (experiment designer and analyzer) for item-randomized tests of product-feed changes. Uses a crossover design, CUPED adjustment for pre-period performance, and outlier trimming. It is the recommended test method for FeedGen, Google's LLM feed optimizer.
  *Use in wiki:* Strong bridge case for M6 and M8: students design and analyze an experiment that tests whether LLM-rewritten product titles actually lift clicks, so they practice CUPED and power analysis on a real marketing decision.
  Tools: feedx, pandas, numpy, scipy · Local copy: `06_M6_Causal_Inference_and_Experiments/repos/google-marketing-solutions__feedx`
  *Note:* Last commit 2026-10-21, very active. Needs Python 3.10 or later. The sister repo google-marketing-solutions/feedgen (LLM feed rewriting) is Apps Script/TypeScript with no notebooks, so link to it rather than download it.

- [core] **[Meridian GeoX: open-source geo experimentation for cross-publisher incrementality](https://github.com/google/meridian-geox)** (2026) — Google. *GitHub (google/meridian-geox); docs at developers.google.com/meridian/geox*
  `package` · `intermediate` · `access: open` · `Apache-2.0`
  Google's current geo-experiment library. It covers study design (holdback, go-dark, heavy-up, multi-cell, stratified sampling) and analysis with time-based regression, and its results feed Meridian MMM priors. Ships two Colab notebooks and example design and analysis CSVs.
  *Use in wiki:* Main in-class lab for incrementality: design a single-cell holdback test, then analyze it and talk about how the lift result would calibrate an MMM.
  [Open-access copy](https://developers.google.com/meridian/geox) · Tools: meridian-geox, google-meridian, jax · Local copy: `06_M6_Causal_Inference_and_Experiments/repos/google__meridian-geox`
  *Note:* Last commit 2026-10-01, actively developed. pip install meridian-geox. Needs Python 3.10 or later, or 3.11 or later alongside Meridian. This is the natural successor to trimmed_match and matched_markets for teaching, and pairs with google/meridian, which is already in the library.

- [core] **[mta: multi-touch attribution models in Python (heuristics, Markov chain, Shapley, Shao, logistic, additive hazard)](https://github.com/eeghor/mta)** (2026) — Korostil, I. (eeghor). *GitHub (eeghor/mta)*
  `package` · `intermediate` · `access: open` · `MIT`
  Small, readable Python library that runs first/last touch, linear, position-based, time-decay, Markov removal-effect, Shapley value, Shao's model, logistic and additive-hazard attribution on one journey dataset (sample data.csv.gz included). Models can be chained to compare credit allocations side by side.
  *Use in wiki:* In-class activity: run every attribution model on the bundled journeys, compare the channel shares, and discuss why none of them is causal (the setup for geo experiments and MMM).
  Tools: mta, pandas, numpy · Local copy: `06_M6_Causal_Inference_and_Experiments/repos/eeghor__mta`
  *Note:* Last commit 2026-10-18. No notebooks; the README has the usage examples, so the instructor or students write the notebook (a good vibe-coding exercise). Alternative: DP6/Marketing-Attribution-Models (Apache-2.0, Polars-based, docs partly in Portuguese).

- [recommended] **[AI-Assisted Statistics for Data Scientists: 50+ Essential Concepts Using R and Python, 3rd ed. (code)](https://github.com/gedeck/ai-assisted-statistics-for-data-scientists)** (2026) — Bruce, P.; Bruce, A.; Gedeck, P. *O'Reilly Media (June 2026)*
  `notebook` · `intermediate` · `access: open` · `GPL-3.0` · `AI angle`
  Python notebooks (ch01–ch10) for the 3rd edition of Practical Statistics for Data Scientists, now retitled for AI-assisted work. Ch3 covers statistical experiments and significance testing (A/B tests, permutation tests on web_page_data and four_sessions), ch4 regression, and ch10 generative AI and LLMs.
  *Use in wiki:* Assign ch03 for the A/B-testing review in M6 and ch04 for the M3 regression refresher. Ch10 supports the course's AI-assisted coding theme.
  Tools: pandas, statsmodels, scipy, scikit-learn · Local copy: `03_M3_Regression/repos/gedeck__ai-assisted-statistics-for-data-scientists`
  *Note:* Supersedes gedeck/practical-statistics-for-data-scientists (2nd ed., GPL-3.0, 3.4k stars), which the author says is no longer maintained. Skip code/data.zip (30 MB) and sp500_data.csv.gz (21 MB). The README does not describe the AI workflows in detail, so check ch10 before assigning it. The tree listing was truncated in docs/, which isn't downloaded.

- [recommended] **[Bayesian CUPED (NumPyro tutorial)](https://num.pyro.ai/en/stable/tutorials/bayesian_cuped.html)** (2026) — NumPyro contributors (adapted from Orduz, J. and Courthoud, M.). *NumPyro documentation*
  `notebook` · `intermediate` · `access: open` · `Apache-2.0`
  Short tutorial on synthetic ad-campaign revenue data. It compares a Bayesian difference-in-means with a CUPED-adjusted model fit in one NumPyro model; the posterior SD shrinks from 0.292 to 0.219 around a true effect of 2.
  *Use in wiki:* Follow-up exercise after frequentist CUPED: students check how much variance reduction they get and why the pre-period covariate matters.
  Tools: numpyro, jax, arviz
  *Note:* Single-file sparse download from a large repo. The repo was updated 2026-10-22.

- [recommended] **[Bytepawn A/B testing notebooks (CUPED, early-stopping pitfall, Fisher/Chi-squared/G/t tests, bandits)](https://github.com/mtrencseni/playground)** (2026) — Trencseni, M. *GitHub (mtrencseni/playground); blog bytepawn.com*
  `notebook` · `intermediate` · `access: open`
  About 20 short, simulation-based notebooks behind the Bytepawn blog: 'AB testing and the pitfall of early stopping', CUPED (including CUPED p-hacking and conversion CUPED), test choice (z, t, chi-squared, Fisher, G), parallel tests, and bandits.
  *Use in wiki:* Link from the M6 page as reading on why peeking inflates false positives and how CUPED can be misused.
  [Open-access copy](https://bytepawn.com/reducing-variance-in-ab-testing-with-cuped.html) · Tools: numpy, scipy, statsmodels
  *Note:* LINK ONLY: the repo has no LICENSE file, so it is all rights reserved. Do not download. The CUPED post (31 July 2021) links CUPED.ipynb in this repo. Repo last commit 2026-09-30.

- [recommended] **[Spotify Confidence: A/B test analysis including group sequential tests and variance reduction](https://github.com/spotify/confidence)** (2026) — Spotify. *GitHub (spotify/confidence)*
  `package` · `intermediate` · `access: open` · `Apache-2.0`
  Python package from Spotify's experimentation team for frequentist and Bayesian A/B test analysis, sample-size calculation, group sequential testing and regression-based variance reduction. Example notebooks are in examples/.
  *Use in wiki:* In-class demo of 'peeking' and why sequential boundaries matter. Use the Sequential and Sample-sizing notebooks as worked examples.
  Tools: spotify-confidence, pandas, statsmodels · Local copy: `06_M6_Causal_Inference_and_Experiments/repos/spotify__confidence`
  *Note:* Last commit 2026-02-26. Latest release badge shows 4.1.0. The notebooks are mostly code with little explanatory text, so pair them with the Courthoud or Trencseni write-ups. The Bayesian and Frequentist example notebooks (7.4 MB) are left out to save space.

- [recommended] **[Bayesian Decision Analysis with PyMC: Beyond A/B Testing (PyData Global 2025 tutorial)](https://github.com/AllenDowney/BDAwithPyMC)** (2025) — Downey, A. *PyData Global 2025 / PyMC Labs*
  `notebook` · `intermediate` · `access: open` · `MIT (code); CC BY-NC-SA 4.0 (text)`
  90-minute workshop notebook with exercise and solution versions: beta-binomial A/B testing, probability of superiority instead of p-values, Bayesian bandits with an adaptive email-campaign simulation, and hierarchical partial pooling. Runs on Colab.
  *Use in wiki:* Drop-in M6 lab: students fill in the exercise notebook, then compare with solutions; the email-campaign bandit is marketing-framed.
  Tools: pymc, arviz, preliz, pandas · Local copy: `06_M6_Causal_Inference_and_Experiments/repos/AllenDowney__BDAwithPyMC`
  *Note:* Pushed 2026-10-21. Requires Python 3.12+ and PyMC 5. The hierarchical example uses MLB batting data, not marketing data. The repo ships a CLAUDE.md, which shows how an author sets up an AI assistant on a teaching repo.

- [recommended] **[Matteo Courthoud's causal data science blog notebooks](https://github.com/matteocourthoud/Blog-Posts)** (2024) — Courthoud, M. *GitHub (matteocourthoud/Blog-Posts); posts on Medium / Towards Data Science*
  `notebook` · `intermediate` · `access: open`
  Notebooks behind clear, well-explained posts on cuped, group_sequential_testing, optimal_stopping, bayesian_ab_test, evaluate_uplift, meta_learners, beyond_churn, synthetic_control, double_ml and more.
  *Use in wiki:* Recommended readings that explain the intuition behind CUPED and sequential testing. Link from the M6 and M7 pages.
  Tools: statsmodels, scikit-learn, econml
  *Note:* LINK ONLY: the GitHub page shows no license, so it is all rights reserved. Last commit 2024-03-17. The NumPyro Bayesian CUPED tutorial credits Courthoud's CUPED post and data-generating code.

- [recommended] **[Behavioral Data Analysis with R and Python (companion code)](https://github.com/BuissonFlorent/BehavioralDataAnalysis)** (2021) — Buisson, F. *O'Reilly Media (June 2021)*
  `notebook` · `intermediate` · `access: open` · `MIT`
  R and Python code for a customer-behavior analytics book: causal diagrams, missing data, bootstrap uncertainty, experimental design basics, stratified randomization, cluster randomization with hierarchical models, moderation, mediation and IV. Includes exercises with solutions.
  *Use in wiki:* M6 lab material on designing (not just analyzing) marketing experiments; the stratified-randomization chapter is a good in-class exercise.
  Tools: pandas, statsmodels, R · Local copy: `06_M6_Causal_Inference_and_Experiments/repos/BuissonFlorent__BehavioralDataAnalysis`
  *Note:* Reached via oreil.ly/BehavioralDataAnalysis, which redirects here. Folder names were read from the repo page; check exact spelling before a sparse checkout. The tree API call failed, so approx_mb is an estimate (the git pack is 55 MB). Last push 2023-07. The book's R package left CRAN; Python users are told to use this repo.

- [optional] **[balance: Python package for adjusting biased samples (survey weighting)](https://github.com/facebookresearch/balance)** (2026) — Meta (facebookresearch). *GitHub (facebookresearch/balance)*
  `package` · `intermediate` · `access: open` · `MIT`
  Meta's package for reweighting non-representative samples (IPW, CBPS, raking, post-stratification), with diagnostics. Includes about 10 quickstart tutorial notebooks.
  *Use in wiki:* Short demo for marketing-research projects that rely on convenience or panel surveys. It is also useful for reweighting LLM 'synthetic respondent' samples against census margins.
  Tools: balance, pandas, scikit-learn
  *Note:* Last commit 2026-10-22, very active.

- [optional] **[Fractional Uplift: uplift modelling with complex or constrained metrics](https://github.com/google-marketing-solutions/fractional_uplift)** (2026) — Google Marketing Solutions. *GitHub (google-marketing-solutions/fractional_uplift)*
  `package` · `advanced` · `access: open` · `Apache-2.0`
  Meta-learner uplift package for targeting ads or promotions to the most incremental customers when the KPI is a ratio such as ROI or cost-constrained conversions. Includes an end-to-end example notebook.
  *Use in wiki:* Advanced extension after scikit-uplift and causalml, which are already in the library. It shows how industry turns uplift scores into ROI-constrained targeting.
  Tools: fractional-uplift, pandas
  *Note:* Last commit 2026-01-12. Needs Python 3.10 or later.

- [optional] **[Introduction to Causal Inference (SciPy 2026 tutorial materials)](https://github.com/ronikobrosly/scipy_2026_causal_inference_tutorial)** (2026) — Kobrosly, R. *SciPy 2026 (July 13, 2026)*
  `notebook` · `intro` · `access: open`
  4-hour hands-on tutorial: correlation vs causation, pitfalls of observational data, common causal approaches including DoWhy, with exercises in marimo notebooks.
  *Use in wiki:* Optional self-study for M6; marimo notebooks are a possible format for the wiki's interactive pages.
  Tools: dowhy, marimo, pandas, scikit-learn
  *Note:* No license, so link only. Not marketing-specific.

- [optional] **[Orbit: Bayesian time-series forecasting and KTR time-varying regression (Uber)](https://github.com/uber/orbit)** (2026) — Uber. *GitHub (uber/orbit)*
  `package` · `advanced` · `access: open` · `Apache-2.0`
  Uber's Bayesian structural time-series package (ETS, LGT, DLT, and KTR kernel time-varying regression). KTR with regression priors is the building block Uber used for MMM-style time-varying media coefficients.
  *Use in wiki:* Optional MMM or forecasting extension. Pair the KTR tutorials with Orduz's orbit_mmm notebook, which applies KTR to media effects.
  Tools: orbit-ml, pyro, cmdstanpy
  *Note:* Default branch is 'dev'. Last commit 2026-05-22. The tutorials are general forecasting with no marketing-specific MMM notebook in the repo. Stan backend compilation can be slow on Colab.

- [optional] **[LightweightMMM end-to-end demo notebooks (deprecated; superseded by Meridian)](https://github.com/google/lightweight_mmm)** (2025) — Google. *GitHub (google/lightweight_mmm)*
  `notebook` · `advanced` · `access: open` · `Apache-2.0`
  NumPyro-based Bayesian MMM. Two demo notebooks: simple end-to-end, and multiple geos with adstock, saturation, response curves and budget optimization.
  *Use in wiki:* Historical reference only: show how the field moved from LMMM to Meridian. Do not assign it for new student work.
  Tools: lightweight_mmm, numpyro, jax
  *Note:* ARCHIVED on 2026-01-19 (read-only). The README says 'LMMM is not supported anymore, so we highly recommend you switch to Meridian'. Last commit 2025-06-17. Pinned JAX and NumPyro versions will likely fail on current Colab.

- [optional] **[Matched Markets: geo experiment design and Time-Based Regression analysis](https://github.com/google/matched_markets)** (2025) — Google. *GitHub (google/matched_markets)*
  `package` · `intermediate` · `access: open` · `Apache-2.0`
  Python library for choosing treatment and control geos (TBR Matched Markets greedy search) and for post-test Time-Based Regression analysis. Two Colab notebooks and small sample CSVs.
  *Use in wiki:* Compact TBR example to set beside Meridian GeoX or Orduz's PyMC TBR notebook, so students can see one method in three implementations.
  Tools: matched_markets, pandas, statsmodels
  *Note:* Last commit 2025-08-21. The README says 'not an officially supported Google product; for research purposes only'.

- [optional] **[Effective-Uplift-Modeling (PyData London 2024 / SciPy 2024 talk materials)](https://github.com/takechanman1228/Effective-Uplift-Modeling)** (2024) — Takeda, H. *PyData London 2024; SciPy 2024*
  `notebook` · `intermediate` · `access: open`
  Demo code for 'Uplift Modeling: How to Enhance Customer Targeting in Marketing with Causal Machine Learning', which uses CausalML to find persuadable customers.
  *Use in wiki:* Optional M6/M7 talk + code pairing; the same author's book repo (downloadable) covers uplift in sec3.6.
  Tools: causalml, pandas
  *Note:* No license (API license null), so link only. Pushed 2026-10-07. Talk pages: london2024.pydata.org/cfp/talk/YAXGMW and cfp.scipy.org/2024/talk/3Y9KPZ.

- [optional] **[Probabilistic Programming and Bayesian Methods for Hackers, Chapter 2 (A/B testing)](https://github.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers)** (2024) — Davidson-Pilon, C. *GitHub open book*
  `notebook` · `intermediate` · `access: open` · `MIT`
  Classic open book. Chapter 2 builds the Bayesian A/B test (and a two-site comparison) from scratch, with a notebook updated for current PyMC alongside PyMC2/PyMC3/TFP versions.
  *Use in wiki:* Optional reading for students who want the Bayesian A/B test explained from first principles.
  Tools: pymc, numpy, matplotlib
  *Note:* Use Ch2_MorePyMC_PyMC_current.ipynb; the PyMC2/PyMC3 versions are legacy. The full repo is about 170 MB, so keep the sparse path.

- [optional] **[Trimmed Match: design and analysis of randomized paired geo experiments](https://github.com/google/trimmed_match)** (2023) — Google. *GitHub (google/trimmed_match)*
  `package` · `advanced` · `access: open` · `Apache-2.0`
  Python library with a C++ core for robust iROAS estimation in matched-pair geo experiments. Includes Colab notebooks for design (with cross-validation) and post-analysis, plus example datasets.
  *Use in wiki:* Instructor background or an optional deep dive on matched-pair geo designs and outlier-robust iROAS. The README's five-pair iROAS example makes a good worked illustration.
  Tools: trimmed_match, pandas, scipy
  *Note:* Last commit 2023-06-01. Not archived, but dormant. Installing it builds a C++ extension with bazel, which is slow and fragile on current Colab. The README says it was tested on Python 3.7. Prefer Meridian GeoX for student labs.

## AI-assisted coding angle for this module

Resources in this folder that show the method done with AI help, LLM versions of the method, or documented failure modes of AI-written analysis:

- [FeedX: transparent, robust A/B experimentation for Shopping feeds](https://github.com/google-marketing-solutions/feedx)
- [CausalPy: causal inference for quasi-experiments in Python](https://github.com/pymc-labs/CausalPy)
- [PyMC-Marketing: Bayesian MMM, CLV and choice models in Python](https://www.pymc-marketing.io/en/stable/)
- [Causal Reasoning and Large Language Models: Opening a New Frontier for Causality](https://arxiv.org/abs/2305.00050)
- [Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus?](https://www.nber.org/papers/w31122)
- [AI-Assisted Statistics for Data Scientists: 50+ Essential Concepts Using R and Python, 3rd ed. (code)](https://github.com/gedeck/ai-assisted-statistics-for-data-scientists)
- [Better Experiments with LLM Evals: A funnel, not a fork](https://engineering.atspotify.com/2026/5/better-experiments-with-llm-evals-a-funnel-not-a-fork)
- [Robyn: Meta's open-source marketing mix modeling package](https://github.com/facebookexperimental/Robyn)
- [Using Large Language Models to Simulate Multiple Humans and Replicate Human Subject Studies](https://arxiv.org/abs/2208.10264)
- [PyWhy-LLM: integrating LLM capabilities into causal analysis](https://github.com/py-why/pywhy-llm)
- [CLadder: Assessing Causal Reasoning in Language Models](https://arxiv.org/abs/2312.04350)

## Also relevant (catalogued in other folders)

- **`01_M1_Marketing_Analytics_and_Python`**: [Applying Data Analytics in Marketing](https://www.coursera.org/learn/applying-data-analytics-business-in-marketing); [Marketing Analytics (MBA/EWMBA 263) course overview, UC Berkeley Haas](https://aiai.berkeley.edu/course-overview-mock-ups/); [Cutting-Edge Marketing Analytics: Real World Cases and Data Sets for Hands On Learning](https://www.oreilly.com/library/view/-/9780133552584/)
- **`02_M2_Customer_Data_and_Visualization`**: [Lab: collecting public data from an API (McBroken, McDonald's ice-cream machines)](https://github.com/nene88991999/BADM534-Marketing-Analytics/tree/main/01_Resources/02_M2_Customer_Data_and_Visualization/mcbroken_api_lab); [Browsing the Aisles or Browsing the App? How Online Grocery Shopping is Changing What We Buy](https://pubsonline.informs.org/doi/10.1287/mksc.2022.0292); [mcbroken-archive: hourly git-scraped snapshots of McBroken since October 2020](https://github.com/MrFlynn/mcbroken-archive)
- **`03_M3_Regression`**: [PyFixest: fast high-dimensional fixed-effects regression in Python (quickstart, tutorials, llms.txt and agent skill file)](https://pyfixest.org/getting-started.html); [The Effect: An Introduction to Research Design and Causality, Chapter 13: Regression](https://theeffectbook.net/ch-StatisticalAdjustment.html); [Coding for Economists: Regression](https://aeturrell.github.io/coding-for-economists/econmt-regression.html); [linearmodels: panel data, instrumental variables and system regression for Python](https://bashtage.github.io/linearmodels/); [Meta-Analysis of Advertising Effectiveness: New Insights from Improved Bias Corrections](https://pure.eur.nl/en/publications/meta-analysis-of-advertising-effectiveness-new-insights-from-impr/); [Are Large Language Models Good Statisticians?](https://arxiv.org/abs/2406.07815); [Are LLMs Capable of Data-based Statistical and Causal Reasoning? Benchmarking Advanced Quantitative Reasoning with Data](https://arxiv.org/abs/2402.17644); [When Should You Adjust Standard Errors for Clustering?](https://www.nber.org/papers/w24003); [Causal Inference: The Mixtape, Chapter 2: Probability and Regression Review](https://mixtape.scunning.com/02-probability_and_regression); [TV Advertising Effectiveness and Profitability: Generalizable Results from 288 Brands](https://papers.ssrn.com/abstract=3273476); [Regression and Other Stories](https://avehtari.github.io/ROS-Examples/); [Bayesian Methods for Media Mix Modeling with Carryover and Shape Effects](https://research.google/pubs/bayesian-methods-for-media-mix-modeling-with-carryover-and-shape-effects/); [Linear Regression in Python (QuantEcon lecture)](https://python.quantecon.org/ols.html); [A Practitioner's Guide to Cluster-Robust Inference](https://cameron.econ.ucdavis.edu/research/Cameron_Miller_JHR_2015_February.pdf); [The garden of forking paths: Why multiple comparisons can be a problem, even when there is no 'fishing expedition' or 'p-hacking' and the research hypothesis was posited ahead of time](https://sites.stat.columbia.edu/gelman/research/unpublished/p_hacking.pdf); [PyMC-Marketing: Additive vs Log vs Log-Log MMMs (and the end-to-end MMM example)](https://www.pymc-marketing.io/en/stable/notebooks/mmm/mmm_multiplicative.html)
- **`04_M4_Conjoint_Segmentation_CLV`**: [Juan Orduz website projects: Bayesian marketing-analytics notebooks](https://github.com/juanitorduz/website_projects); [pyrsm example notebooks (Rady School of Management business-analytics toolkit)](https://github.com/radiant-ai-hub/pyrsm); [TensorHouse: reference notebooks for marketing, promotions and pricing (successor to Introduction to Algorithmic Marketing examples)](https://github.com/ikatsov/tensor-house); [The Challenge of Using LLMs to Simulate Human Behavior: A Causal Inference Perspective](https://arxiv.org/abs/2312.15524); [Using LLMs for Market Research](https://papers.ssrn.com/abstract=4395751); [PyDOE: Design of Experiments for Python (successor to pyDOE3)](https://github.com/pydoe/pydoe)
- **`05_M5_Text_and_Social_Media_Analytics`**: [Seeding Strategies for Viral Marketing: An Empirical Comparison](https://doi.org/10.1509/jm.10.0088); [Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs for Text Annotation](https://arxiv.org/abs/2509.08825v2); [Text as Data: A New Framework for Machine Learning and the Social Sciences](https://press.princeton.edu/books/paperback/9780691207551/text-as-data); [Identifying Influential and Susceptible Members of Social Networks](https://doi.org/10.1126/science.1215842); [The Effect of Word of Mouth on Sales: Online Book Reviews](https://doi.org/10.1509/jmkr.43.3.345)
- **`07_M7_Predictive_Models_ML_and_AI`**: [Following Good Examples: Health Goal-Oriented Food Recommendation based on Behavior Data](https://dl.acm.org/doi/10.1145/3485447.3514193); [The Economics of Recommender Systems: Evidence from a Field Experiment on MovieLens](https://www.econstor.eu/handle/10419/271773); [How Algorithmic Confounding in Recommendation Systems Increases Homogeneity and Decreases Utility](https://www.arxiv.org/abs/1710.11214); [Machine Learning: An Applied Econometric Approach](https://www.aeaweb.org/articles?id=10.1257/jep.31.2.87); [Prediction Policy Problems](https://www.aeaweb.org/articles?id=10.1257/aer.p20151023); [Engagement, User Satisfaction, and the Amplification of Divisive Content on Social Media](https://pmc.ncbi.nlm.nih.gov/articles/PMC11894805/); [Short-term Exposure to Filter-Bubble Recommendation Systems Has Limited Polarization Effects: Naturalistic Experiments on YouTube](https://doi.org/10.1073/pnas.2318127122); [Recommendations as Treatments: Debiasing Learning and Evaluation](https://proceedings.mlr.press/v48/schnabel16.html); [Unintended Consequences of Recommender System Interventions: Evidence from a Field Experiment](https://arxiv.org/abs/2606.08265v1); [Understanding or Manipulation: Rethinking Online Performance Gains of Modern Recommender Systems](https://arxiv.org/abs/2210.05662v2); [Reducing Recommender System Biases: An Investigation of Rating Display Designs](https://misq.org/reeducing-recommender-system-biases-an-investigation-of-rating-display-designs.html); [Is Seeing Believing? How Recommender Interfaces Affect Users' Opinions](https://experts.umn.edu/en/publications/is-seeing-believing-how-recommender-interfaces-affect-users-opini/)
- **`08_M8_Current_Topics_in_Marketing`**: [Competition in Generative AI: Evidence from Consumer Demand](https://www.nber.org/papers/w35953); [Generative-AI Demand: Public Signals and a Synthetic Subscription Panel](https://github.com/nene88991999/BADM534-Marketing-Analytics/tree/main/01_Resources/08_M8_Current_Topics_in_Marketing/genai_demand_lab); [Retail Media ROAS Demystified: Understanding Your Brand's ROAS](https://ovative.com/impact/expert-insights/retail-media-roas-demystified/); [Algorithmic Bias? An Empirical Study of Apparent Gender-Based Discrimination in the Display of STEM Career Ads](https://ideas.repec.org/a/inm/ormnsc/v65y2019i7p2966-2981.html); [Frontiers: Generative AI and Personalized Video Advertisements](https://pubsonline.informs.org/doi/fpi/10.1287/mksc.2023.0494); [Awesome Marketing Science (curated list)](https://github.com/shakostats/Awesome-Marketing-Science)
- **`10_AI_Coding_Concepts_and_Evidence`**: [We are Changing our Developer Productivity Experiment Design](https://metr.org/blog/2026-02-24-uplift-update/); [Generative AI at Work](https://digitaleconomy.stanford.edu/publication/generative-ai-at-work); [Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/); [The Effects of Generative AI on High-Skilled Work: Evidence from Three Field Experiments with Software Developers](https://pubsonline.informs.org/doi/fpi/10.1287/mnsc.2025.00535); [BLADE: Benchmarking Language Model Agents for Data-Driven Science](https://arxiv.org/abs/2408.09667); [Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of AI on Knowledge Worker Productivity and Quality](https://papers.ssrn.com/abstract=4573321); [The Impact of AI on Developer Productivity: Evidence from GitHub Copilot](https://arxiv.org/abs/2302.06590); [Automated Social Science: Language Models as Scientist and Subjects](https://arxiv.org/abs/2404.11794); [How much does AI impact development speed? An enterprise-based randomized controlled trial](https://arxiv.org/abs/2410.12944)
- **`11_AI_Coding_Tools_and_Workflows`**: [Do Users Write More Insecure Code with AI Assistants?](https://arxiv.org/abs/2211.03622)
- **`12_AI_Coding_Pedagogy_and_Policy`**: [Generative AI without guardrails can harm learning: Evidence from high school mathematics](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4895486); [Your Brain on ChatGPT: Accumulation of Cognitive Debt when Using an AI Assistant for Essay Writing Task](https://arxiv.org/abs/2506.08872)
- **`20_Datasets`**: [Google Analytics 4 sample ecommerce dataset (Google Merchandise Store) in BigQuery](https://developers.google.com/analytics/bigquery/web-ecommerce-demo-dataset); [The Upworthy Research Archive](https://upworthy.natematias.com/); [Kevin Hillstrom MineThatData E-Mail Analytics Challenge dataset](https://www.uplift-modeling.com/en/latest/api/datasets/fetch_hillstrom.html); [dunnhumby Source Files: The Complete Journey, Breakfast at the Frat, Carbo-Loading, Let's Get Sort-of-Real](https://www.dunnhumby.com/source-files/); [PyMC-Marketing example data: synthetic MMM and CDNOW CLV](https://www.pymc-marketing.io/en/stable/notebooks/mmm/mmm_example.html); [Epoch AI: Notable AI Models (data hub)](https://epoch.ai/data/notable-ai-models); [causaldata (Python, R and Stata package)](https://pypi.org/project/causaldata/); [Criteo Uplift Prediction Dataset (v2.1)](https://ailab.criteo.com/?p=859); [Dominick's Finer Foods scanner data](https://www.chicagobooth.edu/research/kilts/research-data/dominicks); [Google Meridian simulated geo-level MMM data (geo_all_channels)](https://developers.google.com/meridian/docs/user-guide/load-geo-data-with-organic-and-non-media); [Criteo Attribution Modeling for Bidding Dataset](https://ailab.criteo.com/?p=649); [Open Bandit Dataset and Open Bandit Pipeline](https://github.com/st-tech/zr-obp)
- **`21_Open_Textbooks_and_Courses`**: [Marketing Science in Python: A Practitioner's Guide (companion code)](https://github.com/takechanman1228/marketing-science-in-python); [Data Analytics for Marketing: A practical guide to analyzing marketing data using Python (companion code)](https://github.com/PacktPublishing/Data-Analytics-for-Marketing); [Causal Inference for the Brave and True](https://matheusfacure.github.io/python-causality-handbook/landing-page.html); [The Effect: An Introduction to Research Design and Causality](https://theeffectbook.net/); [Coding for Economists](https://aeturrell.github.io/coding-for-economists/); [Marketing Analytics and Data Science: Tools and Models (supplementary code)](https://link.springer.com/book/9783032111296); [Applied Causal Inference Powered by ML and AI](https://causalml-book.org/); [Machine Learning and Generative AI for Marketing (companion code)](https://github.com/PacktPublishing/Machine-Learning-and-Generative-AI-for-Marketing); [Ad response tutorial: last-click attribution, experiments, MMM and attribution models](https://github.com/eleafeit/ad_response_tutorial); [Computational and Inferential Thinking: The Foundations of Data Science, 2nd ed. (Berkeley Data 8)](https://inferentialthinking.com/); [Business Data Science: code and examples](https://github.com/TaddyLab/BDS); [Darden Business Publishing (cases, simulations, course packs)](https://store.darden.virginia.edu/); [Hands-On Data Science for Marketing (code repository)](https://github.com/PacktPublishing/Hands-On-Data-Science-for-Marketing)
- **`22_Wiki_Design_and_Hosting`**: [Seeing Theory](https://seeing-theory.brown.edu/)
