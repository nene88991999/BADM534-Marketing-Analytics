## Start here: a short reading list

If you only open a dozen items before designing the wiki, open these.

- **The course spine in Python.** {{python-marketing-research-analytics}} covers most modules, and its Apache-2.0 notebooks and data are saved locally. {{wedel-kannan-2016-marketing-analytics-data-rich}} works as an opening framing piece.
- **What AI coding actually does to productivity.** Read {{peng-2023-copilot-rct}}, {{cui-2025-three-field-experiments}} and {{metr-2025-early-ai-os-developer-rct}} together. The first finds speed-ups, the third finds a 19% slowdown, and METR's follow-up {{metr-2026-uplift-update}} is a ready-made M6 case on selection and study design. {{anthropic-claude-code-expertise-2026}} argues that domain expertise still matters.
- **What it does to learning.** {{bastani-2025-genai-without-guardrails}} and {{shen-tamkin-2026-ai-skill-formation}} are the two strongest cautions, and they shape how AI-assisted coding should be scaffolded in a course.
- **Checking AI-written analysis.** Start with {{gu-2024-analysts-verify-ai-analyses}}, {{gu-2024-blade-benchmark}} and {{kapoor-narayanan-leakage}}. This is the course's recurring theme: AI writes the code, and the student has to be able to audit it.
- **Marketing anchors that pair well with an AI angle.** {{berger-2020-uniting-tribes}} with {{gilardi-2023-chatgpt-outperforms-crowd-workers}} (M5). {{gui-toubia-llm-simulation-causal-inference}} with {{digital-twins-funhouse-mirrors}} (M4/M7). The ad-measurement trio {{blake-nosko-tadelis-2015}}, {{lewis-rao-2015-qje}} and {{gordon-zettelmeyer-2019-facebook}} (M6). And {{ascarza-2018-retention-futility}} on why prediction is not targeting (M6/M7).
- **Working with agents.** {{claude-code-best-practices}}, {{willison-agentic-engineering-patterns}} and {{agents-md}}.
- **Wiki platform.** Look at {{quarto}} with {{quarto-live}}, {{jupyter-book-2}} and {{jupyterlite-demo-template}} side by side.

## 2026 changes that affect the course design

All of these were checked against primary or dated sources on 2026-10-23. Recheck them before the term starts.

1. **Which AI tools students may use with university data.** {{uiuc-genai-ai-apps}} lists Microsoft Copilot Chat, Google Gemini, NotebookLM and Illinois Chat for students. Illinois ChatGPT and GitHub Copilot are licensed for faculty and staff only. Claude, Cursor and Codex are not on the list. That matters as soon as students touch real customer data from a project partner.
2. **GitHub Copilot for students is still free but more limited.** Since June 2026 it runs on monthly AI credits with automatic model selection ({{github-copilot-student-plan}}).
3. **Google has reshuffled its tools.** Gemini CLI was replaced by Antigravity CLI for free and consumer users on 18 June 2026 ({{gemini-cli-to-antigravity-transition}}). Separately, Google offers US college students a free year of Google AI Pro if claimed by 31 Dec 2026.
4. **Consolidation among coding tools.** SpaceX agreed in June 2026 to buy Cursor, which then restructured its pricing in October 2026 ({{cursor-pricing-2026}}). Windsurf is now Devin Desktop ({{windsurf-devin-desktop}}), and Posit Assistant replaced Positron Assistant and Databot ({{posit-assistant-positron}}).
5. **GitHub Classroom was deprecated on 27 Aug 2026.** Assignment distribution needs another route; see the hosting section of the wiki folder.
6. **Accessibility is now a hard requirement for the wiki.** Campus standards require WCAG 2.2 AA for internally built web content, including course materials ({{uiuc-minimum-digital-accessibility-standards}}). The federal ADA Title II compliance date for large public entities is now 26 April 2027 ({{ada-title-ii-web-rule}}).
7. **In-browser Python now covers the course stack.** Pyodide ships pandas, scikit-learn and statsmodels ({{pyodide-packages}}), so wiki pages can run real exercises with nothing to install. On the documentation-tool side, Material for MkDocs is now in maintenance mode and Jupyter Book 2 (MyST) has shipped.
8. **M8 refresher.** Chrome is keeping third-party cookies and retiring most Privacy Sandbox APIs ({{privacy-sandbox-update-2025}}). Agentic commerce ({{openai-agentic-commerce-protocol}}) and generative engine optimization ({{geo-generative-engine-optimization}}) are now live topics.

## Known gaps (worth filling before or during wiki design)

- I found no verified public syllabus for a *business-school* course built around vibe coding. {{stanford-cs146s-modern-software-developer}} is the closest model, and it is a CS course.
- I found no published rubric for grading AI-assisted coding work, and no worked, openly licensed RFM-segmentation notebook. Both are good candidates for building yourself.
- No paper targets AI-generated DiD or IV code specifically. The closest evidence is general statistical-reasoning benchmarks such as QRData, StatQA and BLADE.
- The searches found peer marketing-analytics course repositories only for NYU, Chicago Booth, Wharton (via Coursera) and UCSD Rady.
- Items with lingering doubts say so in their *Note* line, e.g. a venue taken from recollection or an unconfirmed dataset license.
