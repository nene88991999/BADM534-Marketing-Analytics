# Data Production and Access

An institution can produce accurate bills while releasing a selected view of household consequences. This original synthetic example constructs two populations with identical restricted public records and opposite population effects. It connects data provenance to identification, inverse-probability weighting, and the responsibility to justify public claims.

## Inputs and Run Commands

The program constructs 400 households in each of two alternative worlds, with four strata of 100. All values are synthetic. The previous bill equals the current no-project bill by construction; no other factor changes. This restriction makes the bill change equal the causal effect within the example. No actual utility records, company code, or external services are used.

Python 3.10 or later and the standard library are sufficient. Run from the repository root:

```sh
python3 03_Data_and_Code/Data_Production/data_availability.py
python3 03_Data_and_Code/Data_Production/verify_example.py
```

The seed is `20261126`. The script resolves its output directory relative to its own path, so it also runs from other working directories. Read [the dictionary](DATA_DICTIONARY.md), [results](results/README.md), and [verification record](VERIFICATION.md). The maintained [program](data_availability.py) appears in full in M2 §2.31.

## Comparisons

All means below use USD per household-month. The target denominator is 400; the released denominator depends on the policy.

| World | Release Policy | Released Households | Released Mean | Target Mean | Weighted Mean |
| --- | --- | --- | --- | --- | --- |
| H | A and B only | 200 | -10 | +10 | Undefined |
| H | All A and B; half of C and D | 300 | 10/3 | +10 | +10 |
| H | Half of every stratum | 200 | +10 | +10 | +10 |
| L | A and B only | 200 | -10 | -10 | Undefined |
| L | All A and B; half of C and D | 300 | -10 | -10 | -10 |
| L | Half of every stratum | 200 | -10 | -10 | -10 |

Half-stratum samples are simple random draws of 50 out of 100, without replacement. Effects are constant within each stratum, so weighted recovery is exact for every draw with positive inclusion in every stratum. This exactness does not generalize to arbitrary outcomes. Under restricted release, missing strata have zero inclusion; weighting alone cannot identify their contribution.

With restricted coverage of one half, an observed mean of -10, and an assumed missing-effect range of [-20, 40], the population mean lies in [-15, 15]. Both constructed worlds fit these limits. The limits are illustrative substantive restrictions, not estimates from actual electricity data.

## Interpretation and Provenance

The same public file is compatible with a population increase and a population decline. A more sophisticated estimator cannot distinguish observationally equivalent worlds without additional evidence or restrictions. All current bills exist internally in the construction; access is the changed mechanism. The oracle potential outcomes are supplied by the example's creator and are not claimed to be observed in an ordinary billing system.

The [resource collection](../../01_Resources/45_Data_Truth_and_Norms/README.md) and [electricity assessment](../../01_Resources/45_Data_Truth_and_Norms/ELECTRICITY_ASSESSMENT.md) distinguish this logical example from documented institutional practices. The example estimates neither the data-center paper's coefficients nor the prevalence of selective release. [Optional practice](../../07_Labs/Data_Truth_and_Norms/README.md) connects the calculation to truth, norms, and household reasons.

## Data as Artifacts

The [subscription program](data_artifacts.py) constructs two releases of six synthetic accounts. Both preserve the same history, while the expanded release adds cancellation requests. Five accounts remain subscribed, and three have pending requests. Reordering the expanded file preserves its keyed records while changing its byte hash. The [results and manifest](artifact_results/README.md) distinguish events, schema, release, and physical copy. The complete code appears in M2 §2.34.

Run `python3 03_Data_and_Code/Data_Production/data_artifacts.py`. Python 3.10 or later and the standard library are sufficient. No external data, API, or account is used. This deterministic example requires no random seed. The program checks identifiers, timing, counts, projection between releases, and equality under the stated identity rule. It makes no empirical claim about a company.

M9 §§9.60–9.65 connects the artifact's production and governed use to reasons owed to the people represented. Three hypothetical agreements change access and publication rights while holding this synthetic history fixed. The [restricted-research guide](../../01_Resources/45_Data_Truth_and_Norms/05_Restricted_Research/README.md) supplies the professional-policy sources and their scope.
