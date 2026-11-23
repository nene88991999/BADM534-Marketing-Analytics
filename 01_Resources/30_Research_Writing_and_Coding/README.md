# Research Writing and AI-Assisted Coding

A marketing recommendation must connect the decision, source evidence, calculation, and interpretation. Keeping those objects in readable project files lets a student inspect the complete argument and lets an assistant work with the same inputs. The central teaching question is whether the recommendation remains supported when the code, editor, or exported format changes.

[Suzuri](https://suzuri.ai/) combines Markdown writing, PDF reading, citations, typesetting, code editing, and agents in a modified Zed editor. The project is useful as an optional authoring environment and as a source of practices for reproducible course work. Its feature set supplies no estimate of how much students learn or how much analyst time they save.

## Useful Connections to the Course

| Course Location | Question | Practice to Adapt |
| --- | --- | --- |
| M1 §1.15 | Can a student explain and verify an AI-assisted analysis? | Keep the task specification, data dictionary, program, expected result, and interpretation together; review the assistant's changes against a small known example |
| M1 §1.11 | Where do project data and model requests go? | Distinguish local files, notebook kernels, configured AI providers, and Git publication |
| M2 and M7 | Does the displayed result preserve the intended comparison? | Assess numerical values, execution, chart rendering, and interpretation separately |
| M8 §8.25 | Can someone else reproduce and assess a recommendation? | Connect the source reading, calculated table, figure, and conclusion through stable relative paths |
| Future Wiki | Does a course page retain its meaning and navigation outside the editor? | Keep Markdown, code, and figures as reusable sources; test links, equations, tables, citations, and downloaded examples in the published output |

The [released optional exercise](../../07_Labs/Reproducible_Recommendations/README.md) reuses the synthetic-consumer calculations in M1 §1.15 and M8 §8.25, with discussion in Sessions 1 and 14. A new wrapper recomputes four saved tables and writes a traceable recommendation. Six checks cover arithmetic, missing values, stale tables, and execution after relocation. The [verification record](../../03_Data_and_Code/Reproducible_Recommendations/VERIFICATION.md) separates course execution and Pandoc checks from unexecuted Suzuri application tests.

## Evidence, Code, and Interpretation in One Project

Suzuri's [repository README](https://github.com/harrywang/suzuri/blob/88f58aae544bdc60d5068e7b5d40a05ca7f1a564/README.md) describes Markdown files, a PDF pane, LaTeX and Typst preview, and code-editor features. These could make it easier to compare a source passage with a calculation and the statement it supports. For students, the transferable practice is a project whose files and run commands remain understandable in another editor. The existing course Markdown, complete Python, data dictionaries, and agent guides already provide that foundation.

The [companion testbed](https://github.com/harrywang/suzuri-testbed/tree/b8c8e974e894f28bd778e47bda91ff4e738c92d3) is especially useful pedagogically. It separates Markdown rendering, notebook execution, document compilation, and PDF display. Its examples include dollar amounts that should remain prose, mathematical expressions in tables, missing links, plots wider than a pane, and notebooks reading files from nested folders. Students can adopt that method by defining expected behavior before asking an assistant to repair a failure. The companion repository's examples were inspected as documentation; they were not executed or republished here.

## Implications for the GitHub Wiki

[Suzuri's export documentation](https://docs.suzuri.ai/writing/export) describes a Pandoc conversion to PDF, Word, HTML, LaTeX, and EPUB. In the inspected release, HTML export requests a standalone page with embedded resources. Internal `[[wikilinks]]` become display text, while supported note embeds insert content. That choice serves a portable document but removes the internal navigation represented by those wikilinks. A successful export therefore supplies insufficient evidence that an interconnected course site works.

For the course, retain standard relative Markdown links, stable module identifiers, source code, data dictionaries, and figure descriptions. A future site build should turn these sources into navigable HTML and check the resulting destinations. Suzuri can edit the source files; a multi-page site still needs its own navigation, search, accessibility checks, executable-example strategy, and publication process. The source inspection did not establish a GitHub Pages deployment feature or a browser Python runtime.

## Optional Use and Publication Choices

The [Zotero documentation](https://docs.suzuri.ai/writing/zotero) and inspected citation code show that selecting a Zotero item can copy its PDF beside the bibliography. Public course release therefore requires checking the newly added files and their recorded redistribution rights. The presence of a citation or a local copy does not itself authorize republishing the PDF.

Version 0.7.0 adds opt-in GitHub synchronization. Its code stages, commits, and pushes project changes after activation. For this public course repository, retain review of the files being published and keep automatic synchronization off during an initial trial. File synchronization and acceptance of an analytical result are separate decisions. A local editor also does not establish where a configured agent processes its requests; the actual provider and tool configuration determine that path.

The existing Beamer template, TikZ figures, and course build commands remain suitable. Current Suzuri documentation exposes a configurable LaTeX engine, including an external command; compatibility with this course's builds has not been tested in Suzuri.

## Sources and Review Status

The [source review](SOURCE_REVIEW.md) distinguishes documented features, inspected implementation, and proposed teaching uses. The [catalog](catalog.json), namespace `research-writing-and-coding`, preserves nine unchanged files from release `suzuri-v0.7.0`, commit `88f58aae544bdc60d5068e7b5d40a05ca7f1a564`, with both license files and verified Git blob identities. Only selected source paths were read. No installation, Rust build, upstream test execution, notebook execution in Suzuri, or model call was performed. The later course integration adds an optional practice exercise and lecture material. It establishes no assessment requirement, required editor, or wiki deployment.
