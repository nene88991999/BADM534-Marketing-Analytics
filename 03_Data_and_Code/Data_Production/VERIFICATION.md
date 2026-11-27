# Verification

Verified November 27, 2026. Both programs use the Python standard library, make no network requests, and execute no downloaded source code.

## Selective Release Example

`data_availability.py` generated two 400-row synthetic ledgers, six releases, six comparison rows, and one bounds row. The independent checks executed on November 26 with Python 3.12.14 verified the full-population effect totals (+4,000 and -4,000), exact identity of the restricted public releases, the broader-release mean (10/3), positive-inclusion weighting, the [-15, 15] support interval, and row-order invariance. Duplicate household identifiers and zero-inclusion weighting fail explicitly. Assigning zero to unreleased effects produces the incorrect mean -5 in world H.

The weighting calculation is the Horvitz–Thompson total divided by the known population size. Its exact recovery in these examples follows from constant effects within strata. The synthetic prior bill equals the current no-project bill by construction. These conditions do not establish empirical identification.

## Dataset Versions and Pending Cancellation

Executed `data_artifacts.py` with Python 3.14.8. The six-account synthetic history gives five retained accounts, four requests, one completion, and three pending requests. Independent checks of the released CSV files verified the account identities, V2 projected onto account/status equaling V1, the pending share of requests (3/4), and the pending share of retained accounts (3/5). Reversing row order changes the file hash and preserves keyed records. The printed fractions, saved summary, and manifest checksums agree.

The comparison of three research agreements holds this event history fixed. The agreements are hypothetical. The checks concern the deterministic example, without estimating empirical cancellation practices or attributing contractual terms to a named study.

## Sources and Teaching Scope

The [catalog](../../01_Resources/45_Data_Truth_and_Norms/catalog.json) records 30 sources and the inspection scope for each. The 14 previously checked local source copies are unchanged. Unavailable full texts and abstract-only entries are identified. Original source files from this collection remain in Dropbox and are excluded from the public Git package.

The electricity assessment identifies existing EIA household billing collection and public expenditure microdata. Contract correspondence documents particular confidentiality practices and exceptions. Proposed legislation remains identified by its status. The research-agreement discussion distinguishes professional publication policies, actual contractual provisions, and hypothetical comparisons. It does not infer a publication veto from an NDA label.

## Code and Document Checks

All 131 Python source blocks in the notes match their standalone files and parse successfully. The existing lecture-example calculations also executed successfully; their CSV values remain unchanged. The artifact calculation received separate checks of records, denominators, identity, and hashes.

The complete notes and standalone Marketing Dialectics chapter were rebuilt from Markdown and TikZ. Sessions 2 and 14 were rebuilt from their maintained source, and the combined deck was regenerated from all 15 session PDFs. The complete notes contain 634 pages and 153 original note figures. Marketing Dialectics contains 119 pages. The combined deck contains 541 pages; Sessions 2 and 14 contain 32 and 108 pages, respectively.

Visual review covered the added sections and adjacent page breaks in both note PDFs, the changed slides, and the three new diagram previews. All changed pages were rendered, with 43 distinct pages inspected across the four PDFs. The affected note and slide builds have no overfull boxes or unresolved references. Source labels, numerical populations, and agreement conditions are preserved in the Markdown companions.
