# Statistical Evidence for a Marketing Decision

This is public optional ungraded practice. Follow any released assignment's specific AI-use rules when applying these ideas to assessed work.

A retailer is deciding whether a promotion produces enough incremental contribution to justify rollout. An mHealth manager is separately examining a change in recorded logging. Use the [programs and commands](../../03_Data_and_Code/Statistical_Inference/README.md) and the [data dictionary](../../03_Data_and_Code/Statistical_Inference/DATA_DICTIONARY.md).

## Preserve the Customer Comparison

1. Reconstruct the mHealth sample. Explain why membership is fixed before May, why food-entry duplicates do not create new logged days, and why a user without June entries remains in the denominator.
2. Hand-check the monthly fractions for a user with two May logging days and one June logging day. Use the different calendar denominators. Explain what an absent entry measures.
3. Reproduce the paired and independent-day uncertainty calculations. Both reject zero at 5%. Explain why that agreement leaves the independence error consequential, and why the observed change does not identify a promotion effect.

## Evaluate a Test When the Effect is Known

1. Read `simulation.json` before inspecting the p-values. Identify the outcome, assignment unit, number of stores, customer count, and true effect.
2. Use `synthetic_store_customers.csv` to compare customer-row and store-mean calculations. Verify their equal point estimates. Explain the equal-size condition that makes them agree.
3. Derive the variance ratio `1 + (m - 1) * rho`. For m=20 and rho=0.3, compare it with empirical effect dispersion and reported standard errors across simulations.
4. Reproduce all 4,000 experiments per correlation. Explain why the Monte Carlo intervals describe rejection fractions, while the first-experiment intervals describe an effect estimate.
5. Repeat with a new seed without changing the method. For an extension, introduce a fixed nonzero effect and measure power, identifying the changed outcome equation. A multiple-outcome or sequential experiment requires a separately specified testing procedure.

## Assess an AI-Generated Analysis

Ask an assistant to analyze the first store dataset with its assignment design and variable definitions, before giving it the reference results. Require the sample, target, estimator, variance calculation, p-value, interval, and managerial interpretation. Preserve the first response and executed program. Score execution, method, numerical reporting, and interpretation separately using M1 §1.18.

After feedback, freeze the program and evaluate it on fresh simulated data. Keep the original task and new data distinct, retain every run, and record model version and prompts. Do not choose the run with the smallest p-value. The provided program results do not constitute a measured comparison of AI models.

## Examine the Advertising Claim

Read M9 §9.24 and the [benchmark question](../../01_Resources/39_Statistical_Inference_and_AI/benchmark_sample/question.txt). State what rejecting a joint null for 13 advertising coefficients would establish under a valid test. Identify the additional evidence needed to assess borrowing costs, comprehension, and customer agency. Evaluate the firm's justification using both Kantian respect for persons and Confucian responsibilities in a relationship of reliance. The benchmark's reference specification remains unverified here; the question supports discussion without supplying a replicated causal or welfare finding.

## Compare Repeated P-Values and Economic Decisions

1. Run `pvalue_distributions.py`. Compare 40 with 160 stores at a fixed eight-dollar true effect. Reconcile bin counts, rejection fractions, analytical power, and the independent-repeat denominator. Explain why a realized p-value does not supply a probability that the null is true or that a repeat will reject.
2. Run `campaign_decisions.py`. Hand-check the lift, break-even threshold, and expected contribution. Explain why a significant increase can leave the campaign unprofitable under the stated costs.
3. Distinguish the size of a test from the false share of expected rejections in the hypothetical portfolio. Explain what additional sampling assumptions would support a probability about a randomly selected rejected claim.
4. Run `equivalence_claims.py`. For each scenario, state separately the zero-null conclusion, two-sided equivalence conclusion, and one-sided excessive-time conclusion. Explain why the five-second margin requires a substantive justification and which outcomes are absent from completed-task time.

## Assess a Paper Using Its Own Tables

Use the [electricity paper and companion](../../01_Resources/41_Statistical_Claims_and_Decisions/README.md), M6 §6.33, and `data_center_claims.py`.

1. Transcribe Table 2 column 4 independently. Verify the coefficient, clustered SE, units, sample, and reference exposure. Distinguish a ratio of reported means from an average of ratios.
2. Calculate power for externally specified $1 and $2 increases. Calculate a two-sided 95% interval, a one-sided 95% upper bound, and an 80% minimum detectable effect. Explain the different questions they answer. State why low power does not prove the true effect is positive.
3. Read Table 4's direct equality test. Explain why the subgroup significance stars cannot replace it. Identify the covariance needed to construct the contrast independently.
4. Use Table 7 to assess a hypothetical MW operating at 25% and 50% utilization during a full quarter. Explain what additional evidence would identify an infrastructure-cost mechanism.
5. Reconstruct the 4% contribution and 96% residual using Table A.4. Identify the further causal decomposition required to attribute the residual to particular causes.
6. Compare the definitions of the model's total revenue requirement, the cost-per-MWh outcome, the ownership categories, and the business-model claims. Record each claim, exact page/table, evidentiary problem, consequential interpretation, and evidence needed for resolution.
7. Separate established interpretation problems from design questions requiring raw data. Propose one sensitivity analysis for donor spillovers, cumulative-treatment variation, delayed recovery, and specification multiplicity. Do not report an unexecuted check as a result.

## Evaluate Public Reassurance and Household Agency

Assess the unsupported categorical HBS reassurance [(Kost, 2026)](https://www.library.hbs.edu/working-knowledge/blaming-data-centers-for-higher-electric-bills-its-not-that-simple) using M8 §8.31.1 and the [public-communication guide](../../01_Resources/41_Statistical_Claims_and_Decisions/PUBLIC_COMMUNICATION_AND_PUBLICATION.md). The central question is when the label “statistically insignificant” supplies no substantive conclusion about harm.

1. Record the exact reassurance, speaker, date, population, and period. Locate the future-price qualification and explain whether it resolves the historical claim.
2. Reconstruct Table 4's four-developer interval with `data_center_claims.py`. State its units and explain why a positive estimate with this uncertainty supports neither categorical harmlessness nor proof of harm. Use the direct equality test to assess the developer contrast.
3. Supply the missing premise for a small-harm claim: a justified threshold, adequate precision, and a research design that measures the relevant burden. Explain why a precise estimate near zero and an imprecise estimate can both be insignificant while supporting different decisions. Distinguish a test's size, power against a specified alternative, and its realized p-value.
4. Compare the HBS interpretation with the other two linked readings. Separate headline, body, and qualifications. Identify which wording preserves the distinction between nonrejection and absence, and justify any criticism using the original table.
5. Write a replacement statement that preserves the estimate, uncertainty, and scope. A supported starting point is: “The reported four-developer estimate is positive and imprecise; the analysis leaves positive price effects unresolved.” Explain the remaining distinction between average residential prices and household bills.
6. State a principle for university research communication and a household's strongest reasonable objection to it. Answer: “What justification does a university owe residents before using its authority to reassure them about costs that its evidence leaves unresolved?” Explain what the institution ought to disclose or correct and why that response addresses the objection.

A corporate dissemination claim requires a specific verified corporate statement. Distinguish the harm a misleading inference could cause from observed consequences established by evidence of the communication's use.

Use the synthetic household allocations to explain why equal mean prices leave distribution unresolved. Then specify evidence about access to reasons, challenge, review, and remedy. Distinguish payment, compliance, endorsement, and authorization. Evaluate a rule that permits interested firms to call an insensitive non-rejection harmless using Kantian universalization, respect for persons, and Confucian trustworthiness. State a defensible approval recommendation, a justified harm threshold, the unresolved risks, and which party should substantiate or bear them.

## Reconstruct and Test an Argument

Use M6 §6.34, M9 §9.27, and the [argument record](../../01_Resources/41_Statistical_Claims_and_Decisions/ARGUMENT_ASSESSMENT.md).

1. Choose one exact claim and record its speaker, page or table, population, time horizon, and degree of certainty. Separate a quotation from your reconstruction.
2. List the reported premises and the additional premise needed for the conclusion. Classify its role: measurement, identification, extrapolation, sampling, or ethical justification.
3. Construct an account in which the reported premises hold and the conclusion fails. Explain which observation could exclude it. Do not present logical possibility as an estimated likelihood or an observed harm.
4. Run `andrews_inverse_power.py`. Reproduce the 50%, 80%, 90%, and 95% thresholds. Explain why the MDE remains fixed when the realized estimate changes while the confidence bound moves. Identify the inverse-power contribution (Andrews, 1989) and the fixed-Wald approximation used here.
5. Use the joint synthetic test to explain why a nonsignificant multivariate result needs direction-specific sensitivity. Identify why the paper's marginal developer SEs are insufficient to perform that calculation for its contrast.
6. Run `logical_counterexamples.py`. Verify exact historical agreement and the future divergence. State the extrapolation restriction that would rule out the threshold account, then identify evidence that could justify it.
7. Write the strongest conclusion currently supported. Preserve contrary findings and qualifications. State what would change your assessment.

A complete response distinguishes a validity failure from a false premise, a scope change, and a genuine contradiction. It uses the reported joint test, preserves units and reference exposure, and keeps harm, intention, and corporate dissemination tied to verified evidence. These are discussion criteria for public ungraded practice.

## Assess the Institutional Comparison

Use the original `institutional_exposure.py` program and M6 §6.35. This practice is optional and ungraded.

1. Reconstruct mean expenditure from revenue, energy sales, and customer-months. Explain why unchanged average revenue per MWh can coexist with higher bills.
2. Verify the three-utility table and its USD 4/MWh change difference. Identify the cost subtracted by the weighted donor comparison.
3. Change the cancelled-project cost to zero, ten, and a negative value. Explain which assumptions determine the direction of the resulting difference.
4. Move a preparatory cost into the fitting period or a recovery charge beyond the observation horizon. State the resulting timing problem without claiming to replicate the paper's estimator.
5. Compare full and partial developer payment, disallowed recovery, and asset reuse. Keep all cost inputs in annual dollars before dividing by annual MWh.
6. Propose a dated project panel and a donor screen using information available at the comparison date. Explain why selecting only eventual successes or failures could introduce further selection.
7. State the additional evidence needed to distinguish an institutional risk from a demonstrated error in the published estimate. Separate price, expenditure, affordability, and authority to allocate costs.

## Evidence and the Proposed Action

Use [Evidence Standards and Reasonable Protection](../Evidence_Standards/README.md) to distinguish an inquiry, a temporary safeguard, and a remedy. Compare the consequences of false alarms and missed harm, defend the interests included in the analysis, and answer the strongest reasonable objection. The complete synthetic calculation appears in M6 §6.44; M9 §§9.55–9.59 connects the decision to disciplinary history and institutional standards.

## Modern Power and Harm Bounds

A household is deciding whether public reassurance about data centers and electricity costs is warranted. Read M6 §§6.47–6.51 and M9 §9.83, then use the [source guide](../../01_Resources/51_Modern_Power_and_Harm_Bounds/README.md) and [reproducible example](../../03_Data_and_Code/Modern_Power/README.md).

1. Run `harm_bounds.py` and `verify_harm_bounds.py`. Reconcile the six price comparisons and three assumed bias bounds with the notes. State the reported source cell, units, reference exposure, and fixed Gaussian approximation.
2. Draw the two rejection regions for the residential example. Explain why a zero-null nonrejection provides no test of a positive harm margin.
3. Explain how 80.9% power at USD 3/MWh can coexist with failure to exclude that increase. Compare repeated-sample power with the realized one-sided upper bound.
4. Derive the scalar folded-normal critical region. Compare its rejection condition with TOST and check its probability at both boundary values. Explain the scope of the result for the six displayed margins.
5. Defend a meaningful price margin from a household's perspective. Identify the consumption, fixed-charge, income, distributional, and horizon information needed to translate a utility-average price effect into a burden.
6. Select one full-design method from the reading guide. Specify its missing inputs and explain how canceled-project exposure could affect the target or donor comparison. Do not substitute an assumed SE multiplier for those inputs.
7. State a definite judgment about the categorical HBS reassurance and support it with the reported estimate and unresolved margins. Separately identify the paper's unsupported affordability interpretation, residual attribution, and significance convention. Defend a correction through a normative premise about reasons owed to residents. Distinguish this demonstrated communication failure from an allegation about intention or a realized household loss.
