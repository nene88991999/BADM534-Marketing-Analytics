# Data, Truth, and Reasons Owed to Households

This is optional ungraded practice. The decision concerns whether a household should accept a public reassurance about electricity development costs, and what evidence the institution communicating it ought to provide.

## Preparation

Read M2 §§2.30–2.31, M6 §6.43, and M9 §§9.51–9.54 in the [notes](../../06_Lecture_Notes/README.md). Use the [categorized readings](../../01_Resources/45_Data_Truth_and_Norms/README.md) and [electricity evidence assessment](../../01_Resources/45_Data_Truth_and_Norms/ELECTRICITY_ASSESSMENT.md). Run the [synthetic example](../../03_Data_and_Code/Data_Production/README.md) before interpreting its outputs.

## Measurement and Identification

1. Predict whether identical released billing records can coexist with opposite target effects. Reconcile your answer with both restricted releases and the full ledgers. State the target population and units.
2. Derive the broader-release mean in H by hand. Explain why positive inclusion permits weighting and why restricted release does not. Identify the special feature that makes recovery exact for every draw.
3. Replace the illustrative missing-effect bounds with [-10, 10], then [0, 50]. Calculate the population intervals using `effect_bounds`. State which constructed worlds each restriction excludes and what external evidence would justify that exclusion.
4. Relax the condition equating prior bills with current no-project bills. Explain why an observed change then combines a project effect with other changes even if disclosure is complete. Separate this identification problem from release selection.

## Philosophical Argument

5. Distinguish a dataset version, a physical file, a recorded charge, an actual payment, and a claim about household harm. Apply the artifact analogy (Thomasson, 1999, 2014) to the first two without treating the household as a fictional character.
6. Identify a semantic, epistemic, legal, and moral norm relevant to the case. Construct an example in which an accurate and lawfully accessed record supports a narrow statement but leaves a proposed action unjustified.
7. Reconstruct the proposed Scanlonian argument in §9.54. Identify the resident's reason, the institution's informational control, feasible safeguards, and the conclusion. Then give the strongest privacy or resource objection and revise the principle to address it.
8. Assess the proposition that controversy makes household costs permanently unavailable. Use the existing RECS collection, contract correspondence, and introduced disclosure bill. Distinguish a verified access restriction from a prediction of secrecy and an allegation of intentional suppression.

## An Evidential Proposal

Specify a project-linked study covering proposed, canceled, delayed, and operating facilities. State the household outcome, counterfactual, dates, financing links, sample restrictions, and required records. Design controlled access and public aggregates that permit criticism while protecting identities. Identify whose question each data holder's system was designed to answer and where additional collection or linkage is needed.

End with a supported public statement and a separate recommendation. Explain which evidence could reverse the factual judgment and which reason could change the recommendation. Do not infer a favorable or adverse causal effect merely from the availability of records.

## Evidence and the Proposed Action

Use [Evidence Standards and Reasonable Protection](../Evidence_Standards/README.md) to distinguish an inquiry, a temporary safeguard, and a remedy. Compare the consequences of false alarms and missed harm, defend the interests included in the analysis, and answer the strongest reasonable objection. The complete synthetic calculation appears in M6 §6.44; M9 §§9.55–9.59 connects the decision to disciplinary history and institutional standards.

## The Dataset as an Artifact

Read M2 §§2.33–2.34 and M9 §§9.60–9.62. Run `python3 03_Data_and_Code/Data_Production/data_artifacts.py` and inspect the [outputs](../../03_Data_and_Code/Data_Production/artifact_results/README.md).

1. Explain why two files with different hashes contain the same records under the stated identity rule. Give a transformation that would preserve a filename while changing the represented comparison.
2. Calculate retention, pending requests among requests, and pending requests among retained accounts by hand. Explain the information supplied by each denominator.
3. Construct a supported status claim and an unsupported claim about voluntary loyalty from V1. Identify the missing premise and how V2 changes the available criticism.
4. Apply creation, meaning, preservation, and evidential-use questions to a billing record, mHealth entry, or call transcript. Identify the represented event separately from its record.
5. Formulate a reasonable principle for correcting a contested classification. State who may challenge it, who has relevant evidence, and how privacy can be protected.

## Should Research Under an NDA Exist?

Read M9 §§9.63–9.65 and the [restricted-research guide](../../01_Resources/45_Data_Truth_and_Norms/05_Restricted_Research/README.md). Agreements A–C are hypothetical. They use the same synthetic account history and differ in the allocation of access and reporting authority.

Compare the three agreements on the questions researchers can ask, the findings they may disclose, preservation, and independent scrutiny. Distinguish a bounded confidentiality review from discretionary control over conclusions. For each agreement, decide separately whether researchers ought to conduct the study, publish it, and use it to justify a public decision.

Defend a principle for proceeding, renegotiating, or refusing. Give the strongest case for allowing confidential research and the strongest reasonable objection from a person affected by its use. Explain which term or circumstance would reverse your judgment. Assess the value of declining a prestigious publication when the agreement prevents adequate public justification.

Finally, assess a paper's actual access and funding statements. Record what the available documents establish, what remains unknown, and which further evidence would distinguish confidentiality from selective reporting. Do not assign a publication veto, suppression decision, or hidden result to a named study without evidence. Draft a public claim whose scope remains supported under the documented restrictions.
