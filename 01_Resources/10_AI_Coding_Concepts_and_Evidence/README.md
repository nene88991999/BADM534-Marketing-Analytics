# AI-Assisted Coding · Concepts, History and Evidence

50 resources (23 core). Built 2026-10-25 from `00_Index/_data/`; edit the YAML there and rerun `00_Index/_build/build_catalog.py` rather than editing this file.

Priority: **core** = likely to assign or build on; **recommended** = strong supplement; **optional** = background or niche. *Access* tells you whether students can open it without a login.

## Contents

- [Origins and definitions](#origins-and-definitions) (9)
- [Practitioner perspectives and books](#practitioner-perspectives-and-books) (7)
- [Productivity evidence](#productivity-evidence) (11)
- [Usage data and surveys](#usage-data-and-surveys) (6)
- [Code quality, security and incidents](#code-quality-security-and-incidents) (6)
- [AI for data analysis and empirical research](#ai-for-data-analysis-and-empirical-research) (11)

## Origins and definitions

- [core] **[Andrej Karpathy: Software Is Changing (Again)](https://www.youtube.com/watch?v=LCEmiRjPEtQ)** (2025) — Karpathy, A. *Y Combinator AI Startup School (YouTube)*
  `video` · `intro` · `access: open` · `AI angle`
  Keynote from 17 June 2025 framing LLMs as a new kind of computer programmed in English ('Software 3.0'). It covers LLM 'psychology', partial-autonomy apps with an autonomy slider, vibe coding, and building software that agents can use.
  *Use in wiki:* Embed as the module's anchor video; assign the vibe coding and 'autonomy slider' segments before the first in-class AI coding lab.
  *Note:* Posted 18 June 2025. Free transcripts exist elsewhere if students prefer reading.

- [core] **[Not all AI-assisted programming is vibe coding (but vibe coding rocks)](https://simonwillison.net/2025/Mar/19/vibe-coding/)** (2025) — Willison, S. *Simon Willison's Weblog*
  `blog` · `intro` · `access: open` · `AI angle`
  Argues that vibe coding means not reviewing the code. If you review, test and can explain the AI's code, that is ordinary software development. He also praises vibe coding for prototypes and for learning what models can do.
  *Use in wiki:* Required reading paired with Karpathy's post; it supplies the course rule that anything submitted must be code you can explain.

- [core] **[There's a new kind of coding I call 'vibe coding' (X post)](https://x.com/karpathy/status/1886192184808149383)** (2025) — Karpathy, A. *X (Twitter)*
  `blog` · `intro` · `access: open` · `AI angle`
  The 2 February 2025 post that coined 'vibe coding': you give in to the vibes, accept AI-generated changes without reading the diffs, and let the model, Cursor Composer in his case, write the code.
  *Use in wiki:* Opening reading for the AI module; students compare Karpathy's throwaway-project framing with the standard required for analysis code they will submit.
  *Note:* URL cited in the Wikipedia 'Vibe coding' article and in Simon Willison's March 2025 post, which also quotes the text in full. x.com may require login to view, so link Willison's post as a backup.

- [core] **[To vibe or not to vibe](https://www.martinfowler.com/articles/exploring-gen-ai/to-vibe-or-not-vibe.html)** (2025) — Böckeler, B. *martinfowler.com*
  `blog` · `intro` · `access: open` · `AI angle`
  Whether AI code needs review depends on three things: how likely the AI is to be wrong, how bad an error would be, and how easily you would notice it. Low-risk, high-detectability work can be vibe-coded; high-impact, low-detectability work needs close scrutiny.
  *Use in wiki:* Turn the three factors into a one-page rubric students apply to each analysis step. A typo in a chart label is low risk; a silent join error in CLV data is high impact and hard to detect.
  *Note:* Published 23 September 2025.

- [core] **[Vibe engineering](https://simonwillison.net/2025/Oct/7/vibe-engineering/)** (2025) — Willison, S. *Simon Willison's Weblog*
  `blog` · `intermediate` · `access: open` · `AI angle`
  Coins 'vibe engineering' (7 October 2025) for experienced engineers who use coding agents while staying accountable for quality. It lists the practices agents reward: automated tests, planning, documentation, version control, code review, manual QA and preview environments.
  *Use in wiki:* Basis for the course's 'vibe engineering' standards: map each practice to a requirement in the team project, such as tests, a README, Git history and peer review.

- [recommended] **[Vibe coding](https://en.wikipedia.org/wiki/Vibe_coding)** (2026) — Wikipedia contributors. *Wikipedia*
  `website` · `intro` · `access: open` · `CC BY-SA 4.0` · `AI angle`
  Running encyclopedia entry covering the term's origin, uptake in industry, and criticism on security, maintainability and open-source impact. It cites METR, Veracode, CodeRabbit, the Replit incident, the 2026 rsync dispute and the 'Vibe Coding Kills Open Source' paper.
  *Use in wiki:* Instructor-only background and a source of incident links; students can use it to find primary sources but should cite those sources instead.

- [recommended] **[Speaking things into existence: Expertise in a vibe-filled world of work](https://www.oneusefulthing.org/p/speaking-things-into-existence)** (2025) — Mollick, E. *One Useful Thing*
  `newsletter` · `intro` · `access: open` · `AI angle`
  A business-school professor vibe codes a 3D game with Claude Code, builds an interactive course, and runs a research analysis on old crowdfunding data. He argues vibe coding redistributes expertise rather than eliminating it: you still need to know what you want and judge what you get.
  *Use in wiki:* Accessible reading for non-CS business students; the crowdfunding-data example works as a model for an AI-assisted marketing analysis.
  *Note:* Published 11 March 2025.

- [optional] **[Vibe coding and agentic engineering are getting closer than I'd like](https://simonwillison.net/2026/May/6/vibe-coding-and-agentic-engineering/)** (2026) — Willison, S. *Simon Willison's Weblog*
  `blog` · `intermediate` · `access: open` · `AI angle`
  In May 2026 Willison admits he now trusts agents enough to skip reviewing some production code. He worries the line he drew in 2025 is blurring, and notes that a polished repository no longer signals careful work.
  *Use in wiki:* Discussion prompt: if experts are reviewing less, what evidence should a student team give that its analysis code is correct?

- [optional] **['Vibe coding' named Collins Dictionary's Word of the Year](https://kvia.com/news/business-technology/cnn-business-consumer/2025/11/06/vibe-coding-named-collins-dictionarys-word-of-the-year/)** (2025) — Kolirin, L. (CNN). *CNN Newsource (republished by KVIA)*
  `website` · `intro` · `access: open` · `AI angle`
  News story from 6 November 2025 on Collins naming 'vibe coding' its 2025 Word of the Year, defined as 'the use of artificial intelligence prompted by natural language to assist with the writing of computer code.'
  *Use in wiki:* One-line hook or sidebar on the wiki's AI landing page, showing how fast the term entered everyday language.
  *Note:* Collins's own word-of-the-year page and the BBC story would not load from this environment, so this is CNN's syndicated copy. Merriam-Webster also lists the term as slang or trending (https://www.merriam-webster.com/slang/vibe-coding): 'writing computer code in a somewhat careless fashion, with AI assistance.'

## Practitioner perspectives and books

- [core] **[Agentic Engineering Patterns (guide)](https://simonwillison.net/guides/agentic-engineering-patterns/what-is-agentic-engineering/)** (2026) — Willison, S. *Simon Willison's Weblog (guides)*
  `tutorial` · `intermediate` · `access: open` · `AI angle`
  A growing guide to working with coding agents. Chapters cover principles ('Writing code is cheap now'), how agents work, Git with agents, subagents, red/green TDD, 'First run the tests', agentic manual testing, linear walkthroughs and interactive explanations, with annotated prompts.
  *Use in wiki:* Link chapters from the wiki as just-in-time references, for example red/green TDD before the regression lab and linear walkthroughs whenever students must explain AI-written code.
  *Note:* Page last updated around 15 March 2026. Willison defines an agent as software that runs tools in a loop toward a goal, and reserves 'vibe coding' for unreviewed prototype code.

- [core] **[The 70% problem: Hard truths about AI-assisted coding](https://addyo.substack.com/p/the-70-problem-hard-truths-about)** (2024) — Osmani, A. *Elevate (Addy Osmani's Substack)*
  `blog` · `intro` · `access: open` · `AI angle`
  Argues that AI tools quickly get non-experts about 70% of the way, but the last 30% (edge cases, debugging, maintainability) needs engineering knowledge. Juniors and seniors get very different value as a result.
  *Use in wiki:* Assigned reading framing why the course still teaches the analysis underneath; pair with Prather et al. (2024) on novices.
  *Note:* The URL came from a linking page (ipspace.net, December 2024); the Substack page itself wasn't fetched. Published December 2024. Summary based on the title and secondary coverage, so skim before assigning.

- [recommended] **[Context Engineering for Coding Agents](https://www.martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html)** (2026) — Böckeler, B. *martinfowler.com*
  `blog` · `intermediate` · `access: open` · `AI angle`
  Explains how to curate what a coding agent sees: CLAUDE.md or AGENTS.md guidance files loaded every session, path-scoped rules, and skills that load instructions or scripts on demand.
  *Use in wiki:* Reference for a lab where each team writes a CLAUDE.md or AGENTS.md describing its dataset, variable definitions and coding conventions.
  *Note:* Published 5 February 2026.

- [recommended] **[Exploring Generative AI (memo series)](https://www.martinfowler.com/articles/exploring-gen-ai.html)** (2026) — Böckeler, B. (main author); Morris, K.; Vaccari, M.; Doernenburg, E.; et al. *martinfowler.com (Thoughtworks)*
  `website` · `intermediate` · `access: open` · `AI angle`
  About 33 memos, from 2023 to October 2026, by Thoughtworks engineers on coding assistants and agents: multi-file editing, autonomous agents, supply-chain risk, spec-driven development, context engineering, harness engineering, TDD inside the agent loop.
  *Use in wiki:* Instructor-only map of the practitioner literature; pick individual memos (below) as readings.

- [recommended] **[Beyond Vibe Coding: From Coder to AI-Era Developer](https://www.oreilly.com/library/view/beyond-vibe-coding/9798341634749)** (2025) — Osmani, A. *O'Reilly Media*
  `book` · `intermediate` · `access: library` · `AI angle`
  O'Reilly book (August 2025) contrasting prompt-first vibe coding with structured, AI-assisted engineering. It covers refining and debugging generated code, the risks of accepting output uncritically, and multi-agent workflows.
  *Use in wiki:* Optional deeper reading; assign single chapters through O'Reilly Learning if the UIUC Library subscription covers it.
  *Note:* Check UIUC Library's O'Reilly Learning access; otherwise paid.

- [recommended] **[Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl](https://www.martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)** (2025) — Böckeler, B. *martinfowler.com*
  `blog` · `intermediate` · `access: open` · `AI angle`
  Compares three spec-driven development tools (Kiro, GitHub spec-kit, Tessl) and proposes three levels: spec-first, spec-anchored and spec-as-source. Also raises concerns about verbosity, review burden and echoes of model-driven development.
  *Use in wiki:* Background for a 'write the analysis plan before prompting' assignment, where students draft a short spec (question, data, method, outputs) that the agent must follow.
  *Note:* Published 15 October 2025.

- [optional] **[Vibe Coding: Building Production-Grade Software With GenAI, Chat, Agents, and Beyond](https://bookshop.org/p/books/vibe-coding-building-production-grade-software-with-genai-chat-agents-and-beyond-gene-kim/b6e53e37eeba8cac)** (2025) — Kim, G.; Yegge, S. *IT Revolution*
  `book` · `intermediate` · `access: paid` · `AI angle`
  Practitioner book (21 October 2025, foreword by Dario Amodei) on using chat and agentic AI for everything from small tools to enterprise systems while keeping engineering discipline.
  *Use in wiki:* Instructor background and a source of war stories for the AI module; too long to assign in full.
  *Note:* ISBN 9781966280026 (paperback). IT Revolution's article about the book: https://itrevolution.com/articles/vibe-coding-the-revolutionary-approach-transforming-software-development/

## Productivity evidence

- [core] **[We are Changing our Developer Productivity Experiment Design](https://metr.org/blog/2026-02-24-uplift-update/)** (2026) — Becker, J.; Rush, N.; Cunningham, T.; Rein, D.; Mahamud, K. (METR). *METR blog*
  `report` · `intermediate` · `access: open` · `AI angle`
  Late-2025 follow-up (57 developers, 800+ tasks). Point estimates now show speedups (-18% time for returning developers, -4% for new ones), but METR calls them weak evidence. Developers increasingly refused to work without AI, causing selection, and METR is redesigning the study.
  *Use in wiki:* Excellent M6 teaching case on selection, attrition and non-compliance when the treatment becomes indispensable; pair with the 2025 study.
  *Note:* Published 24 February 2026. METR calls the central estimate 'a bad proxy for the real productivity impact'.

- [core] **[Generative AI at Work](https://digitaleconomy.stanford.edu/publication/generative-ai-at-work)** (2025) — Brynjolfsson, E.; Li, D.; Raymond, L. *Quarterly Journal of Economics*
  `paper` · `advanced` · `access: open` · `AI angle`
  Staggered rollout of an AI assistant to 5,172 customer-support agents raised issues resolved per hour by about 15% on average. The largest gains went to less experienced and lower-skilled workers; top workers gained little.
  *Use in wiki:* Economics anchor for the heterogeneity theme (who gains from AI); useful in M6 as a staggered-adoption design.
  [Open-access copy](https://arxiv.org/abs/2304.11771)
  *Note:* Customer support, not coding. Published in QJE 2025 (article qjae044, as cited in Shen & Tamkin 2026); the QJE landing page wasn't checked here.

- [core] **[Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)** (2025) — Becker, J.; Rush, N.; Barnes, E.; Rein, D. (METR). *METR (blog + arXiv 2507.09089)*
  `report` · `intermediate` · `access: open` · `AI angle`
  RCT with 16 experienced open-source developers on 246 real issues in their own large repositories. Allowing AI made tasks take 19% longer, yet developers expected a 24% speedup and afterwards believed AI had sped them up by 20%.
  *Use in wiki:* Centerpiece case on perception vs. measurement; students contrast it with Cui et al. and discuss task, population and tool differences.
  DOI [10.48550/arXiv.2507.09089](https://doi.org/10.48550/arXiv.2507.09089) · [Open-access copy](https://arxiv.org/abs/2507.09089)
  *Note:* METR now flags these results as out of date; always pair with the February 2026 update.

- [core] **[The Effects of Generative AI on High-Skilled Work: Evidence from Three Field Experiments with Software Developers](https://pubsonline.informs.org/doi/fpi/10.1287/mnsc.2025.00535)** (2025) — Cui, Z. K.; Demirer, M.; Jaffe, S.; Musolff, L.; Peng, S.; Salz, T. *Management Science*
  `paper` · `advanced` · `access: open` · `AI angle`
  Three randomized field experiments (Microsoft, Accenture, an anonymous Fortune 100 firm; 4,867 developers) find a 26.08% (SE 10.3%) increase in completed tasks with an AI coding assistant (GitHub Copilot).
  *Use in wiki:* Academic anchor in Management Science for M6 (field experiments, staggered rollout, pooling estimates) and the AI module's evidence page.
  DOI [10.1287/mnsc.2025.00535](https://doi.org/10.1287/mnsc.2025.00535) · [Open-access copy](https://economics.mit.edu/sites/default/files/inline-files/draft_copilot_experiments.pdf)
  *Note:* The INFORMS page didn't show volume or issue, so check the final citation. SSRN version: https://papers.ssrn.com/abstract=4945566. The paper also reports heterogeneity by developer experience; check the abstract before quoting.

- [core] **[Vibe coding: programming through conversation with artificial intelligence](https://www.microsoft.com/en-us/research/publication/vibe-coding-programming-through-conversation-with-artificial-intelligence/)** (2025) — Sarkar, A.; Drosos, I. *Proceedings of PPIG 2025 (Psychology of Programming Interest Group)*
  `paper` · `intermediate` · `access: open` · `AI angle`
  Microsoft Research study of more than 8 hours of think-aloud vibe coding sessions. Vibe coding turns out to be iterative cycles of prompting, evaluating and hand-editing, and it shifts expertise toward managing context and judging output rather than removing the need for expertise.
  *Use in wiki:* Academic anchor for the claim that vibe coding still requires expertise; good for a short discussion post.
  [Open-access copy](https://arxiv.org/abs/2506.23253)

- [core] **[Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of AI on Knowledge Worker Productivity and Quality](https://papers.ssrn.com/abstract=4573321)** (2023) — Dell'Acqua, F.; McFowland III, E.; Mollick, E. R.; Lifshitz-Assaf, H.; Kellogg, K.; Rajendran, S.; Krayer, L.; Candelon, F.; Lakhani, K. R. *Harvard Business School Working Paper 24-013*
  `paper` · `intermediate` · `access: open` · `AI angle`
  Preregistered experiment with BCG consultants: GPT-4 improved speed and quality on tasks inside the AI 'frontier' but reduced correctness on a task just outside it. Introduces 'centaur' and 'cyborg' work styles.
  *Use in wiki:* Core business-school reading on why AI help is uneven; students map which Marketing Analytics tasks sit inside or outside the frontier.
  [Open-access copy](https://mitsloan.mit.edu/sites/default/files/2023-10/SSRN-id4573321.pdf)
  *Note:* The SSRN page wouldn't load directly; URL and PDF come from search results. Author list as given in Shen & Tamkin (2026). A later journal version couldn't be confirmed.

- [core] **[The Impact of AI on Developer Productivity: Evidence from GitHub Copilot](https://arxiv.org/abs/2302.06590)** (2023) — Peng, S.; Kalliamvakou, E.; Cihon, P.; Demirer, M. *arXiv 2302.06590*
  `paper` · `intermediate` · `access: open` · `AI angle`
  Controlled experiment in which developers with GitHub Copilot finished an HTTP server in JavaScript 55.8% faster than the control group.
  *Use in wiki:* Classic early RCT; use in M6 as a worked example of a two-arm experiment and of what a narrow, well-specified task can and cannot tell us.
  DOI [10.48550/arXiv.2302.06590](https://doi.org/10.48550/arXiv.2302.06590) · [Open-access copy](https://arxiv.org/abs/2302.06590)

- [recommended] **[Vibe Coding: Practice, Performance, Productivity, and Risk - A State-of-the-Art Review](https://arxiv.org/abs/2608.20446)** (2026) — Michels, D. L.; Abu Ghazaleh, M.; Lazzari, F.; Kassem, N.; Klein, J. *arXiv (cs.SE) 2608.20446*
  `paper` · `advanced` · `access: open` · `AI angle`
  Cross-disciplinary review from August 2026 (software engineering, HCI, labor economics, security, education). It reconciles conflicting productivity results by measurement method, scope and horizon, and conjectures that gains are real for new code but shrink or reverse on mature codebases.
  *Use in wiki:* Instructor background for an evidence lecture; its 'new code vs. mature codebase' conjecture is a good discussion question.
  *Note:* Recent preprint, not peer reviewed. Its HTML version didn't expose the reference list in this pass.

- [recommended] **[Who is using AI to code? Global diffusion and impact of generative AI](https://arxiv.org/abs/2506.08945)** (2025) — Daniotti, S.; Wachs, J.; Feng, X.; Neffke, F. *arXiv 2506.08945*
  `paper` · `advanced` · `access: open` · `AI angle`
  Trains a classifier to detect AI-written Python functions in 30M+ GitHub commits from about 170,000 developers. About 29% of US Python functions are AI-written; AI raises quarterly output by about 3.6%, and gains go mostly to experienced programmers.
  *Use in wiki:* M7 tie-in (a classifier used as a measurement tool) and evidence that AI may widen skill gaps.

- [recommended] **[How much does AI impact development speed? An enterprise-based randomized controlled trial](https://arxiv.org/abs/2410.12944)** (2024) — Paradis, E.; Grey, K.; Madison, Q.; Nam, D.; Macvean, A.; Meimand, V.; Zhang, N.; Ferrari-Church, B.; Chandra, S. *arXiv 2410.12944*
  `paper` · `intermediate` · `access: open` · `AI angle`
  RCT with 96 Google engineers on an enterprise-grade task: AI features cut time on task by about 21%, with a wide confidence interval, and gains were larger for developers who spend more hours a day coding.
  *Use in wiki:* Third data point beside Peng and METR for an in-class 'meta-analysis by hand' exercise.

- [optional] **[Vibe Coding Kills Open Source](https://arxiv.org/abs/2601.15494)** (2026) — Koren, M.; Békés, G.; Hinz, J.; Lohmann, A. *arXiv (econ.GN) 2601.15494*
  `paper` · `advanced` · `access: open` · `AI angle`
  Economic model with entry and quality choice. Vibe coding makes reusing open-source code cheaper but cuts the user engagement that pays maintainers, so wider adoption can mean fewer and lower-quality open-source projects and lower welfare despite higher productivity.
  *Use in wiki:* Case for the 'Current Topics' module on platform and ecosystem externalities of AI tools; Békés also co-wrote a widely used data analysis textbook.
  *Note:* Submitted 21 January 2026.

## Usage data and surveys

- [core] **[Agentic coding and persistent returns to expertise](https://www.anthropic.com/research/claude-code-expertise)** (2026) — Hitzig, Z.; Massenkoff, M.; Lyubich, E.; Zhang, S.; Heller, R.; McCrory, P. (Anthropic). *Anthropic Economic Research*
  `report` · `intermediate` · `access: open` · `AI angle`
  About 400,000 Claude Code sessions (October 2025 to April 2026): users make about 70% of planning decisions but only about 20% of execution decisions. Domain experts succeed more often, non-software occupations succeed at nearly the same rates as engineers, and data analysis is a growing share of use.
  *Use in wiki:* Key evidence for business students that domain expertise, not syntax, drives success with agents; a good opener for the course's 'you decide what, the agent decides how' framing.
  *Note:* Published 16 June 2026. The companion Economic Index report 'Cadences' (26 June 2026) is at https://www.anthropic.com/research/economic-index-june-2026-report

- [core] **[Stack Overflow Developer Survey 2025: AI](https://survey.stackoverflow.co/2025/ai/)** (2025) — Stack Overflow. *Stack Overflow*
  `report` · `intro` · `access: open` · `AI angle`
  Survey of 49,000+ developers: 84% use or plan to use AI tools, but 46% distrust their accuracy. 66% cite 'almost right' solutions as their top frustration, and about 77% say vibe coding isn't part of their professional work.
  *Use in wiki:* Data for a quick M2 visualization exercise (trust vs. use) and a reality check on how professionals use AI.
  *Note:* Released 29 July 2025. Press release: https://stackoverflow.co/company/press/archive/stack-overflow-2025-developer-survey/. The raw data download page may also serve as a class dataset (not checked).

- [recommended] **[Stack Overflow Developer Survey 2026: AI](https://survey.stackoverflow.co/2026/ai)** (2026) — Stack Overflow. *Stack Overflow*
  `report` · `intro` · `access: open` · `AI angle`
  Sixteenth survey (30,903 responses, 169 countries). Coding assistants and agents are now the top AI use case (66%); Claude Code (66%) and GitHub Copilot (59%) lead among coding agents; 48% trust AI only when they can easily check the answer.
  *Use in wiki:* Pair with the 2025 survey to show year-over-year change; the 'trust when verifiable' finding motivates the course's verification habits.
  *Note:* No release date on the page. Figures are as summarized from the page in October 2026, so recheck before citing, especially the trust comparisons with 2025.

- [recommended] **[2025 DORA State of AI-assisted Software Development report](https://cloud.google.com/devops/state-of-devops)** (2025) — DORA (Google Cloud). *Google Cloud / DORA*
  `report` · `intro` · `access: free-registration` · `AI angle`
  Annual DORA survey reframed around AI. It argues that AI amplifies an organization's existing strengths and weaknesses, and introduces a seven-practice DORA AI Capabilities Model.
  *Use in wiki:* Instructor background; the 'AI as amplifier' framing works as a slide for business students thinking about adoption.
  *Note:* Download gated by a contact form. Headline adoption figures weren't visible on the landing page.

- [recommended] **[Anthropic Economic Index: AI's impact on software development](https://www.anthropic.com/research/impact-software-development)** (2025) — Anthropic (Societal Impacts team). *Anthropic*
  `report` · `intro` · `access: open` · `AI angle`
  Analysis of coding conversations from April 2025: about 79% of Claude Code conversations were automation (AI does the task) vs. 49% on Claude.ai. Web languages dominate; Python was 14% and SQL 6%; startups were early Claude Code adopters.
  *Use in wiki:* Shows how privacy-preserving text classification of conversations (M5 methods) produces economic evidence.
  *Note:* Published 28 April 2025. One-week sample covering Free and Pro only; the startup vs. enterprise shares are inconsistent within the post.

- [recommended] **[Measuring AI Ability to Complete Long Software Tasks](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/)** (2025) — Kwa, T.; West, B.; Becker, J.; et al. (METR). *METR (blog + arXiv 2503.14499)*
  `report` · `intermediate` · `access: open` · `AI angle`
  Introduces the '50% time horizon', the length of tasks (in human-expert time) that agents complete with 50% reliability, and finds it doubled roughly every 7 months over six years.
  *Use in wiki:* M3 tie-in: students fit the log-linear trend themselves; also frames why the tools change mid-semester.
  [Open-access copy](https://arxiv.org/abs/2503.14499)
  *Note:* METR says the static March 2025 figures are dated. Current methodology (Time Horizon 1.1, January 2026) is at https://metr.org/time-horizons/

## Code quality, security and incidents

- [core] **[Vibe coding service Replit deleted user's production database, faked data, told fibs galore](https://www.theregister.com/2025/07/21/replit_saastr_vibe_coding_incident/)** (2025) — Sharwood, S. *The Register*
  `website` · `intro` · `access: open` · `AI angle`
  July 2025 incident in which Replit's agent deleted SaaStr founder Jason Lemkin's production database despite instructions not to touch it, generated fake data to hide bugs, and wrongly claimed the data couldn't be restored.
  *Use in wiki:* Short case for a 'guardrails' discussion: separate dev and prod data, use version control, never give an agent write access to the only copy of your data.
  *Note:* Business Insider coverage of the Replit CEO's apology: https://www.businessinsider.com/replit-ceo-apologizes-ai-coding-tool-delete-company-database-2025-7

- [core] **[We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs](https://arxiv.org/abs/2406.10279)** (2025) — Spracklen, J.; Wijewickrama, R.; Sakib, A. H. M. N.; Maiti, A.; Viswanath, B.; Jadliwala, M. *USENIX Security Symposium 2025*
  `paper` · `intermediate` · `access: open` · `AI angle`
  576,000 code samples from 16 LLMs: commercial models hallucinate nonexistent packages at least 5.2% of the time and open-source models 21.7%, producing 205,474 unique fake package names that attackers can register ('slopsquatting').
  *Use in wiki:* Concrete rule for M1 setup labs: verify every pip install suggested by AI against PyPI before running it.
  *Note:* No standalone 'slopsquatting' source was verified in this pass; the Thoughtworks memo 'Coding Assistants Threaten the Software Supply Chain' (https://www.martinfowler.com/articles/exploring-gen-ai/software-supply-chain-attack-surface.html, May 2025) covers the same risk for practitioners.

- [core] **[Asleep at the Keyboard? Assessing the Security of GitHub Copilot's Code Contributions](https://arxiv.org/abs/2108.09293)** (2022) — Pearce, H.; Ahmad, B.; Tan, B.; Dolan-Gavitt, B.; Karri, R. *IEEE Symposium on Security and Privacy 2022*
  `paper` · `intermediate` · `access: open` · `AI angle`
  Generated 1,689 programs with Copilot across 89 security-relevant scenarios and found about 40% vulnerable.
  *Use in wiki:* Classic citation for 'AI code can look right and be unsafe'; a short discussion item in the AI module.

- [recommended] **[GenAI Code Security Report (October 2025 update)](https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/)** (2025) — Veracode. *Veracode*
  `report` · `intro` · `access: free-registration` · `AI angle`
  Industry test of code from 100+ LLMs in Java, JavaScript, Python and C#: AI-generated code introduced risky security flaws in 45% of tests.
  *Use in wiki:* Headline statistic for a slide on why students must not paste credentials or trust generated data-access code.
  *Note:* Vendor report; methodology detail is behind the download. Registration not confirmed on the page.

- [recommended] **[Our new report: AI code creates 1.7x more problems (State of AI vs Human Code Generation)](https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report)** (2025) — Loker, D. (CodeRabbit). *CodeRabbit blog*
  `report` · `intro` · `access: open` · `AI angle`
  Analysis of 470 open-source pull requests: AI-co-authored PRs averaged 10.83 issues vs. 6.45 for human-only PRs, with logic errors 75% more common and readability problems more than 3x.
  *Use in wiki:* Motivates readability and logic-review items on the course's code-review rubric.
  *Note:* Published 17 December 2025. Vendor study; AI authorship was inferred from co-author tags, so some 'human' PRs may involve AI.

- [recommended] **[Vulnerabilities in AI Code Generators: Exploring Targeted Data Poisoning Attacks](https://arxiv.org/abs/2308.04451v3)** (2024) — Cotroneo, D.; Improta, C.; Liguori, P.; Natella, R. *IEEE/ACM International Conference on Program Comprehension (ICPC 2024)*
  `paper` · `advanced` · `access: open` · `AI angle`
  Shows that injecting a small share of poisoned training examples can make AI code generators emit vulnerable code for targeted prompts while overall accuracy stays normal, which makes the attack hard to detect.
  *Use in wiki:* Supports the course rule that AI-written code is reviewed and tested, not trusted; pairs with the slopsquatting and code-security readings in this folder.
  *Note:* Also on the MBA 542 Module 8 reading list. The author list is from recollection of the arXiv entry; confirm it before citing. IEEE Xplore record: https://ieeexplore.ieee.org/document/10556436.

## AI for data analysis and empirical research

- [core] **[AI Agents for Economic Research: August 2025 Update](https://www.aeaweb.org/articles/materials/23826)** (2025) — Korinek, A. *Journal of Economic Literature (online update to Korinek 2023)*
  `paper` · `intermediate` · `access: open` · `AI angle`
  Update to the JEL article on agentic AI for research: what agents are, how economists can use them (deep research, coding agents) and worked examples.
  *Use in wiki:* Bridge reading from chat-based help to agentic workflows (Claude Code, Codex, Gemini CLI) for empirical analysis.
  *Note:* Direct file link: https://www.aeaweb.org/content/file?id=23290. Contents summarized from the title and landing page, so skim before assigning.

- [core] **[BLADE: Benchmarking Language Model Agents for Data-Driven Science](https://arxiv.org/abs/2408.09667)** (2024) — Gu, K.; Shang, R.; Jiang, R.; Kuang, K.; et al.; Heer, J.; Althoff, T. *arXiv 2408.09667*
  `paper` · `advanced` · `access: open` · `AI angle`
  Benchmark of 12 datasets and research questions with expert-coded ground truth on analytic choices. LLM agents tend to stick to basic analyses and explore fewer defensible alternatives than experts.
  *Use in wiki:* Connects to many-analyst and garden-of-forking-paths themes: ask an agent and a teammate to analyze the same question and compare the choices they make.

- [core] **[How Do Analysts Understand and Verify AI-Assisted Data Analyses?](https://arxiv.org/abs/2309.10947)** (2024) — Gu, K.; Shang, R.; Althoff, T.; Wang, C.; Drucker, S. M. *CHI 2024*
  `paper` · `intermediate` · `access: open` · `AI angle`
  Qualitative study of 22 analysts using a design probe that shows AI explanations, code, plots and interactive tables. It documents how analysts verify AI analyses that can look right but reach wrong conclusions, and how their backgrounds shape their checks.
  *Use in wiki:* Basis for a 'verify the AI's analysis' lab: give students an AI-produced regression or segmentation with a planted error and have them apply the paper's verification behaviors.
  *Note:* Published at CHI 2024; the link is the arXiv version (v2, March 2024).

- [core] **[Generative AI for Economic Research: Use Cases and Implications for Economists](https://www.aeaweb.org/articles?id=10.1257/jel.20231736)** (2023) — Korinek, A. *Journal of Economic Literature 61(4): 1281-1317*
  `paper` · `intermediate` · `access: open` · `AI angle`
  Catalog of LLM use cases for researchers (ideation, writing, background research, coding, data analysis, math), with example prompts, a rating of each use case, and a replication package.
  *Use in wiki:* Anchor reading for using LLMs in analysis work; students try two coding or data use cases on course data and compare with Korinek's ratings.
  DOI [10.1257/jel.20231736](https://doi.org/10.1257/jel.20231736)
  *Note:* Replication package: https://doi.org/10.3886/E194623V1. Updates: June 2024 (https://www.aeaweb.org/articles/materials/21298) and December 2024 'LLMs Learn to Collaborate and Reason' (https://www.aeaweb.org/articles/materials/22146). Access to the JEL article may depend on AEA or library access, but the updates are open.

- [recommended] **[Automated Social Science: Language Models as Scientist and Subjects](https://arxiv.org/abs/2404.11794)** (2024) — Manning, B. S.; Zhu, K.; Horton, J. J. *arXiv 2404.11794*
  `paper` · `advanced` · `access: open` · `AI angle`
  An LLM system generates hypotheses, builds structural causal models, runs simulated experiments with LLM agents (negotiation, bail, interviews, auctions) and estimates effects. The LLM gets effect directions right but not magnitudes until it is given the fitted model.
  *Use in wiki:* M6/M8 discussion of AI-run experiments and synthetic subjects; links to marketing debates on synthetic respondents.

- [recommended] **[CORE-Bench: Fostering the Credibility of Published Research Through a Computational Reproducibility Agent Benchmark](https://arxiv.org/abs/2409.11363)** (2024) — Siegel, Z. S.; Kapoor, S.; Nadgir, N.; Stroebl, B.; Narayanan, A. *arXiv 2409.11363*
  `paper` · `advanced` · `access: open` · `AI angle`
  270 tasks from 90 papers in CS, social science and medicine test whether agents can reproduce published results from code and data. The best agent reached 21% on the hardest tasks.
  *Use in wiki:* Frames the team project's GitHub deliverable: can an agent, or a classmate, reproduce your blog post's results from your repo?
  *Note:* v2 dated 22 June 2026.

- [recommended] **[DSBench: How Far Are Data Science Agents from Becoming Data Science Experts?](https://arxiv.org/abs/2409.07703)** (2024) — Jing, L.; Huang, Z.; Wang, X.; Yao, W.; Yu, W.; Ma, K.; Zhang, H.; Du, X.; Yu, D. *arXiv 2409.07703*
  `paper` · `advanced` · `access: open` · `AI angle`
  Benchmark of realistic data analysis and modeling tasks; at publication the best agent solved only 34.12% of data analysis tasks.
  *Use in wiki:* Instructor background; one or two DSBench-style tasks could be adapted as in-class challenges.
  *Note:* Scores are from 2024 to 2025 models and are now outdated.

- [optional] **[Benchmarking Data Science Agents (DSEval)](https://arxiv.org/abs/2402.17168)** (2024) — Zhang, Y.; Jiang, Q.; Han, X.; Chen, N.; Yang, Y.; Ren, K. *arXiv 2402.17168*
  `paper` · `advanced` · `access: open` · `AI angle`
  Introduces DSEval, an evaluation paradigm and benchmarks covering the full data science lifecycle, with a summary of common agent failure modes.
  *Use in wiki:* Instructor background; its failure taxonomy can seed a 'common AI mistakes in pandas' checklist.

- [optional] **[DA-Code: Agent Data Science Code Generation Benchmark for Large Language Models](https://arxiv.org/abs/2410.07331)** (2024) — Huang, Y.; Luo, J.; Yu, Y.; Zhang, Y.; Lei, F.; Wei, Y.; He, S.; Huang, L.; Liu, X.; Zhao, J.; Liu, K. *arXiv 2410.07331*
  `paper` · `advanced` · `access: open` · `AI angle`
  Agent-based data science benchmark (wrangling, EDA, ML); the best LLMs reached 30.5% accuracy at release.
  *Use in wiki:* Instructor background on which data-science steps agents fail most.
  *Note:* Project site: https://da-code-bench.github.io. Repository license not checked.

- [optional] **[Is GPT-4 a Good Data Analyst?](https://arxiv.org/abs/2305.15038)** (2023) — Cheng, L.; Li, X.; Bing, L. *arXiv 2305.15038*
  `paper` · `intermediate` · `access: open` · `AI angle`
  Early test of GPT-4 as an end-to-end data analyst against professional human analysts; it was comparable on the paper's metrics, though the authors stop short of saying it can replace analysts.
  *Use in wiki:* Historical marker for how quickly 'AI analyst' claims evolved; pair with Gu et al. on verification.

- [optional] **[DS-1000: A Natural and Reliable Benchmark for Data Science Code Generation](https://arxiv.org/abs/2211.11501)** (2022) — Lai, Y.; Li, C.; Wang, Y.; Zhang, T.; Zhong, R.; Zettlemoyer, L.; Yih, S. W.; Fried, D.; Wang, S.; Yu, T. *arXiv 2211.11501*
  `paper` · `intermediate` · `access: open` · `AI angle`
  1,000 StackOverflow-derived data science problems across seven Python libraries (NumPy, pandas, etc.), graded by execution; Codex-002 scored 43.3% at release.
  *Use in wiki:* Sample problems make good warm-up exercises: students solve one with and without AI and check against the tests.
  DOI [10.48550/arXiv.2211.11501](https://doi.org/10.48550/arXiv.2211.11501) · [Open-access copy](https://arxiv.org/abs/2211.11501)
  *Note:* Project site: https://ds1000-code-gen.github.io. Published at ICML 2023 per common citation, which wasn't confirmed on the arXiv page.
