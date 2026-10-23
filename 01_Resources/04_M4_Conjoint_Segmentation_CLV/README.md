# M4 · Conjoint Analysis, Clustering and Customer Lifetime Value

33 resources (14 core). Built 2026-10-23 from `00_Index/_data/`; edit the YAML there and rerun `00_Index/_build/build_catalog.py` rather than editing this file.

Priority: **core** = likely to assign or build on; **recommended** = strong supplement; **optional** = background or niche. *Access* tells you whether students can open it without a login.

## Contents

- [Conjoint: foundations](#conjoint-foundations) (5)
- [Conjoint: design, estimation and tools](#conjoint-design-estimation-and-tools) (9)
- [LLMs as survey and conjoint respondents](#llms-as-survey-and-conjoint-respondents) (7)
- [Segmentation and clustering](#segmentation-and-clustering) (4)
- [Customer lifetime value](#customer-lifetime-value) (8)

## Conjoint: foundations

- [core] **[Applied Conjoint Analysis](https://link.springer.com/book/10.1007/978-3-540-87753-0)** (2014) — Rao, V. R. *Springer, Berlin/Heidelberg*
  `book` · `intermediate` · `access: library`
  Comprehensive text in ten chapters: ratings-based and choice-based designs, part-worth estimation, many-attribute methods, and applications to product design, positioning, segmentation, pricing and other marketing-mix decisions.
  *Use in wiki:* Main textbook reference for the conjoint unit. Assign chapters through the UIUC library's Springer access.
  DOI [10.1007/978-3-540-87753-0](https://doi.org/10.1007/978-3-540-87753-0)

- [core] **[Conjoint Analysis, Related Modeling, and Applications](https://mitsloan.mit.edu/shared/ods/documents/?PublicationDocumentID=5592)** (2004) — Hauser, J. R.; Rao, V. R. *Advances in Market Research and Modeling: Progress and Prospects (Kluwer), pp. 141-168*
  `book-chapter` · `intermediate` · `access: open`
  Free review of the field's history, design choices, estimation methods (including HB and adaptive approaches) and applications.
  *Use in wiki:* Free assigned reading that complements Rao (2014).
  *Note:* Download link taken from John Hauser's MIT 'Papers & Books' page.

- [recommended] **[Economic Valuation of Product Features](https://link.springer.com/article/10.1007/s11129-014-9150-x)** (2014) — Allenby, G. M.; Brazell, J. D.; Howell, J. R.; Rossi, P. E. *Quantitative Marketing and Economics 12, 421-456*
  `paper` · `advanced` · `access: library`
  Values a product feature as the change in equilibrium profits, using a conjoint-estimated demand system plus competitor and cost data. With digital camera data, this gives very different answers from naive WTP or welfare measures.
  *Use in wiki:* Key reading for why the 'WTP = -beta/beta_price' shortcut can mislead. It motivates building market simulators with competitors.
  DOI [10.1007/s11129-014-9150-x](https://doi.org/10.1007/s11129-014-9150-x)

- [recommended] **[Conjoint Analysis in Consumer Research: Issues and Outlook](https://academic.oup.com/jcr/article-abstract/5/2/103/1805825)** (1978) — Green, P. E.; Srinivasan, V. *Journal of Consumer Research 5(2), 103-123*
  `paper` · `advanced` · `access: library`
  Foundational review that brought conjoint analysis into consumer research. It covers preference models, data collection, stimulus construction, estimation and reliability.
  *Use in wiki:* Classic citation for the history of conjoint. Instructor background.
  DOI [10.1086/208721](https://doi.org/10.1086/208721)
  *Note:* The 1990 Journal of Marketing follow-up by the same authors was not verified here.

- [optional] **[Polyhedral Methods for Adaptive Choice-Based Conjoint Analysis](https://mitsloan.mit.edu/shared/ods/documents/?PublicationDocumentID=4040)** (2004) — Toubia, O.; Hauser, J. R.; Simester, D. I. *Journal of Marketing Research 41(1), 116-131*
  `paper` · `advanced` · `access: open`
  Adaptive question design for CBC that picks each next choice set to shrink the feasible region of part-worths as fast as possible. A key step from classic to optimization- and ML-based conjoint.
  *Use in wiki:* Instructor background on adaptive design. It also motivates the idea that question design and estimation interact.
  *Note:* Companion review: Toubia, Evgeniou & Hauser (2007), 'Optimization-Based and Machine-Learning Methods for Conjoint Analysis' (https://mitsloan.mit.edu/shared/ods/documents/?PublicationDocumentID=5582). See also Hauser, Eggers & Selove (2019, Marketing Science), 'The Strategic Implications of Scale in Choice-Based Conjoint Analysis' (https://mitsloan.mit.edu/shared/ods/documents/?PublicationDocumentID=5576). Toubia's recent conjoint-adjacent work on LLM digital twins appears below.

## Conjoint: design, estimation and tools

- [core] **[xlogit: GPU-accelerated multinomial and mixed logit estimation in Python](https://github.com/arteagac/xlogit)** — Arteaga, C. and contributors. *GitHub / Read the Docs*
  `package` · `intermediate` · `access: open` · `GPL-3.0`
  Estimates MNL, conditional logit and mixed logit (normal, lognormal, triangular, uniform and truncated-normal mixing), handles panel and unbalanced data with Halton draws, fits WTP-space models, and runs on GPU via CuPy when available.
  *Use in wiki:* Estimation engine for the CBC exercise. The WTP-space notebook (yogurt data ported from R logitr) shows WTP estimated directly, and a Colab-ready mixed logit notebook is provided.
  Tools: xlogit, numpy, cupy · Local copy: `04_M4_Conjoint_Segmentation_CLV/repos/arteagac__xlogit`
  *Note:* WTP-space notebook: https://xlogit.readthedocs.io/en/latest/notebooks/wtp_space.html. Colab: https://colab.research.google.com/github/arteagac/xlogit/blob/master/examples/mixed_logit_model.ipynb. An older alternative is pylogit (BSD-3, https://github.com/timothyb0912/pylogit), which covers MNL, nested and normal-mixing mixed logit and has notebooks in examples/; its maintenance status is unclear.

- [recommended] **[cbcTools and logitr: R packages for designing choice-based conjoint surveys and estimating preference- and WTP-space logit models](https://jhelvy.github.io/cbcTools/)** (2023) — Helveston, J. P. *CRAN; logitr described in Journal of Statistical Software 105(10)*
  `package` · `intermediate` · `access: open` · `MIT`
  cbcTools covers profile generation, priors, random and D-optimal design (labeled, no-choice and dominance-removed), checks for balance, overlap and D-error, simulated choices, and power analysis. logitr fits MNL and mixed logit in preference or WTP space and predicts shares.
  *Use in wiki:* The cleanest end-to-end CBC design workflow. Use it with R, or have students ask an AI assistant to reproduce a cbcTools design in Python and compare D-errors.
  DOI [10.18637/jss.v105.i10](https://doi.org/10.18637/jss.v105.i10) · Tools: R, cbcTools, logitr
  *Note:* logitr docs: https://jhelvy.github.io/logitr/. The DOI is for the logitr JSS article.

- [recommended] **[Conjointly: conjoint analysis for students and academics (fee waiver)](https://conjointly.com/faq/conjoint-analysis-for-students-and-academics/)** — Conjointly. *Conjointly*
  `tool` · `intro` · `access: free-registration`
  Online survey and conjoint platform. Its free Basic tier allows Generic Conjoint up to 20 responses. An academic fee waiver for students and teachers with an academic email gives a one-year licence with unlimited respondents, excluding panel sampling and paid services.
  *Use in wiki:* Easiest way for project teams to field a real CBC. Have students apply for waivers early, since processing can take up to 4 weeks.
  Tools: Conjointly
  *Note:* Free academic users generally get no support. The site lists an 'API and MCP' resource (https://conjointly.com/api/) that was not inspected. Pricing page: https://conjointly.com/pricing/.

- [recommended] **[PyMC-Marketing customer choice notebooks: Multinomial Logit and the IIA property (plus mixed logit, nested logit, MaxDiff)](https://www.pymc-marketing.io/en/stable/notebooks/customer_choice/mnl_logit.html)** — PyMC Labs and PyMC-Marketing contributors. *PyMC-Marketing documentation*
  `notebook` · `intermediate` · `access: open` · `Apache-2.0`
  Bayesian MNL on heating-system choice data, with counterfactual market-share simulations: raising one product's price and removing a product. It shows IIA's proportional substitution and motivates nested logit. Sibling notebooks cover mixed logit, nested logit, consideration sets, MaxDiff and Bayesian BLP.
  *Use in wiki:* Market-simulator demo: change a price and watch shares move. It also gives a concrete, visible case of IIA's proportional-substitution problem.
  Tools: pymc-marketing, pymc · Local copy: `04_M4_Conjoint_Segmentation_CLV/repos/pymc-labs__pymc-marketing`
  *Note:* The MNL notebook does not compute WTP; add -beta_attribute/beta_price yourself. Mixed logit: https://www.pymc-marketing.io/en/stable/notebooks/customer_choice/mixed_logit.html. MaxDiff: https://www.pymc-marketing.io/en/stable/notebooks/customer_choice/maxdiff.html. A simpler PyMC gallery version on the same heating data: https://www.pymc.io/projects/examples/en/latest/generalized_linear_models/GLM-discrete-choice_models.html.

- [recommended] **[Sawtooth Software Lighthouse Studio (CBC, ACBC, MaxDiff, HB estimation, market simulator)](https://sawtoothsoftware.com/lighthouse-studio)** — Sawtooth Software. *Sawtooth Software*
  `tool` · `intermediate` · `access: freemium`
  Industry-standard conjoint and MaxDiff platform with CBC, Adaptive CBC, HB estimation and a market simulator for product, price and competitor scenarios. A free starter account is available.
  *Use in wiki:* Industry reference point and demo. Its technical-papers library (CBC, HB, market simulators, design) is excellent free instructor background.
  Tools: Lighthouse Studio, Discover
  *Note:* Academic access: the site lists 'Student Grants' (studentgrants@sawtooth.com) but has no public page for it, so email them about course licenses. Technical papers: https://sawtoothsoftware.com/resources/technical-papers. The home page mentions an 'AI follow-up' survey element; no synthetic-respondent feature was seen.

- [optional] **[Biogeme: maximum likelihood (and Bayesian) estimation of discrete choice models](https://biogeme.epfl.ch/)** — Bierlaire, M. (EPFL TRANSP-OR). *EPFL*
  `package` · `advanced` · `access: open` · `Distributed free of charge (no license named on the site)`
  Mature discrete choice estimation package built on pandas. Version 3.3.5 adds JAX-based evaluation, Bayesian estimation and richer diagnostics, alongside an examples gallery, a primer and YouTube tutorials.
  *Use in wiki:* Pointer for students who want nested or cross-nested logit or latent-class choice models beyond xlogit.
  Tools: biogeme, pandas, jax
  *Note:* Requires Python 3.12 or later (pip install biogeme). The site asks users to cite the Biogeme primer.

- [optional] **[Choice-Learn: discrete choice modeling with large datasets](https://github.com/artefactory/choice-learn)** — Artefact Research (artefactory). *GitHub*
  `package` · `intermediate` · `access: open` · `MIT`
  Python library with conditional logit, nested logit and neural random-utility models (RUMnet, TasteNet), plus assortment and pricing optimization on top of fitted choice models (needs Gurobi or OR-Tools).
  *Use in wiki:* Extension for teams linking conjoint or choice estimates to assortment and price optimization. The intro notebooks make a clean clogit tutorial.
  Tools: choice-learn, tensorflow, ortools · Local copy: `04_M4_Conjoint_Segmentation_CLV/repos/artefactory__choice-learn`
  *Note:* Notebooks of interest: notebooks/introduction/3_model_clogit.ipynb and notebooks/auxiliary_tools/assortment_example.ipynb.

- [optional] **[PyDOE: Design of Experiments for Python (successor to pyDOE3)](https://github.com/pydoe/pydoe)** — PyDOE contributors. *GitHub / PyPI*
  `package` · `intro` · `access: open` · `BSD-3-Clause`
  Python DOE toolkit covering full and fractional factorial, response-surface, space-filling (Latin hypercube, Sobol), optimal, Taguchi and sequential designs.
  *Use in wiki:* Generate full or fractional factorial profile sets for a toy conjoint. For real CBC choice-set designs, prefer cbcTools or a survey platform.
  Tools: pydoe
  *Note:* pyDOE3 (https://github.com/relf/pyDOE3) is archived and its README tells users to migrate to pydoe/pydoe. pyDOE3 documented optimal designs (Fedorov, DETMAX; D, A and I criteria); confirm the same functions exist in PyDOE.

- [optional] **[Qualtrics Conjoint projects: getting started with choice-based conjoint](https://www.qualtrics.com/support/conjoint-project/getting-started-conjoints/getting-started-choice-based/)** — Qualtrics. *Qualtrics Support*
  `documentation` · `intro` · `access: paid`
  Guide to building choice-based conjoint projects in Qualtrics. Conjoint is a separately purchased add-on that needs Choice Based Conjoint and JavaScript permissions, and analysis is capped below 10,000 responses.
  *Use in wiki:* Only useful if UIUC's campus Qualtrics license includes the Conjoint add-on. Check with campus IT before recommending it.
  Tools: Qualtrics
  *Note:* Whether UIUC has the add-on was not verified. The page does not describe a simulator.

## LLMs as survey and conjoint respondents

- [core] **[AI-Human Hybrids for Marketing Research: Leveraging Large Language Models (LLMs) as Collaborators](https://journals.sagepub.com/doi/10.1177/00222429241276529)** (2025) — Arora, N.; Chakraborty, I.; Nishimura, Y. *Journal of Marketing 89(2), 43-70*
  `paper` · `intermediate` · `access: library` · `AI angle`
  Frames LLMs as collaborators in qualitative research (synthetic respondents, interviews, theme coding) and quantitative research (synthetic survey data). Few-shot prompting and RAG improve quality, and a study replication was run with a Fortune 500 food company.
  *Use in wiki:* Practitioner-facing JM framework for how to use LLMs in market research, rather than whether to. It fits the M4 synthetic-respondent activity.
  DOI [10.1177/00222429241276529](https://doi.org/10.1177/00222429241276529)

- [core] **[Digital Twins as Funhouse Mirrors: Five Key Distortions](https://arxiv.org/abs/2509.19088)** (2025) — Peng, T.; Gui, G.; Brucks, M.; Merlau, D. J.; Fan, G. J.; Ben Sliman, M.; Johnson, E. J.; et al.; Toubia, O. *arXiv:2509.19088 (v5, Apr 2026)*
  `paper` · `intermediate` · `access: open` · `AI angle`
  Mega-study of 19 preregistered studies and 164 outcomes. Digital twins built from 500+ answers per person beat a generic LLM only slightly and correlate weakly with real answers (mean r = 0.20). Five distortions are documented: insufficient individuation, stereotyping, representation bias, ideological bias and hyper-rationality.
  *Use in wiki:* The most current large-scale validation (2025-26) of synthetic respondents. Use it as the critical counterweight in the synthetic-conjoint activity.
  *Note:* A more optimistic 2025 counterpoint is Maier et al., 'LLMs Reproduce Human Purchase Intent via Semantic Similarity Elicitation of Likert Ratings' (https://arxiv.org/abs/2510.08338). Its free-text-plus-embedding method reached about 90% of human test-retest reliability on 57 personal-care surveys. Some of its authors work in industry (Wiecki is, from recollection, at PyMC Labs).

- [core] **[Frontiers: Can Large Language Models Capture Human Preferences?](https://arxiv.org/abs/2305.02531)** (2024) — Goli, A.; Singh, A. *Marketing Science (arXiv preprint 'Can LLMs Capture Human Preferences?')*
  `paper` · `intermediate` · `access: open` · `AI angle`
  Asks GPT-3.5 and GPT-4 intertemporal-choice conjoint-style questions across languages. Both models are far less patient than humans, and 'chain-of-thought conjoint' narrows but doesn't close the gap. The authors recommend LLMs for generating hypotheses, not as stand-ins for respondents.
  *Use in wiki:* Paired reading with Brand et al. Good for a discussion of when synthetic respondents mislead.
  *Note:* Published in Marketing Science (2024). The DOI could not be confirmed because INFORMS blocked automated access.

- [core] **[The Challenge of Using LLMs to Simulate Human Behavior: A Causal Inference Perspective](https://arxiv.org/abs/2312.15524)** (2023) — Gui, G.; Toubia, O. *arXiv:2312.15524 (v3, Nov 2025); SSRN*
  `paper` · `advanced` · `access: open` · `AI angle`
  Shows that LLM-simulated price and attribute experiments are confounded: changing the treatment in a prompt shifts unstated factors, which produces implausible demand curves in a 40-product study. Proposes 'unblinding' (revealing the design) and fine-tuning as fixes.
  *Use in wiki:* Required reading before any synthetic conjoint or pricing exercise. It explains why naive prompts give wrong elasticities.
  DOI [10.2139/ssrn.4650172](https://doi.org/10.2139/ssrn.4650172)

- [core] **[Using LLMs for Market Research](https://papers.ssrn.com/abstract=4395751)** (2023) — Brand, J.; Israeli, A.; Ngwe, D. *Harvard Business School Working Paper 23-062 (SSRN, revised Apr 2026)*
  `paper` · `intermediate` · `access: open` · `AI angle`
  Draws many GPT responses per survey question to estimate WTP for product features. Estimates are sometimes close to human studies but often inaccurate and occasionally wrong-signed. Fine-tuning on past surveys helps for new features in the same category but not for new categories or segment differences.
  *Use in wiki:* Anchor reading for an exercise in which teams run a synthetic-respondent conjoint with an LLM, compare it with their human CBC, and report where it diverges.
  *Note:* The abstract became more cautious over revisions: the HBS page (https://www.hbs.edu/faculty/Pages/item.aspx?num=63859, July 2024) calls the WTP estimates 'plausible', while the April 2026 SSRN revision says they are often inaccurate. Assign the latest version.

- [recommended] **[Synthetic Replacements for Human Survey Data? The Perils of Large Language Models](https://www.cambridge.org/core/journals/political-analysis/article/synthetic-replacements-for-human-survey-data-the-perils-of-large-language-models/B92267DC26195C7F36E63EA04A47D2FE)** (2024) — Bisbee, J.; Clinton, J. D.; Dorff, C.; Kenkel, B.; Larson, J. M. *Political Analysis 32(4), 401-416*
  `paper` · `intermediate` · `access: open` · `CC BY 4.0` · `AI angle`
  ChatGPT personas match ANES group averages but show too little variance, yield regression coefficients that differ significantly from the survey's, shift with small prompt changes, and drift over three months.
  *Use in wiki:* Open-access critique showing that synthetic samples can get the means right but the regressions wrong, which ties M3 back to M4.
  DOI [10.1017/pan.2024.5](https://doi.org/10.1017/pan.2024.5)
  *Note:* Optimistic counterpart: Argyle et al. (2023), 'Out of One, Many: Using Language Models to Simulate Human Samples', Political Analysis 31(3), 337-351, doi 10.1017/pan.2023.2 (paywalled). Also Horton, Filippas & Manning, 'Homo Silicus', NBER w31122 (https://www.nber.org/papers/w31122).

- [optional] **[Twin-2K-500: A dataset for building digital twins of over 2,000 people based on their answers to over 500 questions](https://huggingface.co/datasets/LLM-Digital-Twin/Twin-2K-500)** (2025) — Toubia, O.; Gui, G. Z.; Peng, T.; Merlau, D. J.; Li, A.; Chen, H. *Hugging Face (LLM-Digital-Twin); arXiv:2505.17479*
  `dataset` · `advanced` · `access: open` · `CC BY 4.0` · `AI angle`
  Four-wave survey of 2,058 US participants (demographics, psychological scales, economic preferences, behavioral-economics experiments, and a pricing survey per the paper) with a test-retest wave, released for building and testing LLM persona simulations.
  *Use in wiki:* Optional project dataset for teams testing whether LLM 'twins' reproduce individual consumer answers.
  [Open-access copy](https://arxiv.org/abs/2505.17479)
  *Note:* 733 MB of Parquet on Hugging Face, so link to it rather than mirroring. The HF card does not mention the pricing survey; the arXiv abstract does.

## Segmentation and clustering

- [core] **[Market Segmentation Analysis: Understanding It, Doing It, and Making It Useful](https://link.springer.com/book/10.1007/978-981-10-8818-6)** (2018) — Dolnicar, S.; Grün, B.; Leisch, F. *Springer Singapore (Management for Professionals)*
  `book` · `intro` · `access: open` · `CC BY 4.0`
  Open-access, practitioner-oriented guide to the whole segmentation process: deciding to segment, data, extracting segments (k-means, hierarchical, mixtures), profiling, describing, selecting target segments and customizing the marketing mix, with R examples.
  *Use in wiki:* Main segmentation-and-targeting reading. Because the CC BY license allows it, figures and checklists can be adapted into wiki pages with attribution.
  DOI [10.1007/978-981-10-8818-6](https://doi.org/10.1007/978-981-10-8818-6) · Tools: R
  *Note:* The companion R package (MSA on CRAN) was not verified because CRAN blocked the fetch.

- [core] **[scikit-learn User Guide: Clustering, and Gaussian Mixture Models](https://scikit-learn.org/stable/modules/clustering.html)** — scikit-learn developers. *scikit-learn 1.9 documentation*
  `documentation` · `intro` · `access: open`
  Reference for KMeans and MiniBatchKMeans, agglomerative clustering (Ward, complete, average, single), spectral clustering, DBSCAN and HDBSCAN, OPTICS and BIRCH, with a comparison table and evaluation metrics. The mixture chapter covers GaussianMixture, BIC-based selection of k and BayesianGaussianMixture.
  *Use in wiki:* Primary API reference for the segmentation lab. The BIC model-selection example answers the 'how many segments?' question.
  Tools: scikit-learn
  *Note:* GMM page: https://scikit-learn.org/stable/modules/mixture.html. The KMeans section links a silhouette-analysis example for choosing k.

- [recommended] **[StepMix: latent class and latent profile analysis in Python with a scikit-learn API](https://github.com/Labo-Lacourse/stepmix)** (2025) — Labo-Lacourse (StepMix authors). *GitHub; Journal of Statistical Software 113(8)*
  `package` · `intermediate` · `access: open` · `MIT`
  Generalized mixture models: latent class analysis for categorical survey items, latent profile (Gaussian) for continuous data, and mixed data with FIML for missing values. It supports 1-, 2- and 3-step estimation with covariates and distal outcomes, plus BIC, AIC, BLRT and cross-validation, and has Colab tutorials.
  *Use in wiki:* Latent-class segmentation of survey or attitudinal data as a model-based alternative to k-means. The Colab tutorials can be embedded.
  DOI [10.18637/jss.v113.i08](https://doi.org/10.18637/jss.v113.i08) · Tools: stepmix, scikit-learn
  *Note:* Individual JSS author names were not captured. Cite it from the README's JSS reference.

- [recommended] **[Python Data Science Handbook: In Depth: k-Means Clustering (and the following section on Gaussian Mixture Models)](https://jakevdp.github.io/PythonDataScienceHandbook/05.11-k-means.html)** — VanderPlas, J. *O'Reilly (free online edition)*
  `book-chapter` · `intro` · `access: open` · `Code MIT; text CC BY-NC-ND`
  Clear, visual explanation of k-means as EM, its caveats (local optima, choosing k, linear boundaries) and worked examples. The next section extends this to GMMs.
  *Use in wiki:* Gentle pre-reading before the segmentation lab. The notebooks can be embedded directly.
  Tools: scikit-learn, matplotlib · Local copy: `21_Open_Textbooks_and_Courses/repos/jakevdp__PythonDataScienceHandbook`
  *Note:* The GMM page URL was not fetched separately. Because of the ND clause, mirror the code but link to the prose rather than adapting it.

## Customer lifetime value

- [core] **[PyMC-Marketing CLV Quickstart (BG/NBD + Gamma-Gamma) and CLV model notebooks](https://www.pymc-marketing.io/en/stable/notebooks/clv/clv_quickstart.html)** (2026) — PyMC Labs and PyMC-Marketing contributors. *PyMC-Marketing documentation*
  `notebook` · `intermediate` · `access: open` · `Apache-2.0`
  Uses CDNOW to build an RFM summary with clv.utils.rfm_summary and a train/test split, fits BG/NBD by MAP and MCMC, and computes P(alive) and expected purchases. It then checks the Gamma-Gamma independence assumption, fits Gamma-Gamma and computes discounted CLV with uncertainty intervals.
  *Use in wiki:* Main CLV lab notebook. Sibling notebooks cover Pareto/NBD, MBG/NBD, standalone Gamma-Gamma and sBG with cohorts and covariates for subscription settings.
  Tools: pymc-marketing, pymc, arviz · Local copy: `04_M4_Conjoint_Segmentation_CLV/repos/pymc-labs__pymc-marketing`
  *Note:* BG/NBD: https://www.pymc-marketing.io/en/stable/notebooks/clv/bg_nbd.html. Pareto/NBD: https://www.pymc-marketing.io/en/stable/notebooks/clv/pareto_nbd.html. Gamma-Gamma: https://www.pymc-marketing.io/en/stable/notebooks/clv/gamma_gamma.html. sBG: https://www.pymc-marketing.io/en/stable/notebooks/clv/sbg.html. The quickstart doesn't mention migrating from lifetimes. The rfm_summary definitions of frequency and recency differ from standard RFM scoring, which is worth flagging to students.

- [core] **[Modeling Customer Lifetime Value](https://journals.sagepub.com/doi/10.1177/1094670506293810)** (2006) — Gupta, S.; Hanssens, D.; Hardie, B.; Kahn, W.; Kumar, V.; Lin, N.; Ravishanker, N.; Sriram, S. *Journal of Service Research 9(2), 139-155*
  `paper` · `intermediate` · `access: library`
  Widely cited review of CLV and customer-equity models (RFM, probability, econometric, persistence and computer-science approaches) and their use in segmentation and in allocating spend across acquisition, retention and cross-selling.
  *Use in wiki:* Assigned overview reading that places BTYD models among other CLV approaches.
  DOI [10.1177/1094670506293810](https://doi.org/10.1177/1094670506293810)

- [core] **['Counting Your Customers' the Easy Way: An Alternative to the Pareto/NBD Model](https://www.brucehardie.com/papers/018/)** (2005) — Fader, P. S.; Hardie, B. G. S.; Lee, K. L. *Marketing Science 24(2)*
  `paper` · `advanced` · `access: open`
  Introduces the BG/NBD buy-till-you-die model, a far easier-to-estimate alternative to the Pareto/NBD for non-contractual repeat purchasing, illustrated on CDNOW.
  *Use in wiki:* Primary academic anchor for the BG/NBD model used in the PyMC-Marketing lab.
  DOI [10.1287/mksc.1040.0098](https://doi.org/10.1287/mksc.1040.0098) · [Open-access copy](https://www.brucehardie.com/papers/018/fader_et_al_mksc_05.pdf)
  *Note:* The original Pareto/NBD paper (Schmittlein, Morrison & Colombo, 1987, Management Science) was not verified here.

- [core] **[Bruce Hardie's technical notes on BG/NBD, Pareto/NBD, sBG and Gamma-Gamma models (with Excel implementations)](https://www.brucehardie.com/notes/)** — Fader, P. S.; Hardie, B. G. S. *brucehardie.com*
  `website` · `intermediate` · `access: open`
  Free notes and spreadsheets, including 004 (BG/NBD in Excel), 021 (P(alive)), 039 (step-by-step BG/NBD derivation), 025 (Gamma-Gamma model of monetary value, PDF and calibration xlsx), 008/009 (Pareto/NBD) and 017 (sBG with multiple cohorts).
  *Use in wiki:* Use the Excel implementations to show the likelihood before switching to Python. The Gamma-Gamma note (https://www.brucehardie.com/notes/025/) is the spend-model reading.
  Tools: Excel
  *Note:* Tutorial handout 'Probability Models for Customer-Base Analysis' (2016): https://www.brucehardie.com/talks/cba_tut_art_16_HO.pdf (all versions at https://www.brucehardie.com/talks.html). CDNOW data: https://www.brucehardie.com/notes/026/ covers 23,570 customers from the Q1 1997 cohort, with the full zip at https://www.brucehardie.com/datasets/CDNOW_master.zip (424 KB) and a one-tenth sample. No license is stated, so link rather than mirror.

- [recommended] **[Customer Centricity: Focus on the Right Customers for Strategic Advantage](https://www.pennpress.org/9781613631027/customer-centricity/)** (2020) — Fader, P. S. *Wharton School Press (Wharton Executive Essentials), paperback 2nd ed.*
  `book` · `intro` · `access: paid`
  Short managerial book (about 150 pages) arguing that firms should identify and focus on their most valuable customers using CLV, with examples such as Starbucks and Nordstrom. The 2020 edition adds a new preface and afterword.
  *Use in wiki:* Managerial framing for the CLV module, and a source of discussion prompts for blog-post write-ups.
  *Note:* The original edition dates from 2012 (from recollection). The Wharton School Press URL redirects to Penn Press.

- [recommended] **[Customer-Based Corporate Valuation for Publicly Traded Non-Contractual Firms](https://journals.sagepub.com/doi/abs/10.1177/0022243718802843)** (2018) — McCarthy, D. M.; Fader, P. S. *Journal of Marketing Research 55(5), 617-635*
  `paper` · `advanced` · `access: open`
  Values non-contractual public firms by building acquisition, repeat-purchase and spend models from disclosed customer data, then summing customer lifetime values into firm value.
  *Use in wiki:* Case-style extension of CLV to firm valuation. The student-friendly version is McCarthy & Fader's HBR piece.
  DOI [10.1177/0022243718802843](https://doi.org/10.1177/0022243718802843) · [Open-access copy](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3040422)
  *Note:* Student reading: McCarthy & Fader (2020), 'How to Value a Company by Analyzing Its Customers', HBR 98(1), 51-55 (https://hbr.org/2020/01/are-you-undervaluing-your-customers). Subscription-firm version: McCarthy, Fader & Hardie (2017), JM 81(1), 17-35 (https://journals.sagepub.com/doi/abs/10.1509/jm.15.0519; SSRN https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2701093). Links taken from McCarthy's research page; the task brief's 'non-subscription' wording corresponds to this 'non-contractual' paper.

- [optional] **[lifetimes (archived June 2024): the original Python BTYD package, superseded by PyMC-Marketing](https://github.com/CamDavidsonPilon/lifetimes)** (2024) — Davidson-Pilon, C. and contributors. *GitHub*
  `package` · `intermediate` · `access: open` · `MIT`
  The once-standard Python BG/NBD, Pareto/NBD and Gamma-Gamma library. It was archived read-only on 2024-06-28, and its README names PyMC-Marketing as the successor.
  *Use in wiki:* Warning box for the CLV lab. LLM coding assistants trained on older code may still reach for lifetimes or btyd, so require PyMC-Marketing and show the equivalent calls.
  Tools: lifetimes, pymc-marketing
  *Note:* btyd (https://github.com/ColtAllen/btyd, Apache-2.0) is also archived (2024-07-21) and says development moved to pymc-marketing. The claim that AI assistants suggest lifetimes is the instructor's teaching point, not a documented finding.

- [optional] **[CLVTools: probabilistic customer attrition and CLV models in R](https://www.clvtools.com/)** — Bachmann, P.; Kuebler, N.; Meierer, M.; Naef, J.; Oblander, E. S.; Schilter, P. *CRAN / clvtools.com (v0.12.1)*
  `package` · `intermediate` · `access: open` · `GPL-3`
  R implementation of Pareto/NBD (including time-invariant and time-varying covariates), BG/NBD, GGom/NBD and Gamma-Gamma spending models for non-contractual CLV.
  *Use in wiki:* R option for teams that prefer R. It is also the reference implementation for covariate-extended Pareto/NBD.
  Tools: R, CLVTools

## AI-assisted coding angle for this module

Resources in this folder that show the method done with AI help, LLM versions of the method, or documented failure modes of AI-written analysis:

- [AI-Human Hybrids for Marketing Research: Leveraging Large Language Models (LLMs) as Collaborators](https://journals.sagepub.com/doi/10.1177/00222429241276529)
- [Digital Twins as Funhouse Mirrors: Five Key Distortions](https://arxiv.org/abs/2509.19088)
- [Frontiers: Can Large Language Models Capture Human Preferences?](https://arxiv.org/abs/2305.02531)
- [The Challenge of Using LLMs to Simulate Human Behavior: A Causal Inference Perspective](https://arxiv.org/abs/2312.15524)
- [Using LLMs for Market Research](https://papers.ssrn.com/abstract=4395751)
- [Synthetic Replacements for Human Survey Data? The Perils of Large Language Models](https://www.cambridge.org/core/journals/political-analysis/article/synthetic-replacements-for-human-survey-data-the-perils-of-large-language-models/B92267DC26195C7F36E63EA04A47D2FE)
- [Twin-2K-500: A dataset for building digital twins of over 2,000 people based on their answers to over 500 questions](https://huggingface.co/datasets/LLM-Digital-Twin/Twin-2K-500)

## Also relevant (catalogued in other folders)

- **`01_M1_Marketing_Analytics_and_Python`**: [Applying Data Analytics in Marketing](https://www.coursera.org/learn/applying-data-analytics-business-in-marketing); [Principles of Marketing Engineering and Analytics (3rd ed.)](https://faculty.essec.edu/research/3268-principles-of-marketing-engineering-and-analytics-3rd-edition); [Cutting-Edge Marketing Analytics: Real World Cases and Data Sets for Hands On Learning](https://www.oreilly.com/library/view/-/9780133552584/)
- **`02_M2_Customer_Data_and_Visualization`**: [RFM and CLV: Using Iso-Value Curves for Customer Base Analysis](http://www.brucehardie.com/papers/rfm_clv_2005-02-16.pdf)
- **`05_M5_Text_and_Social_Media_Analytics`**: [Frontiers: Determining the Validity of Large Language Models for Automated Perceptual Analysis](https://doi.org/10.1287/mksc.2023.0454); [Sentence Transformers (SBERT) documentation](https://sbert.net/); [Mine Your Own Business: Market-Structure Surveillance Through Text Mining](https://doi.org/10.1287/mksc.1120.0713)
- **`06_M6_Causal_Inference_and_Experiments`**: [PyMC-Marketing: Bayesian MMM, CLV and choice models in Python](https://www.pymc-marketing.io/en/stable/); [Retention Futility: Targeting High-Risk Customers Might Be Ineffective](https://journals.sagepub.com/doi/10.1509/jmr.16.0163); [MineThatData E-Mail Analytics and Data Mining Challenge (Hillstrom dataset)](https://blog.minethatdata.com/2008/03/minethatdata-e-mail-analytics-and-data.html)
- **`07_M7_Predictive_Models_ML_and_AI`**: [ISLP_labs: Python lab notebooks for ISLP](https://github.com/intro-stat-learning/ISLP_labs); [In Pursuit of Enhanced Customer Retention Management: Review, Key Issues, and Future Directions](https://ideas.repec.org/a/spr/custns/v5y2018i1d10.1007_s40547-017-0080-0.html)
- **`20_Datasets`**: [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce); [R for Marketing Research and Analytics: companion data, code and slides](https://r-marketing.r-forge.r-project.org/); [Online Retail II](https://archive.ics.uci.edu/dataset/502/online+retail+ii); [CDNOW and other BTYD datasets (Bruce Hardie)](https://www.brucehardie.com/datasets/); [dunnhumby Source Files: The Complete Journey, Breakfast at the Frat, Carbo-Loading, Let's Get Sort-of-Real](https://www.dunnhumby.com/source-files/); [PyMC-Marketing example data: synthetic MMM and CDNOW CLV](https://www.pymc-marketing.io/en/stable/notebooks/mmm/mmm_example.html); [Telco Customer Churn (IBM sample data)](https://github.com/IBM/telco-customer-churn-on-icp4d); [Yelp Open Dataset](https://business.yelp.com/data/resources/open-dataset/); [The Instacart Online Grocery Shopping Dataset 2017](https://tech.instacart.com/3-million-instacart-orders-open-sourced-d40d29ead6f2); [statsmodels example datasets and Rdatasets (get_rdataset)](https://www.statsmodels.org/stable/datasets/index.html); [Train and ModeCanada choice datasets (R package mlogit)](https://cran.csiro.au/web/packages/mlogit/vignettes/c2.formula.data.html); [bayesm package datasets (Rossi)](https://www.chicagobooth.edu/research/kilts/research-data/bayesm)
- **`21_Open_Textbooks_and_Courses`**: [An Introduction to Statistical Learning with Applications in Python (ISLP)](https://www.statlearning.com/); [Python for Marketing Research and Analytics](https://python-marketing-research.github.io/); [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/); [Data 100 Course Notes: Principles and Techniques of Data Science](https://ds100.org/course-notes/); [Customer Analytics (Wharton, Coursera)](https://www.coursera.org/learn/wharton-customer-analytics); [Darden Business Publishing (cases, simulations, course packs)](https://store.darden.virginia.edu/); [Hands-On Data Science for Marketing (code repository)](https://github.com/PacktPublishing/Hands-On-Data-Science-for-Marketing); [pyrsm and Radiant: business-analytics teaching tools from UCSD Rady](https://pypi.org/project/pyrsm/)
- **`22_Wiki_Design_and_Hosting`**: [marimo WebAssembly notebooks](https://docs.marimo.io/guides/wasm/); [Packages built in Pyodide](https://pyodide.org/en/stable/usage/packages-in-pyodide.html)
