# Evidence Standards, Error Costs, and Reasonable Protection

By Nathan Yang

This is optional ungraded practice. An authority must decide whether to obtain records, limit exposure temporarily, or seek a remedy for a suspected harmful practice. The exercise separates the evidence about harm from the reasons for the particular action.

## Preparation

Read M4 §4.30, M6 §§6.44–6.45, and M9 §§9.55–9.59 in the [lecture notes](../../06_Lecture_Notes/README.md). The [historical readings](../../01_Resources/46_Measurement_and_Disciplinary_History/README.md) and [evidence-standards readings](../../01_Resources/47_Evidence_Standards_and_Error_Costs/README.md) include supporting and contrary arguments. The [complete program and calculation](../../03_Data_and_Code/Evidence_Standards/README.md) use only Python's standard library and synthetic inputs.

## Predict Before Calculating

The unit is one hypothetical case before its signal is observed. Ten percent of cases involve the specified harm. Signals have normal distributions with means zero and two, respectively, and variance one in both states. A rule acts when the signal exceeds a cutoff. Correct decisions have zero loss.

1. Hold the signal distributions fixed. Predict how the preferred threshold changes when missed harm becomes twenty times as costly as mistaken intervention. Explain who bears each mistake.
2. Reverse those costs. Predict whether a five-percent significance rule remains preferable to a one-percent rule. State which action could plausibly have such costly false positives.
3. Identify the further information needed before using these choices in a pricing investigation or an electricity proceeding. The assumed harmful share, effect size, and costs are illustrative inputs.

## Reproduce and Inspect

From a course checkout, run:

```sh
python3 03_Data_and_Code/Evidence_Standards/error_costs.py
```

The program writes [six decision comparisons](../../03_Data_and_Code/Evidence_Standards/results/decision_rules.csv), [a threshold curve](../../03_Data_and_Code/Evidence_Standards/results/risk_curve.csv), and [the setup and checks](../../03_Data_and_Code/Evidence_Standards/results/summary.json). The complete source appears in M6 §6.44.4 and [error_costs.py](../../03_Data_and_Code/Evidence_Standards/error_costs.py).

4. Derive expected loss for the five-percent rule using the two population shares and conditional error rates. Explain why the false-positive rate is multiplied by 0.90 and the missed-harm rate by 0.10.
5. Reconcile the analytical minimum with the separately enumerated grid. Check why numerical agreement verifies computation without establishing the ethical validity of the costs.
6. Explain why a p-value cannot replace the posterior probability in the rule `q > C_FP / (C_FP + C_FN)`.

To compare additional assumptions without changing the saved course outputs, run this complete sensitivity calculation from the example folder:

```sh
cd 03_Data_and_Code/Evidence_Standards
python3 - <<'PYTHON'
from math import isclose
from error_costs import optimal_cutoff, expected_loss, error_rates

# Synthetic sensitivity: the signal separation remains two standard deviations.
for prevalence in (0.01, 0.10, 0.30):
    cutoff = optimal_cutoff(1, 20, prevalence=prevalence)
    alpha, beta = error_rates(cutoff)
    loss = expected_loss(cutoff, 1, 20, prevalence=prevalence)
    separate = (1 - prevalence) * alpha + prevalence * beta * 20
    assert isclose(loss, separate, abs_tol=1e-12)
    print(f"share={prevalence:.2f}, cutoff={cutoff:.6f}, "
          f"false_positive={alpha:.6f}, missed_harm={beta:.6f}, "
          f"loss={loss:.6f}")
PYTHON
```

7. Explain why a higher assumed harmful share lowers the preferred cutoff under fixed costs and signal distributions. Identify institutional evidence that could inform this share, and explain how a selected complaint sample could distort it.

## Assess the Demand Model

8. A firm claims that flexible heterogeneity explains observed prices. Distinguish model fit, identified conduct, and a justified pricing practice. State the outside option, cost, instrument, and prior assumptions that matter.
9. Derive the single-product markup relation in M4 §4.30.1. Explain why lower absolute elasticity can imply a larger markup. Give a reason that the mathematical operation of integrating tastes supplies no general direction of enforcement bias.
10. Describe a case in which dependence generates an accurately predicted willingness to pay. State the extra premise needed to treat targeting that dependence as permissible. Consider the strongest defense, including access or lower prices for other customers.

## Develop an Ought Argument

Choose targeted pricing or household electricity. Write one connected argument with the following components:

- An affected person, a serious possible burden, and a feasible alternative.
- An ontological premise identifying the interest beyond its recorded proxy.
- An epistemic premise supported by records or testimony, with timing and contrary evidence.
- A normative principle that considers objections from both exposed consumers and people harmed by mistaken restriction.
- A proportionate action, its institutional authority, a review process, and a condition for revision.

For electricity, distinguish realized price, bills, consumption sacrifice, and infrastructure exposure. Preserve the difference between a possible phantom-project mechanism and demonstrated contamination of a particular control group. The [qualitative case](../../03_Data_and_Code/Utility_Cost_Recovery/README.md) records timing and exact excerpts; many selected calls occur after the paper's study period. For pricing, distinguish a positive markup, statutory price gouging, anticompetitive conduct, and a moral objection. The [legal crosswalk](../../01_Resources/16_AI_Experimentation_and_Pricing/ANTITRUST_AND_REASONS.md) states the relevant predicates.

## Compare the Institutional Rules

11. Compare a rule that permits commercial deployment on forecasts with a rule requiring precise causal proof before a low-cost safeguard. Identify who bears uncertainty. Give the strongest reason for the asymmetry and the strongest reasonable objection.
12. Explain how definitions of harm, admissible evidence, and rigor could organize this allocation. State what institutional evidence would establish that the rule actually operates in a particular setting. A conceptual possibility establishes no finding of intentional concealment.
13. Assess the claim that a discipline's emphasis on measurement displaces ethical ends. Use the Cowles change of motto, the role of theory, and continuing societal marketing research to qualify the history. Distinguish missing empirical quantities from Kantian noumena.

## Reasoning and Numerical Checks

With costs one and twenty, the five-percent rule has expected loss 0.767480; the minimum has loss 0.408341 at cutoff 0.600746. Reversing the costs raises the minimum-loss cutoff to 3.596478. Under these reversed costs, the one-percent rule has lower loss than the five-percent rule. These checks preserve the artificial population and comparable loss units.

A strong philosophical response states why its factual premises are credible and why its principle is reasonable from affected positions. It answers a serious objection, preserves a condition that could defeat the conclusion, and avoids treating numerical precision as moral permission. A different recommendation can satisfy these criteria. Expected-loss aggregation is informative while leaving open whether an individual's serious burden can be justified by many small benefits to others.

## AI-Assisted Work

Ask a coding assistant to explain the population denominator before changing a parameter. Require it to distinguish a posterior probability, p-value, power at a specified alternative, and expected loss. Verify one calculation independently. For the argument, ask for the strongest objection and evidence that would change a premise; assess the response against the cited sources rather than treating fluent wording as support.

## Reanalyze Released Accounts

Read M4 §4.31 and the [data and code](../../03_Data_and_Code/Heterogeneity_and_Consumer_Protection/README.md). Run both commands:

```sh
python3 03_Data_and_Code/Heterogeneity_and_Consumer_Protection/heterogeneity_reanalysis.py
python3 03_Data_and_Code/Heterogeneity_and_Consumer_Protection/test_reanalysis.py
```

14. Reconcile the 5,555 observations and 88 accounts with the upstream documentation. Explain why the 77-account preprint prevents a claim to reproduce its tables from this file alone.
15. Compare likelihood and BIC for one and two mixing components. Explain why more in-sample fit leaves the simpler model preferred by BIC.
16. Derive the normal convolution. Verify that shifting each latent mean by minus the imposed restriction leaves every account likelihood unchanged. State which institutional record could distinguish the mechanisms.
17. Give the missing premise in each move from a possible taste explanation, to no harmful restriction, to permission to continue. Defend a proportionate response using the strongest reasons of affected people.

## Greater Precision and Fewer Detected Harms

Read M6 §6.46 and M9 §9.57.5, then run:

```sh
python3 03_Data_and_Code/Heterogeneity_and_Consumer_Protection/harm_elasticity.py
```

18. Explain how average MSE can fall by 71.43% while harmed-group MSE more than doubles. State the population weights before making either claim.
19. Derive the raw-signal threshold under the one-sided posterior rule. Reproduce detection of 63.88% versus 14.07% and the accompanying actual false-flag rates. Explain why nominal 95% posterior credibility does not hold frequentist size fixed.
20. Verify the precision elasticity 0.3999 at the pooled endpoint. State the consumer population, monthly burden, and horizon. Explain why calling this a bias-reduction elasticity would be incorrect.
21. Explain the matched-calibration result. Identify what is preserved in the data and what changes in the rule governing protection.
22. Compare the proposed interpretation with the HBS overstatement. Identify the shared inference from no detected effect to reassurance, and the different statistical designs. State the evidence needed before claiming that shrinkage explains the actual data-center estimates.
23. Assess a rule that accepts smaller average estimation error as sufficient reason to withhold protection. Compare the harmed group's objection with the costs of false flags and a reversible safeguard. Cite (Scanlon, 1998, pp. 195–196) and distinguish the source principle from its application.
