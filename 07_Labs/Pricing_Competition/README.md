# Pricing Information and Customer Outcomes

This is optional ungraded practice. The [complete example](../../03_Data_and_Code/Pricing_Competition/README.md) includes original Python, synthetic inputs, results, and checks. [M4 §4.26](../../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md) supplies the mathematical setup. [M8 §8.28](../../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md) and [M9 §9.22](../../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md) connect evidence to the Wendy's case and ethical evaluation.

## The Decision

A restaurant operator is evaluating a pricing service. The service can improve its demand signal. A separate proposal would choose the prices of both restaurants to maximize joint profit. Explain how the operator should evaluate those changes and what customer outcomes must accompany the profit comparison.

## Reproduce the Comparison

From the repository root, run:

```bash
python3 03_Data_and_Code/Pricing_Competition/evaluate_market.py
python3 -m unittest discover -s 03_Data_and_Code/Pricing_Competition -p 'test_*.py' -v
```

Read the data dictionary before editing code. Hand-check the independent, uninformative benchmark: posted price $16/3, expected total quantity $80/9, expected profit $800/27, and consumer surplus $872/27. Explain why each objective-accuracy pair has probability mass one and why perfect information retains only two cells.

## Separate the Changed Objects

Compare signal accuracies 0.5 and 1 under independent pricing. Identify which state gains quantity and which loses it. Reconcile unchanged mean posted price with changed consumer surplus and quantity-weighted paid price. Then hold accuracy at 0.5 and compare the independent and joint objectives. Account for changes in consumer surplus, profit, and total welfare separately.

Create an alternative parameter file with substitution set to zero and pass it using `--parameters`, saving results outside the released `results` folder with `--output`. Verify that the independent and joint objectives coincide. Next vary cost or the demand gap one object at a time. An input rejected by the interior-support restriction requires a model extension that explicitly handles quantity corners in the pricing problem.

## Assess Evidence and Justification

Read the [source review](../../01_Resources/37_Pricing_Systems_and_Competition/SOURCE_REVIEW.md). Classify the 2022 data announcement, the 2024 pricing clarification, the complaint's coordination allegation, and the original simulation by the claims each supports. Specify the contracts, pricing records, communications, costs, or adoption information that would change your assessment. Explain why the restaurant-availability data cannot substitute for those observations.

State a proposed pricing maxim and examine its treatment of customers' capacity to choose. Apply Confucian trustworthiness to the explanation of who controls prices and how customer-benefit claims are substantiated. Compare the ability to cancel a subscription with the availability of competing restaurant offers. A recommendation should distinguish empirical findings, legal status, and ethical reasons.

## AI-Assisted Coding

An LLM can explain the code, propose a change, and help inspect an error. Ask it to state the observation unit, probabilities, units, information timing, and changed parameter before generating code. Check the resulting calculation against the exact benchmark, consumer-utility calculation, and surplus identity. Describe material AI assistance accurately, and keep any applicable assignment-specific rules separate from this optional exercise.
