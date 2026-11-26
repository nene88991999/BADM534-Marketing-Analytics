# Verification Record

Verified November 24, 2026 with Python's standard library. The source builder read the existing local mHealth release after verifying SHA-256 `2ee04b155a93d51a02ee5acb61ff88a0dde2990b4713668c1b824ae6999ffbea`. It produced a 358-user prior-period roster and two compact task inputs. Input hashes are recorded in [manifest.json](manifest.json).

Executed `build_tasks.py`, `logging_reference.py`, `workflow_costs.py`, and the CSV grader against the valid reference. Eight tests in `test_workflows.py` passed. They cover distinct days, interval boundaries, zero-log users, duplicate roster keys, invalid dates and windows, correct-output acceptance, equal-total customer misassignment, missing and duplicate output rows, nonfinite values, cost denominators, and an independent SQL comparison of every actual customer count in both tasks.

The reference calculation uses sets of dates; the independent comparison uses a SQLite left join and `COUNT(DISTINCT ...)`. The synthetic known-answer case is A=1, B=1, C=0 over 31 days, giving 2/93. The cost example recomputes 350/80 and 200/95 under its explicitly hypothetical inputs.

The CSV grader does not execute generated code. No model calls, external data uploads, upstream package execution, empirical labor-time measurements, or measured comparison of the four AI configurations occurred. Rendering and code-to-notes checks are recorded in the course build documentation; they establish separate properties from the substantive interpretation.

## Econometric Coding Evidence

Verified November 26, 2026 with Python 3.14.0 and the standard library. Three source CSVs match the retrieved v1.2 release byte for byte. The [source manifest](../../01_Resources/40_Econometric_Coding_Workflows/manifest.json) records the pinned commit, matching Zenodo release, CC0 declaration, and file hashes. The six existing mHealth task-input hashes continue to match [manifest.json](manifest.json).

Executed `benchmark_evidence.py`, `semantic_checks.py`, `decision_costs.py`, and `build_coding_figures.py`. A clean copy reproduced all eight result files and both TikZ sources byte for byte. Eleven tests in `test_coding_evidence.py` and the eight existing workflow tests passed. The new checks cover count partitions, zero-failure denominators, prompt-effect scales, source counts, shifted customer values, date boundaries, entry counts, exposure denominators, missing rows and values, duplicate records, nonfinite values, and the hypothetical cost crossing.

The July reference retains 6,455 observed user-days across 358 users and 31 days. Shifting those counts between users changes 331 users' values while preserving the total and mean rate. Four incorrect cases per period pass a total-only check. These deliberately constructed errors establish weaknesses of that check; their frequencies are not estimated LLM error rates. The hypothetical cost calculation equates the two workflows at seven dollars of conditional loss per undetected error, giving expected total cost of 620 dollars for 1,000 assigned tasks.

The general lecture-example checker also passed in a separate copy. All 14 generated CSV and JSON files match the existing examples after newline normalization. The extension's [manifest](coding_evidence_manifest.json) records programs, numerical outputs, TikZ sources, dependencies, and hashes. The original model runs, bootstrap, and source repository programs were not executed. No model API calls or data uploads occurred.
