# Generative-AI Demand Data Dictionary

Inputs remain in `01_Resources/08_M8_Current_Topics_in_Marketing/genai_demand_lab/data/`. Paths below are relative to that folder. [The manifest](manifest.json) hashes the full supplied bundle. All subscription and price-simulation tables are synthetic; names resembling real providers do not make their histories empirical observations.

## Inputs Used by the Course Programs

| File | Unit and Fields | Coverage and Missingness |
| --- | --- | --- |
| `wikipedia_pageviews_daily_2026-10-26.csv` | Article-date. `provider` maps the selected title; `views` counts view events. Collector specification: English Wikipedia, all access, user agent category. | 5,248 supplied title-days across five titles. Dates with no row are unknown unless the retrieval process establishes zero. The executed case uses two Claude titles, June 1–September 30, 2026, with all 244 required title-days present. |
| `synthetic_consumers.csv` | One row per `consumer_id`; `age_group`, `income_group` are simulated categories. | 60,000 consumers, including never-payers. IDs are unique. No names or actual customer records. |
| `synthetic_subscriptions.csv.gz` | Consumer-month-provider holding. `plan`, `tier`, `price` in USD/month, Boolean `promo`, Boolean `new`. | 34,186 rows. Months with no held plan have no row. Under the complete simulator's recording rule, absent holdings are zero. `new` means absent from that provider in the preceding month, including returns. |
| `synthetic_basic_prices.csv` | Available provider-month. `basic_price` is USD/month; `promo` identifies an imposed promotional price. | 179 provider-months. Missing combinations outside this table mean unavailable offers. Zero subscribers within available combinations remain possible. |
| `synthetic_dgp.json` | Parameters and calendar: `n_consumers`, `alpha_price`, `gamma_inertia`, `kappa_satiation`, and `g_trend`. | Forty months, January 2023–April 2026. Positive `alpha_price=0.06` is subtracted in utility. `g_trend` is chosen monthly to approach a target adoption path; its stored values are rounded. |

The supplied product and release tables describe imposed scenarios. Provider start months, premium selection, and quality increments are inputs to that simulation. Current prices, public launch dates, and purchase histories need separate empirical sources.

## Outputs

| File in `results/` | Unit | Definitions |
| --- | --- | --- |
| `wikipedia_title_days.csv` | Calendar day in the chosen 122-day window | One column per selected title; `observed_titles` counts available title counts; `selected_title_views` is their sum only when both are observed. |
| `wikipedia_months.csv` | Calendar month | `calendar_days`, `complete_days`, each title's total, combined total. A total is unknown if any required day is missing. |
| `adoption.csv` | Simulated calendar month | Population, unique payers, subscriptions, multihomers, basic subscriptions, adoption, multihoming conditional on payment, basic share among subscriptions. Conditional shares are missing when their denominator is zero. |
| `cohorts.csv` | Starting provider and months since January 2025 | Fixed `cohort_size`; mutually exclusive `same_provider`, `other_provider_only`, `no_paid_provider`; `continuous_same_provider` requires holding the original provider at every observed monthly date. |
| `acquisition_types.csv` | Acquisition-event category in April 2026 | Counts of first paid entry, category return, complete provider switch, and provider addition. One event per newly held provider; multiple events can belong to one consumer. A complete switch drops every provider held in the prior month. |
| `provider_months.csv` | Available synthetic provider-month | Basic price, promo, basic holders, new basic holders, each count divided by the full roster. Premium holdings are excluded from these two counts. |
| `price_projections.csv` | Outcome specification | Slope of log odds on price after provider/month controls; rows used; sum of squared prices after removing controls. No standard errors or causal interpretation are attached. |

JSON companions record summary counts, interpretations, and verification. `results/verification.json` records the executed environment. Each chart can be reconstructed from the CSVs without accessing an external service.
