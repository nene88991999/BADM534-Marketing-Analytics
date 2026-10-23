# Agent Guide for Lecture Slides

Read the root `AGENTS.md`, `course.json`, and the relevant lecture notes before authoring a deck. Use Nathan Yang's preferred LaTeX Beamer format, supplied on October 23, 2026. The original reference is retained in the instructor's Dropbox at `09_Templates/Lecture_Slides/slides.tex`; that directory stays excluded from Git. The reference's seminar topic, examples, and dates do not establish BADM 534 content or requirements.

## Layout and Typography

- Use `\documentclass[aspectratio=169,14pt]{beamer}` with the default theme and a white background.
- Keep the template's sans-serif text, large bold frame titles, navy body text, orange bullets, and thin orange rules across the top and bottom.
- Hide navigation symbols. Keep the rules free of editorial text and document-status labels.
- Use the template's `slidebullets` environment, with generous spacing and short, substantive statements. Split a crowded frame into additional slides before reducing type size.
- Preserve the reference's simple text, equation, full-width figure, and figure-with-text column layouts. Use vertical whitespace around short text sequences.
- Use title case for headings. Attribute the deck to **By Nathan Yang**. Include the actual course and lecture title; include dates only when supplied or established in current course documents.

## Colors and Figures

The user's UIUC palette requirement applies to course decks. Preserve the template's color roles while replacing its custom navy and burnt orange with Illinois Blue `#13294B` and Illini Orange `#FF5F05`. Use Storm `#707372` for secondary labels and light tints for fills. The course palette is also defined in `../06_Lecture_Notes/figures/style.tex`.

Keep diagrams editable in TikZ or PGFPlots. Use figures to explain consequential mechanisms, comparisons, or uncertainty. Adapt the lecture-note figures to the slide's available space and verify that labels remain legible. Use line styles, markers, and direct labels alongside color. Preserve units, sample restrictions, conditioning, and distinctions between synthetic illustrations and estimated results.

## Content and Presenter Notes

Start with the managerial decision and the evidence needed to inform it. Base course decks on the corresponding module in `../06_Lecture_Notes/modules/`. Explain the economic meaning of equations and calculations. Retain detailed cases, assumptions, derivations, and source references in substantive presenter notes where they exceed the projected slide's space.

Preserve the reference's `\presenterfalse` default and optional `\presentertrue` setting for notes on a second screen. Presenter notes must also follow the user's strong prohibition on meta-comments: omit draft labels, preparation remarks, teaching-stage directions, module previews, and narration such as “this slide shows.” State the substance directly. Avoid em dashes and stock “not X but Y” constructions.

## Files and Verification

Keep each course deck's editable `.tex`, PDF, and same-stem Markdown companion together in this folder. The companion should include slide anchors, substantive explanations, equations, figure descriptions, sources, and any omissions from the conversion. Keep intermediate builds in an ignored directory.

Compile the student-facing deck and inspect every slide for clipping, text density, label collisions, and legibility. Check presenter mode when changing the notes layout. Verify calculations against the associated example data and code. Update this folder's README and the course manifest when a deck is released, and regenerate the LLM context without incorporating unrelated unpublished changes.
