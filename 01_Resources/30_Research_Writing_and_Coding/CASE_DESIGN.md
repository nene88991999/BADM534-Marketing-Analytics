# A Reproducible Product-Screening Recommendation

A product manager asks which body-wash concepts should receive human research. The analyst has a small synthetic example, a working program, and a proposed recommendation. The practical question is whether another person can trace the recommendation to the inputs and reproduce it after the files move to another computer or format.

## Proposed Course Placement

Use an optional short M1 exercise to connect task specification, independent checks, and a readable project. M8 can revisit it when discussing an integrated recommendation. The activity fits any editor with a terminal and Markdown support; Suzuri is one candidate for displaying sources, code, and output together. No session allocation, graded submission, or required software has been added.

## Existing Inputs and Reference Results

Use [Synthetic Consumers](../../03_Data_and_Code/Synthetic_Consumers/README.md), whose two original programs and tests are already released. All inputs are invented. The first program maps imposed similarities to category weights and preserves persona weights. The second compares imposed rating patterns on six fictional concepts.

| Check | Expected Result | What It Establishes |
| --- | --- | --- |
| Refill response, persona p01, repeat 1, Set 1 | Expected rating 4.25 | A hand calculation agrees with the mapping program |
| Refill concept, Set 1 | Equal-persona mean 3.975 | An identical repeat does not give its persona extra weight |
| Pooled concept pattern | Undefined correlation and an unresolved shortlist | Constant means supply no ranking |
| Reversed concept pattern | F and E selected; zero of the reference top two retained | Matching overall category shares can still support the wrong shortlist |

These are reference values from the existing course example. They evaluate the supplied calculations and provide no evidence about real customers or actual language-model performance.

## Evidence to Retain

Keep the decision question in a short Markdown note. Link to the data dictionary, exact input files, executable script, saved table, and figure. Record the command and Python version. State the observation unit and distinguish the two separate synthetic constructions. An agent should be able to locate these objects from the note without ingesting the entire resource library.

Ask the assistant to explain the 4.25 rating and trace the selected concept identifiers to the saved comparison table. The student checks one calculation independently, reviews the changed files, and explains the consequence of a proposed change in persona weighting. A correct-looking paragraph is evaluated against the underlying quantities and sample definition.

## Separate the Failure Types

1. **Calculation:** In a working copy, replace equal-persona aggregation with equal-row aggregation. Identify which reported mean changes and why.
2. **Execution:** Run from the example folder and the course root. The existing scripts locate inputs relative to their own files. An optional notebook comparison should record its kernel directory and environment before loading data.
3. **Display:** Include a dollar amount, an equation, a five-category table, and a figure. Check that currency remains prose, labels remain readable, and the plot agrees with the saved table.
4. **Navigation:** Compare an ordinary relative Markdown link with a `[[wikilink]]` in a small disposable note. In Suzuri's documented export, the wikilink becomes text. Check whether the reader can still reach the intended explanation.
5. **Completeness:** If testing note embeds, remove a referenced section in the disposable copy. Check both the export message and the resulting document. The source allows a missing embed to be reported while export otherwise succeeds.
6. **Publication:** Inspect the proposed Git changes, including any bibliography attachments. Decide which artifacts belong in the public course and verify the final files before publishing.

The last four steps are proposed checks, not completed application tests. Preserve the released inputs and results by working in a separate example copy. Error messages, figures, and exported pages answer different verification questions and should retain separate conclusions.

## Implications for the Future Wiki

Each worked example can offer the decision question, assumptions, source data, editable code, expected numerical checks, interpretation, and downloadable files on one page. Related concepts should remain reachable through ordinary links in both Markdown and HTML. A link graph can help navigate related lessons, but a connection between notes does not establish a statistical or causal relationship.

Before selecting a wiki implementation, test one representative module in a fresh browser and from a clean checkout. Check links, equations, accessible labels, figure scales, downloadable code, and reproduction of the reference output. A working local preview and a successful document export should be recorded separately from a working published course site. The current [wiki plan](../../08_Wiki/README.md) remains pending.
