# AI Inference Efficiency and the Cost of a Useful Response

A retailer choosing a customer-service assistant must compare response quality, waiting time, operating cost, and the consequences of an incorrect answer. A model that generates more tokens per computation can still take longer to serve a request. Specializing the model for the retailer's products can also change the performance of other components that depend on it.

## Drafting and Verification

[Galgani and coauthors](https://arxiv.org/abs/2611.25813v1) study multi-token prediction for speculative decoding. A small drafting component proposes several tokens. The larger target model evaluates those proposals together and supplies the accepted continuation. Their G-MTP architecture reuses the target's internal representations and attention cache, uses one shared drafting block, and reduces vocabulary-projection work for the smaller models through clustering.

Verification here concerns agreement with the target model's decoding rule. It does not establish factual accuracy, executable code, or an appropriate customer response. The [foundational speculative-decoding result](https://proceedings.mlr.press/v202/leviathan23a.html) preserves the target distribution under its specified sampling procedure. Preserving a target's behavior leaves the substantive quality of that behavior as a separate evaluation question. The reviewed repository uses greedy generation.

## More Accepted Tokens Can Accompany Slower Generation

The server experiments use 880 SPEED-Bench prompts, bfloat16 precision, vLLM 0.26, and batch size one. The 26B mixture-of-experts model runs on two H100 GPUs. In Table 5, expanding its draft from four to twelve tokens increases block efficiency from 3.27 to 4.39, while generation throughput falls from 334.0 to 209.5 tokens per second. Relative to the same 248.9-token-per-second baseline, the reported speedup falls from 1.34 to 0.84. The longer draft therefore produces a slowdown under this configuration.

Block efficiency counts output progress per recorded verification step. Drafting and verification both take time, and verification cost depends on the architecture, hardware, and workload. Figure 3 places increasing block efficiency beside throughput curves that eventually fall. A deployment comparison should measure the time and cost of completing the actual task, including retrieval, checks, and review when those steps are required.

## Specialization Changes Component Compatibility

Table 4 evaluates domain adaptation on 500 test examples per dataset, with a training lookahead of three and an evaluation lookahead of seven. On SciQA, tuning only the target raises teacher-forced next-token accuracy from 68.40% to 99.23%, while block efficiency falls from 2.51 to 1.60. Tuning the drafter as well restores efficiency: the joint regime reports 2.96, and the two-stage regime reports 2.80. The latter freezes the adapted target while updating the drafter.

The result supplies an example of a change that improves one component while disrupting compatibility elsewhere. For an AI-assisted marketing workflow, a model update should trigger evaluation of the complete configuration, including dependent models and interfaces. The paper measures token prediction and decoding efficiency on SciQA and GSM8K. Customer-service accuracy and business outcomes require their own evaluation.

## A Large Computational Saving Can Produce a Small Service Gain

The smaller drafters cluster a vocabulary of 262,144 tokens into 2,048 groups and evaluate token logits within 32 selected groups of 128 tokens. Section 3.3 reports about 43 times fewer multiply-accumulate operations in this projection. That quantity concerns one operation within a larger process.

Table 3 evaluates 456 prompts on a Pixel 11 Edge TPU with quantized E2B and E4B models, greedy decoding, and a draft length of three. Adding clustered projection reduces drafting time to 81% and 79% of the full-projection comparison, respectively. Median acceptance falls slightly, and the reported additional decoding speedup is only 1.01 for each model. These results connect clustering to computational design while showing why an intermediate saving needs an end-to-end comparison. Battery consumption and broad device-level memory benefits remain future-work questions in the paper.

## Accuracy Needs an Explicit Unit

The repository's next-token calculation supplies the reference answer as context and checks each answer token against the target's top prediction. It reports both token-weighted accuracy and the mean of per-example accuracies. Neither quantity is the share of independently generated answers that solve the task. For a generated database query, evaluation should separately establish whether the query executes and returns the intended result. For customer service, it should assess whether the response resolves the stated problem without inventing a policy or restricting a customer's options.

The [source inspection](SOURCE_REVIEW.md) also records an incomplete failure roster, reliance on generation-library callback semantics, unpinned dependencies, and differences between the paper's configurations and the repository defaults. These are reasons to specify a replication carefully. No observed failure rate or unpublished benchmark outcome is inferred from the source inspection.

## Course Placement

| Existing Material | Useful Extension |
| --- | --- |
| [M7 §7.27](../../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md) | Compare block efficiency, elapsed time, completed tasks, and cost under a stated workload |
| [M7 §§7.22 and 7.26](../../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md) | Preserve paired requests, failed runs, and distinct task-quality and efficiency outcomes |
| [M1 §§1.5 and 1.13](../../06_Lecture_Notes/modules/M01_Marketing_Analytics_and_Python.md) | Evaluate the complete configuration after changing a model or dependency; distinguish verification of tokens from verification of work |
| [M4 §§4.19–4.20](../../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md) | Use vocabulary clustering as an application of reducing search and projection cost |
| [M8 §§8.5–8.6](../../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md) | Compare the total cost of producing a usable response and the customer's resulting service |

The [case design](CASE_DESIGN.md) proposes a short M7 comparison and a later lightweight Python exercise. This resource review adds no meeting, assignment, or graded requirement. The existing lecture notes and session decks are unchanged by this review.

## Sources and Reuse

The [catalog](catalog.json), namespace `inference-efficiency`, records version 1 of the paper, the repository commit, source hashes, and rights. The [unchanged paper](local_sources/Galgani_Ji_Homburger_Jawahar_Ramanovich_Korotkov_Martins_Evci_Yvinec_Consul_Kumar_Schuster_WorkingPaper2026.pdf) is retained under the CC BY 4.0 license listed by arXiv. Its original copyright footer is preserved. Nine unchanged repository files are saved under `local_sources/gemma4-mtp-drafter-domain-adaptation/`, including the complete Apache 2.0 license. Model weights, datasets, and runtime packages were not downloaded.

The paper's main sections and experimental appendices were read; Tables 1–5 and Figure 3 were visually checked. All six saved Python files were syntax-parsed, and the shell script received a syntax check. No upstream program, test, training run, or model inference was executed. This companion describes the central architecture and course-relevant comparisons; it omits the full derivations, remaining table rows, bibliography, and architecture figures. Consult the original paper for those details.
