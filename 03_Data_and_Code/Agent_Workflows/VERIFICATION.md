# Verification Record

Verified November 24, 2026 with Python's standard library. The source builder read the existing local mHealth release after verifying SHA-256 `2ee04b155a93d51a02ee5acb61ff88a0dde2990b4713668c1b824ae6999ffbea`. It produced a 358-user prior-period roster and two compact task inputs. Input hashes are recorded in [manifest.json](manifest.json).

Executed `build_tasks.py`, `logging_reference.py`, `workflow_costs.py`, and the CSV grader against the valid reference. Eight tests in `test_workflows.py` passed. They cover distinct days, interval boundaries, zero-log users, duplicate roster keys, invalid dates and windows, correct-output acceptance, equal-total customer misassignment, missing and duplicate output rows, nonfinite values, cost denominators, and an independent SQL comparison of every actual customer count in both tasks.

The reference calculation uses sets of dates; the independent comparison uses a SQLite left join and `COUNT(DISTINCT ...)`. The synthetic known-answer case is A=1, B=1, C=0 over 31 days, giving 2/93. The cost example recomputes 350/80 and 200/95 under its explicitly hypothetical inputs.

The CSV grader does not execute generated code. No model calls, external data uploads, upstream package execution, empirical labor-time measurements, or measured comparison of the four AI configurations occurred. Rendering and code-to-notes checks are recorded in the course build documentation; they establish separate properties from the substantive interpretation.
