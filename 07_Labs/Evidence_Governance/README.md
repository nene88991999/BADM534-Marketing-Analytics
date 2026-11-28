# Evidence, Authority, and Correction

Optional, ungraded practice. Allow 25–35 minutes for discussion or use the Python extension independently. No paid model access is required.

A communications manager wants to publish an assurance that data centers cause no household harm. The numerical evidence is a reported utility-price regression. The manager's approval and the eight proposed records in this exercise are fictional. The decision is whether to publish, revise, or withhold the assurance while further evidence is collected.

## Evidence and Claim Assessment

Read M1 §1.25, M7 §7.49, and M9 §9.85. Open the [example guide](../../03_Data_and_Code/Evidence_Governance/README.md), [claim table](../../03_Data_and_Code/Evidence_Governance/results/claim_assessments.csv), and [reported input](../../03_Data_and_Code/Statistical_Inference/results/data_center_estimates.csv).

1. Identify the observation unit, outcome, source table, exposure scaling, and approximation. Explain why utility-average residential price and a household's total bill answer different questions.
2. Before consulting the checker results, judge each complete claim and identify the evidence supporting or contradicting it. A source must resolve, and the statement must retain the source's outcome and uncertainty.
3. Compare the two checkers. Explain why correct metadata can accompany a false sentence. Separate a numerical mistake, an unresolved reference, an outcome substitution, and an unsupported interpretation of nonrejection.
4. Write a defensible public statement containing the estimated change, units, interval, and scope. Identify the additional information needed to assess household bills. Explain why a human signature does not supply that information.

## Sources, Coding, and Institutional Context

Choose one of the boxed utility-call excerpts in M5 §5.27. Record its issuer, date, speaker, source location, and exact passage. Write a separate coding decision about the financing mechanism and a separate substantive conclusion. Identify a contextual passage that could narrow the conclusion, such as a customer-specific tariff, regulatory approval condition, or statement about timing. The 2026 disclosures can motivate mechanism-based inquiry into costs; they do not establish the realized 2020–2025 treatment effect in the earlier panel.

## A Reasonable Objection and a Revision

State a principle permitting publication on the basis of internal approval and a feasible alternative requiring source-supported wording and a visible correction route. Identify an affected household's strongest objection to each principle and the institution's strongest reply. Compare the burdens on persons, including the need for timely information and the cost of unsupported reassurance. State what evidence would change the judgment.

Formulate a maxim with a circumstance, an action, and an end. Explain whether the proposed communication preserves the reader's ability to assess the reasons offered. A principle can be unreasonable even when it is profitable; a valid statistical calculation leaves this moral question open.

## Python Extension

Run the commands in the example guide. Preserve the eight baseline cases. Add a ninth record whose `quantity`, `value`, `target`, and sources are correct but whose prose silently changes the period or population. Predict the result of each checker before running it. Add a targeted check if the new distinction can be represented explicitly, and describe the judgments that remain outside that check.

Inspect the two fictional decisions in `results/decision_history.json`. Explain why a correction should identify the superseded decision and its reason. Demonstrate that exclusive creation prevents an overwrite through this function, then explain which deployment permissions would be needed to enforce preservation across all writers. Submit nothing unless a separate released assignment requests it.
