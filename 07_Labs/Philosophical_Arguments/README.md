# Philosophical Arguments and Stakeholder Reasons

This is optional, ungraded practice. It establishes no assignment, deadline, grade weight, or course-wide AI rule.

Use [M9 §§9.27–9.32 and 9.40](../../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md), the [Scanlon and stakeholder reading guide](../../01_Resources/15_Marketing_Dialectics/07_Stakeholders_and_Reasons/README.md), and the [logic reading guide](../../01_Resources/15_Marketing_Dialectics/08_Logic_and_Analytical_Arguments/README.md). M1 §1.20 introduces a five-step argument exercise; M4 §4.29 and M6 §6.38 supply complete numerical examples.

## Construct an Argument

Choose one specific decision: a cancellation step, mHealth targeting, a pricing rule, an electricity cost allocation, or publication of a research claim. Write an initial conclusion using “ought,” naming the actor, action, and circumstances.

1. State the factual premises and the evidence needed for each. Identify observations, causal estimates, assumptions, and unresolved exposure separately.
2. State the normative principle that connects those facts to the recommendation. Explain why the principle is justified.
3. Identify affected positions beyond the firm, including people absent from the dataset. Describe a concrete interest and burden for each; do not invent testimony.
4. Compare at least one feasible alternative under the same circumstances. Preserve legitimate security, service, and operating needs.
5. Give the strongest reason for rejecting each principle. Assess the reasons from the affected person's position, including how the burden arises and the costs of alternatives.
6. Answer the strongest objection and revise the conclusion where needed. Specify what new fact or better reason would change it.

“The firm can,” “the firm profits,” “customers comply,” and “the public agrees” each leave a further premise to defend. A reasoned conclusion can permit an action, require it, prohibit it, or recommend gathering evidence before acting.

## A Worked Argument

**Hypothetical circumstances:** a subscriber has made a verified cancellation request. A prompt, secure exit is feasible at a reasonable cost. The proposed retention conversation delays exit and permits further charges.

**Proposed principle:** a provider ought to respect a valid withdrawal and justify any remaining burden through the legitimate interests it protects.

**Grounds:** the subscriber has a reason to control unwanted recurring obligations. Other subscribers need account security, and workers need a service that can operate sustainably. The feasible alternative protects those interests through proportionate verification while making retention offers optional.

**Conclusion:** under these circumstances, the provider ought to complete cancellation promptly.

**Objection and reply:** fraud or an irreversible service interruption may justify verification and clear warnings. Establish the risk and the effectiveness of the safeguard. The existence of that risk does not by itself justify compulsory persuasion. If a prompt exit cannot meet necessary protections at a reasonable cost, revise the proposed alternative and assess the remaining burdens.

The normative premise is a proposed course application of Scanlon's approach. Its justification remains open to challenge. It is not a legal determination.

## Recurring Cases

| Course Connection | Philosophical Question | Evidence and Alternative |
| --- | --- | --- |
| M1, AI-assisted coding | What ought an analyst verify before a manager relies on generated output? | Identify affected decisions, independent checks, review costs, and a feasible restriction on use. |
| M2, measurement | Who disappears when the analysis includes only observed customers? | Assess excluded users, zero records, missingness, and the population required by the claim. |
| M3, interpretation | What justifies converting an association into a recommendation? | State the causal and normative premises separately. |
| M4, targeting and pricing | When ought a profitable customer rule be rejected or constrained? | Compare customer burdens, access, legitimate operating needs, and less burdensome rules. |
| M5, text and classification | What authority permits an inferred label to change treatment? | Compare label validity, consequences of errors, review, and opportunities to contest a decision. |
| M6, experiments | What ought be communicated after an inconclusive result? | Retain uncertainty, meaningful effect sizes, and outcomes for affected positions. |
| M7, prediction | When ought a system ask before acting on a predicted preference? | Distinguish prediction, the user's purpose, and the scope of delegation. |
| M8, public communication | Does a favorable description supply a justified reason for acceptance? | Compare complete offers or claims, actual implementation, and material omissions. |
| M9, stakeholder duties | Why does each affected person's claim deserve consideration? | Distinguish influence, cooperative obligations, general duties, and public authority. |

## Publication and the Electricity Case

Use the [statistical examples](../../03_Data_and_Code/Statistical_Inference/README.md) and [institutional assessment](../../01_Resources/41_Statistical_Claims_and_Decisions/INSTITUTIONAL_ASSESSMENT.md). Cite the exact table or public statement being criticized. Keep actual results separate from the synthetic counterexamples.

Compare a delayed release, a corrected release, and rejection of the proposed version. Assess households' reasons to reject unsupported reassurance alongside readers' reasons to retain credible evidence and opportunities for criticism. Explain why the chosen remedy fits the demonstrated defect. For an already public claim, consider visible correction and traceability.

## Assess the Quality of the Reasoning

An effective argument defines its terms, supports its factual premises, defends its normative premise, and states a conclusion that follows under those conditions. It considers people beyond customers and shareholders when the proposed action affects them. It gives a serious objection a fair answer and identifies a meaningful condition for revision.

Reasonable rejection requires an assessment of reasons. It is neither a stakeholder vote nor a test of which group can impose the greatest cost on the firm. Disagreement with the instructor's recommendation is compatible with a strong argument when the premises and reasoning withstand scrutiny.

If an applicable course rule permits an AI assistant, ask it to identify an unstated premise or strengthen an opposing argument. Check the reconstruction against the actual case and verify any citations. A generated stakeholder persona supplies a hypothetical perspective, not evidence of an actual person's views.

## Test an Analytical Argument in Five Steps

Choose a precise claim from a paper, an AI-generated report, or a proposed marketing action. Retain the source passage and any qualification beside it. Use the following sequence before deciding whether to endorse or reject the claim.

1. **Define the claim.** Name the actor, action, population, comparison, period, and meaning of consequential terms.
2. **Expose the premises.** Classify each as factual, measurement, causal, or normative. Identify whether it is observed, estimated, assumed, or argued.
3. **Construct a counterexample.** Preserve every premise under examination while making the conclusion false. State whether the case is hypothetical or supported by actual evidence.
4. **Assess the missing premise.** Explain what rules out the counterexample and why that additional restriction or principle deserves acceptance.
5. **Revise the conclusion.** State what follows and identify evidence or reasons that would strengthen, weaken, or reverse it.

Use [ARGUMENT_RECORD.md](ARGUMENT_RECORD.md) to record the argument. A counterexample to a universal inference need not be common. Establishing that it describes the actual setting requires empirical support. The five-step sequence also applies to your own criticism.

## Equal Fit and Different Policy Effects

Run the two original programs and their checks from the repository root:

```sh
python3 03_Data_and_Code/Analytical_Arguments/price_models.py
python3 03_Data_and_Code/Analytical_Arguments/valuation_sensitivity.py
python3 -m unittest discover -s 03_Data_and_Code/Analytical_Arguments -p 'test_*.py'
```

The [input and output dictionary](../../03_Data_and_Code/Analytical_Arguments/README.md) specifies the imposed populations, probabilities, values, and units. M6 §6.38 prints the complete first program; M4 §4.29 prints the second.

For the price example, verify agreement on all four historical joint cells, including group labels. Explain why observing both prices somewhere in the population does not supply both prices within each group. Compare the predicted response to assigning a common price to everyone. Specify a randomized comparison that would distinguish the two models and discuss customer burdens in that experiment. Exact fit establishes compatibility; the intervention requires further evidence or a restriction on responses outside historical support.

For the valuation example, retain the purchase probabilities and strict rank order. Identify where the largest value gap lies in each scenario and use the cumulative probability changes to explain the opposite welfare signs. Then add the same incremental procedure cost to both scenarios. State which conclusion changes and why. Explain what evidence could justify a cardinal valuation and which questions about consent and reasonable treatment remain separate.

## Repair the Electricity Argument

Assess the exact claim in the [public-communication record](../../01_Resources/41_Statistical_Claims_and_Decisions/PUBLIC_COMMUNICATION_AND_PUBLICATION.md), retaining the paper's actual outcome, sample, qualifications, and positive findings. Reconstruct the proposed movement from nonrejection to harmlessness.

- Identify the effect sizes the study could detect under the specified power calculation. Preserve Donald W. K. Andrews's distinction between detectable departures and an interpretation of the realized effect.
- Explain the additional institutional evidence needed to map the measured unit price to household bills and cost exposure.
- Use the existing [synthetic counterexamples](../../03_Data_and_Code/Statistical_Inference/logical_counterexamples.py) and [institutional assessment](../../01_Resources/41_Statistical_Claims_and_Decisions/INSTITUTIONAL_ASSESSMENT.md) to identify a missing premise.
- Give the strongest supported response to the criticism. A design estimating average prices can still provide useful evidence within that scope.
- State a revised public claim and the further evidence needed for reassurance. Assess separately the reasons for communicating it to affected households.

Also assess the counterclaim that the study proves harm or that low power uniquely explains its nonsignificance. Identify why that inference needs further evidence. A hypothetical project pipeline establishes a possible exposure mechanism; documenting actual exposure in the study sample is a different task.

## Questions, Meaning, and an Ought Conclusion

Rewrite a pricing brief into four questions: who will accept, what the intervention changes, who bears a burden, and what the firm ought to do. List the evidence or reasons needed for each. Compare the roles of “can,” “may,” and “ought,” identifying feasibility, ability, permission, and obligation separately.

Apply the same exercise to an mHealth recommendation. Continued logging supplies evidence about recorded engagement; interpreting it as improved nutrition or authorization for targeting adds premises. Identify the relevant health outcome, the person's stated purpose, and the scope of any delegation before making a recommendation. No new analysis of personal records is required for this conceptual exercise.

If an applicable rule permits AI assistance, use the prompt in M1 §1.20.4 to obtain a counterexample and a strong reply. Verify the source passage, arithmetic, and preservation of premises yourself. Keep the assistant's hypothetical claims separate from evidence about real people. Evaluate both the commercial objective and the reasons supporting the proposed rule under the Scanlonian argument developed above.

## Phenomena, Noumena, and the Worth of the Objective

Use M9 §9.41 to assess a proposed objective before optimizing it. Begin with a pricing rule, an mHealth engagement target, or a public reassurance claim.

1. Identify what the available data represent and the conditions under which the representation is informative.
2. Identify important empirical facts that remain unmeasured and propose evidence for investigating them. Include qualitative evidence where appropriate.
3. Explain the negative sense of Kant's noumenon and why an unmeasured empirical variable does not meet that definition. Explain the limit this places on treating the model as a complete account of the person.
4. State the practical principle supporting respect, authority, or an obligation. Defend it through Kantian or Scanlonian reasoning, preserving the distinction between their arguments.
5. Assess whether the proposed end deserves pursuit. Compare a feasible alternative and allow the conclusion that the objective ought to be abandoned even if the algorithm achieves it accurately.

Give the strongest reply to your judgment and identify a reason or fact that could change it. Greater predictive accuracy, an additional latent variable, or a wider confidence interval does not by itself answer a question about which ends are worthy. An appeal to noumena supplies no evidence that a particular hidden preference or harm actually exists.

Classify a supported finding, a recognized evidence gap, an unanticipated empirical issue, and an acknowledged limit of knowledge. For the last, state the kind of knowledge, the reason for the limit, and whether changing the design could remove it. Compare the price example's conditional non-identification with Kant's restriction on human theoretical cognition. Explain why the need for practical justification remains after that comparison. Use the phrase “known to be the never known” with its scope and argument, as in M9 §9.41.5.

## Ontological Scope and Critiques of Empiricism

Use M9 §§9.42–9.43 and the spectrum to assess one electricity, personalized-pricing, or cancellation interpretation. Record a source passage and its actual claim. Identify the measured object, the broader object invoked by the conclusion, and the additional premise connecting them. Place that inference on the spectrum and justify the placement; do not assign an author or institution an overall score.

Develop one criticism using Kant, Sellars, Bhaskar, Husserl, or Scanlon. State the philosophical argument and explain its specific application. Preserve the difference between empirically investigable mechanisms, the meaning of an action, normative reasons, and Kant's limit of theoretical cognition. Answer the strongest reply, retain supported welfare findings and safeguards, and write a revised conclusion.

For the publication-incentive question, distinguish selection by statistical result from selection by method or question. Propose a sampling frame that includes unpublished or unsubmitted work and identify the comparisons needed. Treat the preference for computational tractability as a hypothesis until that comparison supplies evidence.

For the electricity case, complete the measurement table in M9 §9.42.4. State the claimed construct, recorded variable, unit, denominator, population, and timing. Give a validation argument or a counterexample that preserves the observation while changing the claimed object. Use the existing bill program in M6 §6.35 for the accounting comparison, then state separately what would identify a causal change.
