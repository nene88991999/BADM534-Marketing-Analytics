# Data Dictionary

## Sources and Retrieval

`sources.json` has one row per selected document. `id` is the document key; `issuer` defines the source family; `date` is the publication or call date; `kind` distinguishes calls, announcements, and accounting disclosures. `url` is the requested retrieval address. `primary_url`, when present, identifies the original issuer-hosted transcript. `format`, `start_marker`, `end_marker`, and `identity_markers` govern extraction. `primary_locator`, `retrieval_note`, and `rights` record verification and permitted handling.

`data/retrieval_snapshot.json` contains the frozen executed collection. `source_id` joins the source roster. `status=ok` means the response passed identity and minimum-length checks; `unavailable` carries a reason and has no word or match counts. Successful rows record original and final URLs, HTTP status, UTC retrieval time, SHA-256 of raw bytes, byte length, extraction units (`pages`; one unit for HTML), candidate-window count, word count, and six regex-occurrence counts. The regexes are in `collect.py`. Counts refer to the extracted text, including analyst and management speech. They are not substantive claim labels or unique speakers. Adjacent candidate windows can overlap.

## Qualitative Annotations

`data/claims.json` contains ten purposeful claim records. `claim_id` is unique; `source_id` joins the source register. `speaker_context` and `locator` recover the relevant source passage. `stage` records epistemic or procedural status. `direction` separates increases, offsets, and mechanisms. `mechanism` names the proposed channel; `population` states the affected entity or class. `paraphrase` is original course wording, not a quotation. `counterevidence` preserves contextual qualifications and competing claims. `interpretation_limit` states the inference left unresolved. `annotation_status` identifies assistant source checking and pending independent human review. `historical_causal_effect_identified` is false for every selected claim.

`data/reviewer_template.csv` is a blank review form with claim ID, coder ID, stage, direction, source locator, reason, and unresolved question. Blank entries are uncompleted judgments, not agreement. Keep independent copies before discussing disagreements.

`data/excerpts.json` contains three short verbatim passages reproduced in the lecture notes. `source_id` joins the source register, `text` preserves the source wording, and `locator` identifies the relevant passage. Speaker, date, and contextual interpretation accompany each box in M5 §5.27.2. These excerpts are evidence of attributed statements; their wording does not establish whether a forecast subsequently occurred.

## Outputs

- `results/coverage.csv`: one row per selected source, with observed status, words, and recovery matches. Missing counts remain blank.
- `results/evidence_matrix.csv`: one row per coded claim, retaining all annotation fields, issuer family, date, and source URL. Related documents share a source family.
- `results/bill_illustrations.csv`: monthly usage in kWh, monthly dollar change, percentage where the original bill is supplied, annualized dollar change, and interpretation status. Annualization assumes twelve months of unchanged usage and rates. It does not measure realized yearly expenditure.
- `results/summary.json`: counts of selected documents, calls, source families, claims, stages, and directions. Denominators describe this teaching set only.

The one missing machine-retrieved accounting source is separately source-checked through the web reader. It can support a documented qualitative annotation, but it is excluded from computed text counts.
