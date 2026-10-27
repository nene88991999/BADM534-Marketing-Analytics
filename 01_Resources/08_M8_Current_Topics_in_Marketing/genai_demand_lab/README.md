# Demand for generative AI: public data around Egan, Russel, Shi and Yao (NBER w35953)

For the executed Marketing Analytics cases and interpretation corrections, see the [course adaptation review](COURSE_ADAPTATION.md) and [course programs](../../../03_Data_and_Code/GenAI_Demand/README.md).

**Paper.** Mark L. Egan, Dominic Russel, Claire Shi and Vincent Yao, *Competition in Generative AI: Evidence from Consumer Demand*, NBER Working Paper 35953, October 2026. https://www.nber.org/papers/w35953 (DOI 10.3386/w35953). Transaction-level credit and debit card data for 174 million US consumers (114 billion transactions) are used to measure paid adoption of the major generative-AI services and estimate a structural model of demand and supply.

**What it finds (abstract).** By April 2026 about 2.9% of US consumers paid for at least one major service, more so if young or high-income. Nearly all pay for a basic plan of $30 a month or less. Multihoming is common but falling as providers' capabilities grow; annual retention is 20-45%, low for a subscription product; switching rises around major model releases. The demand model says consumers are highly price-sensitive, far more loyal to AI than to any provider, and treat the services as increasingly substitutable, which limits pricing power unless quality differentiation grows.

**The honest answer to "can we collect this?"** No. Card-transaction panels are licensed from processors and data vendors and never public. What is public are *proxies*, each measuring a different thing, plus one vendor-published card-data index for businesses. This folder maps the paper's objects to those proxies, collects the ones that are one HTTP request away, and uses a simulated panel for the measurements that need individual-level data.

Module fit: **M8** (current topics: competition in AI) as home; **M2** for the API work; **M4** for retention and cohorts; **M6** for the release event study; **M7/M8** for the demand model.

## Crosswalk: paper measure → what you can get

| Paper object | Their source | Public proxy | Where | Access | Captures / misses |
|---|---|---|---|---|---|
| Paid adoption rate, by age and income | card panel | none at consumer level. Closest: **Ramp AI Index** (share of US *businesses* with paid AI spend, by vendor, monthly, from Ramp's card and bill-pay data) | https://ramp.com/data/ai-index | web page, no download | businesses not consumers; Ramp customers only; the only public card-based measure |
| Which services people pay for (shares) | card panel | **App Store top charts** (rank of each assistant app, daily snapshot) | `rss.marketingtools.apple.com/api/v2/us/apps/top-free/100/apps.json` | no key | downloads not payments; rank not level; iOS only. On 27 Oct 2026 ChatGPT was #5, Claude #8, Gemini #13, Grok #43 in the US free chart |
| Same | | **Cloudflare Radar** Internet-services ranking, category "Generative AI" (traffic-based) | `api.cloudflare.com/client/v4/radar/ranking/internet_services/top?serviceCategory=...` | free API token | traffic across all users, free and paid |
| Attention and switching around releases | card panel + release dates | **Wikipedia pageviews**, daily since 2015 | `wikimedia.org/api/rest_v1/metrics/pageviews/per-article/...` | no key, honest User-Agent | curiosity not use; article renames break series (see notebook A2) |
| Model release dates | news | **Epoch AI notable models** (CC BY) and **OpenRouter** model listing dates | `epoch.ai/data/notable_ai_models.csv`; `openrouter.ai/api/v1/models` | no key | Epoch has official dates; OpenRouter lags launch by hours |
| Plan prices and tiers | card amounts | provider pricing pages now; **Wayback Machine CDX API** for history | `web.archive.org/cdx/search/cdx?url=...&output=json` | no key | pages render prices client-side; archived HTML usually has them |
| API-side prices | n/a | **OpenRouter** prices per million tokens, 460+ models | same | no key | the market Fradkin (2025) studies with OpenRouter usage data |
| Multihoming, retention, switching | card panel | nothing public at the individual level. Options: a class survey; the **synthetic panel** here; the aggregate OpenRouter app-level patterns in Fradkin (2025) | `simulate_subscription_panel.py` | | simulation is for method practice only |
| Price sensitivity, substitutability | structural model | the synthetic panel's promotional price variation; a simple logit (notebook Part C) | | | one product's own-price response; no supply side |

## Files

| File | What it is |
|---|---|
| `genai_demand_lab.ipynb` | Executed notebook: Part A public signals, Part B the paper's descriptives on the synthetic panel, Part C a one-line demand model, exercises. |
| `collect_genai_signals.py` | Collectors (importable functions and a CLI): Apple charts, Wikipedia pageviews with redirect resolution, OpenRouter models and a release-event helper, Wayback CDX listing and archived-page text, Epoch AI table, Cloudflare Radar (token). |
| `simulate_subscription_panel.py` | Synthetic consumer-month-product panel calibrated to the abstract's moments; writes the `synthetic_*` files and the true parameters (`synthetic_dgp.json`). |
| `data/apple_top_free_us_2026-10-27.csv` | US top-100 free apps, captured 27 Oct 2026 01:50 UTC. |
| `data/ai_apps_appstore.csv` | App Store ids of the assistant apps, read off the live feed. |
| `data/wikipedia_pageviews_daily_2026-10-26.csv` | Daily views, Nov 2022 to 25 Oct 2026, for ChatGPT, Claude (both titles), Gemini (both titles). |
| `data/wikipedia_pageviews_monthly_2026-10-26.csv` | Monthly views for those plus Grok, Perplexity AI and Microsoft Copilot. |
| `data/openrouter_models_2026-10-27.csv` | 464 models with listing date, context length and USD per million tokens. |
| `data/consumer_plans_2026-10-26.csv` | Consumer plan prices verified on 26 Oct 2026, blanks left where the page renders the amount client-side (Exercise 1 fills them). |
| `data/synthetic_*.csv(.gz)`, `synthetic_dgp.json` | The simulated panel, its consumers, products, release events, basic-plan price path and true parameters. |

## Quick start

```bash
pip install requests pandas matplotlib
python collect_genai_signals.py --all --out data            # live captures (Cloudflare needs --cf-token)
python collect_genai_signals.py --wayback-list https://claude.com/pricing --since 2024-01-01
python simulate_subscription_panel.py --n 60000 --out data  # regenerate the panel (about 15 s)
jupyter lab genai_demand_lab.ipynb
```

Networks that block hobby and API hosts (this notebook was executed on one) make the live cells fall back to the captures in `data/`.

## What the synthetic panel is, and is not

`simulate_subscription_panel.py` draws 60,000 consumers (age group, income tercile, an AI-affinity term), 40 months (Jan 2023 to Apr 2026), six providers with basic and premium plans, release events as quality jumps, inertia, a satiation cost of holding a second subscription that rises over time, and promotional discounts in about a sixth of product-months. A common trend is solved each month so that aggregate adoption follows a logistic path ending at 2.9%. The resulting moments: 97-98% of subscriptions on basic plans; multihoming falling from 8-10% to 4% of payers; twelve-month provider retention 18-38% against 55% for "any provider"; a new-subscriber spike in release months. Launch months and release sizes are inputs, not facts; Exercise 1 checks them against the Wayback record. **Nothing in the panel is an estimate of the real market.**

## Terms, etiquette and attribution

- Apple's chart feeds, Wikimedia's REST API, OpenRouter's model list and the Wayback CDX API are public, keyless and documented. Send an honest `User-Agent` (Wikimedia asks for one and throttles anonymous clients), set timeouts, and keep to one call per source per run. Cloudflare Radar needs a free account token.
- Epoch AI data are CC BY 4.0; cite "Epoch AI, Notable AI Models, https://epoch.ai/data/notable-ai-models".
- Ramp AI Index figures are published on Ramp's site without a download; cite the page and the month.
- Pricing pages are the providers' copyrighted content; store the numbers you extract and the capture URL, not the pages.
- The paper is a working paper; cite it as Egan, Russel, Shi and Yao (2026), NBER WP 35953.

## Related

- Andrey Fradkin, *Demand for LLMs: Descriptive Evidence on Substitution, Market Expansion, and Multihoming* (arXiv 2504.15440, April 2025): the API-side version of the question, using OpenRouter data. https://arxiv.org/abs/2504.15440
- Ramp Economics Lab, *How we built the Ramp AI Index*: https://ramp.com/data/how-we-built-the-ramp-ai-index
- The McBroken lab in `02_M2_Customer_Data_and_Visualization/mcbroken_api_lab/` for the GitHub Actions snapshot pattern that turns any of these feeds into a panel.

*Built 2026-10-26 for BADM 534 course preparation.*
