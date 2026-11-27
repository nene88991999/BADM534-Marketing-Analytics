# M8 · Current Topics in Marketing

113 resources (29 core). Built 2026-11-27 from `00_Index/_data/`; edit the YAML there and rerun `00_Index/_build/build_catalog.py` rather than editing this file.

Priority: **core** = likely to assign or build on; **recommended** = strong supplement; **optional** = background or niche. *Access* tells you whether students can open it without a login.

## Contents

- [Competition and demand in generative AI](#competition-and-demand-in-generative-ai) (8)
- [Generative AI in marketing practice](#generative-ai-in-marketing-practice) (9)
- [Privacy and measurement](#privacy-and-measurement) (5)
- [Retail media, creators and pricing](#retail-media-creators-and-pricing) (3)
- [Algorithmic bias](#algorithmic-bias) (2)
- [Ethics and law: course note and theory](#ethics-and-law-course-note-and-theory) (10)
- [Ethics and law: rules and enforcement](#ethics-and-law-rules-and-enforcement) (33)
- [Ethics and law: evidence on consumer harm](#ethics-and-law-evidence-on-consumer-harm) (20)
- [Industry reports](#industry-reports) (4)
- [Staying current: newsletters and podcasts](#staying-current-newsletters-and-podcasts) (4)
- [Python for marketing analytics: notebooks and code](#python-for-marketing-analytics-notebooks-and-code) (8)
- [Data Artifacts and Research Independence](#data-artifacts-and-research-independence) (6)
- [Data poisoning and measurement integrity](#data-poisoning-and-measurement-integrity) (1)

## Competition and Demand in Generative AI

- [core] **[Census Business Trends and Outlook Survey (BTOS): biweekly AI use by US businesses](https://www.census.gov/hfp/btos/data)** (2026). U.S. Census Bureau
  `dataset` · `intro` · `access: open` · `AI angle`
  Nationally representative biweekly survey of US employer businesses since September 2023, with a question on AI use (revised in November 2025 from 'in producing goods or services' to 'in any business function') and expected use in the next six months, by sector, state, the 25 largest metro areas and firm size. National AI use was 19.8% for the period ending 3 May 2026; 37% for firms with 250+ employees; 39.7% in Information, about 14% in Retail.
  *Use in wiki:* The official counterpart to the Ramp AI Index in genai_demand_lab: compare a probability survey of firms with card-transaction adoption among Ramp customers, and discuss why the levels differ. The November 2025 wording change is a ready-made lesson in series breaks.
  *Note:* Figures from the Census story 'Large Firms With at Least 20 Employees Biggest AI Users' (26 May 2026); supplement documented in CES-WP-26-25. Download files from the BTOS data page.

- [core] **[Competition in Generative AI: Evidence from Consumer Demand](https://www.nber.org/papers/w35953)** (2026). Egan, M. L.; Russel, D.; Shi, C.; Yao, V. *NBER Working Paper 35953*
  `paper` · `advanced` · `access: paid` · `AI angle`
  Card transactions for 174 million US consumers measure paid adoption of generative-AI services: about 2.9% paying by April 2026, skewed young and high-income; almost all on plans of $30 or less; multihoming common but falling; annual retention 20-45%; switching rising around model releases. A structural demand and supply model finds high price sensitivity, loyalty to AI rather than to providers, and rising substitutability that limits pricing power.
  *Use in wiki:* Anchor reading for an M8 session on competition in AI, and the source of the measurements reproduced on the synthetic panel in genai_demand_lab. Pairs with the Fradkin OpenRouter paper for the API side.
  DOI [10.3386/w35953](https://doi.org/10.3386/w35953)
  *Note:* NBER working papers are paywalled for non-subscribers; UIUC has access. The PDF could not be fetched from the workspace, so the entry rests on the NBER abstract page. Fiserv appears in the author disclosures, not as a stated data source.

- [core] **[Generative-AI Demand: Public Signals and a Synthetic Subscription Panel](https://github.com/nene88991999/BADM534-Marketing-Analytics/tree/main/01_Resources/08_M8_Current_Topics_in_Marketing/genai_demand_lab)** (2026). Yang, N. (Marketing Analytics course materials)
  `notebook` · `intermediate` · `access: open` · `Course material; captures and synthetic data, see README` · `AI angle`
  Supplied collectors, dated public captures, a synthetic subscription panel, and a reference notebook. Executed course adaptations measure title-specific attention, fixed-cohort retention, acquisition-event types, and descriptive stock/flow price slopes, with an exact binary-logit recovery benchmark.
  *Use in wiki:* M2 2.17, M4 4.14, and M8 8.13. Use 03_Data_and_Code/GenAI_Demand/README.md for executed programs, complete Python in the notes, Illinois-color figures, and verified output tables.
  Tools: requests, pandas, numpy, matplotlib · Local copy: `08_M8_Current_Topics_in_Marketing/genai_demand_lab`
  *Note:* Original notebook and network collectors were inspected, not rerun. The flow regression does not identify the heterogeneous dynamic generator's price parameter. See genai_demand_lab/COURSE_ADAPTATION.md for fixed-cohort, acquisition, calibration, and event-date corrections. The panel is entirely synthetic.

- [recommended] **[Monitoring AI Adoption in the US Economy](https://www.federalreserve.gov/econres/notes/feds-notes/monitoring-ai-adoption-in-the-u-s-economy-20260403.html)** (2026). Allen, J. S. *FEDS Notes, Board of Governors of the Federal Reserve System, 3 April 2026*
  `report` · `intro` · `access: open` · `AI angle`
  Compares three public measures of AI adoption: Census BTOS (about 18% of firms at year-end 2025), the Atlanta Fed's Survey of Business Uncertainty (about 78% employment-weighted firm adoption, 54% for LLMs) and the Real-Time Population Survey (about 41% of workers using generative AI at work, November 2025), and explains why they differ.
  *Use in wiki:* Five-minute read for the M8 measurement discussion: three numbers that look contradictory until you ask who is counted, how, and whether paid or free use counts. Pairs with Egan et al. (consumers, paid) and the Ramp AI Index (businesses, paid).

- [recommended] **[Ramp AI Index: monthly paid-AI adoption by US businesses, by vendor](https://ramp.com/data/ai-index)** (2026). Ramp Economics Lab
  `dataset` · `intro` · `access: open` · `AI angle`
  Monthly paid-AI adoption and vendor spending measures among businesses in Ramp's transaction sample. Its business population differs from consumer subscription panels, app users, and pageview events.
  *Use in wiki:* M2/M8 comparison of measurement populations and denominators. Consult the dated methodology and sample before comparing business paid adoption with consumer adoption or public attention.
  *Note:* Methodology: https://ramp.com/data/how-we-built-the-ramp-ai-index. Current chart values were not reverified in the course adaptation. No uniqueness claim about all public transaction-based measures is made.

- [recommended] **[Demand for LLMs: Descriptive Evidence on Substitution, Market Expansion, and Multihoming](https://arxiv.org/abs/2504.15440)** (2025). Fradkin, A. *arXiv 2504.15440*
  `paper` · `intermediate` · `access: open` · `AI angle`
  Uses data from OpenRouter, an LLM marketplace, to describe how apps adopt new models: rapid initial adoption that stabilises within weeks, substitution from competing models versus market expansion, and widespread multihoming across models.
  *Use in wiki:* The API-side counterpart of Egan et al.; read the two together to separate consumer subscriptions from developer token demand. OpenRouter's public model list (prices, listing dates) is in the lab's collectors.

- [optional] **[Cloudflare Radar API: Internet services ranking (including a Generative AI category)](https://developers.cloudflare.com/api/resources/radar/subresources/ranking/subresources/internet_services/methods/top/)** (2026). Cloudflare
  `documentation` · `intermediate` · `access: freemium` · `AI angle`
  Token-authenticated Internet-services ranking endpoint, with date and category selection. Supplied collection code was inspected; endpoint response and token scopes were not independently tested during course adaptation.
  *Use in wiki:* Optional traffic-ranking comparison in M2/M8. Retain the rank scale and traffic population; do not convert ranks into market shares.
  *Note:* Verify category labels, permissions, current API schema, and usage terms before calling. No credential or collection workflow was activated.

- [optional] **[OpenRouter Models API: Posted Prices and Listing Dates](https://openrouter.ai/api/v1/models)** (2026). OpenRouter
  `documentation` · `intro` · `access: open` · `AI angle`
  Public model metadata and posted token prices. The supplied dated capture has 464 rows, including model variants and variable-price entries. Marketplace listing timestamps and available offers are distinct from public launch dates and realized usage.
  *Use in wiki:* M2/M8 data definitions and price units. Verify announcement dates separately before constructing a release event study; preserve variants and variable-price status.
  *Note:* Collector inspection confirms conversion from USD per token to USD per million tokens and missing numeric values for negative variable-price sentinels. Endpoint not re-collected during course adaptation.

## Generative AI in Marketing Practice

- [core] **[Buy it in ChatGPT: Instant Checkout and the Agentic Commerce Protocol](https://openai.com/index/buy-it-in-chatgpt/)** (2025). OpenAI. *openai.com (September 29, 2025)*
  `website` · `intro` · `access: open` · `Apache-2.0 (ACP specification)` · `AI angle`
  OpenAI's launch of in-chat purchasing (starting with US Etsy sellers, Shopify planned) and the open Agentic Commerce Protocol (ACP), co-developed with Stripe, in which merchants stay merchant of record.
  *Use in wiki:* Primary source for the agentic-commerce lecture. Ask what happens to brand choice, search ads and retail media when an AI agent does the shopping.
  [Open-access copy](https://www.agenticcommerce.dev/) · Local copy: `08_M8_Current_Topics_in_Marketing/repos/agentic-commerce-protocol__agentic-commerce-protocol`
  *Note:* Developer docs are at developers.openai.com/commerce. The ACP license (Apache 2.0) is stated on agenticcommerce.dev; I did not fetch the GitHub repo itself.

- [core] **[GEO: Generative Engine Optimization](https://arxiv.org/abs/2311.09735)** (2024). Aggarwal, P.; Murahari, V.; Rajpurohit, T.; Kalyan, A.; Narasimhan, K.; Deshpande, A. *arXiv 2311.09735 (v3, June 2024); KDD 2024 per course brief (venue not verified)*
  `paper` · `intermediate` · `access: open` · `AI angle`
  Defines generative engine optimization: making content visible in LLM-generated search answers. Introduces GEO-bench (10K queries) and shows that strategies such as adding citations, quotes and statistics can raise visibility by up to 40%.
  *Use in wiki:* The anchor reading for 'SEO becomes GEO'. Students rewrite a product page with GEO tactics and test their visibility in an LLM answer engine.
  [Open-access copy](https://generative-engines.com/GEO/) · Tools: openai · Local copy: `08_M8_Current_Topics_in_Marketing/repos/GEO-optim__GEO`
  *Note:* The ACM DL page (KDD) could not be fetched, and the project page cites the work only as arXiv. GEO-bench is at huggingface.co/datasets/GEO-optim/geo-bench.

- [recommended] **[Frontiers: Generative AI and Personalized Video Advertisements](https://pubsonline.informs.org/doi/fpi/10.1287/mksc.2023.0494)** (2025). Kapoor, A.; Kumar, M. *Marketing Science 44(4), 733–747*
  `paper` · `advanced` · `access: library`
  Studies the effectiveness of generative-AI personalized video ads relative to non-personalized versions.
  *Use in wiki:* Fills a gap the main search flagged (no good piece on GenAI personalization). Check its design and findings before pairing it with M6.
  DOI [10.1287/mksc.2023.0494](https://doi.org/10.1287/mksc.2023.0494)
  *Note:* Also on the MBA 542 Module 6 reading list. The summary is deliberately brief because the paper itself was not opened; MIT IDE has a research brief (https://ide.mit.edu/insights/personalized-ai-video-ads).

- [recommended] **[Powering AI commerce with the new Agent Payments Protocol (AP2)](https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol)** (2025). Parikh, S.; Surapaneni, R. (Google). *Google Cloud Blog (September 16, 2025)*
  `blog` · `intro` · `access: open` · `AI angle`
  Google's open protocol for AI agents to initiate payments, using signed 'Intent' and 'Cart' mandates as a verification record. More than 60 partners (Mastercard, AmEx, PayPal, Adyen, Coinbase and others) back it, and it works as an extension of A2A alongside MCP.
  *Use in wiki:* Compare with OpenAI's ACP: who controls the customer relationship and the data when agents buy?
  *Note:* The repo is linked as goo.gle/ap2; no direct GitHub URL was verified, and the license was not stated.

- [recommended] **[The Power of Generative Marketing: Can Generative AI Create Superhuman Visual Marketing Content?](https://ideas.repec.org/a/eee/ijrema/v42y2025i1p13-31.html)** (2025). Hartmann, J.; Exner, Y.; Domdey, S. *International Journal of Research in Marketing 42(1), 13–31*
  `paper` · `intermediate` · `access: library`
  Compares AI-generated with human-made marketing images at scale, finding that current generative models can match or exceed human-made visuals on quality and realism measures.
  *Use in wiki:* Evidence for the M8 GenAI-in-marketing discussion. Check the study designs before using it as an M6 example.
  *Note:* Also on the MBA 542 Module 6 reading list. DOI not confirmed in a search result.

- [recommended] **[When AI Guides the Shopping Journey](https://www.iab.com/insights/when-ai-guides-the-shopping-journey/)** (2025). IAB; Talk Shoppe. *IAB (October 28, 2025)*
  `report` · `intro` · `access: free-registration` · `AI angle`
  Mixed-method study (450+ digital ethnographies plus a survey of 600 US consumers). Nearly 40% of US shoppers use AI when shopping. AI reshapes rather than shortens the path to purchase, and trust friction is common.
  *Use in wiki:* Consumer-side evidence to pair with the agentic-commerce protocols, and a source of discussion stats.
  *Note:* Download terms (free or registration) were not stated.

- [recommended] **[Frontiers: Supporting Content Marketing with Natural Language Generation](https://ideas.repec.org/a/inm/ormksc/v41y2022i3p441-452.html)** (2022). Reisenbichler, M.; Reutterer, T.; Schweidel, D. A.; Dan, D. *Marketing Science 41(3): 441-452*
  `paper` · `intermediate` · `access: library` · `AI angle`
  Machine-drafted, human-edited SEO landing-page copy is nearly indistinguishable from expert copy, and in field experiments it ranks better in search at much lower cost.
  *Use in wiki:* Evidence-based case for 'human-in-the-loop' GenAI content, which pairs with GEO as the 'before and after' of LLM search.
  DOI [10.1287/mksc.2022.1354](https://doi.org/10.1287/mksc.2022.1354)

- [optional] **[Universal Commerce Protocol (UCP)](https://ucp.dev/)** (2026). UCP Authors (co-developed by Google, Shopify and others). *ucp.dev*
  `website` · `intro` · `access: open` · `Apache-2.0` · `AI angle`
  An open standard covering the whole agentic shopping flow (discovery, checkout, post-purchase) between platforms, agents and businesses. It builds on AP2 for payments.
  *Use in wiki:* A 2026 snapshot of the competing agentic-commerce standards (ACP vs AP2/UCP) for a short comparison table on the wiki.
  *Note:* The announcement date is not stated on the site. The year 2026 comes from the copyright and the lodging draft. The site lists Amazon, Microsoft and Stripe among co-developers; check this before citing.

- [optional] **[The Caring Machine: Feeling AI for Customer Care](https://www.ama.org/2024/04/23/can-companies-create-a-machine-that-feels-and-cares-using-generative-ai-to-provide-empathetic-customer-care/)** (2024). Huang, M.-H.; Rust, R. T. *Journal of Marketing 88(5)*
  `paper` · `intermediate` · `access: library`
  Conceptual framework for using generative 'feeling AI' to deliver empathetic customer care and build customer lifetime value. The link is the AMA's summary of the article.
  *Use in wiki:* Optional M8 reading if the course touches AI customer service.
  *Note:* Also on the MBA 542 Module 4 reading list. A corrigendum was published (https://journals.sagepub.com/doi/full/10.1177/00222429241270362). The article's own DOI was not confirmed.

## Privacy and Measurement

- [core] **[Retail Media ROAS Demystified: Understanding Your Brand's ROAS](https://ovative.com/impact/expert-insights/retail-media-roas-demystified/)** (2025). Nelson, D. T.; Bante, K.; Gordon, B. R.; Anderson, E. T.; Dantzinger, L.; Armor, S. *Ovative Group with Albertsons Media Collective and Kellogg School of Management (May 15, 2025)*
  `report` · `intermediate` · `access: open`
  Analyzes 573 Albertsons Media Collective campaigns to show how retail-media-network ROAS methods differ and how much reported results shift with methodology. Ends with questions advertisers should ask RMNs.
  *Use in wiki:* Retail-media case reading (with Kellogg co-authors Gordon and Anderson). Students explain why platform-reported ROAS and incremental ROAS differ.
  [Open-access copy](https://ovative.com/wp-content/uploads/2025/05/Retail-Media-ROAS-Demystified-Ovative-Albertsons-Kellogg-Business-School.pdf)
  *Note:* The PDF link was given on the fetched page; I did not fetch the PDF itself.

- [core] **[Update on Plans for Privacy Sandbox Technologies](https://privacysandbox.google.com/blog/update-on-plans-for-privacy-sandbox-technologies)** (2025). Chavez, A. (Google, VP Privacy Sandbox). *privacysandbox.google.com (October 17, 2025)*
  `blog` · `intro` · `access: open`
  Google says Chrome will keep its current approach of user choice on third-party cookies (no deprecation). It is retiring most Privacy Sandbox APIs (Topics, Protected Audience, Attribution Reporting, IP Protection and others) after low adoption, and keeping CHIPS, FedCM and Private State Tokens.
  *Use in wiki:* The definitive answer to 'are cookies dead?' as of late 2026. Use it to open the measurement week and explain why first-party data, clean rooms and MMM matter anyway.
  *Note:* privacysandbox.com/news/... now redirects to privacysandbox.google.com. Check the status page (privacysandbox.google.com/overview/status) before class for any later change.

- [recommended] **[IAB Tech Lab Standards: Data Clean Rooms Guidance, PAIR, and ADMaP](https://iabtechlab.com/standards/)** (2025). IAB Tech Lab (Addressability and PETs Working Group). *iabtechlab.com*
  `website` · `intermediate` · `access: open`
  Industry standards index listing the Data Clean Rooms Guidance (v1.0, July 2024), PAIR for privacy-safe advertiser-publisher ID matching in clean rooms (2024), and ADMaP for sharing conversion data with private set intersection or TEEs (February 2025).
  *Use in wiki:* Instructor background and a short explainer on how clean rooms let a brand and a retailer join first-party data without exchanging it.
  *Note:* The fetched index page did not expose deep links to each standard. For a concrete vendor example, AWS Clean Rooms (aws.amazon.com/clean-rooms/, verified) supports SQL and PySpark analyses, differential privacy and ML on partner data.

- [recommended] **[Insights from an experiment crowdsourcing data from thousands of US Amazon users: the importance of transparency, money, and data use](https://arxiv.org/abs/2404.13172)** (2024). Berke, A.; Mahari, R.; Pentland, S.; Larson, K.; Calacci, D. *Proceedings of the ACM on Human-Computer Interaction 8 (CSCW2), Article 466*
  `paper` · `intermediate` · `access: open`
  Randomised experiment embedded in the data-collection tool behind Open e-commerce 1.0: showing people their own data raises willingness to share it, sharing rises linearly with the payment offered, real money moves people more than hypothetical money (a field test of the privacy paradox), and willingness differs by demographic group.
  *Use in wiki:* M8 privacy session: a field experiment on what consumers' data is worth to them, from the same people whose purchases students can analyse. Also an M6 example of an experiment built into a product flow.
  DOI [10.1145/3687005](https://doi.org/10.1145/3687005)

- [recommended] **[App Tracking Transparency (framework documentation)](https://developer.apple.com/documentation/apptrackingtransparency)** (2021). Apple Developer. *developer.apple.com*
  `documentation` · `intro` · `access: open`
  Apple's official documentation for the ATT permission that apps must request before tracking users across other companies' apps and sites or accessing the IDFA. It was introduced with iOS 14.5.
  *Use in wiki:* Primary source for the ATT shock to mobile ad targeting and attribution, to pair with a discussion of how platforms shifted to modeled conversions and MMM.
  *Note:* The page is JavaScript-rendered, so the fetch returned only metadata. The iOS 14.5 and 2021 dates are standard knowledge, not quoted from the page. No academic ATT study was verified in this pass (search budget ran out).

## Retail Media, Creators and Pricing

- [core] **[2025 Creator Economy Ad Spend & Strategy Report](https://www.iab.com/insights/2025-creator-economy-ad-spend-strategy-report/)** (2025). IAB. *IAB (November 20, 2025)*
  `report` · `intro` · `access: open`
  US creator ad spend projected at $37B in 2025 (+26% year over year, about 4x faster than overall media), $44B expected in 2026. 48% of buyers call creators a 'must buy', and 3 in 4 brands use or plan AI for creator marketing.
  *Use in wiki:* Size-of-market slide and discussion: why creator measurement and standards lag, linked to M5 social media analysis.
  *Note:* The summary page is public and the full PDF is downloadable from it. The page was modified June 2026.

- [recommended] **[The Commerce Media Connection Gap: Why the Next Phase of Growth Depends on the Cohesion of the Ecosystem](https://www.iab.com/wp-content/uploads/2026/10/The-Commerce-Media-Connection-Gap.pdf)** (2026). SMG; IAB; IAB UK. *IAB (October 2026)*
  `report` · `intro` · `access: open`
  Survey of 281 brands, agencies and RMNs in six countries (fieldwork July to August 2026). Reporting is the least connected function, only 14% get unified cross-channel reporting, and 46% of brands say proven incremental ROI would unlock more spend.
  *Use in wiki:* A very current snapshot of retail-media pain points (fragmentation, measurement) for the M8 discussion.
  *Note:* The report contains no RMN spend figures. For market size, see the IAB/PwC Internet Advertising Revenue Report FY2025 (iab.com/insights/internet-advertising-revenue-report-full-year-2025/, verified; about $300B in US internet ad revenue in 2025, +13.9%; key takeaways need a free IAB account).

- [recommended] **[Artificial Intelligence, Algorithmic Pricing, and Collusion](https://www.aeaweb.org/articles?id=10.1257/aer.20190623)** (2020). Calvano, E.; Calzolari, G.; Denicolò, V.; Pastorello, S. *American Economic Review 110(10): 3267-97*
  `paper` · `advanced` · `access: library` · `AI angle`
  Q-learning pricing algorithms in simulated oligopolies learn to sustain supra-competitive prices with punishment strategies, without communicating.
  *Use in wiki:* Background for the algorithmic-pricing discussion (RealPage-style cases). Present the key figure and intuition rather than assigning the full paper.
  DOI [10.1257/aer.20190623](https://doi.org/10.1257/aer.20190623)
  *Note:* Empirical complement: Brown & MacKay (2023), 'Competition in Pricing Algorithms', AEJ: Microeconomics 15(2): 109-56, doi 10.1257/mic.20210158 (aeaweb page verified). It shows that simple rival-responsive pricing algorithms at online retailers can raise prices.

## Algorithmic Bias

- [core] **[Algorithmic Bias? An Empirical Study of Apparent Gender-Based Discrimination in the Display of STEM Career Ads](https://ideas.repec.org/a/inm/ormnsc/v65y2019i7p2966-2981.html)** (2019). Lambrecht, A.; Tucker, C. *Management Science 65(7): 2966-2981*
  `paper` · `intermediate` · `access: library`
  A gender-neutral STEM job ad was shown to fewer women because younger women are a more expensive audience. Cost-minimizing delivery produced the apparent bias, and the pattern held across platforms.
  *Use in wiki:* Core case for algorithmic bias arising from market mechanics rather than intent, discussed alongside Ali et al. (2019).
  DOI [10.1287/mnsc.2018.3093](https://doi.org/10.1287/mnsc.2018.3093)

- [core] **[Discrimination through optimization: How Facebook's ad delivery can lead to skewed outcomes](https://arxiv.org/abs/1904.02095)** (2019). Ali, M.; Sapiezynski, P.; Bogen, M.; Korolova, A.; Mislove, A.; Rieke, A. *Proceedings of the ACM on Human-Computer Interaction (CSCW 2019); arXiv 1904.02095*
  `paper` · `intermediate` · `access: open` · `AI angle`
  Paired ad experiments show that Facebook's delivery optimization skews employment and housing ads by gender and race even with neutral targeting, driven by budget effects and the platform's predicted relevance of the ad content.
  *Use in wiki:* Pair with Lambrecht and Tucker: one shows a market-cost mechanism, the other a platform-prediction mechanism. Good for a debate on who is accountable.
  DOI [10.1145/3359301](https://doi.org/10.1145/3359301)
  *Note:* The venue (PACM HCI/CSCW) is inferred from the ACM DOI listed on arXiv.

## Ethics and Law: Course Note and Theory

- [core] **[Course note: marketing tactics, consumer harm, and the law (crosswalk for M1-M8)](https://github.com/nene88991999/BADM534-Marketing-Analytics/tree/main/01_Resources/08_M8_Current_Topics_in_Marketing/ethics_and_law)** (2026). Yang, N. (Marketing Analytics course materials)
  `tutorial` · `intro` · `access: open` · `AI angle`
  Twelve tactics (subscription traps, drip pricing, fake reviews, influencer disclosure, manufactured urgency, surveillance pricing, consent and privacy, children, AI claims, discriminatory delivery, green claims, experiments on customers), each mapped to the consumer harm, the US federal, Illinois, other-state, EU and UK law, enforcement cases with amounts and dates, research evidence and a discussion question. Statuses checked 2 Nov 2026. Includes a module-by-module 'ethics and law check', a 75-minute M8 session plan and a project risk-memo assignment; crosswalk.csv carries the table for the wiki.
  *Use in wiki:* The hub for the ethics and regulation thread: link each module page's closing 'ethics and law check' here.
  Local copy: `08_M8_Current_Topics_in_Marketing/ethics_and_law`
  *Note:* Teaching material, not legal advice. Pending items (NY One Fair Price Act, EU Digital Fairness Act, FTC negative-option rulemaking, FTC v. Uber, FTC v. Live Nation) need rechecking each term.

- [core] **[Blind Spot: The Attention Economy and the Law](https://scholarship.law.columbia.edu/faculty_scholarship/2029/)** (2019). Wu, T. *Antitrust Law Journal 82(3): 771*
  `paper` · `intermediate` · `access: open`
  Attention is a scarce resource; 'attention brokers' offer free services and sell access to audiences, and antitrust and consumer-protection authorities have struggled to analyse these markets because users pay no money. Distinguishes voluntary exchange from captive exposure.
  *Use in wiki:* Pre-reading for the M8 session; class point that ad load and interstitial questions are a price paid in time.
  *Note:* Reading available through the linked public source; original local copies are excluded from publication.

- [recommended] **[Sludge Audits](https://doi.org/10.1017/bpp.2019.32)** (2022). Sunstein, C. R. *Behavioural Public Policy 6(4): 654-673*
  `paper` · `intro` · `access: open`
  Proposes that firms and governments assess 'sludge', the frictions (forms, waits, steps) that make beneficial actions harder, and quantify its costs.
  *Use in wiki:* Method for the M8 assessment exercise on a real cancellation flow.

- [recommended] **[Online Manipulation: Hidden Influences in a Digital World](https://georgetownlawtechreview.org/online-manipulation-hidden-influences-in-a-digital-world/GLTR-01-2020/)** (2019). Susser, D.; Roessler, B.; Nissenbaum, H. *Georgetown Law Technology Review 4(1)*
  `paper` · `intermediate` · `access: open`
  Defines manipulation as hidden influence that exploits vulnerabilities and argues it threatens autonomy, distinguishing it from persuasion and coercion.
  *Use in wiki:* Ethics reading for defining what makes a tactic manipulative rather than persuasive.
  *Note:* URL pattern from the journal site; confirm before linking students.

- [recommended] **[The Attention Merchants: The Epic Scramble to Get Inside Our Heads](https://scholarship.law.columbia.edu/books/64/)** (2016). Wu, T. *Knopf*
  `book` · `intro` · `access: paid`
  History of the business model that captures attention with free content and resells it to advertisers, from the penny press to social media, including recurring public revolts when advertising overreaches.
  *Use in wiki:* Opening reading for M8 (or M5); pairs with M6 ad-measurement papers: what exactly is being bought?

- [recommended] **[Digital Market Manipulation](https://www.gwlr.org/wp-content/uploads/2014/10/Calo_82_4.pdf)** (2014). Calo, R. *George Washington Law Review 82(4): 995-1051*
  `paper` · `intermediate` · `access: open`
  Argues that firms' data about consumers and control over digital interfaces let them find and exploit each consumer's biases at the moment of decision, and asks how consumer-protection law should respond.
  *Use in wiki:* Legal-theory reading linking data-driven marketing to manipulation.

- [optional] **[The Age of Extraction](https://www.penguinrandomhouse.com/books/691177/the-age-of-extraction-by-tim-wu/)** (2025). Wu, T. *Knopf*
  `book` · `intro` · `access: paid`
  Argues that a handful of tech platforms, after offering convenience, extract money, data and attention from users and dependent businesses, and proposes ways to restore balance.
  *Use in wiki:* Frame for the junk-fee, marketplace-fee and surveillance-pricing rows of the crosswalk.

- [optional] **[Will Artificial Intelligence Eat the Law? The Rise of Hybrid Social-Ordering Systems](https://columbialawreview.org/content/will-artificial-intelligence-eat-the-law-the-rise-of-hybrid-social-ordering-systems/)** (2019). Wu, T. *Columbia Law Review 119*
  `paper` · `intermediate` · `access: open` · `AI angle`
  Argues that automated decision systems need mechanisms that bring hard cases to human judgment, and warns that a nominal human presence can coexist with disempowerment.
  *Use in wiki:* M7: when a model or AI agent decides refunds, retention offers or prices, who can trigger human review?

- [optional] **[The Crisis of Attention Theft: Ads That Steal Your Time for Nothing in Return](https://www.wired.com/2017/04/forcing-ads-captive-audience-attention-theft-crime/)** (2017). Wu, T. *WIRED*
  `blog` · `intro` · `access: open`
  Short essay on ads forced on captive audiences without consent, a readable version of the voluntary-versus-captive distinction.
  *Use in wiki:* Five-minute pre-reading alternative to Blind Spot.

- [optional] **[Machine Speech](https://scholarship.law.columbia.edu/faculty_scholarship/1833/)** (2013). Wu, T. *University of Pennsylvania Law Review 161*
  `paper` · `advanced` · `access: open`
  When is a computer's output the designer's protected speech and when is it a functional tool? Contrasts recommendations based on a user's recorded choices with those reflecting a programmer's judgments.
  *Use in wiki:* Background for First Amendment arguments against algorithm regulation, e.g. retailers' challenge to New York's algorithmic-pricing disclosure law.

## Ethics and Law: Rules and Enforcement

- [core] **[FTC Negative Option Rule: 2024 amendments (vacated 2025) and advance notice of proposed rulemaking (13 March 2026)](https://www.govinfo.gov/content/pkg/FR-2026-03-13/pdf/2026-04952.pdf)** (2026). Federal Trade Commission. *Federal Register 91(49): 12318-12325*
  `report` · `intermediate` · `access: open`
  The 2024 'click-to-cancel' amendments were vacated by the Eighth Circuit on 8 July 2025 (Custom Communications v. FTC) for skipping a required preliminary regulatory analysis. The March 2026 ANPRM restarts the process and asks whether save offers in place of honouring cancellation are unfair or deceptive, requesting data on acceptance rates, savings, delays and state laws.
  *Use in wiki:* M8 group exercise: draft a comment answering the save-offer question using the consumer-agency assessment design.
  *Note:* 2024 final rule: Federal Register 89(221): 90476-90545 (govinfo FR-2024-11-15). Status pending as of Nov 2026.

- [core] **[State surveillance-pricing bans (Maryland, Connecticut, New Jersey; New York pending)](https://www.route-fifty.com/finance/2026/08/states-begin-banning-surveillance-pricing-uses-personal-data-charge-more/415219/)** (2026). Route Fifty (overview)
  `report` · `intro` · `access: open` · `AI angle`
  Enacted: Maryland HB 895 (grocery stores and delivery apps, in force since 1 October 2026), Connecticut PA 26-130 (retailers broadly, signed June 2026, effective 1 July 2027), New Jersey A4085 (grocery, signed July 2026, effective 1 August 2027). New York's One Fair Price Act (A9349/S8623) passed the legislature on 4 June 2026 and had not been delivered to the Governor by 2 November 2026. Most exempt loyalty programmes, coupons and cost-based differences.
  *Use in wiki:* M7/M8 debate: where is the line between a discount and surveillance pricing?
  *Note:* Fast-moving; recheck each term.

- [core] **[FTC Operation AI Comply and later AI-claims cases (2024-2026)](https://www.beneschlaw.com/insight/one-year-in-ftcs-operation-ai-comply-continues-under-new-administration-signaling-enduring-enforcement-focus/)** (2025). Benesch (summary)
  `report` · `intro` · `access: open` · `AI angle`
  Sweep against deceptive AI claims and AI tools for deception: DoNotPay ('robot lawyer'), Rytr (AI testimonials), AI income schemes (2024); Workado's AI-detector accuracy claims (98% claimed versus about 53% found) and Air AI (2025).
  *Use in wiki:* M7/M8: substantiation applies to model-accuracy claims.

- [core] **[FTC v. Amazon (Prime enrolment and cancellation): $2.5 billion settlement (25 September 2025)](https://www.khlaw.com/insights/amazon-pay-record-25-billion-settle-ftc-claims-deceptive-prime-membership-signup-and)** (2025). Federal Trade Commission
  `case` · `intro` · `access: open`
  ROSCA and FTC Act claims that Amazon enrolled consumers in Prime without consent and made cancellation deliberately hard; $1 billion civil penalty plus $1.5 billion refunds; requires a clear decline option and simple cancellation.
  *Use in wiki:* Lead case for the M8 session: what A/B-test metric produced this flow?

- [core] **[FTC Consumer Reviews and Testimonials Rule, 16 CFR Part 465](https://www.ecfr.gov/current/title-16/part-465)** (2024). Federal Trade Commission
  `documentation` · `intro` · `access: open` · `AI angle`
  Bans fake or AI-fabricated reviews and testimonials, sentiment-conditioned incentives, undisclosed insider reviews, company-controlled 'independent' review sites, review suppression and fake social-media indicators; effective 21 October 2024; civil penalties per violation. Warning letters to ten companies on 22 December 2025.
  *Use in wiki:* M5: the legal line around review mining, generation and moderation.

- [core] **[Bringing Dark Patterns to Light (FTC staff report)](https://www.ftc.gov/system/files/ftc_gov/pdf/P214800%20Dark%20Patterns%20Report%209.14.2022%20-%20FINAL.pdf)** (2022). Federal Trade Commission
  `report` · `intro` · `access: open`
  Catalogues dark patterns (disguised ads, hard cancellation, buried terms, data-grabbing defaults, nagging) and the FTC and state cases brought against them.
  *Use in wiki:* Taxonomy for the M8 assessment exercise.

- [core] **[Restore Online Shoppers' Confidence Act (ROSCA), 15 U.S.C. 8401-8405](https://www.law.cornell.edu/uscode/text/15/chapter-110)** (2010). U.S. Congress
  `documentation` · `intro` · `access: open`
  For online negative-option offers: disclose all material terms before billing, obtain express informed consent, and provide a simple mechanism to stop recurring charges; violations are treated as rule violations with civil penalties.
  *Use in wiki:* The statute behind the Amazon Prime and Uber One cases; M4 retention and subscription pricing.

- [core] **[FTC Act Section 5 (15 U.S.C. 45) and the FTC Policy Statement on Deception](https://www.ftc.gov/legal-library/browse/ftc-policy-statement-deception)** (1983). Federal Trade Commission
  `documentation` · `intro` · `access: open`
  The general US prohibition of unfair or deceptive acts. Deception: a representation or omission likely to mislead a reasonable consumer that is material. Unfairness (15 U.S.C. 45(n)): substantial injury, not reasonably avoidable, not outweighed by benefits. Objective claims require prior substantiation. Since AMG Capital (2021) money comes mainly through rule violations (civil penalties up to $53,088 per violation at 2025 levels, unchanged for 2026).
  *Use in wiki:* Legal backbone slide for M8; the substantiation point for M3 (claims built on regressions).

- [recommended] **[FTC and 21 states v. Uber (Uber One subscription), filed April 2025](https://www.courthousenews.com/judge-allows-most-ftc-claims-against-uber-to-survive/)** (2026). Courthouse News (report)
  `case` · `intro` · `access: open`
  Alleges billing and a cancellation process requiring up to 32 actions; most ROSCA and FTC Act claims survived a motion to dismiss in the Northern District of California (Judge Tigar); 21 states joined in December 2025.
  *Use in wiki:* Pending case to follow during the term.
  *Note:* Pending; check status.

- [recommended] **[FTC v. Live Nation and Ticketmaster (deceptive pricing and resale), C.D. Cal. 2:25-cv-08884](https://www.ticketnews.com/2026/10/ftc-live-nation-ticketmaster-jury-trial/)** (2026). TicketNews (status report)
  `case` · `intro` · `access: open`
  Filed September 2025: advertised prices omitting mandatory fees and tolerance of brokers evading purchase limits (BOTS Act and consumer-protection claims). Motion to dismiss denied September 2026; trial dates proposed for 2028.
  *Use in wiki:* Pending case for the drip-pricing row.
  *Note:* Pending; check status.

- [recommended] **[UK CMA direct consumer enforcement under the DMCC Act (first fines, 2025-2026)](https://www.mayerbrown.com/en/insights/publications/2026/08/were-just-getting-started-the-cmas-new-consumer-enforcement-powers-in-action)** (2026). Mayer Brown (overview)
  `report` · `intro` · `access: open`
  Since April 2025 the CMA can fine up to 10% of global turnover. First consumer-law infringement decisions: AA and BSM driving schools GBP 4.2m (drip pricing), Marks Electrical GBP 720,000 (pre-ticked add-ons) and StubHub GBP 889,200 (hidden mandatory fees), with refunds.
  *Use in wiki:* Comparative enforcement for the drip-pricing row.

- [recommended] **[California Privacy Protection Agency v. Honda: $632,500 (March 2025)](https://www.hunton.com/privacy-and-cybersecurity-law-blog/cppa-fines-honda-632-500-for-ccpa-violations)** (2025). Hunton (summary)
  `case` · `intro` · `access: open`
  First CPPA enforcement decision, including privacy choices not offered symmetrically (CCPA regulations 7004(a)(2)) and excessive verification for opt-outs.
  *Use in wiki:* M2 consent design.

- [recommended] **[COPPA Rule, 16 CFR Part 312 (amended 2025)](https://www.ecfr.gov/current/title-16/part-312)** (2025). Federal Trade Commission
  `documentation` · `intro` · `access: open`
  Children under 13. The 2025 amendments (published 22 April 2025) require separate verifiable parental consent before disclosing children's data to third parties for targeted advertising, limit data retention and add biometric identifiers; compliance was due 22 April 2026.
  *Use in wiki:* M8 children and vulnerable consumers; M2 data collection.

- [recommended] **[European Commission fines X EUR 120 million under the Digital Services Act (5 December 2025)](https://digital-strategy.ec.europa.eu/en/news/commission-fines-x-eu120-million-under-digital-services-act)** (2025). European Commission
  `report` · `intro` · `access: open`
  First DSA non-compliance decision: deceptive design of paid 'verified' blue checkmarks, an inadequate ad repository, and barriers to researcher data access.
  *Use in wiki:* Deceptive interface design as a platform-law violation.

- [recommended] **[FTC Rule on Unfair or Deceptive Fees, 16 CFR Part 464](https://www.ecfr.gov/current/title-16/part-464)** (2025). Federal Trade Commission
  `documentation` · `intro` · `access: open`
  Requires total-price display for live-event tickets and short-term lodging and bars misrepresenting fees; effective 12 May 2025; civil penalties.
  *Use in wiki:* M4 pricing: partitioned prices and what must be shown up front.

- [recommended] **[FTC surveillance pricing 6(b) study: initial findings (January 2025)](https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-surveillance-pricing-study-indicates-wide-range-personal-data-used-set-individualized-consumer)** (2025). Federal Trade Commission
  `report` · `intro` · `access: open` · `AI angle`
  Staff research summaries from orders to intermediaries that sell pricing tools, indicating that a wide range of personal data (location, demographics, browsing and purchase history) is used to set individualised prices.
  *Use in wiki:* Evidence that the M7 pricing models students build are already in commercial use.

- [recommended] **[FTC v. HoYoverse (Genshin Impact): $20 million over loot boxes and children's privacy (January 2025)](https://androidauthority.com/genshin-impact-loot-box-fine-3517760)** (2025). Android Authority (report)
  `case` · `intro` · `access: open`
  COPPA and deception claims about loot-box odds and virtual-currency pricing; bars selling loot boxes to under-16s without parental consent.
  *Use in wiki:* Children and vulnerable consumers row.

- [recommended] **[Minnesota Statutes 325G.58 (permission before retention offers)](https://www.revisor.mn.gov/statutes/cite/325G.58)** (2025). Minnesota Legislature
  `documentation` · `intro` · `access: open`
  After a consumer starts to cancel, the business must ask permission once before presenting retention offers; optional questions about reasons for leaving are allowed.
  *Use in wiki:* The closest existing law to a right to refuse the retention conversation.

- [recommended] **[New York Algorithmic Pricing Disclosure Act, Gen. Bus. Law 349-a](https://www.kelleydrye.com/viewpoints/blogs/ad-law-access/surveillance-pricing-key-concepts-the-current-legal-and-legislative-landscape-and-mounting-scrutiny.md)** (2025). New York Legislature
  `documentation` · `intro` · `access: open` · `AI angle`
  In force since November 2025: prices set by an algorithm using a consumer's personal data must carry the notice 'THIS PRICE WAS SET BY AN ALGORITHM USING YOUR PERSONAL DATA'. A retailers' First Amendment challenge failed in district court; the appeal (NRF v. James) was argued in the Second Circuit on 19 October 2026, decision pending.
  *Use in wiki:* M7 personalised pricing: what triggers the disclosure?
  *Note:* URL is a law-firm overview of the US landscape (April 2026).

- [recommended] **[California Automatic Renewal Law, Bus. & Prof. Code 17602 (AB 2863, operative 1 July 2025)](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240AB2863)** (2024). California Legislature
  `documentation` · `intro` · `access: open`
  Online retention offers are allowed only beside a prominent, continuously displayed cancellation control, and cancellation must be processed promptly when the control is used; also requires express consent and annual reminders.
  *Use in wiki:* Contrast with Minnesota's permission-first rule in the M8 session.

- [recommended] **[EU AI Act (Regulation 2024/1689), Article 5 prohibited practices](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)** (2024). European Parliament and Council
  `documentation` · `intermediate` · `access: open` · `AI angle`
  Since 2 February 2025 bans AI systems that deploy subliminal, manipulative or deceptive techniques, or exploit age, disability or socio-economic vulnerabilities, to materially distort behaviour causing significant harm; fines up to EUR 35 million or 7% of turnover.
  *Use in wiki:* AI-powered persuasion limits for M7/M8.

- [recommended] **[FTC and Illinois Attorney General v. Grubhub: $140 million judgment (December 2024)](https://crowell.com/en/insights/client-alerts/lessons-for-e-commerce-and-retail-from-the-ftc-and-illinois-ags-proposed-dollar140-million-settlement-against-grubhub)** (2024). Crowell & Moring (summary)
  `case` · `intro` · `access: open`
  Hidden fees and other deceptive practices toward diners, restaurants and drivers; $140 million judgment, largely suspended, with $25 million paid; Illinois AG co-plaintiff.
  *Use in wiki:* Illinois example for the drip-pricing row.

- [recommended] **[FTC Guides Concerning Endorsements and Testimonials, 16 CFR Part 255 (2023 revision)](https://www.ecfr.gov/current/title-16/part-255)** (2023). Federal Trade Commission
  `documentation` · `intro` · `access: open`
  Material connections between endorsers and brands (payment, free products, employment) must be clearly disclosed; brands are responsible for their influencers' claims and disclosures.
  *Use in wiki:* M5 influencer marketing.

- [recommended] **[FTC v. Rite Aid: five-year ban on facial recognition (December 2023)](https://www.mayerbrown.com/de/insights/publications/2023/12/more-than-a-ban-on-facial-recognition-use-the-us--ftcs-rite-aid-action-and-proposed-stipulated-order)** (2023). Mayer Brown (summary)
  `case` · `intro` · `access: open` · `AI angle`
  Unfair use of facial-recognition surveillance in stores that produced false matches; five-year ban and algorithmic-fairness obligations.
  *Use in wiki:* M7: biased prediction as an unfair practice.

- [recommended] **[FTC v. Epic Games (Fortnite): $245 million refunds for billing dark patterns plus $275 million COPPA penalty (December 2022)](https://www.pbs.org/newshour/amp/nation/fortnite-maker-epic-games-to-settle-ftc-case-pay-520-million-in-penalties-and-refunds)** (2022). PBS NewsHour (report)
  `case` · `intro` · `access: open`
  Settlements over design tricks that led players, including children, into unintended purchases, and over children's privacy violations; $520 million in total.
  *Use in wiki:* Dark patterns and children rows.

- [recommended] **[FTC v. Fashion Nova: $4.2 million for suppressing negative reviews (2022)](https://www.fox26houston.com/news/fashion-nova-to-pay-4-2m-to-settle-claims-it-blocked-negative-online-reviews)** (2022). FOX 26 Houston (report)
  `case` · `intro` · `access: open`
  Online retailer settled claims that it blocked lower-star reviews from its website.
  *Use in wiki:* Review-suppression example for M5.

- [recommended] **[Illinois Automatic Contract Renewal Act, 815 ILCS 601 (online cancellation since 2022, P.A. 102-0517)](https://ilga.gov/Legislation/publicacts/view/102-0517)** (2022). Illinois General Assembly
  `documentation` · `intro` · `access: open`
  Requires clear disclosure of automatic-renewal terms and renewal notices for longer contracts, and since 1 January 2022 lets consumers who accept online cancel exclusively online.
  *Use in wiki:* Home-state law for any subscription product students analyse.

- [recommended] **[United States v. Meta Platforms (housing-ad delivery), S.D.N.Y. settlement (June 2022)](https://www.justice.gov/crt/case/united-states-v-meta-platforms-inc-fka-facebook-inc-sdny)** (2022). U.S. Department of Justice
  `case` · `intro` · `access: open` · `AI angle`
  Fair Housing Act case over ad targeting and delivery; Meta agreed to retire a lookalike tool for housing ads and build a system to reduce demographic skew in delivery.
  *Use in wiki:* Discriminatory delivery row for M7.

- [recommended] **[Illinois Biometric Information Privacy Act (BIPA), 740 ILCS 14](https://www.ilga.gov/legislation/ilcs/ilcs3.asp?ActID=3004&ChapterID=57)** (2008). Illinois General Assembly
  `documentation` · `intro` · `access: open`
  Written consent before collecting biometric identifiers; private right of action with $1,000 (negligent) or $5,000 (intentional or reckless) per violation; a 2024 amendment counts repeated collection from one person as a single violation.
  *Use in wiki:* M2 data collection: why face, voice and fingerprint data are a litigation risk in Illinois.
  *Note:* Confirm the ILGA ActID link before publishing to students.

- [recommended] **[EU Unfair Commercial Practices Directive 2005/29/EC (with Annex I blacklist)](https://eur-lex.europa.eu/eli/dir/2005/29/oj/eng)** (2005). European Parliament and Council
  `documentation` · `intro` · `access: open`
  Bans misleading and aggressive commercial practices; Annex I lists practices always unfair, including point 7 (falsely claiming very limited availability to rush a decision) and disguised advertising. Amended by Directive 2024/825 (green claims, applies from 27 September 2026).
  *Use in wiki:* European counterpart to FTC Act s5; the urgency row of the crosswalk.

- [optional] **[EU Digital Fairness Act (proposal expected November 2026)](https://eurobytenews.com/article/digital-fairness-act-proposal-due/)** (2026). European Commission
  `report` · `intro` · `access: open`
  Planned EU law on dark patterns, addictive design, unfair personalisation, influencer marketing, price presentation and hard-to-cancel subscriptions, with a focus on minors; proposal expected mid-November 2026.
  *Use in wiki:* Watch item for the M8 session.
  *Note:* Not yet published on 2 Nov 2026; replace with the Commission's proposal when available.

- [optional] **[Trump v. Slaughter (U.S. Supreme Court, 29 June 2026)](https://www.venable.com/insights/publications/2026/06/supreme-court-overrules-humphreys-executor)** (2026). Venable (summary)
  `case` · `intro` · `access: open`
  6-3 decision overruling Humphrey's Executor: the President may remove FTC commissioners at will, putting federal enforcement priorities under presidential direction.
  *Use in wiki:* Context for why state AGs and private plaintiffs matter more.

- [optional] **[Executive Order 14036, Promoting Competition in the American Economy (2021; revoked 2025)](https://en.wikipedia.org/wiki/Executive_Order_14036)** (2021). The White House
  `report` · `intro` · `access: open`
  Signed 9 July 2021; a whole-of-government competition agenda covering, among other things, right to repair, non-competes and telecom fees; Tim Wu helped draft and implement it at the National Economic Council. Revoked 13 August 2025 by Executive Order 14337.
  *Use in wiki:* Policy-history example of how fast the federal map changes; links right to repair to the McBroken lab.

## Ethics and Law: Evidence on Consumer Harm

- [core] **[Selling Subscriptions](https://doi.org/10.1257/aer.20231612)** (2025). Einav, L.; Klopack, B.; Mahoney, N. *American Economic Review 115(5): 1650-1671*
  `paper` · `intermediate` · `access: open`
  Card-transaction data on subscription payments and a model of passive renewal: cancellation frictions roughly double seller revenue on average, holding initial subscribers fixed.
  *Use in wiki:* Quantifies the subscription-trap row; pairs with Egan et al. in the genAI lab.

- [core] **[Personalized Pricing and Consumer Welfare](https://doi.org/10.1086/720793)** (2023). Dube, J.-P.; Misra, S. *Journal of Political Economy 131(1): 131-189*
  `paper` · `intermediate` · `access: open`
  Field experiments and machine learning at a digital firm: personalised pricing raises profit substantially versus uniform optimal pricing; most consumers face lower prices, though total consumer surplus falls modestly.
  *Use in wiki:* Evidence base for the surveillance-pricing debate (M7).

- [core] **[Sophisticated Consumers with Inertia: Long-Term Implications from a Large-Scale Field Experiment](https://bfi.uchicago.edu/working-paper/sophisticated-consumers-with-inertia-long-term-implications-from-a-large-scale-field-experiment/)** (2023). Miller, K.; Sahni, N. S.; Strulov-Shlain, A. *Working paper (Becker Friedman Institute)*
  `paper` · `intermediate` · `access: open`
  Large field experiment randomising auto-renewal: auto-renewal raises short-run revenue through inertia, but many consumers anticipate their inertia and decline auto-renewal offers or delay subscribing; after a year revenue is about equal and auto-renewal has fewer subscribers.
  *Use in wiki:* Shows the business case against subscription traps (M4 CLV, M6).

- [core] **[Price Salience and Product Choice](https://doi.org/10.1287/mksc.2020.1261)** (2021). Blake, T.; Moshary, S.; Sweeney, K.; Tadelis, S. *Marketing Science 40(4): 619-636*
  `paper` · `intermediate` · `access: open`
  StubHub experiment: showing fees only at checkout ('back-end' fees) raised spending and the probability of purchase relative to all-in prices.
  *Use in wiki:* Field-experiment evidence for the drip-pricing row (M4/M6).

- [core] **[Shining a Light on Dark Patterns](https://academic.oup.com/jla/article/13/1/43/6180579)** (2021). Luguri, J.; Strahilevitz, L. J. *Journal of Legal Analysis 13(1): 43-109*
  `paper` · `intermediate` · `access: open`
  Experiments on a national sample: mild dark patterns roughly doubled acceptance of a dubious data-protection subscription and aggressive ones nearly quadrupled it, with less-educated participants more affected; discusses how existing law applies.
  *Use in wiki:* Effect sizes for the M8 session; experimental design example for M6.

- [core] **[Dark Patterns at Scale: Findings from a Crawl of 11K Shopping Websites](https://doi.org/10.1145/3359183)** (2019). Mathur, A.; Acar, G.; Friedman, M. J.; Lucherini, E.; Mayer, J.; Chetty, M.; Narayanan, A. *Proceedings of the ACM on Human-Computer Interaction 3 (CSCW)*
  `paper` · `intermediate` · `access: open`
  Automated crawl of about 11,000 shopping sites finding 1,818 dark-pattern instances, including fake countdown timers, fake scarcity and activity messages, and the third parties supplying them.
  *Use in wiki:* Measurement method students can replicate on a small scale (M2 scraping, M5 text classification).

- [recommended] **[Algorithmic Pricing and Competition: Empirical Evidence from the German Retail Gasoline Market](https://doi.org/10.1086/726906)** (2024). Assad, S.; Clark, R.; Ershov, D.; Xu, L. *Journal of Political Economy 132(3): 723-771*
  `paper` · `intermediate` · `access: open`
  Adoption of algorithmic pricing software raised margins, mainly when both stations in a local duopoly adopted.
  *Use in wiki:* Empirical counterpart to Calvano et al.

- [recommended] **[Examining the Efficacy of Time Scarcity Marketing Promotions in Online Retail](https://doi.org/10.1177/00222437221118856)** (2023). Hmurovic, J.; Lamberton, C.; Goldsmith, K. *Journal of Marketing Research 60(2): 299-328*
  `paper` · `intermediate` · `access: open`
  Field and lab evidence that time-limited promotions online have mixed effects on sales, depending on how much time remains and how consumers interpret the deadline.
  *Use in wiki:* Evidence for the manufactured-urgency row.

- [recommended] **[Privacy and Market Concentration: Intended and Unintended Consequences of the GDPR](https://doi.org/10.1287/mnsc.2023.4709)** (2023). Johnson, G. A.; Shriver, S. K.; Goldberg, S. G. *Management Science 69(10): 5695-5721*
  `paper` · `intermediate` · `access: open`
  The GDPR reduced websites' use of web technology vendors and increased vendor market concentration, benefiting large vendors such as Google.
  *Use in wiki:* Unintended effects of regulation (M8 debate balance).

- [recommended] **[The Effect of Privacy Regulation on the Data Industry: Empirical Evidence from GDPR](https://doi.org/10.1111/1756-2171.12455)** (2023). Aridor, G.; Che, Y.-K.; Salz, T. *RAND Journal of Economics 54(4): 695-730*
  `paper` · `intermediate` · `access: open`
  GDPR opt-outs cut recorded consumers by about 12.5%, while the remaining consumers became more trackable and more valuable to advertisers.
  *Use in wiki:* Shows how consent rules change the data students will analyse.

- [recommended] **[Consumer Reactions to Drip Pricing](https://doi.org/10.1287/mksc.2019.1207)** (2020). Santana, S.; Dallas, S. K.; Morwitz, V. G. *Marketing Science 39(1): 188-210*
  `paper` · `intermediate` · `access: open`
  Experiments showing drip pricing raises initial choice of the dripped option but can trigger feelings of deception and backlash once fees appear.
  *Use in wiki:* Consumer-behaviour complement to Blake et al.

- [recommended] **[Dark Patterns after the GDPR: Scraping Consent Pop-ups and Demonstrating their Influence](https://doi.org/10.1145/3313831.3376321)** (2020). Nouwens, M.; Liccardi, I.; Veale, M.; Karger, D.; Kagal, L. *CHI 2020*
  `paper` · `intermediate` · `access: open`
  Scrapes consent banners on top UK sites (few meet minimum legal requirements) and shows experimentally that removing a reject button on the first page and adding granular options sharply changes consent rates.
  *Use in wiki:* M2 consent design; replicable scraping exercise.

- [recommended] **[The Effects of Influencer Advertising Disclosure Regulations: Evidence from Instagram](https://doi.org/10.1145/3391403.3399477)** (2020). Ershov, D.; Mitchell, M. *EC '20: Proceedings of the 21st ACM Conference on Economics and Computation*
  `paper` · `intermediate` · `access: open`
  Uses a German disclosure regulation to study how mandated sponsorship labels change influencer posting and engagement.
  *Use in wiki:* M5 influencer disclosure row.

- [recommended] **[Discrimination through Optimization: How Facebook's Ad Delivery Can Lead to Biased Outcomes](https://doi.org/10.1145/3359301)** (2019). Ali, M.; Sapiezynski, P.; Bogen, M.; Korolova, A.; Mislove, A.; Rieke, A. *Proceedings of the ACM on Human-Computer Interaction 3 (CSCW)*
  `paper` · `intermediate` · `access: open`
  Controlled ad campaigns show Facebook's delivery skewed by gender and race based on ad content and images even with neutral targeting.
  *Use in wiki:* M7 discriminatory delivery row.

- [recommended] **[Objecting to Experiments that Compare Two Unobjectionable Policies or Treatments](https://doi.org/10.1073/pnas.1820701116)** (2019). Meyer, M. N.; Heck, P. R.; Holtzman, G. S.; et al. *Proceedings of the National Academy of Sciences 116(22): 10723-10728*
  `paper` · `intermediate` · `access: open`
  People often judge an A/B test comparing two acceptable policies as less appropriate than implementing either policy untested (the 'A/B effect').
  *Use in wiki:* M6 ethics of experimenting on customers.

- [recommended] **[Demand for 'Healthy' Products: False Claims and FTC Regulation](https://doi.org/10.1509/jmr.15.0398)** (2017). Rao, A.; Wang, E. *Journal of Marketing Research 54(6): 968-989*
  `paper` · `intermediate` · `access: open`
  Uses FTC actions against false health claims to estimate how much those claims had raised demand and what happened after correction.
  *Use in wiki:* Quantitative-marketing model of regulation's effect on demand (M3/M8).

- [recommended] **[Fake It Till You Make It: Reputation, Competition, and Yelp Review Fraud](https://doi.org/10.1287/mnsc.2015.2304)** (2016). Luca, M.; Zervas, G. *Management Science 62(12): 3412-3427*
  `paper` · `intermediate` · `access: open`
  Using Yelp's filtered reviews, finds restaurants commit more positive review fraud when their reputation is weak and more negative fraud against rivals when competition is close.
  *Use in wiki:* M5 fake-review incentives.

- [recommended] **[Promotional Reviews: An Empirical Investigation of Online Review Manipulation](https://doi.org/10.1257/aer.104.8.2421)** (2014). Mayzlin, D.; Dover, Y.; Chevalier, J. *American Economic Review 104(8): 2421-2455*
  `paper` · `intermediate` · `access: open`
  Compares TripAdvisor (anyone can post) with Expedia (verified stays): independent hotels near competitors show more suspicious positive reviews and their neighbours more negative ones.
  *Use in wiki:* Classic identification strategy for M5.

- [recommended] **[Paying Not to Go to the Gym](https://doi.org/10.1257/aer.96.3.694)** (2006). DellaVigna, S.; Malmendier, U. *American Economic Review 96(3): 694-719*
  `paper` · `intermediate` · `access: open`
  Gym members choosing flat-rate contracts pay more per visit than pay-per-visit would cost and are slow to cancel automatically renewing contracts, consistent with overconfidence about future attendance.
  *Use in wiki:* Classic behavioural evidence behind subscription design.

- [recommended] **[Shrouded Attributes, Consumer Myopia, and Information Suppression in Competitive Markets](https://doi.org/10.1162/qjec.2006.121.2.505)** (2006). Gabaix, X.; Laibson, D. *Quarterly Journal of Economics 121(2): 505-540*
  `paper` · `intermediate` · `access: open`
  Shows why firms may hide add-on prices even under competition when some consumers are myopic: unshrouding educates customers who then avoid the add-on.
  *Use in wiki:* Theory for the drip-pricing row.

## Industry Reports

- [core] **[The state of AI in 2026: On the road to ROI](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai)** (2026). Tinkoff, D.; Van der Veken, L.; Chui, M.; Balakrishnan, T. (McKinsey / QuantumBlack). *McKinsey & Company (August 25, 2026)*
  `report` · `intro` · `access: open` · `AI angle`
  McKinsey's annual global AI survey. Agent scaling is concentrated in large firms (40% vs 22%), consumer and retail firms most often use agents in marketing and sales, and marketing and sales is where respondents most often report AI-driven revenue gains.
  *Use in wiki:* Opening reading for M8 with stats for the 'AI in marketing practice' slide. A 31-page PDF is downloadable.
  *Note:* The 2025 edition is listed on the same page as a previous report. For a value estimate, see McKinsey (2023) 'The economic potential of generative AI' (verified): marketing productivity gains of 5-15% of marketing spend.

- [recommended] **[Anthropic Economic Index](https://www.anthropic.com/economic-index)** (2026). Anthropic. *anthropic.com; Hugging Face (Anthropic/EconomicIndex)*
  `dataset` · `intermediate` · `access: open` · `Data CC-BY; code MIT (per dataset card)` · `AI angle`
  Privacy-preserving data on how people use Claude across occupations (O*NET tasks), US states and countries, including automation-vs-augmentation shares. Releases run from February 2025 to June 2026.
  *Use in wiki:* Real dataset for a short in-class exercise on which marketing and sales tasks are being automated vs augmented, using the M2 visualization tools.
  [Open-access copy](https://huggingface.co/datasets/Anthropic/EconomicIndex) · Tools: pandas, datasets
  *Note:* The full HF dataset is 763 MB, so download only the needed release folder (for example 2026-06-26). The main page was last updated June 26, 2026.

- [recommended] **[Exploring Strategic Insights From Gartner's 2026 CMO Spend Survey (webinar)](https://www.gartner.com/en/marketing/research/annual-cmo-spend-survey-research)** (2026). Gartner. *Gartner for Marketing*
  `report` · `intro` · `access: free-registration`
  Gartner's annual survey of CMO budgets: how 2026 budgets are shifting across channels and programs, and how AI is changing marketing capabilities and investment.
  *Use in wiki:* Budget benchmark (marketing spend as a share of revenue, channel mix) for the opening of M8. The instructor can watch it and pull two or three headline numbers.
  *Note:* The public page is a free on-demand webinar (work email registration). The full survey report is usually for Gartner clients only. No headline numbers were visible on the page.

- [recommended] **[The 2026 AI Index Report](https://hai.stanford.edu/ai-index/2026-ai-index-report)** (2026). Stanford Institute for Human-Centered AI (HAI). *Stanford HAI*
  `report` · `intro` · `access: open` · `AI angle`
  Annual data-driven report on AI in nine chapters: R&D, technical performance, responsible AI, economy, science, medicine, education, policy and public opinion. It links a full PDF and public data.
  *Use in wiki:* Use the Economy and Public Opinion chapters for M8, and the public data folder as an M2 visualization exercise dataset.
  *Note:* The release date and license were not stated on the page. The data is on a public Google Drive folder.

## Staying Current: Newsletters and Podcasts

- [core] **[One Useful Thing](https://www.oneusefulthing.org/)** (2026). Mollick, E. *Substack*
  `newsletter` · `intro` · `access: open` · `AI angle`
  Ethan Mollick's newsletter on the practical implications of AI for work and education (488K+ subscribers), with frequent hands-on comparisons of frontier models.
  *Use in wiki:* Weekly 'stay current' link on the wiki. Individual posts work as short discussion readings on AI-assisted analysis.
  *Note:* Free or paid status was not stated on the page. Most posts are free.

- [recommended] **[AdExchanger (AdExchanger Daily newsletter; AdExchanger Talks podcast)](https://www.adexchanger.com/)** (2026). AdExchanger. *adexchanger.com*
  `newsletter` · `intermediate` · `access: freemium`
  News and analysis on data-driven marketing: privacy, measurement, commerce and retail media, and ad tech, with a free weekday newsletter and podcasts (AdExchanger Talks, The Big Story, Inside the Stack).
  *Use in wiki:* Best single feed for following cookies, clean rooms, MMM and retail media during the semester.
  *Note:* Some articles may be paywalled. Marketing Brew (marketingbrew.com, Morning Brew, weekday newsletter; verified) is a lighter, free alternative.

- [recommended] **[Simon Willison's Weblog](https://simonwillison.net/)** (2026). Willison, S. *simonwillison.net*
  `blog` · `intermediate` · `access: open` · `AI angle`
  Very frequent, hands-on posts on new LLM releases, coding agents, 'vibe coding', prompt injection and security, and practical tools (LLM CLI, Datasette).
  *Use in wiki:* The go-to 'staying current' source for the course's AI-assisted coding emphasis, and for spotting agent failure modes and security risks.
  Tools: llm, datasette
  *Note:* The blog is free. A $10/month curated email briefing is optional.

- [recommended] **[The Artificial Intelligence Show](https://podcast.smarterx.ai/)** (2026). Roetzer, P.; Kaput, M. (Marketing AI Institute / SmarterX). *podcast.smarterx.ai*
  `podcast` · `intro` · `access: open` · `AI angle`
  A weekly (Tuesday) podcast, started in 2021 by the Marketing AI Institute founders, covering AI news and practical guidance for marketers and business careers.
  *Use in wiki:* Optional weekly listening, and students can pick an episode to summarize in a short reflection.
  *Note:* marketingaiinstitute.com/podcast-showcase now redirects to podcast.smarterx.ai.

## Python for Marketing Analytics: Notebooks and Code

- [core] **[Gemini API Cookbook: Market a Jet Backpack, JSON sentiment and classification, embeddings classification and clustering](https://github.com/google-gemini/cookbook)** (2026). Google (google-gemini). *GitHub (google-gemini/cookbook)*
  `notebook` · `intro` · `access: open` · `Apache-2.0` · `AI angle`
  Short Colab notebooks on the free-tier Gemini API key. They turn a product sketch into a marketing campaign with JSON taglines, run sentiment analysis, text classification, entity extraction and summarization with JSON output, and classify and cluster text with embeddings.
  *Use in wiki:* First GenAI-for-marketing lab, because it runs in Colab with a free API key and no cloud project. The Jet Backpack notebook is a ready 'AI creative brief' exercise.
  Tools: google-genai, pandas, scikit-learn · Local copy: `08_M8_Current_Topics_in_Marketing/repos/google-gemini__cookbook`
  *Note:* Last commit 2026-10-19. Model names in notebooks change often; tell students to update the model ID. quickstarts/Get_started.ipynb (5.4 MB) is left out to stay lean.

- [recommended] **[Copycat: AI-generated Google Search ad copy that matches your brand style](https://github.com/google-marketing-solutions/copycat)** (2026). Google Marketing Solutions. *GitHub (google-marketing-solutions/copycat)*
  `tool` · `intermediate` · `access: open` · `Apache-2.0` · `AI angle`
  Python package and Colabs (Python quickstart and a GUI) that learn brand style from existing high-performing Responsive Search Ads and generate new headlines and descriptions for new keywords with Gemini. Gemini first drafts a brand style guide from the exemplar ads (optionally from brand-guideline PDFs), which the user can edit before ads are generated.
  *Use in wiki:* Hands-on M8 case: generate RSAs with Copycat, then design a FeedX-style or A/B test to measure whether AI copy beats human copy.
  Tools: gtech-copycat, google-genai, pandas · Local copy: `08_M8_Current_Topics_in_Marketing/repos/google-marketing-solutions__copycat`
  *Note:* Last commit 2026-09-24. Needs Python 3.10 or later and Gemini API or Vertex credentials. The org (150 repos) also has feedgen (LLM feed optimization, Apps Script), vigenair (video ad recrafting) and adspace_agent (an ADK agent for Google Ads planning, 2026), but none has Python teaching notebooks.

- [recommended] **[Google Cloud generative-ai repo: creative content generation, product attribute extraction, multimodal sentiment, AI-assisted data science](https://github.com/GoogleCloudPlatform/generative-ai)** (2026). Google Cloud. *GitHub (GoogleCloudPlatform/generative-ai)*
  `notebook` · `intermediate` · `access: open` · `Apache-2.0` · `AI angle`
  Vertex AI notebooks: marketing creative content generation with Gemini and Imagen, product attribute extraction from images (self-correcting prompts), multimodal retail recommendations, location strategy, multimodal sentiment (audio vs transcript), YouTube video analysis, and a Gemini-assisted data science workflow in BigQuery that ends in customer segments.
  *Use in wiki:* M8 demos of GenAI across the marketing funnel. ai-assisted-data-science is a direct example of the course's AI-assisted analytics theme.
  Tools: google-genai, vertex-ai, bigquery, imagen · Local copy: `08_M8_Current_Topics_in_Marketing/repos/GoogleCloudPlatform__generative-ai`
  *Note:* Last commit 2026-10-22. Most notebooks need a GCP project with Vertex AI and billing, unlike the Gemini cookbook. The related repo GoogleCloudPlatform/genai-for-marketing (Apache-2.0, last commit 2026-01-05) has a notebooks/ folder, but several notebooks target retired PaLM/bison models, so it was left out.

- [recommended] **[Semantic-Similarity Rating (SSR): mapping LLM free-text answers to Likert purchase-intent distributions](https://github.com/pymc-labs/semantic-similarity-rating)** (2025). Maier, B. F.; Aslak, U.; Fiaschi, L.; Rismal, N.; Fletcher, K.; Luhmann, C. C.; Dow, R.; Pappas, K.; Wiecki, T. V. (PyMC Labs). *GitHub (pymc-labs/semantic-similarity-rating); paper arXiv:2510.08338*
  `package` · `advanced` · `access: open` · `Apache-2.0` · `AI angle`
  Package implementing SSR. LLM 'synthetic consumers' answer purchase-intent questions in free text, and the answers are mapped to Likert probability distributions by embedding similarity to anchor statements. The paper is 'LLMs Reproduce Human Purchase Intent via Semantic Similarity Elicitation of Likert Ratings'.
  *Use in wiki:* Current-topics case on LLM-based market research: students simulate concept-test responses, compare direct numeric ratings with SSR, and discuss validity limits.
  [Open-access copy](https://arxiv.org/abs/2510.08338) · Tools: semantic-similarity-rating, polars, numpy, embeddings API · Local copy: `04_M4_Conjoint_Segmentation_CLV/repos/pymc-labs__semantic-similarity-rating`
  *Note:* Last commit 2026-06-04. No notebook; the README quick start is the example. The arXiv page does not link the repo; I matched them through the README's paper title (the README calls it 'Measuring Synthetic Consumer Purchase Intent Using Semantic-Similarity Ratings' (2025), close to the arXiv title, so treat the match as likely but not confirmed). pixi.lock (about 0.5 MB) is excluded.

- [optional] **[Awesome Marketing Science (curated list)](https://github.com/shakostats/Awesome-Marketing-Science)** (2026). shakostats. *GitHub*
  `website` · `intermediate` · `access: open` · `MIT`
  Maintained link list of marketing-measurement resources (geo experiments, MMM, multi-touch attribution, causal inference) from a practitioner.
  *Use in wiki:* Instructor index for M8 updates and for finding student project ideas.
  Local copy: `21_Open_Textbooks_and_Courses/repos/shakostats__Awesome-Marketing-Science`
  *Note:* README only (pushed 2026-05). vkoul/awesome-Marketing-Analytics is a similar list with no license, so this one is preferred.

- [optional] **[Build a Marketing Mix Model with Claude Code: From OLS to Bayesian (workshop)](https://maven.com/pinemarsh/build-a-marketing-mix-model-with-claude-code)** (2026). Diaz-Bérrio, G. *Maven*
  `course` · `intermediate` · `access: paid` · `AI angle`
  One-day workshop by the author of Packt's Data Analytics for Marketing: set up Claude Code with CLAUDE.md, agentic EDA, OLS MMM with adstock and saturation, Bayesian MMM in PyMC, and packaging the pipeline as a reusable SKILL.md.
  *Use in wiki:* Design template for an M8 'vibe-coding an MMM' activity (CLAUDE.md, then EDA, OLS, Bayesian, Skill) built on open data and the downloadable Packt DAM ch12 notebook.
  Tools: claude-code, pymc, pandas
  *Note:* Paid. No date, price or GitHub repo given on the page. Two related free lesson recordings are offered.

- [optional] **[markov-chain-attribution: first-order Markov chain attribution in Python](https://github.com/jerednel/markov-chain-attribution)** (2026). jerednel (GitHub). *GitHub / PyPI (markov-model-attribution)*
  `package` · `intermediate` · `access: open` · `MIT`
  Small package computing Markov-chain removal effects and fractional conversions per channel, with last-touch comparison, from 'start > ... > conv/null' path strings. Based on Anderl et al.'s graph-based attribution framework.
  *Use in wiki:* Compact attribution demo for M8: compare last-touch and Markov credit on toy paths, then on Packt DAM ch11 data.
  Tools: pandas, markov-model-attribution
  *Note:* Proof of concept. The README says to use v0.4 or later (earlier versions could give negative conversions). No notebook, only a README example.

- [optional] **[Digital-Marketing-Analytics: INFO7374 course assignments and Olist project](https://github.com/Nikhilkohli1/Digital-Marketing-Analytics)** (2020). Kohli, N. (Nikhilkohli1). *GitHub (Northeastern INFO7374 coursework)*
  `notebook` · `intermediate` · `access: open`
  Second most-starred rfm-analysis repo: assignments on a VistaPrint marketing mix, an e-commerce dashboard, promotions and adstock, attribution and budget optimization, xDeepFM/Customer2Vec recommendations, and an Olist RFM/segmentation project with Streamlit and Tableau dashboards.
  *Use in wiki:* Shows what a strong semester team project plus GitHub portfolio can look like; link from the project-guidelines page.
  Tools: pandas, scikit-learn, streamlit, tableau
  *Note:* No license, so link only. Last push 2020.

## Data Artifacts and Research Independence

- [recommended] **[Data and Code Availability Policy](https://www.aeaweb.org/journals/data/data-code-policy)** (2026). American Economic Association
  `reading` · `advanced` · `access: linked; see source assessment`
  Documented restricted access can coexist with publication; policy compliance and independent empirical verification remain different assessments.
  *Use in wiki:* Connect data creation and governed use to the reasons owed to affected people; compare confidentiality, publication independence, and refusal of unacceptable terms.
  *Note:* Detailed source record in 01_Resources/45_Data_Truth_and_Norms/catalog.json. Original source copies are excluded from publication.

- [recommended] **[Public Artifacts, Intentions and Norms](https://www.amiethomasson.org/_files/ugd/63fc8a_840cc91860474dfa99802928543989fb.doc)** (2014). Amie L. Thomasson
  `reading` · `advanced` · `access: linked; see source assessment`
  Public artifacts can involve structural, perceptual, receptive, and normative features. A billing record is designed for a practice whose purposes and recognized uses deserve examination.
  *Use in wiki:* Connect data creation and governed use to the reasons owed to affected people; compare confidentiality, publication independence, and refusal of unacceptable terms.
  *Note:* Detailed source record in 01_Resources/45_Data_Truth_and_Norms/catalog.json. Original source copies are excluded from publication.

- [recommended] **[Academic Medical Centers’ Standards for Clinical-Trial Agreements with Industry](https://doi.org/10.1056/NEJMsa044115)** (2005). Michelle M. Mello; Brian R. Clarridge; David M. Studdert
  `reading` · `advanced` · `access: linked; see source assessment`
  Contracts can allocate control over research and publication; the clinical-research survey supplies no prevalence estimate for marketing NDAs.
  *Use in wiki:* Connect data creation and governed use to the reasons owed to affected people; compare confidentiality, publication independence, and refusal of unacceptable terms.
  *Note:* Detailed source record in 01_Resources/45_Data_Truth_and_Norms/catalog.json. Original source copies are excluded from publication.

- [recommended] **[Realism and Human Kinds](https://doi.org/10.1111/j.1933-1592.2003.tb00309.x)** (2003). Amie L. Thomasson
  `reading` · `advanced` · `access: linked; see source assessment`
  Use origin, intended features, and success conditions to distinguish a created dataset from the truth of claims made with it.
  *Use in wiki:* Connect data creation and governed use to the reasons owed to affected people; compare confidentiality, publication independence, and refusal of unacceptable terms.
  *Note:* Detailed source record in 01_Resources/45_Data_Truth_and_Norms/catalog.json. Original source copies are excluded from publication.

- [recommended] **[Fiction and Metaphysics](https://www.cambridge.org/core/books/abs/fiction-and-metaphysics/fictional-characters-as-abstract-artifacts/CE4968D080D4B81C9DE76FF589C70017)** (1999). Amie L. Thomasson
  `reading` · `advanced` · `access: linked; see source assessment`
  Fictional characters depend on creative acts and literary practices. The course applies the questions of origin, persistence, and identity to datasets, while distinguishing records from the people and events they represent.
  *Use in wiki:* Connect data creation and governed use to the reasons owed to affected people; compare confidentiality, publication independence, and refusal of unacceptable terms.
  *Note:* Detailed source record in 01_Resources/45_Data_Truth_and_Norms/catalog.json. Original source copies are excluded from publication.

- [recommended] **[Disclosure of Financial and Non-Financial Relationships and Activities, and Conflicts of Interest](https://www.icmje.org/recommendations/browse/roles-and-responsibilities/author-responsibilities--conflicts-of-interest.html)** (n.d.). International Committee of Medical Journal Editors
  `reading` · `advanced` · `access: linked; see source assessment`
  A professional benchmark for assessing independence. Scope is medical-journal recommendations, with application to marketing presented as a normative comparison.
  *Use in wiki:* Connect data creation and governed use to the reasons owed to affected people; compare confidentiality, publication independence, and refusal of unacceptable terms.
  *Note:* Detailed source record in 01_Resources/45_Data_Truth_and_Norms/catalog.json. Original source copies are excluded from publication.

## Data Poisoning and Measurement Integrity

- [optional] **[Scaling Trends for Data Poisoning in LLMs](https://ojs.aaai.org/index.php/AAAI/article/view/34929)** (2025). Bowen, D.; et al. *Proceedings of the AAAI Conference on Artificial Intelligence 39*
  `paper` · `advanced` · `access: open` · `AI angle`
  Shows that larger language models learn harmful behavior from small amounts of poisoned fine-tuning data more quickly than smaller ones, so scale does not protect against data poisoning.
  *Use in wiki:* Background for an M8 discussion of poisoned online data (e.g., coordinated reviews or synthetic posts) feeding marketing models and AI assistants.
  [Open-access copy](https://arxiv.org/abs/2408.02946)
  *Note:* Also on the MBA 542 Module 8 reading list.

## AI-Assisted Coding Applications

Resources in this folder that show the method done with AI help, LLM versions of the method, or documented failure modes of AI-written analysis:

- [Census Business Trends and Outlook Survey (BTOS): biweekly AI use by US businesses](https://www.census.gov/hfp/btos/data)
- [Competition in Generative AI: Evidence from Consumer Demand](https://www.nber.org/papers/w35953)
- [Course note: marketing tactics, consumer harm, and the law (crosswalk for M1-M8)](https://github.com/nene88991999/BADM534-Marketing-Analytics/tree/main/01_Resources/08_M8_Current_Topics_in_Marketing/ethics_and_law)
- [Gemini API Cookbook: Market a Jet Backpack, JSON sentiment and classification, embeddings classification and clustering](https://github.com/google-gemini/cookbook)
- [Generative-AI Demand: Public Signals and a Synthetic Subscription Panel](https://github.com/nene88991999/BADM534-Marketing-Analytics/tree/main/01_Resources/08_M8_Current_Topics_in_Marketing/genai_demand_lab)
- [One Useful Thing](https://www.oneusefulthing.org/)
- [State surveillance-pricing bans (Maryland, Connecticut, New Jersey; New York pending)](https://www.route-fifty.com/finance/2026/08/states-begin-banning-surveillance-pricing-uses-personal-data-charge-more/415219/)
- [The state of AI in 2026: On the road to ROI](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai)
- [Buy it in ChatGPT: Instant Checkout and the Agentic Commerce Protocol](https://openai.com/index/buy-it-in-chatgpt/)
- [FTC Operation AI Comply and later AI-claims cases (2024-2026)](https://www.beneschlaw.com/insight/one-year-in-ftcs-operation-ai-comply-continues-under-new-administration-signaling-enduring-enforcement-focus/)
- [FTC Consumer Reviews and Testimonials Rule, 16 CFR Part 465](https://www.ecfr.gov/current/title-16/part-465)
- [GEO: Generative Engine Optimization](https://arxiv.org/abs/2311.09735)
- [Discrimination through optimization: How Facebook's ad delivery can lead to skewed outcomes](https://arxiv.org/abs/1904.02095)
- [Anthropic Economic Index](https://www.anthropic.com/economic-index)
- [Copycat: AI-generated Google Search ad copy that matches your brand style](https://github.com/google-marketing-solutions/copycat)
- [Google Cloud generative-ai repo: creative content generation, product attribute extraction, multimodal sentiment, AI-assisted data science](https://github.com/GoogleCloudPlatform/generative-ai)
- [Monitoring AI Adoption in the US Economy](https://www.federalreserve.gov/econres/notes/feds-notes/monitoring-ai-adoption-in-the-u-s-economy-20260403.html)
- [Ramp AI Index: monthly paid-AI adoption by US businesses, by vendor](https://ramp.com/data/ai-index)
- [Simon Willison's Weblog](https://simonwillison.net/)
- [The 2026 AI Index Report](https://hai.stanford.edu/ai-index/2026-ai-index-report)
- [The Artificial Intelligence Show](https://podcast.smarterx.ai/)
- [Demand for LLMs: Descriptive Evidence on Substitution, Market Expansion, and Multihoming](https://arxiv.org/abs/2504.15440)
- [FTC surveillance pricing 6(b) study: initial findings (January 2025)](https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-surveillance-pricing-study-indicates-wide-range-personal-data-used-set-individualized-consumer)
- [New York Algorithmic Pricing Disclosure Act, Gen. Bus. Law 349-a](https://www.kelleydrye.com/viewpoints/blogs/ad-law-access/surveillance-pricing-key-concepts-the-current-legal-and-legislative-landscape-and-mounting-scrutiny.md)
- [Powering AI commerce with the new Agent Payments Protocol (AP2)](https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol)
- [Semantic-Similarity Rating (SSR): mapping LLM free-text answers to Likert purchase-intent distributions](https://github.com/pymc-labs/semantic-similarity-rating)
- [When AI Guides the Shopping Journey](https://www.iab.com/insights/when-ai-guides-the-shopping-journey/)
- [EU AI Act (Regulation 2024/1689), Article 5 prohibited practices](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- [FTC v. Rite Aid: five-year ban on facial recognition (December 2023)](https://www.mayerbrown.com/de/insights/publications/2023/12/more-than-a-ban-on-facial-recognition-use-the-us--ftcs-rite-aid-action-and-proposed-stipulated-order)
- [Frontiers: Supporting Content Marketing with Natural Language Generation](https://ideas.repec.org/a/inm/ormksc/v41y2022i3p441-452.html)
- [United States v. Meta Platforms (housing-ad delivery), S.D.N.Y. settlement (June 2022)](https://www.justice.gov/crt/case/united-states-v-meta-platforms-inc-fka-facebook-inc-sdny)
- [Artificial Intelligence, Algorithmic Pricing, and Collusion](https://www.aeaweb.org/articles?id=10.1257/aer.20190623)
- [Build a Marketing Mix Model with Claude Code: From OLS to Bayesian (workshop)](https://maven.com/pinemarsh/build-a-marketing-mix-model-with-claude-code)
- [Cloudflare Radar API: Internet services ranking (including a Generative AI category)](https://developers.cloudflare.com/api/resources/radar/subresources/ranking/subresources/internet_services/methods/top/)
- [OpenRouter Models API: Posted Prices and Listing Dates](https://openrouter.ai/api/v1/models)
- [Universal Commerce Protocol (UCP)](https://ucp.dev/)
- [Scaling Trends for Data Poisoning in LLMs](https://ojs.aaai.org/index.php/AAAI/article/view/34929)
- [Will Artificial Intelligence Eat the Law? The Rise of Hybrid Social-Ordering Systems](https://columbialawreview.org/content/will-artificial-intelligence-eat-the-law-the-rise-of-hybrid-social-ordering-systems/)

## Related Resources in Other Folders

- **`01_M1_Marketing_Analytics_and_Python`**: [A Strategic Framework for Artificial Intelligence in Marketing](https://link.springer.com/article/10.1007/s11747-020-00749-9); [MSI Research Priorities (booklet)](https://msi.org/wp-content/uploads/sites/2/2025/10/MSI_ResearchPriorities.pdf); [Marketing Analytics Jumpstart (Google Cloud)](https://github.com/GoogleCloudPlatform/marketing-analytics-jumpstart)
- **`02_M2_Customer_Data_and_Visualization`**: [FlowingData (Nathan Yau)](https://flowingdata.com/); [Our World in Data: charts and downloadable data, with a chart-level CSV API](https://ourworldindata.org/); [Wayback Machine CDX Server API (archived-capture index)](https://github.com/internetarchive/wayback/tree/master/wayback-cdx-server); [Wikimedia REST API: pageviews per article (daily since 2015)](https://wikimedia.org/api/rest_v1/); [The Economics of Privacy](https://www.aeaweb.org/articles?id=10.1257/jel.54.2.442); [Apple RSS feed generator: App Store top-free and top-paid charts as JSON](https://rss.marketingtools.apple.com/)
- **`04_M4_Conjoint_Segmentation_CLV`**: [AI-Human Hybrids for Marketing Research: Leveraging Large Language Models (LLMs) as Collaborators](https://journals.sagepub.com/doi/10.1177/00222429241276529); [Digital Twins as Funhouse Mirrors: Five Key Distortions](https://arxiv.org/abs/2509.19088); [TensorHouse: reference notebooks for marketing, promotions and pricing (successor to Introduction to Algorithmic Marketing examples)](https://github.com/ikatsov/tensor-house); [The Challenge of Using LLMs to Simulate Human Behavior: A Causal Inference Perspective](https://arxiv.org/abs/2312.15524); [Using LLMs for Market Research](https://papers.ssrn.com/abstract=4395751); [Synthetic Replacements for Human Survey Data? The Perils of Large Language Models](https://www.cambridge.org/core/journals/political-analysis/article/synthetic-replacements-for-human-survey-data-the-perils-of-large-language-models/B92267DC26195C7F36E63EA04A47D2FE); [Twin-2K-500: A dataset for building digital twins of over 2,000 people based on their answers to over 500 questions](https://huggingface.co/datasets/LLM-Digital-Twin/Twin-2K-500)
- **`05_M5_Text_and_Social_Media_Analytics`**: [Dataset: retailer earnings-call mentions of dynamic, surge, personalized and AI pricing (Nov 2021 - Nov 2026)](https://github.com/nene88991999/BADM534-Marketing-Analytics/tree/main/03_Data_and_Code/Earnings_Calls); [OpenAI Cookbook: embedding and classification notebooks on Amazon fine-food reviews, plus structured outputs and synthetic data](https://github.com/openai/openai-cookbook); [The Market for Fake Reviews](https://doi.org/10.1287/mksc.2022.1353); [Influencer Marketing Effectiveness](https://doi.org/10.1177/00222429221102889); [Online Influencer Marketing](https://ideas.repec.org/a/spr/joamsc/v50y2022i2d10.1007_s11747-021-00829-4.html); [Visual Listening In: Extracting Brand Image Portrayed on Social Media](https://pubsonline.informs.org/doi/fpi/10.1287/mksc.2020.1226); [Facebook Social Connectedness Index (SCI): friendship links between US counties, zip codes and countries](https://ai.meta.com/ai-for-good/datasets/social-connectedness-index/); [Federal Trade Commission Announces Final Rule Banning Fake Reviews and Testimonials](https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials)
- **`06_M6_Causal_Inference_and_Experiments`**: [FeedX: transparent, robust A/B experimentation for Shopping feeds](https://github.com/google-marketing-solutions/feedx); [Meridian GeoX: open-source geo experimentation for cross-publisher incrementality](https://github.com/google/meridian-geox); [mta: multi-touch attribution models in Python (heuristics, Markov chain, Shapley, Shao, logistic, additive hazard)](https://github.com/eeghor/mta); [Meridian: Google's open-source Bayesian marketing mix model](https://developers.google.com/meridian); [PyMC-Marketing: Bayesian MMM, CLV and choice models in Python](https://www.pymc-marketing.io/en/stable/); [Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus?](https://www.nber.org/papers/w31122); [A Comparison of Approaches to Advertising Measurement: Evidence from Big Field Experiments at Facebook](https://www.kellogg.northwestern.edu/academics-research/research/detail/2019/a-comparison-of-approaches-to-advertising-measurement-evidence-from/); [Consumer Heterogeneity and Paid Search Effectiveness: A Large-Scale Field Experiment](https://doi.org/10.3982/ECTA12423); [The Unfavorable Economics of Measuring the Returns to Advertising](https://ideas.repec.org/a/oup/qjecon/v130y2015i4p1941-1973.html); [TFP CausalImpact: Python port of Google's CausalImpact](https://github.com/google/tfp-causalimpact); [Better Experiments with LLM Evals: A funnel, not a fork](https://engineering.atspotify.com/2026/5/better-experiments-with-llm-evals-a-funnel-not-a-fork); [GeoLift: geo-level lift measurement with synthetic control](https://github.com/facebookincubator/GeoLift); [Close Enough? A Large-Scale Exploration of Non-Experimental Approaches to Advertising Measurement](https://www.kellogg.northwestern.edu/academics-research/research/detail/2023/close-enough-a-large-scale-exploration-of-non-experimental/); [Robyn: Meta's open-source marketing mix modeling package](https://github.com/facebookexperimental/Robyn); [Ghost Ads: Improving the Economics of Measuring Online Ad Effectiveness](https://www.kellogg.northwestern.edu/faculty/research/detail/2017/ghost-ads-improving-the-economics-of-measuring-online-ad); [balance: Python package for adjusting biased samples (survey weighting)](https://github.com/facebookresearch/balance); [Meridian GeoX: open-source geo experiments for incrementality and MMM calibration](https://developers.google.com/meridian/geox)
- **`07_M7_Predictive_Models_ML_and_AI`**: [Netflix Recommendations: Beyond the 5 stars (Part 1)](https://netflixtechblog.com/netflix-recommendations-beyond-the-5-stars-part-1-55838468f429); [Engagement, User Satisfaction, and the Amplification of Divisive Content on Social Media](https://pmc.ncbi.nlm.nih.gov/articles/PMC11894805/); [Short-term Exposure to Filter-Bubble Recommendation Systems Has Limited Polarization Effects: Naturalistic Experiments on YouTube](https://doi.org/10.1073/pnas.2318127122); [The Challenge of Understanding What Users Want: Inconsistent Preferences and Engagement Optimization](https://arxiv.org/abs/2202.11776v1); [What are you optimizing for? Aligning Recommender Systems with Human Values](https://arxiv.org/abs/2107.10939v1); [Steering via Algorithmic Recommendations](https://doi.org/10.1111/1756-2171.12481)
- **`10_AI_Coding_Concepts_and_Evidence`**: [Agentic coding and persistent returns to expertise](https://www.anthropic.com/research/claude-code-expertise); [AI Agents for Economic Research: August 2025 Update](https://www.aeaweb.org/articles/materials/23826); [Generative AI at Work](https://digitaleconomy.stanford.edu/publication/generative-ai-at-work); [Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/); [The Effects of Generative AI on High-Skilled Work: Evidence from Three Field Experiments with Software Developers](https://pubsonline.informs.org/doi/fpi/10.1287/mnsc.2025.00535); [Generative AI for Economic Research: Use Cases and Implications for Economists](https://www.aeaweb.org/articles?id=10.1257/jel.20231736); [Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of AI on Knowledge Worker Productivity and Quality](https://papers.ssrn.com/abstract=4573321); [The Impact of AI on Developer Productivity: Evidence from GitHub Copilot](https://arxiv.org/abs/2302.06590); [Speaking things into existence: Expertise in a vibe-filled world of work](https://www.oneusefulthing.org/p/speaking-things-into-existence); [Who is using AI to code? Global diffusion and impact of generative AI](https://arxiv.org/abs/2506.08945); [Automated Social Science: Language Models as Scientist and Subjects](https://arxiv.org/abs/2404.11794); [CORE-Bench: Fostering the Credibility of Published Research Through a Computational Reproducibility Agent Benchmark](https://arxiv.org/abs/2409.11363); [Vulnerabilities in AI Code Generators: Exploring Targeted Data Poisoning Attacks](https://arxiv.org/abs/2308.04451v3); [Vibe Coding Kills Open Source](https://arxiv.org/abs/2601.15494)
- **`11_AI_Coding_Tools_and_Workflows`**: [An important update: Transitioning Gemini CLI to Antigravity CLI](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli); [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/); [Vibe Coding 101 with Replit (DeepLearning.AI)](https://www.deeplearning.ai/short-courses/vibe-coding-101-with-replit/); [claude-persona: Claude Code skill for AI persona panels and concept testing](https://github.com/takechanman1228/claude-persona); [Windsurf, now Devin Desktop (Cognition)](https://devin.ai/desktop); [Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/abs/2302.12173)
- **`12_AI_Coding_Pedagogy_and_Policy`**: [Claude Code and What Comes Next](https://www.oneusefulthing.org/p/claude-code-and-what-comes-next); [The Impact of Generative AI on Critical Thinking: Self-Reported Reductions in Cognitive Effort and Confidence Effects From a Survey of Knowledge Workers](https://www.microsoft.com/en-us/research/publication/the-impact-of-generative-ai-on-critical-thinking-self-reported-reductions-in-cognitive-effort-and-confidence-effects-from-a-survey-of-knowledge-workers/)
- **`20_Datasets`**: [Open e-commerce 1.0: five years of crowdsourced US Amazon purchase histories with user demographics](https://doi.org/10.7910/DVN/YGLYDY); [PyMC-Marketing example data: synthetic MMM and CDNOW CLV](https://www.pymc-marketing.io/en/stable/notebooks/mmm/mmm_example.html); [Epoch AI: Notable AI Models (data hub)](https://epoch.ai/data/notable-ai-models); [S&P 500 Earnings Call Transcripts with Speaker Turns, Roles and SEC CIKs (2005-2025), Hugging Face](https://huggingface.co/datasets/zcyeee/sp500-earnings-call-turns); [Criteo Uplift Prediction Dataset (v2.1)](https://ailab.criteo.com/?p=859); [Dominick's Finer Foods scanner data](https://www.chicagobooth.edu/research/kilts/research-data/dominicks); [Google Meridian simulated geo-level MMM data (geo_all_channels)](https://developers.google.com/meridian/docs/user-guide/load-geo-data-with-organic-and-non-media); [Criteo Attribution Modeling for Bidding Dataset](https://ailab.criteo.com/?p=649); [CTR prediction benchmarks: Avazu (Kaggle) and Criteo 1TB Click Logs](https://www.kaggle.com/c/avazu-ctr-prediction); [NielsenIQ Retail Scanner and Consumer Panel data (Kilts Center)](https://www.chicagobooth.edu/research/kilts/research-data/nielseniq); [Open Bandit Dataset and Open Bandit Pipeline](https://github.com/st-tech/zr-obp)
- **`21_Open_Textbooks_and_Courses`**: [Marketing Science in Python: A Practitioner's Guide (companion code)](https://github.com/takechanman1228/marketing-science-in-python); [Data Analytics for Marketing: A practical guide to analyzing marketing data using Python (companion code)](https://github.com/PacktPublishing/Data-Analytics-for-Marketing); [Marketing Analytics and Data Science: Tools and Models (supplementary code)](https://link.springer.com/book/9783032111296); [Applied Marketing Analytics Using Python](https://collegepublishing.sagepub.com/products/applied-marketing-analytics-using-python-1-288563); [Machine Learning and Generative AI for Marketing (companion code)](https://github.com/PacktPublishing/Machine-Learning-and-Generative-AI-for-Marketing); [Ad response tutorial: last-click attribution, experiments, MMM and attribution models](https://github.com/eleafeit/ad_response_tutorial); [Customer Analytics (Wharton, Coursera)](https://www.coursera.org/learn/wharton-customer-analytics); [Darden Business Publishing (cases, simulations, course packs)](https://store.darden.virginia.edu/); [Marketing Science Institute library (free working papers)](https://www.msi.org/library/)
