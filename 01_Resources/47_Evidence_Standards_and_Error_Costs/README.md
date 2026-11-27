# Evidentiary Standards, Consumer Harm, and Error Costs

A regulator must decide whether to investigate a pricing practice, require disclosure, impose temporary safeguards, or seek a legal remedy. The available evidence may suggest harm without identifying its exact causal magnitude. Requiring certainty before every action allocates the consequences of uncertainty to customers who remain exposed. That allocation is a substantive policy choice. Its justification depends on the seriousness of the suspected harm, the reliability of the evidence, the effects of the proposed action, and the people who bear each consequence.

## Rigor as an Institutional Standard

Conceptual engineering examines how conceptual resources organize inquiry and action, and how those resources should change. A concept can direct attention toward some features of a situation and authorize particular responses (Haslanger, 2022, pp. 1–4). Applied to analytics, this perspective asks what an institution allows the word *harm* to include, what it counts as *evidence*, and which responses it considers *rigorous*. The application to enforcement standards is an argument developed here, rather than a claim made in that philosophical source.

Suppose an institution recognizes harm only when an investigator produces a precisely identified average price effect. That rule excludes burdens arising through access, dependence, coercion, and the distribution of prices unless they can satisfy the same empirical requirement. If unresolved evidence then requires nonintervention, the rule also determines who bears uncertainty. A harmful firm can benefit from that arrangement even when each individual estimation procedure is implemented correctly. Establishing that a particular firm acted unlawfully requires evidence about its conduct and the applicable law. Establishing deliberate manipulation of the evidentiary rule requires additional institutional evidence.

The criticism becomes especially strong when the rule applies asymmetrically. A firm can introduce a practice on the basis of forecasts and expected profit, while those exposed to the practice must establish its harmful effects with substantially stronger evidence before receiving protection. Whether this asymmetry is justified depends on the consequences on both sides. Treating continuation of the practice as costless removes the consumers' losses from the decision before any calculation begins.

Inductive risk concerns the consequences of accepting or rejecting an uncertain claim. Where errors have important social consequences, judgments about their acceptability enter choices of methods, characterization of observations, and interpretation (Douglas, 2000). Values can guide the scrutiny required and the action taken. They do not supply missing observations or turn a desired conclusion into a finding.

## Type I and Type II Errors

Fix the null hypothesis as the absence of the specified harmful practice. A Type I error falsely flags harm when that null is true. A Type II error misses harm under a specified harmful alternative. Power is one minus the Type II error probability at that alternative. Reversing the null changes the labels, so the affected state and decision must accompany them.

For a simplified binary decision, expected loss across a specified population of cases is

$$R=(1-\pi)\alpha C_{FP}+\pi\beta C_{FN}.$$

Here, $\pi$ is the share of harmful cases in the population, $\alpha$ is the false-positive probability among harmless cases, $\beta$ is the false-negative probability among harmful cases, and $C_{FP}$ and $C_{FN}$ are the respective losses per error in common units. Correct decisions have zero loss in this illustration. A composite alternative requires averaging over harmful states or evaluating them separately. The equation is a decision model, not a legal burden of proof.

A small false-positive rate can coexist with large expected loss when missed harms are frequent, persistent, or severe. Conversely, an intervention with severe and irreversible consequences can make false positives especially costly. A conventional significance level fixes one error probability without specifying these consequences. An unbiased estimator likewise supplies no complete ranking of decisions: its variance, the policy response, and the losses from that response still matter.

The [complete Python example](../../03_Data_and_Code/Evidence_Standards/README.md) uses a synthetic signal with known distributions. It keeps those distributions fixed, compares one-percent and five-percent tests, and calculates the threshold minimizing expected loss under two opposing cost specifications. The output also separates an assumed posterior probability of harm from a p-value. The comparison measures the consequences of explicit decision rules; it supplies no estimate of misconduct in an actual market.

## The Antitrust Dispute About Error Costs

One influential defense of limited antitrust intervention argues that mistaken condemnation can persist through precedent, whereas market entry can correct some tolerated monopoly power (Easterbrook, 1984, pp. 2–4). The opposing critique examines assumptions about self-correction, entry, innovation, courts, and litigation that overstate false positives and understate false negatives (Baker, 2015, pp. 1–5). The disagreement concerns the economic and institutional content assigned to error costs. Decision theory itself does not require a presumption favoring firms.

The appropriate comparison must also identify the action. Opening an investigation, requiring relevant records, imposing a reversible safeguard, and awarding damages create different costs and evidentiary obligations. Legal burdens affect deterrence, beneficial conduct, and enforcement incentives as well as errors in an individual adjudication (Kaplow, 2012). A numerical loss threshold cannot simply replace the governing law.

Current United States merger guidance offers an example of evidence that extends beyond a precisely estimated price effect. It considers the totality of evidence, including documents, testimony, economic analysis, and structural presumptions; merger review addresses threats to competition in their incipiency ([DOJ and FTC, 2023, overview](https://www.justice.gov/atr/merger-guidelines/overview) and [§4.1](https://www.justice.gov/atr/merger-guidelines/tools/sources-of-evidence)). The guidelines describe agency practice and are not binding law. Their treatment of prospective mergers is distinct from the elements of a retrospective monopolization or damages claim. Positive markups, statutory price gouging, anticompetitive conduct, and moral wrong require different predicates. The [existing legal crosswalk](../16_AI_Experimentation_and_Pricing/ANTITRUST_AND_REASONS.md) states those distinctions.

## Heterogeneity, Model Fit, and Market Power

Integrating over heterogeneous tastes constructs aggregate demand from individual choice probabilities. A representative Bayesian aggregate-share model assumes a distribution of preferences and common demand shocks, then uses the likelihood and priors to characterize parameter uncertainty (Jiang et al., 2007, §§2–3; published 2009). The [implementation documentation](https://search.r-project.org/CRAN/refmans/bayesm/html/rbayesBLP.html) makes the assumed normal heterogeneity and the additional instrumental-variable structure explicit. This is a specified model with restrictions. It does not permit an arbitrary explanation of every possible pattern.

The substantive concern arises when estimated differences in willingness to pay acquire a further interpretation as justified differences in treatment. A consumer with little ability to switch may appear price insensitive. An estimate of that response leaves open whether the relevant mechanism is preference, dependence, restricted access, or an objectionable feature of the market. A flexible demand fit can hide this interpretive choice when the analysis treats the estimated preference distribution as the complete account of consumer interests.

The direction of a markup conclusion is model dependent. For a single-product firm choosing an interior profit-maximizing price, differentiable demand and constant marginal cost imply $(p-c)/p=1/|\varepsilon|$, where $p$ is price, $c$ is marginal cost, and $\varepsilon$ is the own-price elasticity at the optimum. Lower elasticity implies a larger implied markup under those conditions. Integration over heterogeneity therefore has no general tendency to produce lower markups. In multiproduct settings, substitution patterns and ownership enter the pricing conditions as well.

Four points require separate assessment:

1. **Identification:** Which variation distinguishes tastes, common demand shocks, price endogeneity, and competing conduct models? Nonparametric identification results can help discriminate among oligopoly models under stated restrictions (Berry and Haile, 2010; published 2014).
2. **Prior Sensitivity:** How much precision comes from observations and how much from restrictions or priors? In partially identified models, a Bayesian credible set can remain inside the identified set even in large samples. Report the identified set and the conditional prior alongside posterior conclusions (Moon and Schorfheide, 2012).
3. **Institutional Content:** What do the outside option, switching costs, available products, and cost records represent? Which mechanisms are absent from the model? Assess alternative specifications against institutional evidence, rather than allowing good fit to settle their interpretation.
4. **Decision Consequences:** How does each plausible specification change the action and its distribution of losses? Sensitivity analysis that relaxes an instrument's exclusion restriction provides a concrete way to reason with imperfect assumptions (Conley et al., 2012).

These distinctions support a demanding critique of how models are used. A blanket claim that Bayesian methods or identification necessarily prevent enforcement is inconsistent with the methods and their possible applications. The testable concern is whether a particular specification or institutional standard excludes relevant harm, obscures consequential uncertainty, or places unjustified burdens on the people seeking protection.

## An Argument for Protection Under Uncertainty

**Ontological premise.** A person's dependence, financial burden, or loss of authority can exist whether or not the analyst has a variable that adequately represents it. A missing measure does not remove the underlying interest. Empirically unobserved interests and Kantian noumena remain distinct concepts.

**Epistemic premise.** Credible institutional mechanisms, documents, testimony, and descriptive patterns can support concern while leaving causal magnitude unresolved. The strength of that concern depends on the source quality, alternative explanations, timing, and the actual exposure. A non-significant estimate does not establish harmlessness.

**Normative premise.** People have reasons to reject an institutional rule that exposes them to serious, avoidable burdens merely because others cannot meet a demanding identification requirement. The competing reasons include mistaken restriction, livelihood, useful innovation, procedural fairness, and the costs of collecting evidence. Contractualist assessment compares principles through the objections affected individuals could reasonably raise (Scanlon, 1998, chapter 5).

**Action conclusion.** When credible evidence indicates serious exposure and a feasible intervention has smaller, proportionate, and reversible costs, acting before precise causal identification can be justified. Relevant actions include obtaining records, limiting exposure temporarily, and requiring a review as evidence improves. An accusation or punitive remedy remains subject to its separate factual and legal requirements. A low-cost response to a credible threat requires a different justification from a severe sanction imposed on an uncertain attribution.

Expected-loss calculations make the distribution of error costs visible. A contractualist assessment also asks whether a particular person's serious burden is defensible; summing small benefits to others does not automatically answer that objection. The moral importance of a consequence cannot be inferred from how readily it fits into a common monetary unit.

## Household Electricity and Targeted Pricing

For household electricity, an average revenue-per-kWh result concerns a different object from a household's bill, consumption sacrifice, disconnection risk, or exposure to future infrastructure charges. The [existing institutional assessment](../44_Bad_Controls_and_Project_Exposure/CASE_ASSESSMENT.md) identifies mechanisms and records needed to evaluate phantom projects, investment timing, and comparison-group exposure. The [data assessment](../45_Data_Truth_and_Norms/ELECTRICITY_ASSESSMENT.md) documents what is collected and where access or linkage remains incomplete. These distinctions can justify further inquiry without establishing the causal effect of a particular project.

For targeted pricing, prediction of willingness to pay helps a firm select offers. It does not establish that each person's limited alternatives supply a reasonable justification for charging more. Evidence about dependency, suppressed alternatives, and targeting rules bears directly on that question. Consumers should not disappear from moral consideration because the analyst can estimate their demand more readily than their freedom to refuse.

## Sources and Reproduction

The [annotated readings](READINGS.md) and [catalog](catalog.json) record 16 sources, including contrary evidence, inspection scope, local copies, and publication versions. Eight new PDFs and two existing local readings support the collection. It links to the [historical collection](../46_Measurement_and_Disciplinary_History/README.md) and existing philosophy readings. Source PDFs in `readings/` remain local to Dropbox. Public course materials contain original explanations, links, and reproducible synthetic calculations. This collection makes no empirical finding of unlawful conduct by a named firm and no finding of intentional misconduct by a method's author.

## Teaching Integration

[The lecture notes](../../06_Lecture_Notes/README.md#measurement-traditions-and-evidence-for-protection) integrate the argument across M1–M9, with full Python in M6 §6.44 and extended philosophy in M9 §§9.55–9.59. [Selected session discussions](../../05_Slides/SESSION_PLAN.md#evidence-standards-and-unequal-error-costs), the syllabus, and [optional practice](../../07_Labs/Evidence_Standards/README.md) connect the readings to pricing, household electricity, and prediction thresholds.

## Released Data, Precision, and the Burden of Proof

The [retail reanalysis](../../03_Data_and_Code/Heterogeneity_and_Consumer_Protection/README.md) uses public data attributed to a hierarchical trade-promotion study (Boatwright et al., 1999). It preserves the difference between the package and preprint samples. Exact mixture integration changes fitted coefficients while leaving a constructed taste-versus-restriction decomposition unidentified. M4 §4.31 contains the complete program.

The separate synthetic comparison in M6 §6.46 shows narrower posterior intervals and lower average MSE alongside fewer detected harms under a fixed posterior-credibility rule. The group suffering the burden has greater MSE. Actual false-positive rates and a matched-calibration check identify the decision-rule tradeoff. The algebra of pooling supports the mechanism (Gelman et al., 2012, pp. 196–198); the consumer losses and precision elasticity are original constructions.

M9 §§9.57.1–9.57.6 connects the missing empirical and normative premises to criticism of the Given, the distinction between ontology and knowledge, modal discourse, and reasonable rejection. An inability to rule out every preference explanation can impose an unreasonable burden before proportionate protection. The later circulated discussion considers relevant personal reasons across affected parties and revises a strictly bilateral treatment of aggregation (Scanlon, 2025, pp. 41–43). The argument supplies no general theorem that more heterogeneity lowers detection or that prior precision establishes harmlessness.

Catalog records E17–E20 identify the public dataset and the newly inspected readings. Restricted source PDFs remain in Dropbox; the public repository contains annotations, links, licensed package data, and original teaching materials.

The [method crosswalk](../../03_Data_and_Code/Heterogeneity_and_Consumer_Protection/METHOD_CROSSWALK.md) establishes the exact conditional correspondence with the hierarchical regression (Rossi, 2025), while separating full posterior sampling from the fixed-hyperparameter calculation.
