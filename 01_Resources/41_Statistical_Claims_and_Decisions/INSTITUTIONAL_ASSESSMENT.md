# Electricity Prices, Project Pipelines, and Household Costs

## Decision and Evidence

A household needs to know how much it will pay and which risks it is required to bear. A regulator needs to know whether developer commitments cover the costs allocated to other customers. Those decisions require project histories, tariffs, consumption, and payment records alongside an estimate of average revenue per MWh.

Rana, Kaps, and Netessine's working paper describes the institutional distinction between regulated and restructured markets and explains its use of realized revenue per MWh (pp. 14–16). Its treatment is capacity beginning operation, with the first positive addition since 2020 defining the anchor. Its donor rule excludes positive additions of the selected operational treatment during the post-anchor horizon (pp. 16–18, Equations 15–20). The stated rule does not separately establish absence of project requests, preparatory investment, cancellations, or associated cost recovery.

The resulting identification concern is conditional. An eligible donor could have project-related costs despite no operating addition. The paper's panel and project records are needed to determine whether that occurred, which donors carried weight, and how the slope changed. The course makes no finding that a particular donor was contaminated or that this mechanism explains the published estimate.

## Verified Institutional Sources

Checked November 26, 2026. The links distinguish reporting, an operator's service process, official data definitions, and a commissioner's legal reasoning. These sources are linked; no complete copyrighted article is republished.

| Source | Date and Scope | Verified Contribution | Evidentiary Status |
| --- | --- | --- | --- |
| [Miranda Davis and Josh Saul, Bloomberg, ComEd Inks Deals to Keep Data Centers From Boosting Energy Bills](https://news.bloomberglaw.com/environment-and-energy/comed-inks-deals-to-keep-data-centers-from-boosting-energy-bills) | January 6, 2026; ComEd, northern Illinois | Reports agreements intended to address customer exposure to proposed projects that fail to materialize. | Full syndicated text read at [Energy Connects](https://www.energyconnects.com/news/utilities/2026/january/chicago-s-biggest-electricity-company-inks-deals-to-keep-data-centers-from-boosting-energy-bills/). Does not identify failures in the paper's sample. |
| [Ohio Power, Data Center Tariff and Service Process](https://www.aepohio.com/company/about/rates/data-center-tariff/) | Ohio Power territory; approved July 9, 2025, effective July 23, 2025 | Describes application, studies, contracts, and reimbursement for specified cancellation or delay before energization. | Current operator description of an approved tariff; coverage and historical contract dates matter. |
| [FERC Commissioner Judy Chang, ComEd Agreement Concurrence](https://ferc.gov/news-events/news/commissioner-changs-concurrence-transmission-security-agreement-between) | February 17, 2026; federal transmission regulation | Explains why accepting an agreement does not itself establish full protection of other customers from cost shifts. | Individual concurrence concerning an accepted agreement; distinct from a commission-wide empirical finding of harm or a retail tariff. |
| [EIA, Electricity Monthly Update, Retail Rates/Prices and Consumption](https://www.eia.gov/electricity/monthly/update/print-version.php) | Official US measurement explanation, current page checked November 26, 2026 | Defines revenue per kWh as a proxy for retail rates and prices. | Source definition; no new empirical electricity series is imported. |
| [EIA, Electric Sales, Revenue, and Average Price](https://www.eia.gov/electricity/sales_revenue_price/) | Archived 2024 data, released October 7, 2025 | Distinguishes average retail price tables from average monthly bill tables. | Product is discontinued; EIA directs users to EIA-861 files. |

The 2026 reporting and concurrence postdate the paper's 2020–2025 operating-entry sample. They establish the relevance of investigating institutional mechanisms. They do not establish the historical contracts or exposures of its utilities. The FERC page's title and displayed docket line differ; the course identifies the concurrence by commissioner, date, and subject without resolving that metadata discrepancy.

## Measurement and Identification

| Question | Required Object | Error in an Unsupported Extension | Evidence Needed |
| --- | --- | --- | --- |
| Did a representative household spend more? | Matched household payments and use over a stated interval | Replacing dollars per household with dollars per MWh | Customer-month denominators, tariffs, consumption, and bills |
| Did expenditure become less affordable? | Payments relative to income and essential needs | Treating an average unit price as a complete burden measure | Household resources, energy requirements, and distribution |
| Is a donor unexposed to the investment cycle? | Requests, commitments, investment, cancellations, and recovery | Equating zero operational additions with zero economic exposure | Dated project/utility links and cost-allocation records |
| What is the effect of completed operation? | An operational-entry estimand under a specified institutional environment | Substituting that estimand for all consequences of development | An explicit counterfactual and defensible comparison group |
| Who bears a failed project's costs? | Enforceable payments and allowed recovery by customer class | Assuming either automatic pass-through or automatic protection | Contracts, guarantees, collections, reuse, recovery decisions, and timing |

Neither a descriptive bill increase nor a cost-recovery possibility establishes a data-center causal effect. Likewise, a completion-based coefficient cannot settle the consequences of the entire project pipeline without additional assumptions. More precise estimates leave these distinctions intact.

## Reproducible Counterexamples

The original [institutional exposure program](../../03_Data_and_Code/Statistical_Inference/institutional_exposure.py) uses synthetic values only. It produces four tables:

1. The same 1,000 customers have a mean monthly bill of $100 at $100/MWh, then $110 at the same average price when mean use rises from 1 to 1.1 MWh. A separate scenario has the same $100 bill at $125/MWh and 0.8 MWh.
2. A completed project raises its utility's price by $10/MWh. A cancelled project raises an eligible operationally untreated donor's price by $8. A second donor has no project and no change.
3. Fixed weights of 0.75 and 0.25 produce a $6 donor increase and a $4 change difference. Equal baseline prices and no other changes are imposed. This is a two-period illustration, separate from the paper's within-utility capacity regression.
4. An annual revenue requirement of $1 million, residential share 0.8, and residential sales of 100,000 MWh produce $8/MWh under full recovery and no offset. Developer payments, asset reuse, or disallowed recovery can reduce that amount.

The donor example demonstrates attenuation under its chosen positive exposure. General bias need not be downward. Earlier exposure can enter the fitting window, later recovery can fall outside the outcome window, and shared markets can transmit costs beyond the local utility. Investigating these mechanisms requires the relevant dates and boundaries.

Full code and derivations appear in M6 §6.35; measurement is developed in M2 §2.28.1; the missing-premise argument appears in M9 §9.27.6. The optional lab asks students to change donor costs, payment guarantees, and the outcome denominator while preserving the stated comparison.

## Qualitative Corroboration and Its Scope

The [utility-disclosure example](../../03_Data_and_Code/Utility_Cost_Recovery/README.md) traces investment recovery, proposed customer charges, and revenue offsets using public sources. It preserves verbatim excerpts in M5 §5.27 and distinguishes the household bill from wholesale capacity costs and utility construction recovery. The paper itself discusses these mechanisms; selected disclosures therefore challenge overbroad assurance without independently refuting the historical coefficient. Most selected disclosures occur after the 2020–2025 study window.

## Bad Controls and the Observation Window

The [project-exposure assessment](../44_Bad_Controls_and_Project_Exposure/CASE_ASSESSMENT.md) adds evidence inside 2020–2025, particularly its later years, and separates adjustment covariates from exposed donors, anticipation, and completion selection. M6 §§6.40–6.42 provide complete synthetic calculations. Thoughtful design requires a baseline preceding relevant commitments and a sample aligned with the affected population. An appealing fit or recent data alone does not establish those conditions.
