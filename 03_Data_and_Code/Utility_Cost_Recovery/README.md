# Utility Disclosures and Household Costs

A household advocate must assess whether an assurance about electricity affordability addresses infrastructure cost recovery. The example retrieves public disclosures, identifies passages for contextual reading, and compares claims about investment, customer charges, and revenue offsets. The resulting evidence establishes institutional mechanisms and stated plans. A data-center-specific causal effect requires a separate empirical comparison.

## Inputs and Reproduction

The purposeful selection contains six documents from five issuer families, including three earnings calls. Ten course-authored paraphrases retain speakers, locators, populations, evidence stages, counterevidence, and interpretation limits. These are assistant-prepared annotations checked against sources, with independent human coding pending. Counts describe the selection. They do not estimate prevalence among utilities.

From this directory, use Python 3.10 or later:

```sh
python3 analyze.py
python3 test_examples.py
```

Both commands run offline using committed metadata. `analyze.py` creates the [comparison matrix and coverage outputs](results/README.md), including two transparent bill calculations. The [data dictionary](DATA_DICTIONARY.md) defines every field. The [codebook](CODEBOOK.md) explains interpretation; the [methodological readings](../../01_Resources/42_Qualitative_Evidence/README.md) support the qualitative practices.

To retrieve the fixed public-source list:

```sh
python3 collect.py --download
python3 collect.py
```

The first command makes sequential requests and caches accessible documents with hashes and retrieval receipts. The second reprocesses the cache without network access. HTML extraction uses explicit article boundaries and excludes scripts and styles. PDF extraction, when used, requires `pypdf`; it removes repeated page furniture and retains page locators. Current verified runs use HTML renditions. The retrieval output and passage windows remain in ignored `.cache/`. Download failures remain unavailable; they never become zero-match documents. Inspect extracted boundaries and complete speaker turns before annotating. No API key, paid service, or external LLM upload is needed.

Direct automated retrieval of the Evergy and CenterPoint issuer-hosted PDFs and the SEC accounting disclosure returned HTTP 403. Separately accessible public ROIC transcript renditions were retrieved for both calls. Their selected passages were cross-checked against the issuer PDFs using the web reader. The PSEG passage was checked against its public transcript rendition and the regulator's related announcement; the original call recording was not independently transcribed. The accounting passage was checked with the web reader but remains absent from the machine-extracted corpus. The frozen snapshot records five successful document downloads and one unavailable document. A fresh collection writes a separate snapshot; it never silently replaces the committed release.

## Evidence and Course Coverage

M5 §5.27 supplies complete collection and analysis code, the qualitative procedure, and the source comparison. M6 §6.36 separates mechanism evidence from identification. M9 §9.33 uses the evidence in a stakeholder argument. Sessions 7 and 14 include the corresponding discussion. The [lab](../../07_Labs/Qualitative_Evidence/README.md) is optional ungraded practice.

The reviewed electricity paper itself allows cost recovery and reports positive residential spillovers. The case challenges categorical reassurance, residual causal attribution, and extrapolation beyond the study's 2020–2025 window. It does not claim that these disclosures overturn the historical coefficient. Most selected disclosures were made in 2026, after that window.

## Provenance and Rights

The instructor's existing analysis supplied research leads. The public adaptation uses independently checked third-party disclosures and original code and paraphrases; private notes and manuscripts are excluded. [sources.json](sources.json) identifies the primary documents and retrieval renditions. Full transcripts and lengthy extracts remain local because no redistribution permission was established. Public outputs contain metadata, counts, short original paraphrases, citations, and three brief [verbatim excerpts](data/excerpts.json) reproduced in boxes in M5. The [manifest](manifest.json) records hashes and the [verification record](VERIFICATION.md) distinguishes executed work from proposed qualitative checks.
