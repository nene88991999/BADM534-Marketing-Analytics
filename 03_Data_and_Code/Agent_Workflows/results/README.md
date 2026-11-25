# Logging and Workflow Results

The logging calculations use transformed real mHealth records and a roster fixed from January–June observations. The two task windows use 358 users and 31 days per user, giving 11,098 possible user-days each.

| Task | Recorded User-Days | Zero-Log Users | Mean Logging Rate |
| --- | ---: | ---: | ---: |
| July development | 6,455 | 39 | 58.16% |
| August evaluation | 6,501 | 41 | 58.58% |

[logging_summary.json](logging_summary.json) retains the exact fractions and excluded boundary-row counts. The reference CSVs provide one row per roster user. An independent SQLite calculation reproduces every customer count in both files. The same roster is used in both periods; the rate concerns record presence, not intake or health.

[hypothetical_costs.json](hypothetical_costs.json) uses invented model charges, valid-output counts, review time, and correction time. At 60 dollars per analyst hour, its two total costs are 350 and 200 dollars, with 80 and 95 valid outputs out of 100 assigned tasks. These values illustrate cost accounting and are not measured model performance or labor savings.

No four-configuration model experiment was executed. The [protocol](../EXPERIMENT_PROTOCOL.md) identifies how to collect those outcomes separately.
