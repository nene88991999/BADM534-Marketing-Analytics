# What MBA 542 can contribute to BADM 534

*Assessment of the two Box folders (`2026_Spring_Yang`, `2026_Spring2_Yang`), 2026-10-23.*

## Bottom line

MBA 542 overlaps with BADM 534 less in topic than in **method**. Its live sessions already run the loop BADM 534 needs: hand students a small, purpose-built dataset, let an LLM do the first pass, then make them judge the output. The difference is the tooling. In MBA 542 students upload a CSV to ChatGPT and ask questions ("no coding is required"). In BADM 534 they use an AI coding assistant to write and verify the analysis code themselves. Most of the reusable value is in that scaffolding:

- the synthetic datasets
- the prompt → breakout → debrief activity pattern
- the LLM-use guide
- the AI-assisted grading prompts
- about 30 lecture scripts that can become first drafts of wiki pages

None of the 60 videos needs to move. The scripts carry the same content as text, which suits a wiki better.

## Crosswalk

| MBA 542 asset | Where it fits in BADM 534 | Recommended use |
|---|---|---|
| **Synthetic grocery trips** (2 variants × 1,000 trips: date, Instacart vs in-person, basket string) | M2 customer data and wrangling; M4 basket segmentation; M6 online-vs-offline comparison | **Copy.** Ideal first AI-assisted coding exercise: parse basket strings, compute size, variety and repetition by channel. Pairs with Chintala, Liaukonytė & Yang (2024). |
| **Synthetic Netflix viewing profile** (500 events, 9 columns) | M7 recommender systems; M2 visualization | **Copy.** Upgrade the MBA 542 "describe it to ChatGPT" prompt into code: content-based recommender, then a diversity-aware re-rank. |
| **Synthetic Substack natural-health posts** (180 posts: claim intensity, citation style, engagement, excerpt) | M5 LLM text classification; M3 regression (engagement on claim intensity); M8 data poisoning | **Copy.** Strong M5 and M3 bridge: label excerpts with an LLM API, validate a sample by hand, then regress engagement on the labels. |
| **TikTok livestream transcripts A/B** | M5 LLM annotation (expertise, authenticity, parasocial cues) | **Copy.** Small enough to hand-code, which makes a clean exercise in validating LLM annotations. |
| **Starbucks.zip** (16 Instagram images) | M5 extension to image data | **Reference only.** These are brand-owned social images: fine for a closed class session, not for a public GitHub wiki. |
| **Live-session prompt files** (8 × 4 questions) | In-class activity templates for every module | **Copy.** Keep the question structure and add a coding step ("now write code that reproduces the LLM's claim"). |
| **Breakout sheets** (BR1/BR2 per module) and **group-activity debriefs** | Wiki activity pages; post-class synthesis pages | **Copy.** The debriefs (aggregate findings, no student names) are exactly the "what we learned" page format a wiki can carry. |
| **Optimal LLM Usage Guide** (3 pp.) | Folder 12 policy; the wiki's AI-use page | **Copy and adapt.** The core rules carry over: thinking aid, not answer engine; ask "what could be wrong?"; you must be able to defend it. It needs a coding section: verify by running, test, and log prompts. |
| **TA grading prompts** (master prompt plus per-module rubric prompts) | Folder 12: AI-assisted grading of the essay assignment and project reports | **Copy and adapt.** This partly fills the "no rubric for AI-assisted coding" gap: reuse the format and add criteria for correctness, reproducibility and disclosure. |
| **Fall 2026 Canvas update** (post-semester changes) | 00_Index design notes | **Copy the lessons, not the document.** Free tiers must suffice. Onboard tools in week 1. Size tasks to free-tier upload limits. Map every assignment to the content that teaches it. Don't require skills the materials don't cover, which is the main risk for a coding-heavy BADM 534. |
| **Lecture scripts, MOOC 2 Module 1: Recommendation Systems** (6 + Instacart case) | M7 | **Copy.** First drafts for the recommender wiki page: trust, diversity, multi-objective design, evaluation. |
| **Lecture scripts, MOOC 2 Module 4: Measurement Challenges** (6) | M6 (data gaps, attribution bias → why experiments); M8 and AI track (data poisoning) | **Copy.** Ready-made wiki prose. *Update needed:* M2M4L2 still describes third-party cookies as deprecated in major browsers, but Chrome has since kept them. |
| **Lecture scripts, MOOC 1 Module 2: Content design, GEO, virality** (6) | M5 (text features of virality); M8 (GEO) | **Copy.** |
| **Lecture scripts, MOOC 1 Module 3: Social, influencer, livestreaming** (6) | M5 social media analytics | **Copy.** |
| **Lecture scripts, MOOC 1 Module 1: Omnichannel** (6) | M1/M2 framing for customer data | **Copy (optional).** |
| **Lecture scripts, MOOC 2 Module 2: Visual listening** (6) | M5, if you extend content analysis to images | **Optional.** |
| Lecture scripts, MOOC 1 Module 4 (AI service) and MOOC 2 Module 3 (blockchain) | M8 at most | **Skip** unless M8 covers AI service. |
| **Design Ideas** ("fix the story", "numbers to narrative", stakeholder presentation) | M2 Pyramid Principle and visualization activities; final project presentations | **Copy.** Short, directly usable. |
| **Gies Style Guide**, DM style sheet (Source Sans Pro), live-session slide backgrounds | 22_Wiki: brand colors and type for the site | **Reference** (the style guide is 19 MB; point to it in Box). |
| **Citation and Copyright Collection Form** | 22_Wiki: image and screenshot policy for a public site | **Reference.** Its table of what needs citations (CC vs public domain vs screenshots) applies to wiki images. |
| Extended Transcripts | — | **Skip.** The spot-checked file is byte-identical to its script. |
| Videos (60 files, 53 GB) | — | **Skip.** Link the public Coursera MOOCs as optional viewing if wanted. |
| Zoom chat logs | — | **Exclude.** They contain student names (FERPA). |
| Meeting notes, timelines, QC reports, production templates, rosters | — | **Skip.** Administrative. |

## Readings from MBA 542 worth adding to the BADM 534 catalog

**Done 2026-10-23.** All 17 below were added to the catalog (`_data/MBA542_READINGS.yaml`), each tagged with its BADM 534 module and noted as "Also on the MBA 542 Module N reading list."

- **M5:** Berger & Milkman (2012, JMR), "What makes online content viral?"; Lin, Yao & Chen (2021, JMR), "Happiness begets money" (emotion in live streaming); Liu, Dzyabura & Mizik (2020, *Marketing Science*), "Visual listening in"; Berger (2014, JCP), WOM review.
- **M2/M6:** Chintala, Liaukonytė & Yang (2024, *Marketing Science*), "Browsing the aisles or browsing the app?"; Narang & Shankar (2019, *Marketing Science*), mobile app introduction and purchases/returns. That is Unnati's paper, which gives continuity with the previous course and makes a clean DiD example.
- **M7:** Provost & Fawcett, *Data Science for Business*; Shani & Gunawardana, "Evaluating recommendation systems"; Adomavicius et al. (2019, MISQ), recommender biases; Chawla et al. (2002), SMOTE (imbalanced churn data).
- **M8:** Hartmann, Exner & Domdey (2025, IJRM), generative visual marketing content; Kapoor & Kumar (2025, *Marketing Science*), GenAI personalized video ads; Huang & Rust (2024, JM), "The caring machine"; Bowen et al. (2025, AAAI), data-poisoning scaling in LLMs.
- **AI-coding track:** Cotroneo et al. (2024, ICPC), targeted data-poisoning attacks on AI code generators.
- **Optional:** Dubé, Cohen, Yang & Monla (eds., 2024), *Precision Retailing*.

## Proposed placement

A single `30_From_MBA_542/` folder keeps the provenance clear and keeps your own materials apart from third-party ones. Each module README would cross-reference it:

```
30_From_MBA_542/
  datasets/              grocery A/B, Netflix, Substack, TikTok transcripts (+ data dictionary)
  activity_templates/    8 prompt files, 15 breakout sheets, 8 debriefs
  policy_and_grading/    LLM usage guide, TA grading prompts, Fall 2026 lessons learned
  lecture_scripts/       ~31 scripts (MOOC 2 M1 + Instacart case, MOOC 2 M4, MOOC 1 M1–M3)
  design/                Design Ideas
```

The total is under 5 MB.
