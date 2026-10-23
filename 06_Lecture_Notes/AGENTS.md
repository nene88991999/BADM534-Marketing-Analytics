# Agent Guide for Lecture Notes

Read the root `AGENTS.md` and `course.json` first. These lecture notes are by Nathan Yang. The historical syllabus determines topic coverage only; it does not establish current requirements. Practice questions and explanations here are public teaching examples.

## Source and Output Files

- Edit `modules/M*.md` as the primary prose source. Keep module IDs and numbered section references stable when practical.
- Edit `figures/M*.tex` for figures and `figures/style.tex` for shared styling. Keep the PNG filename synchronized with the Markdown image link.
- Run `build_notes.py` to regenerate `BADM534_Lecture_Notes.tex` and the PDF. Do not make prose changes only in the generated LaTeX file.
- Use `--figures` when a TikZ figure changes. The PDF and Markdown previews should represent the same figure.
- Intermediate build products belong in ignored `build/`. Do not commit local runtime tools or private source documents.

## Teaching and Verification

Begin with the managerial choice and the comparison needed to inform it. Define units, timing, populations, and conditioning before interpreting a numerical result. Keep descriptive relationships, predictive performance, causal effects, imposed model examples, and published findings distinct.

Use connected prose, title-case headings, and explicit first-paragraph `\noindent` in generated LaTeX. Avoid em dashes and stock contrast constructions. Omit editorial meta-comments throughout the lecture text: no module previews, remarks about how the notes were prepared, draft labels, cover footers describing the document, or narration such as “this module develops” and “the figure illustrates.” State the substantive mechanism directly. Keep numerical assumptions, synthetic-data labels where needed, and material qualifications beside the results they constrain. Introduce equations through their purpose and interpret their terms immediately afterward.

Use figures to explain a mechanism or comparison that benefits from visual reasoning. State what varies, what is held fixed, and whether the result is synthetic. Follow the official Illinois palette and use labels, markers, or line styles in addition to color. Retain figure descriptions in the Markdown prose for accessibility and LLM use.

Reproduce changed numerical examples with `../03_Data_and_Code/Lecture_Examples/verify_examples.py`, adding independent checks when appropriate. Inspect source assumptions before treating agreement with code as substantive validation. Compile and visually inspect the final PDF and all changed figure previews. Do not claim to have executed a downloaded reference notebook merely because a small teaching calculation ran.

Preserve original author attribution and source URLs. The user-supplied writing preferences and published papers guide prose and selected case motivation; they do not authorize copying full texts into this repository.

## Data Examples and Nutrition Screens

Whenever an example uses data, include detailed runnable Python directly in the Markdown notes and maintain a matching script. Define loading, sample restrictions, transformations, estimands, units, outputs, and checks. Keep the visible `Python source:` label so `scripts/check_lecture_code.py` can verify the code against its file. Run the affected calculation and update its aggregate results.

The mHealth cohort and shared functions are in `../03_Data_and_Code/mHealth/recurring_examples`. Keep data-cleaning flags separate from analysis exclusions. Nutrition screens require a stated instrument, population, and information set; missing physiological inputs must remain missing. Label imposed screening bounds, simulations, and financial inputs explicitly. Preserve the distinction between observed logging, recorded diet, usual intake, prediction, and causal health effects.
