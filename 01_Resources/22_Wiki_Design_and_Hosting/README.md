# Interactive Wiki · Design and Hosting

44 resources (20 core). Built 2026-10-23 from `00_Index/_data/`; edit the YAML there and rerun `00_Index/_build/build_catalog.py` rather than editing this file.

Priority: **core** = likely to assign or build on; **recommended** = strong supplement; **optional** = background or niche. *Access* tells you whether students can open it without a login.

## Contents

- [Hosting and deployment](#hosting-and-deployment) (6)
- [Site frameworks](#site-frameworks) (10)
- [Running Python in the browser](#running-python-in-the-browser) (10)
- [Interactive components](#interactive-components) (11)
- [Accessibility](#accessibility) (4)
- [Exemplar course sites](#exemplar-course-sites) (3)

## Hosting and deployment

- [core] **[About GitHub Education for teachers](https://docs.github.com/en/education/about-github-education/github-education-for-teachers/about-github-education-for-teachers)** (2026) — GitHub. *GitHub Docs*
  `documentation` · `intro` · `access: free-registration` · `AI angle`
  Benefits for verified faculty at accredited institutions: a free GitHub Team plan (unlimited users and private repos) and a free GitHub Copilot Pro subscription.
  *Use in wiki:* Instructor-only: create a course GitHub organization for the wiki repo and team projects, and use Copilot Pro to demonstrate AI-assisted coding in class.
  Tools: GitHub, GitHub Copilot
  *Note:* Copilot Pro setup for teachers: https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-for-teachers-and-os-maintainers (seen in search, not fetched). This page still refers to GitHub Classroom as active, which is stale after the August 2026 shutdown. Student benefits were not checked here; check the campus program first.

- [core] **[GitHub Classroom deprecated](https://github.blog/changelog/2026-08-27-github-classroom-deprecated)** (2026) — GitHub. *GitHub Changelog*
  `blog` · `intro` · `access: open`
  GitHub Classroom shut down on 2026-08-28, including its website, APIs and services. Classroom and assignment names, tests defined outside repos and LTI rosters will be deleted; user accounts, repos and organizations stay.
  *Use in wiki:* Instructor-only: don't build BADM 534's assignment distribution on GitHub Classroom. Use Classroom 50, Codio, or plain template repositories instead.
  Tools: GitHub Classroom
  *Note:* New sign-ups ended 2026-05-26 (https://github.blog/changelog/2026-05-26-github-classroom-sign-ups-are-no-longer-available, fetched). GitHub's migration page names Codio and Classroom 50 as partner options and describes a gh CLI export utility (https://docs.github.com/en/education/manage-coursework-with-github-classroom/get-started-with-github-classroom/export-or-migrate-github-classroom-data, fetched). Older GitHub Education pages still describe Classroom as active and are stale.

- [core] **[GitHub Pages limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits)** (2026) — GitHub. *GitHub Docs*
  `documentation` · `intro` · `access: open`
  Official GitHub Pages limits: a published site can be at most 1 GB, and the source repo should stay under 1 GB. Soft limits are 100 GB/month of bandwidth and 10 builds/hour (custom GitHub Actions builds are exempt), and deployments time out after 10 minutes. Pages is not meant for commercial or sensitive-transaction sites.
  *Use in wiki:* Instructor-only planning: keep the wiki's datasets and media under these caps, host large data elsewhere (GitHub Releases, Box, Hugging Face), and never collect passwords or student data on the site.
  Tools: GitHub Pages
  *Note:* Rate-limited requests get HTTP 429. Custom domains use a CNAME record for a subdomain or A/ALIAS/ANAME for an apex domain; verify the domain first to prevent takeover (https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages, fetched). A campus subdomain such as *.illinois.edu would need campus DNS cooperation; that is my inference, not from GitHub's docs.

- [core] **[Using custom workflows with GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)** (2026) — GitHub. *GitHub Docs*
  `documentation` · `intermediate` · `access: open`
  How to build and deploy a Pages site with GitHub Actions using actions/configure-pages@v5, actions/upload-pages-artifact@v4 and actions/deploy-pages@v4 (the examples also use actions/checkout@v6). The deploy job needs the pages: write and id-token: write permissions.
  *Use in wiki:* Reference for the wiki's build pipeline; Quarto, Jupyter Book 2, marimo and JupyterLite sites all deploy this way.
  Tools: GitHub Actions, GitHub Pages
  *Note:* The artifact must be a gzipped tar under 10 GB with no symbolic or hard links. Action versions are as shown on 2026-10-23; pin them in the workflow file.

- [recommended] **[Classroom 50](https://www.classroom50.org/)** (2026) — Classroom 50 (reported to be the Fifty Foundation, the nonprofit behind CS50)
  `tool` · `intermediate` · `access: open`
  Free, open-source replacement for GitHub Classroom that distributes and autogrades programming assignments in GitHub repos. Features include template repos, due dates, individual or group work, pytest or input/output tests, CSV rosters and score export.
  *Use in wiki:* Candidate tool for handing out starter notebooks and programming assignments through GitHub, linked from the wiki's assignment pages.
  Tools: GitHub, pytest
  *Note:* The sponsoring organization and the feature list come from a third-party blog (https://bruceelgort.com/2026/07/20/github-classroom-is-gone-heres-the-free-tool-that-replaces-it/, fetched); the official homepage only says it is the free, open-source alternative to GitHub Classroom, with no license named. It needs a GitHub organization on a Team plan (free for verified educators) and broad read/write access to the org's repos. It reached general availability on 2026-07-01 per GitHub's migration doc. It is new, so pilot it before relying on it.

- [optional] **[Netlify pricing update: introducing credit-based plans](https://www.netlify.com/changelog/netlify-pricing-update-introducing-credit-based-plans/)** (2025) — Netlify. *Netlify Changelog*
  `blog` · `intro` · `access: freemium`
  Since 2025-09-05, Netlify plans run on credits. The free plan gives 300 credits a month. Each production deploy costs 15 credits, bandwidth 10 credits per GB, and web requests 3 credits per 10,000; preview deploys are free.
  *Use in wiki:* Instructor-only comparison: at 15 credits per production deploy, a free Netlify site allows at most about 20 deploys a month even before bandwidth. That is tight for a wiki updated often; GitHub Pages has no such meter.
  Tools: Netlify, Cloudflare Pages
  *Note:* Cloudflare Pages' free plan allows 500 builds a month, 20,000 files per site and 25 MiB per file (https://developers.cloudflare.com/pages/platform/limits, fetched). Both hosts offer deploy previews, which GitHub Pages lacks. Netlify's changelog does not say what happens when free credits run out.

## Site frameworks

- [core] **[Quarto](https://quarto.org/)** (2026) — Posit (Quarto project). *quarto.org*
  `tool` · `intermediate` · `access: open` · `AI angle`
  Open-source, Pandoc-based publishing system that turns .qmd, .ipynb and Markdown files containing Python or R code into websites, books, slides and PDFs. Websites get navigation, cross-references and a built-in local search index.
  *Use in wiki:* Leading candidate engine for the BADM 534 wiki. One source produces pages, slides and notebooks, and freeze means heavy Python runs only on the instructor's machine.
  Tools: quarto, jupyter, knitr, pandoc
  *Note:* Version status on 2026-10-23: 1.10.x is the current stable line (GitHub marks v1.10.18 as Latest, July 2026), and 1.11.x is in pre-release. Quarto 1.9 (2026-03-24, https://opensource.posit.co/blog/2026-03-24_1.9-release/, fetched) added 'llms-txt: true' for websites, which writes an llms.txt index plus a .llms.md copy of each page so students can feed the wiki to an AI assistant. It also made opt-in (express) cookie consent the default, added screen-reader labels for videos, and added experimental PDF/UA output. Release posts now live on opensource.posit.co. Algolia is an optional alternative to the built-in search.

- [core] **[Quarto: GitHub Pages publishing guide](https://quarto.org/docs/publishing/github-pages)** (2026) — Posit (Quarto project). *quarto.org*
  `documentation` · `intermediate` · `access: open`
  Covers three ways to publish: render to a docs/ folder, run 'quarto publish gh-pages', or use a GitHub Action (quarto-dev/quarto-actions/publish@v2). Also explains 'execute: freeze: auto', which runs code locally and commits the results in _freeze.
  *Use in wiki:* Step-by-step deployment for a Quarto wiki. Freeze avoids rebuilding Python environments in CI on every commit.
  Tools: quarto, GitHub Actions
  *Note:* Add a .nojekyll file when publishing from docs/. The Action route needs read/write workflow permissions.

- [core] **[Quickstart for GitHub Pages](https://docs.github.com/en/pages/quickstart)** (2026) — GitHub. *GitHub Docs*
  `documentation` · `intro` · `access: open`
  Shortest path to a live site: create a username.github.io repo and publish from a branch. The default pipeline assumes Jekyll and a _config.yml.
  *Use in wiki:* Baseline for the plain HTML + JS option: commit hand-written pages or single-file interactive HTML artifacts, and add an empty .nojekyll file to skip Jekyll processing.
  Tools: GitHub Pages, Jekyll
  *Note:* The quickstart itself does not mention .nojekyll; that tip comes from Quarto's GitHub Pages guide. Plain HTML gives full control and needs no build step, but you get no built-in navigation, search, cross-references or notebook rendering. Pair it with Pagefind for search.

- [core] **[Jupyter Book 2](https://jupyterbook.org/)** (2025) — Jupyter Book team (Project Jupyter). *jupyterbook.org*
  `tool` · `intermediate` · `access: open`
  Jupyter Book 2 was released the week of 2025-11-04, keeping the jupyter-book package name, and is rebuilt on the MyST Document Engine. Authors write in notebooks or MyST Markdown and get cross-references, build-time execution, and interactivity in the browser or through Binder/JupyterHub.
  *Use in wiki:* Strong alternative to Quarto if the wiki is notebook-first; it is the stack behind the Data 8 textbook and QuantEcon-style lecture sites.
  Tools: jupyter-book, mystmd
  *Note:* Known limitations versus v1 (https://jupyterbook.org/stable/resources/faq, fetched): pretty URLs, so my_page.html becomes /my-page/; myst.yml replaces _config.yml; not yet at parity on execution features, editable Thebe cells or autodoc. The v1 Sphinx stack is 'mostly in maintenance mode'; pin jupyter-book<2 to stay on v1. Release rationale: https://jupyterbook.org/blog/posts/2025-11-04-why-make-a-major-release. The blog shows active 2026 development: mystmd 1.8.2 (Mar 2026), an AnyWidget directive (Mar 2026), accessibility work on the MyST theme (May 2026), a 'Demystifying MyST Markdown in Education' event (Apr 2026) and a new release (Sep 2026).

- [recommended] **[MyST guide: exercises and solutions](https://mystmd.org/guide/exercises)** (2026) — MyST Markdown project. *mystmd.org*
  `documentation` · `intermediate` · `access: open`
  Documents MyST's numbered {exercise} directive and linked {solution} directive, including hidden and dropdown options. Gated start/end syntax lets executable code cells sit inside exercises while staying notebook-compatible.
  *Use in wiki:* Pattern for in-text exercises with collapsible solutions if the wiki is built with Jupyter Book 2 / MyST.
  Tools: mystmd, jupyter-book
  *Note:* There is no built-in quiz or auto-grading; pair with JupyterLite or Pyodide cells for runnable code.

- [recommended] **[Material for MkDocs Insiders – now free for everyone](https://squidfunk.github.io/mkdocs-material/blog/2025/11/11/insiders-now-free-for-everyone/)** (2025) — squidfunk (Material for MkDocs team). *Material for MkDocs blog*
  `blog` · `intro` · `access: open`
  Announces that Material for MkDocs 9.7.0 is the final feature release. The project is in maintenance mode with no new features, Insiders features are now free, and development moves to Zensical.
  *Use in wiki:* Instructor-only: the reason not to start a new course wiki on MkDocs + Material in 2026.
  Tools: mkdocs, mkdocs-material
  *Note:* Follow-up post on 2026-02-18 (https://squidfunk.github.io/mkdocs-material/blog/2026/02/18/mkdocs-2.0/, fetched): MkDocs 1.x is unmaintained. MkDocs 2.0 is a pre-release rewrite with TOML config and no plugin system, and Material will not support it. Material 9.7.5 pins MkDocs <2.0, and critical maintenance is extended through 2027-05-05. Material's GitHub Discussions went read-only in November 2025.

- [optional] **[Docusaurus blog and releases](https://docusaurus.io/blog)** (2026) — Meta Open Source. *docusaurus.io*
  `tool` · `advanced` · `access: open` · `MIT (code); CC BY 4.0 (docs)`
  React/MDX documentation-site generator from Meta. Version 3.10 (2026-04-07) is announced as the last release in the v3 line, ahead of v4.
  *Use in wiki:* Optional, and only if the wiki needs custom React components. Its JavaScript toolchain is heavier than Quarto or MyST for a non-CS course.
  Tools: docusaurus, react
  *Note:* Docusaurus has no native notebook execution, so Python content must be pre-rendered. A v4 major release is coming; expect migration work.

- [optional] **[Starlight (Astro documentation framework)](https://starlight.astro.build/)** (2026) — Astro / Starlight contributors. *starlight.astro.build*
  `tool` · `intermediate` · `access: open` · `MIT`
  Astro-based docs framework with built-in navigation, i18n, dark mode, Markdown/MDX/Markdoc, and Pagefind search that needs no configuration.
  *Use in wiki:* Optional fast, accessible site shell if the wiki is mostly prose plus embedded HTML artifacts.
  Tools: astro, starlight, pagefind
  *Note:* Still pre-1.0 (v0.42.6 per site metadata). Pagefind is the default search; Algolia DocSearch is available through a plugin (https://starlight.astro.build/guides/site-search/, fetched). Repo: https://github.com/withastro/starlight (MIT).

- [optional] **[VitePress](https://vitepress.dev/)** (2026) — Evan You and VitePress contributors. *vitepress.dev*
  `tool` · `intermediate` · `access: open` · `MIT`
  Vite + Vue static site generator for Markdown documentation. The site lists 2.0.0-alpha.20 as current and keeps docs for the 1.6.4 stable line.
  *Use in wiki:* Optional; similar trade-offs to Docusaurus, with Vue components instead of React.
  Tools: vitepress, vue
  *Note:* 2.0 was still in alpha on 2026-10-23. Repo: https://github.com/vuejs/vitepress.

- [optional] **[Zensical](https://zensical.org/)** (2025) — Zensical (Material for MkDocs team). *zensical.org*
  `tool` · `intermediate` · `access: open` · `MIT`
  Successor static site generator from the makers of Material for MkDocs. It reads existing mkdocs.yml projects and adds faster differential rebuilds and a new client-side search engine (Disco).
  *Use in wiki:* Keep on the watch list if a Markdown-only docs look is preferred; it is too young to be the main engine for an upcoming semester.
  Tools: zensical
  *Note:* Status on 2026-10-23: pre-0.1 (the site is built with zensical 0.0.70). A 'dependable release line' starting with 0.1 is scheduled for 2026-11-05. Only a subset of MkDocs plugins is supported. An October 2026 update says the planned Rust Markdown parser has been replaced by a Python-Markdown-compatible one. Announcement: https://squidfunk.github.io/mkdocs-material/blog/2025/11/05/zensical/. It has no notebook-execution story comparable to Quarto or MyST.

## Running Python in the browser

- [core] **[JupyterLite documentation](https://jupyterlite.readthedocs.io/en/stable/)** (2026) — JupyterLite contributors (Project Jupyter). *Read the Docs*
  `documentation` · `intermediate` · `access: open`
  A JupyterLab and Notebook distribution that runs entirely in the browser, with Pyodide or Xeus Python kernels in Web Workers. It deploys as a static site with no server.
  *Use in wiki:* Give students a full notebook interface from a wiki link (for example a 'Try it' button on each module) with no accounts or installs.
  Tools: jupyterlite, pyodide, xeus-python
  *Note:* The docs were labeled 0.8.6 when fetched, while their compatibility table listed jupyterlite-core 0.7.0 (bundling JupyterLab 4.5 and Notebook 7.5); confirm the current version before pinning. Only the last two releases are supported. Not every JupyterLab feature works. Student files are kept in browser storage, so test how work persists before relying on it for assignments.

- [core] **[jupyterlite/demo: template for deploying JupyterLite to GitHub Pages](https://github.com/jupyterlite/demo)** (2026) — JupyterLite contributors. *GitHub*
  `tool` · `intro` · `access: open` · `BSD-3-Clause`
  Template repo that builds a JupyterLite site and deploys it to GitHub Pages with GitHub Actions. Notebooks go in the content folder, and kernels and extensions are listed in requirements.txt.
  *Use in wiki:* Use as the template for a BADM 534 'lab' subsite that holds the module notebooks and is linked from the wiki.
  Tools: jupyterlite, GitHub Actions · Local copy: `22_Wiki_Design_and_Hosting/repos/jupyterlite__demo`
  *Note:* Deploy guide (https://jupyterlite.readthedocs.io/en/stable/quickstart/deploy.html, fetched): click 'Use this template', enable Actions, set workflow permissions to read/write and the Pages source to GitHub Actions. For pre-installed packages, use the xeus-python demo with an environment.yml. Live demo at jupyterlite.github.io/demo. Requires Firefox 90+ or Chromium 89+.

- [core] **[marimo WebAssembly notebooks](https://docs.marimo.io/guides/wasm/)** (2026) — marimo team. *docs.marimo.io*
  `documentation` · `intermediate` · `access: open`
  marimo's reactive notebooks can run entirely in the browser through Pyodide. numpy, scipy, scikit-learn, pandas and matplotlib are pre-installed, and other pure-Python wheels install automatically on import.
  *Use in wiki:* Build reactive demos (for example sliders driving a CLV or conjoint simulator), export them as static HTML, and embed them in wiki pages.
  Tools: marimo, pyodide
  *Note:* Export with 'marimo export html-wasm notebook.py -o out --mode run' for a read-only app or '--mode edit' for an editable notebook. The export must be served over HTTP, not opened from file://, and Pyodide and packages load from a CDN. Run 'marimo check --select MW' to catch incompatible packages (https://docs.marimo.io/guides/exporting/webassembly_html/, fetched). Limits: 2 GB memory, emulated concurrency, no PDB. marimo islands, which embed single reactive cells in any HTML page, are still a 'Preview' feature (https://docs.marimo.io/guides/island_example/, fetched).

- [core] **[Packages built in Pyodide](https://pyodide.org/en/stable/usage/packages-in-pyodide.html)** (2026) — Pyodide contributors. *pyodide.org*
  `documentation` · `intermediate` · `access: open`
  List of compiled packages shipped with Pyodide 314.0.7, including pandas 3.0.2, scikit-learn 1.8.0, statsmodels 0.14.6, scipy 1.18.0, matplotlib 3.10.8 and numpy 2.4.6. Seaborn is not on the built-in list.
  *Use in wiki:* Check before writing in-browser exercises: the core M2–M7 stack (pandas wrangling, statsmodels OLS/logit, scikit-learn clustering and prediction) runs in the browser.
  Tools: pandas, scikit-learn, statsmodels, scipy, matplotlib, numpy
  *Note:* Trade-offs: the first page load downloads the runtime and packages. marimo's docs cite a 2 GB memory cap and no true threading or multiprocessing under WASM. Packages with compiled code that are not on this list (for example PyTorch) generally won't install. Seaborn is pure Python and should install through micropip (not tested). pandas 3.0 is a major release, so syntax can differ from older tutorials and from whatever pandas version Colab ships; check version parity before mixing Colab and in-browser cells.

- [core] **[Using Google Colab with GitHub (colab-github-demo notebook)](https://github.com/googlecolab/colabtools/blob/main/notebooks/colab-github-demo.ipynb)** (2026) — Google Colab team. *GitHub (googlecolab/colabtools)*
  `notebook` · `intro` · `access: open`
  Official Colab notebook explaining the colab.research.google.com/github/<org>/<repo>/blob/<branch>/<path>.ipynb URL pattern and the 'Open In Colab' badge in Markdown and HTML. It also covers saving copies to Drive or back to GitHub, and access to private repos.
  *Use in wiki:* Put an Open in Colab badge on every wiki notebook so students can run the full analysis (with Gemini in Colab) on Google's servers.
  Tools: Google Colab
  *Note:* Colab opens an editable copy and leaves the repo unchanged. Saving back to GitHub requires granting Colab permission to push commits. The notebook text was read from the raw.githubusercontent.com copy.

- [core] **[Quarto Live: interactive code blocks and exercises (webR and Pyodide)](https://r-wasm.github.io/quarto-live/)** (2024) — r-wasm project (Stagg, G.). *r-wasm.github.io*
  `package` · `intermediate` · `access: open` · `MIT`
  Quarto extension that adds editable, runnable R (webR) and Python (Pyodide) code blocks to HTML pages. It supports exercises with blanks, hints, solutions and custom grading, all running in the browser on any static host such as GitHub Pages.
  *Use in wiki:* Embed in-browser Python practice cells and auto-checked exercises in wiki pages so students can try code without Colab or a local install.
  Tools: quarto, pyodide, webR
  *Note:* The 0.1.1 announcement (https://tidyverse.org/blog/2024/10/quarto-live-0-1-1/, fetched) explains exercise, setup and check blocks. The repo (https://github.com/r-wasm/quarto-live, MIT) has no tagged releases and shows a 0.1.2-dev version. The docs site was rebuilt with Quarto 1.9.38 in 2026, but recent commit dates could not be confirmed, so treat it as early-stage (0.x). The community alternative coatless-quarto/pyodide (https://github.com/coatless-quarto/pyodide) itself points users to quarto-live as the official option.

- [recommended] **[marimo: reactive Python notebook (GitHub repository)](https://github.com/marimo-team/marimo)** (2026) — marimo team. *GitHub*
  `tool` · `intermediate` · `access: open` · `Apache-2.0` · `AI angle`
  Open-source reactive Python notebook stored as plain .py files. It has a built-in AI assistant that sees in-memory variables, Copilot completion, bring-your-own-key or local models, and 'marimo pair' for working alongside Claude Code, Codex or OpenCode.
  *Use in wiki:* Option for in-class vibe-coding activities: notebooks diff cleanly in Git and work with coding agents, and the same files export to WASM pages for the wiki.
  Tools: marimo, GitHub Copilot, Claude Code, Codex
  *Note:* 22.3k stars when fetched. The latest release number was not visible on the fetched page.

- [recommended] **[Pyodide changelog](https://pyodide.org/en/stable/project/changelog.html)** (2026) — Pyodide contributors. *pyodide.org*
  `package` · `advanced` · `access: open`
  Pyodide, CPython compiled to WebAssembly, is the engine under quarto-live, JupyterLite, marimo WASM and PyScript. The 314.x line (314.0.0 on 2026-06-09) runs Python 3.14, and 314.0.7 (2026-09-14) is the latest release.
  *Use in wiki:* Instructor-only reference for which Python version and package builds students get in any in-browser cell.
  Tools: pyodide, micropip
  *Note:* Version numbers jumped from 0.x (0.28 shipped Python 3.13) to 314.x. The changelog announces no policy, so the link to the Python version is my inference. 0.29.5 and 0.27.8 got Node 26 fixes in September 2026. Pure-Python wheels install through micropip.

- [optional] **[Binder (mybinder.org) user guidelines](https://mybinder.readthedocs.io/en/latest/about/user-guidelines.html)** (2026) — Binder Project. *mybinder.readthedocs.io*
  `documentation` · `intermediate` · `access: open`
  Free service that launches a GitHub repo of notebooks in a temporary cloud Jupyter session. Sessions get 1–2 GB of RAM, shut down after 10 minutes idle, last up to about 6 hours, and are capped at 100 simultaneous users per repository.
  *Use in wiki:* Fallback 'Launch Binder' button for notebooks that need packages Pyodide lacks. The 100-user cap and slow cold starts make it unreliable for a whole class at once.
  Tools: binder, thebe, repo2docker
  *Note:* The mybinder.org homepage says the service is 'currently in testing'. Thebe (https://github.com/jupyter-book/thebe, BSD-3-Clause, fetched) turns static code cells into runnable ones backed by a Jupyter server, or by JupyterLite through thebe-lite. Thebe 0.9.0 is still in development, and Jupyter Book 2 does not yet support editable Thebe cells.

- [optional] **[PyScript](https://pyscript.net/)** (2026) — PyScript Development Team (originated at Anaconda). *pyscript.net*
  `tool` · `advanced` · `access: open`
  Open-source platform for running Python inside web pages. The current release is 2026.7.3 (year-based version numbers), with docs at pyscript.github.io/docs/latest/.
  *Use in wiki:* Optional for hand-built plain-HTML widgets; for course notebooks, quarto-live, JupyterLite or marimo are more turnkey.
  Tools: pyscript, pyodide
  *Note:* The fetched homepage names neither its runtimes nor its license; check the docs before adopting.

## Interactive components

- [core] **[Illinois Chat (formerly UIUC.chat) documentation](https://docs.uiuc.chat/)** (2026) — University of Illinois (Center for AI Innovation GitHub organization). *docs.uiuc.chat*
  `tool` · `intro` · `access: free-registration` · `MIT (backend repo)` · `AI angle`
  Campus-supported platform for building course chatbots over uploaded materials (PDFs, slides, videos, a web crawl, or a Canvas connection). Answers cite their sources, and a tutor-mode prompt is available. The official instance is chat.illinois.edu.
  *Use in wiki:* Build a BADM 534 assistant grounded in the wiki by crawling the GitHub Pages site, and link it from every page.
  Tools: Illinois Chat, OpenAI API, Canvas
  *Note:* UIUC.chat is moving to chat.illinois.edu, and chatbot creation is disabled on the old site (https://docs.uiuc.chat/migration/migrate-to-illinois-chat.md, fetched). Per the FAQ it is free to use but you supply your own OpenAI API key, and data is stored on AWS with no guarantees; the FAQ may predate the campus migration. Privacy: there is no FERPA statement and no documented iframe embed, so keep student records and grades out of it. Backend: https://github.com/Center-for-AI-Innovation/ai-ta-backend (public, MIT); access to the frontend repo appears restricted. Support: genaisupport@mx.uillinois.edu.

- [core] **[MLU-Explain](https://mlu-explain.github.io/)** — Amazon Machine Learning University. *mlu-explain.github.io*
  `website` · `intro` · `access: open` · `CC BY-SA 4.0 (articles); modified MIT (sample code)`
  Interactive scrollytelling explainers covering linear and logistic regression, train/test/validation splits, cross-validation, precision and recall, ROC/AUC, decision trees, random forests, the bias-variance trade-off and double descent.
  *Use in wiki:* Link or assign from the M3 and M7 pages; also a model for the visual-explainer style the wiki could adopt.
  *Note:* The GitHub repo was archived (read-only) on 2026-03-06, so expect no more updates; the site still loads. The site lists 14 articles and the repo holds 10.

- [recommended] **[Pagefind](https://pagefind.app/)** (2026) — Pagefind contributors (originally CloudCannon). *pagefind.app*
  `tool` · `intermediate` · `access: open` · `MIT`
  Static search library that indexes the built HTML from any site generator and serves a chunked index. It claims a total payload under 300 kB for a full-text search of a 10,000-page site. The current version is 1.5.2.
  *Use in wiki:* Adds search to a plain-HTML or mixed-tool wiki; it is also Starlight's default search.
  Tools: pagefind
  *Note:* Repo: https://github.com/pagefind/pagefind (MIT). Lunr.js (https://github.com/olivernn/lunr.js, MIT, fetched) is the older in-browser alternative; it shows 105 open issues and recent activity could not be confirmed. Quarto and Jupyter Book 2 have built-in search, so Pagefind matters mainly for plain-HTML builds.

- [recommended] **[Quarto extensions listing: filters](https://quarto.org/docs/extensions/listing-filters.html)** (2026) — Posit (Quarto project). *quarto.org*
  `website` · `intro` · `access: open`
  Official directory of Quarto filter extensions. Quiz and exercise options include quizdown, shortiquiz, stepbystep (guided tasks with progress checkboxes) and assign (instructions paired with solutions).
  *Use in wiki:* Shortlist of self-check and exercise widgets to embed in module pages.
  Tools: quarto
  *Note:* Repos named in the listing: https://github.com/parmsam/quarto-quizdown, https://github.com/skyfroger/stepbystep and https://github.com/coatless-quarto/assign. I did not fetch these individually; check license and activity before adopting.

- [recommended] **[Seeing Theory](https://seeing-theory.brown.edu/)** — Kunin, D.; Guo, J.; Devlin, T. D.; Xiang, D. *Brown University*
  `website` · `intro` · `access: open`
  Brown University's D3-based visual introduction to probability and statistics. It runs from basic probability through distributions, frequentist and Bayesian inference, and regression.
  *Use in wiki:* Refresher links on the M3 (regression) and M6 (inference) pages for students who are rusty on statistics.
  Tools: d3
  *Note:* The site is now archived for reference. The page states no license. Source: https://github.com/seeingtheory/Seeing-Theory (license not checked).

- [recommended] **[shortiquiz: interactive quiz questions for Quarto HTML documents](https://github.com/skyfroger/shortiquiz)** — skyfroger. *GitHub*
  `package` · `intro` · `access: open` · `GPL-3.0`
  Quarto extension offering multiple-choice, multi-answer, text-input, dropdown, Parsons (reorder lines of code), image-hotspot, flashcard and gated-stage questions. Install with 'quarto add skyfroger/shortiquiz'.
  *Use in wiki:* Low-stakes self-checks at the end of each module page. Parsons problems suit code-reading practice for non-CS students checking AI-generated code.
  Tools: quarto
  *Note:* GPL-3.0 copyleft applies to the extension code shipped with the site. The repo has 59 commits; the last-commit date was not visible. Answers sit in the page source, so use it for ungraded practice only and keep graded quizzes in Canvas.

- [optional] **[CS50.ai (CS50 Duck)](https://cs50.ai/)** (2026) — Harvard CS50. *cs50.ai*
  `tool` · `intro` · `access: free-registration` · `AI angle`
  CS50's ChatGPT-based 'duck debugger' for students and teachers, supported by Microsoft and OpenAI. It is the best-known example of a course-specific AI tutor.
  *Use in wiki:* Instructor-only model for an AI-help policy and tutor design (guide students rather than solve for them).
  Tools: OpenAI
  *Note:* The fetched page describes neither its guardrails nor whether courses outside CS50 can use it. A CS50 team paper at SIGCSE 2024 describes the design, but I did not verify its URL.

- [optional] **[H5P](https://h5p.org/)** (2026) — H5P. *h5p.org*
  `tool` · `intermediate` · `access: freemium` · `MIT (core technology)`
  Open HTML5 framework (MIT) for interactive content such as interactive video, presentations and quiz-style games. The paid H5P.com service adds LTI integration with Canvas and other LMSs.
  *Use in wiki:* Optional for richer self-checks. On a static site, h5p-standalone (https://github.com/tunapanda/h5p-standalone, MIT, 3.x) plays .h5p packages without a server.
  Tools: H5P, h5p-standalone
  *Note:* Authoring needs an H5P-enabled platform or H5P.com. The paid Premium tier adds AI-powered 'Smart Import'. Content embedded in a GitHub Pages wiki sends no grades back, so keep graded quizzes in Canvas.

- [optional] **[Observable Framework](https://observablehq.github.io/framework/)** (2026) — Observable, Inc. *observablehq.github.io*
  `tool` · `advanced` · `access: open` · `ISC`
  Open-source static site generator for data apps, dashboards and reports. Pages are Markdown with reactive JavaScript, and data loaders written in Python, R or SQL snapshot the data at build time.
  *Use in wiki:* Option for interactive dashboards inside the wiki (for example a customer-segmentation explorer) where Python prepares the data at build time.
  Tools: observable-framework, javascript
  *Note:* v1.13.4 per the site. The docs now live at observablehq.github.io/framework, and observablehq.com/framework redirects there. No maintenance notice was seen, but check recent activity before committing. Repo: https://github.com/observablehq/framework (ISC).

- [optional] **[The Pudding](https://pudding.cool/)** (2026) — The Pudding. *pudding.cool*
  `website` · `intro` · `access: open`
  Digital publication of visual essays that explain ideas with data; still active, with new stories through October 2026.
  *Use in wiki:* Examples of data storytelling for the M2 Pyramid Principle and visualization module, and models for the team blog-post deliverable.
  *Note:* Whether the stories' code is open source was not verified.

- [optional] **[Distill Hiatus](https://distill.pub/2021/distill-hiatus/)** (2021) — Distill editorial team. *Distill*
  `blog` · `advanced` · `access: open` · `CC BY 4.0 (text and diagrams)`
  Distill, the interactive machine-learning journal, paused publication in July 2021. Its archive of interactive articles and its article template remain models for explorable explanations.
  *Use in wiki:* Instructor-only design inspiration for interactive figures; selected articles could be optional M7 reading.
  *Note:* The hiatus is open-ended, so expect no new articles. The Explorable Explanations hub (https://explorabl.es/, fetched) is a related source of interactive examples, though its subject listings did not render in the fetch.

## Accessibility

- [core] **[University of Illinois Minimum Digital Accessibility Standards](https://access.illinois.edu/ada/digital-accessibility-policy/minimum-standards/)** (2026) — University of Illinois Urbana-Champaign. *access.illinois.edu*
  `documentation` · `intro` · `access: open`
  Campus standard under the Digital Accessibility Policy (HR-86). Internally developed web content must meet the most recent recommended WCAG, currently 2.2 AA, use WAI-ARIA 1.2, and work with major browsers and screen readers. Course content and training materials are explicitly in scope.
  *Use in wiki:* The binding target for the BADM 534 wiki: design to WCAG 2.2 AA and test with NVDA and VoiceOver.
  *Note:* Commercial SaaS is held to 2.1 AA. Campus resources: instructor tips at https://itaccessibility.illinois.edu/tips-instructor and evaluation tools at https://itaccessibility.illinois.edu/web-evaluation-tools (links seen on itaccessibility.illinois.edu). The page lists no deadlines.

- [core] **[WCAG 2 Overview](https://www.w3.org/WAI/standards-guidelines/wcag/)** (2025) — W3C Web Accessibility Initiative. *W3C WAI*
  `documentation` · `intermediate` · `access: open`
  W3C overview of WCAG 2.0, 2.1 and 2.2 and the A, AA and AAA conformance levels. W3C recommends WCAG 2.2, which is backward compatible with 2.1 and is also published as ISO/IEC 40500:2025.
  *Use in wiki:* Instructor-only reference for setting the wiki's accessibility target.
  *Note:* WCAG 2.1 was last updated 2025-05-06, and WCAG 3 is still an early draft. UIUC's own standard requires 2.2 AA for internally built web content (see uiuc-minimum-digital-accessibility-standards).

- [core] **[ADA.gov fact sheet: Title II rule on web content and mobile app accessibility](https://www.ada.gov/resources/2024-03-08-web-rule/)** (2024) — U.S. Department of Justice, Civil Rights Division. *ADA.gov*
  `documentation` · `intro` · `access: open`
  The DOJ's ADA Title II rule requires web content from state and local governments, including public universities, to meet WCAG 2.1 AA. An April 2026 interim final rule moved compliance to 2027-04-26 for entities serving 50,000+ people and 2028-04-26 for smaller ones.
  *Use in wiki:* Instructor-only: a public-university course wiki should meet WCAG 2.1 AA by April 2027 at the latest.
  *Note:* The exceptions for archived content and individualized password-protected documents are narrow and don't cover public HTML course pages. This is a summary, not legal advice. The page title shown here is paraphrased.

- [core] **[WebAIM's WCAG 2 Checklist](https://webaim.org/standards/wcag/checklist)** (2024) — WebAIM (Utah State University). *WebAIM*
  `documentation` · `intro` · `access: open`
  Plain-language checklist of the WCAG 2.2 success criteria at levels A, AA and AAA, with filters for 2.0 and 2.1.
  *Use in wiki:* QA checklist to run before each module page goes live: alt text, captions, 4.5:1 contrast, keyboard access, real headings, a lang attribute, and reflow at 200% zoom.
  *Note:* Last updated 2024-06-20. Interactive widgets (quizzes, sliders, in-browser code editors) need separate keyboard and screen-reader testing.

## Exemplar course sites

- [recommended] **[Teaching and Learning with Jupyter](https://jupyter4edu.github.io/jupyter-edu-book/)** (2019) — Barba, L. A.; Barker, L. J.; Blank, D. S.; Brown, J.; Downey, A. B.; George, T.; Heagy, L. J.; Mandli, K. T.; Moore, J. K.; Lippert, D.; Niemeyer, K. E.; Watkins, R. R.; West, R. H.; Wickes, E.; Willing, C.; Zingale, M. *jupyter4edu (GitHub Pages)*
  `book` · `intro` · `access: open` · `CC BY 4.0`
  Open handbook on teaching with Jupyter. It includes a catalogue of 23 pedagogical patterns (for example 'Shift-Enter for the win', 'Fill in the blanks' and test-driven development) and practical chapters on running a class.
  *Use in wiki:* Instructor-only guide for structuring in-class coding activities and notebook exercises on the wiki.
  Tools: jupyter
  *Note:* Built with bookdown/GitBook rather than Jupyter Book. Written in 2019, before AI coding assistants.

- [recommended] **[Intermediate Quantitative Economics with Python](https://python.quantecon.org/intro.html)** — Sargent, T. J.; Stachurski, J. *QuantEcon*
  `course` · `advanced` · `access: open` · `CC BY-SA 4.0`
  QuantEcon's open course of 149 lectures, built with Jupyter Book and a QuantEcon theme. A 'Launch Notebook' button opens each lecture in Colab.
  *Use in wiki:* Model for lecture-as-webpage design with downloadable notebooks and one-click Colab launch.
  Tools: jupyter-book, quantecon-book-theme
  *Note:* Source is MyST Markdown (repo lecture-python.myst), and the Colab links point to a generated lecture-python.notebooks repo. Whether it has moved to Jupyter Book 2 was not confirmed.

- [recommended] **[UBC Master of Data Science: public course materials](https://github.com/UBC-MDS/public)** — UBC Master of Data Science. *GitHub*
  `course` · `intermediate` · `access: open` · `CC BY-SA 3.0 (unless otherwise noted)`
  Index of 25 UBC MDS courses (DSCI 511–591) linking to course repos: syllabi for all 25, lecture notes for 15 and labs for 7.
  *Use in wiki:* Mine the syllabi, lab structure and rubrics when designing programming assignments; also a model for an open course repo.
  *Note:* Related UBC exemplars: 'Data Science: A First Introduction with Python' (https://python.datasciencebook.ca/, CC BY-NC-SA 4.0, a Sphinx/Docutils site, probably Jupyter Book v1) and 'Programming in Python for Data Science' (https://prog-learn.mds.ubc.ca/, built on Ines Montani's Gatsby course-starter-python template, an older stack). The program site ubc-mds.github.io is built with Hugo.
