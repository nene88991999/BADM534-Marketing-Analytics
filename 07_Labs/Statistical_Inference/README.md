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

Compare the verified HBS article with the reported bounds. Identify the speaker, exact claim, date, population, and uncertainty. A corporate dissemination claim requires a specific verified corporate statement. Distinguish the harm a misleading inference could cause from observed consequences established by a causal study.

Use the synthetic household allocations to explain why equal mean prices leave distribution unresolved. Then specify evidence about access to reasons, challenge, review, and remedy. Distinguish payment, compliance, endorsement, and authorization. Evaluate a rule that permits interested firms to call an insensitive non-rejection harmless using Kantian universalization, respect for persons, and Confucian trustworthiness. State a defensible approval recommendation, a justified harm threshold, the unresolved risks, and which party should substantiate or bear them.
