# Agent Guide for Slides

Read the root `AGENTS.md`, `course.json`, the session plan, and the relevant module notes. Use Marketing Analytics as the title and By Nathan Yang as the author. Keep the course code out of decks and notes.

## Content and Course Authority

The plan has 15 meetings of 170 minutes, based on the historical syllabus. It includes 13 instructional meetings and two provisional presentation meetings. There are no guest speakers. The Spring 2027 meeting dates are available in the session plan. Graded presentation requirements, weights, deadlines, and course-wide AI policy remain pending. Preserve that distinction when answering students.

Begin with the managerial decision, then the information, comparison, method, and consequence. Keep claims consistent across projected text, presenter notes, Markdown companions, code, and the full module notes. Define populations, denominators, units, horizons, and synthetic inputs. Keep consequential assumptions beside the result.

Integrate new ethics and regulation material wherever it affects the methods and cases, as well as in the dedicated consumer-choice session. Verify legal propositions against primary sources and record jurisdiction, scope, status, and effective date. Use `../06_Lecture_Notes/ETHICS_AND_REGULATION.md` for the checked source record. Incorporate the instructor's own ideas without citing, naming, linking, or uploading the underlying papers.

## Format and Artwork

Use the November 2026 reference deck's 16:9 Beamer layout with 14-point base text, sans-serif typography, parchment RGB 234/220/201, Illinois Blue text, Illini Orange bullets and rules, and generous space. The reference's content does not establish course requirements. The earlier white-background guide is superseded.

Keep `theme.tex` as the common style. Preserve editable TikZ for analytical diagrams and exact Illinois palette values. Follow `ART_DIRECTION.md` for Chinese ink-and-color illustrations. Use textured brushwork, restrained washes, open space, and atmospheric distance. Keep quantitative information in analytical figures and text.

Use title case. Omit draft labels, preparation remarks, cover footers, and narration about what a slide or module will do. Substantive presenter notes follow the same prose conventions. Avoid em dashes and stock contrast constructions.

## Editing and Verification

Edit `source/sessions.json` as the primary slide content. The builder generates same-stem `.tex` and `.md` companions and compiles each PDF. Edit `theme.tex` for shared layout and `../06_Lecture_Notes/figures/` for shared diagrams. The Markdown companions must include projected text, equations, tables, code, substantive notes, and figure descriptions.

Keep runnable examples in `../03_Data_and_Code`, with inputs, outputs, and commands. Short projected snippets supplement the full programs. Run affected code, check figures against aggregate tables, compile all affected decks, and inspect every changed page. Check presenter mode when modifying notes layout. Keep build files and preview images in ignored directories.

Update README, `SESSION_PLAN.md`, `session_plan.json`, and `course.json` together when changing coverage. Regenerate `llms-full.txt` from the reviewed publication snapshot. Preserve concurrent resource-library edits and instructor-only folders.

Keep historical reference templates in Dropbox only. They do not establish course dates, requirements, or content.

Use “assessment” for data-quality and evidence checks, and “evaluation” for model, policy, and customer-outcome comparisons. Use “assess” and “evaluate” as the corresponding verbs. Apply this terminology consistently in headings, prose, code examples, and output names; preserve original third-party titles and quotations.
