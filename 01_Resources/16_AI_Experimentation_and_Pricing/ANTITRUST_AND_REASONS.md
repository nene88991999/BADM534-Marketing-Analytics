# Antitrust Evidence and Reasons Owed to Customers

U.S. federal framework, checked November 26, 2026. The course application is hypothetical. Research methods and model predictions are not findings of unlawful conduct by the researchers or firms using their work.

## Match the Conduct to the Claim

| Issue | Legal Source and Scope | Evidence to Seek | Scanlonian Connection |
|---|---|---|---|
| Concerted restraint | [15 U.S.C. §1](https://www.law.cornell.edu/uscode/text/15/1); [*Twombly*, 550 U.S. 544, 553–557 (2007)](https://www.law.cornell.edu/supct/html/05-1126.ZO.html) | Agreements, confidential input sharing, communications, recommendation commitments, independent overrides | People have reasons to object to coordinated removal of independent alternatives. Mere parallel behavior leaves agreement unresolved. |
| Monopolization | [*Trinko*, 540 U.S. 398, 407 (2004)](https://www.law.cornell.edu/supremecourt/text/02-682) | Monopoly power and a specified exclusionary mechanism | Unilateral exploitation can remain morally objectionable even where monopoly pricing alone is legally insufficient. |
| Price discrimination | [FTC Robinson–Patman guidance](https://www.ftc.gov/advice-guidance/competition-guidance/guide-antitrust-laws/price-discrimination-robinson-patman-violations) | Covered commodity sales, competitive injury, timing, cost justification and meeting-competition defenses | Equal prices and fair treatment are distinct questions; categorical statutory coverage does not exhaust a person's reasons. Recruitment services and admissions are not ordinary covered commodity sales. |
| Attributable injury | [*Brunswick*, 429 U.S. 477, 489 (1977)](https://www.law.cornell.edu/supremecourt/text/429/477) | Harm flowing from the anticompetitive aspect of the conduct | A justified remedy responds to an attributable burden while protecting against sanctions for unrelated losses. |
| Damages and class proof | [*Comcast*, 569 U.S. 27, 35–38 (2013)](https://www.law.cornell.edu/supremecourt/text/11-864) | A counterfactual and damages model matched to the accepted liability theory; heterogeneity and common proof | Accountability requires evidence of who is harmed; an aggregate change cannot answer every person's claim. |

These connections are philosophical interpretations of institutional reasons. Courts do not apply Scanlon's contractualism as the governing antitrust test. Moral standing also extends to people who may lack a particular damages claim.

## Legal Literature

[Ezrachi and Stucke, “Artificial Intelligence & Collusion: When Computers Inhibit Competition,” 2017 University of Illinois Law Review 1775–1810](https://illinoislawreview.org/print/vol-2017-no-5/artificial-intelligence-collusion/) distinguishes a computer implementing an agreement, hub-and-spoke arrangements, predictable agents, and autonomous learning. Sections III–IV explain why the factual mechanism and legal response differ. The taxonomy motivates competing hypotheses; its discussion of enforcement gaps is not a rule that algorithmic price similarity establishes an agreement.

## RealPage: Allegations, Proposed Terms, and an Entered Judgment

The [DOJ case record](https://www.justice.gov/atr/case/us-and-plaintiff-states-v-realpage-inc) lists the November 24, 2025 [RealPage Competitive Impact Statement](https://www.justice.gov/atr/media/1419471/dl?inline=) and [proposed final judgment](https://www.justice.gov/atr/media/1419451/dl?inline=). The former describes allegations about competitors' nonpublic data and pricing alignment, and proposed remedies addressing inputs, training, software features, and monitoring. These documents are proposals and government allegations, not a trial finding. The same case page separately lists the [Greystar final judgment entered March 2, 2026](https://www.justice.gov/atr/media/1430091/dl?inline=). The recorded status is document-specific; the proposed RealPage terms are not described as a generally binding rule for other firms.

## Evidence and Counterfactuals

Use the pricing research to define customer segments, price support, substitution, rival responses, and welfare incidence. Then identify the conduct absent from the lawful counterfactual. A model trained on post-conduct customer states may preserve reduced alternatives in that counterfactual. A change in model fit does not resolve that causal issue. Demand experiments can inform price sensitivity while still leaving the effect of the alleged coordination unidentified.

The [worked Python example](../../03_Data_and_Code/AI_Experimentation_and_Pricing/compare_pricing_damages.py) assumes 92 actual units at $120 and a lawful price of $100 with 100 counterfactual units. It produces $1,840 in signed invoice differences and $1,040 in revenue growth. The eight excluded purchases require separate welfare evidence. The assumed benchmark is varied to show the sensitivity of the damages calculation. No actual firm, plaintiff class, violation, or empirically estimated damages is represented.

## A Defensible Ought Conclusion

Specify the affected person's burden, the institutional mechanism producing it, a feasible alternative, and the strongest objection to that alternative. A firm may reasonably invoke viability and useful forecasting. Those interests do not automatically justify a feature that suppresses independent discounts. If useful forecasting remains available without the restrictive feature, necessity is an empirical claim to test. Protecting customers against unjustified extraction and protecting defendants against unsupported attribution both matter to the justification of an enforcement institution.

See [M9 §§9.38–9.39](../../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md) for the detailed argument and complete code. This federal antitrust comparison does not determine separate consumer-protection, privacy, civil-rights, state-law, or non-U.S. claims.
