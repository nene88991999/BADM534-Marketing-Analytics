# AI-Assisted Coding · Tools and Workflows

72 resources (23 core). Built 2026-10-25 from `00_Index/_data/`; edit the YAML there and rerun `00_Index/_build/build_catalog.py` rather than editing this file.

Priority: **core** = likely to assign or build on; **recommended** = strong supplement; **optional** = background or niche. *Access* tells you whether students can open it without a login.

## Contents

- [Coding agents and assistants](#coding-agents-and-assistants) (14)
- [AI inside notebooks and data apps](#ai-inside-notebooks-and-data-apps) (11)
- [Student and education access](#student-and-education-access) (6)
- [Free courses](#free-courses) (7)
- [Standards: MCP, AGENTS.md, skills, context](#standards-mcp-agentsmd-skills-context) (10)
- [Workflows, prompting and verification](#workflows-prompting-and-verification) (11)
- [Security, privacy and risk](#security-privacy-and-risk) (11)
- [Python for marketing analytics: notebooks and code](#python-for-marketing-analytics-notebooks-and-code) (2)

## Coding agents and assistants

- [core] **[An important update: Transitioning Gemini CLI to Antigravity CLI](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli)** (2026) — Lyalin, D.; Mullen, T. (Google). *Google Developers Blog*
  `blog` · `intro` · `access: open` · `AI angle`
  Google announced on May 19, 2026 that on June 18, 2026 Gemini CLI and the Gemini Code Assist IDE extensions would stop serving Google AI Pro/Ultra subscribers and free individual users. Antigravity CLI, a new Go-based terminal agent that shares a harness with the Antigravity 2.0 desktop app, replaces them. Enterprise Code Assist customers keep Gemini CLI.
  *Use in wiki:* Use it as a dated warning on the tools page, and as an M8 example of how fast the AI tooling market shifts (tutorials from 2025 will mislead students).
  Tools: gemini-cli, antigravity
  *Note:* Antigravity CLI supports Agent Skills, hooks, subagents and plugins (formerly extensions), but did not launch with full Gemini CLI feature parity. The post does not state a free-tier limit.

- [core] **[Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)** (2026) — Anthropic. *code.claude.com*
  `documentation` · `intermediate` · `access: open` · `AI angle`
  Anthropic's guide to agentic coding. Topics: give Claude a check it can run (tests, scripts, screenshots); explore, then plan, then code (plan mode); write a short CLAUDE.md; manage context aggressively (/clear, /compact, subagents); use checkpoints and rewind; run a writer/reviewer pattern; avoid common failures such as the 'trust-then-verify gap'.
  *Use in wiki:* Assigned reading before the first vibe-coding lab. Turn its 'Avoid common failure patterns' list into a classroom checklist for AI-generated analysis code.
  Tools: claude-code
  *Note:* The old Anthropic Engineering post at https://www.anthropic.com/engineering/claude-code-best-practices now returns HTTP 302 to this docs page, so cite this URL. I did not re-verify the original post's publication date or byline.

- [core] **[Claude Code documentation: overview and quickstart](https://code.claude.com/docs/en/overview)** (2026) — Anthropic. *code.claude.com*
  `documentation` · `intro` · `access: open` · `AI angle`
  The official Claude Code docs. The quickstart covers the native installer (macOS, Linux, WSL, Windows), login, a first session, Git use, and essential commands. Claude Code also runs on the web, in a desktop app, in VS Code and JetBrains, in Slack, and in GitHub Actions.
  *Use in wiki:* Link it from the M1 setup page. Students install Claude Code and complete the quickstart's 'explore a repo, make a change, commit' loop on the course starter repo.
  Tools: claude-code, git
  *Note:* Quickstart fetched at https://code.claude.com/docs/en/quickstart.md; the overview link appears in it. Requires a paid Claude plan (Pro, Max, Team or Enterprise), a Console (API) account, or a cloud provider. The Free claude.ai plan does not include Claude Code (see claude-pricing-plans). The quickstart links free 'Claude Code 101' and other courses on Claude Academy. The full page index is at https://code.claude.com/docs/llms.txt.

- [core] **[Codex documentation: CLI, IDE extension, cloud, and app (ChatGPT Learn)](https://learn.chatgpt.com/docs)** (2026) — OpenAI. *learn.chatgpt.com*
  `documentation` · `intro` · `access: freemium` · `AI angle`
  Codex is OpenAI's coding agent. It runs in the ChatGPT desktop, web and mobile apps, as the Codex CLI (works on local files, scriptable with `codex exec`), as an IDE extension (VS Code, Cursor, Windsurf; JetBrains and Xcode integrations), and as Codex Cloud (remote tasks that end in a PR). It is included in every ChatGPT plan, Free through Enterprise.
  *Use in wiki:* Alternative agent for students who already pay for ChatGPT Plus. The Free plan gives limited Codex access for quick tasks.
  Tools: codex, chatgpt
  *Note:* developers.openai.com/codex now 302-redirects to learn.chatgpt.com/docs. Pricing (https://learn.chatgpt.com/codex/pricing, fetched 2026-10-23): Free $0 (limited); Go $8/month; Plus $20; Pro from $100 ($100/$200/$500); Business $20/user/month annual or $25 monthly; Edu and Enterprise by quote. CLI: https://learn.chatgpt.com/codex/cli; IDE: https://learn.chatgpt.com/codex/ide; Cloud: https://learn.chatgpt.com/codex/cloud. The CLI is open source (Apache-2.0) at https://github.com/openai/codex.

- [recommended] **[Build with AI in VS Code (agents, chat, MCP, customization)](https://code.visualstudio.com/docs/copilot/overview)** (2026) — Microsoft (VS Code). *code.visualstudio.com*
  `documentation` · `intro` · `access: freemium` · `AI angle`
  VS Code's AI hub: agents in the Chat view or Agents window (the Copilot harness, or Anthropic Claude and OpenAI Codex harnesses), model choice including your own API key or a local model, MCP servers, project instructions, agent skills, plugins, and permissions, approvals and terminal sandboxing.
  *Use in wiki:* Default free IDE for students not on Cursor. Link it from the M1 setup page along with the Python and Jupyter extensions.
  Tools: vscode, copilot, mcp
  *Note:* Agents overview: https://code.visualstudio.com/docs/agents/overview. MCP: https://code.visualstudio.com/docs/agent-customization/mcp-servers. Copilot setup: https://code.visualstudio.com/docs/setup/copilot (links from the fetched page). Notebooks: 'Jupyter Notebooks in VS Code' (https://code.visualstudio.com/docs/datascience/jupyter-notebooks, fetched) covers Variable Explorer, Data Viewer and export to .py, but does not describe Copilot in notebooks. Data Wrangler quick start: https://code.visualstudio.com/docs/datascience/data-wrangler-quick-start (link only).

- [recommended] **[Claude plans and pricing](https://claude.com/pricing)** (2026) — Anthropic. *claude.com*
  `website` · `intro` · `access: freemium` · `AI angle`
  As of 2026-10-23: Free $0 (no Claude Code); Pro $20/month monthly or $17/month billed annually, with Claude Code included in all paid plans; Max from $100/month (5x or 20x Pro usage); Team standard seats $20 (annual) or $25 (monthly), premium seats $100 or $125; Enterprise $20/seat/month plus usage at API rates.
  *Use in wiki:* Use it for the 'which tool should I pay for?' table on the M1 setup page.
  Tools: claude-ai, claude-code
  *Note:* The page mentions an Education plan for whole universities with 'discounted rates', but gives no price and no individual student discount.

- [recommended] **[Copilot agent mode in the IDE and Copilot cloud agent (formerly coding agent)](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/use-copilot-agents/use-agent-mode)** (2026) — GitHub. *GitHub Docs*
  `documentation` · `intermediate` · `access: freemium` · `AI angle`
  Agent mode takes a high-level task, picks which files to edit, makes the edits and runs commands (with approval) in VS Code, Visual Studio, JetBrains, Xcode and Eclipse. The cloud agent works in the background on GitHub repos and is started from issues, the mobile app, IDEs, the CLI, MCP or Slack/Jira/Linear, and returns a pull request.
  *Use in wiki:* Demo: assign a GitHub issue ('add a cohort-retention chart to the notebook') to the cloud agent and review the PR it opens in class.
  Tools: copilot, vscode, github
  *Note:* Cloud agent docs: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/start-copilot-sessions (fetched; 'available for all paid Copilot plans'). Tips: https://docs.github.com/en/copilot/tutorials/cloud-agent/get-the-best-results (link only).

- [recommended] **[Cursor plans and pricing (restructured October 2026)](https://cursor.com/pricing)** (2026) — Cursor (Anysphere). *cursor.com*
  `tool` · `intro` · `access: freemium` · `AI angle`
  An AI-first code editor (a VS Code fork) with agent, chat, tab completion, MCP and rules. As of 2026-10-23 the plans are Free (limited agent and chat requests), Plus $8/month (Grok models only), Premium $30 (4x Plus, cloud agents, third-party models billed at API list price), Super $100, Ultra $200, Teams $30+/user and Enterprise.
  *Use in wiki:* List it as an alternative IDE. Warn students that the cheap tier now uses only xAI Grok models and that Claude or GPT models cost extra.
  Tools: cursor
  *Note:* SHAKY, FAST-MOVING. SpaceX/xAI agreed to buy Anysphere for $60B (Techzine, June 16, 2026: https://www.techzine.eu/news/devops/142197/spacex-acquires-cursor-for-60-billion/, expected to close Q3 2026). PricingSaaS reports the rebuilt lineup around Oct 13-19, 2026 (https://pricingsaas.com/news/article/cursor-rebuilds-its-pricing-around-grok-and-x-with-plans-from-8-to-200); the old lineup was Individual $20 with Pro/Pro+/Ultra options and Teams $40. Cursor MCP docs: https://cursor.com/docs/context/mcp (link from the MCP docs; not opened).

- [recommended] **[GitHub Copilot plans (Free, Pro, Pro+, Max; usage-based AI credits)](https://github.com/features/copilot/plans)** (2026) — GitHub. *github.com*
  `tool` · `intro` · `access: freemium` · `AI angle`
  As of 2026-10-23: Free $0 (2,000 completions and 50 chat requests per month, limited agent use, Copilot CLI); Pro $10/month ($15 of AI credits); Pro+ $39 ($70); Max $100 ($200). Paid plans include unlimited completions, agent mode, the cloud agent and the CLI. Pro+ and Max can hand tasks to third-party agents (Claude, Codex).
  *Use in wiki:* Use it on the M1 tool-comparison table. The Free tier is enough for in-class completions inside VS Code or Codespaces.
  Tools: copilot, vscode
  *Note:* Usage-based billing started June 1, 2026 (GitHub blog, May 12, 2026: https://github.blog/news-insights/company-news/GitHub-copilot-individual-plans-introducing-flex-allotments-in-pro-and-pro-and-a-new-max-plan/). Copilot CLI docs: https://docs.github.com/en/copilot/how-tos/copilot-cli (link from a GitHub docs page; not opened).

- [recommended] **[Google Antigravity (agentic IDE, desktop app, CLI, SDK)](https://antigravity.google)** (2026) — Google. *antigravity.google*
  `tool` · `intermediate` · `access: freemium` · `AI angle`
  Google's agent-first development platform: Antigravity IDE (an agentic IDE with an agent manager and artifacts), the Antigravity App for coordinating multiple agents, a CLI (`agy`), extensions for VS Code, JetBrains, Visual Studio, Zed and Xcode, and a Python SDK. It supports SKILL.md skills, rules and MCP, with tool approval gates, a terminal sandbox and sandboxed browser automation.
  *Use in wiki:* Google's replacement for the free Gemini CLI path. The free individual tier makes it viable for students who have no paid subscription.
  Tools: antigravity
  *Note:* It exists (verified). Pricing (https://antigravity.google/pricing): Free individual tier ($0, a range of agent models, unlimited Tab completions, basic weekly rate limits); Google AI Pro and Ultra add higher limits and AI credits; business plans through Google Cloud. Docs: https://antigravity.google/docs/overview. Security: https://antigravity.google/docs/permissions/ and https://antigravity.google/docs/sandbox/. The docs page did not mention AGENTS.md. Desktop builds for macOS, Windows and Linux.

- [recommended] **[Use Claude Code in the cloud (Claude Code on the web) and the Claude Code desktop app](https://code.claude.com/docs/en/claude-code-on-the-web)** (2026) — Anthropic. *code.claude.com*
  `documentation` · `intro` · `access: freemium` · `AI angle`
  Cloud sessions run Claude Code on Anthropic-managed VMs. You start them from claude.ai/code in a browser, from the mobile app, from the desktop app's Code tab, or with `claude --cloud`. They clone a GitHub repository and can open pull requests. The desktop app (macOS, Windows, Linux beta) gives a graphical interface for parallel sessions, diff review and pull-request management.
  *Use in wiki:* A no-terminal on-ramp: students who struggle with local installs can run their project repo in a cloud session from a browser or the desktop app.
  Tools: claude-code, github
  *Note:* Cloud sessions are available on Pro, Max and Team plans, and for Enterprise users with premium seats or Chat + Claude Code seats. They share rate limits with other Claude usage, with no separate compute charge. Repo cloning and PRs require GitHub. Desktop docs: https://code.claude.com/docs/en/desktop (fetched). Before sharing a session publicly from a Pro or Max account, check it for credentials.

- [optional] **[Gemini CLI (google-gemini/gemini-cli) and docs](https://github.com/google-gemini/gemini-cli)** (2026) — Google. *GitHub*
  `tool` · `intermediate` · `access: freemium` · `Apache-2.0` · `AI angle`
  An open-source terminal agent for Gemini models, with GEMINI.md context files, MCP servers, extensions, sandboxing and trusted folders. The README still advertises a free tier (60 requests/minute and 1,000/day with a personal Google account), but see the notes.
  *Use in wiki:* Mention it as historical context only. Point students to Antigravity CLI or another tool instead (see gemini-cli-to-antigravity-transition).
  Tools: gemini-cli
  *Note:* IMPORTANT: The docs (https://geminicli.com/docs/) say 'Unpaid tier and Google One users: Gemini CLI was replaced by Antigravity CLI on June 18th, 2026.' The README's free-tier description looks out of date. Gemini CLI is still available through paid API keys and Gemini Code Assist Standard or Enterprise licenses. Free course: DeepLearning.AI 'Gemini CLI: Code & Create with an Open-Source Agent' (Jack Wotherspoon, Google; 1h23m, beginner; https://www.deeplearning.ai/short-courses/gemini-cli-code-and-create-with-an-open-source-agent/, fetched). It includes a data-analysis dashboard lesson that mixes local CSVs with cloud data, and the page now lists a 'Gemini CLI Deprecation for Free, Pro, and Ultra Users' reading.

- [optional] **[Jules: Google's asynchronous coding agent](https://jules.google)** (2026) — Google. *jules.google*
  `tool` · `intermediate` · `access: freemium` · `AI angle`
  An autonomous agent that clones a GitHub repo into a cloud VM, proposes a plan, and opens a PR for bug fixes, tests, version bumps or features. Plans: free (15 tasks/day, 3 concurrent), AI Pro (100/day), AI Ultra (300/day).
  *Use in wiki:* Optional comparison with Copilot's cloud agent and Codex Cloud: assign the same 'write unit tests for clv.py' issue to each and compare the PRs.
  Tools: jules, github
  *Note:* The fetched page listed Gemini 2.5 Pro and Gemini 3 Pro as the models, which may be out of date. App: https://jules.google.com/.

- [optional] **[Windsurf, now Devin Desktop (Cognition)](https://devin.ai/desktop)** (2026) — Cognition. *devin.ai*
  `tool` · `intro` · `access: freemium` · `AI angle`
  Windsurf, the agentic IDE, has been renamed Devin Desktop. It keeps the Windsurf IDE and adds an Agent Command Center for local and cloud agents. Plans: Free $0, Pro $20/month, Max $200, Teams $80/month plus $40 per seat, Enterprise.
  *Use in wiki:* Use it in M8 as a case on AI-tooling industry dynamics. The 2025 acquisition saga is a good IO discussion of acqui-hires and licensing.
  Tools: windsurf, devin
  *Note:* windsurf.com/editor 302-redirects here. ACQUISITION HISTORY: OpenAI's roughly $3B deal for Windsurf collapsed on July 11, 2025, and Google DeepMind hired CEO Varun Mohan, co-founder Douglas Chen and researchers under a nonexclusive technology license reported by Bloomberg at about $2.4B (TechCrunch, Maxwell Zeff, July 11, 2025: https://techcrunch.com/2025/07/11/windsurfs-ceo-goes-to-google-openais-acquisition-falls-apart/). Cognition then signed a definitive agreement to acquire Windsurf's IP, product, brand and employees (Cognition blog, July 14, 2025: https://cognition.com/blog/windsurf, redirected from cognition.ai). The Windsurf JetBrains plugin is still available.

## AI inside notebooks and data apps

- [core] **[Create and edit files with Claude (code execution and file creation)](https://support.claude.com/en/articles/12111783)** (2026) — Anthropic (Claude Help Center). *support.claude.com*
  `documentation` · `intro` · `access: freemium` · `AI angle`
  Claude can run code in a sandbox to analyze uploaded CSV/TSV files (up to 30 MB) and create Excel, PowerPoint, Word, PDF, Python and PNG chart outputs. The feature is available on Free, Pro, Max, Team and Enterprise, across web, desktop and mobile.
  *Use in wiki:* The zero-install option for M1/M2 labs: students upload a sample customer CSV, ask for an RFM table and chart, then download and inspect the Python that produced it.
  Tools: claude-ai, python
  *Note:* On by default on Free, Pro and Max, with network egress on. The article warns about prompt injection through hidden instructions in files or websites, and notes that file creation uses more of the plan's usage. The older URL support.anthropic.com/en/articles/12111783-create-and-edit-files-with-claude appeared in search results. Hands-on review: Simon Willison, 'My review of Claude's new Code Interpreter, released under a very confusing name' (September 9, 2025; https://simonwillison.net/2025/Sep/9/claude-code-interpreter, fetched). He found a Python/Node sandbox with about 9 GB RAM and PyPI installs, needed several rounds of prompting for a usable chart, and planned to avoid using it with data he would not want leaked. A good short M2 reading.

- [core] **[Data analysis with ChatGPT](https://help.openai.com/en/articles/8437071-data-analysis-with-chatgpt)** (2026) — OpenAI Help Center. *help.openai.com*
  `documentation` · `intro` · `access: freemium` · `AI angle`
  ChatGPT analyzes uploaded spreadsheets (.xls, .xlsx, .csv), PDFs and text or data files (JSON, XML, YAML) in a Python environment with no internet access. Availability and limits depend on model, plan and workspace settings.
  *Use in wiki:* Parallel to the Claude file-creation lab: students run the same RFM or segmentation prompt in both tools and compare the code and numbers each produces.
  Tools: chatgpt, python
  *Note:* The article does not list plans per feature. It warns that large or complex files may not be fully analyzed, which is a good prompt to teach 'check the row count'.

- [core] **[Google Colab: AI-powered notebooks (Gemini in Colab)](https://developers.google.com/colab)** (2026) — Google. *developers.google.com*
  `tool` · `intro` · `access: freemium` · `AI angle`
  Colab's landing page presents it as an AI coding assistant. Gemini generates, explains, debugs, refactors and documents code from plain-language prompts, and 'autonomous analysis' generates and runs code to answer questions about data. Pro and Pro+ add compute and background execution.
  *Use in wiki:* Default environment for in-class labs. The wiki can link 'Open in Colab' badges for every notebook, with Gemini as the built-in assistant.
  Tools: colab, gemini
  *Note:* colab.google now 302-redirects here. Try AI-first Colab at https://colab.new/ (link only). Teaching posts: https://medium.com/google-colab/tagged/education (link only). Colab AI features require age 18+ and may vary by locale (see colab-faq-ai-privacy).

- [core] **[Data Science Agent in Colab: The future of data analysis with Gemini](https://developers.googleblog.com/en/data-science-agent-in-colab-with-gemini/)** (2025) — Fine, J.; Kolla, M.; Soloducho, I. (Google). *Google Developers Blog*
  `blog` · `intro` · `access: open` · `AI angle`
  Announces Colab's Data Science Agent. You upload a data file and describe a goal in the Gemini side panel, and the agent generates a complete, executable notebook (imports, loading, cleaning, plots). The post warns that the agent may make mistakes and cites a 4th-place finish on the DABStep data-agent benchmark.
  *Use in wiki:* Demo in M2 or M3: students let the agent build a first-pass EDA or regression notebook, then audit every cell for correctness.
  Tools: colab, gemini, pandas
  *Note:* Published March 3, 2025. At launch it was for users 18+ in select countries. On the current Colab page this capability appears as 'autonomous analysis'. Benchmark: https://huggingface.co/spaces/adyen/DABstep (link only).

- [recommended] **[Jupyter AI (jupyterlab/jupyter-ai) v3](https://github.com/jupyterlab/jupyter-ai)** (2026) — Project Jupyter. *GitHub / Read the Docs*
  `package` · `intermediate` · `access: open` · `BSD-3-Clause` · `AI angle`
  An open-source JupyterLab extension that connects AI agents (Claude, Codex, GitHub Copilot, Goose, Kiro, Mistral Vibe, OpenCode and others) to notebooks through the Agent Client Protocol. A built-in Jupyter MCP server lets agents edit and run cells, and a permission system asks before any write or command.
  *Use in wiki:* For students on local JupyterLab: shows agents working inside the notebook with approval prompts, in contrast with copy-pasting into chat.
  Tools: jupyterlab, jupyter-ai, mcp
  *Note:* Docs: https://jupyter-ai.readthedocs.io/en/stable/ (v3.2.0). The older v2 docs, with %%ai magics and provider-based chat, are at https://jupyter-ai.readthedocs.io/en/v2/.

- [recommended] **[marimo: generate notebooks with AI (built-in assistant, marimo pair, text-to-notebook)](https://docs.marimo.io/guides/generate_with_ai/)** (2026) — marimo. *docs.marimo.io*
  `documentation` · `intermediate` · `access: open` · `AI angle`
  Three AI routes in the reactive marimo notebook: (1) 'marimo pair', which lets agent CLIs such as Claude Code, Codex or OpenCode read variables and run or edit cells in a live notebook; (2) the editor's assistant (chat in Manual, Ask, Agent and Code modes; cell generation; inline completion; providers OpenAI, Anthropic, Google, Copilot, Bedrock, Ollama); and (3) `marimo new PROMPT` to generate a whole notebook.
  *Use in wiki:* Recommended for the notebook-vs-script lesson. marimo notebooks are plain .py files, which diff cleanly in Git and are easy for agents to edit.
  Tools: marimo, claude-code, codex
  *Note:* Editor assistant: https://docs.marimo.io/guides/editor_features/ai_completion/ (fetched). marimo pair: https://docs.marimo.io/guides/generate_with_ai/marimo_pair/ (link). The agents panel is experimental.

- [recommended] **[Posit Assistant in Positron (replaces Positron Assistant and Databot)](https://positron.posit.co/assistant.html)** (2026) — Posit. *positron.posit.co*
  `tool` · `intermediate` · `access: freemium` · `AI angle`
  Positron, Posit's data-science IDE, ships Posit Assistant as its default AI experience from Positron 2026.07, replacing Positron Assistant and Databot. It uses session context (loaded data, plots, console history, variable types) for EDA, cleaning, modeling and app building in R and Python, and includes skills such as shiny-bslib, quarto-authoring and predictive-modeling-r.
  *Use in wiki:* Best fit for students using R alongside Python. Demo how session-aware context (it 'sees' the data frame) changes the quality of AI-generated analysis code.
  Tools: positron, r, python
  *Note:* Positron Assistant and Databot are marked deprecated (Databot page: https://positron.posit.co/databot.html). Bring-your-own-key: Anthropic, Amazon Bedrock, GitHub Copilot or OpenAI, or Posit AI Pass (whether AI Pass costs money was not stated). No student offer. Docs: https://assistant.posit.co/docs/getting-started/. Provider privacy: https://positron.posit.co/assistant-provider-info.html.

- [optional] **[Julius AI](https://julius.ai)** (2026) — Julius AI. *julius.ai*
  `tool` · `intro` · `access: freemium` · `AI angle`
  A chat-first AI workspace for analyzing uploaded data and producing charts, dashboards, presentations and reports, with connectors to Google Drive, OneDrive and SharePoint.
  *Use in wiki:* Use it as a contrast case: compare a no-code AI analysis app's output with code-first analysis (Colab plus agent), with emphasis on transparency and reproducibility.
  Tools: julius
  *Note:* Pricing (https://julius.ai/pricing, 2026-10-23): Free (daily credits, 'Julius Lite' models); Plus $20/month ($16 annual, 2,000 credits); Pro $45 ($37); Business $450 ($375); Enterprise custom. No student discount listed. The pricing page does not say whether user data trains models (it cites SOC 2 Type II). A similar tool: Deepnote's Education plan (https://deepnote.com/education, fetched) is free with a school email but excludes Deepnote AI.

- [optional] **[Lovable (AI full-stack web app builder)](https://docs.lovable.dev/introduction)** (2026) — Lovable. *lovable.dev*
  `tool` · `intro` · `access: freemium` · `AI angle`
  Builds and deploys web apps (frontend, backend, database, auth) from natural-language prompts, with editable code synced to GitHub, GitLab or Bitbucket. Pricing is credit-based.
  *Use in wiki:* Option for teams building an interactive companion app, such as a CLV calculator, for their project.
  Tools: lovable
  *Note:* Student discount (https://lovable.dev/students): 50% off Pro for up to 12 months ($12.50 instead of $25/month, 100 credits/month), verified with a school email and no card required. The pricing page did not show free-plan limits when fetched.

- [optional] **[Replit Agent](https://docs.replit.com/replitai/agent)** (2026) — Replit. *docs.replit.com*
  `tool` · `intro` · `access: freemium` · `AI angle`
  A browser-based AI builder that turns plain-language descriptions into deployed apps, data visualizations and slides. It plans, writes code, sets up infrastructure and tests, with a Plan mode for reviewing the task list first. Free Mode covers everyday use, and paid Power and Max modes handle harder work.
  *Use in wiki:* For teams that want an interactive dashboard to accompany their blog post without managing hosting.
  Tools: replit
  *Note:* Pricing (https://replit.com/pricing, 2026-10-23): Core $20/month ($18 annual), Pro $100 ($90), Enterprise custom. Free or Starter details were not stated clearly on the pricing page. No education offer listed.

- [optional] **[v0 by Vercel](https://v0.app/docs)** (2026) — Vercel. *v0.app*
  `tool` · `intro` · `access: freemium` · `AI angle`
  An AI agent that builds landing pages, dashboards and full-stack apps (Next.js, Tailwind, shadcn/ui) from prompts or mockups, with one-click deploy to Vercel and GitHub sync.
  *Use in wiki:* For students who want a polished front-end dashboard for project results.
  Tools: v0, nextjs
  *Note:* Pricing (https://v0.app/pricing, 2026-10-23): Free (7 messages/day, deploy, GitHub sync); Plus $30/user/month; Business $100/user/month (training opt-out by default); Enterprise custom. Note that the free and Plus tiers do not opt out of training by default. A similar builder: Bolt.new by StackBlitz (https://bolt.new, fetched) builds websites and apps from chat, with Bolt Cloud hosting, databases and auth. Its landing page says 'start for free' but lists no limits or prices.

## Student and education access

- [core] **[Access GitHub Copilot for free as a student (Copilot Student plan)](https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-for-students)** (2026) — GitHub. *GitHub Docs*
  `documentation` · `intro` · `access: free-registration` · `AI angle`
  Verified GitHub Education students activate the free 'Copilot Student' plan from their education benefits settings, and eligibility is rechecked monthly. This is no longer 'free Copilot Pro'. Since March 12, 2026 students cannot hand-pick premium models such as Claude Opus/Sonnet or GPT-5.x. Since June 1 the plan includes 200 monthly AI credits plus unlimited completions. Since June 24 auto model selection is the only option.
  *Use in wiki:* Use it for the step-by-step setup on day one, and correct the outdated 'free Copilot Pro for students' claim found in many 2025 guides.
  Tools: copilot
  *Note:* Change log: GitHub Community discussion #189268 'Important Updates to GitHub Copilot for Students' (March 11, 2026, with later updates): https://github.com/orgs/community/discussions/189268. Students can upgrade to Pro or Pro+ and keep their other Pack benefits. Docs say the cloud agent is 'available for all paid Copilot plans', and I could not confirm whether the Student plan includes it. Instructors: GitHub docs page 'Access Copilot Pro for free as a teacher or open source maintainer' (https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-for-teachers-and-os-maintainers) appeared in search results. Apply: https://docs.github.com/en/education/about-github-education/github-education-for-students/apply-to-github-education-as-a-student.

- [core] **[Google AI Pro for students (free for 1 year)](https://gemini.google/students/)** (2026) — Google. *gemini.google*
  `website` · `intro` · `access: free-registration` · `AI angle`
  As of 2026-10-23: eligible US college students aged 18+ get Google AI Pro free for one year (higher Gemini limits, 5 TB storage and other features) if they redeem by December 31, 2026. Eligibility is verified each year. A payment method is required, and the plan auto-renews at $19.99/month unless cancelled.
  *Use in wiki:* Day-one setup: remind students to set a calendar reminder to cancel before the renewal charge. AI Pro also raises Antigravity and Jules limits.
  Tools: gemini, antigravity, jules
  *Note:* The page does not mention NotebookLM, Jules or Colab. Students whose 2025 AI Pro trial expired can re-qualify.

- [recommended] **[Claude for Education (Claude for higher education)](https://claude.com/solutions/education)** (2026) — Anthropic. *claude.com*
  `website` · `intro` · `access: paid` · `AI angle`
  Anthropic's higher-education offering is a university-wide plan bought by institutions. Students cannot sign up individually. It includes learning mode, which tutors Socratically, and points students to a free 'AI Fluency for students' course.
  *Use in wiki:* State plainly on the wiki that UIUC does not list Claude among its approved AI apps, so students would use personal Free or Pro accounts. Pair this with the privacy guidance.
  Tools: claude-ai
  *Note:* anthropic.com/education 302-redirects here. Original announcement: https://www.anthropic.com/news/introducing-claude-for-education (April 2, 2025), which describes learning mode, campus-wide agreements (Northeastern, LSE, Champlain), Campus Ambassadors and API credits for student builders. The current page does not mention API credits or a student discount. See uiuc-genai-approved-apps. Free student course: 'AI Fluency for students' on Anthropic Academy (https://anthropic.skilljar.com/ai-fluency-for-students; from the catalog listing, not opened), suitable as pre-course homework for non-CS students.

- [recommended] **[GitHub Education and the Student Developer Pack](https://github.com/education)** (2026) — GitHub. *github.com*
  `website` · `intro` · `access: free-registration` · `AI angle`
  GitHub Education gives verified students free professional tools, including GitHub Copilot Student and Codespaces, plus the Student Developer Pack's dozens of partner offers (cloud hosting, developer platforms, learning content).
  *Use in wiki:* Day-one onboarding: every student applies for GitHub Education, since the course already requires GitHub for project code.
  Tools: github, copilot, codespaces
  *Note:* Pack: https://education.github.com/pack. Students page: https://github.com/education/students. Both links came from the fetched page and were not opened. Partner offers change often.

- [optional] **[ChatGPT Edu (ChatGPT for education)](https://chatgpt.com/business/education/)** (2026) — OpenAI. *chatgpt.com*
  `website` · `intro` · `access: paid` · `AI angle`
  A campus-licensed ChatGPT workspace with the flagship model, data analysis, custom GPTs, an admin console and SSO. OpenAI states that Edu data and conversations are not used for training. It is sold to institutions through sales, with no individual student offer on the page.
  *Use in wiki:* Explain to students why institutional licenses differ from personal accounts. At UIUC the related 'Illinois ChatGPT' license is for faculty and staff only.
  Tools: chatgpt
  *Note:* Launch post (May 30, 2024): https://openai.com/index/introducing-chatgpt-edu/. The page does not say whether Edu includes Codex, but the Codex pricing page lists Edu among the plans that include it. chatgpt.com/students could not be fetched (client error), so I could not verify any current consumer student offer.

- [optional] **[Cursor for Students](https://www.cursor.com/students)** (2026) — Cursor (Anysphere). *cursor.com*
  `website` · `intro` · `access: freemium` · `AI angle`
  Cursor's student page currently says anyone can start free, with upgrades offered through promotions at campus and online events 'this fall' and a campus newsletter. It does not describe a standing free-Pro-for-students offer, a duration, eligibility or verification.
  *Use in wiki:* Tell students not to count on free Cursor Pro. The Free plan or other tools are the safe default.
  Tools: cursor
  *Note:* In 2025 Cursor offered one year of free Pro to verified university students (Cursor forum threads such as https://forum.cursor.com/t/major-bug-verified-students-get-one-year-of-free-cursor-pro/88376 appeared in search results). The current page no longer describes that offer, so treat it as ended or changed.

## Free courses

- [core] **[Claude Code in Action (Anthropic Academy)](https://anthropic.skilljar.com/claude-code-in-action)** (2026) — Anthropic. *Anthropic Academy (Skilljar)*
  `course` · `intermediate` · `access: free-registration` · `AI angle`
  A free self-paced course on running longer, less-supervised Claude Code sessions. Lessons: steering long sessions, a CLAUDE.md the agent actually follows, verification skills, permission modes, hooks, routines and headless runs, GitHub Actions code review, verifying unsupervised runs, and plugins. Ends with a quiz.
  *Use in wiki:* Optional certificate-style module after students finish the basics; its 'verifying unsupervised runs' lesson fits the course's emphasis on checking AI-generated analysis.
  Tools: claude-code
  *Note:* Marked 'Register | FREE'. The page gives no duration and does not confirm a certificate. The beginner course 'Claude Code 101' is at https://anthropic.skilljar.com/claude-code-101 (catalog listing; also linked from the Claude Code quickstart as academy.claude.com/courses/claude-code-101).

- [core] **[Claude Code: A Highly Agentic Coding Assistant (DeepLearning.AI)](https://www.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant)** (2025) — Schoppik, E. (Anthropic). *DeepLearning.AI*
  `course` · `intermediate` · `access: free-registration` · `AI angle`
  A 2-hour course (10 video lessons) built with Anthropic: exploring, testing, refactoring and debugging codebases; MCP servers (Playwright, Figma); CLAUDE.md, context management, planning, subagents, worktrees, GitHub integration and hooks. Projects include refactoring a Jupyter notebook into a dashboard.
  *Use in wiki:* Core assigned course. The notebook-to-dashboard project maps directly onto the M2 visualization module.
  Tools: claude-code, mcp, jupyter
  *Note:* Fetched via https://www.deeplearning.ai/short-courses/claude-code-a-highly-agentic-coding-assistant/, which declares this canonical URL. Prerequisites: Python and Git. Free 'for a limited time during the platform beta'; graded work needs Pro. Year approximate (2025).

- [recommended] **[Agent Skills with Anthropic (DeepLearning.AI)](https://www.deeplearning.ai/short-courses/agent-skills-with-anthropic/)** (2026) — Schoppik, E. (Anthropic). *DeepLearning.AI*
  `course` · `intro` · `access: free-registration` · `AI angle`
  A 2h19m beginner course: skill folder structure and SKILL.md, progressive disclosure, how skills compare with tools, MCP and subagents, pre-built skills (Excel, PowerPoint, skill creation), custom skills, and using skills across Claude.ai, Claude Code, the API and the Agent SDK.
  *Use in wiki:* Assign it before students write a team analysis skill.
  Tools: claude-code, claude-ai
  *Note:* The page does not state a price; quizzes and certificates need DeepLearning.AI Pro. Year inferred (late 2025 or 2026), not confirmed on the page.

- [recommended] **[Generative AI for Beginners (21 lessons)](https://github.com/microsoft/generative-ai-for-beginners)** (2026) — Microsoft. *GitHub*
  `course` · `intro` · `access: open` · `MIT` · `AI angle`
  A free 21-lesson course with Python and TypeScript samples on LLM fundamentals, prompt engineering, text generation, chat, RAG, function calling (lesson 11) and AI agents (lesson 17). The repo has about 122k stars.
  *Use in wiki:* Background for M5 and M7. Embed or adapt the prompt-engineering and function-calling lessons as optional readings.
  Tools: python, openai, azure-openai
  *Note:* The repo is large (translations and images), so clone with --depth 1 or a sparse checkout of the needed lesson folders rather than mirroring everything. It does not cover AI coding tools or MCP; Microsoft has a separate 'MCP for Beginners' course, which I did not verify. Many samples assume Azure OpenAI or GitHub Models.

- [recommended] **[Getting Started with GitHub Copilot (GitHub Skills exercise)](https://github.com/skills/getting-started-with-github-copilot)** (2026) — GitHub. *GitHub Skills*
  `course` · `intro` · `access: open` · `MIT` · `AI angle`
  A free, under-an-hour exercise that runs in a preconfigured Codespace. Students use Copilot to explain, write, plan and develop code while updating a sample school-activities website.
  *Use in wiki:* Optional pre-lab. Students who finish it arrive knowing Copilot chat, inline suggestions and Codespaces.
  Tools: copilot, codespaces
  *Note:* skills.github.com now redirects to GitHub Learn (https://learn.github.com/skills). Codespaces usage on private repos uses Actions or Codespaces minutes. Other Copilot exercises in the org (https://github.com/skills, fetched; licenses not checked one by one): build-applications-w-copilot-agent-mode, expand-your-team-with-copilot (coding agent), integrate-mcp-with-copilot, customize-your-github-copilot-experience, test-and-debug-with-github-copilot, and idea-to-merge-with-the-copilot-app. Each lives at github.com/skills/<name>, and test-and-debug fits the course's verification theme.

- [recommended] **[Vibe Coding 101 with Replit (DeepLearning.AI)](https://www.deeplearning.ai/short-courses/vibe-coding-101-with-replit/)** (2025) — Catasta, M.; Palmer, M. (Replit). *DeepLearning.AI*
  `course` · `intro` · `access: free-registration` · `AI angle`
  A 1h34m beginner course: principles of agentic coding (one task at a time, fresh sessions per feature), PRDs and wireframes as prompts, building and deploying two apps, debugging, persistent storage, and reviewing what the agent built.
  *Use in wiki:* Good first exposure for non-CS students. Its 'review what the agent built' habit sets up the verification lessons.
  Tools: replit
  *Note:* Year approximate (2025). Free 'for a limited time during the platform beta'. Certificate needs Pro.

- [optional] **[Build Apps with Windsurf's AI Coding Agents (DeepLearning.AI)](https://www.deeplearning.ai/short-courses/build-apps-with-windsurfs-ai-coding-agents/)** (2025) — Ramachandran, A. (Codeium/Windsurf). *DeepLearning.AI*
  `course` · `intro` · `access: free-registration` · `AI angle`
  A 1h30m beginner course on agentic IDE workflows: multi-file edits, debugging and auto-fixing tests, how agents use tools and context, upgrading legacy code, and building a Wikipedia data-analysis app with caching and visualization.
  *Use in wiki:* Optional. Its agent concepts transfer to any IDE, though the product is now Devin Desktop.
  Tools: windsurf
  *Note:* Year approximate (2025). Free access 'for a limited time during the platform beta'. Graded items need Pro.

## Standards: MCP, AGENTS.md, skills, context

- [core] **[AGENTS.md: a simple, open format for guiding coding agents](https://agents.md)** (2026) — Agentic AI Foundation (Linux Foundation); originally OpenAI Codex, Amp, Google Jules, Cursor, Factory. *agents.md*
  `website` · `intro` · `access: open` · `AI angle`
  AGENTS.md is a plain-Markdown 'README for agents' with no required fields. Codex, Jules, Gemini CLI, Cursor, VS Code, GitHub Copilot coding agent, Windsurf, Zed, Aider and others read it. The Agentic AI Foundation now stewards it.
  *Use in wiki:* Have each team commit an AGENTS.md (with a CLAUDE.md that points to it) so the project works the same whether a teammate uses Claude Code, Codex, Copilot or Cursor.
  Tools: codex, claude-code, copilot, cursor, gemini-cli
  *Note:* Repo: https://github.com/agentsmd/agents.md (link from the site). Codex docs on how AGENTS.md files are discovered and merged: https://learn.chatgpt.com/codex/agent-configuration/agents-md. Claude Code reads AGENTS.md (see claude-code-memory-claude-md).

- [core] **[How Claude remembers your project (CLAUDE.md, AGENTS.md, auto memory)](https://code.claude.com/docs/en/memory)** (2026) — Anthropic. *code.claude.com*
  `documentation` · `intermediate` · `access: open` · `AI angle`
  Explains CLAUDE.md files at project, user and organization scope, .claude/rules/ for rules scoped to file types, and auto memory, which holds notes Claude writes itself. It states that Claude Code can read a repository's AGENTS.md in place of CLAUDE.md.
  *Use in wiki:* Give every team a starter CLAUDE.md/AGENTS.md for the semester project (data paths, 'never print raw customer rows', test command), and use this page to explain how it works.
  Tools: claude-code
  *Note:* These instructions are advisory context, not enforced configuration. For hard rules the docs point to hooks (for example a PreToolUse hook).

- [core] **[What is the Model Context Protocol (MCP)? (official docs)](https://modelcontextprotocol.io/docs/getting-started/intro)** (2026) — Model Context Protocol project. *modelcontextprotocol.io*
  `documentation` · `intro` · `access: open` · `AI angle`
  MCP is an open-source standard for connecting AI applications to external data, tools and workflows, described as 'a USB-C port for AI applications'. Claude, ChatGPT, VS Code, Cursor and others support it. The docs cover building servers and clients and MCP Apps. The current docs version is dated 2026-07-28.
  *Use in wiki:* Concept page: show how an agent could query a course SQL database or Google Drive through MCP instead of students pasting data into chat.
  Tools: mcp, claude-code, vscode, cursor
  *Note:* Anthropic's launch post (November 25, 2024): https://www.anthropic.com/news/model-context-protocol. MCP is now listed as a project of the Agentic AI Foundation, under the Linux Foundation (https://aaif.io). Free courses: DeepLearning.AI 'MCP: Build Rich-Context AI Apps with Anthropic' (https://www.deeplearning.ai/courses/mcp-build-rich-context-ai-apps-with-anthropic) and Anthropic Academy 'Introduction to Model Context Protocol' (https://anthropic.skilljar.com/introduction-to-model-context-protocol); both URLs came from catalog listings. Claude Code MCP setup: https://code.claude.com/docs/en/mcp. Security: the MCP Security Best Practices page (https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md, fetched) covers confused deputy, token passthrough, SSRF and local-server compromise; its local-server section is a good warning against installing random MCP servers. Governance: the Agentic AI Foundation (https://aaif.io, fetched) hosts MCP, AGENTS.md, Agent Skills, A2A, goose and others.

- [core] **[Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)** (2025) — Rajasekaran, P.; Dixon, E.; Ryan, C.; Hadfield, J. (Anthropic Applied AI). *Anthropic Engineering*
  `blog` · `intermediate` · `access: open` · `AI angle`
  Argues that for multi-turn agents the job shifts from wording prompts to curating 'the smallest useful set of tokens' in a limited context window. Covers system prompts, tools, examples, retrieval at run time, compaction, structured note-taking and sub-agents.
  *Use in wiki:* Canonical source for the wiki's 'context engineering' concept page. It explains why students should give the agent a data dictionary rather than paste in a 100k-row CSV.
  Tools: claude-code
  *Note:* Published September 29, 2025.

- [recommended] **[Agent Skills: open format specification](https://agentskills.io/)** (2026) — Agent Skills project (originally Anthropic). *agentskills.io*
  `website` · `intermediate` · `access: open` · `AI angle`
  The canonical site for the open Agent Skills format: a skill is a folder with a SKILL.md (name and description at minimum) plus optional scripts/, references/ and assets/. It explains progressive disclosure (discovery, activation, execution) and links the specification, a quickstart and a list of client tools that support skills.
  *Use in wiki:* Cite it as the vendor-neutral definition of a skill. The same skill folder works across Claude Code, Antigravity, VS Code and other compatible agents.
  Tools: claude-code, antigravity, vscode
  *Note:* Spec and discussion repo: https://github.com/agentskills/agentskills (link seen on the page; I did not check its license). Agent Skills is now listed as a project of the Agentic AI Foundation (https://aaif.io), which also hosts MCP and AGENTS.md.

- [recommended] **[Extend Claude with skills (Claude Code docs)](https://code.claude.com/docs/en/skills)** (2026) — Anthropic. *code.claude.com*
  `documentation` · `intermediate` · `access: open` · `AI angle`
  A skill is a SKILL.md file with YAML frontmatter and markdown instructions, kept in ~/.claude/skills/, .claude/skills/, a plugin, or synced from claude.ai. Claude loads skills automatically when relevant, or you call one with /skill-name. Claude Code skills follow the open Agent Skills standard and add extensions.
  *Use in wiki:* Demo: the instructor ships a course skill (for example 'marketing-analysis-checks', which runs assertions and reproduces headline numbers) in the starter repo so every student's agent follows the same verification routine.
  Tools: claude-code
  *Note:* Anthropic Academy also runs a free 'Introduction to agent skills' course at https://anthropic.skilljar.com/introduction-to-agent-skills (seen on the Skilljar catalog; I did not open the course page itself).

- [recommended] **[GitHub Spec Kit: toolkit for spec-driven development](https://github.com/github/spec-kit)** (2026) — GitHub. *GitHub*
  `tool` · `intermediate` · `access: open` · `MIT` · `AI angle`
  An open-source toolkit that runs inside an agent's chat as /speckit-* skills: constitution (project principles), specify, plan, tasks, implement and converge, plus optional bug-fix and idea-assessment extensions. It turns 'vibe coding' into a spec, then plan, then tasks, then implement workflow.
  *Use in wiki:* Use it for the team project kickoff: students write a constitution and spec for their analytics blog post before any code is generated.
  Tools: spec-kit, copilot, claude-code
  *Note:* Docs: https://github.github.io/spec-kit/. The README examples use Copilot, and other agents plug in through an integration key. I could not verify a GitHub blog post on spec-driven development because the search budget ran out.

- [recommended] **[Spec-Driven Development with Coding Agents (DeepLearning.AI short course)](https://www.deeplearning.ai/courses/spec-driven-development-with-coding-agents)** (2026) — Everitt, P. (JetBrains). *DeepLearning.AI*
  `course` · `intro` · `access: free-registration` · `AI angle`
  A 1h16m beginner course: compares vibe coding with spec-driven development, then covers writing project constitutions and feature specs, a plan-implement-verify loop, replanning, building an MVP, applying the method to legacy code, and packaging the workflow as an agent skill.
  *Use in wiki:* Assign it before the project proposal milestone.
  Tools: coding-agents
  *Note:* Last updated April 18, 2026. The page does not say whether viewing is free; quizzes, graded work and certificates need DeepLearning.AI Pro.

- [recommended] **[Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)** (2025) — Zhang, B.; Lazuka, K.; Murag, M. (Anthropic). *Anthropic Engineering*
  `blog` · `intermediate` · `access: open` · `AI angle`
  Introduces Agent Skills: folders of instructions, scripts and resources that agents load through progressive disclosure. The agent sees only the metadata at startup, reads the full SKILL.md when a skill is relevant, and opens other files only as needed. The post advises auditing skills from less-trusted sources.
  *Use in wiki:* Background reading for the wiki page on 'how agents get context', paired with the context-engineering post.
  Tools: claude-code, claude-ai
  *Note:* Published October 16, 2025. An update note on the page says Agent Skills was published as an open standard (agentskills.io).

- [optional] **[anthropics/skills: public repository of Agent Skills](https://github.com/anthropics/skills)** (2026) — Anthropic. *GitHub*
  `package` · `intermediate` · `access: open` · `Apache-2.0 for many skills; the docx/pdf/pptx/xlsx document skills are source-available, not open source` · `AI angle`
  Anthropic's example skills (about 183k stars). They cover creative, technical, enterprise and document work (docx, pdf, pptx, xlsx), and each is a folder with a SKILL.md.
  *Use in wiki:* Use it as a template gallery when students write their own analysis skill, for example for a team project's data-cleaning conventions.
  Tools: claude-code
  *Note:* Check each skill folder's license before you redistribute it on the wiki.

## Workflows, prompting and verification

- [core] **[Here's how I use LLMs to help me write code](https://simonwillison.net/2025/Mar/11/using-llms-for-code/)** (2025) — Willison, S. *Simon Willison's Weblog*
  `blog` · `intro` · `access: open` · `AI angle`
  Practical advice: treat LLMs as overconfident pair programmers; account for training cut-offs and prefer well-known libraries; manage context; ask for options before committing; be specific; 'test everything' (if you haven't seen it run, it isn't working); vibe-code to learn but not for production.
  *Use in wiki:* First-week reading that sets norms for the course: AI writes the draft, the student verifies.
  Tools: chatgpt, claude-ai

- [core] **[My LLM codegen workflow atm](https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/)** (2025) — Reed, H. *harper.blog*
  `blog` · `intro` · `access: open` · `AI angle`
  A widely cited workflow: brainstorm a spec with an LLM asking one question at a time (spec.md), have a reasoning model write a step-by-step plan and prompts (prompt_plan.md, todo.md), then execute step by step with tests. Brownfield work uses repomix to pack context for review and for finding missing tests.
  *Use in wiki:* Assigned reading. Students apply the spec, plan, execute loop to their team project and commit spec.md and todo.md to the repo.
  Tools: claude-code, aider, repomix
  *Note:* Published February 16, 2025. Follow-up 'Basic Claude Code' (May 8, 2025): https://harper.blog/2025/05/08/basic-claude-code/ (link from the post).

- [recommended] **[Claude Cookbooks (anthropics/claude-cookbooks)](https://github.com/anthropics/claude-cookbooks)** (2026) — Anthropic. *GitHub*
  `notebook` · `intermediate` · `access: open` · `MIT` · `AI angle`
  Jupyter notebooks and recipes for the Claude API: tool use, SQL queries, JSON or structured extraction, PDF summarization, reading charts, classification, RAG, skills and the Agent SDK.
  *Use in wiki:* Embed selected notebooks in the wiki. misc/how_to_make_sql_queries.ipynb and the JSON-mode or structured-extraction recipes suit M5 text analysis; multimodal/reading_charts_graphs_powerpoints.ipynb suits M2.
  Tools: anthropic, python, jupyter
  *Note:* Running these notebooks needs an Anthropic API key, which costs money. The README links still point to the old anthropics/anthropic-cookbook name, so the repo appears to have been renamed.

- [recommended] **[pandera: statistical data testing for DataFrames](https://github.com/unionai-oss/pandera)** (2026) — Union.ai / pandera contributors. *GitHub*
  `package` · `intermediate` · `access: open` · `MIT` · `AI angle`
  A lightweight library for declaring DataFrame schemas (types, ranges, allowed values) and validating pandas or polars data with `schema.validate()`. Failures surface silent errors that AI-written cleaning code can introduce.
  *Use in wiki:* Exercise: students ask the agent to write the cleaning step and also a pandera schema plus pytest assertions, then deliberately break the data to check that the tests catch it.
  Tools: pandera, pandas, polars, pytest
  *Note:* Docs: https://pandera.readthedocs.io. In recent versions use `import pandera.pandas as pa`; the top-level import is deprecated. Pair with pytest: https://docs.pytest.org/en/stable/getting-started.html (fetched).

- [recommended] **[Prompt engineering (OpenAI API docs)](https://developers.openai.com/api/docs/guides/prompt-engineering)** (2026) — OpenAI. *developers.openai.com*
  `documentation` · `intro` · `access: open` · `AI angle`
  OpenAI's guide to consistent results: choosing between reasoning and GPT models, instructions and message roles, Markdown or XML structure, few-shot examples, RAG context, prompt caching, and model-specific advice for coding and agentic tasks.
  *Use in wiki:* Second canonical prompting reference next to Anthropic's. Students compare the two and distill a one-page 'prompting for analysis code' checklist.
  Tools: openai
  *Note:* platform.openai.com/docs/guides/prompt-engineering 302-redirects here. A Codex-specific prompting page appears in the navigation at https://developers.openai.com/codex/prompting (not opened).

- [recommended] **[Prompt engineering overview and Prompting best practices (Claude Platform docs)](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)** (2026) — Anthropic. *platform.claude.com*
  `documentation` · `intro` · `access: open` · `AI angle`
  Anthropic's entry point to prompting. Before tuning a prompt, define success criteria and a way to test against them. Techniques (clarity, examples, XML structure, roles, thinking, chaining) are collected in the 'Prompting best practices' reference.
  *Use in wiki:* Link it from the prompting page, and use its 'define success criteria first' framing to teach students to specify expected numbers or tests before asking for analysis code.
  Tools: claude-ai
  *Note:* docs.claude.com/... 302-redirects here. Best-practices page: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices. An interactive tutorial is at https://github.com/anthropics/prompt-eng-interactive-tutorial, written for Claude 3, so some advice is dated, and I did not check its license. A metaprompt notebook can be opened in Colab from the claude-cookbooks repo.

- [recommended] **[The Turing Way: Guide for Reproducible Research](https://book.the-turing-way.org/reproducible-research/reproducible-research)** (2026) — The Turing Way Community. *The Turing Way*
  `book` · `intro` · `access: open` · `CC BY 4.0 (text); MIT (code)`
  An open handbook by more than 300 contributors. Its chapters on version control, testing, reproducible environments and code review give a vendor-neutral base for checking any analysis, including AI-written code.
  *Use in wiki:* Link the Testing (https://book.the-turing-way.org/reproducible-research/testing) and Reproducible Environments (https://book.the-turing-way.org/reproducible-research/renv) chapters from the project-requirements page.
  Tools: git, pytest, conda
  *Note:* Subchapter URLs come from the fetched page. CC BY lets the wiki adapt excerpts with attribution.

- [recommended] **[Using Git with coding agents](https://simonwillison.net/guides/agentic-engineering-patterns/using-git-with-coding-agents/)** (2026) — Willison, S. *Simon Willison's Weblog (Agentic Engineering Patterns)*
  `blog` · `intro` · `access: open` · `AI angle`
  Git as the safety net for agent work. Have agents init repos, commit and review recent commits to load context; explain merge, rebase and squash; resolve conflicts with tests; recover lost work from the reflog; write git-bisect test scripts; and tidy history.
  *Use in wiki:* Short reading for the GitHub-workflow lab: commit before every agent run, and review the diff before accepting.
  Tools: git, claude-code, codex
  *Note:* Last updated March 21, 2026 (from page metadata).

- [recommended] **[uv: Python package and project manager](https://docs.astral.sh/uv/)** (2026) — Astral. *docs.astral.sh*
  `tool` · `intermediate` · `access: open`
  A fast Rust-based replacement for pip, virtualenv, pip-tools and pyenv. It provides a universal lockfile (`uv lock`, `uv sync`), `uv run` for isolated execution, and inline script dependency metadata (`uv add --script`).
  *Use in wiki:* Require a uv lockfile (or requirements.txt for Colab) in team repos, so the analysis an agent produced on one laptop reruns on the grader's machine.
  Tools: uv, python
  *Note:* Repo: https://github.com/astral-sh/uv. I did not verify the license from the fetched page. In Colab, students can instead pin versions in a requirements.txt and run `pip install -r`.

- [recommended] **[What to look for in a code review (Google Engineering Practices)](https://google.github.io/eng-practices/review/reviewer/looking-for.html)** (2019) — Google. *google.github.io/eng-practices*
  `documentation` · `intro` · `access: open`
  Google's reviewer checklist: design, functionality and edge cases, complexity and over-engineering, tests that actually fail when code breaks, naming, and comments that explain why.
  *Use in wiki:* Adapt it into the course's 'AI-generated analysis code review checklist', adding data-specific items: row counts, joins, missing values, units, and reproducing headline numbers.
  *Note:* The page does not state a license; it says the site is open source on GitHub. The year is approximate (the guide was first published around 2019) and was not verified.

- [recommended] **[Good enough practices in scientific computing](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510)** (2017) — Wilson, G.; Bryan, J.; Cranston, K.; Kitzes, J.; Nederbragt, L.; Teal, T. K. *PLOS Computational Biology 13(6): e1005510*
  `paper` · `intro` · `access: open` · `CC BY 4.0`
  A minimal set of practices for newcomers: keep raw data unchanged, script every processing step, write short well-named functions, state dependencies explicitly, use a consistent project layout with README, LICENSE and CITATION files, and use version control.
  *Use in wiki:* Academic anchor for the team-project repo rubric. Students can have the agent scaffold this layout.
  DOI [10.1371/journal.pcbi.1005510](https://doi.org/10.1371/journal.pcbi.1005510) · Tools: git

## Security, privacy and risk

- [core] **[Claude Code data usage (training, retention, telemetry)](https://code.claude.com/docs/en/data-usage)** (2026) — Anthropic. *code.claude.com*
  `documentation` · `intro` · `access: open` · `AI angle`
  Free, Pro and Max (consumer) accounts choose whether their data trains future models. With the setting on, retention is 5 years; with it off, 30 days. Team, Enterprise and API (commercial) data is not used for training by default, and standard retention is 30 days. Local transcripts are stored in plaintext under ~/.claude/projects/ for 30 days.
  *Use in wiki:* Use it on the data-privacy wiki page to show why personal accounts differ from institutional ones, and have students check their claude.ai privacy setting before using course or client data.
  Tools: claude-code
  *Note:* Transcripts sent with /feedback are retained for 5 years. Telemetry can be disabled with environment variables. Point out to students that local plaintext transcripts can contain any data the agent has read.

- [core] **[Claude Code security (permission modes, prompt-injection safeguards, MCP and cloud security)](https://code.claude.com/docs/en/security)** (2026) — Anthropic. *code.claude.com*
  `documentation` · `intermediate` · `access: open` · `AI angle`
  Covers Claude Code's permission architecture (read-only by default in Manual mode; auto mode uses a classifier model to review actions), sandboxed bash, the working-directory boundary, prompt-injection protections, MCP server trust, isolation of cloud sessions, and best practices for untrusted content.
  *Use in wiki:* Required reading for the 'running agents safely' wiki page. Students configure /permissions and /sandbox before the first assignment that touches course data.
  Tools: claude-code
  *Note:* Related pages: https://code.claude.com/docs/en/permissions, https://code.claude.com/docs/en/permission-modes and https://code.claude.com/docs/en/sandboxing. As of v2.1.283, auto mode is the default starting permission mode for interactive terminal sessions, so instructors may want to recommend Manual mode or plan mode at first.

- [core] **[Colab FAQ: AI features, data use, and Colab Pro for Education](https://research.google.com/colaboratory/faq.html)** (2026) — Google. *research.google.com*
  `documentation` · `intro` · `access: open` · `AI angle`
  Colab's AI features are on by default for eligible users aged 18+. Google collects prompts, related code, outputs and feedback, human reviewers may read them, and data is kept up to 18 months. Users are asked not to include sensitive or personally identifying information. Colab Pro for Education (free Pro for US students) is no longer open to new signups.
  *Use in wiki:* Key slide for the privacy lesson: in Colab, never paste customer PII into a Gemini prompt, and use synthetic or anonymized course datasets.
  Tools: colab, gemini
  *Note:* By default Colab AI cannot read Drive files or secrets, but it can write code that does when you ask. Note the contrast with Google Workspace for Education terms on the UIUC page.

- [core] **[OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/)** (2025) — OWASP Gen AI Security Project. *OWASP*
  `report` · `intermediate` · `access: open` · `CC BY-SA 4.0` · `AI angle`
  The standard list of LLM application risks: LLM01 prompt injection, LLM02 sensitive information disclosure, LLM03 supply chain, LLM04 data and model poisoning, LLM05 improper output handling, LLM06 excessive agency, LLM07 system prompt leakage, LLM08 vector and embedding weaknesses, LLM09 misinformation, LLM10 unbounded consumption.
  *Use in wiki:* Security page backbone. Map LLM01, LLM02, LLM06 and LLM09 to concrete student behaviors with agents and data.
  *Note:* Agent-specific companion: 'OWASP Top 10 for Agentic Applications for 2026' (published December 9, 2025; https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/, fetched). Its landing page does not list the ten items; the PDF is at https://genai.owasp.org/download/52117/?tmstv=1765059207 (not opened).

- [core] **[The lethal trifecta for AI agents: private data, untrusted content, and external communication](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)** (2025) — Willison, S. *Simon Willison's Weblog*
  `blog` · `intro` · `access: open` · `AI angle`
  An agent that combines access to private data, exposure to untrusted content and the ability to communicate externally can be steered by prompt injection into leaking data. Guardrails help only partly, so avoid giving one agent all three.
  *Use in wiki:* The single most teachable security concept. Students check their own setup (for example customer CSV + web browsing + MCP email = all three) against it.

- [recommended] **[Codex sandboxing and approval modes](https://learn.chatgpt.com/codex/sandboxing)** (2026) — OpenAI. *learn.chatgpt.com*
  `documentation` · `intermediate` · `access: open` · `AI angle`
  Explains Codex's OS-enforced sandbox modes (read-only, workspace-write as the local default, and full access) and the approval policies that decide when the agent must stop and ask.
  *Use in wiki:* Comparison row on the 'running agents safely' page: Codex's workspace-write mode next to Claude Code's sandbox and VS Code approvals.
  Tools: codex
  *Note:* Related: https://learn.chatgpt.com/codex/agent-approvals-security and https://learn.chatgpt.com/codex/security (links from the docs hub).

- [recommended] **[Enterprise privacy at OpenAI (business data commitments)](https://openai.com/enterprise-privacy/)** (2026) — OpenAI. *openai.com*
  `documentation` · `intro` · `access: open` · `AI angle`
  By default OpenAI does not train on business data from ChatGPT Business, Enterprise, Edu or the API. Admins set retention for Enterprise and Edu, and API data is generally kept up to 30 days. Personal (consumer) accounts are handled differently and may be used for training.
  *Use in wiki:* Data-privacy page: the core lesson that the same model under a different account type carries different data terms. Never paste client or customer PII into a personal account.
  Tools: chatgpt, openai

- [recommended] **[Securing AI-assisted development in VS Code (prompt injection, Workspace Trust, approvals, sandboxing)](https://code.visualstudio.com/docs/agents/run/security)** (2026) — Microsoft (VS Code). *code.visualstudio.com*
  `documentation` · `intermediate` · `access: open` · `AI angle`
  Explains the risks of agents and MCP servers, with prompt injection through tool output as the central concern. It recommends Restricted Mode (Workspace Trust) for untrusted projects and reviewing edits, terminal commands and tool calls through approval prompts.
  *Use in wiki:* Pair it with the Claude Code security page so students see the same principles across tools.
  Tools: vscode, copilot
  *Note:* Related: https://code.visualstudio.com/docs/agents/run/approvals and https://code.visualstudio.com/docs/agents/run/agent-sandboxing (links only).

- [recommended] **[Beyond permission prompts: making Claude Code more secure and autonomous](https://www.anthropic.com/engineering/claude-code-sandboxing)** (2025) — Dworken, D.; Weller-Davies, O. (Anthropic). *Anthropic Engineering*
  `blog` · `intermediate` · `access: open` · `AI angle`
  Explains Claude Code's sandbox, which combines filesystem isolation with network isolation through a domain-allowlisting proxy, enforced with OS tools (bubblewrap on Linux, seatbelt on macOS). It argues that both are needed to stop a compromised agent from exfiltrating data.
  *Use in wiki:* Instructor background for teaching why sandboxing matters and how it reduces 'approval fatigue'.
  Tools: claude-code
  *Note:* Published October 20, 2025. Open-source runtime: https://github.com/anthropic-experimental/sandbox-runtime (link from the post; I did not check its license).

- [recommended] **[Do Users Write More Insecure Code with AI Assistants?](https://arxiv.org/abs/2211.03622)** (2023) — Perry, N.; Srivastava, M.; Kumar, D.; Boneh, D. *ACM (DOI prefix 10.1145; likely ACM CCS 2023)*
  `paper` · `intermediate` · `access: open` · `AI angle`
  In a user study, participants with an AI assistant wrote significantly less secure code yet were more confident it was secure. Participants who trusted the AI less and refined their prompts more produced fewer vulnerabilities.
  *Use in wiki:* Evidence for the course norm 'confidence is not correctness'. Pair it with an in-class exercise auditing AI-generated code.
  DOI [10.1145/3576915.3623157](https://doi.org/10.1145/3576915.3623157) · [Open-access copy](https://arxiv.org/abs/2211.03622)
  *Note:* The arXiv page shows the ACM DOI but not the venue name. CCS 2023 is inferred from the DOI and should be confirmed before citing.

- [optional] **[Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/abs/2302.12173)** (2023) — Greshake, K.; Abdelnabi, S.; Mishra, S.; Endres, C.; Holz, T.; Fritz, M. *arXiv (cs.CR)*
  `paper` · `advanced` · `access: open` · `AI angle`
  The foundational paper on indirect prompt injection. Instructions hidden in content an LLM retrieves can hijack the application, causing data theft, worming and contamination of information ecosystems. Demonstrated against Bing Chat and code-completion engines.
  *Use in wiki:* Academic citation for the security page, and for M5's point that scraped social-media text may itself contain injected instructions.
  DOI [10.48550/arXiv.2302.12173](https://doi.org/10.48550/arXiv.2302.12173) · [Open-access copy](https://arxiv.org/abs/2302.12173)
  *Note:* The arXiv page lists no venue. The paper is widely cited as appearing at ACM AISec 2023, which I did not verify here.

## Python for marketing analytics: notebooks and code

- [recommended] **[claude-ecom: Claude Code plugin that turns order CSVs into business reviews](https://github.com/takechanman1228/claude-ecom)** (2026) — Takeda, H. (takechanman1228). *GitHub*
  `tool` · `intro` · `access: open` · `MIT` · `AI angle`
  A Python engine computes KPI trees, multi-horizon dashboards, repeat-purchase and new-vs-returning metrics plus health checks from order data; Claude then writes the narrative REVIEW.md. Includes an Online Retail II example review and a test fixture of sample orders.
  *Use in wiki:* M2 'vibe coding' case: students run the skill on Online Retail, then audit its numbers against their own pandas code and judge the narrative with the Pyramid Principle.
  Tools: claude-code, pandas · Local copy: `11_AI_Coding_Tools_and_Workflows/repos/takechanman1228__claude-ecom`
  *Note:* assets/ (9.6 MB demo GIF and banner) is skipped. The README doesn't claim RFM or cohort tables. The Online Retail II data itself is not in the repo.

- [optional] **[claude-persona: Claude Code skill for AI persona panels and concept testing](https://github.com/takechanman1228/claude-persona)** (2026) — Takeda, H. (takechanman1228). *GitHub*
  `tool` · `intermediate` · `access: open` · `MIT` · `AI angle`
  Generates diverse persona panels (TinyTroupe-inspired), runs each persona in an isolated claude -p subprocess, and produces concept-test and messaging reports. Four demos (running shoes, Gen Z skincare, meal kits, SaaS).
  *Use in wiki:* M4/M8 discussion: compare a synthetic concept test with a real conjoint or survey and connect it to the digital-twin validity readings in M3_M4.yaml.
  Tools: claude-code
  *Note:* Its 'Why trust the results' section shows stability across model versions, not validity against real consumers. Teach it as a hypothesis generator. Size estimated.
