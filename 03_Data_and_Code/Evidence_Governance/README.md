# Evidence, Claims, and Decisions

This original standard-library Python example evaluates whether eight authored claim records justify a public reassurance about electricity costs. It separates record completeness, numerical and outcome checks, support for the prose, and responsibility for a decision.

## Inputs and Comparison

The input is the `residential_reference` row of [the existing reported-table reconstruction](../Statistical_Inference/results/data_center_estimates.csv). It records a coefficient of 0.261 and clustered standard error of 0.158 from Table 2, column 4, with the reference-exposure calculation on pp. 23–24 (Rana et al., 2026). The [source record](../../01_Resources/41_Statistical_Claims_and_Decisions/manifest.json) identifies the paper version and provenance. This is a reconstruction from reported statistics, without the original utility panel.

Multiplying both coefficient and standard error by `100 * 456 / 6804` gives 1.7492 and 1.0589 USD/MWh. Under the stated normal approximation, the two-sided zero-null p-value is 0.0986, the 95% interval is [−0.3262, 3.8246], and the one-sided 95% upper bound is 3.4910 USD/MWh. The reference exposure uses a ratio of reported means. The outcome is utility-average residential electricity price, with no observation of individual household bills.

The eight claim records, reference judgments, managerial approval, and decision history are constructed teaching cases. A reference judgment assesses the complete claim and its traceable support. A correct number with an unresolved source fails that criterion. Neither checker reads the reference judgment when deciding whether to accept a record.

## Run

Python 3.10 or later; no additional packages, model access, credentials, or upstream code.

```sh
cd 03_Data_and_Code/Evidence_Governance
python3 evidence_example.py
python3 -m unittest -v
```

Use `python3 evidence_example.py --out /tmp/evidence_example_results` to write a separate result set. The notes reproduce the complete program in M9 §9.85.5.

## Expected Results

| Checker | Records | Accepted | Unsupported Claims Accepted | Supported Claims Rejected |
| --- | --- | --- | --- | --- |
| Required fields and resolving sources | 8 | 7 | 4 | 0 |
| Above plus quantity, unit, outcome, and number checks | 8 | 4 | 1 | 0 |

The second checker catches the wrong number and the explicit substitution of household bills for the recorded price outcome. It still accepts a record whose valid nonrejection metadata accompany misleading prose asserting no harm. These are deliberately selected diagnostic cases, with three acceptable and five unacceptable records. The counts describe these cases only; they are not population error rates or a comparison of language models.

`append_record` rejects an attempt to overwrite an existing decision filename. A new decision records `supersedes`, leaving both decisions available. This function demonstrates exclusive creation within the teaching program. Filesystem permissions and repository protection would be required to prevent a person or another program from bypassing it.

## Outputs

- [Claim assessments](results/claim_assessments.csv): each statement, reference judgment, checks, and reasons for rejection.
- [Checker comparison](results/checker_comparison.csv): case counts by checker.
- [Reconstructed quantities](results/table_reconstruction.json): inputs, units, and normal-approximation calculations.
- [Decision history](results/decision_history.json) and [preservation checks](results/preservation_checks.json): fictional approval, correction, and preservation results.
- [Manifest](results/manifest.json): hashes of the input, program, and outputs.

The [verification record](VERIFICATION.md) identifies the checks executed. The [resource guide](../../01_Resources/53_Evidence_Governance/README.md) distinguishes the source protocol from the independently implemented course example.
