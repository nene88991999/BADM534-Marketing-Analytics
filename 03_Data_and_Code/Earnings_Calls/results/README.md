# Earnings-Call Results

Executed November 2, 2026 using the supplied snapshot. Four analysis programs and nine counterexample tests passed. The source hash manifest verifies the exported inputs; no live transcript collection or model API was run.

- The roster has 123 firms; 122 have supplied calls. Of 2,326 calls, 2,325 have positive word counts. The empty Dollar Tree record is unknown for language presence.
- Core terms occur in 112 observed calls (4.8172%). Restricting the denominator to 445 calls with any dictionary match raises the apparent rate to 25.1685% by selection.
- Core-call rates are 36/1,241 (2.9009%) in retail, 9/445 (2.0225%) in restaurants, and 67/639 (10.4851%) in the supplied comparison group. These are call-weighted disclosure rates in a selected corpus.
- Management accounts for 127 core matches in 16,685,338 attributed words (0.076115 per 10,000 words); analysts account for 23 in 2,761,999 words (0.083273). Among 2,240 nonempty calls with detected Q&A, the management rate is 115/15,985,597 × 10,000 = 0.071940; the analyst rate remains 0.083273. Role and format differences remain material.
- In the common-firm comparison group around the February 27, 2024 clarification, 27 calls from the same 27 firms appear in each 90-day window. Core occurrences fall from five to two; two calls contain core language in each window, so incidence remains 7.4074%. This descriptive comparison supplies no untreated counterfactual.
- Eight synthetic sentences expose lexical and substantive differences: denial, future intention, questions, price displays, and infrastructure can match; a paraphrase of current demand-responsive fares can fail to match. Seven selected real-call paraphrases provide interpretation cases. No population accuracy estimate follows.

`call_status.csv`, `firm_coverage.csv`, and `assessment.json` document inclusion. `group_rates.csv`, `role_rates.csv`, and `quarter_rates.csv` document denominators. `event_windows.csv` records both samples, all three windows, call counts, and firm-equal rates. `synthetic_construct_checks.csv` and `interpretation_summary.csv` separate imposed tests from actual disclosure examples. The three TikZ figures are generated from these tables with explicit value checks.
