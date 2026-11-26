# Verification Record

## Executed Collection and Analysis

The November 26, 2026 release contains six selected public documents, five retrieved HTML documents, three call excerpts, and ten source-checked paraphrases. The SEC accounting disclosure was checked through a web reader and remains unavailable in the machine-extracted corpus. Its text counts are missing. The collection used fixed URLs, sequential requests, document-identity checks, and SHA-256 receipts. Original transcripts and local passage windows are excluded from Git.

The Evergy and CenterPoint passages were checked against their issuer-hosted transcripts and retrieved public renditions. The PSEG passage was checked against its public rendition; the original recording was not independently transcribed. All three quoted passages match the extracted source text verbatim. The New Jersey announcement independently supports the announced-price bill illustration, while retaining the difference between supply costs and construction-cost recovery.

Executed with Python 3.12.14. Commands from this directory:

```sh
python3 collect.py --download
python3 collect.py
python3 analyze.py
python3 test_examples.py
```

The offline analysis reproduced all four result exports without byte changes. Eight tests passed: exclusion of hidden markup, document-identity rejection, article boundaries, preservation of negation for contextual review, missing counts, grouping related documents, retention of offsets, and exact bill arithmetic. The PDF extraction branch was inspected but was not used in the executed collection. Fresh network retrieval depends on source availability and can differ from the frozen snapshot.

From the repository root, `python3 scripts/check_lecture_code.py` verified 115 matching Python blocks and their syntax, including the two complete programs in M5 §5.27. This check establishes agreement between printed and runnable code; the example tests separately evaluate the specified behaviors.

## Interpretation and Human Review

The annotations were prepared by the assistant and checked against the selected sources. No independent human coding, inter-coder agreement estimate, saturation assessment, or population-prevalence estimate has been completed. The blank review form supports a subsequent independent reading. Counts describe purposeful selections and preserve shared issuer families.

The bill calculations use the source documents' stated monthly usage and prices. Annualization assumes twelve identical months and unchanged rates. They do not measure realized household expenditure or isolate a data-center-specific causal effect. The example does not replicate the reviewed electricity paper's statistical analysis. The paper itself permits cost recovery and positive residential spillovers; the qualitative comparison assesses broader reassurance and the institutional steps required to support it.

## Rendered Materials

The lecture notes, standalone Marketing Dialectics chapter, Sessions 7 and 14, and the combined slide deck were rebuilt. The new sections, boxed excerpts, editable TikZ diagram, and changed slide pages were rendered for visual inspection. [The manifest](manifest.json) records the public input, code, and result hashes for this release.
