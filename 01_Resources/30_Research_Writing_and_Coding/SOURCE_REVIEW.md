# Suzuri Source Review

Reviewed November 22, 2026. Source inspection supports a proposed writing and coding exercise and future wiki design decisions. It does not establish application performance, reliability on student computers, or a learning effect.

## Versions and Reading Scope

The landing page displayed version 0.6.4 dated November 15 when reviewed. The GitHub releases API identified [version 0.7.0](https://github.com/harrywang/suzuri/releases/tag/suzuri-v0.7.0), published November 20, as the latest release. The reviewed implementation is pinned to its commit, `88f58aae544bdc60d5068e7b5d40a05ca7f1a564`. The observed main-branch head was `10b663c756aa928d41827104463454900ad0742d`, dated November 22. Release and development versions are recorded separately.

The website described Tectonic as its LaTeX compiler. The current settings and LaTeX-engine documentation, confirmed by the release source, instead specify `latexmk` by default with managed TeX Live as a fallback and other configurable engines. This discrepancy gives students a concrete reason to record the version and inspect the relevant implementation before relying on a landing-page description.

The README, release record, settings, export, linking, Zotero, and LaTeX-engine documentation were read. Selected functions and tests in five Rust source files were inspected for export conversion, PDF copying, automatic synchronization, and compiler selection. The inherited Zed AI-privacy document was read for its distinction among request paths. The companion testbed README was read at commit `b8c8e974e894f28bd778e47bda91ff4e738c92d3`; its fixture files were not individually executed or comprehensively reviewed. Several live documentation routes, including privacy and sync, could not be retrieved through the web reader. Claims about sync below rely on the pinned code and release record.

## Findings Supported by the Source

| Finding | Pinned Source or Documentation | Interpretation for the Course |
| --- | --- | --- |
| Notes, code, PDFs, and typesetting share a file-based project | [README](local_sources/suzuri/README.md) | The environment may support reading, calculation, and interpretation together; efficiency and learning effects remain unmeasured |
| Wikilinks become display text during export | [preprocess.rs](local_sources/suzuri/crates/markdown_export/src/preprocess.rs), `convert_wikilinks`, lines 972–987; test at 1341–1349 | Internal editor navigation can disappear in an otherwise successful exported document |
| HTML conversion requests standalone output and embedded resources | [pandoc.rs](local_sources/suzuri/crates/markdown_export/src/pandoc.rs), `convert`, lines 273–340 | A portable HTML document is supported; a site-wide navigation or hosting system was not established |
| Missing note or section embeds can be reported while export continues | [preprocess.rs](local_sources/suzuri/crates/markdown_export/src/preprocess.rs), `expand_embed`, lines 421–470; tests at 1578–1589 | Build success should be accompanied by a completeness check |
| Zotero insertion can copy a PDF beside the bibliography | [insert_citation.rs](local_sources/suzuri/crates/citations/src/insert_citation.rs), `insert`, lines 407–468 | Review imported files against the course's publication rights and source manifest |
| Automatic sync requires opt-in and then stages all changes in a sync cycle | [suzuri_sync.rs](local_sources/suzuri/crates/suzuri_sync/src/suzuri_sync.rs), lines 640–775 and 1151–1168 | Automatic backup should remain distinct from review and publication of course material |
| Sync checks repository trust, conflicts, and Git ignore status | [suzuri_sync.rs](local_sources/suzuri/crates/suzuri_sync/src/suzuri_sync.rs), lines 642–698 | These checks address Git operations; they do not evaluate analytical validity or publication rights |
| LaTeX compilation has explicit engine selection | [typeset_preview.rs](local_sources/suzuri/crates/typeset_preview/src/typeset_preview.rs), `latex_invocation` and `compile_command`, lines 483–568 | Preserve the course's build settings and verify template compatibility before adopting an editor preview |

The source tests cited in the table were read, not run. Their assertions describe intended behavior and support interpretation of the corresponding implementation. Runtime verification would require a separate installation and execution exercise.

## Local Files and External Requests

The repository contains an inherited [Zed AI-privacy document](local_sources/suzuri/docs/src/ai/privacy-and-security.md) distinguishing hosted models, provider API keys, external agents, gateways, local models, and terminal tools. This supports a useful conceptual distinction between where files reside and where computation occurs. Its Zed-specific contractual statements are not treated as verified terms for every Suzuri configuration. Version 0.7.0's release note also reports disabling Zed telemetry by default; that setting alone does not describe an agent's model requests.

An optional classroom demonstration should identify the files made available to the agent, the configured model path, and the output sent to GitHub. A small synthetic case makes those objects inspectable. No provider account or private data is needed for the proposed exercise.

## Publication and Source Rights

The Suzuri README describes the codebase as primarily GPL-3.0-or-later with Apache-2.0 components where marked. Both original license files accompany the nine-file reference subset. The Rust excerpts are preserved as source references, with no modification or incorporation into executable course code. The full editor, bundled assets, dependency tree, build tooling, and binaries are omitted.

The testbed repository had no license declaration in its repository metadata, and the inspected README did not supply a general redistribution license. It is linked as a design reference; its fixtures and third-party examples are not copied into this course. Proposed examples use the course's own synthetic inputs and code.

The new sync feature reads Git ignore status and calls `stage_all`. The [Git documentation](https://git-scm.com/docs/gitignore) explains that ignore rules do not affect files already tracked by Git. More generally, neither an ignore rule nor a copied citation determines whether a document may be published. The course's existing file exclusions and release review remain relevant.

## Primary Links

- [Suzuri project](https://github.com/harrywang/suzuri/tree/88f58aae544bdc60d5068e7b5d40a05ca7f1a564)
- [Release 0.7.0](https://github.com/harrywang/suzuri/releases/tag/suzuri-v0.7.0)
- [Export behavior](https://docs.suzuri.ai/writing/export)
- [Wikilinks and backlinks](https://docs.suzuri.ai/writing/wikilinks)
- [Zotero integration](https://docs.suzuri.ai/writing/zotero)
- [Settings](https://docs.suzuri.ai/reference/settings)
- [LaTeX engine selection](https://docs.suzuri.ai/typesetting/latex-engines)
- [Pinned companion testbed](https://github.com/harrywang/suzuri-testbed/tree/b8c8e974e894f28bd778e47bda91ff4e738c92d3)

## Verification Record

Every saved file's byte length and Git blob SHA-1 were checked against GitHub's release-directory metadata. SHA-256 hashes in [catalog.json](catalog.json) support subsequent local checks. Documentation and source findings remain separate from proposed course activities. The review introduced no application settings, new dependencies, credentials, external model requests, or changes to released lectures and course requirements.
