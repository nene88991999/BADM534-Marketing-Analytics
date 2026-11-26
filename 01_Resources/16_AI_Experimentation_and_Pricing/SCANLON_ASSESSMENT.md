# Pricing, Individual Reasons, and the Scope of Demand Models

## Empirical Claims and Normative Premises

A seller's ability to predict willingness to pay does not establish its authority to exploit the circumstances producing that willingness. The course compares the empirical representation, customer incidence, feasible alternatives, and reasons for adopting a pricing principle. The assessment concerns arguments and methods. Evidence of personal intentions, misconduct, exploitation of vulnerable individuals, or unlawful coordination would require additional facts.

| Work | Verified Setting and Contribution | Question for Assessment |
|---|---|---|
| Dubé and Misra, *Personalized Pricing and Consumer Welfare*, JPE 131(1), 2023 | Recruitment-service customers are employers; rich observed features predict demand parameters; empirical residual is logistic. June 2021 revision reports lower total customer surplus and a majority receiving lower prices. | Which circumstances, affected people, welfare assumptions, and alternatives determine whether the pricing rule is justifiable? |
| Angelopoulos, Lee, and Misra, *Causal Alignment*, August 2026 | Email subject lines, campaign click outcomes, human selection, and acceptability screening. | What customer outcomes and permissions remain outside click-based learning? This is not a field test of personalized prices. |
| Farrell, Korganbekova, and Misra, *Robust A/B Decisions*, 2609.07633v1 | Decisions under distributional ambiguity for a selected payoff. | Robustness to distribution change leaves the choice and justification of the payoff open. |
| Zhang and Misra, *Coarse Personalization*, 2204.05793v4 | A small number of segments can retain much of modeled personalization profit. | A short price menu does not itself establish morally appropriate classifications or customer control. |
| Dubé, Fang, Fong, and Luo, *Competitive Price Targeting with Smartphone Coupons*, Marketing Science 36(6), 2017 | Randomized mobile promotions; historical visits and location; estimated static competitive pricing game. | Permission to use location history, inference from visits, competitive responses, and reasons beyond firm revenue. |

The detailed discussion and complete code are in [M9 §§9.34–9.39](../../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md). [M6 §6.37](../../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md) separates correct experimental estimation from a justified allocation of exposure. [Optional practice](../../07_Labs/Scanlon_Pricing/README.md) requires an objection, the strongest defense, and an explicit condition for revising the conclusion.

## Heterogeneity and Harm

M9 §§9.34.3–9.34.4 distinguish measurement quality, the worth of an objective, and the reasonableness of a governing principle. Unbiasedness and precision support reliance on factual estimates. Justifying an action also requires reasons concerning the people affected, their authority, burdens, and alternatives. A seller's profitable choice and a dependent customer's acceptance may each be instrumentally rational while the governing rule faces a strong reasonable objection. This is an application of Scanlon's distinction in chapter 5, §2; it does not reduce rationality in every sense to self-interest or treat every objection as decisive.

The strongest supported criticism is that a fitted representation can omit morally relevant mechanisms and that finite experimental support can leave welfare conclusions dependent on structure. Flexible heterogeneity does not generally imply downward-biased estimates of harm. The pricing paper itself finds a decline in total customer surplus. Its rich observed interactions also differ from learning all unobserved preferences: the residual remains uncertain to the firm.

The original course example uses two monotone demand completions with identical purchase probabilities at every tested price. Their candidate policies produce the same revenue increase but opposite aggregate surplus changes. The higher-price group loses in both. This is an identification counterexample, not evidence that either completion describes the original experiment. Under quasilinear utility, surplus differences are integrals between prices; arbitrary utility rescaling is not a valid critique of correctly computed money-metric compensating variation.

Welfare weights require separate interpretation. Lower modeled surplus does not establish lower income or weaker social advantage, and an enterprise's surplus is not a complete account of the people affected. The authors' inequality-sensitive welfare comparisons, fairness discussion, and recognition of limits are material responses to criticism. They still do not establish authorization, the absence of exploitation, or reasonable acceptability of the governing principle.

## Reading Locations

- [Dubé and Misra](https://www.nber.org/papers/w23775): June 2021 NBER revision, §§2.2–2.3, §§3–4, empirical model, validation experiment, welfare and conclusion. Local PDF pages 9–16, 25–28, 37–40 provide the model and central discussion; use printed headings because pagination differs from the [2023 publication](https://doi.org/10.1086/720793).
- [Dubé, Fang, Fong, and Luo](https://www.fox.temple.edu/sites/fox/files/competitive-price-targeting-pub.pdf): published pp. 949–951 for sampling and measurement, pp. 963–966 for the equilibrium and Table 9. Table 9 was checked against the rendered page, then transcribed into an original JSON input.
- [Scanlon, *What We Owe to Each Other*, chapter 5 §§1–3](https://e-edu.nbu.bg/pluginfile.php/314831/mod_resource/content/0/scanlon_5.1-3.pdf): reasons, reasonable rejection, and feasible principles. The water-owner example is on p. 192. Weak bargaining power does not determine the strength of a moral claim.
- [Scanlon, John Locke Lecture 2](https://media.philosophy.ox.ac.uk/assets/pdf_file/0008/25856/Lecture_2.pdf): pp. 12–14 for the normative relation. The course distinguishes this metaethical account from its own assessment of analytical representation.
- [Scanlon, Lecture 4](https://media.philosophy.ox.ac.uk/assets/pdf_file/0010/25858/Lecture_4.pdf): reflective equilibrium and justification. A defensible principle is tested against cases and objections.
- [Kant, *Groundwork*](https://www.earlymoderntexts.com/assets/pdfs/kant1785.pdf): second section, Academy 4:421–430 for universalization and humanity. The linked Bennett text is a modernized rendering; Academy references identify the original passages. The course's hypothetical concealed-tracking maxim is an application, not an allegation about the experiment.
- [Suikkanen (2019)](https://doi.org/10.1007/s10892-019-09282-6), *Journal of Ethics* 23, 77–98: §§1–5 distinguish ex ante and ex post objections and propose a synthesis. The course does not treat expected harm, maximin, or majority voting as a complete Scanlonian decision rule.

## Replication Access

The [JPE supplement](https://www.journals.uchicago.edu/doi/suppl/10.1086/720793/suppl_file/20190715data.zip) is publicly linked by the journal, but its download returned HTTP 403 on November 26, 2026. Its contents have not been verified.

The [Marketing Science supplement](https://pubsonline.informs.org/doi/suppl/10.1287/mksc.2017.1042) links to an [INFORMS download form](https://services.informs.org/dataset/mksc/download.php?doi=mksc.2017.1042). The form states that files may be used to verify the paper's main results using the same data and models, restricts other reuse without permission, and specifies Marketing Science as the venue for a follow-up article documenting corrected central results. Download requires an email and acceptance of those terms. The course uses the executed published-table reconstruction. At the instructor's request, the form was not submitted and replication microdata were not downloaded.

The public repository contains original course programs, synthetic inputs, a transcribed aggregate payoff table, and source links. Local full-text references remain in Dropbox. A successful table reconstruction does not establish successful estimation from replication microdata.
