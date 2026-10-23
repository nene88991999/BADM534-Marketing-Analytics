# M8 · Current Topics in Marketing

35 resources (10 core). Built 2026-10-23 from `00_Index/_data/`; edit the YAML there and rerun `00_Index/_build/build_catalog.py` rather than editing this file.

Priority: **core** = likely to assign or build on; **recommended** = strong supplement; **optional** = background or niche. *Access* tells you whether students can open it without a login.

## Contents

- [Generative AI in marketing practice](#generative-ai-in-marketing-practice) (9)
- [Privacy and measurement](#privacy-and-measurement) (4)
- [Retail media, creators and pricing](#retail-media-creators-and-pricing) (3)
- [Algorithmic bias](#algorithmic-bias) (2)
- [Industry reports](#industry-reports) (4)
- [Staying current: newsletters and podcasts](#staying-current-newsletters-and-podcasts) (4)
- [Python for marketing analytics: notebooks and code](#python-for-marketing-analytics-notebooks-and-code) (8)
- [Data poisoning and measurement integrity](#data-poisoning-and-measurement-integrity) (1)

## Generative AI in marketing practice

- [core] **[Buy it in ChatGPT: Instant Checkout and the Agentic Commerce Protocol](https://openai.com/index/buy-it-in-chatgpt/)** (2025) — OpenAI. *openai.com (September 29, 2025)*
  `website` · `intro` · `access: open` · `Apache-2.0 (ACP specification)` · `AI angle`
  OpenAI's launch of in-chat purchasing (starting with US Etsy sellers, Shopify planned) and the open Agentic Commerce Protocol (ACP), co-developed with Stripe, in which merchants stay merchant of record.
  *Use in wiki:* Primary source for the agentic-commerce lecture. Ask what happens to brand choice, search ads and retail media when an AI agent does the shopping.
  [Open-access copy](https://www.agenticcommerce.dev/) · Local copy: `08_M8_Current_Topics_in_Marketing/repos/agentic-commerce-protocol__agentic-commerce-protocol`
  *Note:* Developer docs are at developers.openai.com/commerce. The ACP license (Apache 2.0) is stated on agenticcommerce.dev; I did not fetch the GitHub repo itself.

- [core] **[GEO: Generative Engine Optimization](https://arxiv.org/abs/2311.09735)** (2024) — Aggarwal, P.; Murahari, V.; Rajpurohit, T.; Kalyan, A.; Narasimhan, K.; Deshpande, A. *arXiv 2311.09735 (v3, June 2024); KDD 2024 per course brief (venue not verified)*
  `paper` · `intermediate` · `access: open` · `AI angle`
  Defines generative engine optimization: making content visible in LLM-generated search answers. Introduces GEO-bench (10K queries) and shows that strategies such as adding citations, quotes and statistics can raise visibility by up to 40%.
  *Use in wiki:* The anchor reading for 'SEO becomes GEO'. Students rewrite a product page with GEO tactics and test their visibility in an LLM answer engine.
  [Open-access copy](https://generative-engines.com/GEO/) · Tools: openai · Local copy: `08_M8_Current_Topics_in_Marketing/repos/GEO-optim__GEO`
  *Note:* The ACM DL page (KDD) could not be fetched, and the project page cites the work only as arXiv. GEO-bench is at huggingface.co/datasets/GEO-optim/geo-bench.

- [recommended] **[Frontiers: Generative AI and Personalized Video Advertisements](https://pubsonline.informs.org/doi/fpi/10.1287/mksc.2023.0494)** (2025) — Kapoor, A.; Kumar, M. *Marketing Science 44(4), 733–747*
  `paper` · `advanced` · `access: library`
  Studies the effectiveness of generative-AI personalized video ads relative to non-personalized versions.
  *Use in wiki:* Fills a gap the main search flagged (no good piece on GenAI personalization). Check its design and findings before pairing it with M6.
  DOI [10.1287/mksc.2023.0494](https://doi.org/10.1287/mksc.2023.0494)
  *Note:* Also on the MBA 542 Module 6 reading list. The summary is deliberately brief because the paper itself was not opened; MIT IDE has a research brief (https://ide.mit.edu/insights/personalized-ai-video-ads).

- [recommended] **[Powering AI commerce with the new Agent Payments Protocol (AP2)](https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol)** (2025) — Parikh, S.; Surapaneni, R. (Google). *Google Cloud Blog (September 16, 2025)*
  `blog` · `intro` · `access: open` · `AI angle`
  Google's open protocol for AI agents to initiate payments, using signed 'Intent' and 'Cart' mandates as an audit trail. More than 60 partners (Mastercard, AmEx, PayPal, Adyen, Coinbase and others) back it, and it works as an extension of A2A alongside MCP.
  *Use in wiki:* Compare with OpenAI's ACP: who controls the customer relationship and the data when agents buy?
  *Note:* The repo is linked as goo.gle/ap2; no direct GitHub URL was verified, and the license was not stated.

- [recommended] **[The Power of Generative Marketing: Can Generative AI Create Superhuman Visual Marketing Content?](https://ideas.repec.org/a/eee/ijrema/v42y2025i1p13-31.html)** (2025) — Hartmann, J.; Exner, Y.; Domdey, S. *International Journal of Research in Marketing 42(1), 13–31*
  `paper` · `intermediate` · `access: library`
  Compares AI-generated with human-made marketing images at scale, finding that current generative models can match or exceed human-made visuals on quality and realism measures.
  *Use in wiki:* Evidence for the M8 GenAI-in-marketing discussion. Check the study designs before using it as an M6 example.
  *Note:* Also on the MBA 542 Module 6 reading list. DOI not confirmed in a search result.

- [recommended] **[When AI Guides the Shopping Journey](https://www.iab.com/insights/when-ai-guides-the-shopping-journey/)** (2025) — IAB; Talk Shoppe. *IAB (October 28, 2025)*
  `report` · `intro` · `access: free-registration` · `AI angle`
  Mixed-method study (450+ digital ethnographies plus a survey of 600 US consumers). Nearly 40% of US shoppers use AI when shopping. AI reshapes rather than shortens the path to purchase, and trust friction is common.
  *Use in wiki:* Consumer-side evidence to pair with the agentic-commerce protocols, and a source of discussion stats.
  *Note:* Download terms (free or registration) were not stated.

- [recommended] **[Frontiers: Supporting Content Marketing with Natural Language Generation](https://ideas.repec.org/a/inm/ormksc/v41y2022i3p441-452.html)** (2022) — Reisenbichler, M.; Reutterer, T.; Schweidel, D. A.; Dan, D. *Marketing Science 41(3): 441-452*
  `paper` · `intermediate` · `access: library` · `AI angle`
  Machine-drafted, human-edited SEO landing-page copy is nearly indistinguishable from expert copy, and in field experiments it ranks better in search at much lower cost.
  *Use in wiki:* Evidence-based case for 'human-in-the-loop' GenAI content, which pairs with GEO as the 'before and after' of LLM search.
  DOI [10.1287/mksc.2022.1354](https://doi.org/10.1287/mksc.2022.1354)

- [optional] **[Universal Commerce Protocol (UCP)](https://ucp.dev/)** (2026) — UCP Authors (co-developed by Google, Shopify and others). *ucp.dev*
  `website` · `intro` · `access: open` · `Apache-2.0` · `AI angle`
  An open standard covering the whole agentic shopping flow (discovery, checkout, post-purchase) between platforms, agents and businesses. It builds on AP2 for payments.
  *Use in wiki:* A 2026 snapshot of the competing agentic-commerce standards (ACP vs AP2/UCP) for a short comparison table on the wiki.
  *Note:* The announcement date is not stated on the site. The year 2026 comes from the copyright and the lodging draft. The site lists Amazon, Microsoft and Stripe among co-developers; check this before citing.

- [optional] **[The Caring Machine: Feeling AI for Customer Care](https://www.ama.org/2024/04/23/can-companies-create-a-machine-that-feels-and-cares-using-generative-ai-to-provide-empathetic-customer-care/)** (2024) — Huang, M.-H.; Rust, R. T. *Journal of Marketing 88(5)*
  `paper` · `intermediate` · `access: library`
  Conceptual framework for using generative 'feeling AI' to deliver empathetic customer care and build customer lifetime value. The link is the AMA's summary of the article.
  *Use in wiki:* Optional M8 reading if the course touches AI customer service.
  *Note:* Also on the MBA 542 Module 4 reading list. A corrigendum was published (https://journals.sagepub.com/doi/full/10.1177/00222429241270362). The article's own DOI was not confirmed.

## Privacy and measurement

- [core] **[Retail Media ROAS Demystified: Understanding Your Brand's ROAS](https://ovative.com/impact/expert-insights/retail-media-roas-demystified/)** (2025) — Nelson, D. T.; Bante, K.; Gordon, B. R.; Anderson, E. T.; Dantzinger, L.; Armor, S. *Ovative Group with Albertsons Media Collective and Kellogg School of Management (May 15, 2025)*
  `report` · `intermediate` · `access: open`
  Analyzes 573 Albertsons Media Collective campaigns to show how retail-media-network ROAS methods differ and how much reported results shift with methodology. Ends with questions advertisers should ask RMNs.
  *Use in wiki:* Retail-media case reading (with Kellogg co-authors Gordon and Anderson). Students explain why platform-reported ROAS and incremental ROAS differ.
  [Open-access copy](https://ovative.com/wp-content/uploads/2025/05/Retail-Media-ROAS-Demystified-Ovative-Albertsons-Kellogg-Business-School.pdf)
  *Note:* The PDF link was given on the fetched page; I did not fetch the PDF itself.

- [core] **[Update on Plans for Privacy Sandbox Technologies](https://privacysandbox.google.com/blog/update-on-plans-for-privacy-sandbox-technologies)** (2025) — Chavez, A. (Google, VP Privacy Sandbox). *privacysandbox.google.com (October 17, 2025)*
  `blog` · `intro` · `access: open`
  Google says Chrome will keep its current approach of user choice on third-party cookies (no deprecation). It is retiring most Privacy Sandbox APIs (Topics, Protected Audience, Attribution Reporting, IP Protection and others) after low adoption, and keeping CHIPS, FedCM and Private State Tokens.
  *Use in wiki:* The definitive answer to 'are cookies dead?' as of late 2026. Use it to open the measurement week and explain why first-party data, clean rooms and MMM matter anyway.
  *Note:* privacysandbox.com/news/... now redirects to privacysandbox.google.com. Check the status page (privacysandbox.google.com/overview/status) before class for any later change.

- [recommended] **[IAB Tech Lab Standards: Data Clean Rooms Guidance, PAIR, and ADMaP](https://iabtechlab.com/standards/)** (2025) — IAB Tech Lab (Addressability and PETs Working Group). *iabtechlab.com*
  `website` · `intermediate` · `access: open`
  Industry standards index listing the Data Clean Rooms Guidance (v1.0, July 2024), PAIR for privacy-safe advertiser-publisher ID matching in clean rooms (2024), and ADMaP for sharing conversion data with private set intersection or TEEs (February 2025).
  *Use in wiki:* Instructor background and a short explainer on how clean rooms let a brand and a retailer join first-party data without exchanging it.
  *Note:* The fetched index page did not expose deep links to each standard. For a concrete vendor example, AWS Clean Rooms (aws.amazon.com/clean-rooms/, verified) supports SQL and PySpark analyses, differential privacy and ML on partner data.

- [recommended] **[App Tracking Transparency (framework documentation)](https://developer.apple.com/documentation/apptrackingtransparency)** (2021) — Apple Developer. *developer.apple.com*
  `documentation` · `intro` · `access: open`
  Apple's official documentation for the ATT permission that apps must request before tracking users across other companies' apps and sites or accessing the IDFA. It was introduced with iOS 14.5.
  *Use in wiki:* Primary source for the ATT shock to mobile ad targeting and attribution, to pair with a discussion of how platforms shifted to modeled conversions and MMM.
  *Note:* The page is JavaScript-rendered, so the fetch returned only metadata. The iOS 14.5 and 2021 dates are standard knowledge, not quoted from the page. No academic ATT study was verified in this pass (search budget ran out).

## Retail media, creators and pricing

- [core] **[2025 Creator Economy Ad Spend & Strategy Report](https://www.iab.com/insights/2025-creator-economy-ad-spend-strategy-report/)** (2025) — IAB. *IAB (November 20, 2025)*
  `report` · `intro` · `access: open`
  US creator ad spend projected at $37B in 2025 (+26% year over year, about 4x faster than overall media), $44B expected in 2026. 48% of buyers call creators a 'must buy', and 3 in 4 brands use or plan AI for creator marketing.
  *Use in wiki:* Size-of-market slide and discussion: why creator measurement and standards lag, linked to M5 social media analysis.
  *Note:* The summary page is public and the full PDF is downloadable from it. The page was modified June 2026.

- [recommended] **[The Commerce Media Connection Gap: Why the Next Phase of Growth Depends on the Cohesion of the Ecosystem](https://www.iab.com/wp-content/uploads/2026/10/The-Commerce-Media-Connection-Gap.pdf)** (2026) — SMG; IAB; IAB UK. *IAB (October 2026)*
  `report` · `intro` · `access: open`
  Survey of 281 brands, agencies and RMNs in six countries (fieldwork July to August 2026). Reporting is the least connected function, only 14% get unified cross-channel reporting, and 46% of brands say proven incremental ROI would unlock more spend.
  *Use in wiki:* A very current snapshot of retail-media pain points (fragmentation, measurement) for the M8 discussion.
  *Note:* The report contains no RMN spend figures. For market size, see the IAB/PwC Internet Advertising Revenue Report FY2025 (iab.com/insights/internet-advertising-revenue-report-full-year-2025/, verified; about $300B in US internet ad revenue in 2025, +13.9%; key takeaways need a free IAB account).

- [recommended] **[Artificial Intelligence, Algorithmic Pricing, and Collusion](https://www.aeaweb.org/articles?id=10.1257/aer.20190623)** (2020) — Calvano, E.; Calzolari, G.; Denicolò, V.; Pastorello, S. *American Economic Review 110(10): 3267-97*
  `paper` · `advanced` · `access: library` · `AI angle`
  Q-learning pricing algorithms in simulated oligopolies learn to sustain supra-competitive prices with punishment strategies, without communicating.
  *Use in wiki:* Background for the algorithmic-pricing discussion (RealPage-style cases). Present the key figure and intuition rather than assigning the full paper.
  DOI [10.1257/aer.20190623](https://doi.org/10.1257/aer.20190623)
  *Note:* Empirical complement: Brown & MacKay (2023), 'Competition in Pricing Algorithms', AEJ: Microeconomics 15(2): 109-56, doi 10.1257/mic.20210158 (aeaweb page verified). It shows that simple rival-responsive pricing algorithms at online retailers can raise prices.

## Algorithmic bias

- [core] **[Algorithmic Bias? An Empirical Study of Apparent Gender-Based Discrimination in the Display of STEM Career Ads](https://ideas.repec.org/a/inm/ormnsc/v65y2019i7p2966-2981.html)** (2019) — Lambrecht, A.; Tucker, C. *Management Science 65(7): 2966-2981*
  `paper` · `intermediate` · `access: library`
  A gender-neutral STEM job ad was shown to fewer women because younger women are a more expensive audience. Cost-minimizing delivery produced the apparent bias, and the pattern held across platforms.
  *Use in wiki:* Core case for algorithmic bias arising from market mechanics rather than intent, discussed alongside Ali et al. (2019).
  DOI [10.1287/mnsc.2018.3093](https://doi.org/10.1287/mnsc.2018.3093)

- [core] **[Discrimination through optimization: How Facebook's ad delivery can lead to skewed outcomes](https://arxiv.org/abs/1904.02095)** (2019) — Ali, M.; Sapiezynski, P.; Bogen, M.; Korolova, A.; Mislove, A.; Rieke, A. *Proceedings of the ACM on Human-Computer Interaction (CSCW 2019); arXiv 1904.02095*
  `paper` · `intermediate` · `access: open` · `AI angle`
  Paired ad experiments show that Facebook's delivery optimization skews employment and housing ads by gender and race even with neutral targeting, driven by budget effects and the platform's predicted relevance of the ad content.
  *Use in wiki:* Pair with Lambrecht and Tucker: one shows a market-cost mechanism, the other a platform-prediction mechanism. Good for a debate on who is accountable.
  DOI [10.1145/3359301](https://doi.org/10.1145/3359301)
  *Note:* The venue (PACM HCI/CSCW) is inferred from the ACM DOI listed on arXiv.

## Industry reports

- [core] **[The state of AI in 2026: On the road to ROI](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai)** (2026) — Tinkoff, D.; Van der Veken, L.; Chui, M.; Balakrishnan, T. (McKinsey / QuantumBlack). *McKinsey & Company (August 25, 2026)*
  `report` · `intro` · `access: open` · `AI angle`
  McKinsey's annual global AI survey. Agent scaling is concentrated in large firms (40% vs 22%), consumer and retail firms most often use agents in marketing and sales, and marketing and sales is where respondents most often report AI-driven revenue gains.
  *Use in wiki:* Opening reading for M8 with stats for the 'AI in marketing practice' slide. A 31-page PDF is downloadable.
  *Note:* The 2025 edition is listed on the same page as a previous report. For a value estimate, see McKinsey (2023) 'The economic potential of generative AI' (verified): marketing productivity gains of 5-15% of marketing spend.

- [recommended] **[Anthropic Economic Index](https://www.anthropic.com/economic-index)** (2026) — Anthropic. *anthropic.com; Hugging Face (Anthropic/EconomicIndex)*
  `dataset` · `intermediate` · `access: open` · `Data CC-BY; code MIT (per dataset card)` · `AI angle`
  Privacy-preserving data on how people use Claude across occupations (O*NET tasks), US states and countries, including automation-vs-augmentation shares. Releases run from February 2025 to June 2026.
  *Use in wiki:* Real dataset for a short in-class exercise on which marketing and sales tasks are being automated vs augmented, using the M2 visualization tools.
  [Open-access copy](https://huggingface.co/datasets/Anthropic/EconomicIndex) · Tools: pandas, datasets
  *Note:* The full HF dataset is 763 MB, so download only the needed release folder (for example 2026-06-26). The main page was last updated June 26, 2026.

- [recommended] **[Exploring Strategic Insights From Gartner's 2026 CMO Spend Survey (webinar)](https://www.gartner.com/en/marketing/research/annual-cmo-spend-survey-research)** (2026) — Gartner. *Gartner for Marketing*
  `report` · `intro` · `access: free-registration`
  Gartner's annual survey of CMO budgets: how 2026 budgets are shifting across channels and programs, and how AI is changing marketing capabilities and investment.
  *Use in wiki:* Budget benchmark (marketing spend as a share of revenue, channel mix) for the opening of M8. The instructor can watch it and pull two or three headline numbers.
  *Note:* The public page is a free on-demand webinar (work email registration). The full survey report is usually for Gartner clients only. No headline numbers were visible on the page.

- [recommended] **[The 2026 AI Index Report](https://hai.stanford.edu/ai-index/2026-ai-index-report)** (2026) — Stanford Institute for Human-Centered AI (HAI). *Stanford HAI*
  `report` · `intro` · `access: open` · `AI angle`
  Annual data-driven report on AI in nine chapters: R&D, technical performance, responsible AI, economy, science, medicine, education, policy and public opinion. It links a full PDF and public data.
  *Use in wiki:* Use the Economy and Public Opinion chapters for M8, and the public data folder as an M2 visualization exercise dataset.
  *Note:* The release date and license were not stated on the page. The data is on a public Google Drive folder.

## Staying current: newsletters and podcasts

- [core] **[One Useful Thing](https://www.oneusefulthing.org/)** (2026) — Mollick, E. *Substack*
  `newsletter` · `intro` · `access: open` · `AI angle`
  Ethan Mollick's newsletter on the practical implications of AI for work and education (488K+ subscribers), with frequent hands-on comparisons of frontier models.
  *Use in wiki:* Weekly 'stay current' link on the wiki. Individual posts work as short discussion readings on AI-assisted analysis.
  *Note:* Free or paid status was not stated on the page. Most posts are free.

- [recommended] **[AdExchanger (AdExchanger Daily newsletter; AdExchanger Talks podcast)](https://www.adexchanger.com/)** (2026) — AdExchanger. *adexchanger.com*
  `newsletter` · `intermediate` · `access: freemium`
  News and analysis on data-driven marketing: privacy, measurement, commerce and retail media, and ad tech, with a free weekday newsletter and podcasts (AdExchanger Talks, The Big Story, Inside the Stack).
  *Use in wiki:* Best single feed for following cookies, clean rooms, MMM and retail media during the semester.
  *Note:* Some articles may be paywalled. Marketing Brew (marketingbrew.com, Morning Brew, weekday newsletter; verified) is a lighter, free alternative.

- [recommended] **[Simon Willison's Weblog](https://simonwillison.net/)** (2026) — Willison, S. *simonwillison.net*
  `blog` · `intermediate` · `access: open` · `AI angle`
  Very frequent, hands-on posts on new LLM releases, coding agents, 'vibe coding', prompt injection and security, and practical tools (LLM CLI, Datasette).
  *Use in wiki:* The go-to 'staying current' source for the course's AI-assisted coding emphasis, and for spotting agent failure modes and security risks.
  Tools: llm, datasette
  *Note:* The blog is free. A $10/month curated email briefing is optional.

- [recommended] **[The Artificial Intelligence Show](https://podcast.smarterx.ai/)** (2026) — Roetzer, P.; Kaput, M. (Marketing AI Institute / SmarterX). *podcast.smarterx.ai*
  `podcast` · `intro` · `access: open` · `AI angle`
  A weekly (Tuesday) podcast, started in 2021 by the Marketing AI Institute founders, covering AI news and practical guidance for marketers and business careers.
  *Use in wiki:* Optional weekly listening, and students can pick an episode to summarize in a short reflection.
  *Note:* marketingaiinstitute.com/podcast-showcase now redirects to podcast.smarterx.ai.

## Python for marketing analytics: notebooks and code

- [core] **[Gemini API Cookbook: Market a Jet Backpack, JSON sentiment and classification, embeddings classification and clustering](https://github.com/google-gemini/cookbook)** (2026) — Google (google-gemini). *GitHub (google-gemini/cookbook)*
  `notebook` · `intro` · `access: open` · `Apache-2.0` · `AI angle`
  Short Colab notebooks on the free-tier Gemini API key. They turn a product sketch into a marketing campaign with JSON taglines, run sentiment analysis, text classification, entity extraction and summarization with JSON output, and classify and cluster text with embeddings.
  *Use in wiki:* First GenAI-for-marketing lab, because it runs in Colab with a free API key and no cloud project. The Jet Backpack notebook is a ready 'AI creative brief' exercise.
  Tools: google-genai, pandas, scikit-learn · Local copy: `08_M8_Current_Topics_in_Marketing/repos/google-gemini__cookbook`
  *Note:* Last commit 2026-10-19. Model names in notebooks change often; tell students to update the model ID. quickstarts/Get_started.ipynb (5.4 MB) is left out to stay lean.

- [recommended] **[Copycat: AI-generated Google Search ad copy that matches your brand style](https://github.com/google-marketing-solutions/copycat)** (2026) — Google Marketing Solutions. *GitHub (google-marketing-solutions/copycat)*
  `tool` · `intermediate` · `access: open` · `Apache-2.0` · `AI angle`
  Python package and Colabs (Python quickstart and a GUI) that learn brand style from existing high-performing Responsive Search Ads and generate new headlines and descriptions for new keywords with Gemini. Gemini first drafts a brand style guide from the exemplar ads (optionally from brand-guideline PDFs), which the user can edit before ads are generated.
  *Use in wiki:* Hands-on M8 case: generate RSAs with Copycat, then design a FeedX-style or A/B test to measure whether AI copy beats human copy.
  Tools: gtech-copycat, google-genai, pandas · Local copy: `08_M8_Current_Topics_in_Marketing/repos/google-marketing-solutions__copycat`
  *Note:* Last commit 2026-09-24. Needs Python 3.10 or later and Gemini API or Vertex credentials. The org (150 repos) also has feedgen (LLM feed optimization, Apps Script), vigenair (video ad recrafting) and adspace_agent (an ADK agent for Google Ads planning, 2026), but none has Python teaching notebooks.

- [recommended] **[Google Cloud generative-ai repo: creative content generation, product attribute extraction, multimodal sentiment, AI-assisted data science](https://github.com/GoogleCloudPlatform/generative-ai)** (2026) — Google Cloud. *GitHub (GoogleCloudPlatform/generative-ai)*
  `notebook` · `intermediate` · `access: open` · `Apache-2.0` · `AI angle`
  Vertex AI notebooks: marketing creative content generation with Gemini and Imagen, product attribute extraction from images (self-correcting prompts), multimodal retail recommendations, location strategy, multimodal sentiment (audio vs transcript), YouTube video analysis, and a Gemini-assisted data science workflow in BigQuery that ends in customer segments.
  *Use in wiki:* M8 demos of GenAI across the marketing funnel. ai-assisted-data-science is a direct example of the course's AI-assisted analytics theme.
  Tools: google-genai, vertex-ai, bigquery, imagen · Local copy: `08_M8_Current_Topics_in_Marketing/repos/GoogleCloudPlatform__generative-ai`
  *Note:* Last commit 2026-10-22. Most notebooks need a GCP project with Vertex AI and billing, unlike the Gemini cookbook. The related repo GoogleCloudPlatform/genai-for-marketing (Apache-2.0, last commit 2026-01-05) has a notebooks/ folder, but several notebooks target retired PaLM/bison models, so it was left out.

- [recommended] **[Semantic-Similarity Rating (SSR): mapping LLM free-text answers to Likert purchase-intent distributions](https://github.com/pymc-labs/semantic-similarity-rating)** (2025) — Maier, B. F.; Aslak, U.; Fiaschi, L.; Rismal, N.; Fletcher, K.; Luhmann, C. C.; Dow, R.; Pappas, K.; Wiecki, T. V. (PyMC Labs). *GitHub (pymc-labs/semantic-similarity-rating); paper arXiv:2510.08338*
  `package` · `advanced` · `access: open` · `Apache-2.0` · `AI angle`
  Package implementing SSR. LLM 'synthetic consumers' answer purchase-intent questions in free text, and the answers are mapped to Likert probability distributions by embedding similarity to anchor statements. The paper is 'LLMs Reproduce Human Purchase Intent via Semantic Similarity Elicitation of Likert Ratings'.
  *Use in wiki:* Current-topics case on LLM-based market research: students simulate concept-test responses, compare direct numeric ratings with SSR, and discuss validity limits.
  [Open-access copy](https://arxiv.org/abs/2510.08338) · Tools: semantic-similarity-rating, polars, numpy, embeddings API · Local copy: `04_M4_Conjoint_Segmentation_CLV/repos/pymc-labs__semantic-similarity-rating`
  *Note:* Last commit 2026-06-04. No notebook; the README quick start is the example. The arXiv page does not link the repo; I matched them through the README's paper title (the README calls it 'Measuring Synthetic Consumer Purchase Intent Using Semantic-Similarity Ratings' (2025), close to the arXiv title, so treat the match as likely but not confirmed). pixi.lock (about 0.5 MB) is excluded.

- [optional] **[Awesome Marketing Science (curated list)](https://github.com/shakostats/Awesome-Marketing-Science)** (2026) — shakostats. *GitHub*
  `website` · `intermediate` · `access: open` · `MIT`
  Maintained link list of marketing-measurement resources (geo experiments, MMM, multi-touch attribution, causal inference) from a practitioner.
  *Use in wiki:* Instructor index for M8 updates and for finding student project ideas.
  Local copy: `21_Open_Textbooks_and_Courses/repos/shakostats__Awesome-Marketing-Science`
  *Note:* README only (pushed 2026-05). vkoul/awesome-Marketing-Analytics is a similar list with no license, so this one is preferred.

- [optional] **[Build a Marketing Mix Model with Claude Code: From OLS to Bayesian (workshop)](https://maven.com/pinemarsh/build-a-marketing-mix-model-with-claude-code)** (2026) — Diaz-Bérrio, G. *Maven*
  `course` · `intermediate` · `access: paid` · `AI angle`
  One-day workshop by the author of Packt's Data Analytics for Marketing: set up Claude Code with CLAUDE.md, agentic EDA, OLS MMM with adstock and saturation, Bayesian MMM in PyMC, and packaging the pipeline as a reusable SKILL.md.
  *Use in wiki:* Design template for an M8 'vibe-coding an MMM' activity (CLAUDE.md, then EDA, OLS, Bayesian, Skill) built on open data and the downloadable Packt DAM ch12 notebook.
  Tools: claude-code, pymc, pandas
  *Note:* Paid. No date, price or GitHub repo given on the page. Two related free lesson recordings are offered.

- [optional] **[markov-chain-attribution: first-order Markov chain attribution in Python](https://github.com/jerednel/markov-chain-attribution)** (2026) — jerednel (GitHub). *GitHub / PyPI (markov-model-attribution)*
  `package` · `intermediate` · `access: open` · `MIT`
  Small package computing Markov-chain removal effects and fractional conversions per channel, with last-touch comparison, from 'start > ... > conv/null' path strings. Based on Anderl et al.'s graph-based attribution framework.
  *Use in wiki:* Compact attribution demo for M8: compare last-touch and Markov credit on toy paths, then on Packt DAM ch11 data.
  Tools: pandas, markov-model-attribution
  *Note:* Proof of concept. The README says to use v0.4 or later (earlier versions could give negative conversions). No notebook, only a README example.

- [optional] **[Digital-Marketing-Analytics: INFO7374 course assignments and Olist project](https://github.com/Nikhilkohli1/Digital-Marketing-Analytics)** (2020) — Kohli, N. (Nikhilkohli1). *GitHub (Northeastern INFO7374 coursework)*
  `notebook` · `intermediate` · `access: open`
  Second most-starred rfm-analysis repo: assignments on a VistaPrint marketing mix, an e-commerce dashboard, promotions and adstock, attribution and budget optimization, xDeepFM/Customer2Vec recommendations, and an Olist RFM/segmentation project with Streamlit and Tableau dashboards.
  *Use in wiki:* Shows what a strong semester team project plus GitHub portfolio can look like; link from the project-guidelines page.
  Tools: pandas, scikit-learn, streamlit, tableau
  *Note:* No license, so link only. Last push 2020.

## Data poisoning and measurement integrity

- [optional] **[Scaling Trends for Data Poisoning in LLMs](https://ojs.aaai.org/index.php/AAAI/article/view/34929)** (2025) — Bowen, D.; et al. *Proceedings of the AAAI Conference on Artificial Intelligence 39*
  `paper` · `advanced` · `access: open` · `AI angle`
  Shows that larger language models learn harmful behavior from small amounts of poisoned fine-tuning data more quickly than smaller ones, so scale does not protect against data poisoning.
  *Use in wiki:* Background for an M8 discussion of poisoned online data (e.g., coordinated reviews or synthetic posts) feeding marketing models and AI assistants.
  [Open-access copy](https://arxiv.org/abs/2408.02946)
  *Note:* Also on the MBA 542 Module 8 reading list.

## AI-assisted coding angle for this module

Resources in this folder that show the method done with AI help, LLM versions of the method, or documented failure modes of AI-written analysis:

- [Gemini API Cookbook: Market a Jet Backpack, JSON sentiment and classification, embeddings classification and clustering](https://github.com/google-gemini/cookbook)
- [One Useful Thing](https://www.oneusefulthing.org/)
- [The state of AI in 2026: On the road to ROI](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai)
- [Buy it in ChatGPT: Instant Checkout and the Agentic Commerce Protocol](https://openai.com/index/buy-it-in-chatgpt/)
- [GEO: Generative Engine Optimization](https://arxiv.org/abs/2311.09735)
- [Discrimination through optimization: How Facebook's ad delivery can lead to skewed outcomes](https://arxiv.org/abs/1904.02095)
- [Anthropic Economic Index](https://www.anthropic.com/economic-index)
- [Copycat: AI-generated Google Search ad copy that matches your brand style](https://github.com/google-marketing-solutions/copycat)
- [Google Cloud generative-ai repo: creative content generation, product attribute extraction, multimodal sentiment, AI-assisted data science](https://github.com/GoogleCloudPlatform/generative-ai)
- [Simon Willison's Weblog](https://simonwillison.net/)
- [The 2026 AI Index Report](https://hai.stanford.edu/ai-index/2026-ai-index-report)
- [The Artificial Intelligence Show](https://podcast.smarterx.ai/)
- [Powering AI commerce with the new Agent Payments Protocol (AP2)](https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol)
- [Semantic-Similarity Rating (SSR): mapping LLM free-text answers to Likert purchase-intent distributions](https://github.com/pymc-labs/semantic-similarity-rating)
- [When AI Guides the Shopping Journey](https://www.iab.com/insights/when-ai-guides-the-shopping-journey/)
- [Frontiers: Supporting Content Marketing with Natural Language Generation](https://ideas.repec.org/a/inm/ormksc/v41y2022i3p441-452.html)
- [Artificial Intelligence, Algorithmic Pricing, and Collusion](https://www.aeaweb.org/articles?id=10.1257/aer.20190623)
- [Build a Marketing Mix Model with Claude Code: From OLS to Bayesian (workshop)](https://maven.com/pinemarsh/build-a-marketing-mix-model-with-claude-code)
- [Universal Commerce Protocol (UCP)](https://ucp.dev/)
- [Scaling Trends for Data Poisoning in LLMs](https://ojs.aaai.org/index.php/AAAI/article/view/34929)

## Also relevant (catalogued in other folders)

- **`01_M1_Marketing_Analytics_and_Python`**: [A Strategic Framework for Artificial Intelligence in Marketing](https://link.springer.com/article/10.1007/s11747-020-00749-9); [MSI Research Priorities (booklet)](https://msi.org/wp-content/uploads/sites/2/2025/10/MSI_ResearchPriorities.pdf); [Marketing Analytics Jumpstart (Google Cloud)](https://github.com/GoogleCloudPlatform/marketing-analytics-jumpstart); [Precision Retailing: Driving Results with Behavioral Insights and Data Analytics](https://utorontopress.com/9781487542719/precision-retailing)
- **`02_M2_Customer_Data_and_Visualization`**: [The Economics of Privacy](https://www.aeaweb.org/articles?id=10.1257/jel.54.2.442)
- **`04_M4_Conjoint_Segmentation_CLV`**: [AI-Human Hybrids for Marketing Research: Leveraging Large Language Models (LLMs) as Collaborators](https://journals.sagepub.com/doi/10.1177/00222429241276529); [Digital Twins as Funhouse Mirrors: Five Key Distortions](https://arxiv.org/abs/2509.19088); [TensorHouse: reference notebooks for marketing, promotions and pricing (successor to Introduction to Algorithmic Marketing examples)](https://github.com/ikatsov/tensor-house); [The Challenge of Using LLMs to Simulate Human Behavior: A Causal Inference Perspective](https://arxiv.org/abs/2312.15524); [Using LLMs for Market Research](https://papers.ssrn.com/abstract=4395751); [Synthetic Replacements for Human Survey Data? The Perils of Large Language Models](https://www.cambridge.org/core/journals/political-analysis/article/synthetic-replacements-for-human-survey-data-the-perils-of-large-language-models/B92267DC26195C7F36E63EA04A47D2FE); [Twin-2K-500: A dataset for building digital twins of over 2,000 people based on their answers to over 500 questions](https://huggingface.co/datasets/LLM-Digital-Twin/Twin-2K-500)
- **`05_M5_Text_and_Social_Media_Analytics`**: [OpenAI Cookbook: embedding and classification notebooks on Amazon fine-food reviews, plus structured outputs and synthetic data](https://github.com/openai/openai-cookbook); [Influencer Marketing Effectiveness](https://doi.org/10.1177/00222429221102889); [Online Influencer Marketing](https://ideas.repec.org/a/spr/joamsc/v50y2022i2d10.1007_s11747-021-00829-4.html); [The Market for Fake Reviews](https://doi.org/10.1287/mksc.2022.1353); [Visual Listening In: Extracting Brand Image Portrayed on Social Media](https://pubsonline.informs.org/doi/fpi/10.1287/mksc.2020.1226); [Federal Trade Commission Announces Final Rule Banning Fake Reviews and Testimonials](https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials)
- **`06_M6_Causal_Inference_and_Experiments`**: [FeedX: transparent, robust A/B experimentation for Shopping feeds](https://github.com/google-marketing-solutions/feedx); [Meridian GeoX: open-source geo experimentation for cross-publisher incrementality](https://github.com/google/meridian-geox); [mta: multi-touch attribution models in Python (heuristics, Markov chain, Shapley, Shao, logistic, additive hazard)](https://github.com/eeghor/mta); [Meridian: Google's open-source Bayesian marketing mix model](https://developers.google.com/meridian); [PyMC-Marketing: Bayesian MMM, CLV and choice models in Python](https://www.pymc-marketing.io/en/stable/); [Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus?](https://www.nber.org/papers/w31122); [A Comparison of Approaches to Advertising Measurement: Evidence from Big Field Experiments at Facebook](https://www.kellogg.northwestern.edu/academics-research/research/detail/2019/a-comparison-of-approaches-to-advertising-measurement-evidence-from/); [Consumer Heterogeneity and Paid Search Effectiveness: A Large-Scale Field Experiment](https://doi.org/10.3982/ECTA12423); [The Unfavorable Economics of Measuring the Returns to Advertising](https://ideas.repec.org/a/oup/qjecon/v130y2015i4p1941-1973.html); [TFP CausalImpact: Python port of Google's CausalImpact](https://github.com/google/tfp-causalimpact); [Better Experiments with LLM Evals: A funnel, not a fork](https://engineering.atspotify.com/2026/5/better-experiments-with-llm-evals-a-funnel-not-a-fork); [GeoLift: geo-level lift measurement with synthetic control](https://github.com/facebookincubator/GeoLift); [Close Enough? A Large-Scale Exploration of Non-Experimental Approaches to Advertising Measurement](https://www.kellogg.northwestern.edu/academics-research/research/detail/2023/close-enough-a-large-scale-exploration-of-non-experimental/); [Robyn: Meta's open-source marketing mix modeling package](https://github.com/facebookexperimental/Robyn); [Ghost Ads: Improving the Economics of Measuring Online Ad Effectiveness](https://www.kellogg.northwestern.edu/faculty/research/detail/2017/ghost-ads-improving-the-economics-of-measuring-online-ad); [balance: Python package for adjusting biased samples (survey weighting)](https://github.com/facebookresearch/balance); [Meridian GeoX: open-source geo experiments for incrementality and MMM calibration](https://developers.google.com/meridian/geox)
- **`07_M7_Predictive_Models_ML_and_AI`**: [Netflix Recommendations: Beyond the 5 stars (Part 1)](https://netflixtechblog.com/netflix-recommendations-beyond-the-5-stars-part-1-55838468f429); [Engagement, User Satisfaction, and the Amplification of Divisive Content on Social Media](https://pmc.ncbi.nlm.nih.gov/articles/PMC11894805/); [Short-term Exposure to Filter-Bubble Recommendation Systems Has Limited Polarization Effects: Naturalistic Experiments on YouTube](https://doi.org/10.1073/pnas.2318127122); [The Challenge of Understanding What Users Want: Inconsistent Preferences and Engagement Optimization](https://arxiv.org/abs/2202.11776v1); [What are you optimizing for? Aligning Recommender Systems with Human Values](https://arxiv.org/abs/2107.10939v1); [Steering via Algorithmic Recommendations](https://doi.org/10.1111/1756-2171.12481)
- **`10_AI_Coding_Concepts_and_Evidence`**: [Agentic coding and persistent returns to expertise](https://www.anthropic.com/research/claude-code-expertise); [AI Agents for Economic Research: August 2025 Update](https://www.aeaweb.org/articles/materials/23826); [Generative AI at Work](https://digitaleconomy.stanford.edu/publication/generative-ai-at-work); [Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/); [The Effects of Generative AI on High-Skilled Work: Evidence from Three Field Experiments with Software Developers](https://pubsonline.informs.org/doi/fpi/10.1287/mnsc.2025.00535); [Generative AI for Economic Research: Use Cases and Implications for Economists](https://www.aeaweb.org/articles?id=10.1257/jel.20231736); [Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of AI on Knowledge Worker Productivity and Quality](https://papers.ssrn.com/abstract=4573321); [The Impact of AI on Developer Productivity: Evidence from GitHub Copilot](https://arxiv.org/abs/2302.06590); [Speaking things into existence: Expertise in a vibe-filled world of work](https://www.oneusefulthing.org/p/speaking-things-into-existence); [Who is using AI to code? Global diffusion and impact of generative AI](https://arxiv.org/abs/2506.08945); [Automated Social Science: Language Models as Scientist and Subjects](https://arxiv.org/abs/2404.11794); [CORE-Bench: Fostering the Credibility of Published Research Through a Computational Reproducibility Agent Benchmark](https://arxiv.org/abs/2409.11363); [Vulnerabilities in AI Code Generators: Exploring Targeted Data Poisoning Attacks](https://arxiv.org/abs/2308.04451v3); [Vibe Coding Kills Open Source](https://arxiv.org/abs/2601.15494)
- **`11_AI_Coding_Tools_and_Workflows`**: [An important update: Transitioning Gemini CLI to Antigravity CLI](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli); [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/); [Vibe Coding 101 with Replit (DeepLearning.AI)](https://www.deeplearning.ai/short-courses/vibe-coding-101-with-replit/); [claude-persona: Claude Code skill for AI persona panels and concept testing](https://github.com/takechanman1228/claude-persona); [Windsurf, now Devin Desktop (Cognition)](https://devin.ai/desktop); [Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/abs/2302.12173)
- **`12_AI_Coding_Pedagogy_and_Policy`**: [Claude Code and What Comes Next](https://www.oneusefulthing.org/p/claude-code-and-what-comes-next); [The Impact of Generative AI on Critical Thinking: Self-Reported Reductions in Cognitive Effort and Confidence Effects From a Survey of Knowledge Workers](https://www.microsoft.com/en-us/research/publication/the-impact-of-generative-ai-on-critical-thinking-self-reported-reductions-in-cognitive-effort-and-confidence-effects-from-a-survey-of-knowledge-workers/)
- **`20_Datasets`**: [PyMC-Marketing example data: synthetic MMM and CDNOW CLV](https://www.pymc-marketing.io/en/stable/notebooks/mmm/mmm_example.html); [Criteo Uplift Prediction Dataset (v2.1)](https://ailab.criteo.com/?p=859); [Dominick's Finer Foods scanner data](https://www.chicagobooth.edu/research/kilts/research-data/dominicks); [Google Meridian simulated geo-level MMM data (geo_all_channels)](https://developers.google.com/meridian/docs/user-guide/load-geo-data-with-organic-and-non-media); [Criteo Attribution Modeling for Bidding Dataset](https://ailab.criteo.com/?p=649); [CTR prediction benchmarks: Avazu (Kaggle) and Criteo 1TB Click Logs](https://www.kaggle.com/c/avazu-ctr-prediction); [NielsenIQ Retail Scanner and Consumer Panel data (Kilts Center)](https://www.chicagobooth.edu/research/kilts/research-data/nielseniq); [Open Bandit Dataset and Open Bandit Pipeline](https://github.com/st-tech/zr-obp)
- **`21_Open_Textbooks_and_Courses`**: [Marketing Science in Python: A Practitioner's Guide (companion code)](https://github.com/takechanman1228/marketing-science-in-python); [Data Analytics for Marketing: A practical guide to analyzing marketing data using Python (companion code)](https://github.com/PacktPublishing/Data-Analytics-for-Marketing); [Marketing Analytics and Data Science: Tools and Models (supplementary code)](https://link.springer.com/book/9783032111296); [Applied Marketing Analytics Using Python](https://collegepublishing.sagepub.com/products/applied-marketing-analytics-using-python-1-288563); [Machine Learning and Generative AI for Marketing (companion code)](https://github.com/PacktPublishing/Machine-Learning-and-Generative-AI-for-Marketing); [Ad response tutorial: last-click attribution, experiments, MMM and attribution models](https://github.com/eleafeit/ad_response_tutorial); [Customer Analytics (Wharton, Coursera)](https://www.coursera.org/learn/wharton-customer-analytics); [Darden Business Publishing (cases, simulations, course packs)](https://store.darden.virginia.edu/); [Marketing Science Institute library (free working papers)](https://www.msi.org/library/)
