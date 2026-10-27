# Agent Guide for Generative-AI Demand

Read the root `AGENTS.md`, this folder's README, and the data dictionary before analysis. Use Marketing Analytics as the course title.

- Distinguish the supplied public captures from the entirely synthetic consumer panel. Treat provider names and simulated release dates as labels and inputs, not actual market observations.
- Run the offline programs for the course results. Do not silently replace captures with live values or call paid model APIs. Original collector and notebook outputs have a separate verification status.
- Preserve the full consumer denominator, available-provider support, calendar completeness, and one-row-per-observation keys. Unknown pageview records remain unknown.
- Compare provider and category retention within the same starting cohort. Report endpoint and continuous retention separately. Cohorts of existing subscribers differ from acquisition cohorts.
- `new` means newly held relative to the preceding month. Use history to separate first entry, category return, replacement of prior providers, and additions. State whether the denominator is events or consumers.
- Stock and flow price slopes are descriptive projections of a heterogeneous dynamic simulation. An exact binary-logit benchmark passes a parameter-recovery check by construction; this does not establish identification in the dynamic panel or the real market.
- Do not infer nested-logit parameters from retention gaps, public release dates from marketplace timestamps, or paid adoption from app ranks or pageviews.
- Keep matching Python blocks in M2 §2.17, M4 §4.14, and M8 §8.13 synchronized. Re-run affected analyses and counterexamples, regenerate figures when needed, and update the source-hash record without editing original data.
