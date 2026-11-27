# Subscription Records and Their Intended Uses

The records are synthetic. All six accounts were subscribed at the start of January 2027. Four accounts submitted cancellation requests before the cutoff, 00:00 UTC on February 1. One request was completed; three remained pending. No new subscription or other closure occurs in this constructed history.

| Quantity | Numerator | Denominator | Result |
|---|---:|---:|---:|
| Retained accounts | 5 | 6 initial accounts | 83.33% |
| Pending requests | 3 | 4 submitted requests | 75% |
| Retained accounts with pending requests | 3 | 5 retained accounts | 60% |

`retention_v1.csv` contains subscription status. `assessment_v2.csv` adds submitted and completed request indicators. Projecting V2 onto the V1 columns reproduces V1 exactly. `assessment_v2_reordered.csv` changes only row order. Under the declared identity rule, the two V2 files contain the same records despite different byte hashes.

`manifest.json` records the cutoff, population, unit, intended uses, release relationship, identity rule, and file hashes. `summary.json` records counts and fractions. A hash verifies a file's bytes against a reference; it supplies no evidence that the records describe real events. The synthetic example establishes coexistence of the two descriptive results. It identifies neither a causal effect of cancellation procedures nor the prevalence of obstructed cancellation in any company.

Reproduce with `python3 03_Data_and_Code/Data_Production/data_artifacts.py` from the repository root. The program uses the Python standard library and overwrites only these generated example files.
