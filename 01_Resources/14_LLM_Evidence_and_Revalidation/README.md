# LLM Evidence, Model Updates, and Revalidation

A marketing team deciding whether to replace an AI workflow needs evidence about the proposed configuration, the tasks it will receive, and the costs of its mistakes. A finding about an earlier model supplies a testable hypothesis. Its relevance depends on whether the current workflow retains the mechanism and conditions that generated it.

## The Shelf Life of LLM Findings

[Queen and Zou (2026)](https://zou-group.github.io/llm-claims-shelf-life/) revisit 50 selected claims across 20 models. Their September 2026 classifications contain 22 expired, 17 weakened, eight persistent, and three strengthened claims. The snapshot has 1,000 model-claim observations, of which eight are flagged as unreliable for comparison. These are selected findings and models, rather than a random sample of all AI research or deployments.

The [released tables](source_tables/README.md) and fitted results are pinned to repository commit `710517ed80e1c85cc3a5fe1cef2f7c4045e59b3d`, dated November 2, 2026. The authors' [MIT license](source_tables/LICENSE) accompanies their files. [Provenance](provenance.json) records the source URLs, Git blob identifiers, checksums, and retrieval date. Third-party benchmark inputs and model-call programs are outside this teaching copy.

The copy contains `claims.csv`, `panel_values.csv`, `post_results.json`, the original table README, and the license. The upstream README also describes `claims.json` and `run_manifest.csv`, which are omitted here.

An independent course script reconciles the counts and calculates follow-up summaries from the published estimated dates. Among the 22 expired claims, the mean is 15.75 months and the median is 14.65 months. Treating the other 28 as right-censored gives estimated expiration shares of 4.0%, 16.0%, and 38.9% at six, twelve, and twenty-four months. These calculations use the released dates as fixed inputs. They do not repeat the underlying model calls, refit the trends, or propagate uncertainty in estimated expiration dates.

## What the Result Supports

The evidence motivates recurring, task-specific evaluation. It does not supply a universal deadline after which an AI paper becomes false. Model release dates, evaluation dates, and publication dates are different variables. A benchmark observation from an older experiment may still describe a model that remains in service. A released model can also behave differently when its prompts, tools, reasoning settings, or input distribution change.

The project's relative effect normalizes an outcome against a claim-specific reference and null value. Its expiration zone permits a residual effect. A point estimate below a threshold and an uncertainty interval wholly below that threshold are different statements. The website's fitted categories also use additional rules and uncertainty; two expired categories follow a recent-model count even though their fitted curves remain above the threshold. Preserve the released classifications when reproducing the headline counts.

The date trend compares different model configurations. It does not identify a causal effect of elapsed time, one architectural change, or one provider's training procedure. Reproduction sometimes uses a substitute for a retired model, and default reasoning budgets differ across the panel. These conditions belong beside any inference about current capabilities.

## Related Research and Course Uses

| Source | Evidence and Scope | Course Application |
| --- | --- | --- |
| [Chen, Zaharia, and Zou (2024), How Is ChatGPT's Behavior Changing Over Time?](https://hdsr.mitpress.mit.edu/pub/y95zitmz/release/2) | Compares March and June 2023 service snapshots across tasks. Section 3.5 separates directly executable code from correctness after removing surrounding noncode text. | Keep parsing, execution, and analytical correctness as separate checks. A formatting change can break a pipeline even when the code inside is useful. |
| [Zheng et al. (2023), Judging LLM-as-a-Judge](https://arxiv.org/abs/2306.05685) | Evaluates agreement with human preferences and documents position, verbosity, and self-enhancement biases in the tested judges. Sections 3.3-3.4 examine answer-order checks. | Score the same saved outputs with a stable rubric; swap answer order and retain inconsistent verdicts. Agreement with preferences does not establish factual accuracy. |
| [Panickssery, Bowman, and Feng (2024), LLM Evaluators Recognize and Favor Their Own Generations](https://arxiv.org/abs/2404.13076) | Examines self-recognition and self-preference in summarization, including controlled fine-tuning comparisons. Broader task coverage remains an extension. | Concealing a model's name may leave stylistic cues. Include an independently assessed sample when evaluating generated review or earnings-call summaries. |
| [Sharma et al. (ICLR 2024; revised 2025), Towards Understanding Sycophancy in Language Models](https://arxiv.org/abs/2310.13548v4) | Tests several forms of agreement and feedback behavior and examines human preferences as a possible contributor. The specific models and prompts delimit its findings. | Hold a marketing proposal fixed while varying whether a sponsor likes it. Check evidence quality separately from approval or flattering language. |
| [White et al. (ICLR 2025), LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://arxiv.org/abs/2406.19314v2) | Uses periodically refreshed tasks and objective scoring; its maintenance discussion distinguishes benchmark versions and exposure. | Combine a fixed regression set with fresh cases. Track task composition when comparing scores across releases. Freshness reduces some exposure concerns without guaranteeing independence. |
| [Jain et al. (2024), LiveCodeBench](https://arxiv.org/abs/2403.07974v2) | Uses dated competition problems and examines generation, repair, execution, and test-output prediction. Publication windows help examine potential contamination. | Evaluate generated Python on new schemas, edge cases, and independent expected outputs. Contest performance alone does not establish the validity of a marketing estimand. |

The six related papers are available in Dropbox's `local_papers/`; [download records](reading_downloads.json) identify versions and rights. PDF originals remain outside Git. The summaries, links, licensed project tables, and original course code are public. The reading review covers the methods and sections used above, not an independent replication of each paper.

## Worked Examples and Teaching Placement

[LLM Revalidation](../../03_Data_and_Code/LLM_Revalidation/README.md) contains three executable programs, a data dictionary, independent checks, and results. M1 §1.13 specifies versioned evidence. M2 §2.21 interprets the published claim panel and censoring. M5 §5.18 separates generator changes from judge changes. M7 §7.22 examines paired regressions and failure costs. M8 §8.18 connects revalidation to deployment scale and consumer consequences. Sessions 01, 03, 07, 11, and 14 include the corresponding discussion within their existing time allocations.
