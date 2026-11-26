# Logging and Workflow Results

The logging calculations use transformed real mHealth records and a roster fixed from January–June observations. The two task windows use 358 users and 31 days per user, giving 11,098 possible user-days each.

| Task | Recorded User-Days | Zero-Log Users | Mean Logging Rate |
| --- | ---: | ---: | ---: |
| July development | 6,455 | 39 | 58.16% |
| August evaluation | 6,501 | 41 | 58.58% |

[logging_summary.json](logging_summary.json) retains the exact fractions and excluded boundary-row counts. The reference CSVs provide one row per roster user. An independent SQLite calculation reproduces every customer count in both files. The same roster is used in both periods; the rate concerns record presence, not intake or health.

[hypothetical_costs.json](hypothetical_costs.json) uses invented model charges, valid-output counts, review time, and correction time. At 60 dollars per analyst hour, its two total costs are 350 and 200 dollars, with 80 and 95 valid outputs out of 100 assigned tasks. These values illustrate cost accounting and are not measured model performance or labor savings.

No four-configuration model experiment was executed. The [protocol](../EXPERIMENT_PROTOCOL.md) identifies how to collect those outcomes separately.

## Published Coding Benchmark

`benchmark_failure_rates.csv` reconstructs success and failure fractions from the authors' integer counts. `benchmark_prompt_contrasts.csv` reports percentage-point gains and fractions of baseline failures removed. `benchmark_incremental_cost.csv` divides the additional mean token cost per assigned run by the additional success probability, separately by model. `benchmark_summary.json` records scope and aggregate contrasts. Inputs come from the identified CC0 release; these files contain no newly collected model runs.

Each workflow has 14,400 assigned runs. The agent's 338 silent failures represent 2.35% of assigned runs and 89.18% of 379 failures. The example prompt adds 4.42 percentage points under the chatbot and 0.79 under the agent, removing 23.86% and 26.15% of their no-example failures. These are different denominators. The two-panel TikZ figure retains the authors' task-cluster intervals from the source CSV.

## Constructed Coding Errors

`semantic_checks.csv` evaluates eight constructed programs on each of the two mHealth tasks. The cases are deliberately chosen and supply no estimate of their frequency in model output. A total-only check accepts four incorrect cases per period: a wrong exposure denominator, reassigned users, omitted zero-log users, and a missing rate value. The complete per-user comparison rejects all seven incorrect cases in each period and accepts both correct cases.

The July shifted-user case changes 331 users' values while retaining 6,455 recorded user-days and the 58.16% mean. In August it changes 324 users while retaining 6,501 days and a 58.58% mean. `semantic_summary.json` counts these constructed checks. Missing output values remain blank; they are not zeros.

## Hypothetical Losses

`decision_costs.csv` and `decision_cost_summary.json` use hypothetical task costs and undetected-error probabilities. For 1,000 analyses, operating costs are 270 and 550 dollars. At a ten-dollar conditional loss, expected total costs are 770 and 650 dollars. The seven-dollar crossing follows from 280 dollars of additional operating cost divided by 40 fewer expected undetected errors. Neither review savings nor customer harm is estimated.
