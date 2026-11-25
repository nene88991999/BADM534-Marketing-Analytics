## Selected Readings by Analytical Question

- **Marketing Decisions and Python.** {{python-marketing-research-analytics}} provides notebooks and data across the core modules. {{wedel-kannan-2016-marketing-analytics-data-rich}} connects analytical methods to marketing decisions.
- **Coding Productivity.** Compare {{peng-2023-copilot-rct}}, {{cui-2025-three-field-experiments}}, and {{metr-2025-early-ai-os-developer-rct}} by task, participants, assignment, and completion time. The first reports faster completion, while the third reports a 19% slowdown. {{metr-2026-uplift-update}} develops the selection and study-design issues, and {{anthropic-claude-code-expertise-2026}} examines the role of expertise.
- **Learning and Independent Performance.** {{bastani-2025-genai-without-guardrails}} and {{shen-tamkin-2026-ai-skill-formation}} connect assisted task completion to subsequent understanding and skill. Compare the outcome measured during assistance with performance after assistance ends.
- **Verification of Generated Analysis.** {{gu-2024-analysts-verify-ai-analyses}}, {{gu-2024-blade-benchmark}}, and {{kapoor-narayanan-leakage}} motivate checks of assumptions, code, and interpretation. Students should be able to reproduce a calculation and explain why it answers the stated question.
- **Text, Preferences, and Incremental Effects.** Pair {{berger-2020-uniting-tribes}} with {{gilardi-2023-chatgpt-outperforms-crowd-workers}} for M5, and {{gui-toubia-llm-simulation-causal-inference}} with {{digital-twins-funhouse-mirrors}} for M4/M7. In M6, {{blake-nosko-tadelis-2015}}, {{lewis-rao-2015-qje}}, and {{gordon-zettelmeyer-2019-facebook}} examine advertising effects and their measurement. {{ascarza-2018-retention-futility}} explains why predicted retention and the response to intervention can rank customers differently.
- **Recommendation Quality and Customer Goals.** {{wang-li-chen-2025-recpie-explanations}} examines explanations, {{chaney-stewart-engelhardt-2018-algorithmic-confounding}} studies feedback from exposure, and {{aridor-2022-movielens-field-experiment}} provides an experimental comparison. Evaluate customer goals and variety alongside prediction accuracy.
- **Python Implementations.** {{packt-data-analytics-for-marketing-2024}} and {{takeda-marketing-science-in-python}} provide book-length notebook collections. {{pyrsm-examples-ucsd-rady}} includes conjoint and multinomial-logit examples; {{katsov-tensor-house}} covers pricing and promotions. {{google-meridian-geox}}, {{feedx-shopping-feed-experiments}}, and {{orduz-website-projects-marketing-notebooks}} provide experimental and marketing applications. Adjacent source records identify local copies and licensing.
- **Agent Instructions and Verification.** {{claude-code-best-practices}}, {{willison-agentic-engineering-patterns}}, and {{agents-md}} inform project instructions and reproducible coding workflows.
- **Interactive Publishing.** Compare {{quarto}} with {{quarto-live}}, {{jupyter-book-2}}, and {{jupyterlite-demo-template}} by the code students need to execute, installation requirements, and accessibility.

## 2026 Changes That Affect the Course Design

All of these were checked against primary or dated sources on 2026-10-23. Recheck them before the term starts.

1. **Which AI tools students may use with university data.** {{uiuc-genai-ai-apps}} lists Microsoft Copilot Chat, Google Gemini, NotebookLM and Illinois Chat for students. Illinois ChatGPT and GitHub Copilot are licensed for faculty and staff only. Claude, Cursor and Codex are not on the list. That matters as soon as students touch real customer data from a project partner.
2. **GitHub Copilot for students is still free but more limited.** Since June 2026 it runs on monthly AI credits with automatic model selection ({{github-copilot-student-plan}}).
3. **Google Tool Availability.** Gemini CLI was replaced by Antigravity CLI for free and consumer users on 18 June 2026 ({{gemini-cli-to-antigravity-transition}}). Separately, Google offers US college students a free year of Google AI Pro if claimed by 31 Dec 2026.
4. **Consolidation among coding tools.** SpaceX agreed in June 2026 to buy Cursor, which then restructured its pricing in October 2026 ({{cursor-pricing-2026}}). Windsurf is now Devin Desktop ({{windsurf-devin-desktop}}), and Posit Assistant replaced Positron Assistant and Databot ({{posit-assistant-positron}}).
5. **GitHub Classroom was deprecated on 27 Aug 2026.** Assignment distribution needs another route; see the hosting section of the wiki folder.
6. **Accessibility is now a requirement for the wiki.** Campus standards require WCAG 2.2 AA for internally built web content, including course materials ({{uiuc-minimum-digital-accessibility-standards}}). The federal ADA Title II compliance date for large public entities is now 26 April 2027 ({{ada-title-ii-web-rule}}).
7. **In-browser Python now covers the course stack.** Pyodide ships pandas, scikit-learn and statsmodels ({{pyodide-packages}}), so wiki pages can run real exercises with nothing to install. On the documentation-tool side, Material for MkDocs is now in maintenance mode and Jupyter Book 2 (MyST) has shipped.
8. **M8 Topics.** Chrome is keeping third-party cookies and retiring most Privacy Sandbox APIs ({{privacy-sandbox-update-2025}}). Agentic commerce ({{openai-agentic-commerce-protocol}}) and generative engine optimization ({{geo-generative-engine-optimization}}) are now live topics.

## Resource Coverage and Access

- The recorded search found no verified public syllabus for a *business-school* course built around vibe coding. {{stanford-cs146s-modern-software-developer}} is the closest model, and it is a CS course.
- The recorded search found no published rubric for grading AI-assisted coding work, and no worked, openly licensed RFM-segmentation notebook. These remain candidates for original course development.
- No paper targets AI-generated DiD or IV code specifically. The closest evidence is general statistical-reasoning benchmarks such as QRData, StatQA and BLADE.
- The searches found peer marketing-analytics course repositories only for NYU, Chicago Booth, Wharton (via Coursera) and UCSD Rady.
- Items with lingering doubts say so in their *Note* line, e.g. a venue taken from recollection or an unconfirmed dataset license.

## Catalog Verification

A separate checker re-verified a random sample of 47 entries, weighted toward core items, against the live pages, Crossref and OpenAlex. All 47 links resolved to the named resource. Five entries had a wrong field, all now corrected: two access labels (Reddit data, Sawtooth Lighthouse Studio), one open-access link that pointed to an earlier working paper, one author line and one venue. Two details could not be confirmed and are flagged in their notes. The per-entry results are in `_data/spotcheck_results_2026-10-23.yml`.
