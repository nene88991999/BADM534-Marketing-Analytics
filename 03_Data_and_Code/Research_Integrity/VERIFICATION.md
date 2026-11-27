# Verification Record

Verified November 27, 2026.

## Execution and Independent Checks

Executed `assess_records.py` with Python 3 and `openpyxl`. The input SHA-256 matches `source.json`. The program checked unique masked identifiers, agreement between the supplied font label and actual cell formatting, paired-car counts, and stored policy-average differences. It changed no source cells and executed no downloaded analysis code or workbook macros.

A separate read of the workbook's ZIP/XML contents, without `openpyxl`, independently confirmed 13,488 policy rows, 6,744 rows in each font group, all twelve saved rounding fractions and denominators, all ten mileage-bin counts, the minimum and maximum increments, and the 44-record restriction. It also confirmed that the 22 four-car candidate pairs form a one-to-one match under the stated rule.

The M2 table and TikZ bars use the car 1 multiple-of-100 fractions in `results/rounding.csv`. The plotted percentages use a common denominator, preserve both font groups and both times, and introduce no uncertainty intervals or causal estimates. Unknown measurement intervals remain unknown.

## Scope

These are independently executed descriptive checks of the archived artifact. The exercise does not repeat every analysis in the original investigation, estimate the probability of fabrication, validate the observations as genuine events, or identify an individual fabricator. Publication status and author responses are documented separately in the [source guide](../../01_Resources/52_Research_Integrity_and_Replication/README.md).
