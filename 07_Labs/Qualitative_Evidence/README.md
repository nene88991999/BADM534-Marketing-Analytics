# Utility Disclosures, Qualitative Evidence, and Affordability

A household advocate must respond to an assurance that data-center development creates little concern for electricity affordability. Use the [source register](../../03_Data_and_Code/Utility_Cost_Recovery/sources.json), [codebook](../../03_Data_and_Code/Utility_Cost_Recovery/CODEBOOK.md), and M5 §5.27 to identify what the evidence supports. This activity is optional ungraded practice; it establishes no assessment requirements.

## Define the Inquiry

Write the decision, population, time horizon, and comparison before reading the coded results. Record your prior expectation and the evidence that would change it. Explain why calls addressed to investors can reveal recovery plans while leaving household experience unobserved. Consult Hsieh and Shannon (2005) on directed content analysis and SRQR (O'Brien et al., 2014) on reporting context and reflexivity; full citations are in the [methods guide](../../01_Resources/42_Qualitative_Evidence/README.md).

## Retrieve and Assess Sources

Run the offline analysis first:

```sh
python3 03_Data_and_Code/Utility_Cost_Recovery/analyze.py
python3 03_Data_and_Code/Utility_Cost_Recovery/test_examples.py
```

The optional `collect.py --download` command retrieves the fixed public source list and creates local review windows. Inspect the article boundaries, issuer, date, speaker turn, and any preceding question. Compare a selected passage with the original issuer-hosted document. Record a failed retrieval as unavailable. Choose at least one unmatched passage to assess what the search missed; do not label the resulting check representative accuracy.

## Code Before Comparing

Two readers independently fill copies of `data/reviewer_template.csv` after reading the relevant source contexts. Preserve both records before discussion. Identify which disagreements concern the definition, the unit of text, or substantive interpretation; revise the codebook and revisit affected claims. If working alone, record that status and compare alternative readings without calling them independent coding. O'Connor and Joffe (2020) support deliberation about coding consistency; Braun and Clarke (2021) explain why this is not a universal requirement for every qualitative approach.

Build a comparison matrix with sources as rows and recovery, allocation, timing, and offsets as columns. Keep subsidiary and customer-class differences visible. This adapts the within-case and between-case comparisons of Gale et al. (2013). Explain why the Evergy call and release constitute one corporate source family and why a transcript mirror adds no independent observation.

## Test the Strongest Alternative Interpretation

Compare the investment-related increase with the offset in the Evergy and CenterPoint calls. For Evergy's later request, distinguish a lower requested amount than otherwise from a lower bill than today. For CenterPoint, identify the charge component and avoid treating a distribution revenue requirement as residential expenditure. Compare PSEG's explicit residential-bill statement with the New Jersey agency's multiple explanations and the absence of an estimated data-center share.

Prepare a short evidence table containing a supported statement, its strongest contrary or qualifying passage, and the remaining question. Propose the order, tariff, cost-allocation filing, or household outcome that would address that question. Select one conclusion you changed after examining counterevidence and explain the reason.

## Construct an Ought Argument

Use M9 §9.33 to formulate a recommendation. State a factual premise, a normative principle concerning burdens imposed on households, a feasible alternative, and the strongest objection. Explain why new costs and claimed offsets require transparent substantiation. Then consider the firm's objection that premature criticism could obstruct beneficial investment. Specify what evidence would justify modifying either recommendation.

The household advocate may criticize an overbroad assurance while accepting that the historical paper estimates a small average effect. A final answer must distinguish empirical contradiction, a competing mechanism, a scope problem, and a normative objection. It must also state whose experience the documents leave unrepresented.

## Evidence and the Proposed Action

Use [Evidence Standards and Reasonable Protection](../Evidence_Standards/README.md) to distinguish an inquiry, a temporary safeguard, and a remedy. Compare the consequences of false alarms and missed harm, defend the interests included in the analysis, and answer the strongest reasonable objection. The complete synthetic calculation appears in M6 §6.44; M9 §§9.55–9.59 connects the decision to disciplinary history and institutional standards.
