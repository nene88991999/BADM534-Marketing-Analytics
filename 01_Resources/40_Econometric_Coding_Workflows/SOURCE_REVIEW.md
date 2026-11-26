# AI Agents and Prompt Engineering in Econometric Coding

Sebastian Galiani, Federico A. López, and Raul A. Sosa. NBER Working Paper 35588, issued August 2026 and revised November 2026. Reviewed November 26, 2026.

## Sources and Design

The [NBER record](https://www.nber.org/papers/w35588) and [45-page author manuscript](https://lopezfe.de/chatbots-agents-econometrics/paper.pdf) describe six models, 40 tasks, 32 simulated datasets, three languages, two prompt conditions, three agency conditions, and ten repetitions per cell: 43,200 runs. Earlier versions used smaller samples and report different headline numbers.

The researcher specifies the method, sample, target quantities, inference convention, and output. A chatbot supplies one script. Self-repair returns execution failures or missing values and allows up to three revisions. A constrained agent can execute and revise, choose when to stop, and is instructed to perform an independent numerical check. The agent contrast therefore changes several workflow components together. It does not isolate tool access or test independent choice of an identification strategy.

The scoring rules compare requested numerical values with verified reference computations. Nine tasks additionally score standard errors. Known wrong methods can fail even within a numerical tolerance. Other incorrect methods can produce sufficiently close values, so numerical agreement remains an incomplete assessment of implementation. See §§II–III and Appendix A4.

## Findings and Denominators

Each agency condition contains 14,400 assigned runs. Success is 83.69% for the chatbot, 93.29% for self-repair, and 97.37% for the agent. The corresponding loud-failure counts are 1,694, 167, and 41; silent-failure counts are 654, 799, and 338. Loud means failed execution or incomplete requested output. Silent means complete output with at least one incorrect scored value. These classifications depend on the task's requested output.

The agent's silent failures are 2.35% of assigned runs and 89.18% of its 379 failures. Self-repair can expose a silent error by fixing a script that previously failed to run. Its higher silent-failure count does not establish that repair made already-correct programs worse. The supplied intervals resample 40 tasks, preserving runs within each task. The paper also checks inference using the 32 shared input datasets.

The one-example prompt raises success by 4.42 percentage points under the chatbot and 0.79 under the agent. These changes remove 23.86% and 26.15% of their respective zero-shot failures. The interaction's interpretation depends on the outcome scale and proximity to perfect success.

## Figures and Tables

Figure 1 defines the task-by-language-by-prompt-by-agency design. Figure 2 compares success by prompt and language, with task-cluster bootstrap intervals. Figure 3 places failures per assigned run beside silent failures as a share of all failures; the denominators differ. Figure 4 compares task success and token expenditure, using separate cost axes for model groups. Table 1 reports cell contrasts, and Table B1 separates failure types by model, language, and workflow.

The three archived CSVs cover Figure 3, Figure 2's prompt/platform summaries, and model-level success and cost summaries. They do not contain individual run records. Recomputing their counts checks aggregation; it does not reproduce the bootstrap, code scoring, or model collection.

## Repository and Course Applications

The [public release](https://github.com/fedear402/agents-metrics-data/tree/51911f03da4d97b249084124eca655b42869c8f8) contains task inputs, reference programs, prompts, scoring rules, and archived runs. The inspected v1.2 tag matches that commit. Its Zenodo record declares CC0. The full run archives expand to approximately 21 GB; the course uses only the three small tables.

M1 §1.19 reconstructs the published comparison. M3 §3.18 connects executable calculations to dependence assumptions. M6 §6.31 examines interaction scales and controlled workflow contrasts. M7 §7.46 evaluates original incorrect programs against the fixed mHealth tasks. M8 §8.30 compares hypothetical review costs and undetected decision errors. M9 §9.24 connects numerical competence to responsibility for customer consequences. No API call or downloaded upstream program was executed for this integration.
