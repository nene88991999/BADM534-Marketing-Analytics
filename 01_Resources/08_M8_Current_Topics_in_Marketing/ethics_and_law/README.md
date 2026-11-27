# Marketing Tactics, Consumer Harm, and the Law

**Marketing Analytics · course note for M8 (Current Topics), with an "ethics and law check" for M1–M7**

*Status of every rule, case and bill below was checked on 2 November 2026. Laws in this area are moving quickly (several items are pending), so recheck before each term. This note is teaching material, not legal advice.*

---

## Why This Belongs in an Analytics Course

The tools in this course are the same tools behind most of the conduct regulators now pursue. A/B tests tune cancellation flows, CLV models decide who gets a retention pitch, propensity models set personalised prices, text models write reviews, and LLM agents now do all of this faster. The largest consumer-protection settlement the FTC has ever obtained under the Restore Online Shoppers' Confidence Act, **$2.5 billion from Amazon in September 2025**, was about a sign-up and cancellation interface: a product that analytics teams design, test and optimise.

Under opposed firm and consumer interests, fixed stakes, and the specified choice-response model, selecting the procedure with the highest purchase rate also selects the largest consumer loss within the tested set. The firm's gain equals the consumer's loss rescaled by the ratio of their stakes. This conditional comparison directs attention to the objective and the available procedures. Ethical justification requires reasons concerning affected people; compliance with law supplies a separate assessment.

Three questions for every project in the course:

1. **Whose interest does the optimisation target serve, and can it run against the customer's?** (Renewals of a subscription the customer would rather cancel; purchases at a price set from their data.)
2. **Would the customer agree to the procedure if they could see it?** (Could they refuse the retention questions, see the fee, know the price was personalised?)
3. **Which law already covers it, and who can sue?** (The FTC, a state attorney general, a class of consumers, a competitor.)

---

## The Legal Backbone

### United States: Federal

| Law | What it covers | Who enforces; what it costs |
|---|---|---|
| **FTC Act §5**, [15 U.S.C. §45](https://www.law.cornell.edu/uscode/text/15/45) | *Deceptive* acts: a representation or omission likely to mislead a reasonable consumer, that is material ([FTC Policy Statement on Deception, 1983](https://www.ftc.gov/legal-library/browse/ftc-policy-statement-deception)). *Unfair* acts: substantial injury, not reasonably avoidable, not outweighed by benefits (§45(n)). Objective claims need a reasonable basis (substantiation) *before* they are made. | FTC. Since *AMG Capital Management v. FTC* (2021) the FTC cannot get money under §13(b) ([CRS summary](https://www.everycrsreport.com/reports/LSB10596.html)). Money now comes mainly through **rule violations**: civil penalties of up to **$53,088 per violation** (2025 level, [kept unchanged for 2026](https://public-inspection.federalregister.gov/2026-18853.pdf)) plus consumer redress. Hence the importance of the trade-regulation rules below. |
| **ROSCA**, [15 U.S.C. §§8401–8405](https://www.law.cornell.edu/uscode/text/15/chapter-110) | Online negative options (free trials, auto-renewals): disclose material terms before billing, get express informed consent, give a simple way to stop charges. | FTC (violations are treated as rule violations, so civil penalties apply) and state AGs. |
| **Rule on Unfair or Deceptive Fees**, [16 CFR Part 464](https://www.ecfr.gov/current/title-16/part-464) | All-in price display for **live-event tickets and short-term lodging**; effective 12 May 2025. | FTC; civil penalties. |
| **Consumer Reviews and Testimonials Rule**, [16 CFR Part 465](https://www.ecfr.gov/current/title-16/part-465) | Bans fake or AI-fabricated reviews, buying reviews conditioned on sentiment, undisclosed insider reviews, company-run "independent" review sites, review suppression, and fake followers or views. Effective 21 October 2024. | FTC; civil penalties. Warning letters to ten companies on [22 December 2025](https://www.beneschlaw.com/insight/five-stars-zero-tolerance-ftc-turns-up-enforcement-under-consumer-review-rule/). |
| **Negative Option Rule**, 16 CFR Part 425 | The 2024 "click-to-cancel" amendments ([final rule](https://www.govinfo.gov/content/pkg/FR-2024-11-15/pdf/2024-25534.pdf)) were **vacated by the Eighth Circuit on 8 July 2025** (*Custom Communications v. FTC*). The FTC restarted with an [advance notice of proposed rulemaking on 13 March 2026](https://www.govinfo.gov/content/pkg/FR-2026-03-13/pdf/2026-04952.pdf), which asks whether **save offers instead of honouring a cancellation** are unfair or deceptive and requests data on acceptance rates, savings and cancellation delays. | No new requirements yet; ROSCA and §5 still apply. |
| **Endorsement Guides**, [16 CFR Part 255](https://www.ecfr.gov/current/title-16/part-255) (revised 2023) | Influencer and employee endorsements need clear disclosure of material connections; brands are responsible for their influencers. | Guides are not binding rules, but they describe how the FTC reads §5. |
| **COPPA Rule**, [16 CFR Part 312](https://www.ecfr.gov/current/title-16/part-312) | Children under 13. The amended rule (published 22 April 2025) requires **separate parental consent before disclosing children's data to third parties for targeted advertising**, limits retention, and adds biometric identifiers; compliance was due **22 April 2026**. | FTC and state AGs; civil penalties. |
| **Green Guides**, [16 CFR Part 260](https://www.ecfr.gov/current/title-16/part-260) | Environmental claims ("recyclable", "carbon neutral"). | Guides; enforced through §5. |
| **TCPA**, [47 U.S.C. §227](https://www.law.cornell.edu/uscode/text/47/227) | Autodialled or prerecorded marketing calls and texts without prior express consent. | **Private right of action, $500–$1,500 per call or text**: the main source of marketing class actions. The FCC's one-to-one consent rule was vacated by the Eleventh Circuit in January 2025, and after *McLaughlin Chiropractic v. McKesson* (2025) courts are not bound by FCC interpretations ([overview](https://www.troutman.com/insights/why-does-the-tcpa-equal-chaos-the-us-supreme-court-opens-fcc-orders-to-new-challenges.html)). |
| **Lanham Act §43(a)**, [15 U.S.C. §1125](https://www.law.cornell.edu/uscode/text/15/1125) | False or misleading advertising about your own or a competitor's product. | **Competitors** sue (and use NAD self-regulation): a comparison-ad claim built on a weak regression is a litigation risk. |

**Who is enforcing.** In *Trump v. Slaughter* (29 June 2026, 6–3) the Supreme Court overruled *Humphrey's Executor*: the President can now remove FTC commissioners at will ([summary](https://www.venable.com/insights/publications/2026/06/supreme-court-overrules-humphreys-executor)). Federal priorities can therefore shift with each administration. Subscription traps and junk fees have nonetheless been pursued under both recent administrations (Amazon settled under the current FTC; Uber was sued in April 2025). **State attorneys general and private plaintiffs** carry an increasing share of enforcement.

### United States: States (Illinois First)

| Law | What it covers | Note |
|---|---|---|
| **Illinois Consumer Fraud and Deceptive Business Practices Act**, [815 ILCS 505](https://www.ilga.gov/legislation/ilcs/ilcs3.asp?ActID=2356&ChapterID=67) | Illinois's UDAP statute: deceptive and unfair practices. | AG enforcement and a **private right of action**. The Illinois AG was co-plaintiff in the Grubhub case below. |
| **Illinois Automatic Contract Renewal Act**, 815 ILCS 601 ([P.A. 102-0517](https://ilga.gov/Legislation/publicacts/view/102-0517)) | Clear disclosure of auto-renewal terms; renewal notices for longer contracts; **consumers who sign up online must be able to cancel exclusively online** (since 1 January 2022). | Applies to every subscription product sold to Illinois consumers. |
| **Illinois Biometric Information Privacy Act**, [740 ILCS 14](https://www.ilga.gov/legislation/ilcs/ilcs3.asp?ActID=3004&ChapterID=57) | Written consent before collecting face, voice or fingerprint data. | Private right of action, **$1,000 per negligent and $5,000 per intentional or reckless violation**; a 2024 amendment counts repeated collection from one person as a single violation ([summary](https://www.seyfarth.com/news-insights/bipa-legislative-update-governor-pritzker-signs-amendment-limiting-damages-to-a-single-recovery-1.html)). |
| **California Automatic Renewal Law**, Bus. & Prof. Code §17602 ([AB 2863](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240AB2863)) | From 1 July 2025: a retention offer may appear only next to a prominent, continuously displayed cancellation button, and cancellation must be processed promptly when the button is used. | |
| **Minnesota**, [Stat. §325G.58](https://www.revisor.mn.gov/statutes/cite/325G.58) | The business must **ask permission once** before presenting retention offers after a cancellation request; optional questions about reasons for leaving are allowed. | The closest existing law to a "right to refuse the retention conversation". |
| **CCPA Regulations**, Cal. Code Regs. tit. 11, §7004 | Privacy choices must be **symmetrical** (opting out no harder than opting in); consent obtained through dark patterns is not consent. | California Privacy Protection Agency: Honda, $632,500 (March 2025), for asymmetric choices among other violations ([summary](https://www.hunton.com/privacy-and-cybersecurity-law-blog/cppa-fines-honda-632-500-for-ccpa-violations)); Todd Snyder, $345,178 (May 2025), for a broken cookie opt-out. |
| **New York Algorithmic Pricing Disclosure Act**, Gen. Bus. Law §349-a | In force since November 2025: a price set by an algorithm using the customer's personal data must carry the notice "THIS PRICE WAS SET BY AN ALGORITHM USING YOUR PERSONAL DATA." | A First Amendment challenge by the National Retail Federation failed in district court; the appeal (*NRF v. James*) was argued in the Second Circuit on 19 October 2026, with a decision pending ([summary](https://www.kelleydrye.com/viewpoints/blogs/ad-law-access/surveillance-pricing-key-concepts-the-current-legal-and-legislative-landscape-and-mounting-scrutiny.md)). |
| **Surveillance-pricing bans** | Enacted: **Maryland** HB 895 (grocery stores and delivery apps, in force since 1 October 2026), **Connecticut** PA 26-130 (retailers broadly, signed June 2026, effective 1 July 2027), **New Jersey** A4085 (grocery, signed July 2026, effective 1 August 2027) ([overview](https://www.route-fifty.com/finance/2026/08/states-begin-banning-surveillance-pricing-uses-personal-data-charge-more/415219/)). **New York's One Fair Price Act** (A9349/S8623) passed the legislature on 4 June 2026 and, at the time of writing, had not yet been delivered to the Governor; action is customarily taken by year-end ([summary](https://www.wsgrdataadvisor.com/2026/06/new-york-legislature-passes-ban-on-personalized-pricing/)). | Most bans exempt loyalty programmes, coupons and cost-based differences, so the line between a "discount" and "surveillance pricing" is the live question. |

### Europe and the UK

| Law | What it covers | Note |
|---|---|---|
| **Unfair Commercial Practices Directive**, [2005/29/EC](https://eur-lex.europa.eu/eli/dir/2005/29/oj/eng) | General ban on misleading and aggressive practices, plus a blacklist (Annex I). Point 7 bans **falsely claiming a product will be available only for a very limited time** to rush a decision. | Member-state enforcement. |
| **Empowering Consumers for the Green Transition Directive**, 2024/825 | Amends the UCPD: bans generic environmental claims ("eco-friendly") without recognised excellent performance, and unverified sustainability labels; **applies from 27 September 2026** ([status](https://www.mayerbrown.com/en/insights/publications/2026/10/the-eu-directive-on-empowering-consumers-for-the-green-transition-two-years-on-what-it-requires-and-where-the-member-states-stand)). | |
| **Digital Services Act**, Regulation 2022/2065 | Platforms may not use interface design that deceives or manipulates users. | First DSA fine: **X, €120 million (5 December 2025)**, partly for the "deceptive design" of paid blue checkmarks ([Commission](https://digital-strategy.ec.europa.eu/en/news/commission-fines-x-eu120-million-under-digital-services-act)). |
| **AI Act**, [Regulation 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj), Art. 5 | Since 2 February 2025: bans AI systems using subliminal, manipulative or deceptive techniques, or exploiting age, disability or economic vulnerability, that materially distort behaviour and cause significant harm. | Fines up to €35 million or 7% of global turnover. |
| **Digital Fairness Act** (proposal) | Expected from the Commission in **mid-November 2026**: dark patterns, addictive design, unfair personalisation, influencer marketing, price presentation, hard-to-cancel subscriptions ([preview](https://eurobytenews.com/article/digital-fairness-act-proposal-due/)). | Not yet published at the time of writing. |
| **UK Digital Markets, Competition and Consumers Act 2024** | Since April 2025 the CMA can fine directly, up to **10% of global turnover**. First consumer-law infringement decisions: AA and BSM driving schools, £4.2 million for drip pricing; Marks Electrical, £720,000 for pre-ticked add-ons; StubHub, £889,200 for hidden mandatory fees (both June 2026) ([summary](https://www.mayerbrown.com/en/insights/publications/2026/08/were-just-getting-started-the-cmas-new-consumer-enforcement-powers-in-action)). | |

---

## The Crosswalk: Tactic → Harm → Law → Case → Module

The same table, with discussion questions, is in [`crosswalk.csv`](crosswalk.csv) for the wiki.

### 1. Subscription Traps and Retention Flows (M4, M6)

**The tactic.** Easy sign-up, hard exit: many cancellation steps, phone-only cancellation, save offers and questions placed before the cancel button, renewals billed without notice.

**The harm.** Inertia does the selling. Using card data on passive renewal, [Einav, Klopack and Mahoney (2025, *AER*)](https://doi.org/10.1257/aer.20231612) estimate that cancellation frictions roughly double seller revenue, holding initial subscribers fixed. [Miller, Sahni and Strulov-Shlain](https://bfi.uchicago.edu/working-paper/sophisticated-consumers-with-inertia-long-term-implications-from-a-large-scale-field-experiment/) find in a large field experiment that auto-renewal lifts short-run revenue, but many consumers anticipate their own inertia and turn down auto-renewal offers or put off subscribing; after a year revenue is about the same and there are fewer subscribers. The course experiment compares retention questions under opposed firm and consumer interests. Within its specified choice-response model and fixed stakes, selecting the highest purchase rate also selects the greatest consumer loss among the procedures tested.

**The law.** ROSCA; FTC Act §5; state renewal laws (Illinois 815 ILCS 601, California §17602, Minnesota §325G.58); the FTC's March 2026 rulemaking notice on save offers.

**Cases.** *FTC v. Amazon* (Prime): $2.5 billion ($1 billion civil penalty plus $1.5 billion refunds), 25 September 2025. The complaint described manipulative "dark patterns" in enrolment and a deliberately complicated cancellation path; the order requires a clear "decline" option and a simple cancellation ([summary](https://www.khlaw.com/insights/amazon-pay-record-25-billion-settle-ftc-claims-deceptive-prime-membership-signup-and)). *FTC v. Uber* (Uber One): filed April 2025, 21 states joined in December 2025; the complaint counts up to 32 actions to cancel, and most claims survived a motion to dismiss in the Northern District of California ([report](https://www.courthousenews.com/judge-allows-most-ftc-claims-against-uber-to-survive/)).

**Discussion.** A retention flow raises 12-month renewals by 8 points in an A/B test. What would you need to measure before calling that a success? (Hint: a direct-cancellation arm, an independent measure of what renewing is worth to these customers, and whether the cancel button was reachable before the questions.)

### 2. Drip Pricing and Junk Fees (M3, M4)

**The tactic.** Advertise a low base price and reveal mandatory fees at checkout.

**The harm.** Shrouded attributes survive competition ([Gabaix and Laibson 2006](https://doi.org/10.1162/qjec.2006.121.2.505)). In a large StubHub experiment, showing fees only at checkout raised spending and the probability of purchase ([Blake, Moshary, Sweeney and Tadelis 2021](https://doi.org/10.1287/mksc.2020.1261)); see also [Santana, Dallas and Morwitz (2020)](https://doi.org/10.1287/mksc.2019.1207) on how consumers react once they notice.

**The law.** FTC fees rule (tickets and lodging); §5 elsewhere; state UDAP laws; UCPD; UK DMCC Act.

**Cases.** *FTC and Illinois AG v. Grubhub* (December 2024): $140 million judgment, largely suspended, $25 million paid, over hidden fees and other practices ([summary](https://crowell.com/en/insights/client-alerts/lessons-for-e-commerce-and-retail-from-the-ftc-and-illinois-ags-proposed-dollar140-million-settlement-against-grubhub)). *FTC v. Live Nation and Ticketmaster* (filed September 2025, C.D. Cal.): advertised prices that omit mandatory fees, plus resale practices; the motion to dismiss was denied in September 2026 and the parties have proposed 2028 trial dates ([status](https://www.ticketnews.com/2026/10/ftc-live-nation-ticketmaster-jury-trial/)). CMA: StubHub, AA and BSM (above).

**Discussion.** Your conjoint study shows customers are less price-sensitive to a "service fee" than to the base price. Is using that finding legal in your industry? Is it ethical?

### 3. Fake, Bought and Suppressed Reviews (M5)

**The tactic.** Buy or write reviews, pay only for five-star ones, hide negative reviews, buy followers, generate reviews with an LLM.

**The harm.** Reviews are the main quality signal online; fakes shift demand to worse products. Facebook-group review markets raise sales briefly while quality ratings later fall ([He, Hollenbeck and Proserpio 2022](https://doi.org/10.1287/mksc.2022.1353)); review fraud rises when reputations weaken and competition grows ([Luca and Zervas 2016](https://doi.org/10.1287/mnsc.2015.2304)); see also [Mayzlin, Dover and Chevalier 2014](https://doi.org/10.1257/aer.104.8.2421).

**The law.** 16 CFR Part 465 (civil penalties per violation); FTC Act §5; UK DMCC Act.

**Cases.** *Fashion Nova*: $4.2 million (2022) for suppressing negative reviews ([report](https://www.fox26houston.com/news/fashion-nova-to-pay-4-2m-to-settle-claims-it-blocked-negative-online-reviews)). *Rytr* (2024, Operation AI Comply): an AI writing tool marketed for generating testimonials. December 2025 warning letters under Part 465.

**Discussion.** You built an M5 model that detects fake reviews. Could the same pipeline write undetectable ones? What does Part 465 say about a business that "should have known" its reviews were fake?

### 4. Undisclosed Influencer and Native Advertising (M5)

**The tactic.** Paid posts without clear disclosure; employees or affiliates posting as ordinary customers.

**The harm.** Consumers discount ads but not recommendations. Disclosure rules changed how sponsored content performs on Instagram ([Ershov and Mitchell 2020](https://doi.org/10.1145/3391403.3399477)).

**The law.** Endorsement Guides (16 CFR 255); §5; the UCPD's ban on disguised advertising; the coming EU Digital Fairness Act.

**Discussion.** You find that undisclosed posts drive 40% more clicks than disclosed ones. What, if anything, should you do with that estimate?

### 5. Manufactured Urgency, Nagging and Confirmshaming (M6, M8)

**The tactic.** Fake countdown timers, "only 2 left", repeated offers after a "no", "No thanks, I don't like saving money" buttons.

**The harm.** A crawl of 11,000 shopping sites found fake urgency and scarcity among the most common dark patterns ([Mathur et al. 2019](https://doi.org/10.1145/3359183)). In experiments, mild dark patterns roughly doubled acceptance of a dubious offer and aggressive ones nearly quadrupled it ([Luguri and Strahilevitz 2021](https://academic.oup.com/jla/article/13/1/43/6180579)). Time-scarcity promotions online have mixed effects on sales ([Hmurovic, Lamberton and Goldsmith 2023](https://doi.org/10.1177/00222437221118856)). The course choice model gives a conditional welfare comparison. A false belief that the offer may expire discourages a worthwhile second look, so the consumer's loss equals the value of the review she skipped. A seller who keeps returning to refusals and stops at the first "yes" can push conversion toward 100%, but those sales are fragile. If one more return converts 30% of initial refusers, at least 30% of those converts would reverse when given a chance to reconsider.

**The law.** FTC Act §5 (a false deadline is a false claim); UCPD Annex I point 7; DSA deceptive-design ban for platforms; the FTC's [2022 staff report on dark patterns](https://www.ftc.gov/system/files/ftc_gov/pdf/P214800%20Dark%20Patterns%20Report%209.14.2022%20-%20FINAL.pdf).

**Cases.** *Epic Games* (Fortnite): $245 million in refunds over billing dark patterns, alongside a $275 million COPPA penalty (December 2022) ([report](https://www.pbs.org/newshour/amp/nation/fortnite-maker-epic-games-to-settle-ftc-case-pay-520-million-in-penalties-and-refunds)).

**Discussion.** Design an experiment that tells apart "the timer made people decide faster" from "the timer made people decide worse". Give a randomly chosen group an opportunity to reconsider and assess what reversals reveal under the stated assumptions.

### 6. Personalised ("surveillance") and Algorithmic Pricing (M4, M7)

**The tactic.** Prices set per customer from browsing, location, device or purchase history; or competitors using a common pricing algorithm.

**The harm.** Personalised pricing can raise profits and help some consumers while hurting others ([Dubé and Misra 2023, *JPE*](https://doi.org/10.1086/720793)). Algorithms can learn to sustain supracompetitive prices ([Calvano et al. 2020](https://doi.org/10.1257/aer.20190623)), and German gasoline stations' margins rose after both stations in a duopoly adopted algorithmic pricing ([Assad et al. 2024](https://doi.org/10.1086/726906)).

**The law.** New York §349-a disclosure; state surveillance-pricing bans (Maryland, Connecticut, New Jersey; New York pending); FTC Act §5; antitrust. The FTC's [surveillance-pricing study](https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-surveillance-pricing-study-indicates-wide-range-personal-data-used-set-individualized-consumer) (initial findings January 2025) documents the data used. In *U.S. v. RealPage* the DOJ's proposed settlement (24 November 2025) bars using competitors' nonpublic data in live rent recommendations ([summary](https://www.fenwick.com/insights/publications/dojs-realpage-settlement-a-blueprint-for-safer-algorithmic-pricing)).

**Discussion.** Your M7 model predicts willingness to pay from a customer's zip code and device. Under New York's disclosure law and Connecticut's ban (effective July 2027), which uses require a disclosure, and which are banned? Which exemptions (loyalty discounts, coupons) would your design rely on?

**Data and Code.** The [public earnings-call example](../../../03_Data_and_Code/Earnings_Calls/README.md) contains 2,326 call records and 971 dictionary-match records. Its documentation distinguishes the firm roster, observed calls, matching rules, source-linked paraphrases, and original transcript excerpts retained locally. Use the executed coverage and interpretation checks before treating a mention as evidence of actual pricing practice.

### 7. Data Collection, Consent and Privacy (M1, M2)

**The tactic.** Pre-ticked consent, buried opt-outs, collecting more than needed, biometric capture without consent, scraping in breach of terms.

**The harm.** Loss of control over personal data; costs are hard for consumers to see ([Acquisti, Taylor and Wagman 2016](https://doi.org/10.1257/jel.54.2.442)). Consent pop-up design changes consent rates dramatically ([Nouwens et al. 2020](https://doi.org/10.1145/3313831.3376321)). Regulation has costs too: the GDPR reduced the data and trackers available to firms and increased market concentration among vendors ([Johnson, Shriver and Goldberg 2023](https://doi.org/10.1287/mnsc.2023.4709); [Aridor, Che and Salz 2023](https://doi.org/10.1111/1756-2171.12455)).

**The law.** CCPA regulations (symmetry in choice); Illinois BIPA; COPPA; GDPR in Europe.

**Cases.** CPPA: Honda and Todd Snyder (above). *FTC v. Rite Aid* (December 2023): five-year ban on facial recognition after false-positive matches that disproportionately affected some groups ([summary](https://www.mayerbrown.com/de/insights/publications/2023/12/more-than-a-ban-on-facial-recognition-use-the-us--ftcs-rite-aid-action-and-proposed-stipulated-order)).

**Course tie-in.** The McBroken lab (M2) is a good place to discuss terms of use and polite collection; the Open e-commerce dataset forbids re-identification of participants, and its authors' [CSCW 2024 experiment](https://arxiv.org/abs/2404.13172) measures what it takes for people to share their data. On the AI-coding side (M1): never paste customer data into an AI tool the university has not approved.

### 8. Children and Vulnerable Consumers (M8)

Loot boxes and virtual currencies that hide real prices; targeted advertising to minors. *HoYoverse (Genshin Impact)*: $20 million (January 2025) under COPPA and for deceptive loot-box odds, with a ban on selling loot boxes to under-16s without parental consent ([report](https://androidauthority.com/genshin-impact-loot-box-fine-3517760)). The amended COPPA Rule and the EU AI Act's ban on exploiting age-related vulnerabilities also apply.

### 9. Claims About AI ("AI Washing") and AI-enabled Deception (M7, M8)

**Cases.** FTC Operation AI Comply (September 2024 onwards): DoNotPay's "robot lawyer", Rytr, and AI "passive income" schemes. Under the current FTC: *Workado*, which advertised 98% accuracy for an AI-content detector the FTC found was about 53% accurate (2025); *Air AI* (August 2025) ([summary](https://www.beneschlaw.com/insight/one-year-in-ftcs-operation-ai-comply-continues-under-new-administration-signaling-enduring-enforcement-focus/)). Cox Media Group and two partners agreed to pay $930,000 over an "Active Listening" ad product that claimed to target ads from conversations captured by smart devices (order finalised August 2026).

**Discussion.** Students' own products count too. If your M7 model has 71% hold-out accuracy, what may you say about it in a pitch? Substantiation applies to accuracy claims exactly as it does to "clinically proven".

### 10. Discrimination Through Targeting and Delivery (M7)

**The harm.** Cost-optimised ad delivery showed a gender-neutral STEM job ad to fewer women, because women are more expensive to reach ([Lambrecht and Tucker 2019](https://doi.org/10.1287/mnsc.2018.3093)); Facebook's delivery skewed audiences by race and gender even with neutral targeting ([Ali et al. 2019](https://doi.org/10.1145/3359301)).

**The law.** Fair Housing Act, Equal Credit Opportunity Act and employment law for housing, credit and job ads; civil-rights provisions in several surveillance-pricing bills. *United States v. Meta Platforms* (S.D.N.Y., settled June 2022): Meta agreed to replace its housing-ad tool and build a system to reduce demographic skew in delivery ([DOJ case page](https://www.justice.gov/crt/case/united-states-v-meta-platforms-inc-fka-facebook-inc-sdny)).

### 11. Environmental Claims (M5, M8)

Green Guides in the U.S.; from 27 September 2026 the EU bans generic environmental claims and uncertified sustainability labels. A good M5 text exercise: classify product-page claims as specific, generic or unverifiable.

### 12. Experiments On Customers (M6)

A/B testing is legal and usually beneficial, but a test that randomises customers into a deceptive variant is a deceptive practice for everyone in that arm. People often object to experiments even when they accept either policy on its own ([Meyer et al. 2019, *PNAS*](https://doi.org/10.1073/pnas.1820701116)). The course model gives a conditional warning: with opposed interests, "ship the winner" selects the most harmful variant tested.

---

## Choice, Experimentation, and Consumer Interests

A firm can choose which questions precede an offer, which refusals are reopened, and when an interaction ends. Under opposed interests, fixed stakes, and stable procedure-specific responses, selecting the highest purchase rate can also select the largest consumer loss within the tested set. The conclusion depends on the specified welfare comparison and choice process. The [lecture notes](../../../06_Lecture_Notes/README.md) provide the assumptions, complete calculations, and reasons relevant to an ethical assessment.

Evaluate the direct-choice comparison, independent evidence about customer interests, implementation of cancellation requests, and the ability to refuse optional content before exposure. Consumer authority over the interaction can matter even when final recorded choices coincide. The [Marketing Dialectics practice](../../../07_Labs/Philosophical_Arguments/README.md) develops premises, objections, and conditions for revision.

## Attention, Extraction, and the Law

Attention-funded services raise questions about what consumers give up when the monetary price is zero and how competition and consumer-protection frameworks represent that cost (Wu, 2016, 2019). The historical comparison connects the sale of audience attention to the authority consumers retain over exposure.

| Work | Use in the course |
|---|---|
| [*The Attention Merchants: The Epic Scramble to Get Inside Our Heads*](https://scholarship.law.columbia.edu/books/64/) (Knopf, 2016) | Opening reading for M8 (or M5): a history of the business model that resells captured attention to advertisers, from the penny press and posters to radio, television and social media, including the recurring public revolts when advertising overreaches. Pairs with the ad-measurement papers in M6: what exactly is being bought? |
| ["Blind Spot: The Attention Economy and the Law"](https://scholarship.law.columbia.edu/faculty_scholarship/2029/), *Antitrust Law Journal* 82(3): 771 (2019) | Attention is a scarce resource. "Attention brokers" offer free services and sell access to the resulting audience, and regulators have struggled to analyse those markets because no money changes hands with the user. Voluntary exchanges differ from **captive exposure** (Wu, 2019). The essay ["The Crisis of Attention Theft"](https://www.wired.com/2017/04/forcing-ads-captive-audience-attention-theft-crime/) (2017) gives a short, readable version of that consent distinction. **Class point:** ad load is a price. A retention question or an interstitial costs the customer time even when the purchase does not change; a purchase-effect comparison can hold that cost fixed, while a fuller welfare calculation includes it. |
| [*The Age of Extraction*](https://www.penguinrandomhouse.com/books/691177/the-age-of-extraction-by-tim-wu/) (Knopf, November 2025) | Platforms that began as conveniences now extract money, data and attention from users and the businesses that depend on them. A frame for the junk-fee, marketplace-fee and surveillance-pricing rows of the crosswalk. |
| ["Machine Speech"](https://scholarship.law.columbia.edu/faculty_scholarship/1833/), *University of Pennsylvania Law Review* 161 (2013) | When is an algorithm's output the designer's protected speech, and when is it a functional tool? Background for the First Amendment arguments that recur whenever states regulate algorithms, such as the retailers' challenge to New York's algorithmic-pricing disclosure. |
| ["Will Artificial Intelligence Eat the Law? The Rise of Hybrid Social-Ordering Systems"](https://columbialawreview.org/content/will-artificial-intelligence-eat-the-law-the-rise-of-hybrid-social-ordering-systems/), *Columbia Law Review* 119 (2019) | Automated systems need mechanisms that send hard cases to human judgment, and a nominal human in the loop can coexist with real disempowerment. For M7: when your model or AI agent decides who gets a refund, a retention offer or a price, who can trigger human review? |
| "The Tyranny of Convenience", *New York Times* (2018) | Convenience as a design ideology: easy defaults shape what people do. The asymmetry between one-click sign-up and multi-step cancellation is the crosswalk's first row. |

**Policy history worth telling.** Wu served at the White House National Economic Council in 2021–2023 and helped write Executive Order 14036, *Promoting Competition in the American Economy* (9 July 2021). The order pushed agencies on, among other things, the right to repair, which links to the US Copyright Office's 2024 repair exemption in the McBroken lab. It was revoked on 13 August 2025 by Executive Order 14337 ([history](https://en.wikipedia.org/wiki/Executive_Order_14036)). Together with *Trump v. Slaughter*, it is a compact lesson that the federal side of this map can change within one degree programme, while state laws and private litigation persist.


---

## Suggested Use

**A 10-minute "ethics and law check" closing each module.**

| Module | Check |
|---|---|
| M1 Python and AI coding | Which AI tools may touch customer data (UIUC's approved-tools list); never paste personal data into an unapproved assistant. |
| M2 Customer data and visualisation | Consent and data minimisation; CCPA symmetry; BIPA; terms of use and scraping etiquette (McBroken lab); re-identification bans (Open e-commerce data). |
| M3 Regression | Substantiation: an advertised claim ("cuts costs 30%") needs evidence that would survive an FTC or Lanham Act challenge. |
| M4 Conjoint, segmentation, CLV | Retention targeting and cancellation law; fee presentation; personalised-pricing disclosures and bans. |
| M5 Text and social media | Fake reviews (Part 465); influencer disclosure; LLM-generated content; environmental claims. |
| M6 Experiments | Testing a deceptive variant is itself deceptive; the experimentation-selects-harm result; designing audits with a direct-choice arm and a reconsideration opportunity. |
| M7 Prediction, ML and AI | Algorithmic pricing (disclosure, bans, antitrust); discriminatory delivery; AI capability claims. |
| M8 Current topics | The full session below. |

**A 75-minute M8 session.**

0. (Before class) Read Wu, "Blind Spot" sections I–II, or the "Attention Theft" essay; skim the Amazon settlement summary.
1. (10 min) Amazon Prime: the complaint's description of the sign-up and cancellation flows, and the settlement terms. Ask: what was the A/B-test metric?
2. (20 min) Agency erosion model: the 20% → 10–60% example, the $4/$5 welfare numbers, and why experimentation selects harm.
3. (15 min) Law map: FTC Act §5 and ROSCA, the vacated click-to-cancel rule and the 2026 notice, Illinois/California/Minnesota cancellation laws, the EU and UK.
4. (20 min) Groups audit a real flow (a streaming or gym cancellation) using the audit checklist above, then draft one paragraph of an FTC comment answering the March 2026 notice's question on save offers.
5. (10 min) Surveillance pricing: a bill vote on New York's One Fair Price Act exemptions.

**Assignment: a one-page legal and ethical risk memo for each term project.** Identify the optimisation target; whether it can oppose customer interests; the applicable rules (federal, Illinois, plus any other state or country where customers are); the worst plausible enforcement headline; and the design change that removes the risk at least cost.

---

## Further Reading

- FTC staff, [*Bringing Dark Patterns to Light*](https://www.ftc.gov/system/files/ftc_gov/pdf/P214800%20Dark%20Patterns%20Report%209.14.2022%20-%20FINAL.pdf) (2022).
- Calo, R. (2014), "Digital market manipulation", *George Washington Law Review* 82(4): 995–1051.
- Susser, D., Roessler, B. and Nissenbaum, H. (2019), "Online manipulation: hidden influences in a digital world", *Georgetown Law Technology Review* 4(1).
- Sunstein, C. R. (2022), [Sludge audits](https://doi.org/10.1017/bpp.2019.32), *Behavioural Public Policy* 6(4): 654–673.
- Rao, A. and Wang, E. (2017), [Demand for "healthy" products: false claims and FTC regulation](https://doi.org/10.1509/jmr.15.0398), *Journal of Marketing Research* 54(6): 968–989, a quantitative-marketing study of what happens to demand after the FTC acts on false claims.
- DellaVigna, S. and Malmendier, U. (2006), [Paying not to go to the gym](https://doi.org/10.1257/aer.96.3.694), *American Economic Review* 96(3): 694–719, the classic on contract choice and inertia.

*Prepared 2 November 2026 for Marketing Analytics. Sources are linked inline; statuses marked "pending" or "at the time of writing" should be rechecked before teaching.*
