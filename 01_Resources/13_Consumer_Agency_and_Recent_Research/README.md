# Consumer Agency and Recent Marketing Research

How should a firm evaluate an interface that raises adoption or retention while weakening customers' understanding or ability to leave? This collection connects recent marketing research to consumer agency, clustering, and cancellation policy.

## Collection and Review

The November 5, 2026 census contains **886 unique DOI records** from Journal of Marketing, Journal of Marketing Research, and Marketing Science. The date rule includes records with an online or issue-publication date from January 1, 2023 through November 5, 2026. The same paper appears once even when its online and issue years differ. Future 2026 publications are outside this snapshot.

Crossref queries using each journal's verified ISSNs establish the metadata census. Publisher tables of contents have not been exhaustively reconciled against it. Screening removes 62 front-matter, correction, retraction, or related notice records, leaving 824 eligible records, including substantive editorials and commentaries. The screen is not a claim that every eligible record is an empirical research article.

| Journal | DOI Records | Eligible | Retrieved Full Texts or Related Versions |
| --- | --- | --- | --- |
| Journal of Marketing | 276 | 273 | 48 |
| Journal of Marketing Research | 266 | 262 | 25 |
| Marketing Science | 344 | 289 | 30 |
| Total | 886 | 824 | 103 |

There are **721 eligible records without a verified retrieved full text**. Publisher restrictions and inaccessible repository links limit coverage. The UIUC Library route available in the browser still returned a publisher access screen on November 5; a separate desktop session could not be checked while the Mac was locked. No institutional entitlement is inferred from a browser login or an OpenAlex open-access flag.

The collection provides **144 original paper summaries**, covering every retrieved paper plus 41 selected abstract-only records. Most summaries are based on abstracts; selected teaching cases additionally use full-text discussion or conclusion sections. Each card states its actual evidence basis. The review does not claim a complete assessment of the methods and results in all 103 downloads.

## Navigation

- [Article Index](CATALOG.md): every DOI, publication dates, access status, and available review card.
- [Machine-Readable Catalog](catalog.json) and [CSV](catalog.csv): metadata, original implications, coding, and evidence basis.
- [Access Ledger](access_ledger.csv): source, retrieved version, file checksum, and local path; the [JSON ledger](access_ledger.json) also preserves attempted URLs and failures.
- [Missing Full Texts](access_gaps.csv): the unresolved acquisition queue.
- [Retrieval Manifest](retrieval_manifest.json): query URLs, inclusion rule, retrieval dates, and source counts.
- [Clustering Example](../../03_Data_and_Code/Consumer_Agency_Literature/README.md): code, data dictionary, sensitivity checks, and results.
- [Cancellation Policy](Policy/README.md): verified jurisdictions, status, effective dates, and official legal texts.

The original short-ID and module resource catalogs overlap with other course materials. This journal census is a separate DOI-based collection; its records should not be added to those catalog counts as a unique-resource total.

## Rights, Versions, and Identity

Research PDFs are organized by journal in Dropbox-only `local_papers/` subfolders. Their redistribution rights have not been individually cleared, so the public repository contains metadata, original summaries, and links. Open availability alone is insufficient permission to republish a PDF. Official legal texts have separate provenance in `Policy/sources.json`.

Retrieved versions include published articles, accepted manuscripts, working papers, and one dissertation containing an earlier related chapter. The ledger identifies those differences. Numerical results in an early version must be checked against the version being cited. Downloads were checked for PDF format, extractable text, and title consistency. Two unrelated documents found through repository links were rejected; one was subsequently replaced with the correct article. The remaining rejected document is counted as an access gap.

## Interpretation of Agency

The coding distinguishes reported choice concerns, possible dual use, protective mechanisms, and concerns not established on the reviewed evidence. A possible misuse is an inference about a mechanism, not an allegation about the authors or proof that a firm deployed it. The [codebook](../../03_Data_and_Code/Consumer_Agency_Literature/CODEBOOK.md) states definitions and unresolved reliability limitations.

Clustering describes the mechanism composition of the selected review sample. Access, publication selection, abstract coverage, and coding choices affect its result. The frequency of a mechanism in papers does not measure the frequency or severity of agency erosion in markets.

## University Affiliations

The [affiliation analysis](../../03_Data_and_Code/Consumer_Agency_Literature/AFFILIATIONS.md) covers 745 of the 824 eligible papers, with 424 higher-education institutions after a verified source correction. It groups institutions through shared-paper links and overlays reviewed mechanisms using fractional paper weights. [Complete membership and sensitivity outputs](../../03_Data_and_Code/Consumer_Agency_Literature/results/affiliations/README.md) distinguish exploratory network structure from claims about institutional intent.
