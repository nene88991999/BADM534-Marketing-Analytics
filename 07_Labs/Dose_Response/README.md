# Discount Response Curves and Customer Outcomes

**Optional, ungraded practice.** The course's released assignment rules remain separate. [M6 §§6.22–6.27](../../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md) and [the code guide](../../03_Data_and_Code/Dose_Response/README.md) provide full explanations, programs, and saved outputs. M8 §8.22 compares decision objectives; M9 §9.18.1 examines customer judgment.

## The Retailer's Decision

A retailer chooses a promotion-week discount for eligible customers. It needs profit at different discount levels for the same population. Managers have previously assigned larger discounts to a customer type with higher expected profit, creating selection. Every record in this exercise is synthetic, and the population response is known. Discount is measured in percentage points, while profit is dollars per eligible customer.

## A 20-Minute Discussion

1. **Minutes 0–4:** Compare the known inverted-U curve with its uniform-randomization linear projection. Explain why a zero linear slope leaves the discount decision unresolved.
2. **Minutes 4–9:** Read the four-model table. Identify which nuisance specification is wrong in each row, and explain why the first three rows need not have the same finite-sample error.
3. **Minutes 9–14:** Compare the two overlap panels and saved effective sample sizes. Explain how rare, heavily weighted observations can be absent from a sample with a high effective sample size.
4. **Minutes 14–20:** Compare pointwise and whole-grid coverage. Choose which comparison would matter for one prespecified discount, and which would matter for searching over the curve. State what additional inference work is required.

## Reproduce and Change the Analysis

Follow the environment and commands in the code guide. Run `test_examples.py`, then all three analysis programs with `--output local_runs`. Compare the regenerated numeric tables with `results/`; small floating-point differences can depend on the numerical library. The source uses independent sample seeds and preserves one fixed reference dataset.

Change one object at a time. Reduce the dose-assignment noise to weaken overlap, change the smoothing bandwidth, or change the weight cap. State the target population and grid before interpreting changes. Examine bias and coverage, including each dose's Monte Carlo standard error. A lower observed error after a chosen modification is evidence about that simulated design, not a general estimator ranking.

For the hidden-confounder extension, derive the conditional mean of U with Bayes' rule and reconcile it with the program's hyperbolic-tangent expression. Explain why perfect prediction of the observed outcome does not identify the intervention curve after U is omitted. Distinguish this failure from the misspecification experiments.

For pooling, inspect stores 0 and 4, the equal-store aggregate comparison, and all nine validation penalty pairs. Explain why partial pooling improves the aggregate while worsening one store's estimate. Propose how repeated samples would evaluate the stability of that ranking. Do not use the known curves to tune the penalty.

## A Decision and Its Justification

Use `decision_objectives.py` to compare the revenue, profit, and complaint-constrained choices. Verify profit as revenue minus unit cost times expected units. Explain the consequence of the 0.1-point search grid. The complaint function and 3% cap are imposed assumptions; a low complaint rate does not establish consent or customer benefit.

Write a recommendation stating the feasible discount range, the target population, the chosen outcome, and the evidence needed before deployment. Identify a practice that would remain unacceptable even if the estimated profit increased. Explain how customers could understand and refuse the offer.

## AI-Assisted Coding

Ask an assistant to explain a short function before requesting a change. Require it to identify the target population, treatment units, nuisance-training folds, and which uncertainty the reported standard error includes. Request one independent hand-check for the proposed modification. Compare its explanation with the saved program and primary sources. Do not describe a generated confidence interval as valid solely because the code executes.
