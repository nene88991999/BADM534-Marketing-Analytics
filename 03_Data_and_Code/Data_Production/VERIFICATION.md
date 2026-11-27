# Verification

Verified November 26, 2026 with Python 3.12.14. The original example uses the standard library. It makes no network requests and executes no downloaded source code.

## Numerical Checks

`data_availability.py` generated two 400-row synthetic ledgers, six releases, six comparison rows, and one bounds row. `verify_example.py` passed independent checks of the full-population effect totals (+4,000 and -4,000), exact identity of the restricted public releases, the broader-release mean (10/3), positive-inclusion weighting, the [-15, 15] support interval, and row-order invariance. Duplicate household identifiers and zero-inclusion weighting fail explicitly. Assigning zero to unreleased effects is shown to produce the incorrect mean -5 in world H.

The weighting calculation is the Horvitz–Thompson total divided by the known population size. Its exact recovery in the constructed examples follows from constant effects within strata. The synthetic prior bill equals the current no-project bill by construction; this is not an empirical identification result.

The course checker verified 129 matching, syntactically valid Python source blocks, including the full program in M2 §2.31. The existing small lecture-example checks also passed. Their generated CSV values agree with the committed inputs.

## Sources and Teaching Scope

The [catalog](../../01_Resources/45_Data_Truth_and_Norms/catalog.json) records 26 sources and the inspection scope for each. Checksums match all 14 local source copies. Unavailable full texts and abstract-only entries are identified. No original source file from this collection is included in the public Git package.

The source assessment verifies existing EIA household billing collection and public expenditure microdata. Contract correspondence documents particular confidentiality practices and exceptions. The introduced text of S. 5640 is treated as proposed federal legislation; no enactment or effective reporting duty is inferred. The course does not estimate actual utility harms, identify the target paper's donor contamination, or establish intentional suppression.

## Document Checks

The complete notes and standalone Marketing Dialectics chapter were rebuilt from Markdown and TikZ. The syllabus and Sessions 2, 10, and 14 were rebuilt from maintained sources, and the combined deck was regenerated from all 15 session PDFs. The complete notes contain 603 pages and 147 original note figures; Marketing Dialectics contains 105 pages; the combined deck contains 520 slides. Sessions 2, 10, and 14 contain 29, 30, and 101 pages, respectively. The syllabus remains two pages.

Visual review covered the changed material and neighboring page breaks, the table of contents, all three new diagram previews, the changed slides, and both syllabus pages. Slide-specific diagram layouts preserve the comparisons with larger projected labels. Complete notes, standalone notes, and the syllabus contain no replacement characters in extracted text. The final note builds have no overfull boxes or unresolved references.
