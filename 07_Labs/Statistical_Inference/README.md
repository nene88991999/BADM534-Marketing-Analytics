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
