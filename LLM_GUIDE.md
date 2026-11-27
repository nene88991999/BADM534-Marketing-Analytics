# Student and LLM Guide

## Get the Right Context

Start with [the course map](COURSE_MAP.md). For a particular task, provide your assistant the root [agent guide](AGENTS.md), [course manifest](course.json), the current syllabus, your assignment brief, and the relevant notes or data dictionary. Supply the actual data only when permitted and needed.

For a broad overview, use [llms-full.txt](llms-full.txt). It contains navigation and resource summaries. Read the linked source for details, equations, examples, and qualifications. The full file is generated from repository sources; do not edit it directly.

A private repository URL works only with tools authorized to read that repository. Downloading selected Markdown files gives you a portable alternative. Choose an approved service before uploading nonpublic materials. No paid assistant or particular vendor has been selected for this course.

## Useful Prompts

When writing an explanation or revising course prose, follow [WRITING_STYLE.md](WRITING_STYLE.md): begin with the decision, develop the reasoning, define the comparison, and state the implication with its consequential conditions.

### Understand a Module

> Read AGENTS.md, course.json, and COURSE_MAP.md. Help me learn M3. Identify the relevant files, explain the managerial question and key concepts, and give one small numerical example. Cite file paths and source sections. Tell me which materials you could not access.

### Plan an Analysis

> Read this assignment and data dictionary. First restate the decision, outcome, unit of observation, available information, and constraints. Propose a short analysis plan and identify choices I need to make before you write code. Follow the assignment's AI rules and distinguish requirements from suggestions.

### Debug Code

> Explain why this code produces this error. Propose the smallest correction and a simple check. State what you inspected and what you actually ran. Help me understand the changed lines.

### Review a Result

> Assess my analysis for incorrect joins, missing-data decisions, units, leakage, and unsupported causal claims. Compare each concern with the assignment and data dictionary. Prioritize issues that could change the managerial conclusion, and give a check I can run.

### Compare AI Workflows

> Read the AI_Workflows README and the relevant M6–M8 note sections. Identify what changes across conditions, which outcomes guided development, and what evidence remains independent. Reproduce the relevant synthetic calculation, then explain which additional observations would be needed for a claim about actual model performance or business value.

### Prepare for Class

> Use only the materials I provide to make a study outline for this module. Cite the supporting file and heading for each topic. Separate course requirements from optional background. Ask me five questions and wait for my answers before giving explanations.

## Check the Assistant's Work

A program can run successfully and still answer the wrong question. Inspect a few rows, check totals and units, compare with a simple baseline, and explain the results in your own words. Keep a record of consequential AI assistance when your assessment requires it. Ask for clarification when current course documents leave a requirement unresolved.

## Definitions and Representation Quality

For questions about cancellation records, begin with [the dictionary and executed example](03_Data_and_Code/Ontology_and_Evidence/README.md), then M1 §1.16 and M2 §2.25. Keep raw rows, events, requests, subscriptions, and unknown states distinct. A missing confirmation creates a review condition within the available records.

For feature-quality questions, begin with [the representation example](03_Data_and_Code/Representation_Evaluation/README.md), then M7 §§7.39–7.40. Preserve coordinate scales and denominators, and distinguish reconstruction, task usefulness, matching stability, and causal meaning. No learned model or empirical customer outcome was produced by these synthetic calculations. Optional labs do not establish assignment requirements.

## Context and Evidence for Coding Tasks

Supply the task definition, relevant data dictionary, input versions, and required output before expanding the context. Record durable progress with links to actual files and checks. Ask the assistant to separate a proposed operation, an executed operation, and its verified result. [The workflow exercise](03_Data_and_Code/Agent_Workflows/README.md) distinguishes output correctness, permitted actions, and checker validity. During a measured comparison, keep final evaluation answers outside the model workspace and preserve every assigned attempt, including failures.

## Examine an Analytical Argument

Use M1 §1.20 and M9 §9.40 to define the claim, expose its premises, construct a counterexample that preserves them, assess the missing premise, and revise the conclusion. Distinguish a hypothetical possibility from evidence that it occurs. Ask for the strongest supported reply to the criticism and a meaningful condition for revision. [The argument record](07_Labs/Philosophical_Arguments/ARGUMENT_RECORD.md) and [exact examples](03_Data_and_Code/Analytical_Arguments/README.md) supply concrete checks. Apply the relevant assessment's AI-use rules.

When discussing M9 §§9.41–9.43, distinguish unmeasured empirical objects, conditional identification limits, the negative concept of noumenon (Kant, 1781/1787), and normative reasons. Unknown unknowns are unrecognized issues; an acknowledged limit needs a scope and argument. Apply the ontological spectrum to a source's particular inference, preserving its welfare findings and safeguards. The spectrum supplies no numerical author ranking. Philosophical criticism of reduction does not excuse unsupported factual accusations. Read the linked primary-source guide for passage-level scope.

## Alternative Explanations and Independent Reasoning

Use the [electricity lesson companion](08_Wiki/pilot/LESSON.md) when explaining prices, bills, and household-cost claims. Preserve the same definitions, units, assumptions, and conclusion when changing representations. Ask for a prediction and justification before supplying the calculation, and invite a supported objection. The [learning-design examples](03_Data_and_Code/Learning_Design/README.md) distinguish rounded published summaries from original synthetic values. Do not describe a correct calculation or a usable page as evidence of a learning benefit. The [HTML agent guide](08_Wiki/AGENTS.md) records implementation and verification requirements.

## Conflicts of Interest and Engagement

Use M9 §§9.45–9.49 and the [worked example](03_Data_and_Code/Conflicts_of_Interest/README.md). Identify the duty that an interest threatens before calling a situation a professional conflict. Preserve the synthetic data labels and distinguish behavioral reward learning from dopamine measurements and clinical diagnoses. A score weight is not a Scanlonian criterion. Require factual premises, a defended normative principle, objections to feasible alternatives, and reasons for revision. Treat the optional lab as ungraded practice.
