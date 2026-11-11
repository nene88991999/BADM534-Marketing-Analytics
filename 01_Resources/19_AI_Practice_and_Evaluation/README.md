# AI Practice and Evaluation

A marketing analyst must decide which evidence to provide, which claims the evidence supports, and whether an automated reviewer applies a defensible rule. The Stanford CS193T course, Thinking with AI, supplies useful teaching activities for these decisions. The [source record](catalog.json) identifies the public pages reviewed on November 11, 2026. The course adaptations use original fictional cases and programs; Stanford pages, slides, and assignment PDFs are linked rather than republished.

## Selected Activities and Course Applications

| Source | Marketing Analytics Application |
| --- | --- |
| [Managing Sources and Context](https://web.stanford.edu/class/archive/cs/cs193t/cs193t.1272/assignments/3-managing-sources/) | M5 §5.19: compare the same earnings-call questions with and without a misleading secondary memo |
| [Evals: Grading the Graders](https://web.stanford.edu/class/archive/cs/cs193t/cs193t.1272/assignments/7-evals/) | M5 §5.20 and M7 §7.26: compare graders against explicit reference judgments, retain unscored cases, and evaluate asymmetric errors |
| [Models and Prompting](https://web.stanford.edu/class/archive/cs/cs193t/cs193t.1272/assignments/2-models-prompting/) | M1 §1.14: specify success before reviewing anonymous outputs; compare model configurations on the same task |
| [Coding Agents](https://web.stanford.edu/class/archive/cs/cs193t/cs193t.1272/assignments/6-coding-agents/) | Define an executable result, inspect a failure or unchecked component, and verify a calculation independently |
| [AI Foundations](https://web.stanford.edu/class/archive/cs/cs193t/cs193t.1272/assignments/1-ai-foundations/) | Explain and reproduce a small calculation without the assistant after completing AI-assisted work |
| [Browser Agents](https://web.stanford.edu/class/archive/cs/cs193t/cs193t.1272/assignments/5b-browser-agents/) | Compare a claimed action with the saved file or observable result, using authorized public inputs |
| [Deep Research](https://web.stanford.edu/class/archive/cs/cs193t/cs193t.1272/assignments/4a-deep-research/) | Trace an important factual claim to its original evidence and separate factual disagreements from differences in values |
| [Tutorial Structure](https://web.stanford.edu/class/archive/cs/cs193t/cs193t.1272/course/about_tutorial/) | Combine a short demonstration with build time and explanation; adapt to the existing 170-minute meetings |

## Evidence and Adaptation

The Stanford exercises motivate the activity design. They provide no empirical estimate that a particular prompting strategy, grader, or tool improves marketing outcomes. The [original worked examples](../../03_Data_and_Code/AI_Evidence_and_Evaluation/README.md) use constructed inputs to make denominators and failure types visible. The [practice lab](../../07_Labs/AI_Evidence_and_Evaluation/README.md) explains how to collect new model responses while holding the task fixed.

Source quality depends on relevance and evidentiary support. Contradictory evidence deserves examination; disagreement alone is not grounds for exclusion. A confidence declaration, a citation, or agreement among models supplies no independent guarantee of correctness. Reference labels should have reasons and a process for resolving disagreement.

## Interactive Wiki Design

A future wiki can show a small evidence collection, record the student's initial judgment, then reveal an additional memo and ask which conclusions remain supported. A companion table can let students vary the costs of false approval, false rejection, and human review while preserving the underlying cases. Show counts and denominators beside each score. A public page can hide labels visually until requested, but this does not make those labels secret or create a held-out assessment set.

The current release contains Markdown instructions, complete Python, data, and diagrams. No wiki application or live model experiment is represented as completed.
