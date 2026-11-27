# Text, Social Media, and Networks

By Nathan Yang

Session 07. M5. 170 minutes.

[PDF](S07_Text_Social_Media_and_Networks.pdf) | [LaTeX](S07_Text_Social_Media_and_Networks.tex) | [Session Plan](SESSION_PLAN.md)

## Learning Objectives

- Define a text construct and evaluate labels on the deployment population.
- Distinguish prevalence, text exposure, retrieval, and substantive interpretation.
- Explain network reach and brokerage without inferring influence from correlation.
- Distinguish citation presence from support using a controlled source comparison.
- Trace how anchors, similarities, and persona weighting determine a text-based rating.
- Compare feature preservation, group weighting, and access at original network origins.
- Distinguish recorded-category agreement from the compatibility of a replacement text representation.
- Use contextual coding, negative cases, and source comparison to assess utility cost-recovery claims.
- Use credible qualitative mechanisms to justify proportionate inquiry.
- Distinguish engagement evidence, user endorsement, unwanted continuation, and documented research use.

## Related Materials

- [M5 lecture notes](../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md)
- [Runnable small examples](../03_Data_and_Code/Lecture_Examples/session_examples.py)
- [mHealth text code](../03_Data_and_Code/mHealth/recurring_examples/m05.py)
- [Ethics and regulation](../06_Lecture_Notes/ETHICS_AND_REGULATION.md)
- [Earnings-call worked example](../03_Data_and_Code/Earnings_Calls/README.md)
- [AI workflow calculations](../03_Data_and_Code/AI_Workflows/README.md)
- [Consumer Agency Literature and Clustering](../03_Data_and_Code/Consumer_Agency_Literature/README.md)
- [University Affiliation Clustering](../03_Data_and_Code/Consumer_Agency_Literature/AFFILIATIONS.md)
- [LLM Evidence and Revalidation](../03_Data_and_Code/LLM_Revalidation/README.md)
- [Evidence and Grader Practice](../07_Labs/AI_Evidence_and_Evaluation/README.md)
- [Retail Accessibility: Programs and Inputs](../03_Data_and_Code/Retail_Accessibility/README.md)
- [Optional Retail Access Practice](../07_Labs/Retail_Accessibility/README.md)
- [Synthetic Consumer Measurement](../03_Data_and_Code/Synthetic_Consumers/README.md)
- [Graph Coarsening: Data and Code](../03_Data_and_Code/Graph_Coarsening/README.md)
- [Graph Coarsening: Optional Practice](../07_Labs/Graph_Coarsening/README.md)
- [Representation Alignment: Programs and Results](../03_Data_and_Code/Representation_Alignment/README.md)
- [Representation Alignment: Optional Practice](../07_Labs/Representation_Alignment/README.md)
- [Evidence Standards and Optional Practice](../07_Labs/Evidence_Standards/README.md)
- [Marketing Research and Online Engagement](../01_Resources/49_Online_Engagement_and_Agency/README.md)

## Slide 1: Text, Social Media, and Networks

Marketing Analytics. By Nathan Yang.

## Slide 2: A Customer-Service Decision

- A retailer wants to detect delivery complaints quickly.
- The document may be a review, sentence, or service conversation.
- The action is a review queue with limited staff capacity.

The unit and label definition determine the evaluation. A negative review can concern price, quality, or delivery. A classifier needs a construct that identifies the service action the manager can take.

Source: M5, Section 5.1, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 3: Text Preparation

- Keep negation and domain-specific terms when they affect meaning.
- Document language, duplicates, and boilerplate.
- Fit the vocabulary on training documents.

Removing the word not can reverse a sentiment label. Duplicate descriptions across train and test can produce a favorable score for a task requiring generalization to new text.

Source: M5, Section 5.2, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 4: TF-IDF Representation

Weight a term by frequency in a document and rarity across documents.

$$
\operatorname{tfidf}_{td}=\operatorname{tf}_{td}\log\!\left(\frac{N}{\operatorname{df}_t}\right)
$$

Tokenization, smoothing, and normalization are implementation choices that need a record.

Different packages use different conventions. A rare word can be predictive without being substantively important. The vocabulary and IDF values must be learned from the training corpus.

Source: M5, Section 5.2, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 5: Embeddings and Similarity

- Embeddings place text in a numerical representation.
- Nearby descriptions may share meaning or usage.
- A useful similarity measure still requires domain validation.

A semantic model can confuse closely related foods that have distinct nutritional properties. A cosine score is a representation-based similarity, not a probability of label correctness.

Source: M5, Section 5.3, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 6: A Text-to-Rating Measurement Rule

For one response and one anchor set, subtract the least similar category and normalize.

$$
p_r=\frac{s_r-\min_j s_j}{\sum_{k=1}^{5}(s_k-\min_j s_j)}
$$

The similarities $s_r$ depend on the anchors and embedding. Equal similarities leave the denominator at zero.

This is the paper setting with epsilon zero and SSR temperature one. The normalized weights describe a mapping to rating categories. Calibration against human outcomes requires separate evidence. The course code explicitly abstains when the spread is at most 1e-12. That numerical threshold is not evidence of consumer indifference.

Source: (Maier et al., 2025, Table 1, Appendix A.3). https://arxiv.org/abs/2510.08338v3 M4 §4.23, M5 §5.23, and M7 §7.36. ../03_Data_and_Code/Synthetic_Consumers/README.md

## Slide 7: The Same Response Under Different Anchors

Fixed authored response and imposed similarities. The mean rating changes from 4.25 to 3.70.

**Figure description:** Paired bars show category weights 0, 5, 15, 30, and 50 percent for Set 1 and 0, 10, 30, 40, and 20 percent for Set 2. The probability assigned to categories 4 and 5 falls from 80 to 60 percent.

[Editable TikZ](../06_Lecture_Notes/figures/M05_anchor_ratings.tex)

The response is: I would consider it if the refill is convenient and the total price is acceptable. The two sets express increasing purchase intent with different wording. The similarities are deliberately imposed, so their difference does not estimate the effect of these words on an embedding model. Across the supplied three concepts and two personas, Set 1 favors refillable body wash while Set 2 favors fragrance-free. Averaging sets does not establish validity against consumers.

Source: M4 §4.23, M5 §5.23, and M7 §7.36. ../03_Data_and_Code/Synthetic_Consumers/README.md

## Slide 8: A Hand-Checkable Rating

Run from the Synthetic_Consumers example folder with the complete local program.

```python
from anchor_measurement import rating_distribution

scores = [0.20, 0.23, 0.29, 0.38, 0.50]
weights = rating_distribution(scores)
value = sum((r + 1) * p for r, p in enumerate(weights))
assert abs(value - 4.25) < 1e-12
```

Imposed inputs. The full program preserves persona weights and incomplete mappings.

Subtracting 0.20 yields 0, 0.03, 0.09, 0.18, and 0.30, whose sum is 0.60. The category weights are 0, 0.05, 0.15, 0.30, and 0.50. Average repeats within persona before averaging personas. For the refill example, equal-persona weighting gives 3.975 while counting an identical repeated response as another person gives 4.067. No model account is needed for this calculation.

Source: M4 §4.23, M5 §5.23, and M7 §7.36. ../03_Data_and_Code/Synthetic_Consumers/README.md

## Slide 9: Labels, Sentiment, and Topics

- Sentiment measures an evaluative construct.
- Aspect labels distinguish the object of a complaint.
- Topics summarize recurring term patterns under a model.

A high-weight topic term does not establish a causal driver of satisfaction. Topic names are interpretations that should be checked against representative documents.

Source: M5, Section 5.4, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 10: Rare Complaints Lower Precision

Synthetic classifier. Sensitivity is 80% and specificity is 90%.

**Figure description:** At 1% prevalence, only about 7.5% of flagged reviews are true complaints. At 20% prevalence, precision rises to 66.7%.

[Editable TikZ](../06_Lecture_Notes/figures/M05_prevalence.tex)

The classifier has unchanged conditional error rates. The changing base rate alters the composition of the flagged group and therefore the workload of human reviewers.

Source: M5, Section 5.5, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 11: Precision Depends on Prevalence

Let $\pi$ be complaint prevalence, $s$ sensitivity, and $c$ specificity.

$$
\Pr(Y=1\mid\widehat Y=1)=\frac{s\pi}{s\pi+(1-c)(1-\pi)}
$$

False positives can dominate a queue when the target condition is rare.

The formula applies to the specified population and classifier. Use prevalence from the intended deployment population; an artificially balanced training set changes that share.

Source: M5, Section 5.5, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 12: Expected Queue Composition

In 10,000 synthetic reviews, complaint prevalence is 1%.

```python
n, prevalence = 10000, 0.01
sensitivity, specificity = 0.8, 0.9
tp = n * prevalence * sensitivity
fp = n * (1-prevalence) * (1-specificity)
precision = tp / (tp + fp)
assert round(precision, 4) == 0.0748
```

The expected queue contains 80 true complaints and 990 false positives.

These are expected counts under the imposed rates. Actual counts vary. Capacity planning should consider the queue size as well as sensitivity.

Source: M5, Section 5.5, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 13: Human and LLM Annotation

- Write a label definition with difficult boundary examples.
- Measure agreement and adjudicate disagreements.
- Assess a held-out sample with human labels.
- Record the model, prompt, and response format.

Agreement measures consistency, not necessarily construct validity. When a model labels the data used to evaluate itself, the resulting score can reproduce its own labeling choices. A sponsor-framing comparison can hold the same proposal fixed while varying whether the sponsor likes it. Evaluate factual criticism separately from approval. This is a proposed exercise motivated by Sharma et al.; no course model responses have been collected.

Source: M5, Section 5.6, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md (Sharma et al., 2024), https://arxiv.org/abs/2310.13548v4. M5 §5.18.

## Slide 14: Agency Labels Need Supporting Evidence

- Extract the outcome, mechanism, study design, and supporting passage.
- Separate reported choice concerns from inferred possible misuse.
- Retain uncertain cases and compare independent coding.

Consumer agency concerns understanding, choice, action, and revision or exit. Persuasion alone does not establish impairment. The current literature codes are preliminary AI-assisted annotations without independent human adjudication. Immersive Service supplies qualitative agency evidence; Nudging App Adoption supplies evidence about choice presentation whose misuse requires an additional inference. See M5 Section 5.16.

Source: ../03_Data_and_Code/Consumer_Agency_Literature/README.md

## Slide 15: mHealth Food Descriptions

- Descriptions can recur across many users and dates.
- A repeated-description split evaluates familiar language.
- A held-out-description split tests generalization to new language.

The source category is an imperfect label. The same normalized description can have multiple source labels. Retaining that ambiguity lets the evaluation distinguish inconsistent labeling from classifier mistakes.

Source: M5, Section 5.10, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 16: Familiar and New Text Are Different Tests

mHealth text classification uses the stated training and evaluation splits.

**Figure description:** The comparison separates repeated descriptions from new descriptions and identifies source-label ambiguity. Performance depends on the deployment question.

[Editable TikZ](../06_Lecture_Notes/figures/M05_mhealth_text.tex)

A random event split can place an identical description in both training and test. That may be useful for repeated lookup but overstate performance on new descriptions.

Source: M5, Section 5.10, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 17: A New Encoder Changes the Coordinates

- Compare word and character features on unseen descriptions.
- Fit vocabulary, weights, directions, and alignment using training data.
- Choose dimensions on validation; retain every test category.
- Recorded categories define the target, including ambiguous labels.

The mHealth comparison gives equal weight to 6,000 training descriptions, 1,500 validation descriptions, and 1,500 test descriptions. Normalized descriptions are disjoint across splits, although users and periods are shared, so the test concerns new descriptions within that setting. Seventy-four test descriptions have multiple recorded categories; the modal category with alphabetical tie breaking defines the reference. Retaining categories such as default and recipe makes agreement with the recorded system the measured outcome. Nutritional correctness requires a separately justified reference.

Source: M5 §5.26. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 18: Topic Shares Need a Denominator

mHealth topic summaries compare documents, entries, and users under defined weights.

**Figure description:** A topic common in repeated entries can look less prevalent when distinct descriptions or equally weighted users form the denominator.

[Editable TikZ](../06_Lecture_Notes/figures/M05_topic_denominators.tex)

Long documents and repeated records can dominate term-weighted summaries. A business question about the fraction of affected customers needs a customer denominator.

Source: M5, Section 5.12, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 19: Which Pricing Statements Deserve Review?

- A retailer reviews competitors' public pricing communication.
- A keyword occurrence supplies a reading lead.
- Define the priced object, timing, and evidence before interpreting adoption.

The supplied corpus includes core terms for pricing methods and shelf-label infrastructure. Among observed calls, core-call rates are 2.90% in retail, 2.02% in restaurants, and 10.49% in the selected comparison group. These are call-weighted disclosure rates.

Source: M5, Section 5.14, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 20: Speaking Time Changes the Comparison

Observed calls; heuristic roles. Management includes prepared remarks and Q&A.

**Figure description:** Management has 127 core occurrences in 16,685,338 words, versus analysts' 23 in 2,761,999 words. Rates are 0.076 and 0.083 per 10,000 words.

[Editable TikZ](../06_Lecture_Notes/figures/M05_calls_exposure.tex)

Raw counts rank management higher, whereas exposure-adjusted intensity is slightly higher for analysts. This is a descriptive arithmetic comparison, with different formats and heuristic labels. Restricting both counts and words to detected-Q&A calls gives rates of 0.072 and 0.083.

Source: M5, Section 5.14, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 21: Same Vocabulary, Different Evidence

- Amazon: current price information; Eventbrite: advertising cost per click.
- Wendy's: planned tests; Kroger: shelf-label infrastructure.
- A claim about use still requires evidence on implementation and outcomes.

Seven purposeful, source-linked paraphrases are provided in interpretation_cases.csv. They are examples of construct distinctions, not a representative precision sample. Delta's January 2025 question recorded as management/prepared also motivates reviewing heuristic speaker boundaries.

Source: M5, Section 5.14, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 22: Match Counts and Words to the Same Calls

From the Earnings_Calls folder, compare the verified metadata.

```python
from assessment import load_checked
from disclosure import role_rates
calls, mentions, _, _ = load_checked()
rates = role_rates(calls, mentions, require_qa=True)
assert rates.calls.eq(2240).all()
print(rates[['role', 'core_matches', 'per_10000_words']])
```

Excluding a call removes both its occurrences and its words.

Run disclosure.py for group, quarterly, and role tables. The counterexample test includes one excluded call with many words; dropping only its matches would change the rate incorrectly.

Source: M5, Section 5.14, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 23: Evaluate Retrieval and Interpretation Separately

- A denial and a future intention can match the same phrase.
- Relevant paraphrases can escape the dictionary.
- Validate held-out firms or later calls with independently labeled hits and misses.

Run construct_checks.py for eight synthetic sentences. A purposeful case set cannot estimate corpus precision or recall. Probability sampling and appropriate weights are needed for population metrics. No external model or labeling API was run for the supplied course example.

Source: M5, Section 5.14, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 24: What Does a Utility Disclosure Establish?

- Identify the speaker, customer class, charge component, and horizon.
- Separate a forecast, request, approval, and household outcome.
- Compare recovery claims with offsetting revenues and protections.

The source set has six purposeful documents, including three calls, and ten claim records. Public coding uses original paraphrases and locators; the notes retain three short verbatim excerpts. Five documents were downloaded. The accounting passage was checked separately through a web reader. Counts describe this selection and provide no prevalence estimate. Hsieh and Shannon (2005), https://doi.org/10.1177/1049732305276687; O'Brien et al. (2014), https://doi.org/10.1097/ACM.0000000000000388; Gale et al. (2013), https://doi.org/10.1186/1471-2288-13-117; O'Connor and Joffe (2020), https://doi.org/10.1177/1609406919899220; Braun and Clarke (2021), https://doi.org/10.1080/14780887.2020.1769238.

Source: M5 §5.27. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 25: Follow the Cost into the Bill

Each transition requires evidence appropriate to its institutional stage.

**Figure description:** Investment plans lead to recovery requests, then authorized charges and household bills. New-load revenue and protections can reduce the requested amount. Dashed arrows identify transitions requiring additional records.

[Editable TikZ](../06_Lecture_Notes/figures/M05_utility_evidence_chain.tex)

A smaller requested increase can coexist with a higher bill than today. Electricity supply procurement differs from construction recovery. Check the legal entity and customer class before connecting passages across documents. A statement at one stage does not establish all subsequent outcomes.

Source: M5 §5.27. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 26: Keep the Case That Challenges Your Interpretation

- Evergy discusses investment-related rate pressure and benefits from growing sales.
- Its later request proposes a higher residential bill while claiming a revenue offset.
- A lower bill than otherwise can still be a higher bill than today.

The later announcement proposes a USD 17.25 monthly increase at 1005 kWh, conditional on approval, and a USD 61 million reduction in the annual revenue request from anticipated data-center revenue. The comparison does not identify a data-center-specific causal effect. Read both sides of the account before developing an explanatory theme.

Source: M5 §5.27. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md Evergy, November 3, 2026, https://newsroom.evergy.com/2026-11-03-Evergy-files-Missouri-West-rate-request-focused-on-reliability-and-new-generation-investments

## Slide 27: Qualitative Quality Depends on the Analytical Approach

- State selection rules, prior expectations, and changes to the codebook.
- Compare within cases; retain source locators and negative cases.
- Use independent review for the shared coding frame and explain disagreements.

This is directed content analysis with a codebook. Independent human coding has not yet been completed. Agreement would concern coding consistency, not the truth of a corporate statement. Reflexive thematic analysis makes different methodological commitments. Retain investigator interpretation and the limits of investor-facing documents. Hsieh and Shannon (2005), https://doi.org/10.1177/1049732305276687; O'Brien et al. (2014), https://doi.org/10.1097/ACM.0000000000000388; Gale et al. (2013), https://doi.org/10.1186/1471-2288-13-117; O'Connor and Joffe (2020), https://doi.org/10.1177/1609406919899220; Braun and Clarke (2021), https://doi.org/10.1080/14780887.2020.1769238.

Source: M5 §5.27. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md (Hsieh and Shannon, 2005), https://doi.org/10.1177/1049732305276687; (O'Brien et al., 2014), https://doi.org/10.1097/ACM.0000000000000388; (Gale et al., 2013), https://doi.org/10.1186/1471-2288-13-117; (O'Connor and Joffe, 2020), https://doi.org/10.1177/1609406919899220; (Braun and Clarke, 2021), https://doi.org/10.1080/14780887.2020.1769238.

## Slide 28: Prompt Revision Uses Evaluation Evidence

- A passage used to revise a prompt becomes development material.
- Keep passages from one call together when constructing a split.
- Freeze the prompt and reference-label procedure before fresh evaluation.

A test on new firms addresses a different deployment population from a test on later calls from familiar firms. Repeated passages are not independent firm-level replications. Evaluate a competent dictionary baseline with the same eligible evidence. Once final labels guide a revision, a later confirmation needs new evidence or a justified adaptive-evaluation design.

Source: Marketing Analytics Lecture Notes, M5 §5.15.

## Slide 29: Citations and Supporting Evidence

Four fictional pricing questions; authored answers and reference annotations.

**Figure description:** All four answers cite a source in every condition. Supported counts are four with curated sources, two after a misleading memo is added, and four after review. The contrast is stipulated.

[Editable TikZ](../06_Lecture_Notes/figures/M05_source_selection.tex)

The synthetic records support different kinds of statements: S1 reports a price increase and a before-after unit change without a causal design, S2 contains an unanswered question about discounts, and S3 defines a selected panel-member denominator. S4 incorrectly converts these records into claims of causality and a discount announcement. The comparison shows why citations must support the particular inference being made. Because no model responses were collected, the counts describe these constructed claims and establish no effect of context on model performance.

Source: M5 §5.19. ../03_Data_and_Code/AI_Evidence_and_Evaluation/README.md

## Slide 30: A Controlled Source Comparison

- Hold the questions, model version, and scoring rule fixed.
- Use fresh conversations and preserve raw responses.
- Repeat paired runs; randomize condition order.
- Assess support independently and retain missing answers.

Run source_selection.py to reproduce the constructed example. In an optional live extension, supply the excerpts and questions without the saved answers or support labels. A single pair gives a descriptive comparison. Repetition helps separate sampling variation from a stable context effect. Credible contradictory evidence requires review; disagreement alone is not a reason to exclude a source. The class activity fits the existing earnings-call Python block.

Source: M5 §5.19; ../07_Labs/AI_Evidence_and_Evaluation/README.md; https://web.stanford.edu/class/archive/cs/cs193t/cs193t.1272/assignments/3-managing-sources/

## Slide 31: Generator and Judge Changes

Identical saved outputs are scored by both judges. All scores are stipulated.

**Figure description:** Old-judge scores are 60 and 62; new-judge scores are 75 and 77. The generator gain is two points within either judge, while the diagonal comparison is seventeen.

[Editable TikZ](../06_Lecture_Notes/figures/M05_judge_change.tex)

A stable judge supplies a common comparison but still requires validation. Position, verbosity, and self-preference can affect evaluation. For earnings-call summaries, independently check factual support, speaker role, and whether a statement concerns a plan or an implemented action. Preserve inconsistent judgments.

Source: M5 §5.18. (Zheng et al., 2023), https://arxiv.org/abs/2306.05685; (Panickssery et al., 2024), https://arxiv.org/abs/2404.13076

## Slide 32: Network Objects

- Nodes identify customers or accounts.
- Edges represent a defined relationship in a time window.
- Degree counts links, while brokerage concerns paths between groups.

An edge could mean following, messaging, purchasing together, or co-occurrence. Those meanings are not interchangeable. The network boundary determines which relationships are visible.

Source: M5, Section 5.7, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 33: Few Links Can Connect Separate Groups

Synthetic undirected network. R has only two links.

**Figure description:** R connects two otherwise separate four-person groups. Its low degree coexists with a central position on paths between the groups.

[Editable TikZ](../06_Lecture_Notes/figures/M05_network_bridge.tex)

Brokerage can matter for reach even when a node has few direct neighbors. Observed network structure does not by itself establish the effect of targeting that person.

Source: M5, Section 5.7, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 34: The Nearest Store Depends on the Route

Synthetic population: 800. Access threshold: five minutes. Schematic spacing is not a distance scale.

**Figure description:** A northern bridge joins the two riverbanks. The straight-line proxy from W0 to B is two minutes; the graph route is eighteen. The nearest known available store from W0 is C at eight minutes. Isolated X contains 150 people and an unknown-status store.

[Editable TikZ](../06_Lecture_Notes/figures/M05_access_network.tex)

W0, W1, W2, E0, E1, E2, and X receive weights 100, 300, 100, 50, 50, 50, and 150. Store B at E0 and C at W2 are available; A and D are unavailable. U at X is unknown. All weights, graph times, the proxy, and the threshold are imposed. Straight-line access includes 650 people; known network access includes 550.

Source: Marketing Analytics Lecture Notes. M5 §§5.21–5.22. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 35: Hold the Comparison Fixed

- Same six connected origins; one directed neighbor each.
- Each metric creates six links; only two links coincide.
- Network time along selected links averages 10 versus 3.33 minutes.
- Population access retains all 800 people: 68.75% to 87.50%.

The neighbor comparison fixes k=1 and resolves ties alphabetically. The ten-minute average uses straight-line-selected links; 3.33 uses network-selected links. X is excluded only from this neighbor comparison, while remaining in the population-access denominator. Unknown U yields lower and upper counts of 550 and 700. These are missing-status bounds conditional on the fixed graph, not confidence intervals. A proximity link does not establish customer influence or substitution.

Source: Marketing Analytics Lecture Notes. M5 §§5.21–5.22. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 36: The Route Changes the Nearest Alternative

Four observed restaurant origins; other available same-chain targets. October status, November network.

**Figure description:** Paired points give nearest straight-line and modeled-network distances for each selected restaurant. For North Neil, the selected destination changes from Mattis at 3.478 kilometers straight-line to South Neil at 4.757 kilometers on the network.

[Editable TikZ](../06_Lecture_Notes/figures/M05_restaurant_distances.tex)

The four records are observed on October 24, 2026; OpenStreetMap is dated November 18. Each origin is excluded from its own target set, including when available. Distances include straight connectors to the closest retained nodes. The network is undirected and uses stated access filters. North Neil is the only recorded unavailable origin. These are selected restaurant-origin comparisons, with no population weights. © OpenStreetMap contributors, ODbL 1.0.

Source: Marketing Analytics Lecture Notes. M5 §§5.21–5.22. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md https://www.openstreetmap.org/copyright

## Slide 37: Interpret the Observed Comparison

- Hold the same observed origin and target set fixed across metrics.
- At four kilometers: three of four origins by straight line; zero by network.
- Check boundaries, access tags, entrance locations, and snapping.
- Customer substitution requires evidence about feasible choices and behavior.

The four-kilometer threshold is imposed. Available means recorded ordering availability, not a verified mechanical condition. The later street extract does not reconstruct the historical network. Directional pedestrian restrictions, crossing barriers, actual entrances, and straight connector feasibility are unverified. Different chains and restaurants outside the selection box are absent. A local count of restaurant origins cannot establish the access experienced by city residents.

Source: Marketing Analytics Lecture Notes. M5 §§5.21–5.22. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 38: A Group Mean Needs a Group Size

Four synthetic zones earn 10, 10, 10, and 40 dollars per week.

$$
\overline{x}=\frac{3(10)+1(40)}{4}=17.50\qquad \mathrm{Total}=70
$$

Groups {A, B, C} and {D} have mean revenues 10 and 40. Equal group weights give 25 dollars per zone.

The observation unit is a zone, and each zone has 100 people. Binary membership and the combinatorial convention produce group means. Counts three and one restore the original mean and total. These are weekly zone totals, not individual spending. GraCo defaults to normalized_self_loop, whose degree-normalized lifting generally differs from this averaging rule.

Source: Marketing Analytics Lecture Notes, M5 §5.24. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md https://arxiv.org/abs/2611.01200v1

## Slide 39: Exact Revenue, Distorted Access

Synthetic inputs. Five-minute access is evaluated at the four original origins.

**Figure description:** The path A-B-C-D has edge travel times 4, 1, and 4 minutes, with the available store at D. Grouping A, B, and C preserves revenues and their energy but omits internal travel. The original routes to D take 9, 5, 4, and 0 minutes; naive reciprocal coarse-edge routes take 4, 4, 4, and 0. Access changes from 300 of 400 people to an apparent 400 of 400.

[Editable TikZ](../06_Lecture_Notes/figures/M05_graph_coarsening.tex)

Affinity is defined as one divided by travel minutes; coarse adjacency sums affinities between groups. Internal edges are removed. Revenue reconstruction error is zero and both combinatorial energies equal 225 dollars squared per minute. This preserves the chosen block-constant feature and quadratic form. It does not preserve every graph property or shortest paths. The incorrect coarse travel interpretation is an original constructed example, with no GraCo execution.

Source: Marketing Analytics Lecture Notes, M5 §5.24. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 40: Preprocessing Changes the Population

- The existing retail case includes 150 people at a disconnected origin.
- Known access stays at 550 people when that origin is removed.
- Changing the denominator from 800 to 650 raises access from 68.75% to 84.62%.
- Retain original weights, excluded origins, and the meaning of each edge.

This is the separate seven-origin case in Section 5.21, not the four-zone compression example. GraCo preprocessing defaults to largest-component selection, symmetrization, and removing self-loops. Weighted reciprocal edges are averaged. A referral or one-way trip can change meaning under symmetrization. Check algorithm support before changing these options; preserve excluded people in the original-population accounting. No access improved in this calculation.

Source: Marketing Analytics Lecture Notes, M5 §5.24. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md ../01_Resources/32_Graph_Coarsening/SOURCE_REVIEW.md

## Slide 41: University Affiliations Create a Research Network

- 745 papers identify 424 higher-education institutions.
- Split one unit of link weight across each paper's university pairs.
- Shared-paper links can also arise from a single author's dual affiliation.

The eligible census has 824 papers; 79 lack identified education affiliations. Work-specific metadata is used rather than current author profiles. One missing University of Vaasa affiliation was verified from a published article and corrected. Louvain clustering at resolution one and seed 534 finds 19 communities among 415 linked institutions; nine remain unconnected. See M5 Section 5.17.

Source: ../03_Data_and_Code/Consumer_Agency_Literature/AFFILIATIONS.md

## Slide 42: Affiliation Groups Depend on the Representation

Fractional papers in the six largest of 19 communities. All 745 papers contribute one in total.

**Figure description:** Bars show C01 154.15, C02 84.54, C03 74.65, C04 67.16, C05 57.80, and C06 48.52 fractional papers. Group membership is based on shared university affiliations, independently of agency coding.

[Editable TikZ](../06_Lecture_Notes/figures/M05_affiliation_communities.tex)

The median adjusted Rand agreement across twenty seeds is 0.522; switching from fractional to full edge counting gives 0.193. These are exploratory communities. The selected mechanism overlay has uneven review coverage and cannot establish institutional intent or rank universities by harm. The full program and all memberships appear in M5 Section 5.17 and the affiliation outputs.

Source: ../03_Data_and_Code/Consumer_Agency_Literature/AFFILIATIONS.md

## Slide 43: Coding Exercise: A Label Assessment

- Reproduce the four-question source comparison.
- Trace each unsupported claim to its inferential error.
- Explain why citation counts remain unchanged.
- Check one result without the coding assistant.

Use ten minutes to introduce the question and demonstrate the output, twenty-five minutes for the source comparison, and ten minutes for independent explanation within the existing forty-five-minute Python block. The supplied answers are synthetic. Earnings-call retrieval checks and mHealth text comparisons remain available as extensions. No grading requirements are established.

Source: M5 §§5.19–5.20. ../07_Labs/AI_Evidence_and_Evaluation/README.md

## Slide 44: Engagement and Commercial Value

- Likes and comments measure platform responses.
- Sales and contribution require separate outcome records.
- Network similarity can reflect common interests or common exposure.

Homophily and shared shocks can generate correlated behavior among connected users. A causal influence claim requires an assignment or identification design beyond a network correlation.

Source: M5, Section 5.8, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 45: Continued Use Leaves the Purpose Open

- A sequence can change the preference the system predicts.
- A displayed streak can become a goal in itself.
- Identify purpose, control, and consequences before claiming benefit.

Content-sequence and logged-streak experiments concern specified behavioral outcomes (Woolley and Sharif, 2022; Silverman and Barasch, 2023). Continued activity can reflect enjoyment, a chosen commitment, an induced goal, or difficulty stopping. A retention measure does not distinguish these explanations. M5 §5.29 and M9 §§9.70–9.71.

Source: ../01_Resources/49_Online_Engagement_and_Agency/README.md

## Slide 46: Classify the Claim Before Coding the Text

- Separate a mechanism, deployed feature, citation, and harmful outcome.
- Retain source role, chronology, and the population represented.
- Code endorsed long use alongside unwanted continuation.

The company method report explicitly cites streak research (Freeman et al., 2023); its earlier experiment predates the paper (Duolingo, 2020). A citation documents a connection without establishing that the paper originated a feature. Qualitative coding should distinguish a stated purpose, exposure, reported consequence, and stopping attempt. Public complaints are selected accounts, and copied statements are not independent cases. M5 §5.29.

Source: ../01_Resources/49_Online_Engagement_and_Agency/README.md

## Slide 47: Authenticity of Reviews and Endorsements

- A generated product description and a claimed customer review serve different roles.
- A fabricated experience misrepresents the source of the evidence.
- Keep sponsored relationships and substantive editing traceable.

The FTC review rule addresses business conduct involving fake or false reviews. Its FAQ distinguishes mere review hosting from creation, purchase, and dissemination of testimonials, with provision-specific conditions.

Source: FTC Consumer Reviews and Testimonials Rule Q&A. https://www.ftc.gov/business-guidance/resources/consumer-reviews-testimonials-rule-questions-answers

## Slide 48: Mechanism Evidence Can Justify an Inquiry

- Preserve source role, timing, exact wording, and contrary passages.
- Use cost-recovery statements to identify the records an inquiry needs.
- Distinguish a credible mechanism from an estimated historical bill effect.

Most selected utility-call material concerns 2026, after the study’s 2020–2025 period. The study also discusses cost recovery and reports some positive residential spillovers. These facts constrain a claim of contradiction. Contextual coding can support inquiry into commitments, canceled projects, tariff cases, and customer classes without establishing the magnitude of pass-through. The evidence for requesting records differs from the evidence for assigning liability. M5 §§5.27–5.28.

Source: ../01_Resources/47_Evidence_Standards_and_Error_Costs/README.md

## Slide 49: Text-Analysis Discussion

- Which label disagreement would change the service decision?
- How does the expected queue change when prevalence falls?
- What comparison would distinguish exposure from influence?

A practical assessment prioritizes errors that alter the action. False positives determine review burden, while false negatives determine missed cases. Both should be evaluated in the deployment population.

Source: M5, Section 5.9, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md
