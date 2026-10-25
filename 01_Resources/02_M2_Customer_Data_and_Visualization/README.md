# M2 · Customer Data and Visualization

57 resources (13 core). Built 2026-10-25 from `00_Index/_data/`; edit the YAML there and rerun `00_Index/_build/build_catalog.py` rather than editing this file.

Priority: **core** = likely to assign or build on; **recommended** = strong supplement; **optional** = background or niche. *Access* tells you whether students can open it without a login.

## Contents

- [Customer data](#customer-data) (5)
- [Collecting data from APIs](#collecting-data-from-apis) (4)
- [Privacy and customer data](#privacy-and-customer-data) (4)
- [Visualization principles](#visualization-principles) (5)
- [Visualization in Python](#visualization-in-python) (5)
- [Communicating results: Pyramid Principle, SCQA, storytelling](#communicating-results-pyramid-principle-scqa-storytelling) (8)
- [AI-generated charts and analysis](#ai-generated-charts-and-analysis) (6)
- [Data visualization: practitioners, guides and code](#data-visualization-practitioners-guides-and-code) (17)
- [Python for marketing analytics: notebooks and code](#python-for-marketing-analytics-notebooks-and-code) (3)

## Customer data

- [core] **[Browsing the Aisles or Browsing the App? How Online Grocery Shopping is Changing What We Buy](https://pubsonline.informs.org/doi/10.1287/mksc.2022.0292)** (2024) — Chintala, S. C.; Liaukonytė, J.; Yang, N. *Marketing Science*
  `paper` · `advanced` · `access: library`
  Household panel evidence on how the same shoppers' baskets differ when they buy groceries online versus in store: fewer impulse and unhealthy items and more repetition online, with implications for new-product introduction.
  *Use in wiki:* Instructor's own paper; a natural M2/M6 case. Pairs with the synthetic Instacart vs. in-person grocery data used in MBA 542 Module 1.
  DOI [10.1287/mksc.2022.0292](https://doi.org/10.1287/mksc.2022.0292)
  *Note:* Also on the MBA 542 Module 1 reading list. The summary is high-level; check the wording against the published abstract before quoting it on the wiki.

- [core] **[RFM and CLV: Using Iso-Value Curves for Customer Base Analysis](http://www.brucehardie.com/papers/rfm_clv_2005-02-16.pdf)** (2005) — Fader, P.S.; Hardie, B.G.S.; Lee, K.L. *Journal of Marketing Research (2005)*
  `paper` · `advanced` · `access: open`
  Links RFM summaries to a probability model (Pareto/NBD plus gamma-gamma) so that recency, frequency and monetary value map into CLV through 'iso-value' curves.
  *Use in wiki:* Academic anchor that turns M2's descriptive RFM into M4's CLV; instructor background plus a figure to show in class.
  [Open-access copy](http://www.brucehardie.com/papers/rfm_clv_2005-02-16.pdf)
  *Note:* The fetched PDF is the authors' February 2005 working-paper version and does not name the journal. Publication in JMR 42(4), 2005, is from instructor knowledge and was not verified here; no DOI seen.

- [recommended] **[Google Analytics demo account](https://support.google.com/analytics/answer/6367342)** (2026) — Google. *Analytics Help*
  `documentation` · `intro` · `access: free-registration`
  Free, viewer-level access to live GA4 properties (Google Merchandise Store web data and the Flood-It! app) so students can explore standard reports and explorations.
  *Use in wiki:* In-class walkthrough of acquisition, engagement and monetization reports before moving to raw data in Python.
  Tools: Google Analytics 4
  *Note:* Limits: obfuscated data, no export, no Data API access.

- [recommended] **[What is a CDP? (CDP Institute definition)](https://www.cdpinstitute.org/learning-center/what-is-a-cdp/)** (2026) — CDP Institute (Raab, D.). *CDP Institute Learning Center*
  `website` · `intro` · `access: open`
  Industry definition of a CDP as 'software that creates and maintains a persistent, unified customer record that is accessible to other systems', with own-store, warehouse-native (composable) and hybrid deployments.
  *Use in wiki:* Short reading for the 'where first-party data lives' lecture; connects identity resolution to the student datasets.
  *Note:* Vendor-neutral industry body, but not academic. Definition labeled as the 2026 version.

- [optional] **[[GA4] Cohort exploration](https://support.google.com/analytics/answer/9670133)** (2026) — Google. *Analytics Help*
  `documentation` · `intro` · `access: open`
  Defines cohort settings in GA4: inclusion criteria, return criteria, granularity, and standard, rolling or cumulative calculation.
  *Use in wiki:* Concept page for cohort retention; students then build the same table from Online Retail II in pandas.
  Tools: Google Analytics 4
  *Note:* No verified Python cohort-analysis tutorial was found before the search budget ran out (gap).

## Collecting data from APIs

- [core] **[Lab: collecting public data from an API (McBroken, McDonald's ice-cream machines)](https://github.com/nene88991999/BADM534-Marketing-Analytics/tree/main/01_Resources/02_M2_Customer_Data_and_Visualization/mcbroken_api_lab)** (2026) — Yang, N. (BADM 534 course materials)
  `notebook` · `intro` · `access: open` · `Course material; derived data, see README` · `AI angle`
  Executed notebook plus two scripts. fetch_mcbroken.py calls https://mcbroken.com/markers.json (one GeoJSON feature per store, gzip, undocumented), checks status, decompresses, flattens to a DataFrame and saves a timestamped copy, with a fallback to a public-domain GitHub archive. build_panel.py walks that archive's 60,000-commit git history and writes daily (one year) and weekly (six years) panels by country, US state and store. Includes a GitHub Actions template for students to build their own daily snapshots.
  *Use in wiki:* M2 session on data collection: HTTP requests, headers, status codes, JSON to table, polite scraping, and git scraping as a cheap way to build a time series. Exercise 1 has students audit AI-written request code (timeout, User-Agent, status check, gzip, raw copy). Exercise 5 previews M6 with a right-to-repair event study (US Copyright Office exemption, late Oct 2024).
  Tools: requests, pandas, matplotlib, git, GitHub Actions · Local copy: `02_M2_Customer_Data_and_Visualization/mcbroken_api_lab`
  *Note:* Measurement caveats are in the README: is_broken means the McDonald's app refused an ice-cream order (also fires when a store is closed); the denominator is stores checked in that hour and the checking cadence changed over the years. Raw JSON is not redistributed; derived aggregates and one snapshot are.

- [core] **[mcbroken-archive: hourly git-scraped snapshots of McBroken since October 2020](https://github.com/MrFlynn/mcbroken-archive)** (2020) — MrFlynn (GitHub). *GitHub*
  `dataset` · `intro` · `access: open` · `Unlicense`
  A GitHub Actions job downloads markers.json several times a day (hourly cron, in practice 4 to 40 commits a day over the years), keeps the stores checked in the previous hour, and commits the file; 60,000+ commits from 2020-10-24 onward. Includes a git-history transform script for loading everything into SQLite.
  *Use in wiki:* Source of the lab's time series via build_panel.py. Also the clearest small example of git scraping to show students.
  Tools: git, GitHub Actions, jq, git-history
  *Note:* Each commit holds only recently checked stores, so coverage per snapshot varies (15,000 to 25,000 of about 30,000). The Unlicense covers the repository, not McDonald's underlying facts.

- [recommended] **[Git scraping: track changes over time by scraping to a Git repository](https://simonwillison.net/2020/Oct/9/git-scraping/)** (2020) — Willison, S
  `blog` · `intro` · `access: open`
  The post that named the pattern: a scheduled GitHub Actions workflow fetches a public file and commits it, so the git history becomes a time series at zero hosting cost. Links to worked examples and to the git-history tool for turning the history into a database.
  *Use in wiki:* Ten-minute read before the lab's time-series section; the snapshot_mcbroken.yml template follows it.

- [recommended] **[McBroken: real-time tracker of McDonald's ice-cream machines](https://mcbroken.com/)** (2020) — Zahid, R
  `website` · `intro` · `access: open` · `none stated`
  Hobby site (October 2020) that checks each McDonald's every few minutes by trying to add an ice-cream item to a cart through McDonald's ordering API; the map is drawn from https://mcbroken.com/markers.json and the city table from https://mcbroken.com/stats.json. Covers 30,000+ stores in 50+ countries.
  *Use in wiki:* The worked example for M2 data collection. Students open stats.json in a browser first, then call it from Python.
  *Note:* No documented API, no terms of use and no licence: treat as publicly viewable, not openly licensed. Blocked on some campus and corporate networks; the lab falls back to the GitHub archive.

## Privacy and customer data

- [recommended] **[The Economics of Privacy](https://www.aeaweb.org/articles?id=10.1257/jel.54.2.442)** (2016) — Acquisti, A.; Taylor, C.; Wagman, L. *Journal of Economic Literature 54(2), 442-492*
  `paper` · `advanced` · `access: library`
  Survey of theory and evidence on the value of protecting versus disclosing personal data. It concludes there is no unified theory, that privacy protection can raise or lower welfare, and that consumers often cannot see how their data is used.
  *Use in wiki:* Instructor background and an optional reading that frames privacy as a trade-off rather than a compliance checklist.
  DOI [10.1257/jel.54.2.442](https://doi.org/10.1257/jel.54.2.442)

- [optional] **[California Consumer Privacy Act (CCPA)](https://oag.ca.gov/privacy/ccpa)** (2026) — State of California Department of Justice, Office of the Attorney General. *oag.ca.gov*
  `website` · `intro` · `access: open`
  Official summary of CCPA/CPRA consumer rights (know, delete, opt out including Global Privacy Control, correct, limit sensitive data) and business obligations.
  *Use in wiki:* Reference box on the privacy page; ties opt-out signals to why first-party datasets have gaps.
  *Note:* Last updated Aug 28, 2026 at time of fetch.

- [optional] **[General Data Protection Regulation (GDPR), structured text](https://gdpr-info.eu/)** (2016) — intersoft consulting (unofficial consolidation of Regulation (EU) 2016/679). *gdpr-info.eu*
  `website` · `intro` · `access: open`
  Searchable article-by-article GDPR text with linked recitals, covering lawful basis (Art. 6), consent (Art. 7), and data-subject rights including erasure, portability and profiling (Arts. 15-22).
  *Use in wiki:* Quick lookup when discussing international students' home-market rules and consent-based data collection.
  *Note:* Unofficial; the site links to the authoritative EUR-Lex PDF.

- [optional] **[Protecting Personal Information: A Guide for Business](https://www.ftc.gov/business-guidance/resources/protecting-personal-information-guide-business)** (2016) — U.S. Federal Trade Commission. *FTC Business Guidance*
  `report` · `intro` · `access: open`
  Five plain-language principles for handling customer data: take stock, scale down, lock it, pitch it, plan ahead.
  *Use in wiki:* Data-handling rules for the team project (minimize, de-identify, never commit raw PII to GitHub or paste it into chatbots).

## Visualization principles

- [core] **[The Python Graph Gallery](https://python-graph-gallery.com/)** (2026) — Holtz, Y. *python-graph-gallery.com*
  `website` · `intro` · `access: open` · `0BSD (site repo)`
  Hundreds of reproducible matplotlib, seaborn, plotly and plotnine examples grouped by chart purpose (distribution, correlation, ranking, flow), following the Data-to-Viz classification.
  *Use in wiki:* Go-to reference: students find a chart type here, then ask an AI assistant to adapt the code to their own data.
  Tools: matplotlib, seaborn, plotly, plotnine
  *Note:* Site source at https://github.com/holtzy/The-Python-Graph-Gallery (0BSD). Repo size not checked, so no download entry.

- [recommended] **[From Data to Viz](https://www.data-to-viz.com/)** (2026) — Holtz, Y.; Healy, C. *data-to-viz.com*
  `website` · `intro` · `access: open`
  Decision tree for choosing a chart from the data type, with 'common mistakes' notes per chart and a caveats gallery (pie charts, cut y-axes, overplotting, rainbow palettes), linked to Python code.
  *Use in wiki:* In-class exercise: given a marketing question and dataset, pick the chart with the tree and defend the choice.

- [recommended] **[Data Visualization: A Practical Introduction](https://socviz.co/)** (2018) — Healy, K. *Princeton University Press (draft readable online)*
  `book` · `intermediate` · `access: open`
  Practical introduction to the why and how of good graphics, from perception and honesty to workflow, with a full draft readable online.
  *Use in wiki:* Assign Chapter 1 ('Look at data') for perception and honesty principles; skip the R code.
  Tools: R, ggplot2
  *Note:* Code is R/ggplot2, not Python. The online text is a 2018-04-25 draft. The full subtitle and the free-access status are from instructor knowledge; the page shows purchase links but no license.

- [recommended] **[The Visual Display of Quantitative Information (2nd ed.)](https://www.edwardtufte.com/book/the-visual-display-of-quantitative-information/)** (2001) — Tufte, E.R. *Graphics Press*
  `book` · `intro` · `access: paid`
  Classic on graphical integrity, data-ink, chartjunk and small multiples (1st ed. 1983, 2nd ed. 2001).
  *Use in wiki:* Short excerpts on the lie factor and data-ink ratio; students critique an AI-generated chart against Tufte's rules.

- [optional] **[Communicating with Interactive Articles](https://distill.pub/2020/communicating-with-interactive-articles/)** (2020) — Hohman, F.; Conlen, M.; Heer, J.; Chau, D.H. *Distill 5(9), e28*
  `paper` · `intermediate` · `access: open` · `CC BY 4.0`
  Review of research on interactive articles (details-on-demand, prediction prompts, simulations, personalization) and the evidence on when interactivity helps or costs too much.
  *Use in wiki:* Design reference for the interactive HTML wiki, and inspiration for ambitious team blog posts.
  DOI [10.23915/distill.00028](https://doi.org/10.23915/distill.00028)

## Visualization in Python

- [core] **[Matplotlib Quick start guide (and official cheatsheets)](https://matplotlib.org/stable/users/explain/quick_start.html)** (2026) — Matplotlib development team. *matplotlib.org (v3.11)*
  `documentation` · `intro` · `access: open` · `AI angle`
  Official intro to Figure, Axes and Artists, and to the explicit (object-oriented) versus implicit (pyplot) interfaces, plus styling, labels, scales, dates and colormaps.
  *Use in wiki:* Teach the fig, ax = plt.subplots() pattern so students can read and fix AI-generated plotting code, which often mixes the two interfaces.
  Tools: matplotlib
  *Note:* Cheatsheet PDFs: https://matplotlib.org/cheatsheets/cheatsheets.pdf and https://matplotlib.org/cheatsheets/handout-beginner.pdf

- [core] **[seaborn user guide and tutorial](https://seaborn.pydata.org/tutorial.html)** (2024) — Waskom, M. et al. *seaborn.pydata.org (v0.13.2)*
  `documentation` · `intro` · `access: open`
  Tutorial on statistical graphics: relational, distribution and categorical plots, error bars, regression fits, multi-plot grids, palettes, and the seaborn.objects interface.
  *Use in wiki:* Default library for M2 exploratory charts of customer segments; the error-bar chapter supports M3.
  Tools: seaborn, matplotlib, pandas

- [recommended] **[Plotly Express in Python](https://plotly.com/python/plotly-express/)** (2026) — Plotly. *plotly.com*
  `documentation` · `intro` · `access: open`
  High-level px API that builds interactive figures in one call; the figures export to HTML and can be embedded in web pages and Dash apps.
  *Use in wiki:* Use for interactive charts in student blog posts and in the GitHub Pages wiki.
  Tools: plotly
  *Note:* The page also promotes Plotly Studio (AI app builder), a commercial product.

- [optional] **[Vega-Altair: Declarative Visualization in Python](https://altair-viz.github.io/)** (2026) — Vega-Altair developers. *altair-viz.github.io (v6)*
  `documentation` · `intermediate` · `access: open`
  Grammar-of-graphics library built on Vega-Lite; charts are specified as data, encodings and marks and render as interactive web graphics.
  *Use in wiki:* Alternative for interactive, web-native charts on the wiki; its declarative specs are easy for LLMs to generate and for students to read.
  Tools: altair
  *Note:* Gallery: https://altair-viz.github.io/gallery/index.html

- [optional] **[Visualization Curriculum (interactive Altair notebooks)](https://idl.uw.edu/visualization-curriculum/)** (2020) — UW Interactive Data Lab (Heer, J. et al.). *University of Washington IDL*
  `notebook` · `intro` · `access: open` · `BSD-3-Clause`
  Seven Colab-ready notebooks teaching visualization principles through Altair: marks and encodings, transforms, scales and legends, multi-view composition, interaction, maps, plus a debugging guide.
  *Use in wiki:* Embed one notebook (marks and encoding) as an in-class activity on encoding choices.
  Tools: altair, Colab · Local copy: `02_M2_Customer_Data_and_Visualization/repos/uwdata__visualization-curriculum`
  *Note:* Year approximate; not confirmed on the page.

## Communicating results: Pyramid Principle, SCQA, storytelling

- [core] **[storytelling with data: a data visualization guide for business professionals](https://www.storytellingwithdata.com/books)** (2015) — Knaflic, C.N. *Wiley*
  `book` · `intro` · `access: paid`
  Business-oriented guide to context, choosing visuals, removing clutter, focusing attention and telling a story. The companion site adds free makeovers, a chart guide, a podcast and sample chapters.
  *Use in wiki:* Core M2 reading for the blog-post deliverable; use SWD 'makeovers' as before-and-after critique exercises.
  *Note:* Year and publisher (2015, Wiley) are from instructor knowledge; the books page links to Wiley but shows no dates. Free chart guide: https://www.storytellingwithdata.com/chart-guide . Workbook 'let's practice!' has exercise solutions on the site.

- [core] **[The Minto Pyramid Principle: Logic in Writing, Thinking and Problem Solving](https://www.barbaraminto.com/)** (1996) — Minto, B. *Minto International (barbaraminto.com)*
  `book` · `intro` · `access: paid`
  The source text on top-down, answer-first business writing: a governing thought supported by MECE groups of ideas, opened with the Situation-Complication-Question framework.
  *Use in wiki:* Core reading for M2's communication unit and the template for every project blog post and in-class readout.
  *Note:* The 1996 revised edition is the authoritative one (originally 1987; the Pearson reissue is not the revised text, per Minto). Her site calls the intro the 'SCQ Framework'; SCQA adds the Answer. The official online course costs $1,200. No free official summary.

- [recommended] **[Creating a Blog (Quarto) and Publishing to GitHub Pages](https://quarto.org/docs/websites/website-blog.html)** (2026) — Posit / Quarto. *quarto.org*
  `documentation` · `intro` · `access: open`
  How to create a Quarto blog (quarto create project blog) whose posts can be Jupyter notebooks or .qmd files with frozen outputs, and how to publish it to GitHub Pages.
  *Use in wiki:* Recommended toolchain for team blog posts, and a candidate engine for the course wiki itself.
  Tools: Quarto, Jupyter, GitHub Pages
  *Note:* GitHub Pages guide (verified): https://quarto.org/docs/publishing/github-pages.html . Three options: render to docs/, 'quarto publish gh-pages', or a GitHub Action; use freeze: auto to avoid re-running notebooks in CI.

- [recommended] **[Minto Pyramid (Untools)](https://untools.co/minto-pyramid/)** (2026) — Untools. *untools.co*
  `website` · `intro` · `access: open`
  One-page summary with an example: start with the conclusion (BLUF), give key supporting points, then supporting data.
  *Use in wiki:* Embed as the quick-reference card; students run their draft blog post through its three steps.
  *Note:* Does not cover SCQA. All rights reserved, so link rather than copy.

- [recommended] **[Advice to aspiring data scientists: start a blog](http://varianceexplained.org/r/start-blog/)** (2017) — Robinson, D. *Variance Explained*
  `blog` · `intro` · `access: open`
  Widely shared essay on why public analysis blog posts build skills, a portfolio and feedback, and why not to wait for an audience.
  *Use in wiki:* Motivation reading when introducing the blog-post-plus-GitHub project format.
  *Note:* The fetch confirmed the author and content; the title and 2017 date are from memory, not shown in the fetched text.

- [optional] **[Barbara Minto: 'MECE: I invented it, so I get to say how to pronounce it'](https://www.mckinsey.com/alumni/news-and-events/global-news/alumni-news/barbara-minto-mece-i-invented-it-so-i-get-to-say-how-to-pronounce-it)** (2026) — McKinsey Alumni Center. *McKinsey & Company Alumni News*
  `blog` · `intro` · `access: open`
  Free interview in which Minto explains the pyramid (summary point over logically grouped ideas), the origin of MECE, and why thinking comes before slides.
  *Use in wiki:* Free, authoritative 10-minute primer to assign in place of the book.
  *Note:* Publication date not shown on the page; the year field is the fetch year, not the publication year.

- [optional] **[Minto Pyramid & SCQA (ModelThinkers)](https://modelthinkers.com/mental-model/minto-pyramid-scqa)** (2026) — ModelThinkers. *modelthinkers.com*
  `website` · `intro` · `access: freemium`
  Summary of SCQA (situation, complication, question, answer) as the pyramid's introduction, with action-statement recommendations and MECE support; notes the limits of answer-first framing.
  *Use in wiki:* Short SCQA explainer; the free preview covers the key structure.
  *Note:* Partly paywalled (members-only sections, US$5/month). No fully open SCQA summary was verified (gap).

- [optional] **[The Cognitive Style of PowerPoint: Pitching Out Corrupts Within](https://www.edwardtufte.com/book/the-cognitive-style-of-powerpoint-pitching-out-corrupts-within-ebook/)** (2006) — Tufte, E.R. *Graphics Press (32-page eBook)*
  `book` · `intro` · `access: paid`
  Essay ($5 PDF) arguing that bullet-outline slideware weakens reasoning and distorts statistical analysis.
  *Use in wiki:* Counterpoint reading in the communication unit, and a reason the course uses a blog post instead of a deck.
  *Note:* Year from memory (2nd ed. 2006); the page does not show it. For examples of consulting-style action titles, Analyst Academy keeps a free list of 600+ public consulting decks: https://www.theanalystacademy.com/consulting-presentations/ (verified; the site promotes paid courses).

## AI-generated charts and analysis

- [core] **[LIDA: A Tool for Automatic Generation of Grammar-Agnostic Visualizations and Infographics using Large Language Models](https://aclanthology.org/2023.acl-demo.11)** (2023) — Dibia, V. *ACL 2023 System Demonstrations, pp. 113-126*
  `paper` · `intermediate` · `access: open` · `MIT (code)` · `AI angle`
  Microsoft Research system that treats visualization as code generation in four stages: a Summarizer that describes the data, a Goal Explorer that proposes questions, a VisGenerator that writes, repairs and filters matplotlib, seaborn or Altair code, and an Infographer.
  *Use in wiki:* Explains what Gemini, ChatGPT and Claude do under the hood when they 'make a chart'; run the tutorial notebook in Colab as a demo.
  DOI [10.18653/v1/2023.acl-demo.11](https://doi.org/10.18653/v1/2023.acl-demo.11) · [Open-access copy](https://arxiv.org/abs/2303.02927) · Tools: lida, matplotlib, seaborn, altair · Local copy: `02_M2_Customer_Data_and_Visualization/repos/microsoft__lida`
  *Note:* The README warns that LIDA executes generated code, so run it in a sandbox. Maintenance activity unclear. Supports OpenAI, Azure, PaLM, Cohere, Hugging Face and local models via llmx. No error-rate figures were confirmed on the fetched abstract pages.

- [recommended] **[Data Formulator: AI-powered data exploration with visualizations](https://github.com/microsoft/data-formulator)** (2026) — Microsoft Research. *GitHub (microsoft/data-formulator)*
  `tool` · `intro` · `access: open` · `MIT` · `AI angle`
  Open-source app that mixes drag-and-drop encoding with natural-language prompts, so AI agents transform data and build charts while users branch into alternative analyses. Works with OpenAI, Azure, Anthropic or Ollama models.
  *Use in wiki:* Hands-on lab: students explore a customer dataset in Data Formulator, then rebuild the best chart in their own notebook code.
  Tools: data_formulator, uv
  *Note:* Install with 'uvx data_formulator' or pip; runs locally at localhost:5567. Latest stable 0.7 (May 2026), 0.8 beta (Aug 2026). Needs an LLM API key.

- [recommended] **[DABStep: Data Agent Benchmark for Multi-step Reasoning](https://huggingface.co/blog/dabstep)** (2025) — Adyen; Hugging Face. *Hugging Face blog*
  `blog` · `intermediate` · `access: open` · `AI angle`
  Benchmark of over 450 real-world data-analysis tasks that combine tables with documentation. At launch (Feb 2025) the best agent scored only 16% on hard tasks (o3-mini; Claude Sonnet 12%).
  *Use in wiki:* A sobering number for students: AI agents handle easy descriptive analysis but often fail multi-step business questions, so verify.
  *Note:* Leaderboard: https://huggingface.co/spaces/adyen/DABstep (scores have since risen; check the current state before citing). Google's Colab agent claimed 4th place in March 2025. Earlier, more optimistic baseline: Cheng, Li and Bing (2023), 'Is GPT-4 a Good Data Analyst?', https://arxiv.org/abs/2305.15038 (verified).

- [recommended] **[SWD + AI: data storytelling with AI](https://www.storytellingwithdata.com/ai-data-storytelling)** (2025) — storytelling with data (Knaflic, C.N. et al.). *storytellingwithdata.com*
  `website` · `intro` · `access: open` · `AI angle`
  Free guide, videos and blog series on using AI as a 'thought partner' for data storytelling. It compares five AI tools on one dataset and shows that prompting with SWD principles improves AI-made graphs.
  *Use in wiki:* Lab: students get a default chart from Gemini or ChatGPT, then re-prompt it with SWD principles and compare.
  *Note:* Year approximate; one part of the blog series was marked 'coming soon' when fetched.

- [recommended] **[VisEval: A Benchmark for Data Visualization in the Era of Large Language Models](https://arxiv.org/abs/2407.00981)** (2024) — Chen, N.; Zhang, Y.; Xu, J.; Ren, K.; Yang, Y. *arXiv:2407.00981*
  `paper` · `advanced` · `access: open` · `AI angle`
  Natural-language-to-visualization benchmark (2,524 queries over 146 databases) with automated checks of validity, legality and readability; it documents recurring LLM chart-generation failures.
  *Use in wiki:* Evidence for the course rule that AI-made charts must be checked; turn its three criteria into a rubric for student chart audits.
  *Note:* The arXiv page lists no peer-reviewed venue; publication in IEEE TVCG (VIS 2024) is believed but was not verified.

- [optional] **[How Good (Or Bad) Are LLMs at Detecting Misleading Visualizations?](https://arxiv.org/abs/2407.17291)** (2024) — Lo, L.Y.-H.; Qu, H. *arXiv:2407.17291*
  `paper` · `intermediate` · `access: open` · `AI angle`
  Tests four multimodal LLMs with nine prompting strategies on misleading real-world charts (up to 21 issue types). Detection is promising but depends heavily on the prompt.
  *Use in wiki:* Exercise: students ask an AI to critique a deliberately misleading chart (truncated axis, dual axis) and compare its answer with their own.

## Data visualization: practitioners, guides and code

- [core] **[FlowingData (Nathan Yau)](https://flowingdata.com/)** (2026) — Yau, N
  `website` · `intro` · `access: freemium`
  Nathan Yau's long-running site on visualization and statistics: free posts that collect and critique notable charts, plus step-by-step tutorials (mostly R, some Python and JavaScript) and the 'Process' newsletter, which are for paying members.
  *Use in wiki:* Source of strong current examples for an M2 'chart critique' activity. Link to the posts; the members-only tutorials cannot be redistributed.
  *Note:* Tutorials are members-only (https://flowingdata.com/membership/). Nothing was downloaded.

- [core] **[seaborn user-guide tutorial notebooks](https://github.com/mwaskom/seaborn/tree/master/doc/_tutorial)** (2025) — Waskom, M
  `notebook` · `intro` · `access: open` · `BSD-3-Clause`
  The notebooks behind seaborn's official user guide: the objects interface, distributions, relational and categorical plots, regression plots, multi-plot grids, aesthetics and color palettes.
  *Use in wiki:* Core M2 lab material in the library students will use most. Adapt sections into wiki exercises rather than linking the whole guide.
  Tools: seaborn, matplotlib, pandas · Local copy: `02_M2_Customer_Data_and_Visualization/repos/mwaskom__seaborn`

- [core] **[Visual Vocabulary (Financial Times chart-doctor)](https://github.com/Financial-Times/chart-doctor/blob/main/visual-vocabulary/README.md)** (2021) — Financial Times Visual Journalism team
  `website` · `intro` · `access: open` · `MIT (repository)`
  The FT's one-page poster that organizes chart types by the relationship you want to show (deviation, correlation, ranking, distribution, change over time, part-to-whole, magnitude, spatial, flow).
  *Use in wiki:* M2 reference for choosing a display from the analytical question. Preserve attribution and the MIT license when reproducing the poster.
  Local copy: `02_M2_Customer_Data_and_Visualization/repos/Financial-Times__chart-doctor`

- [recommended] **[Matplotlib cheatsheets and handouts (source)](https://github.com/matplotlib/cheatsheets)** (2025) — Matplotlib developers; Rougier, N. P
  `tool` · `intro` · `access: open` · `BSD-2-Clause`
  Source for the official Matplotlib cheatsheets and beginner, intermediate and tips handouts.
  *Use in wiki:* Link the rendered PDFs (matplotlib.org/cheatsheets) from the wiki; the saved source lets you rebuild or adapt them.
  Tools: matplotlib · Local copy: `02_M2_Customer_Data_and_Visualization/repos/matplotlib__cheatsheets`

- [recommended] **[Datawrapper blog: guides to color in data visualization](https://www.datawrapper.de/blog/10-ways-to-use-fewer-colors-in-your-data-visualizations)** (2024) — Muth, L. C. (Datawrapper)
  `blog` · `intro` · `access: open`
  Practical, well-illustrated posts on using fewer colors, building palettes, color keys and style-guide colors.
  *Use in wiki:* Short readings for the design part of M2. Related posts: https://www.datawrapper.de/blog/create-good-color-palettes and https://www.datawrapper.de/blog/colors-for-data-vis-style-guides.

- [recommended] **[Urban Institute Data Visualization Style Guide (source)](https://github.com/UrbanInstitute/graphics-styleguide)** (2024) — Urban Institute
  `website` · `intro` · `access: open` · `Apache-2.0`
  Source for one of the best-known public data-visualization style guides: chart types, colors, typography, labels and accessibility rules for a research organization.
  *Use in wiki:* Reference for chart conventions, labels, and accessibility. Graded requirements belong in released assignment briefs. Link to the published guide.
  *Note:* Default branch is 'oct_2024'. The repository is the style guide's website source (about 157 MB, mostly images), so it is linked rather than downloaded. Jon Schwabish (PolicyViz) discusses style guides at https://policyviz.com/2016/11/30/style-guides.

- [recommended] **[Visualize This: The FlowingData Guide to Design, Visualization, and Statistics (2nd ed.)](https://book.flowingdata.com/)** (2024) — Yau, N. *Wiley*
  `book` · `intro` · `access: paid`
  Revised second edition (2024) of Yau's practical guide to turning data into charts, covering design choices, chart types for time, proportions, relationships and space, and tools from spreadsheets to R and JavaScript.
  *Use in wiki:* Instructor reference and optional student reading for M2. Check whether the UIUC library offers an e-book licence.
  *Note:* Commercial book with no open code repository found; link only.

- [recommended] **[Scientific Visualization: Python + Matplotlib (open-access book and code)](https://github.com/rougier/scientific-visualization-book)** (2021) — Rougier, N. P
  `book` · `intermediate` · `access: open` · `BSD-2-Clause (code); CC BY-NC-SA 4.0 (book), separately specified in LICENSE.txt`
  Open-access book on making publication-quality figures with Matplotlib (anatomy of a figure, colors, typography, layout, animation, common pitfalls), with the full source code for every figure.
  *Use in wiki:* Instructor resource for polishing the course's own figures, and a source of 'make this chart better' exercises. The code folder is saved locally.
  Tools: matplotlib · Local copy: `02_M2_Customer_Data_and_Visualization/repos/rougier__scientific-visualization-book`
  *Note:* The book PDF was not downloaded. LICENSE.txt separately licenses code under BSD-2-Clause and book material under CC BY-NC-SA 4.0. The original license file is retained.

- [recommended] **[storytelling-with-data: Python/Matplotlib recreations of Knaflic's figures](https://github.com/empathy87/storytelling-with-data)** (2020) — empathy87 (GitHub). *GitHub*
  `notebook` · `intro` · `access: open`
  Notebooks that rebuild figures from 'Storytelling with Data' in Matplotlib, showing the before-and-after decluttering steps in code.
  *Use in wiki:* Strong model for a 'declutter this chart with AI, then explain each change' exercise. Link only.
  Tools: matplotlib
  *Note:* The repository has no LICENSE file (all rights reserved by default), so it was not downloaded.

- [recommended] **[Altair tutorial notebooks (Exploratory Data Visualization with Altair)](https://github.com/altair-viz/altair-tutorial)** (2018) — VanderPlas, J.; Altair developers
  `notebook` · `intro` · `access: open` · `MIT`
  Short, sequenced notebooks introducing declarative visualization with Altair: simple charts, binning and aggregation, compound charts, interactivity and exploration.
  *Use in wiki:* Altair renders in the browser, so these suit interactive wiki pages. Pairs with the UW visualization curriculum already in this folder.
  Tools: altair · Local copy: `02_M2_Customer_Data_and_Visualization/repos/altair-viz__altair-tutorial`
  *Note:* The repository identifies the tutorial as PyCon 2018 and uses older selection APIs. The original course adaptation uses Altair 5.5.0; see visualization_charts.py.

- [recommended] **[From Data to Viz: a decision tree for choosing charts](https://github.com/holtzy/data_to_viz)** (2018) — Holtz, Y.; Healy, C
  `website` · `intro` · `access: open` · `MIT (repository)`
  Decision tree that leads from the type of data you have to suitable chart types, with a page per chart on caveats and common mistakes. Its sister site is the Python Graph Gallery.
  *Use in wiki:* Pair with the FT Visual Vocabulary: one organizes charts by message, the other by data type.
  *Note:* The repository is the website's source (mostly HTML and images), so it was catalogued rather than downloaded.

- [optional] **[HoloViz tutorial (hvPlot, Panel, HoloViews)](https://github.com/holoviz/holoviz/tree/main/examples/tutorial)** (2025) — HoloViz developers
  `notebook` · `intermediate` · `access: open` · `BSD-3-Clause`
  Tutorial notebooks showing how to go from pandas to interactive plots with one-line hvPlot calls and build simple dashboards with Panel.
  *Use in wiki:* Optional route to interactive dashboards for teams that want one in the final project.
  Tools: hvplot, panel, holoviews · Local copy: `02_M2_Customer_Data_and_Visualization/repos/holoviz__holoviz`
  *Note:* Some notebooks download example data on first run.

- [optional] **[PyNarrative: A Python Library for Data Storytelling](https://www.scitepress.org/PublishedPapers/2025/132599)** (2025) — SciTePress paper (2025)
  `paper` · `intermediate` · `access: open`
  Describes a Python library built on Altair for adding narrative structure (titles, annotations, story steps) to charts.
  *Use in wiki:* Optional tool for students who want annotated, story-style charts in their final blog.
  Tools: altair
  *Note:* The paper's author list was not confirmed in search results; check it before citing.

- [optional] **[Bokeh tutorial notebooks](https://github.com/bokeh/tutorial)** (2024) — Bokeh developers
  `notebook` · `intro` · `access: open` · `BSD-3-Clause`
  Official 15-notebook Bokeh tutorial on interactive web plots: basic plots, styling, layouts, interactions, data sources and widgets.
  *Use in wiki:* Option for interactive dashboards on the wiki or in final-project blogs.
  Tools: bokeh · Local copy: `02_M2_Customer_Data_and_Visualization/repos/bokeh__tutorial`

- [optional] **[VisEval: benchmark for LLM-generated visualizations (code)](https://github.com/microsoft/VisEval)** (2024) — Microsoft Research
  `tool` · `advanced` · `access: open` · `MIT` · `AI angle`
  Code and data for evaluating whether charts generated by language models are valid, legal for the data and readable, the benchmark behind the VisEval paper already in this folder.
  *Use in wiki:* Instructor background for the 'audit the AI's chart' activity; its checklist of failure types adapts well to a student rubric.
  Local copy: `02_M2_Customer_Data_and_Visualization/repos/microsoft__VisEval`

- [optional] **[Matplotlib cheat sheet (Rougier)](https://github.com/rougier/matplotlib-cheatsheet)** (2021) — Rougier, N. P
  `tool` · `intro` · `access: open` · `BSD-2-Clause`
  Compact cheat sheet covering Matplotlib's figure anatomy, styles, colormaps and annotation options, with the scripts that generate it.
  *Use in wiki:* Optional quick reference alongside the official cheatsheets.
  Tools: matplotlib · Local copy: `02_M2_Customer_Data_and_Visualization/repos/rougier__matplotlib-cheatsheet`

- [optional] **[Visualization Analysis and Design: course page and lecture slides (CPSC 547)](https://cs.ubc.ca/~tmm/courses/547-19)** (2019) — Munzner, T
  `course` · `advanced` · `access: open`
  Tamara Munzner's UBC graduate course built on her textbook 'Visualization Analysis and Design', with free slides on the what-why-how framework, marks and channels, and evaluation.
  *Use in wiki:* Instructor background for the conceptual framing of M2 (marks and channels, effectiveness rankings).

## Python for marketing analytics: notebooks and code

- [recommended] **[EcommerceTools: data science toolkit for ecommerce and marketing science](https://github.com/practical-data-science/ecommercetools)** (2024) — Clarke, M. (practical-data-science). *GitHub / PyPI*
  `package` · `intro` · `access: open` · `MIT`
  pandas-based package with an Examples notebook: builds transaction and customer tables from the Online Retail data, cohort matrices and retention, purchase latency, ABC and RFM(H) segmentation, product repurchase rates, and BG/NBD + Gamma-Gamma CLV via lifetimes. Also has SEO and reporting helpers.
  *Use in wiki:* M2 demo of one-line cohort and RFM tables. Have students rebuild ecommercetools' cohort matrix by hand in pandas (with AI help) and compare.
  Tools: pandas, lifetimes · Local copy: `02_M2_Customer_Data_and_Visualization/repos/practical-data-science__ecommercetools`
  *Note:* Last updated about Jan 2024 (topic page). The CLV functions depend on the archived lifetimes package, so swap in PyMC-Marketing for CLV. The NLP module downloads a large Hugging Face model. Repo size is estimated (API lookup failed).

- [optional] **[Data Storytelling with Altair and AI (book code)](https://github.com/alod83/Data-Storytelling-with-Altair-and-AI)** (2024) — Lo Duca, A. (alod83). *Manning*
  `notebook` · `intermediate` · `access: open` · `AI angle`
  Code for a Manning book on data storytelling with Altair and generative AI, organized by the DIKW pyramid. It includes a GitHub Copilot chapter (04/copilot) and case studies.
  *Use in wiki:* Example for the M2 page of using Copilot to build charts that still follow a storytelling structure.
  Tools: altair, github-copilot, pandas
  *Note:* No license in the repo, so link only. The author name comes from the repo owner; year from the last push (2024-10).

- [optional] **[RFM-analysis: Python script and notebook for RFM segmentation](https://github.com/joaolcorreia/RFM-analysis)** (2019) — Correia, J. L. *GitHub*
  `notebook` · `intro` · `access: open` · `Apache-2.0`
  Most-starred repo on the rfm-analysis topic (286 stars): a short notebook and CLI script that turn an orders CSV (sample-orders.csv, included) into RFM tables and segments.
  *Use in wiki:* Minimal first RFM exercise for M2. Students can extend it to the UCI Online Retail data or ask an AI assistant to vectorize and test it.
  Tools: pandas · Local copy: `02_M2_Customer_Data_and_Visualization/repos/joaolcorreia__RFM-analysis`
  *Note:* Last push 2019, so pandas idioms may be dated. Tiny repo.

## AI-assisted coding angle for this module

Resources in this folder that show the method done with AI help, LLM versions of the method, or documented failure modes of AI-written analysis:

- [Lab: collecting public data from an API (McBroken, McDonald's ice-cream machines)](https://github.com/nene88991999/BADM534-Marketing-Analytics/tree/main/01_Resources/02_M2_Customer_Data_and_Visualization/mcbroken_api_lab)
- [Matplotlib Quick start guide (and official cheatsheets)](https://matplotlib.org/stable/users/explain/quick_start.html)
- [LIDA: A Tool for Automatic Generation of Grammar-Agnostic Visualizations and Infographics using Large Language Models](https://aclanthology.org/2023.acl-demo.11)
- [Data Formulator: AI-powered data exploration with visualizations](https://github.com/microsoft/data-formulator)
- [DABStep: Data Agent Benchmark for Multi-step Reasoning](https://huggingface.co/blog/dabstep)
- [SWD + AI: data storytelling with AI](https://www.storytellingwithdata.com/ai-data-storytelling)
- [VisEval: A Benchmark for Data Visualization in the Era of Large Language Models](https://arxiv.org/abs/2407.00981)
- [Data Storytelling with Altair and AI (book code)](https://github.com/alod83/Data-Storytelling-with-Altair-and-AI)
- [How Good (Or Bad) Are LLMs at Detecting Misleading Visualizations?](https://arxiv.org/abs/2407.17291)
- [VisEval: benchmark for LLM-generated visualizations (code)](https://github.com/microsoft/VisEval)

## Also relevant (catalogued in other folders)

- **`01_M1_Marketing_Analytics_and_Python`**: [10 minutes to pandas (official quick start)](https://pandas.pydata.org/docs/user_guide/10min.html); [Plotting and Programming in Python (Software Carpentry)](https://swcarpentry.github.io/python-novice-gapminder); [pandas_exercises](https://github.com/guipsamora/pandas_exercises); [Marketing Analytics Jumpstart (Google Cloud)](https://github.com/GoogleCloudPlatform/marketing-analytics-jumpstart); [Python for Excel, 2nd edition (companion repo)](https://github.com/fzumstein/python-for-excel)
- **`04_M4_Conjoint_Segmentation_CLV`**: [PyMC-Marketing CLV Quickstart (BG/NBD + Gamma-Gamma) and CLV model notebooks](https://www.pymc-marketing.io/en/stable/notebooks/clv/clv_quickstart.html)
- **`06_M6_Causal_Inference_and_Experiments`**: [Mobile App Introduction and Online and Offline Purchases and Product Returns](https://pubsonline.informs.org/doi/10.1287/mksc.2019.1169); [balance: Python package for adjusting biased samples (survey weighting)](https://github.com/facebookresearch/balance); [McDonald's franchisees will now have an easier time repairing ice cream machines (US Copyright Office DMCA exemption for commercial food-preparation equipment)](https://www.nrn.com/quick-service/mcdonald-s-franchisees-will-now-have-an-easier-time-repairing-ice-cream-machines)
- **`07_M7_Predictive_Models_ML_and_AI`**: [Consumption Variety in Food Recommendation](https://www.journals.uchicago.edu/doi/10.1086/720453); [Fighting Churn with Data (companion code)](https://github.com/carl24k/fight-churn)
- **`08_M8_Current_Topics_in_Marketing`**: [Update on Plans for Privacy Sandbox Technologies](https://privacysandbox.google.com/blog/update-on-plans-for-privacy-sandbox-technologies); [Anthropic Economic Index](https://www.anthropic.com/economic-index); [The 2026 AI Index Report](https://hai.stanford.edu/ai-index/2026-ai-index-report)
- **`10_AI_Coding_Concepts_and_Evidence`**: [Stack Overflow Developer Survey 2025: AI](https://survey.stackoverflow.co/2025/ai/); [How Do Analysts Understand and Verify AI-Assisted Data Analyses?](https://arxiv.org/abs/2309.10947); [Stack Overflow Developer Survey 2026: AI](https://survey.stackoverflow.co/2026/ai); [Is GPT-4 a Good Data Analyst?](https://arxiv.org/abs/2305.15038)
- **`11_AI_Coding_Tools_and_Workflows`**: [Claude Code data usage (training, retention, telemetry)](https://code.claude.com/docs/en/data-usage); [Colab FAQ: AI features, data use, and Colab Pro for Education](https://research.google.com/colaboratory/faq.html); [Create and edit files with Claude (code execution and file creation)](https://support.claude.com/en/articles/12111783); [Data analysis with ChatGPT](https://help.openai.com/en/articles/8437071-data-analysis-with-chatgpt); [Google Colab: AI-powered notebooks (Gemini in Colab)](https://developers.google.com/colab); [Claude Code: A Highly Agentic Coding Assistant (DeepLearning.AI)](https://www.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant); [Data Science Agent in Colab: The future of data analysis with Gemini](https://developers.googleblog.com/en/data-science-agent-in-colab-with-gemini/); [claude-ecom: Claude Code plugin that turns order CSVs into business reviews](https://github.com/takechanman1228/claude-ecom); [Enterprise privacy at OpenAI (business data commitments)](https://openai.com/enterprise-privacy/); [marimo: generate notebooks with AI (built-in assistant, marimo pair, text-to-notebook)](https://docs.marimo.io/guides/generate_with_ai/); [pandera: statistical data testing for DataFrames](https://github.com/unionai-oss/pandera); [Julius AI](https://julius.ai); [Lovable (AI full-stack web app builder)](https://docs.lovable.dev/introduction); [Replit Agent](https://docs.replit.com/replitai/agent); [v0 by Vercel](https://v0.app/docs); [Build Apps with Windsurf's AI Coding Agents (DeepLearning.AI)](https://www.deeplearning.ai/short-courses/build-apps-with-windsurfs-ai-coding-agents/)
- **`12_AI_Coding_Pedagogy_and_Policy`**: [Enterprise GenAI: AI Apps (University of Illinois)](https://genai.illinois.edu/ai-apps/)
- **`20_Datasets`**: [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce); [Google Analytics 4 sample ecommerce dataset (Google Merchandise Store) in BigQuery](https://developers.google.com/analytics/bigquery/web-ecommerce-demo-dataset); [R for Marketing Research and Analytics: companion data, code and slides](https://r-marketing.r-forge.r-project.org/); [Online Retail II](https://archive.ics.uci.edu/dataset/502/online+retail+ii); [dunnhumby Source Files: The Complete Journey, Breakfast at the Frat, Carbo-Loading, Let's Get Sort-of-Real](https://www.dunnhumby.com/source-files/); [Yelp Open Dataset](https://business.yelp.com/data/resources/open-dataset/); [Online Shoppers Purchasing Intention Dataset](https://archive.ics.uci.edu/dataset/468/online+shoppers+purchasing+intention+dataset); [Kaggle Datasets](https://www.kaggle.com/datasets); [TidyTuesday weekly datasets](https://github.com/rfordatascience/tidytuesday)
- **`21_Open_Textbooks_and_Courses`**: [Data Analytics for Marketing: A practical guide to analyzing marketing data using Python (companion code)](https://github.com/PacktPublishing/Data-Analytics-for-Marketing); [Python for Data Analysis, 3rd Edition (Open Access)](https://wesmckinney.com/book/); [Python for Marketing Research and Analytics](https://python-marketing-research.github.io/); [Fundamentals of Data Visualization](https://clauswilke.com/dataviz/); [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/); [Coding for Economists](https://aeturrell.github.io/coding-for-economists/); [Applied Marketing Analytics Using Python](https://collegepublishing.sagepub.com/products/applied-marketing-analytics-using-python-1-288563); [Data 100 Course Notes: Principles and Techniques of Data Science](https://ds100.org/course-notes/); [Machine Learning and Generative AI for Marketing (companion code)](https://github.com/PacktPublishing/Machine-Learning-and-Generative-AI-for-Marketing); [Data Science for Marketing Analytics, Second Edition (companion code)](https://github.com/PacktPublishing/Data-Science-for-Marketing-Analytics-Second-Edition); [Data Science DISCOVERY (University of Illinois)](https://discovery.cs.illinois.edu/); [Dealing with Data (NYU teaching notebooks)](https://github.com/ipeirotis/dealing_with_data); [Kaggle Learn micro-courses](https://www.kaggle.com/learn); [QuantEcon DataScience: Introduction to Economic Modeling and Data Science](https://datascience.quantecon.org/); [Think Stats, 3rd Edition](https://allendowney.github.io/ThinkStats/); [Data Science for Marketing Analytics (first edition, companion code)](https://github.com/TrainingByPackt/Data-Science-for-Marketing-Analytics); [R_to_Python_marketing_analysis: Python translation of R for Marketing Research and Analytics](https://github.com/Charlotte2110/R_to_Python_marketing_analysis); [Hands-On Data Science for Marketing (code repository)](https://github.com/PacktPublishing/Hands-On-Data-Science-for-Marketing)
- **`22_Wiki_Design_and_Hosting`**: [Packages built in Pyodide](https://pyodide.org/en/stable/usage/packages-in-pyodide.html); [Quickstart for GitHub Pages](https://docs.github.com/en/pages/quickstart); [Observable Framework](https://observablehq.github.io/framework/); [The Pudding](https://pudding.cool/)
