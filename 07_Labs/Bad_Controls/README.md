# Bad Controls and Thoughtful Research Design

This practice is optional and ungraded. Use the [programs](../../03_Data_and_Code/Bad_Controls/README.md), [readings](../../01_Resources/44_Bad_Controls_and_Project_Exposure/README.md), M3 §§3.20–3.21, and M6 §§6.40–6.42.

## Defend the Comparison

A regulator is considering financial protections for households when a proposed data center fails. Write the intervention, outcome, population, and time horizon before examining the operating-facility dataset. Distinguish the effect of opening an operating facility from the effect of initiating a project that can later fail. Specify whether the outcome is average revenue per MWh, a standardized household bill, or actual household expenditure.

## Predict, Calculate, and Explain

1. Draw a confounder, mediator, and collider graph. Predict which paths conditioning changes. Run `control_paths.py`, then explain why adjusting for the measured confounder improves one comparison while adjusting for an instrument-like variable worsens it.
2. Run `panel_covariates.py`. Derive the true ATT of 4. Explain why both 5.5 and −2 answer the target question incorrectly. Remove knowledge of the baseline variable W conceptually: identify which premise for the imputation would then lack support.
3. Run `project_pipeline.py`. Derive the comparisons 10, 7, and 4 by hand. Name the baseline, donor exposure, and target effect represented by each. Explain why constant canceled-project costs after the opening baseline do not further change that particular difference-in-differences calculation.
4. Compare the full proposal mean with the completed-project mean under both scenarios. Explain why selection can either conceal or exaggerate the burden of the full pipeline. Distinguish a different estimand from a biased estimator of a fixed estimand.
5. In the real case, build an evidence table with event date, publication date, source, project status, utility link, commitment, recovery, and offsets. Use the 2023 cancellation and 2025 institutional sources as leads. Leave unsupported cost cells missing. Describe what the 2026 records can and cannot establish about the prior window.

## Make a Philosophical Argument

Evaluate the proposed principle: “A regulator may reassure households about the full development process whenever an operating-capacity estimate is statistically insignificant.” Identify the household's reason for objection, the required empirical premises, and the strongest defensible reply. State a narrower conclusion that the evidence could support. Explain why residents' missing records do not remove their standing to question the decision.

## AI-Assisted Coding

Ask an assistant to propose a causal graph and a competing graph that would change the adjustment decision. Require it to name the institutional evidence needed to distinguish them. Compare every generated numerical claim against the CSV outputs and your hand calculation. A working regression command, a larger sample, and a narrow interval each leave the identification argument to be defended.
