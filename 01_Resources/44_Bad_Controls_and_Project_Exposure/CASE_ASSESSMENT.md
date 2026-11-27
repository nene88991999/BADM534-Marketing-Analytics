# Bad Controls, Phantom Projects, and Research Design

## The Decision and the Target Effect

Households and regulators need to know whether data-center development creates costs that households must bear, including costs incurred before a facility operates or after a proposal fails. An incremental operating-capacity effect and the total effect of the project pipeline answer different questions. A narrow result requires an explicit argument before it can support broad reassurance about household burdens.

Rana, Kaps, and Netessine's saved September 30, 2026 paper uses operating additions to anchor treatment in 2020–2025. Its donor screen excludes positive additions of the selected operating-capacity measure during the relevant post-anchor horizon. Equations 15–20, pp. 17–18, describe this procedure. Equation 21 relates synthetic-control gaps to cumulative capacity with utility and quarter-of-year fixed effects. The paper explicitly discusses possible spillovers on p. 20. These are verified design features. The methods do not establish a separate screen for every donor's requests, canceled projects, or unrecovered preparatory commitments. [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7580459).

The synthetic weights use 16 quarters preceding the operating-entry anchor, so early anchors can use outcome data from before 2020. The relevant assessment is whether these quarters precede the economic exposure, including project commitments. Calendar precedence relative to opening alone does not establish that condition.

The phrase “bad controls” covers a covariate problem in its usual econometric use. Exposed donor units, anticipation, and selection into observed operating facilities are related design concerns with different mechanisms. The paper is not shown here to regress on post-entry infrastructure spending as a control. Its cost outcomes must not be misreported as adjustment covariates.

## Why the Study Window Deserves Particular Scrutiny

The concern has evidence inside 2020–2025, especially toward the end of the period. On July 20, 2023, the Port of Cascade Locks and Roundhouse announced cancellation after insufficient community support. In January 2025, LBNL discussed financial risks from underused large-load infrastructure. Ohio Power's data-center tariff was adopted in July 2025 and introduced financial commitments concerning project-related risks. These events make preparatory exposure and project failure material questions for the chosen window. They do not show that any named donor in the paper incurred residential costs. [Port announcement](https://www.portofcascadelocks.gov/july-20-2023-cascade-locks-port-and-roundhouse-inc-jointly-announce-decision-to-discontinue-datacenter-project), [LBNL](https://emp.lbl.gov/publications/electricity-rate-designs-large-loads), [tariff record](https://www.aepohio.com/company/about/rates/data-center-tariff/).

Data Center Watch's first report describes $64 billion in blocked or delayed proposed investment; its Q2 2025 summary reports 20 affected projects and $98 billion. This is evidence of substantial disruption during the later part of the sample, collected from public records and reporting. The collection targets opposition, lacks a consistent all-project denominator across earlier years, and mixes blocked and delayed projects. These totals measure proposed investment, not utility expenditure, cancellations alone, or household losses. The reports have overlapping coverage and evolving records, so their totals should not be summed. [Initial report](https://www.datacenterwatch.org/report), [Q2 2025 summary](https://www.datacenterwatch.org/q22025).

The strongest supported historical statement is that project opposition and uncertainty were conspicuous within the latter part of the authors' window. A claim that cancellation rates were uniformly higher throughout 2020–2025 than in an earlier period would require a consistent project census. In particular, later reporting from 2026 is subsequent institutional evidence and does not substitute for dated exposures in 2020–2025.

## Four Distinct Routes to a Misleading Interpretation

| Mechanism | Consequence | Evidence Needed |
| --- | --- | --- |
| Adjusting for treatment-induced investment | May remove a pathway from the total effect or open a collider path | Actual covariate definitions, causal graph, dates |
| Matching on outcomes after project commitments | May absorb part of the project effect into the baseline | Request, commitment, expenditure, and recovery dates |
| A donor with no new operating MW bears project costs | May shift the counterfactual away from no project exposure | Donor weights, project histories, contracts, recovered amounts |
| Observing only completed facilities by the cutoff | Changes the represented project population and can create selection | Complete proposal cohort, completion determinants, pending statuses |

A service request is not an infrastructure expenditure. An expenditure is not automatically recoverable from households. Establish the sequence from request to binding commitment, spending, authorized recovery, customer allocation, and actual payment. Collect enforceable developer contributions, asset reuse, and disallowed costs as potential offsets. Projects with no incurred cost or with complete developer coverage are informative negative cases.

## Convenience and Identification

A recent dataset can offer accurate records of operating facilities while omitting the states needed to define an unexposed comparison. A cutoff can also classify a delayed project as untreated simply because its opening occurs later. If commitments already affect prices, that project is exposed during the observed window. The issue is internal validity when the proposed counterfactual is wrong, and external validity when a valid effect for selected completed projects is generalized to all projects. These failures can coexist.

The empirical defense must establish that the window contains a baseline preceding the relevant exposure, that its donors identify the specified counterfactual, and that its outcome measures the burden being discussed. A rationale for using recent data does not establish these conditions. More observations or a smaller standard error can increase confidence in a misaligned comparison. Thoughtful design begins with the intervention and affected population, then asks which records and time span are required.

## A Feasible Reassessment

1. Define separate estimands for operating additions and the full project pipeline, including the horizon and household-cost measure.
2. Reconstruct dated proposal cohorts, including withdrawals, cancellations, postponements, and pending projects. Link duplicate requests and alternative sites.
3. Map projects to utilities and shared transmission exposure. Preserve uncertainty in the mapping.
4. Identify obligations and recovery under the contracts and regulations then in force. Preserve zero-cost and fully offset cases.
5. Report how much synthetic-control weight rests on each exposure category. Refit under defensible alternative donor rules and earlier exposure dates; report loss of support and fit.
6. Compare cohorts with a common follow-up horizon. A project still pending at the cutoff remains pending, rather than being coded as a confirmed cancellation.
7. Present sensitivity ranges when the exposure history is incomplete. State which claim remains supported and which would require additional evidence.

The [synthetic programs](../../03_Data_and_Code/Bad_Controls/README.md) isolate possible mechanisms. They do not reestimate the published coefficient, establish its bias direction, or demonstrate that a particular donor is contaminated.
