# Data Dictionary

All records are original synthetic teaching inputs or derived results. No customer records, actual model outputs, measured device latencies, or real monetary expenses are included. Numbers rounded in prose retain full precision in CSV.

## Decoding Inputs and Round Records

`data/request_roster.csv` has 24 rows. `request_id` identifies a request; `split` is development or evaluation; `content_tokens` is 24, 48, or 96; `eos_tokens` is one; `seed` initializes Python `random.Random`. A target sequence contains content placeholders followed by `<EOS>`. The same position draws are reused across all policies for that request. Different splits use distinct IDs and seeds.

`results/rounds.csv` has one row per target pass, per request and configuration. `regime` names ordinary, aligned, mismatched, or realigned; `k` is the maximum proposed draft length; `round` and `start_position` are zero-based. `proposed` counts all charged proposals; `accepted` counts the consecutive matching prefix; `target_token` is one when a correction or bonus is emitted. `emitted` includes accepted tokens and any target token. It includes EOS. `draft_ms` and `verify_ms` are imposed milliseconds. `ended_with_eos` identifies the final pass. Prefill is charged once per request and is absent from these round rows.

## Decoding Aggregates

`results/decoding_summary.csv` has 74 rows: two splits, each with ordinary generation plus twelve draft lengths for each of three compatibility regimes. Every row summarizes twelve requests and 684 emitted tokens. `compatibility` is the imposed probability that a draft proposal agrees with the fixed target at a position. The ordinary row has no proposals.

`passes`, `proposed`, `accepted`, and `emitted_including_eos` are totals. `block_efficiency` is total emitted tokens divided by passes. `generation_ms` sums drafting and verification; `total_ms` adds 40 milliseconds per request. `generation_tokens_per_second` excludes prefill; `total_tokens_per_second` includes it. These are ratios of totals, not means of request-specific ratios. `mean_request_ms` divides total time by attempted requests. Queueing, network delay, retrieval, and task evaluation are outside both timing measures.

`results/frozen_choices.csv` has one row per compatibility regime. `selected_k` maximizes development total throughput, with ties going to smaller k. The remaining fields report throughput on development and evaluation requests and evaluation mean request time at that fixed choice. Evaluation results never select the length. The public evaluation curves remain descriptive after further tuning on them.

## Service Inputs

`data/service_requests.csv` has twelve requests. `days_since_purchase` is elapsed whole days; `unused` is a Boolean. `eligible` follows the imposed rule `unused and days_since_purchase <= 30`, with day 30 included. Six requests qualify.

`data/teacher_forced_predictions.csv` has 240 rows: two targets, twelve requests, and ten reference word positions. `position` is zero-based. `reference_token` is a whitespace-delimited word or punctuation token. `prediction_given_reference_prefix` is a constructed top prediction conditional on all preceding reference words. `correct` records equality. Those predictions are not fed back to construct the free-response table.

`data/free_responses.csv` has 24 rows: the same twelve requests under each hypothetical target. `status` is completed or timeout. A timeout has an empty answer, false answer correctness, and false action completion. `answer_correct` checks the eligibility decision; `action_completed` records completion of the promised service step; `correctly_resolved` requires both. The generated answer is constructed independently of the teacher-forced prediction sequence. `response_wait_seconds` includes timed-out attempts. Compute cost is $0.002 times response wait; triage cost is $0.20 for each unresolved request. Triage does not establish a subsequent human resolution.

## Service Aggregates

`results/service_summary.csv` and `.json` contain identical two-row results. Reference-token accuracy uses all 120 tokens per target. `attempted`, `completed`, and `failed` retain the entire request roster. `correct_answers` and `correctly_resolved` count different outcomes. Answer accuracy among completed responses conditions on completion; answer accuracy and resolution per attempt divide by twelve. `mean_wait_seconds` includes all attempts. Total cost adds compute and triage for all attempts. `cost_per_correct_resolution` divides that cost by correct automatic resolutions and is null when zero. Accuracy among completed responses is null when none complete.
