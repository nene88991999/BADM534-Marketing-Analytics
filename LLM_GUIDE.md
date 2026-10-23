# Student and LLM Guide

## Get the Right Context

Start with [the course map](COURSE_MAP.md). For a particular task, provide your assistant the root [agent guide](AGENTS.md), [course manifest](course.json), the current syllabus, your assignment brief, and the relevant notes or data dictionary. Supply the actual data only when permitted and needed.

For a broad overview, use [llms-full.txt](llms-full.txt). It contains navigation and resource summaries. Read the linked source for details, equations, examples, and qualifications. The full file is generated from repository sources; do not edit it directly.

A private repository URL works only with tools authorized to read that repository. Downloading selected Markdown files gives you a portable alternative. Choose an approved service before uploading nonpublic materials. No paid assistant or particular vendor has been selected for this course.

## Useful Prompts

### Understand a Module

> Read AGENTS.md, course.json, and COURSE_MAP.md. Help me learn M3. Identify the relevant files, explain the managerial question and key concepts, and give one small numerical example. Cite file paths and source sections. Tell me which materials you could not access.

### Plan an Analysis

> Read this assignment and data dictionary. First restate the decision, outcome, unit of observation, available information, and constraints. Propose a short analysis plan and identify choices I need to make before you write code. Follow the assignment's AI rules and distinguish requirements from suggestions.

### Debug Code

> Explain why this code produces this error. Propose the smallest correction and a simple check. State what you inspected and what you actually ran. Help me understand the changed lines.

### Review a Result

> Audit my analysis for incorrect joins, missing-data decisions, units, leakage, and unsupported causal claims. Compare each concern with the assignment and data dictionary. Prioritize issues that could change the managerial conclusion, and give a check I can run.

### Prepare for Class

> Use only the materials I provide to make a study outline for this module. Cite the supporting file and heading for each topic. Separate course requirements from optional background. Ask me five questions and wait for my answers before giving explanations.

## Check the Assistant's Work

A program can run successfully and still answer the wrong question. Inspect a few rows, check totals and units, compare with a simple baseline, and explain the results in your own words. Keep a record of consequential AI assistance when your assessment requires it. Ask for clarification when current course documents leave a requirement unresolved.
