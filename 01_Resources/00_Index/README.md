# BADM 534 Resource Library — Master Index

530 catalogued resources across 14 folders · built 2026-10-23.

The course spine is the previous syllabus's eight modules (M1–M8). On top of that sit a dedicated AI-assisted coding track (folders 10–12), a datasets folder, cross-module open textbooks, and resources for designing and hosting the interactive wiki.

**How this is organised**

- Each folder's `README.md` is an annotated catalog grouped by subtopic and ranked core → recommended → optional.
- `resource_catalog.xlsx` / `.csv` hold the same entries in one filterable table. `resource_catalog.json` is the structured version the wiki can be generated from later.
- `_data/*.yaml` is the source of truth. Edit an entry there, then run `python3 _build/build_catalog.py` (from `00_Index`) to regenerate everything.
- `repos/` subfolders inside a module folder hold local copies of openly licensed GitHub material (notebooks, code, small datasets). Each one includes a `SOURCE.md` giving its origin and license.

## Start here: a short reading list

If you only open a dozen items before designing the wiki, open these.

- **The course spine in Python.** [Python for Marketing Research and Analytics](https://python-marketing-research.github.io/) covers most modules, and its Apache-2.0 notebooks and data are saved locally. [Marketing Analytics for Data-Rich Environments](https://journals.sagepub.com/doi/full/10.1509/jm.15.0413) works as an opening framing piece.
- **What AI coding actually does to productivity.** Read [The Impact of AI on Developer Productivity: Evidence from GitHub Copilot](https://arxiv.org/abs/2302.06590), [The Effects of Generative AI on High-Skilled Work: Evidence from Three Field Experiments with Software Developers](https://pubsonline.informs.org/doi/fpi/10.1287/mnsc.2025.00535) and [Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) together. The first finds speed-ups, the third finds a 19% slowdown, and METR's follow-up [We are Changing our Developer Productivity Experiment Design](https://metr.org/blog/2026-02-24-uplift-update/) is a ready-made M6 case on selection and study design. [Agentic coding and persistent returns to expertise](https://www.anthropic.com/research/claude-code-expertise) argues that domain expertise still matters.
- **What it does to learning.** [Generative AI without guardrails can harm learning: Evidence from high school mathematics](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4895486) and [How AI assistance impacts the formation of coding skills (paper: How AI Impacts Skill Formation)](https://www.anthropic.com/research/AI-assistance-coding-skills) are the two strongest cautions, and they shape how AI-assisted coding should be scaffolded in a course.
- **Checking AI-written analysis.** Start with [How Do Analysts Understand and Verify AI-Assisted Data Analyses?](https://arxiv.org/abs/2309.10947), [BLADE: Benchmarking Language Model Agents for Data-Driven Science](https://arxiv.org/abs/2408.09667) and [Leakage and the Reproducibility Crisis in ML-based Science](https://reproducible.cs.princeton.edu/). This is the course's recurring theme: AI writes the code, and the student has to be able to audit it.
- **Marketing anchors that pair well with an AI angle.** [Uniting the Tribes: Using Text for Marketing Insight](https://doi.org/10.1177/0022242919873106) with [ChatGPT outperforms crowd workers for text-annotation tasks](https://doi.org/10.1073/pnas.2305016120) (M5). [The Challenge of Using LLMs to Simulate Human Behavior: A Causal Inference Perspective](https://arxiv.org/abs/2312.15524) with [Digital Twins as Funhouse Mirrors: Five Key Distortions](https://arxiv.org/abs/2509.19088) (M4/M7). The ad-measurement trio [Consumer Heterogeneity and Paid Search Effectiveness: A Large-Scale Field Experiment](https://doi.org/10.3982/ECTA12423), [The Unfavorable Economics of Measuring the Returns to Advertising](https://ideas.repec.org/a/oup/qjecon/v130y2015i4p1941-1973.html) and [A Comparison of Approaches to Advertising Measurement: Evidence from Big Field Experiments at Facebook](https://www.kellogg.northwestern.edu/academics-research/research/detail/2019/a-comparison-of-approaches-to-advertising-measurement-evidence-from/) (M6). And [Retention Futility: Targeting High-Risk Customers Might Be Ineffective](https://journals.sagepub.com/doi/10.1509/jmr.16.0163) on why prediction is not targeting (M6/M7).
- **Working with agents.** [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices), [Agentic Engineering Patterns (guide)](https://simonwillison.net/guides/agentic-engineering-patterns/what-is-agentic-engineering/) and [AGENTS.md: a simple, open format for guiding coding agents](https://agents.md).
- **Wiki platform.** Look at [Quarto](https://quarto.org/) with [Quarto Live: interactive code blocks and exercises (webR and Pyodide)](https://r-wasm.github.io/quarto-live/), [Jupyter Book 2](https://jupyterbook.org/) and [jupyterlite/demo: template for deploying JupyterLite to GitHub Pages](https://github.com/jupyterlite/demo) side by side.

## 2026 changes that affect the course design

All of these were checked against primary or dated sources on 2026-10-23. Recheck them before the term starts.

1. **Which AI tools students may use with university data.** [Enterprise GenAI: AI Apps (University of Illinois)](https://genai.illinois.edu/ai-apps/) lists Microsoft Copilot Chat, Google Gemini, NotebookLM and Illinois Chat for students. Illinois ChatGPT and GitHub Copilot are licensed for faculty and staff only. Claude, Cursor and Codex are not on the list. That matters as soon as students touch real customer data from a project partner.
2. **GitHub Copilot for students is still free but more limited.** Since June 2026 it runs on monthly AI credits with automatic model selection ([Access GitHub Copilot for free as a student (Copilot Student plan)](https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-for-students)).
3. **Google has reshuffled its tools.** Gemini CLI was replaced by Antigravity CLI for free and consumer users on 18 June 2026 ([An important update: Transitioning Gemini CLI to Antigravity CLI](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli)). Separately, Google offers US college students a free year of Google AI Pro if claimed by 31 Dec 2026.
4. **Consolidation among coding tools.** SpaceX agreed in June 2026 to buy Cursor, which then restructured its pricing in October 2026 ([Cursor plans and pricing (restructured October 2026)](https://cursor.com/pricing)). Windsurf is now Devin Desktop ([Windsurf, now Devin Desktop (Cognition)](https://devin.ai/desktop)), and Posit Assistant replaced Positron Assistant and Databot ([Posit Assistant in Positron (replaces Positron Assistant and Databot)](https://positron.posit.co/assistant.html)).
5. **GitHub Classroom was deprecated on 27 Aug 2026.** Assignment distribution needs another route; see the hosting section of the wiki folder.
6. **Accessibility is now a hard requirement for the wiki.** Campus standards require WCAG 2.2 AA for internally built web content, including course materials ([University of Illinois Minimum Digital Accessibility Standards](https://access.illinois.edu/ada/digital-accessibility-policy/minimum-standards/)). The federal ADA Title II compliance date for large public entities is now 26 April 2027 ([ADA.gov fact sheet: Title II rule on web content and mobile app accessibility](https://www.ada.gov/resources/2024-03-08-web-rule/)).
7. **In-browser Python now covers the course stack.** Pyodide ships pandas, scikit-learn and statsmodels ([Packages built in Pyodide](https://pyodide.org/en/stable/usage/packages-in-pyodide.html)), so wiki pages can run real exercises with nothing to install. On the documentation-tool side, Material for MkDocs is now in maintenance mode and Jupyter Book 2 (MyST) has shipped.
8. **M8 refresher.** Chrome is keeping third-party cookies and retiring most Privacy Sandbox APIs ([Update on Plans for Privacy Sandbox Technologies](https://privacysandbox.google.com/blog/update-on-plans-for-privacy-sandbox-technologies)). Agentic commerce ([Buy it in ChatGPT: Instant Checkout and the Agentic Commerce Protocol](https://openai.com/index/buy-it-in-chatgpt/)) and generative engine optimization ([GEO: Generative Engine Optimization](https://arxiv.org/abs/2311.09735)) are now live topics.

## Known gaps (worth filling before or during wiki design)

- I found no verified public syllabus for a *business-school* course built around vibe coding. [CS146S: The Modern Software Developer](https://themodernsoftware.dev/) is the closest model, and it is a CS course.
- I found no published rubric for grading AI-assisted coding work, and no worked, openly licensed RFM-segmentation notebook. Both are good candidates for building yourself.
- No paper targets AI-generated DiD or IV code specifically. The closest evidence is general statistical-reasoning benchmarks such as QRData, StatQA and BLADE.
- The searches found peer marketing-analytics course repositories only for NYU, Chicago Booth, Wharton (via Coursera) and UCSD Rady.
- Items with lingering doubts say so in their *Note* line, e.g. a venue taken from recollection or an unconfirmed dataset license.

## Folders

| Folder | Resources | Core | Open access | AI angle |
|---|---:|---:|---:|---:|
| [M1 · Introduction to Marketing Analytics and Python](../01_M1_Marketing_Analytics_and_Python/README.md) | 14 | 6 | 7 | 4 |
| [M2 · Customer Data and Visualization](../02_M2_Customer_Data_and_Visualization/README.md) | 33 | 8 | 25 | 7 |
| [M3 · Regression Analysis: A Review](../03_M3_Regression/README.md) | 21 | 6 | 19 | 5 |
| [M4 · Conjoint Analysis, Clustering and Customer Lifetime Value](../04_M4_Conjoint_Segmentation_CLV/README.md) | 33 | 14 | 24 | 7 |
| [M5 · Content Analysis, Text and Social Media](../05_M5_Text_and_Social_Media_Analytics/README.md) | 54 | 17 | 29 | 19 |
| [M6 · Causal Models and Experiments](../06_M6_Causal_Inference_and_Experiments/README.md) | 53 | 26 | 44 | 8 |
| [M7 · Predictive Models, AI and Machine Learning](../07_M7_Predictive_Models_ML_and_AI/README.md) | 33 | 16 | 28 | 10 |
| [M8 · Current Topics in Marketing](../08_M8_Current_Topics_in_Marketing/README.md) | 27 | 9 | 18 | 15 |
| [AI-Assisted Coding · Concepts, History and Evidence](../10_AI_Coding_Concepts_and_Evidence/README.md) | 50 | 23 | 46 | 50 |
| [AI-Assisted Coding · Tools and Workflows](../11_AI_Coding_Tools_and_Workflows/README.md) | 70 | 23 | 39 | 66 |
| [AI-Assisted Coding · Teaching, Learning and Policy](../12_AI_Coding_Pedagogy_and_Policy/README.md) | 29 | 9 | 28 | 29 |
| [Datasets for Exercises and Projects](../20_Datasets/README.md) | 36 | 13 | 28 | 2 |
| [Open Textbooks and Courses (cross-module)](../21_Open_Textbooks_and_Courses/README.md) | 33 | 11 | 25 | 5 |
| [Interactive Wiki · Design and Hosting](../22_Wiki_Design_and_Hosting/README.md) | 44 | 20 | 39 | 5 |

## Module × AI-assisted coding crosswalk

For each module, the core resources together with the resources that carry an AI-assisted coding angle. Use this as a starting point when designing each wiki page.

### M1 · Introduction to Marketing Analytics and Python

*Core:* [10 minutes to pandas (official quick start)](https://pandas.pydata.org/docs/user_guide/10min.html); [Access GitHub Copilot for free as a student (Copilot Student plan)](https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-for-students); [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices); [Claude Code documentation: overview and quickstart](https://code.claude.com/docs/en/overview); [Codex documentation: CLI, IDE extension, cloud, and app (ChatGPT Learn)](https://learn.chatgpt.com/docs); [Colab FAQ: AI features, data use, and Colab Pro for Education](https://research.google.com/colaboratory/faq.html); [Create and edit files with Claude (code execution and file creation)](https://support.claude.com/en/articles/12111783); [Data analysis with ChatGPT](https://help.openai.com/en/articles/8437071-data-analysis-with-chatgpt); [Enterprise GenAI: AI Apps (University of Illinois)](https://genai.illinois.edu/ai-apps/); [Google AI Pro for students (free for 1 year)](https://gemini.google/students/); [Google Colab: AI-powered notebooks (Gemini in Colab)](https://developers.google.com/colab); [Project Jupyter (JupyterLab and Jupyter Notebook)](https://jupyter.org/)

*AI angle:* [10 minutes to pandas (official quick start)](https://pandas.pydata.org/docs/user_guide/10min.html); [Access GitHub Copilot for free as a student (Copilot Student plan)](https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-for-students); [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices); [Claude Code documentation: overview and quickstart](https://code.claude.com/docs/en/overview); [Codex documentation: CLI, IDE extension, cloud, and app (ChatGPT Learn)](https://learn.chatgpt.com/docs); [Colab FAQ: AI features, data use, and Colab Pro for Education](https://research.google.com/colaboratory/faq.html); [Create and edit files with Claude (code execution and file creation)](https://support.claude.com/en/articles/12111783); [Data analysis with ChatGPT](https://help.openai.com/en/articles/8437071-data-analysis-with-chatgpt); [Enterprise GenAI: AI Apps (University of Illinois)](https://genai.illinois.edu/ai-apps/); [Google AI Pro for students (free for 1 year)](https://gemini.google/students/)

### M2 · Customer Data and Visualization

*Core:* [10 minutes to pandas (official quick start)](https://pandas.pydata.org/docs/user_guide/10min.html); [Claude Code data usage (training, retention, telemetry)](https://code.claude.com/docs/en/data-usage); [Colab FAQ: AI features, data use, and Colab Pro for Education](https://research.google.com/colaboratory/faq.html); [Create and edit files with Claude (code execution and file creation)](https://support.claude.com/en/articles/12111783); [Data analysis with ChatGPT](https://help.openai.com/en/articles/8437071-data-analysis-with-chatgpt); [Enterprise GenAI: AI Apps (University of Illinois)](https://genai.illinois.edu/ai-apps/); [Google Colab: AI-powered notebooks (Gemini in Colab)](https://developers.google.com/colab); [Matplotlib Quick start guide (and official cheatsheets)](https://matplotlib.org/stable/users/explain/quick_start.html); [Packages built in Pyodide](https://pyodide.org/en/stable/usage/packages-in-pyodide.html); [PyMC-Marketing CLV Quickstart (BG/NBD + Gamma-Gamma) and CLV model notebooks](https://www.pymc-marketing.io/en/stable/notebooks/clv/clv_quickstart.html); [Quickstart for GitHub Pages](https://docs.github.com/en/pages/quickstart); [The Python Graph Gallery](https://python-graph-gallery.com/)

*AI angle:* [10 minutes to pandas (official quick start)](https://pandas.pydata.org/docs/user_guide/10min.html); [Claude Code data usage (training, retention, telemetry)](https://code.claude.com/docs/en/data-usage); [Colab FAQ: AI features, data use, and Colab Pro for Education](https://research.google.com/colaboratory/faq.html); [Create and edit files with Claude (code execution and file creation)](https://support.claude.com/en/articles/12111783); [Data analysis with ChatGPT](https://help.openai.com/en/articles/8437071-data-analysis-with-chatgpt); [Enterprise GenAI: AI Apps (University of Illinois)](https://genai.illinois.edu/ai-apps/); [Google Colab: AI-powered notebooks (Gemini in Colab)](https://developers.google.com/colab); [Matplotlib Quick start guide (and official cheatsheets)](https://matplotlib.org/stable/users/explain/quick_start.html); [Claude Code: A Highly Agentic Coding Assistant (DeepLearning.AI)](https://www.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant); [Data Science Agent in Colab: The future of data analysis with Gemini](https://developers.googleblog.com/en/data-science-agent-in-colab-with-gemini/)

### M3 · Regression Analysis: A Review

*Core:* [Google Colab: AI-powered notebooks (Gemini in Colab)](https://developers.google.com/colab); [Packages built in Pyodide](https://pyodide.org/en/stable/usage/packages-in-pyodide.html); [AI Agents for Economic Research: August 2025 Update](https://www.aeaweb.org/articles/materials/23826); [Data Science Agent in Colab: The future of data analysis with Gemini](https://developers.googleblog.com/en/data-science-agent-in-colab-with-gemini/); [Meridian: Google's open-source Bayesian marketing mix model](https://developers.google.com/meridian); [PyFixest: fast high-dimensional fixed-effects regression in Python (quickstart, tutorials, llms.txt and agent skill file)](https://pyfixest.org/getting-started.html); [BLADE: Benchmarking Language Model Agents for Data-Driven Science](https://arxiv.org/abs/2408.09667); [How Do Analysts Understand and Verify AI-Assisted Data Analyses?](https://arxiv.org/abs/2309.10947); [seaborn user guide and tutorial](https://seaborn.pydata.org/tutorial.html); [An Introduction to Statistical Learning with Applications in Python (ISLP)](https://www.statlearning.com/); [Generative AI for Economic Research: Use Cases and Implications for Economists](https://www.aeaweb.org/articles?id=10.1257/jel.20231736); [ISLP_labs: Python lab notebooks for ISLP](https://github.com/intro-stat-learning/ISLP_labs)

*AI angle:* [Google Colab: AI-powered notebooks (Gemini in Colab)](https://developers.google.com/colab); [AI Agents for Economic Research: August 2025 Update](https://www.aeaweb.org/articles/materials/23826); [Data Science Agent in Colab: The future of data analysis with Gemini](https://developers.googleblog.com/en/data-science-agent-in-colab-with-gemini/); [PyFixest: fast high-dimensional fixed-effects regression in Python (quickstart, tutorials, llms.txt and agent skill file)](https://pyfixest.org/getting-started.html); [BLADE: Benchmarking Language Model Agents for Data-Driven Science](https://arxiv.org/abs/2408.09667); [How Do Analysts Understand and Verify AI-Assisted Data Analyses?](https://arxiv.org/abs/2309.10947); [Generative AI for Economic Research: Use Cases and Implications for Economists](https://www.aeaweb.org/articles?id=10.1257/jel.20231736); [pandera: statistical data testing for DataFrames](https://github.com/unionai-oss/pandera); [Posit Assistant in Positron (replaces Positron Assistant and Databot)](https://positron.posit.co/assistant.html); [Large Language Models: An Applied Econometric Framework](https://nber.org/papers/w33344)

### M4 · Conjoint Analysis, Clustering and Customer Lifetime Value

*Core:* [marimo WebAssembly notebooks](https://docs.marimo.io/guides/wasm/); [Packages built in Pyodide](https://pyodide.org/en/stable/usage/packages-in-pyodide.html); [PyMC-Marketing CLV Quickstart (BG/NBD + Gamma-Gamma) and CLV model notebooks](https://www.pymc-marketing.io/en/stable/notebooks/clv/clv_quickstart.html); [AI-Human Hybrids for Marketing Research: Leveraging Large Language Models (LLMs) as Collaborators](https://journals.sagepub.com/doi/10.1177/00222429241276529); [Digital Twins as Funhouse Mirrors: Five Key Distortions](https://arxiv.org/abs/2509.19088); [PyMC-Marketing: Bayesian MMM, CLV and choice models in Python](https://www.pymc-marketing.io/en/stable/); [Browsing the Aisles or Browsing the App? How Online Grocery Shopping is Changing What We Buy](https://pubsonline.informs.org/doi/10.1287/mksc.2022.0292); [Frontiers: Can Large Language Models Capture Human Preferences?](https://arxiv.org/abs/2305.02531); [Frontiers: Determining the Validity of Large Language Models for Automated Perceptual Analysis](https://doi.org/10.1287/mksc.2023.0454); [An Introduction to Statistical Learning with Applications in Python (ISLP)](https://www.statlearning.com/); [ISLP_labs: Python lab notebooks for ISLP](https://github.com/intro-stat-learning/ISLP_labs); [The Challenge of Using LLMs to Simulate Human Behavior: A Causal Inference Perspective](https://arxiv.org/abs/2312.15524)

*AI angle:* [AI-Human Hybrids for Marketing Research: Leveraging Large Language Models (LLMs) as Collaborators](https://journals.sagepub.com/doi/10.1177/00222429241276529); [Digital Twins as Funhouse Mirrors: Five Key Distortions](https://arxiv.org/abs/2509.19088); [PyMC-Marketing: Bayesian MMM, CLV and choice models in Python](https://www.pymc-marketing.io/en/stable/); [Frontiers: Can Large Language Models Capture Human Preferences?](https://arxiv.org/abs/2305.02531); [Frontiers: Determining the Validity of Large Language Models for Automated Perceptual Analysis](https://doi.org/10.1287/mksc.2023.0454); [The Challenge of Using LLMs to Simulate Human Behavior: A Causal Inference Perspective](https://arxiv.org/abs/2312.15524); [Using LLMs for Market Research](https://papers.ssrn.com/abstract=4395751); [PyMC-Marketing example data: synthetic MMM and CDNOW CLV](https://www.pymc-marketing.io/en/stable/notebooks/mmm/mmm_example.html); [Applying Data Analytics in Marketing](https://www.coursera.org/learn/applying-data-analytics-business-in-marketing); [Synthetic Replacements for Human Survey Data? The Perils of Large Language Models](https://www.cambridge.org/core/journals/political-analysis/article/synthetic-replacements-for-human-survey-data-the-perils-of-large-language-models/B92267DC26195C7F36E63EA04A47D2FE)

### M5 · Content Analysis, Text and Social Media

*Core:* [Bluesky API Directory: public endpoints (no authentication)](https://docs.bsky.app/docs/advanced-guides/api-directory); [NetworkX Tutorial](https://networkx.org/documentation/stable/tutorial.html); [Transformers Pipelines documentation (text-classification, zero-shot-classification)](https://huggingface.co/docs/transformers/main_classes/pipelines); [Working With Text Data (scikit-learn tutorial)](https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html); [2025 Creator Economy Ad Spend & Strategy Report](https://www.iab.com/insights/2025-creator-economy-ad-spend-strategy-report/); [AI-Human Hybrids for Marketing Research: Leveraging Large Language Models (LLMs) as Collaborators](https://journals.sagepub.com/doi/10.1177/00222429241276529); [Using natural language processing to analyse text data in behavioural science](https://www.nature.com/articles/s44159-024-00392-z); [Amazon Reviews 2023 (Amazon Reviews'23)](https://amazon-reviews-2023.github.io/); [Best Practices for Text Annotation with Large Language Models](https://sociologica.unibo.it/article/view/19461); [Classification with Claude: Insurance Support Ticket Classifier (Claude Cookbook)](https://platform.claude.com/cookbook/capabilities-classification-guide); [Frontiers: Determining the Validity of Large Language Models for Automated Perceptual Analysis](https://doi.org/10.1287/mksc.2023.0454); [GEO: Generative Engine Optimization](https://arxiv.org/abs/2311.09735)

*AI angle:* [AI-Human Hybrids for Marketing Research: Leveraging Large Language Models (LLMs) as Collaborators](https://journals.sagepub.com/doi/10.1177/00222429241276529); [Using natural language processing to analyse text data in behavioural science](https://www.nature.com/articles/s44159-024-00392-z); [Amazon Reviews 2023 (Amazon Reviews'23)](https://amazon-reviews-2023.github.io/); [Best Practices for Text Annotation with Large Language Models](https://sociologica.unibo.it/article/view/19461); [Classification with Claude: Insurance Support Ticket Classifier (Claude Cookbook)](https://platform.claude.com/cookbook/capabilities-classification-guide); [Frontiers: Determining the Validity of Large Language Models for Automated Perceptual Analysis](https://doi.org/10.1287/mksc.2023.0454); [GEO: Generative Engine Optimization](https://arxiv.org/abs/2311.09735); [Hands-On Large Language Models (official code repository)](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models); [Sentiment Analysis in the Age of Generative AI](https://link.springer.com/doi/10.1007/s40547-024-00143-4); [ChatGPT outperforms crowd workers for text-annotation tasks](https://doi.org/10.1073/pnas.2305016120)

### M6 · Causal Models and Experiments

*Core:* [CausalML: uplift modeling and causal inference with ML (Uber)](https://github.com/uber/causalml); [We are Changing our Developer Productivity Experiment Design](https://metr.org/blog/2026-02-24-uplift-update/); [CausalPy: causal inference for quasi-experiments in Python](https://github.com/pymc-labs/CausalPy); [Generative AI at Work](https://digitaleconomy.stanford.edu/publication/generative-ai-at-work); [Generative AI without guardrails can harm learning: Evidence from high school mathematics](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4895486); [Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/); [Meridian: Google's open-source Bayesian marketing mix model](https://developers.google.com/meridian); [PyFixest: fast high-dimensional fixed-effects regression in Python (quickstart, tutorials, llms.txt and agent skill file)](https://pyfixest.org/getting-started.html); [PyMC-Marketing: Bayesian MMM, CLV and choice models in Python](https://www.pymc-marketing.io/en/stable/); [Retail Media ROAS Demystified: Understanding Your Brand's ROAS](https://ovative.com/impact/expert-insights/retail-media-roas-demystified/); [The Effects of Generative AI on High-Skilled Work: Evidence from Three Field Experiments with Software Developers](https://pubsonline.informs.org/doi/fpi/10.1287/mnsc.2025.00535); [BLADE: Benchmarking Language Model Agents for Data-Driven Science](https://arxiv.org/abs/2408.09667)

*AI angle:* [We are Changing our Developer Productivity Experiment Design](https://metr.org/blog/2026-02-24-uplift-update/); [CausalPy: causal inference for quasi-experiments in Python](https://github.com/pymc-labs/CausalPy); [Generative AI at Work](https://digitaleconomy.stanford.edu/publication/generative-ai-at-work); [Generative AI without guardrails can harm learning: Evidence from high school mathematics](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4895486); [Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/); [PyFixest: fast high-dimensional fixed-effects regression in Python (quickstart, tutorials, llms.txt and agent skill file)](https://pyfixest.org/getting-started.html); [PyMC-Marketing: Bayesian MMM, CLV and choice models in Python](https://www.pymc-marketing.io/en/stable/); [The Effects of Generative AI on High-Skilled Work: Evidence from Three Field Experiments with Software Developers](https://pubsonline.informs.org/doi/fpi/10.1287/mnsc.2025.00535); [BLADE: Benchmarking Language Model Agents for Data-Driven Science](https://arxiv.org/abs/2408.09667); [Causal Reasoning and Large Language Models: Opening a New Frontier for Causality](https://arxiv.org/abs/2305.00050)

### M7 · Predictive Models, AI and Machine Learning

*Core:* [CausalML: uplift modeling and causal inference with ML (Uber)](https://github.com/uber/causalml); [Forecasting: Principles and Practice, the Pythonic Way](https://otexts.com/fpppy/); [Packages built in Pyodide](https://pyodide.org/en/stable/usage/packages-in-pyodide.html); [scikit-learn User Guide 12: Common pitfalls and recommended practices](https://scikit-learn.org/stable/common_pitfalls.html); [scikit-learn User Guide 3.1: Cross-validation, evaluating estimator performance](https://scikit-learn.org/stable/modules/cross_validation.html); [SHAP documentation: 'An introduction to explainable AI with Shapley values'](https://shap.readthedocs.io/en/latest/example_notebooks/overviews/An%20introduction%20to%20explainable%20AI%20with%20Shapley%20values.html); [StatsForecast: fast forecasting with statistical and econometric models](https://github.com/Nixtla/statsforecast); [Transformers Pipelines documentation (text-classification, zero-shot-classification)](https://huggingface.co/docs/transformers/main_classes/pipelines); [Working With Text Data (scikit-learn tutorial)](https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html); [XGBoost Documentation (incl. 'Introduction to Boosted Trees' and scikit-learn interface)](https://xgboost.readthedocs.io/en/stable/); [AI-Human Hybrids for Marketing Research: Leveraging Large Language Models (LLMs) as Collaborators](https://journals.sagepub.com/doi/10.1177/00222429241276529); [Andrej Karpathy: Software Is Changing (Again)](https://www.youtube.com/watch?v=LCEmiRjPEtQ)

*AI angle:* [scikit-learn User Guide 12: Common pitfalls and recommended practices](https://scikit-learn.org/stable/common_pitfalls.html); [AI-Human Hybrids for Marketing Research: Leveraging Large Language Models (LLMs) as Collaborators](https://journals.sagepub.com/doi/10.1177/00222429241276529); [Andrej Karpathy: Software Is Changing (Again)](https://www.youtube.com/watch?v=LCEmiRjPEtQ); [Data Science Agent in Colab: The future of data analysis with Gemini](https://developers.googleblog.com/en/data-science-agent-in-colab-with-gemini/); [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/); [Amazon Reviews 2023 (Amazon Reviews'23)](https://amazon-reviews-2023.github.io/); [Frontiers: Determining the Validity of Large Language Models for Automated Perceptual Analysis](https://doi.org/10.1287/mksc.2023.0454); [Hands-On Large Language Models (official code repository)](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models); [Using large language models to generate silicon samples in consumer and marketing research: Challenges, opportunities, and guidelines](https://business.columbia.edu/faculty/research/using-large-language-models-generate-silicon-samples-consumer-and-marketing); [Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus?](https://www.nber.org/papers/w31122)

### M8 · Current Topics in Marketing

*Core:* [Agentic coding and persistent returns to expertise](https://www.anthropic.com/research/claude-code-expertise); [An important update: Transitioning Gemini CLI to Antigravity CLI](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli); [One Useful Thing](https://www.oneusefulthing.org/); [The state of AI in 2026: On the road to ROI](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai); [2025 Creator Economy Ad Spend & Strategy Report](https://www.iab.com/insights/2025-creator-economy-ad-spend-strategy-report/); [AI Agents for Economic Research: August 2025 Update](https://www.aeaweb.org/articles/materials/23826); [AI-Human Hybrids for Marketing Research: Leveraging Large Language Models (LLMs) as Collaborators](https://journals.sagepub.com/doi/10.1177/00222429241276529); [Buy it in ChatGPT: Instant Checkout and the Agentic Commerce Protocol](https://openai.com/index/buy-it-in-chatgpt/); [Digital Twins as Funhouse Mirrors: Five Key Distortions](https://arxiv.org/abs/2509.19088); [Generative AI at Work](https://digitaleconomy.stanford.edu/publication/generative-ai-at-work); [Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/); [Meridian: Google's open-source Bayesian marketing mix model](https://developers.google.com/meridian)

*AI angle:* [Agentic coding and persistent returns to expertise](https://www.anthropic.com/research/claude-code-expertise); [An important update: Transitioning Gemini CLI to Antigravity CLI](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli); [One Useful Thing](https://www.oneusefulthing.org/); [The state of AI in 2026: On the road to ROI](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai); [AI Agents for Economic Research: August 2025 Update](https://www.aeaweb.org/articles/materials/23826); [AI-Human Hybrids for Marketing Research: Leveraging Large Language Models (LLMs) as Collaborators](https://journals.sagepub.com/doi/10.1177/00222429241276529); [Buy it in ChatGPT: Instant Checkout and the Agentic Commerce Protocol](https://openai.com/index/buy-it-in-chatgpt/); [Digital Twins as Funhouse Mirrors: Five Key Distortions](https://arxiv.org/abs/2509.19088); [Generative AI at Work](https://digitaleconomy.stanford.edu/publication/generative-ai-at-work); [Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)

## Merged duplicates

These entries turned up in more than one search. Each was kept once, and its module tags were merged:

- `fowler-bliki-vibe-coding` → `wikipedia-vibe-coding`
- `willison-how-i-use-llms-for-code` → `willison-using-llms-for-code`
- `willison-agentic-engineering-patterns-2` → `willison-agentic-engineering-patterns`
- `peng-copilot-productivity` → `peng-2023-copilot-rct`
- `cui-genai-high-skilled-work` → `cui-2025-three-field-experiments`
- `metr-ai-developer-productivity` → `metr-2025-early-ai-os-developer-rct`
- `becker-metr-2025-ai-developer-productivity` → `metr-2025-early-ai-os-developer-rct`
- `dellacqua-jagged-frontier` → `dellacqua-2023-jagged-frontier`
- `dellacqua-2023-jagged-technological-frontier` → `dellacqua-2023-jagged-frontier`
- `korinek-2023-genai-economic-research` → `korinek-2023-jel-generative-ai-economic-research`
- `gu-2023-verify-ai-assisted-analyses` → `gu-2024-analysts-verify-ai-analyses`
- `blade-benchmark-data-driven-science` → `gu-2024-blade-benchmark`
- `dsbench-data-science-agents` → `jing-2024-dsbench`
- `ds-1000-benchmark` → `lai-2023-ds-1000`
- `manning-zhu-horton-automated-social-science` → `manning-zhu-horton-2024-automated-social-science`
- `stanford-cs146s` → `stanford-cs146s-modern-software-developer`
- `deeplearningai-claude-code-course` → `dlai-claude-code-course`
- `deeplearningai-vibe-coding-101-replit` → `dlai-vibe-coding-replit`
- `uiuc-genai-approved-apps` → `uiuc-genai-ai-apps`
- `github-copilot-for-students` → `github-copilot-student-plan`
- `openai-chatgpt-data-analysis` → `chatgpt-data-analysis`
- `google-colab-faq-ai-first` → `colab-faq-ai-privacy`
- `colab-data-science-agent-2025` → `colab-data-science-agent`
- `colab-data-science-agent-2` → `colab-data-science-agent`
- `uv-python-package-manager` → `uv-python`
- `uci-online-retail-ii-dataset` → `uci-online-retail-ii`
- `uci-online-retail-ii-2` → `uci-online-retail-ii`
- `ga4-bigquery-ecommerce-sample` → `ga4-obfuscated-sample-ecommerce`
- `criteo-uplift-dataset` → `criteo-uplift`
- `amazon-reviews-2023-2` → `amazon-reviews-2023`
- `yelp-open-dataset-2` → `yelp-open-dataset`
- `dominicks-scanner-data` → `dominicks-finer-foods`
- `robyn-simulated-mmm` → `robyn-meta-mmm`
- `snap-network-datasets-2` → `snap-network-datasets`
- `mckinney-python-for-data-analysis-3e` → `mckinney-python-data-analysis-3e`
- `vanderplas-python-data-science-handbook-2` → `vanderplas-python-data-science-handbook`
- `islp-ch3-linreg-ch12-unsup` → `islp`
- `islp-book` → `islp`
- `data8-textbook` → `berkeley-data8-inferential-thinking`
- `fastai-course` → `fastai-practical-deep-learning`
- `brave-and-true-facure` → `facure-causal-inference-brave-true`
- `causal-inference-brave-true` → `facure-causal-inference-brave-true`
- `the-effect-huntington-klein` → `huntington-klein-the-effect`
- `causalml-book-chernozhukov` → `causalml-book`
- `huggingface-llm-course-2` → `huggingface-llm-course`
- `wilke-fundamentals-of-data-visualization` → `wilke-fundamentals-data-visualization`
- `jurafsky-martin-slp3-2` → `jurafsky-martin-slp3`
- `missing-semester-2026` → `mit-missing-semester`
- `schwarz-chapman-feit-2020-python-marketing-research` → `python-marketing-research-analytics`
- `python-marketing-research-site` → `python-marketing-research-analytics`
- `deeplearningai-ai-python-for-beginners` → `deeplearningai-ai-python-beginners`
- `msi-research-priorities` → `msi-research-priorities-current`
- `huang-rust-2021-ai-framework` → `huang-rust-2021-strategic-framework-ai-marketing`
- `github-pages-quickstart` → `github-pages-quickstart-plain-html`
- `fader-hardie-lee-2005-rfm-clv-isovalue-2` → `fader-hardie-lee-2005-rfm-clv-isovalue`
- `pymc-marketing-rfm-clv-quickstart` → `pymc-marketing-clv-quickstart`
- `google-privacy-sandbox-retirement-2025` → `privacy-sandbox-update-2025`
- `pyfixest` → `pyfixest-docs-and-llm-skill`
- `linearmodels` → `linearmodels-panel-iv`
- `qrdata-2024` → `qrdata-statistical-causal-reasoning`
- `brand-israeli-ngwe-llm-market-research` → `brand-israeli-ngwe-llms-market-research`
- `brand-israeli-ngwe-llm-market-research-2` → `brand-israeli-ngwe-llms-market-research`
- `arora-chakraborty-nishimura-2025-ai-human-hybrids-2` → `arora-chakraborty-nishimura-2025-ai-human-hybrids`
- `arora-2025-ai-human-hybrids` → `arora-chakraborty-nishimura-2025-ai-human-hybrids`
- `gui-toubia-llm-simulation-causal` → `gui-toubia-llm-simulation-causal-inference`
- `gui-toubia-llm-causal` → `gui-toubia-llm-simulation-causal-inference`
- `li-2024-llm-perceptual-analysis` → `li-castelo-katona-sarvary-2024-llm-perceptual`
- `google-meridian-mmm` → `meridian-google-mmm`
- `pymc-marketing-2` → `pymc-marketing`
- `causalml-uplift` → `causalml-uber`
- `ascarza-2018-retention-futility-2` → `ascarza-2018-retention-futility`
- `horton-homo-silicus-2` → `horton-homo-silicus`
