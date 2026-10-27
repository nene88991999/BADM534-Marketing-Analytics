# Generative-AI Demand: Course Adaptation Review

Reviewed October 26, 2026. Executed course examples are in [GenAI_Demand](../../../03_Data_and_Code/GenAI_Demand/README.md). The supplied collector, simulator, notebook, HTML, and input tables remain reference originals. A saved notebook output is separate from the verification status of the course adaptations.

## Resources and Incorporation

| Additional-Catalog ID | Assessment | Course Use |
| --- | --- | --- |
| `egan-russel-shi-yao-2026-competition-generative-ai` | NBER abstract and bibliographic record checked. Full paper unavailable during this review. | M8 §8.13: consumer subscription demand and competitive pressure. Detailed model structure, data-vendor identity, and identifying variation are not inferred from the abstract. |
| `genai-demand-lab` | Inspected both scripts, all notebook cells, saved outputs, data schemas, and simulation parameters. | M2 §2.17, M4 §4.14, M8 §8.13: three new offline course programs, three TikZ figures, eight counterexample tests. |
| `fradkin-2025-demand-for-llms-openrouter` | arXiv abstract checked. | M8 §8.13: distinguish application-level model use from consumer subscription demand. |
| `wikimedia-pageviews-api` | Official pageview definition checked; supplied daily table audited. | M2 §2.17: title identity, selected-title totals, repeated observations, and unknown dates. |
| `openrouter-models-api` | Supplied parser and capture schema inspected; endpoint not re-collected. | Units and available-offer measurement. Listing date is retained as a marketplace timestamp; it is not automatically a public release date. |
| `apple-rss-top-charts` | Supplied parser, app mapping, and rank snapshot inspected; endpoint not re-collected. | Ordinal ranks, storefront scope, and top-list censoring. No conversion of ranks to market shares. |
| `ramp-ai-index` | Supplied entry and links reviewed; current chart values not reverified. | Business sample versus consumer population. No claim that this is the only public transaction-based measure. |
| `epoch-ai-notable-models` | Link and supplied collection function reviewed; no local model-table capture in this bundle. | Optional event-date research. Check each relevant record and announcement before constructing causal event windows. |
| `wayback-cdx-api` | Supplied retrieval functions inspected; archive queries not run. | Optional historical-price exercise with plan, billing-period, region, and capture-date validation. A regex alone does not establish the correct price. |
| `cloudflare-radar-internet-services-ranking` | Supplied collector inspected; token-required endpoint not called. | Optional traffic ranking. Verify token scope and API schema before use; ranks do not establish market shares. |

## Corrections Needed for Interpretation

1. **Fixed cohorts.** The source notebook compares separate provider cohorts with a pooled all-payer cohort. The course adaptation computes provider and category outcomes for exactly the same starting customers. It also separates endpoint retention from holding the original provider in every intervening month.
2. **New subscriptions.** The simulator's `new` flag means absent from that provider in the preceding month. In the last simulated month, 401 such events include first entry, returns, additions, and 32 complete provider switches. The original event plot does not by itself isolate switching.
3. **Price recovery.** The notebook's static log-odds regressions are not inversions of the supplied heterogeneous, dynamic, multiple-holding generator. Its flow coefficient being close to the imposed utility coefficient in one realization does not demonstrate identification. The course adaptation labels both slopes descriptive and adds a separate exact binary-logit recovery benchmark.
4. **Calibration.** The generator recalibrates common utility monthly to target adoption. Its stated endpoint target is approximately 2.9%, and the saved panel has 2.902%. Provider retention is not constrained to the abstract's reported range: the five January 2025 provider cohorts range from 1.2% to 37.7% twelve-month endpoint retention in the supplied simulation. Premium-plan prices do not enter the provider-selection utility; tier assignment happens afterward.
5. **Substitution models.** A retention gap does not identify a nested-logit inclusive-value coefficient. Single-choice nested logit also changes the choice structure when consumers can hold several providers. A structural extension requires a suitable bundle or multiple-choice model, an information set, and justified variation.
6. **Public signals.** App rank, view events, business spending, posted prices, and subscriptions have different populations and denominators. The Wikipedia result sums two explicitly selected titles. It does not deduplicate people or reconstruct every historical title. Unknown API observations remain unknown until collection status supports a zero.
7. **Release timing and events.** An OpenRouter listing timestamp is marketplace-specific. Public release timing, rolling access, price changes, publicity, overlapping releases, and the relevant event risk set require separate verification. The supplied synthetic release dates and quality increments remain imposed inputs.
8. **Execution and rights.** The original notebook reports fallback captures after failed live calls. This review executes only the three new offline course analyses and their tests. Captures retain their source terms; keyless access does not establish unrestricted reuse. No paid API call, new scheduled collection, paper download, or credential handling occurred.

The [manifest](../../../03_Data_and_Code/GenAI_Demand/manifest.json) records source hashes, and [verification](../../../03_Data_and_Code/GenAI_Demand/results/verification.json) records the executed environment and numerical checks. Full Python appears in the lecture notes. All new figures use the Illinois palette and have table/text companions.
