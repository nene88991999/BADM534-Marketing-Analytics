# Collection Provenance and Maintenance

[Resource Library](../README.md)

This collection was assembled on October 23, 2026 after reviewing the six-page sample syllabus in `00_Sample_Materials`. Work was confined to `01_Resources`; the sample syllabus and `02_Syllabus` were not changed. No GitHub repository, website deployment, student account, paid purchase, or service registration was created.

## Selection and Search

Searches covered the syllabus's eight module families, Python marketing analytics, official package documentation, open teaching texts, author repositories, customer and campaign datasets, AI-assisted programming studies, current assistant documentation, and static HTML notebook execution. Sources were selected for direct course relevance, author or institutional provenance, usable written material, teaching examples, and identifiable access terms. Current documentation and 2026 research were included alongside foundational work.

The structured catalog records annotations and direct source URLs. `link_checks.json` records all source checks, response status, redirects, and observed page titles. HTTP success establishes retrieval, not a complete technical review. Two non-core leads remain access-limited: the DecisionPro textbook page returned 403, and GroupLens timed out. Search-indexed official pages supplied the leads; verify direct access before assigning either.

## File Inventory

- `../RESOURCE_CATALOG.json`: stable resource IDs, topic, priority, source, teaching use, cautions, rights, local files, and link status.
- `download_plan.json`: selected public assets and intended local destinations.
- `download_manifest.json`: actual download status, source URL, bytes, SHA-256 checksum, and local path.
- `extracted_files.json`: original archive, output path, bytes, and checksum for extracted dataset files.
- `link_checks.json`: source availability checks as of collection.
- `validation.json`: integrity and local-link verification results.
- `collect_resources.py`: checks URLs and downloads selected assets without executing them.
- `build_guides.py`: creates topic README files, the master guide, Finder bookmarks, and extracted dataset files from the catalog.

GitHub download URLs include a commit SHA for the marketing research, ISLP, causal handbook, and PyMC-Marketing repositories. Downloaded notebooks are unmodified source references and may retain output from their authors. The 24 notebooks have not been run locally, and included dependency lists have not been installed. Some notebooks require assets, package datasets, or a particular execution directory beyond the selected files.

## Refreshing the Library

Run from the course folder with a Python 3 interpreter:

```sh
python3 01_Resources/_maintenance/collect_resources.py check
python3 01_Resources/_maintenance/collect_resources.py download
python3 01_Resources/_maintenance/build_guides.py
```

The scripts use standard-library modules. Network access is needed for the first two commands. Existing downloads are preserved rather than silently replaced. A deliberate update should record new source versions and compare content before replacing files. Review annotation accuracy, current access, and permissions as well as link status. The date labels in scripts and documentation describe this collection and should be updated for a later collection run.

The build script uses optional temporary primary-page metadata from `/tmp/badm534-research/pages` when available; the curated catalog and included manifests remain the durable record. Planning notes, teaching notes, dataset guidance, and design notes are maintained separately from the generated indexes.

## Reuse

Repository licenses are saved next to their code. Dataset and document terms are recorded per resource. A public link, a successful download, or a license on code does not automatically grant redistribution rights to a book, third-party dataset, image, or article. The full instructor library should not be published wholesale. Select or link each item for the future wiki according to its recorded terms.

## Shared-Folder Changes

An independent `00_Index` catalog and additional module folders appeared during this run. They were not created, edited, merged, or validated as part of this collection. The validation scope is the catalog and downloaded-file manifest maintained here, plus the guides linked from the main README.
