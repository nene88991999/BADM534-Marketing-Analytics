# Agent Workflow Evaluation

An AI-generated analysis can fail because of its calculation, supplied information, available tools, execution environment, or checker. This collection connects those possibilities to a controlled comparison of coding workflows and to the cost of obtaining a valid analysis.

## Reading and Original Applications

Li and coauthors' [Agent Harness Engineering: A Survey](LiXiaoZhangLiuEtAl_WorkingPaper2026.pdf) organizes execution, tools, context, orchestration, observability, evaluation, and governance. Read §8 for task definition, environment readiness, execution records, separate judgments of outputs and actions, and evaluation of the checker itself. Sections 5 and 11 connect persistent context and interacting components to workflow design. Section 9 discusses authority and enforcement.

- [Source review](SOURCE_REVIEW.md): evidence, scope, companion repository, and rights.
- [Original case design](CASE_DESIGN.md): managerial question, information-by-feedback experiment, and interpretation.
- [Course example](../../03_Data_and_Code/Agent_Workflows/README.md): actual mHealth logging calculations, independent tests, and hypothetical cost comparison.
- [Optional ungraded lab](../../07_Labs/Agent_Workflows/README.md): guided checks and an optional measured model comparison.
- [Catalog](catalog.json) and [manifest](manifest.json): versioned source information.

The paper's figures include a seven-layer taxonomy and a five-stage evaluation cycle. The course adaptation uses original editable TikZ diagrams for the factorial design and the difference between matching an aggregate and assigning values to the correct customers. This Markdown guide summarizes selected arguments; it is not a complete transcription of the 71-page survey.
