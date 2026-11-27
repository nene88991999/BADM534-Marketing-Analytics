# Electricity-Price Claims and Their Evidentiary Support

## Demonstrated Problems in Interpretation

**Nonrejection used as reassurance.** Table 2, column 4 reports 0.261 (SE 0.158). At the paper's reference exposure, the estimate is $1.749/MWh, with approximate 95% interval [-0.326, 3.825] and one-sided 95% upper bound 3.491. Normal-test power at fixed reported precision is 15.7% for a $1 increase and 47.2% for a $2 increase. Those effects remain unresolved. Table 4's four-owner coefficient is a different estimand: 0.158 (SE 0.160) dollars/MWh per exposure percentage point. Its positive upper bound gives no support for categorical harmlessness. The paper is not uniformly insignificant and has positive findings in other specifications.

**A significance contrast exceeds its direct test.** Table 4 and p. 26 report a Wald p-value of 0.101 for equality across developer categories. The text calls the difference marginally significant, although 0.101 exceeds the displayed 10% convention. Separate stars against zero do not test equality. Preserve covariance when estimating a difference. The reported p-value is used directly; the course does not reconstruct an unavailable covariance matrix.

**A residual becomes a causal explanation.** Page 3 assigns 96% of observed residential price growth to inflation, fuel expenses, and modernization/resilience costs. Table A.4's 166.85 minus 123.59 equals $43.26/MWh. Dividing the reference estimate by this rise yields about 4.04%; subtracting it yields about 95.96%. This arithmetic does not estimate the contributions of the named causes. The denominator is observed historical growth, not a prespecified household-harm threshold.

**A weak sales test carries a mechanism conclusion.** Table 7, column 2 reports 291 (SE 493) quarterly MWh per added MW. Its approximate 95% interval is [-675, 1257]. A hypothetical full quarter at 50% utilization and no displacement adds 1095 MWh per MW and has only 60.3% power; at 25% utilization, power is 19.9%. The result leaves substantial consumption unresolved. Separate cost and sales regressions alone do not identify the share of price changes caused by infrastructure versus procurement.

**The cost ratio is described as a numerator.** Section 4.2, p. 16 defines utility cost per MWh and says it corresponds to the model's cost numerator. The model uses a total revenue requirement. A ratio changes with both total cost and sales, so a numerator interpretation requires an additional reconciliation. Table 6 uses 22 utilities and 377 observations; Table 7 uses 42 and 648. Cross-equation claims should also reconcile samples.

**Ownership is substituted for a business model.** Section 4.1 assigns four named firms to a cloud group and all remaining owners to a third-party group. Table A.2 includes Apple and xAI among the latter. Apple's own environmental report distinguishes its own data centers from its use of colocation. Owner identity alone cannot classify each facility's operating model, customers, utilization, procurement, or contracts. The valid operational label is four named owners versus other owners until those attributes are observed.

## Design Questions Requiring Replication

These concerns follow from the specified design. Their empirical size and sign have not been established here.

- Equation 21 uses post-anchor gaps with utility fixed effects. A utility with no subsequent addition has constant cumulative treatment after its anchor. Its stock is absorbed by its fixed effect. Report the identifying within-utility variation, leverage, weights, and support before generalizing the slope to all additions.
- Quarter-of-year fixed effects absorb recurring seasonality. Differential calendar shocks, endogenous activation timing, anticipatory investment, and delayed rate recovery require separate assessment.
- Donors without new centers may share wholesale-market or transmission exposure. Overlapping donor weights can induce dependence across treated gaps. Examine market-based donor exclusions and inference that re-estimates the full procedure.
- Appendix B reports pre-treatment fit and donor concentration. Report post/pre fit diagnostics, influence and leave-one-utility-out results, alternative donor sets, and placebo or resampling procedures suited to the design. A good fit before entry does not guarantee a valid counterfactual afterward.
- The model includes thresholds and endogenous cost allocation. A common linear stock effect needs support before extrapolation to larger future facilities or different regulatory arrangements.
- Table 5 investigates several outcomes, interactions, and specifications. Distinguish prespecified from exploratory hypotheses and account for the tested family. The number of comparisons alone does not establish selective reporting or p-hacking.

## Ontology and Agency

Average utility revenue, household expenditure, affordability, welfare, and agency are different objects. A narrow price study can answer a narrow price question. Treating its average as a complete representation of household harm omits incidence, income, reliability, timing, and feasible alternatives. Treating payment as endorsement omits reasons and authority. These are failures of scope and category when broad reassurance relies on them; the existence of a restricted estimand alone is not a philosophical refutation of the empirical work.

The synthetic incidence example preserves total revenue and use while changing which households pay. It establishes non-identification of distribution from the average. Access to explanations, review, correction, and remedy requires further institutional evidence. Kantian respect for persons and Confucian responsibilities of truthful service motivate scrutiny of how analytical authority is used. They do not provide a numerical harm tolerance or establish individual misconduct.

## Communication and Potential Harm

The HBS article provides an example of overstatement: its categorical developer claim exceeds the uncertain Table 4 estimates [(Kost, 2026)](https://www.library.hbs.edu/working-knowledge/blaming-data-centers-for-higher-electric-bills-its-not-that-simple). Its future-price qualification leaves the historical inference unresolved. Statistical insignificance alone supplies no substantive conclusion about harmlessness; the [communication exercise](../../07_Labs/Statistical_Inference/README.md#evaluate-public-reassurance-and-household-agency) requires an estimate, uncertainty, a justified harm threshold, and the missing premise. This is academic coverage. Company circulation on X has not been verified: public web searches did not produce a confirmed company post, and direct X search required a login on November 26, 2026. Absence of a verified post is an access and evidence limit, not proof that no such post exists.

Overstated reassurance could weaken scrutiny of cost allocation, guarantees, and review, leaving households exposed to risks that the study has not ruled out. Demonstrating that this paper caused an approval, a weakened safeguard, or a household loss requires additional evidence. A rigorous classroom criticism identifies the unsupported inference and its possible decision consequences without inventing intention, corporate dissemination, or observed harm.

See [M6 §6.33](../../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md) for complete calculations and [M9 §9.26](../../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md) for the philosophical argument.

## Logical Reconstruction and Power

The [argument record](ARGUMENT_ASSESSMENT.md) makes each missing premise explicit. M9 §9.27 distinguishes deductive validity, empirical support, and normative justification, with reproducible counterexamples. M6 §6.34 bases the power analysis on the inverse-power framework (Andrews, 1989). The course retains a fixed reported-covariance approximation and does not claim a full-design or uniform power calculation.

## Project Status and the Outcome Denominator

The [institutional assessment](INSTITUTIONAL_ASSESSMENT.md) identifies two additional unsupported extensions: zero operating additions imply zero project exposure, and an average unit-price result determines household expenditure. Both require additional evidence. The paper discusses realized payments and regulation; the criticism concerns the scope of the reported outcome and donor screen.
