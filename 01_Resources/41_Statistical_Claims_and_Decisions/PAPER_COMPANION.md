# The Cost of Intelligence: Paper Companion

Vishrut Rana, Christian Kaps, and Serguei Netessine. *The Cost of Intelligence: Impacts of AI Data Centers on US Electricity Prices*. Working paper dated September 30, 2026; SSRN record last revised October 12, 2026. [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7580459), [42-page reading copy](RanaKapsNetessine_WorkingPaper2026.pdf). The source is licensed CC BY 4.0 according to its SSRN record; this file is unchanged.

## Question, Sample, and Design

The paper studies how additional data-center capacity affects utility electricity prices and costs. Facilities of at least 10 MW activated in 2020–2025 are mapped to utilities with bundled service. The industrial sample contains 42 treated utilities and 648 utility-quarter observations; the main residential sample contains 41 and 627. The design constructs a synthetic control from 16 pre-treatment quarters, holds donor weights fixed, and regresses post-anchor gaps on cumulative capacity additions, with utility and quarter-of-year fixed effects in preferred specifications.

Revenue divided by MWh measures average payments per unit of electricity. Added capacity is measured in MW or as a percentage of the receiving utility's pre-treatment peak demand. The comparison concerns expansion relative to the pre-anchor baseline, which can already include data centers. It is not a comparison of an economy with data centers against one without them.

## Findings and Interpretation

Preferred estimates are positive for industrial and residential prices. At a reference exposure formed from reported average added capacity and average peak demand, the paper reports roughly $5.4/MWh for industry and $1.7/MWh for residences. The preferred residential ratio slope meets its 10% significance convention; other residential specifications meet 5%. The four-owner subgroup estimate is positive and imprecise. A direct developer-difference test reports p=0.101. The paper discusses cost recovery and infrastructure mechanisms, while acknowledging limited power, unobserved shocks, market spillovers, linearity, and unresolved developer channels.

These results motivate scrutiny of the effects that remain plausible, the claims added in prose, and the distinction between utility averages and household welfare. See the [claim assessment](CLAIM_ASSESSMENT.md) for exact anchors and calculations.

## Figure and Table Map

- Figures 1–3, pp. 13–14: growth, facility-size distributions, and locations. These describe the input inventory rather than causal effects.
- Figure 4, p. 15, and A.4, PDF p. 39: average price paths and inflation-adjusted paths. Comparisons depend on composition and the denominator.
- Figures 5–6 and Tables 1–3, pp. 21–25: industrial and residential synthetic comparisons and price regressions. A visual mean trajectory does not replace the specified counterfactual assumptions.
- Tables 4–5, pp. 26–28: owner and utility heterogeneity. Read joint contrasts and interactions, including uncertainty.
- Tables 6–7, pp. 30–31: cost and sales outcomes. Their samples and units differ from the price regressions.
- Tables A.1–A.4, PDF pp. 36–39: owner/utility classifications and descriptive magnitudes.
- Tables B.5–B.7, PDF pp. 40–42: pre-treatment fit and donor concentration. Pre-treatment fit supports a diagnostic; post-treatment validity requires additional conditions.

This companion is a selective guide and original assessment, not a full text conversion. Mathematical model derivations, all reference entries, facility maps, and detailed utility rows remain in the PDF. Course figures and programs reproduce selected implications of reported entries, not the original figures or underlying utility estimates.
