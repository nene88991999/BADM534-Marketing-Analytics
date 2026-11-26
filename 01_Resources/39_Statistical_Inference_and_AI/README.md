# Statistical Inference and AI-Assisted Analysis

A marketing decision can rest on executable code and still use an unsuitable statistical comparison. Fisher-R1 and P-Bench motivate separate assessment of execution, statistical method, numerical reporting, and interpretation.

The [source review](SOURCE_REVIEW.md) is the Markdown companion to the archived [paper](readings/Miao_Mu_Chen_Zou_WorkingPaper2026.pdf). It explains the benchmark, findings, figures, repository, and scope of the course adaptation. The [catalog](catalog.json) uses the namespace `statistical-inference`; the [manifest](manifest.json) pins inspected files and the GitHub commit. See [rights](RIGHTS.md) for the distinction between the paper, benchmark, model weights, and code.

## Course Applications

| Material | Application |
| --- | --- |
| M1 §1.18; Session 1 | Assess execution, method, reported numbers, and managerial interpretation separately. |
| M3 §3.18; Session 4 | Reconstruct mHealth pairs and compare uncertainty while holding the point estimate fixed. |
| M6 §6.30; Session 9 | Evaluate rejection rates under a known zero effect with store assignment and correlated customer outcomes. |
| M9 §9.24; Session 14 | Distinguish a joint advertising test from claims about mechanisms, welfare, and customer agency. |

The [original Python examples](../../03_Data_and_Code/Statistical_Inference/README.md) have complete source in the lecture notes and an [optional ungraded lab](../../07_Labs/Statistical_Inference/README.md). Their simulation measures false-positive rates. It does not reproduce Fisher-R1's model-performance evaluation.

## Public Sources

- Jiacheng Miao, Jin Mu, Guanhua Chen, and James Zou (2026), [Fisher-R1: Training LLM Agents for Reliable Hypothesis Testing](https://arxiv.org/abs/2608.07437).
- [FisherR1 repository](https://github.com/jmu27/FisherR1/tree/968dd38bea50102a313d7d36843aba564eabc33f), inspected at the pinned commit; code linked only.
- [P-Bench](https://huggingface.co/datasets/May2222/P-Bench), including the archived [consumer-credit advertising question](benchmark_sample/question.txt), its [reference answer](benchmark_sample/answer_key.json), and [dataset documentation](benchmark_sample/UPSTREAM_README.md).

The consumer-credit question is available for discussion. Its reference p-value has not been independently reproduced, and its dataset is not included in this collection. It does not establish a customer-welfare result.
