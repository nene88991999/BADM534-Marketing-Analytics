# Source Review: Multi-Token Prediction and Domain Adaptation

Reviewed November 22, 2026. Paper: [arXiv 2611.25813v1](https://arxiv.org/abs/2611.25813v1), submitted November 19; its PDF cover is dated November 20. Repository: [google-research/gemma4-mtp-drafter-domain-adaptation](https://github.com/google-research/gemma4-mtp-drafter-domain-adaptation), inspected at commit `3ca321f2a356bd29d99c5d5fcea4018960f8b691` dated September 8, 2026. The paper and repository dates identify different release objects.

## What the Paper Establishes

The architecture uses a shared four-layer drafting transformer, target activations, direct access to the target's stored attention keys and values, and clustered vocabulary projection for E2B and E4B. The projection first scores clusters and then selected tokens. The target performs the verification. A proposal that is cheap to construct remains useful only when its acceptance and verification costs yield a favorable total comparison.

| Comparison | Population and Configuration | Reported Result and Scope |
| --- | --- | --- |
| Server throughput, Tables 1–2 | 880 SPEED-Bench prompts; batch size 1; bfloat16; vLLM 0.26; one H100 for E2B, E4B, and 12B; two H100s for 26B and 31B | Selected G-MTP configurations yield speedups from 1.34 to 3.14. This range concerns the listed models and selected draft lengths. |
| Draft length, Table 5 and Figure 3 | The server workload across alternative lookahead lengths | For 26B MoE, length 4 gives block efficiency 3.27 and 334.0 tokens/s; length 12 gives 4.39 and 209.5 tokens/s. The higher internal efficiency coexists with lower throughput. |
| Clustered projection, Table 3 | 456 single-turn prompts; Pixel 11 Edge TPU; four-bit E2B and E4B; greedy decoding; length 3; at most 600 output tokens | Drafting time falls to 0.81 and 0.79 of the full-projection comparison; the reported additional decoding speedup is 1.01 for each model. Values are medians over prompts, with speedup defined as a ratio of median throughput. |
| Domain adaptation, Table 4 | SciQA and GSM8K; 500 test examples per domain; E4B; LoRA updates; train length 3, evaluation length 7 | Target-only tuning increases teacher-forced token accuracy but lowers block efficiency. Joint tuning or a second stage that trains the drafter against a frozen adapted target restores efficiency. |
| Mobile GPU, Table 7 | 76 short prompts; four task types; median input length 29; Galaxy S26 Ultra; LiteRT-LM; greedy decoding; length 3; at most 512 output tokens; full vocabulary projection | Ratios of median throughput are 1.69 for E2B and 2.18 for E4B. The prompt population differs from the server and mobile NPU comparisons. |

Appendix A.1 selects draft length from the evaluated grid. A course replication should preserve a separate workload for final confirmation after selecting a configuration. Published speedups do not directly determine customer latency, API charges, energy use, or answer correctness. The paper explicitly leaves broader memory and battery evaluation to future work.

Table 4 calls the two-stage result approximately 96% of the untuned block-efficiency reference. That ratio fits GSM8K (3.58/3.73), while the displayed SciQA values give 2.80/2.51, which exceeds the untuned reference. Use the individual rows instead of repeating that caption as a common percentage across both domains.

## Metrics and Their Denominators

Appendix A.3.3 defines acceptance rate as total accepted draft tokens divided by total proposed tokens. Block efficiency is one plus accepted draft tokens per target step. Neither expression includes the duration of drafting or verification. Target-step counts also need the same output task and a stated stopping rule before they support a cost comparison.

In [eval_utils.py](local_sources/gemma4-mtp-drafter-domain-adaptation/eval_utils.py), `compute_ntp_accuracy` evaluates the target on the complete reference sequence. Each prediction conditions on earlier reference tokens. Its `total_accuracy` weights examples by answer-token count; `mean_per_sample_accuracy` gives each retained example equal weight. A high value does not measure complete-answer execution or independently generated reasoning. The prompt/answer boundary is inferred from tokenized template lengths, so a replication should verify prefix alignment and answer-token masks for its tokenizer.

`compute_block_efficiency` requests greedy generation and defaults to 64 new tokens. The entry point calls it without overriding that default. It does not record elapsed time. Its returned fields therefore support a token/step comparison, subject to the callback's coverage, rather than a wall-clock reproduction of the server tables.

## Repository Findings

These findings concern the pinned source. They do not establish that the corresponding condition occurred in the authors' reported runs.

1. **Failure coverage.** `compute_block_efficiency` catches three classes of generation exception, prints the sample index and error, and continues. The returned dictionary contains no attempted, completed, or failed request counts. The shared log is reset once before the loop; entries already recorded for a request can remain if it later fails. An adaptation should retain a per-request status and define the treatment of partial output before aggregating.
2. **Callback semantics.** `patched_update_assisted` logs only calls for which `scores.shape[1] > 1`, and uses that shape as the proposed-token count. `total_steps` is the length of this filtered log. The coverage of verification passes and the meaning of the score dimension must be checked against the exact installed Transformers implementation. These fields should not be relabeled as measured hardware work without that reconciliation.
3. **Runtime and artifact versions.** The README suggests upgrading dependencies without a lock file. Model-loading calls use repository names without revision hashes and enable remote model code. SciQA loading uses the moving `refs/convert/parquet` ref. A reproducible environment should record library versions, model and dataset revisions, tokenizer settings, and the generation configuration actually used.
4. **Defaults differ across entry points.** The Python entry point defaults to 100 evaluation examples, learning rate 0.00002, MTP loss weight 0.1, and distillation weight 0.9. The shell pipeline chooses SciQA, 500 evaluation examples, learning rate 0.0002, joint MTP weight 0.4, and pure distillation. The paper reports a different learning rate for GSM8K. Copying a single README command does not reproduce every experiment.
5. **Draft length needs an explicit setting.** The paper specifies evaluation lookahead seven. The saved evaluator does not set `num_assistant_tokens` or a proposal schedule, so its effective draft policy depends on the loaded model and runtime configuration. Record the resolved settings before comparing a run with Table 4.
6. **Adaptation scope differs in one material detail.** Appendix A.3.1 says the output projection remains fixed so that the original vocabulary clusters stay valid. The repository's assistant LoRA target list includes `lm_head`. Whether that name matches an enabled layer depends on the loaded model and PEFT version. Inspect the actual trainable parameter names and resulting projection before claiming an exact reproduction of the stated configuration.
7. **Sample construction.** The formatter can skip records without a usable instruction. The training path truncates sequences to 512 tokens and masks prompt labels. For a dataset lacking a training split, the training entry point creates a seeded split from its first available partition, while the separate evaluation entry point loads a dataset partition named `test`. A transfer to another dataset must reconcile these sample identities; this is not evidence of overlap in the paper's SciQA or GSM8K experiments.
8. **Tests cover model loading and adapters.** The saved test file loads models and performs a small training step. It is not a lightweight test of every metric, failure path, or full-generation quality. The tests were read and syntax-parsed, without execution.

Relevant source anchors in the pinned repository are [the generation log and NTP calculation](https://github.com/google-research/gemma4-mtp-drafter-domain-adaptation/blob/3ca321f2a356bd29d99c5d5fcea4018960f8b691/eval_utils.py), [training and evaluation orchestration](https://github.com/google-research/gemma4-mtp-drafter-domain-adaptation/blob/3ca321f2a356bd29d99c5d5fcea4018960f8b691/run_experiments.py), [pipeline settings](https://github.com/google-research/gemma4-mtp-drafter-domain-adaptation/blob/3ca321f2a356bd29d99c5d5fcea4018960f8b691/run_pipeline.sh), and [the distillation implementation](https://github.com/google-research/gemma4-mtp-drafter-domain-adaptation/blob/3ca321f2a356bd29d99c5d5fcea4018960f8b691/training_gemma4.py).

## Useful Implementation Ideas

The code separates data preparation, model loading, training, and evaluation. It supports target-only adaptation, joint adaptation, and a second stage with a frozen target. The loss combines ordinary language-model training with total-variation distillation, while optional detachment controls whether the drafting objective changes target representations. These are useful examples of specifying which component changes and which comparison remains fixed.

The package primarily supports the domain-adaptation part of the paper. The H100/vLLM and mobile throughput studies require additional runtimes and benchmark configurations. The public model documentation provides a separate [MTP inference guide](https://gemma.ai/get-started/capabilities/mtp/). The reviewed source selection is reference material; it is not a course-tested environment or a complete reproduction of all reported experiments.

## Retrieval and Verification

Nine files were retained unchanged: the README, Apache 2.0 license, six Python files, and the shell pipeline. Their bytes match the pinned Git blobs. The repository's issue/PR templates and contributor-policy documents were omitted. The catalog records SHA-256 hashes, upstream blob identifiers, paths, and retrieval date. Python syntax parsing and `bash -n` succeeded. No imported repository module, upstream test, dataset loader, model loader, training pipeline, or inference call was executed.
