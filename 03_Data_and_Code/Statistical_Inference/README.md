# Statistical Inference and AI-Assisted Analysis

A manager needs uncertainty calculated for the comparison that informs the decision. These original programs reconstruct observed mHealth logging and simulate a store-randomized promotion. They distinguish a program that runs, a justified method, a faithfully reported number, and a supported managerial conclusion.

## Inputs and Commands

Use Python 3.12 with the pinned [requirements](requirements.txt). From the repository root:

```bash
python3 -m pip install -r 03_Data_and_Code/Statistical_Inference/requirements.txt
python3 03_Data_and_Code/mHealth/download_data.py
python3 03_Data_and_Code/Statistical_Inference/mhealth_pairing.py
python3 03_Data_and_Code/Statistical_Inference/store_randomization.py
python3 03_Data_and_Code/Statistical_Inference/build_figures.py
python3 -m unittest discover -s 03_Data_and_Code/Statistical_Inference -p 'test_*.py' -v
```

The downloader verifies the existing public mHealth release. Skip it when the release files are already present. The food-entry file is about 304 MB compressed; the program checks its hash and reads identifiers and dates in chunks. The simulation needs no external data. The figure builder writes two editable sources under `06_Lecture_Notes/figures`.

## Comparisons and Expected Results

- `mhealth_pairing.py` fixes the established cohort before May 2016, retains zero-log users, and counts distinct calendar days. The 340-user mean change is -5.123 percentage points. The paired standard error is 1.379 pp; the deliberately incorrect independent-day comparison gives 0.663 pp. Both reject zero at 5%, demonstrating that decision agreement can conceal a precision error. This is a descriptive change in logging.
- `store_randomization.py` generates 4,000 independent experiments at each within-store correlation, with 40 stores and 20 customers per store. The effect is zero for every customer. At correlation 0.3, the customer-row test rejects in 44.9% of experiments, compared with 4.7% using store means. The first experiment is retained without selecting on its result.
- `build_figures.py` draws assignment and outcome units and plots rejection fractions with Monte Carlo intervals. Counts and numerical values are in the [results](results/README.md).

The programs use Student/Welch approximations. The simulation comparison covers independent Gaussian stores, balanced assignment, equal customer counts, complete observation, and one prespecified hypothesis. Unequal sizes, few clusters, non-Gaussian shocks, spillovers, missing outcomes, sequential monitoring, and selection among outcomes require additional design choices. No AI model performance is measured by these reference calculations.

## Course Connections and Provenance

Complete code appears in M3 §3.18 and M6 §6.30. M1 §1.18 supplies the assessment protocol; M9 §9.24 examines advertising response and customer reasons. The [optional ungraded lab](../../07_Labs/Statistical_Inference/README.md) includes hand checks, method comparison, and an optional recorded AI exercise.

The [Fisher-R1 source review](../../01_Resources/39_Statistical_Inference_and_AI/README.md) motivates statistical assessment. Its code was inspected and linked, without copying or execution. These Python programs are original course implementations. The benchmark's consumer-credit question is discussion material; its reference p-value has not been independently reproduced. See the [data dictionary](DATA_DICTIONARY.md), [manifest](manifest.json), and [verification record](VERIFICATION.md).

## P-Values, Decision Thresholds, and Electricity-Price Claims

From the repository root, run:

```bash
python3 03_Data_and_Code/Statistical_Inference/pvalue_distributions.py
python3 03_Data_and_Code/Statistical_Inference/campaign_decisions.py
python3 03_Data_and_Code/Statistical_Inference/equivalence_claims.py
python3 03_Data_and_Code/Statistical_Inference/data_center_claims.py
python3 03_Data_and_Code/Statistical_Inference/build_claim_figures.py
```

`pvalue_distributions.py` generates 20,000 independent experiment pairs per scenario, with 40 or 160 stores and true effects of zero or eight dollars. `campaign_decisions.py` uses hypothetical purchase counts and fixed contribution inputs. `equivalence_claims.py` uses hypothetical sufficient statistics, rather than pretending to observe individual task times. `data_center_claims.py` transcribes published coefficients and their clustered standard errors, computes sensitivity and bounds, and supplies a synthetic household-incidence counterexample. No utility-level panel or original estimator is reproduced.

Full source listings appear in M3 §3.19, M6 §§6.32–6.33, and M9 §9.25. The five additional editable TikZ figures cover repeated p-values, campaign profit, equivalence, electricity-price power, and household incidence. The recurring electricity case also appears in M2 §2.28, M8 §8.31, and M9 §9.26. Read the [resource guide and claim assessment](../../01_Resources/41_Statistical_Claims_and_Decisions/README.md) before extending its conclusions.

## Inverse Power and Logical Counterexamples

```bash
python3 03_Data_and_Code/Statistical_Inference/andrews_inverse_power.py
python3 03_Data_and_Code/Statistical_Inference/logical_counterexamples.py
python3 03_Data_and_Code/Statistical_Inference/build_logic_figures.py
```

Run from the repository root with the existing NumPy, pandas, and SciPy environment. `andrews_inverse_power.py` uses the inverse-power approach (Andrews, 1989) to invert noncentral chi-squared power at fixed covariance. It exports scalar thresholds, assumed precision scenarios, and an explicitly synthetic two-outcome comparison. Full code is in M6 §6.34. `logical_counterexamples.py` uses exact rational arithmetic to construct historical agreement with future divergence and cost-ratio counterexamples; full code is in M9 §9.27. Its outputs are synthetic, with no utility observations. The figure builder maps those tables into two editable Illinois-color TikZ sources. See the [argument assessment](../../01_Resources/41_Statistical_Claims_and_Decisions/ARGUMENT_ASSESSMENT.md).

## Institutional Exposure and Household Costs

Run `python3 03_Data_and_Code/Statistical_Inference/institutional_exposure.py`, then `python3 03_Data_and_Code/Statistical_Inference/build_logic_figures.py`. The first program creates four synthetic CSV tables covering matched price/bill denominators, operating additions and cancelled-project costs, a weighted two-period comparison, and annual cost recovery. Full source appears in M6 §6.35. The four-dollar comparison gap and eight-dollar unprotected recovery example follow imposed inputs; neither estimates an actual utility effect. Read the [institutional assessment](../../01_Resources/41_Statistical_Claims_and_Decisions/INSTITUTIONAL_ASSESSMENT.md) for project states, source dates, and the additional records needed to evaluate the paper.

## Further Price-Margin Analysis

The [Modern Power example](../Modern_Power/README.md) connects the reported-price assessment to explicit harm margins, scalar equivalence, and bounded bias. Its six comparisons and complete Python appear in M6 §§6.47–6.51; [optional practice](../../07_Labs/Statistical_Inference/README.md#modern-power-and-harm-bounds) develops the interpretation.
