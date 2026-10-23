# M1 · Introduction to Marketing Analytics and Python

18 resources (6 core). Built 2026-10-23 from `00_Index/_data/`; edit the YAML there and rerun `00_Index/_build/build_catalog.py` rather than editing this file.

Priority: **core** = likely to assign or build on; **recommended** = strong supplement; **optional** = background or niche. *Access* tells you whether students can open it without a login.

## Contents

- [What is marketing analytics?](#what-is-marketing-analytics) (6)
- [Textbooks from the previous syllabus](#textbooks-from-the-previous-syllabus) (2)
- [Python setup and basics](#python-setup-and-basics) (4)
- [Git and GitHub](#git-and-github) (2)
- [Python for marketing analytics: notebooks and code](#python-for-marketing-analytics-notebooks-and-code) (4)

## What is marketing analytics?

- [core] **[A Strategic Framework for Artificial Intelligence in Marketing](https://link.springer.com/article/10.1007/s11747-020-00749-9)** (2021) — Huang, M.-H.; Rust, R.T. *Journal of the Academy of Marketing Science 49, 30-50*
  `paper` · `intro` · `access: open` · `CC BY 4.0` · `AI angle`
  Open-access framework that sorts AI into mechanical, thinking and feeling types and maps each onto research, STP strategy and the 4Ps.
  *Use in wiki:* Gives students an open-access framework for placing each later module (and each AI tool) in the marketing process.
  DOI [10.1007/s11747-020-00749-9](https://doi.org/10.1007/s11747-020-00749-9)
  *Note:* Published online March 2020; issue year 2021.

- [core] **[Marketing Analytics for Data-Rich Environments](https://journals.sagepub.com/doi/full/10.1509/jm.15.0413)** (2016) — Wedel, M.; Kannan, P.K. *Journal of Marketing 80(6), 97-121*
  `paper` · `intermediate` · `access: library`
  Widely cited JM review of how marketing analytics evolved and how data-rich environments change models for CRM, the marketing mix, personalization and privacy, ending with a research agenda.
  *Use in wiki:* Assigned framing reading for week 1; its sections map onto the course modules and give students a vocabulary for the whole semester.
  DOI [10.1509/jm.15.0413](https://doi.org/10.1509/jm.15.0413)
  *Note:* Citation confirmed on an AMA summary page. Won the 2017 Sheth/JM award per a UMD news page seen in search. No verified open-access copy.

- [recommended] **[Applying Data Analytics in Marketing](https://www.coursera.org/learn/applying-data-analytics-business-in-marketing)** (2025) — Narang, U. (University of Illinois Urbana-Champaign). *Coursera*
  `course` · `intro` · `access: freemium` · `AI angle`
  Gies MOOC taught by Unnati Narang, about 16-20 hours with Python demos. Four modules: course intro and causal analysis (experiments, matching, IV, DiD); AI, prediction and ML including LLM applications; user, firm and AI-generated content analysis; and segmentation, conjoint, CLV and churn.
  *Use in wiki:* Link as optional video backup for students who want lectures; its module order closely tracks Marketing Analytics.
  Tools: Python, Generative AI
  *Note:* Year is approximate: the page shows no launch date, but its LLM content suggests a 2024-2025 revision. Rated 4.5/5 (206 reviews) when fetched. Can count toward UIUC degree programs.

- [recommended] **[MSI Research Priorities (booklet)](https://msi.org/wp-content/uploads/sites/2/2025/10/MSI_ResearchPriorities.pdf)** (2025) — Marketing Science Institute. *Marketing Science Institute*
  `report` · `intro` · `access: open` · `AI angle`
  MSI's current priority list from member firms. 'Marketing Analytics: AI, models, measurement, and communication' is the first of four themes, and it includes integrating AI into analytics and combining disparate data sources.
  *Use in wiki:* Show on the course home page as evidence of what practitioners say they need: AI, measurement, and communicating results.
  [Open-access copy](https://msi.org/wp-content/uploads/sites/2/2025/10/MSI_ResearchPriorities.pdf)
  *Note:* The PDF does not state a year range; the upload folder dates it to October 2025. The earlier 2024 announcement (same four themes) is at https://www.msi.org/article/msi-announces-2024-research-priorities/

- [recommended] **[Editorial: Marketing Science and Big Data](https://doi.org/10.1287/mksc.2016.0996)** (2016) — Chintagunta, P.; Hanssens, D.M.; Hauser, J.R. *Marketing Science 35(3), 341-342*
  `paper` · `intro` · `access: open` · `CC BY-NC-SA 4.0 (MIT DSpace author manuscript)`
  Two-page editorial arguing that big data does not replace marketing science; theory, causal identification and managerial relevance still matter.
  *Use in wiki:* Short opening reading next to Wedel and Kannan; a good prompt for a discussion on 'data vs. models'.
  DOI [10.1287/mksc.2016.0996](https://doi.org/10.1287/mksc.2016.0996) · [Open-access copy](https://dspace.mit.edu/handle/1721.1/111088)

- [optional] **[Precision Retailing: Driving Results with Behavioral Insights and Data Analytics](https://utorontopress.com/9781487542719/precision-retailing)** (2024) — Dubé, L.; Cohen, M.; Yang, N.; Monla, B. (eds.). *University of Toronto Press*
  `book` · `intermediate` · `access: paid`
  Edited volume on combining behavioral insight and data analytics in retail, co-edited by the instructor.
  *Use in wiki:* Optional instructor-authored background; individual chapters could anchor M1 framing or M8 retail topics.
  *Note:* Also on the MBA 542 Module 1 reading list.

## Textbooks from the previous syllabus

- [optional] **[Principles of Marketing Engineering and Analytics (3rd ed.)](https://faculty.essec.edu/research/3268-principles-of-marketing-engineering-and-analytics-3rd-edition)** (2017) — Lilien, G.L.; Rangaswamy, A.; De Bruyn, A. *DecisionPro*
  `book` · `intermediate` · `access: paid`
  Model-based marketing decision-making text (segmentation, positioning, conjoint, forecasting, CLV, resource allocation) built around the browser-based Enginius software.
  *Use in wiki:* Instructor background, and a source of model templates that students can rebuild in Python with AI help.
  Tools: Enginius
  *Note:* No Python companion found. Its companion software is Enginius (https://www.enginius.biz/), a web platform with segmentation, conjoint, positioning, Bass, CLV, text and network tools; pricing is quote-based and Python is not mentioned.

- [optional] **[Cutting-Edge Marketing Analytics: Real World Cases and Data Sets for Hands On Learning](https://www.oreilly.com/library/view/-/9780133552584/)** (2014) — Venkatesan, R.; Farris, P.; Wilcox, R.T. *Pearson FT Press*
  `book` · `intermediate` · `access: library`
  Darden case-based text with technical notes and real datasets on resource allocation, marketing mix, pricing, customer and digital analytics, and dashboards.
  *Use in wiki:* Source of case narratives that students can redo in Python; suggested textbook on the old syllabus.
  *Note:* No Python companion found. The O'Reilly page does not say which software the data exercises assume. Free Pearson sample pages appeared in search: https://ptgmedia.pearsoncmg.com/images/9780133552522/samplepages/9780133552522.pdf . O'Reilly Learning is often available through university libraries; check UIUC access.

## Python setup and basics

- [core] **[10 minutes to pandas (official quick start)](https://pandas.pydata.org/docs/user_guide/10min.html)** (2026) — pandas development team. *pandas 3.1 documentation*
  `documentation` · `intro` · `access: open` · `BSD-3-Clause (pandas)` · `AI angle`
  Official quick tour of Series and DataFrame: selection with loc and iloc, missing data, groupby, merge, pivot_table, time series, categoricals, plotting and I/O.
  *Use in wiki:* Reference card for the first coding lab; students can ask an AI assistant to explain each code block.
  Tools: pandas
  *Note:* The docs are now pandas 3.x, which changed copy-on-write and default string dtype behavior. Code that LLMs write from older training data may use deprecated 1.x and 2.x idioms, so students should be told to check warnings. (The license is the well-known pandas BSD-3 and was not rechecked on this page.)

- [core] **[Project Jupyter (JupyterLab and Jupyter Notebook)](https://jupyter.org/)** (2026) — Project Jupyter. *jupyter.org*
  `tool` · `intro` · `access: open`
  Home of the notebook format, with JupyterLab, the classic Notebook, JupyterHub, Voila and Jupyter Book; includes a try-in-browser option and install docs.
  *Use in wiki:* Background page explaining what a notebook is, since Colab, VS Code and Cursor all run the same .ipynb format.
  Tools: JupyterLab, Jupyter Notebook
  *Note:* Try online: https://jupyter.org/try ; install: https://jupyter.org/install . AI option for local JupyterLab users: the Jupyter AI extension (BSD-3-Clause), https://github.com/jupyterlab/jupyter-ai , which connects agents such as Claude, Codex, Copilot and Gemini through the Agent Client Protocol.

- [recommended] **[Plotting and Programming in Python (Software Carpentry)](https://swcarpentry.github.io/python-novice-gapminder)** (2025) — The Carpentries. *Software Carpentry*
  `tutorial` · `intro` · `access: open` · `CC BY 4.0`
  Twenty-episode workshop lesson for novices using JupyterLab: variables, lists, loops and functions, reading tabular data into DataFrames, and plotting.
  *Use in wiki:* Ready-made, openly licensed lesson that can be adapted into the wiki's Python bootcamp pages.
  Tools: Python, JupyterLab, pandas, matplotlib
  *Note:* The year reflects the continuously updated lesson, not a fixed edition.

- [optional] **[Anaconda Distribution](https://www.anaconda.com/download)** (2026) — Anaconda, Inc. *anaconda.com*
  `tool` · `intro` · `access: freemium`
  Bundled Python data-science distribution with conda, Jupyter Notebook and JupyterLab.
  *Use in wiki:* Mention as the traditional install path, with the licensing caveat; steer students to Colab or uv first.
  Tools: conda, Jupyter
  *Note:* Licensing caveat: per its terms, organizations with more than 200 employees or contractors need a paid license unless eligible for free use. Check UIUC's status before recommending. Free alternative: Miniforge (conda-forge only, BSD-3-Clause) at https://github.com/conda-forge/miniforge

## Git and GitHub

- [core] **[Introduction to GitHub (GitHub Skills exercise)](https://github.com/skills/introduction-to-github)** (2025) — GitHub. *GitHub Skills*
  `tutorial` · `intro` · `access: free-registration` · `MIT`
  Self-guided, under-one-hour exercise in the browser: create a branch, commit a file, open and merge a pull request; it ends with a profile README.
  *Use in wiki:* First-week graded check-in: each student completes it and submits the resulting repo link.
  Tools: GitHub
  *Note:* skills.github.com now redirects to GitHub Learn (https://learn.github.com/skills), which lists further exercises (GitHub Pages, Markdown, Copilot); that catalog did not render on fetch.

- [core] **[Version Control with Git (Software Carpentry)](https://swcarpentry.github.io/git-novice)** (2025) — The Carpentries. *Software Carpentry*
  `tutorial` · `intro` · `access: open` · `CC BY 4.0`
  Novice lesson on setting up Git, tracking changes, history, .gitignore, GitHub remotes, collaborating, resolving conflicts, licensing, citation and hosting.
  *Use in wiki:* Adapt into the wiki's 'Git for your team project' page; the collaboration and conflict episodes fit team blog-plus-code projects.
  Tools: git, GitHub

## Python for marketing analytics: notebooks and code

- [recommended] **[pandas_exercises](https://github.com/guipsamora/pandas_exercises)** (2024) — Samora, G. (guipsamora) and contributors. *GitHub*
  `notebook` · `intro` · `access: open` · `BSD-3-Clause`
  13k-star exercise bank in 11 topics (getting to know data, filtering, grouping, apply, merge, stats, visualization, time series...). Each comes in exercise, code-free solution and full-solution versions. Datasets include Chipotle orders and Online Retail.
  *Use in wiki:* Warm-up drills for M1/M2. A good format for 'try it alone, then with an AI assistant, then compare to the solution' activities.
  Tools: pandas, matplotlib, seaborn · Local copy: `01_M1_Marketing_Analytics_and_Python/repos/guipsamora__pandas_exercises`
  *Note:* Size unverified (tree API failed). Most exercises load data from raw GitHub URLs, which works from Colab. Some solutions use pre-pandas-2 idioms.

- [optional] **[Marketing Analytics Jumpstart (Google Cloud)](https://github.com/GoogleCloudPlatform/marketing-analytics-jumpstart)** (2026) — Google Cloud Platform. *GitHub*
  `tool` · `advanced` · `access: open` · `Apache-2.0`
  Terraform-deployed solution that ingests GA4 and Google Ads exports into BigQuery, builds features with Dataform, trains purchase-propensity, CLV and churn models (Vertex AutoML) plus BigQuery ML k-means audiences, and sends predictions back to GA4. Includes a workshop events_analysis notebook.
  *Use in wiki:* Instructor background on how GA4 exports feed CLV and segmentation in industry. Show the architecture diagram; don't assign it.
  Tools: bigquery, dataform, vertex-ai, terraform
  *Note:* Openly licensed but cataloged link-only on purpose: it needs a GCP project and GA4 property, so it's poor for students. Its notebooks/events_analysis.ipynb (6 MB) holds saved widget state with real-looking GA4 event values, including a Log4j-style JNDI probe string captured from traffic; it's harmless in Python but should be cleared before reuse. Not an officially supported Google product.

- [optional] **[Python for Excel, 2nd edition (companion repo)](https://github.com/fzumstein/python-for-excel)** (2026) — Zumstein, F. *O'Reilly (2nd ed., June 2026)*
  `notebook` · `intro` · `access: open` · `MIT`
  Chapter notebooks for using pandas with Excel files: reading and writing workbooks, openpyxl, XlsxWriter and xlwings sales-report scripts, and sample sales data. Runs in Binder except the chapter that needs desktop Excel.
  *Use in wiki:* M1 on-ramp for students whose analytics background is Excel: convert a familiar Excel sales report into a pandas script.
  Tools: pandas, openpyxl, xlsxwriter, xlwings
  *Note:* Default branch is '2e' (1st ed. is on another branch). The xl/ folder (28 MB, including a 21 MB big.xlsx) is skipped; some ch08–ch10 cells need files from xl/. The repo doesn't cover Microsoft's Python-in-Excel feature.

- [optional] **[Marketing Analytics (MBA/EWMBA 263) course overview, UC Berkeley Haas](https://aiai.berkeley.edu/course-overview-mock-ups/)** (2025) — UC Berkeley Haas School of Business (aiai initiative). *Berkeley Haas aiai*
  `syllabus` · `intro` · `access: open`
  Course overview for a 3-unit MBA marketing analytics course taught in Jupyter/Python: acquisition, targeting and retention, experimental design, SEO and web analytics. Methods include RFM and clustering, logistic regression, neural nets and discrete choice with full-factorial designs.
  *Use in wiki:* Benchmark for scoping Marketing Analytics against a peer MBA course.
  Tools: jupyter, python
  *Note:* The page is titled 'Course Overview Mock-ups' and names no instructor; year is approximate. No public notebooks. Public university marketing-analytics course repos in Python turned out to be rare; those found were R-based (Tilburg gknox79/customer-analytics, Kellogg fzettelmeyer/mktg482, USC dadepro/mkt566) or unlicensed student work.

## AI-assisted coding angle for this module

Resources in this folder that show the method done with AI help, LLM versions of the method, or documented failure modes of AI-written analysis:

- [10 minutes to pandas (official quick start)](https://pandas.pydata.org/docs/user_guide/10min.html)
- [A Strategic Framework for Artificial Intelligence in Marketing](https://link.springer.com/article/10.1007/s11747-020-00749-9)
- [Applying Data Analytics in Marketing](https://www.coursera.org/learn/applying-data-analytics-business-in-marketing)
- [MSI Research Priorities (booklet)](https://msi.org/wp-content/uploads/sites/2/2025/10/MSI_ResearchPriorities.pdf)

## Also relevant (catalogued in other folders)

- **`02_M2_Customer_Data_and_Visualization`**: [Matplotlib cheatsheets and handouts (source)](https://github.com/matplotlib/cheatsheets); [EcommerceTools: data science toolkit for ecommerce and marketing science](https://github.com/practical-data-science/ecommercetools)
- **`05_M5_Text_and_Social_Media_Analytics`**: [Introduction to Cultural Analytics & Python](https://melaniewalsh.github.io/Intro-Cultural-Analytics/welcome.html); [Natural Language Processing with Python: Analyzing Text with the Natural Language Toolkit](https://www.nltk.org/book/)
- **`06_M6_Causal_Inference_and_Experiments`**: [statsmodels.stats.power: tt_ind_solve_power / NormalIndPower](https://www.statsmodels.org/v0.14.4/generated/statsmodels.stats.power.tt_ind_solve_power.html)
- **`07_M7_Predictive_Models_ML_and_AI`**: [Data Science for Business: What You Need to Know about Data Mining and Data-Analytic Thinking](https://oreilly.com/library/view/data-science-for/9781449374273)
- **`08_M8_Current_Topics_in_Marketing`**: [Simon Willison's Weblog](https://simonwillison.net/)
- **`10_AI_Coding_Concepts_and_Evidence`**: [Andrej Karpathy: Software Is Changing (Again)](https://www.youtube.com/watch?v=LCEmiRjPEtQ); [Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/); [Not all AI-assisted programming is vibe coding (but vibe coding rocks)](https://simonwillison.net/2025/Mar/19/vibe-coding/); [There's a new kind of coding I call 'vibe coding' (X post)](https://x.com/karpathy/status/1886192184808149383); [To vibe or not to vibe](https://www.martinfowler.com/articles/exploring-gen-ai/to-vibe-or-not-vibe.html); [We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs](https://arxiv.org/abs/2406.10279); [How Do Analysts Understand and Verify AI-Assisted Data Analyses?](https://arxiv.org/abs/2309.10947); [The 70% problem: Hard truths about AI-assisted coding](https://addyo.substack.com/p/the-70-problem-hard-truths-about); [Generative AI for Economic Research: Use Cases and Implications for Economists](https://www.aeaweb.org/articles?id=10.1257/jel.20231736); [Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of AI on Knowledge Worker Productivity and Quality](https://papers.ssrn.com/abstract=4573321); [DS-1000: A Natural and Reliable Benchmark for Data Science Code Generation](https://arxiv.org/abs/2211.11501)
- **`11_AI_Coding_Tools_and_Workflows`**: [Access GitHub Copilot for free as a student (Copilot Student plan)](https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-for-students); [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices); [Claude Code documentation: overview and quickstart](https://code.claude.com/docs/en/overview); [Codex documentation: CLI, IDE extension, cloud, and app (ChatGPT Learn)](https://learn.chatgpt.com/docs); [Colab FAQ: AI features, data use, and Colab Pro for Education](https://research.google.com/colaboratory/faq.html); [Create and edit files with Claude (code execution and file creation)](https://support.claude.com/en/articles/12111783); [Data analysis with ChatGPT](https://help.openai.com/en/articles/8437071-data-analysis-with-chatgpt); [Google AI Pro for students (free for 1 year)](https://gemini.google/students/); [Google Colab: AI-powered notebooks (Gemini in Colab)](https://developers.google.com/colab); [Claude Code: A Highly Agentic Coding Assistant (DeepLearning.AI)](https://www.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant); [Data Science Agent in Colab: The future of data analysis with Gemini](https://developers.googleblog.com/en/data-science-agent-in-colab-with-gemini/); [Here's how I use LLMs to help me write code](https://simonwillison.net/2025/Mar/11/using-llms-for-code/); [Build with AI in VS Code (agents, chat, MCP, customization)](https://code.visualstudio.com/docs/copilot/overview); [Claude plans and pricing](https://claude.com/pricing); [claude-ecom: Claude Code plugin that turns order CSVs into business reviews](https://github.com/takechanman1228/claude-ecom); [Cursor plans and pricing (restructured October 2026)](https://cursor.com/pricing); [Getting Started with GitHub Copilot (GitHub Skills exercise)](https://github.com/skills/getting-started-with-github-copilot); [GitHub Copilot plans (Free, Pro, Pro+, Max; usage-based AI credits)](https://github.com/features/copilot/plans); [GitHub Education and the Student Developer Pack](https://github.com/education); [Google Antigravity (agentic IDE, desktop app, CLI, SDK)](https://antigravity.google); [Jupyter AI (jupyterlab/jupyter-ai) v3](https://github.com/jupyterlab/jupyter-ai); [marimo: generate notebooks with AI (built-in assistant, marimo pair, text-to-notebook)](https://docs.marimo.io/guides/generate_with_ai/); [Posit Assistant in Positron (replaces Positron Assistant and Databot)](https://positron.posit.co/assistant.html); [The Turing Way: Guide for Reproducible Research](https://book.the-turing-way.org/reproducible-research/reproducible-research); [Use Claude Code in the cloud (Claude Code on the web) and the Claude Code desktop app](https://code.claude.com/docs/en/claude-code-on-the-web); [Using Git with coding agents](https://simonwillison.net/guides/agentic-engineering-patterns/using-git-with-coding-agents/); [uv: Python package and project manager](https://docs.astral.sh/uv/); [Vibe Coding 101 with Replit (DeepLearning.AI)](https://www.deeplearning.ai/short-courses/vibe-coding-101-with-replit/); [Good enough practices in scientific computing](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510)
- **`12_AI_Coding_Pedagogy_and_Policy`**: [Enterprise GenAI: AI Apps (University of Illinois)](https://genai.illinois.edu/ai-apps/); [Six Opportunities for Scientists and Engineers to Learn Programming Using AI Tools such as ChatGPT](https://pg.ucsd.edu/publications/scientists-engineers-learning-programming-using-ai_CiSE-2023.pdf)
- **`20_Datasets`**: [Online Retail II](https://archive.ics.uci.edu/dataset/502/online+retail+ii); [Kaggle Datasets](https://www.kaggle.com/datasets); [statsmodels example datasets and Rdatasets (get_rdataset)](https://www.statsmodels.org/stable/datasets/index.html); [Google Dataset Search](https://datasetsearch.research.google.com/)
- **`21_Open_Textbooks_and_Courses`**: [The Missing Semester of Your CS Education](https://missing.csail.mit.edu/); [AI Python for Beginners](https://www.deeplearning.ai/short-courses/ai-python-for-beginners/); [Data Analytics for Marketing: A practical guide to analyzing marketing data using Python (companion code)](https://github.com/PacktPublishing/Data-Analytics-for-Marketing); [Python for Data Analysis, 3rd Edition (Open Access)](https://wesmckinney.com/book/); [Python for Marketing Research and Analytics](https://python-marketing-research.github.io/); [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/); [Coding for Economists](https://aeturrell.github.io/coding-for-economists/); [Think Python, 3rd Edition](https://allendowney.github.io/ThinkPython/); [Marketing Analytics and Data Science: Tools and Models (supplementary code)](https://link.springer.com/book/9783032111296); [Machine Learning and Generative AI for Marketing (companion code)](https://github.com/PacktPublishing/Machine-Learning-and-Generative-AI-for-Marketing); [Data Science for Marketing Analytics, Second Edition (companion code)](https://github.com/PacktPublishing/Data-Science-for-Marketing-Analytics-Second-Edition); [Computational and Inferential Thinking: The Foundations of Data Science, 2nd ed. (Berkeley Data 8)](https://inferentialthinking.com/); [Data Science DISCOVERY (University of Illinois)](https://discovery.cs.illinois.edu/); [Dealing with Data (NYU teaching notebooks)](https://github.com/ipeirotis/dealing_with_data); [Kaggle Learn micro-courses](https://www.kaggle.com/learn); [Python for Everybody (PY4E)](https://www.py4e.com/); [QuantEcon DataScience: Introduction to Economic Modeling and Data Science](https://datascience.quantecon.org/); [Think Stats, 3rd Edition](https://allendowney.github.io/ThinkStats/); [Introduction to Python for Econometrics, Statistics and Numerical Analysis](https://www.kevinsheppard.com/teaching/python/notes/); [Data Science for Marketing Analytics (first edition, companion code)](https://github.com/TrainingByPackt/Data-Science-for-Marketing-Analytics); [Data Science for Economists (EC 607 lecture notes)](https://github.com/uo-ec607/lectures)
- **`22_Wiki_Design_and_Hosting`**: [Quickstart for GitHub Pages](https://docs.github.com/en/pages/quickstart); [Using Google Colab with GitHub (colab-github-demo notebook)](https://github.com/googlecolab/colabtools/blob/main/notebooks/colab-github-demo.ipynb)
