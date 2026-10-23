# AI Coding and Assessment Notes

[AI Resources](../README.md) | [Resource Library](../../README.md)

Students should be able to use an assistant to implement a marketing analysis and explain why its inputs, transformations, method, and conclusions fit the decision. That objective requires repeated practice evaluating generated work as well as requesting it.

## A Workflow to Adapt Across Modules

1. **Specify the decision.** State the population, unit of observation, decision time, available information, output, and relevant business costs.
2. **Inspect the data.** Read the dictionary and a small sample. Confirm types, missing values, identifiers, and table relationships.
3. **Plan a small step.** Ask for a proposed implementation and identify assumptions before accepting code.
4. **Implement and inspect.** Review the resulting change and ask for explanations of unfamiliar operations.
5. **Check the result.** Compare with a known example, verify invariants, inspect diagnostics, and run an appropriate evaluation.
6. **Interpret and record.** Explain the result in marketing terms, save a reproducible version, and document consequential AI contributions and corrections.

This is an instructor synthesis for the course. Provider references [AI01](https://learn.chatgpt.com/guides/best-practices), [AI03](https://code.claude.com/docs/en/best-practices), and [AI04](https://docs.github.com/en/copilot/get-started/best-practices) offer alternative implementations of context, iteration, and review. Select one supported primary tool and a practical fallback after checking student access. Exact prices, quotas, and educational eligibility have not been established by this collection.

## A Reusable Task Specification

> Decision: What marketing action will this analysis inform? Data: Which files and columns are available, and what does one row represent? Timing: Which fields are known when the decision is made? Output: What table, estimate, or figure is required, with which units? Constraints: Which packages and data may be used? Checks: Which small examples, invariants, or evaluation results would establish that this step is working? Before coding, identify missing information and consequential assumptions. After coding, show the change and the checks performed.

A specification should stay short enough that students can explain every part. Do not include private customer information or real credentials in demonstrations. Use the supplied public datasets or clearly labeled synthetic examples.

## Evidence to Read Before Setting Assessments

| Research | Evidence and Setting | Course Implication to Consider |
| --- | --- | --- |
| [Kazemitabaar et al., 2023](https://arxiv.org/abs/2302.07427) | Controlled study involving 69 novices aged 10-17 using an earlier Codex tool. | Assess code authoring and subsequent understanding separately; the study population differs from graduate business students. |
| [Prather et al., 2024](https://arxiv.org/abs/2405.17739) | Qualitative observations from 21 novice programming sessions. | Include checks that reveal misunderstanding even when an apparently complete solution has been produced. |
| [Kazemitabaar et al., 2023](https://arxiv.org/abs/2309.14049) | Analysis of how novices prompt, combine, and modify generated code. | Practice stepwise requests and manual modification rather than assessing only task completion. |
| [Peng et al., 2023](https://arxiv.org/abs/2302.06590) | Controlled experiment with a bounded JavaScript implementation task. | Productivity on a specific task is a separate outcome from learning and long-term maintenance. |
| [Becker et al., 2025](https://arxiv.org/abs/2507.09089) | Randomized tasks for 16 experienced developers in familiar repositories using early-2025 tools. | Effects depend on task and setting; avoid a universal claim about time saved. |
| [Perry et al., 2023 version](https://arxiv.org/abs/2211.03622) | A user study of security-focused programming tasks with an earlier assistant. | Review generated file, API, and credential handling, using dummy examples in class. |
| [Shen and Tamkin, 2026](https://arxiv.org/abs/2601.20245) | Randomized experiments on learning a new programming library with AI assistance. | Check debugging and understanding after assisted completion; do not infer semester-long effects directly. |

The assessment suggestions are pedagogical judgments informed by these studies. The studies use different populations, tasks, tools, and outcomes and do not jointly establish one causal effect for this course.

## Possible Assessment Components

Require a runnable analysis, a concise explanation of its major choices, and a record of substantive checks. Use short individual tasks that ask students to interpret a result, repair a planted error, change an assumption, or explain a transformation. If some checks must be completed without AI, state that explicitly in the revised syllabus and assignment instructions. Avoid making prompt length or the amount of generated code a proxy for learning.

Keep a short record of consequential prompts, important corrections, and checks rather than demanding large unstructured transcripts. The original syllabus already requests attribution and documentation, which provides continuity for this approach.
