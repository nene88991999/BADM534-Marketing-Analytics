# Bad Controls and Project Exposure

A causal analysis must establish which comparison answers the decision maker's question. An extra covariate, a recent dataset, or a close pre-treatment fit can conceal a mismatch between that question and the estimated effect. The electricity case makes the distinction consequential: operating capacity, project commitments, and household cost exposure can begin at different times.

The collection contains **22 methodological readings and 8 institutional sources**, checked November 26, 2026. Nineteen public PDFs are saved in categorized local reading folders. The public repository contains the annotated guides, source links, and original teaching materials. The [catalog](catalog.json) records versions, access status, inspection scope, and hashes for downloaded files. Link-only entries identify material that was not downloaded. This is a broad teaching collection rather than an exhaustive census of causal-inference research.

| Category | Main Question |
| --- | --- |
| [Foundations and Causal Graphs](01_Foundations/README.md) | Which paths does adjustment close or open? |
| [Adjustment and Selection](02_Adjustment_and_Selection/README.md) | What changes when analysis conditions on a response or completion? |
| [Longitudinal Identification](03_Longitudinal_Identification/README.md) | How should treatment-affected covariates and histories enter a panel design? |
| [Timing and Comparison Groups](04_Timing_and_Comparison_Groups/README.md) | When does exposure start, and who provides the counterfactual? |
| [Project Exposure and the 2020–2025 Window](05_Project_Exposure/README.md) | Which requests, commitments, cancellations, and protections occurred within the study period? |

## Suggested Reading Sequence

1. Cinelli, Forney, and Pearl (BC02), followed by Wysocki, Lawson, and Rhemtulla (BC10): explain each covariate's role before fitting the regression.
2. Rosenbaum (BC03), Elwert and Winship (BC04), and Montgomery, Nyhan, and Torres (BC05): compare adjustment with sample selection.
3. Abadie (BC19), Malani and Reif (BC18), and Butts (BC20): establish the exposure date and the comparison boundary.
4. Caetano, Callaway, Payne, and Sant’Anna (BC13): examine why inclusion and exclusion can both fail. Read its identifying assumptions before using the [authors' package](https://github.com/hugosantanna/badcontrols).
5. Read the [case assessment](CASE_ASSESSMENT.md), then reproduce the [original Python comparisons](../../03_Data_and_Code/Bad_Controls/README.md).

BC13 and BC14 replace the authors' earlier joint paper on time-varying covariates. They are recorded as the current complementary treatments; the earlier version is not counted as a separate contribution. Marginal structural models (BC22 and BC11) address sequential treatment histories under assumptions that differ from conditional parallel trends.

## Course Connections

- M3 §§3.20–3.21: adjustment, causal paths, and exact synthetic regressions.
- M6 §§6.40–6.42: treatment-affected covariates, phantom projects, and sample-window design.
- M9 §9.50: the reasons owed to households whose burdens are excluded from a convenient comparison.
- Sessions 4, 10, and 14: selected explanations within existing meeting allocations.
- [Optional ungraded practice](../../07_Labs/Bad_Controls/README.md): defend the estimand, test competing graphs, and reconstruct project exposure.

## Reading Copies and Reuse

Local PDF copies are under `readings/`, grouped by the five categories above. That folder is excluded from Git. Public availability does not by itself establish republication rights; original terms continue to apply. Source PDFs are unchanged. Figures, programs, and numerical constructions in the course are original. No downloaded program was executed to prepare the collection.
