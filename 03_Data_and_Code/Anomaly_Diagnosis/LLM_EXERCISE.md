# Evidence for a Retail Diagnosis

Use one run from `results/evidence_packets.json` and `data/variable_dictionary.json`. The packet includes observed measurements, missing entries, and alerts produced by the frozen mean-deviation rule. Treat missing values as unknown. The full roster includes nine runs, including those without a constructed incident.

## Prompt

> A retailer must decide whether to investigate an observed change and which additional evidence to obtain. Review the supplied measurements and alert intervals. State what changed, identify the supporting variables and timestamps, and give plausible explanations. Distinguish observations from causal hypotheses. Identify a check that would distinguish the leading hypotheses. State when the evidence is insufficient for a diagnosis. Return a JSON object with `observations`, `hypotheses`, `additional_evidence`, `proposed_action`, and `uncertainty`. Each observation must include its variable, time interval, units, and supporting values. Do not infer customer intent or misconduct from a deviation alone.

## Evaluation

Inspect the response before opening `data/events.csv`. The event table and generator disclose the imposed causes and provide public practice answers. Record separately whether numerical statements agree with the packet, the stated timing fits the observations, the proposed component is supported, the explanation acknowledges credible alternatives, and the proposed response follows from the available evidence. A correct cause name accompanied by fabricated evidence receives a separate factual-error finding.

Compare three input conditions on the same run roster: observations and alerts; the same information plus the variable dictionary; and selected plots of the same measurements with their units and timestamps. The dictionary must add definitions without revealing incident labels. Keep model version, prompt, decoding settings, response, and evaluator judgments. Invalid outputs, missing responses, and abstentions remain in the roster. No model calls or performance results are supplied here.

A stronger evaluation uses newly constructed incidents and independent reference judgments after the prompt and scoring rubric are fixed. The public examples support practice and arithmetic checks. Their disclosed construction makes them unsuitable as a hidden final test after repeated revision.
