# Variables, Units, and Provenance

## Synthetic Ridge Results

`results/mixture_comparison.csv` has 261 rows: three penalty regimes, three similarity values, and 29 count comparisons. `regime` is reference (`a=50,c=1500`), equal_feature_scales (`a=c=1500`), or weaker_penalty (`a=5,c=150`). `design` is add_clean or fixed_total. `n_a` and `n_b` count constructed expected observations. `q` is task-feature similarity, using a Source B task feature of `sqrt(q)`. The penalty coefficients `a` and `c` have example units under the sum-loss objective.

`task_contribution` and `tag_contribution` are fitted changes in the response-style score in arbitrary units. `source_a_prediction` is their sum. The evaluation vector contains the tag without the task, so its fitted change equals `tag_contribution`. These columns are not probabilities. The noise-free expected scores are fixed at one for Source A and zero for Source B. All inputs and outcomes are synthetic; the penalties follow the illustrative constants in the source paper.

## Synthetic Service Records

`data/service_requests.csv` contains one row per request and version. `request_id` is unique within a version and shared across versions. `context` is product_support, refund, or cancellation. `version` is original or combined. `response_received` records whether a response exists; `correct_resolution` records whether the requested service was completed correctly. Both indicators are imposed binary values. A correct resolution requires a received response.

The original version has correct counts 855, 76, and 19 across the three contexts. The combined version has 882, 60, and 8. The last ten refund requests and last five cancellation requests lack a combined-version response. Successes occupy the first stated number of requests in each context, which determines the paired gains and losses. No actual customer records, text, training data, or model outputs appear in this file.

`results/service_contexts.csv` contains two versions by three contexts plus an overall row. `attempted`, `received`, `missing`, and `correct` are counts. `rate_per_attempt` divides correct resolutions by attempts; `rate_per_response` divides by received responses. A zero denominator produces an empty CSV value corresponding to Python `None`. `results/paired_changes.json` counts matched request IDs, recoveries from incorrect to correct, and regressions from correct to incorrect. Changes concern the fixed synthetic roster.

## Published Results

`results/published_checkpoints.csv` contains nine selected Qwen training runs from Clarke and coauthors, arXiv 2611.10110v1. Conditions are 5,000 constructed examples with no clean examples, 5,000 with 100,000 clean examples, and 9,000 with 21,000 clean examples. `raw_log_rows` counts file lines; `distinct_epochs` counts ten evaluated epochs after retaining the last record for repeated epochs. `final_rate` selects epoch 10; `peak_rate` selects the maximum across those epochs. Rates are fractions of 50 German-classified responses under the trigger prompt per checkpoint, with ten questions and five sampled responses per question.

`results/published_conditions.csv` has 51 rows: 17 constructed shares by three prompt conditions, each averaging three runs. `inoculation` is the trained trigger; the source key `trigger` means the approximate prompt absent from training; `assistant` is the ordinary prompt. `constructed_share` is the source's rounded fraction in 970 training examples. `mean_rate` is judge-classified misalignment per response. Interior cells have 560 responses per run and condition; endpoint cells have 840. The selected checkpoint maximizes the inoculation-prompt rate and has partial reuse of selection and reporting responses. These results are reported experimental aggregates, not prospective customer outcomes.

The original files, licenses, and hashes remain in `01_Resources/28_Training_Data_Mixtures`. The source commit is `a9fab54c4bc226321877aadf81a36799c7d325c5`. Derived CSVs change the presentation and retain the source's units and selection rules. No published response was regenerated or independently judged.
