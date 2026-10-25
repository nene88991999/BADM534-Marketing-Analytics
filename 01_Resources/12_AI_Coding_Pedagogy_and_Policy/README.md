# AI-Assisted Coding · Teaching, Learning and Policy

29 resources (9 core). Built 2026-10-25 from `00_Index/_data/`; edit the YAML there and rerun `00_Index/_build/build_catalog.py` rather than editing this file.

Priority: **core** = likely to assign or build on; **recommended** = strong supplement; **optional** = background or niche. *Access* tells you whether students can open it without a login.

## Contents

- [Evidence: learning with AI](#evidence-learning-with-ai) (12)
- [Course exemplars and AI tutors](#course-exemplars-and-ai-tutors) (5)
- [Assignment and assessment design](#assignment-and-assessment-design) (8)
- [Illinois and Gies policy](#illinois-and-gies-policy) (4)

## Evidence: learning with AI

- [core] **[How AI assistance impacts the formation of coding skills (paper: How AI Impacts Skill Formation)](https://www.anthropic.com/research/AI-assistance-coding-skills)** (2026) — Shen, J. H.; Tamkin, A. (Anthropic). *Anthropic Research; arXiv 2601.20245*
  `paper` · `intermediate` · `access: open` · `AI angle`
  RCT with 52 mostly junior Python engineers learning the Trio library. Those with an AI assistant scored about 17 points lower on a follow-up quiz (about 50% vs. 67%), with the biggest gap on debugging, and weren't significantly faster. People who asked conceptual questions kept their learning; those who fully delegated did not.
  *Use in wiki:* Central evidence for the course's 'ask for explanations, not just code' norm; show the six interaction patterns and have students self-classify their own AI logs.
  [Open-access copy](https://arxiv.org/abs/2601.20245)
  *Note:* Anthropic blog post 29 January 2026; arXiv v1 28 January 2026, v2 1 February 2026.

- [core] **[Generative AI without guardrails can harm learning: Evidence from high school mathematics](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4895486)** (2025) — Bastani, H.; Bastani, O.; Sungu, A.; et al. *PNAS*
  `paper` · `intermediate` · `access: open` · `AI angle`
  Field experiment with about 1,000 Turkish high school math students: unrestricted GPT-4 ('GPT Base') raised practice scores 48% but lowered later unassisted exam scores 17%. A tutor version with teacher-designed hints ('GPT Tutor') raised practice 127% with no exam penalty.
  *Use in wiki:* Required reading for the course's AI policy: explains why labs use hint-first tutors and unassisted checkpoints. Also a clean M6 example of a three-arm field experiment.
  *Note:* The PNAS pages wouldn't load from this environment, so the URL is the SSRN working paper 'Generative AI Can Harm Learning', linked from Wharton Knowledge (https://knowledge.wharton.upenn.edu/article/without-guardrails-generative-ai-can-harm-education/) and from Mollick's 'Post-apocalyptic education'. PNAS title and venue as given in the brief; DOI and full author list not verified here.

- [core] **[The Widening Gap: The Benefits and Harms of Generative AI for Novice Programmers](https://arxiv.org/abs/2405.17739)** (2024) — Prather, J.; Reeves, B.; Leinonen, J.; MacNeil, S.; Randrianasolo, A. S.; Becker, B.; Kimmel, B.; Wright, J.; Briggs, B. *ICER 2024*
  `paper` · `intermediate` · `access: open` · `AI angle`
  Eye-tracking and interview study of 21 novices: students who already had a plan used GenAI to speed up, while struggling students were further derailed, often ending with an 'illusion of competence'.
  *Use in wiki:* Motivates mandatory 'plan first, then prompt' steps and short self-explanation checks in labs; shows students the gap they may fall into.
  *Note:* Published at ICER 2024; the link is the arXiv preprint.

- [recommended] **[Linear walkthroughs (Agentic Engineering Patterns)](https://simonwillison.net/guides/agentic-engineering-patterns/linear-walkthroughs/)** (2026) — Willison, S. *Simon Willison's Weblog (guides)*
  `tutorial` · `intro` · `access: open` · `AI angle`
  A pattern for having an agent produce a structured, step-by-step walkthrough of a codebase so a human can actually understand code they didn't write. The companion chapter 'Interactive explanations' covers the same goal interactively.
  *Use in wiki:* Required step before submission: students generate a walkthrough of their own analysis notebook, then annotate where they agree or disagree, which serves as a comprehension check.
  *Note:* Posted 25 February 2026. Summary based on the chapter title and guide context; the chapter text itself wasn't fetched. Companion: https://simonwillison.net/guides/agentic-engineering-patterns/interactive-explanations/

- [recommended] **[Anthropic Education Report: How University Students Use Claude](https://www.anthropic.com/news/anthropic-education-report-how-university-students-use-claude)** (2025) — Anthropic. *Anthropic*
  `report` · `intro` · `access: open` · `AI angle`
  Privacy-preserving analysis of student conversations: CS students are heavily overrepresented, about 47% of conversations are 'direct' (answer-seeking), and Claude mostly performs higher-order Bloom's tasks (creating, analyzing), raising concerns about offloading.
  *Use in wiki:* Discussion opener on how students actually use AI, and an M5 example of classifying text at scale.
  *Note:* Published 8 April 2025. The CS share appears as both 36.8% and 38.6% within the report.

- [recommended] **[The Impact of Generative AI on Critical Thinking: Self-Reported Reductions in Cognitive Effort and Confidence Effects From a Survey of Knowledge Workers](https://www.microsoft.com/en-us/research/publication/the-impact-of-generative-ai-on-critical-thinking-self-reported-reductions-in-cognitive-effort-and-confidence-effects-from-a-survey-of-knowledge-workers/)** (2025) — Lee, H.-P.; Sarkar, A.; Tankelevitch, L.; Drosos, I.; Rintel, S.; Banks, R.; Wilson, N. *CHI 2025*
  `paper` · `intermediate` · `access: open` · `AI angle`
  Survey of 319 knowledge workers (936 examples): more confidence in GenAI predicts less critical thinking, more self-confidence predicts more. GenAI shifts effort toward verifying, integrating and 'stewarding' output.
  *Use in wiki:* Short reading for business students on how over-trust erodes review; supports building verification into every assignment.
  [Open-access copy](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/01/lee_2025_ai_critical_thinking_survey.pdf)

- [recommended] **[Your Brain on ChatGPT: Accumulation of Cognitive Debt when Using an AI Assistant for Essay Writing Task](https://arxiv.org/abs/2506.08872)** (2025) — Kosmyna, N.; Hauptmann, E.; Yuan, Y. T.; Situ, J.; Liao, X.-H.; Beresnitzky, A. V.; Braunstein, I.; Maes, P. *arXiv 2506.08872 (MIT Media Lab)*
  `paper` · `intermediate` · `access: open` · `AI angle`
  EEG study of 54 participants writing essays with an LLM, a search engine, or no tools. LLM users showed the weakest brain connectivity, the lowest sense of ownership and trouble quoting their own essays; the authors call this 'cognitive debt'.
  *Use in wiki:* Use as a critical-reading exercise: students evaluate the design (small sample, 18 in the crossover session, essay task, preprint) before accepting the headlines.
  *Note:* Not peer reviewed as of v2 (31 December 2025). MIT Media Lab project page: https://www.media.mit.edu/projects/your-brain-on-chatgpt/overview/. Published critiques couldn't be verified in this pass because the search budget ran out; the course should add one before assigning.

- [recommended] **[Computing Education in the Era of Generative AI](https://arxiv.org/abs/2306.02608)** (2024) — Denny, P.; Prather, J.; Becker, B. A.; Finnie-Ansley, J.; Hellas, A.; Leinonen, J.; Luxton-Reilly, A.; Reeves, B. N.; Santos, E. A.; Sarsa, S. *Communications of the ACM*
  `paper` · `intro` · `access: open` · `AI angle`
  Accessible overview of what code-generating models mean for programming instructors, summarizing studies of model performance on intro problems and of AI-generated learning resources.
  *Use in wiki:* Instructor-only background for course design decisions.
  *Note:* Published in Communications of the ACM (2024). The link is the arXiv preprint (June 2023) because the ACM Digital Library blocked automated access.

- [recommended] **[From 'Ban It Till We Understand It' to 'Resistance is Futile': How University Programming Instructors Plan to Adapt as More Students Use AI Code Generation and Explanation Tools such as ChatGPT and GitHub Copilot](https://pg.ucsd.edu/publications/cs-instructors-adapting-to-chatgpt-copilot-ai-tools_ICER-2023.pdf)** (2023) — Lau, S.; Guo, P. J. *ICER 2023*
  `paper` · `intro` · `access: open` · `AI angle`
  Interviews with university programming instructors on short- and long-term plans for AI coding tools, from banning them to fully embracing them.
  *Use in wiki:* Instructor-only map of policy options; useful when writing the syllabus AI section.
  *Note:* Related: Lau & Guo, 'The Design Space of LLM-Based AI Coding Assistants: An Analysis of 90 Systems' (VL/HCC 2025), https://pg.ucsd.edu/publications/ai-coding-assistants-design-space_VLHCC-2025.pdf

- [recommended] **[Six Opportunities for Scientists and Engineers to Learn Programming Using AI Tools such as ChatGPT](https://pg.ucsd.edu/publications/scientists-engineers-learning-programming-using-ai_CiSE-2023.pdf)** (2023) — Guo, P. J. *IEEE Computing in Science & Engineering*
  `paper` · `intro` · `access: open` · `AI angle`
  Short essay on how people who program as a means to an end (scientists, engineers, and by extension analysts) can use AI tools to learn programming.
  *Use in wiki:* Good fit for the course's non-CS audience; assign in Week 1 alongside Willison.

- [recommended] **[Studying the Effect of AI Code Generators on Supporting Novice Learners in Introductory Programming](https://arxiv.org/abs/2302.07427)** (2023) — Kazemitabaar, M.; Chow, J.; Ma, C. K. T.; Ericson, B. J.; Weintrop, D.; Grossman, T. *CHI 2023*
  `paper` · `intermediate` · `access: open` · `AI angle`
  Controlled study of 69 learners aged 10 to 17 on 45 Python tasks: Codex access raised completion (about 1.15x) and scores (about 1.8x) without hurting manual code-modification skills. Retention a week later was slightly, not significantly, higher.
  *Use in wiki:* A counterweight to the harm studies; discuss what differs (scaffolded tasks, novices, manual-modification checks).
  DOI [10.1145/3544548.3580919](https://doi.org/10.1145/3544548.3580919)

- [optional] **[Anthropic Education Report: How educators use Claude](https://www.anthropic.com/news/anthropic-education-report-how-educators-use-claude)** (2025) — Anthropic. *Anthropic*
  `report` · `intro` · `access: open` · `AI angle`
  About 74,000 higher-education conversations plus Northeastern faculty interviews: curriculum development dominates, educators build interactive artifacts (simulations, quizzes, dashboards), and grading is the use faculty trust least.
  *Use in wiki:* Instructor background and validation for building the course itself as interactive HTML artifacts.
  *Note:* Published 27 August 2025.

## Course exemplars and AI tutors

- [core] **[CS146S: The Modern Software Developer](https://themodernsoftware.dev/)** (2026) — Eric, M. (Stanford University). *Stanford University*
  `course` · `intermediate` · `access: open` · `AI angle`
  Stanford course, first offered Fall 2025 and again in Fall 2026, on building software with LLM coding agents: MCP, agent skills, spec-driven development, loop engineering and the 'software factory', with hands-on assignments, industry guest talks and a final project.
  *Use in wiki:* Benchmark for topic coverage and sequencing; borrow the spec-driven and context-engineering units at a business-analytics level.
  *Note:* Fall 2025 archive: https://themodernsoftware.dev/fall2025. No AI policy, weekly syllabus or GitHub repo visible from the fetched pages.

- [recommended] **[Claude Code and What Comes Next](https://www.oneusefulthing.org/p/claude-code-and-what-comes-next)** (2026) — Mollick, E. *One Useful Thing*
  `newsletter` · `intro` · `access: open` · `AI angle`
  Mollick watches Claude Code (Opus 4.5) build and deploy a working sales website from one request. He explains context compaction, Skills and subagents, and argues that agentic coding tools preview changes to all knowledge work.
  *Use in wiki:* Accessible intro to agents for business students before the first Claude Code lab.
  *Note:* Published 7 January 2026. Related: 'A Guide to Which AI to Use in the Agentic Era' (https://www.oneusefulthing.org/p/a-guide-to-which-ai-to-use-in-the), updated periodically.

- [recommended] **[Teaching CS50 with AI: Leveraging Generative Artificial Intelligence in Computer Science Education](https://cs.harvard.edu/malan/publications/V1fp0567-liu.pdf)** (2024) — Liu, R.; et al. (Harvard CS50; Malan, D. J.). *SIGCSE 2024*
  `paper` · `intro` · `access: open` · `AI angle`
  How Harvard's CS50 deployed AI tools, including the CS50 Duck rubber-duck debugger, built to guide students toward solutions rather than hand them answers, and how students responded.
  *Use in wiki:* Model for a course-specific hint-first AI tutor (for example a Claude Project or custom GPT with a 'don't give full solutions' system prompt) for Marketing Analytics labs.
  *Note:* Full author list not captured, so check the PDF. Follow-up: 'Improving AI in CS50: Leveraging Human Feedback for Better Learning' (SIGCSE 2025), https://cs.harvard.edu/malan/publications/fp0627-liu.pdf

- [optional] **[Introducing Claude for Education (learning mode)](https://www.anthropic.com/news/introducing-claude-for-education)** (2025) — Anthropic. *Anthropic*
  `documentation` · `intro` · `access: open` · `AI angle`
  April 2025 announcement of Claude for Education and its 'learning mode', which guides students' reasoning with Socratic questions instead of giving answers.
  *Use in wiki:* Option for a hint-first course tutor, but note that UIUC does not list Claude among licensed tools, so students would need personal accounts.

- [optional] **[Solve It With Code (Solveit)](https://solve.it.com/)** (2025) — Howard, J.; Whitaker, J.; Ries, E. (Answer.AI). *Answer.AI*
  `course` · `intro` · `access: paid` · `AI angle`
  Five-week course and platform built around the 'Solveit method': use AI to become a better problem solver rather than outsource thinking. Write one or two lines at a time, check results right away, then package working steps into functions. Draws on Pólya's How to Solve It.
  *Use in wiki:* Pedagogical model for small-step, check-as-you-go AI coding in Colab labs.
  *Note:* Signups were closed when checked; the page gives conflicting price information ($500 course vs. $10/month platform).

## Assignment and assessment design

- [core] **[Best Practice: Acknowledge AI Use and Cite AI-Generated Content (Illinois)](https://genai.illinois.edu/best-practice-acknowledge-ai-use-and-cite-ai-generated-content/)** (2026) — University of Illinois, Office of the CIO. *genai.illinois.edu*
  `website` · `intro` · `access: open` · `AI angle`
  Campus guidance on disclosure: name the tool, how it was used and how much it shaped the result, optionally with prompts. Links an AI-use worksheet (draft and Google Forms versions) and discourages AI detectors and AI-plagiarism accusations.
  *Use in wiki:* Base the course's AI-use statement template (blog-post footer plus README section) on this page and its worksheet.
  *Note:* No date on the page; the linked citation-style guidance was current as of March 2024.

- [core] **[The AI Assessment Scale (AIAS)](https://aiassessmentscale.com/)** (2025) — Perkins, M.; Furze, L.; Roe, J.; MacVaugh, J. *aiassessmentscale.com; JUTLP 2025*
  `website` · `intro` · `access: open` · `CC BY-NC-SA 4.0 (diagrams and resource assets only)` · `AI angle`
  Widely adopted five-level scale for how much AI an assessment allows: No AI, AI Planning, AI Collaboration, Full AI, AI Exploration. Now at version 2.1.
  *Use in wiki:* Tag every Marketing Analytics assignment with an AIAS level on the wiki (for example, concept checks at Level 1, labs at Level 3 or 4, the team project at Level 5).
  [Open-access copy](https://arxiv.org/abs/2312.07086)
  *Note:* Updated paper 'Reimagining the AIAS' (JUTLP 2025): https://doi.org/10.53761/rrm4y757. Resources: https://aiassessmentscale.com/resources/

- [core] **[Assigning AI: Seven Approaches for Students, with Prompts](https://arxiv.org/abs/2306.10052)** (2023) — Mollick, E.; Mollick, L. *arXiv 2306.10052 (also SSRN)*
  `paper` · `intro` · `access: open` · `AI angle`
  Seven roles for AI in courses (tutor, coach, mentor, teammate, tool, simulator, student), each with sample prompts, benefits and risks, plus risk-management advice that keeps students 'in the loop'.
  *Use in wiki:* Framework for labeling each wiki activity by the AI role it uses; the AI-student role (students teach or correct the AI) suits code review.

- [recommended] **[claude-code-transcripts: tools for publishing transcripts of Claude Code sessions](https://github.com/simonw/claude-code-transcripts)** (2025) — Willison, S. *GitHub*
  `tool` · `intermediate` · `access: open` · `Apache-2.0` · `AI angle`
  Command-line tool (uvx claude-code-transcripts) that turns local Claude Code session files into paginated HTML transcripts, with a timeline of prompts and commits.
  *Use in wiki:* Make it the standard way students attach AI-use logs to team-project repos, so graders can see the prompts behind each commit.
  Tools: Claude Code, uv
  *Note:* Launched around 25 December 2025. The 'web' commands were broken at the time of checking (unofficial API changes); the 'local' command is what students would use.

- [recommended] **[4 Steps to Design an AI-Resilient Learning Experience (with Data Analytics toolkit example)](https://mitsloanedtech.mit.edu/ai/teach/4-steps-to-design-an-ai-resilient-learning-experience/)** (2024) — MIT Sloan Teaching & Learning Technologies. *MIT Sloan Teaching & Learning Technologies*
  `tutorial` · `intro` · `access: open` · `AI angle`
  Backward-design guide: learners, outcomes (Bloom's higher levels), assessments (AI required, allowed or banned for each), activities. Comes with a Word toolkit and a worked Data Analytics course example.
  *Use in wiki:* Use the Data Analytics toolkit example (https://mitsloanedtech.mit.edu/wp-content/uploads/2024/03/AIHub_ToolkitExampleDataAnalytics.pdf) as a template when redesigning each Marketing Analytics module.
  *Note:* Toolkit files dated March 2024; page modified September 2026. Toolkit (docx): https://mitsloanedtech.mit.edu/wp-content/uploads/2024/03/AIHub_AI-ResilientLXDesignToolkit.docx

- [recommended] **[AI Detectors Don't Work. Here's What to Do Instead.](https://mitsloanedtech.mit.edu/ai/teach/ai-detectors-dont-work/)** (2024) — MIT Sloan Teaching & Learning Technologies. *MIT Sloan Teaching & Learning Technologies*
  `tutorial` · `intro` · `access: open` · `AI angle`
  Business-school guidance explaining why AI detectors are unreliable and offering strategies for academic honesty in their place.
  *Use in wiki:* Instructor reference that backs the decision not to use detectors, consistent with Illinois guidance.
  *Note:* Original publication year not shown (page modified 14 September 2026).

- [recommended] **[Post-apocalyptic education](https://www.oneusefulthing.org/p/post-apocalyptic-education)** (2024) — Mollick, E. *One Useful Thing*
  `newsletter` · `intro` · `access: open` · `AI angle`
  Argues that the 'homework apocalypse' has arrived and describes two illusions: that teachers can detect AI work, and that students learn from AI answers. Suggests tutor-style prompts and in-class verification instead.
  *Use in wiki:* Instructor background for the assessment plan. A reader comment by Tyler Ransom describes AI-permitted coding assignments followed by one-on-one oral exams, a model worth copying.
  *Note:* Published 30 August 2024. Links to research on AI detection and to the Bastani SSRN paper.

- [recommended] **[AI Pedagogy Project](https://aipedagogy.org/)** (2023) — metaLAB (at) Harvard, Berkman Klein Center. *metaLAB (at) Harvard*
  `website` · `intro` · `access: open` · `AI angle`
  Curated, open-access library of about 40 classroom assignments that use AI critically, plus an AI Guide (AI Starter, LLM comparison, resources).
  *Use in wiki:* Source of adaptable activities, for example 'Questioning the Bot' (https://aipedagogy.org/assignment/questioning-the-bot-socratic-chats-with-ai-2/) recast as interrogating an AI's regression interpretation.
  *Note:* Few coding- or data-specific assignments on the first page of the listing. Reuse terms are on https://aipedagogy.org/using-our-content/

## Illinois and Gies policy

- [core] **[Enterprise GenAI: AI Apps (University of Illinois)](https://genai.illinois.edu/ai-apps/)** (2026) — University of Illinois, Office of the CIO. *genai.illinois.edu*
  `website` · `intro` · `access: open` · `AI angle`
  Official list of approved AI tools and data classifications. For students: Microsoft Copilot Chat, Illinois Chat, Google Gemini, Google NotebookLM and Zoom AI Companion, plus Illinois Computes for grad students. Faculty and staff only: Illinois ChatGPT ($11/month), Microsoft 365 Copilot add-on, and GitHub Copilot (security review advised).
  *Use in wiki:* Link from the wiki's 'Tools and accounts' page; Gemini (Internal and Public data) is the licensed path for Colab-adjacent work, and Claude and ChatGPT Edu are not on the student list.
  *Note:* Checked 2026-10-23: Claude isn't listed; ChatGPT is faculty and staff only. Gemini page (https://genai.illinois.edu/ai-apps-google-gemini/) says Public and Internal data only, Illinois-managed account required, and doesn't mention Gemini in Colab or Gemini CLI. Illinois Chat: https://chat.illinois.edu/. Students can get GitHub Copilot separately through GitHub Education (not verified here).

- [core] **[Integrate AI into your Teaching (CITL, Illinois)](https://citl.illinois.edu/integrate-ai-your-teaching)** (2026) — Center for Innovation in Teaching & Learning, University of Illinois. *citl.illinois.edu*
  `website` · `intro` · `access: open` · `AI angle`
  CITL guidance (updated 17 August 2026): avoid blanket bans, specify when and how AI may be used, and redesign assignments toward presentations, applied group work and visible learning. Links syllabus resources, including Gies syllabus guidance and College of Law sample statements.
  *Use in wiki:* Primary campus reference for the syllabus and assessment design; CITL also offers consultations and departmental workshops.
  *Note:* The older CITL ChatGPT page linked from genai.illinois.edu now redirects to the CITL home page. Related: AI Curriculum and Training (https://citl.illinois.edu/ai-curriculum-and-training), Generative AI Fluency Modules (https://citl.illinois.edu/generative-ai-fluency-modules), College of Law sample syllabus statements (https://publish.illinois.edu/ai-law-teaching/syllabus-statements/).

- [recommended] **[Best Practices in Teaching and Learning (Enterprise GenAI, Illinois)](https://genai.illinois.edu/best-practices-teaching-and-learning/)** (2026) — University of Illinois, Office of the CIO. *genai.illinois.edu*
  `website` · `intro` · `access: open` · `AI angle`
  Campus framework of principles (GenAI literacy, academic integrity, keeping humans active, inclusion, data privacy) with practice pages: notify learners of expectations, acknowledge AI use, foster critical evaluation, use AI for assessment and feedback.
  *Use in wiki:* Cite in the syllabus AI policy so it lines up with campus expectations.
  *Note:* No date on the page. Expectations page: https://genai.illinois.edu/best-practice-notify-learners-of-expectations-for-using-generative-ai-to-support-learning/

- [recommended] **[Gies Generative AI Guiding Principles](https://answers.uillinois.edu/gies/128405)** (2025) — Gies College of Business, University of Illinois. *Illinois Answers (Gies KB 128405)*
  `website` · `intro` · `access: open` · `AI angle`
  College-level infographic and links for instructors, including Gies syllabus guidance on setting permitted AI uses, having students document and cite AI use, and checking AI output for accuracy.
  *Use in wiki:* Make sure the Marketing Analytics AI policy is consistent with college principles; link from the syllabus.
  *Note:* Created 19 May 2023; last updated 6 November 2025. Some linked tool names (for example Google Bard) are dated.
