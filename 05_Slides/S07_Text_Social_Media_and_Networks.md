# Text, Social Media, and Networks

By Nathan Yang

Session 07. M5. 170 minutes.

[PDF](S07_Text_Social_Media_and_Networks.pdf) | [LaTeX](S07_Text_Social_Media_and_Networks.tex) | [Session Plan](SESSION_PLAN.md)

## Learning Objectives

- Define a text construct and evaluate labels on the deployment population.
- Distinguish prevalence, text exposure, retrieval, and substantive interpretation.
- Explain network reach and brokerage without inferring influence from correlation.

## Related Materials

- [M5 lecture notes](../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md)
- [Runnable small examples](../03_Data_and_Code/Lecture_Examples/session_examples.py)
- [mHealth text code](../03_Data_and_Code/mHealth/recurring_examples/m05.py)
- [Ethics and regulation](../06_Lecture_Notes/ETHICS_AND_REGULATION.md)
- [Earnings-call worked example](../03_Data_and_Code/Earnings_Calls/README.md)
- [AI workflow calculations](../03_Data_and_Code/AI_Workflows/README.md)
- [Consumer Agency Literature and Clustering](../03_Data_and_Code/Consumer_Agency_Literature/README.md)
- [University Affiliation Clustering](../03_Data_and_Code/Consumer_Agency_Literature/AFFILIATIONS.md)

## Slide 1: Text, Social Media, and Networks

Marketing Analytics. By Nathan Yang.

## Slide 2: A Customer-Service Decision

- A retailer wants to detect delivery complaints quickly.
- The document may be a review, sentence, or service conversation.
- The action is a review queue with limited staff capacity.

The unit and label definition determine the evaluation. A negative review can concern price or quality rather than delivery. A classifier needs a construct that matches the service action.

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

## Slide 6: Labels, Sentiment, and Topics

- Sentiment measures an evaluative construct.
- Aspect labels distinguish the object of a complaint.
- Topics summarize recurring term patterns under a model.

A high-weight topic term does not establish a causal driver of satisfaction. Topic names are interpretations that should be checked against representative documents.

Source: M5, Section 5.4, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 7: Rare Complaints Lower Precision

Synthetic classifier. Sensitivity is 80% and specificity is 90%.

**Figure description:** At 1% prevalence, only about 7.5% of flagged reviews are true complaints. At 20% prevalence, precision rises to 66.7%.

[Editable TikZ](../06_Lecture_Notes/figures/M05_prevalence.tex)

The classifier has unchanged conditional error rates. The changing base rate alters the composition of the flagged group and therefore the workload of human reviewers.

Source: M5, Section 5.5, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 8: Precision Depends on Prevalence

Let $\pi$ be complaint prevalence, $s$ sensitivity, and $c$ specificity.

$$
\Pr(Y=1\mid\widehat Y=1)=\frac{s\pi}{s\pi+(1-c)(1-\pi)}
$$

False positives can dominate a queue when the target condition is rare.

The formula applies to the specified population and classifier. Prevalence should come from an appropriate deployment sample rather than an artificially balanced training set.

Source: M5, Section 5.5, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 9: Expected Queue Composition

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

## Slide 10: Human and LLM Annotation

- Write a label definition with difficult boundary examples.
- Measure agreement and adjudicate disagreements.
- Assess a held-out sample with human labels.
- Record the model, prompt, and response format.

Agreement measures consistency, not necessarily construct validity. When a model labels the data used to evaluate itself, the resulting score can reproduce its own labeling choices.

Source: M5, Section 5.6, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 11: Agency Labels Need Supporting Evidence

- Extract the outcome, mechanism, study design, and supporting passage.
- Separate reported choice concerns from inferred possible misuse.
- Retain uncertain cases and compare independent coding.

Consumer agency concerns understanding, choice, action, and revision or exit. Persuasion alone does not establish impairment. The current literature codes are preliminary AI-assisted annotations without independent human adjudication. Immersive Service supplies qualitative agency evidence; Nudging App Adoption supplies evidence about choice presentation whose misuse requires an additional inference. See M5 Section 5.16.

Source: ../03_Data_and_Code/Consumer_Agency_Literature/README.md

## Slide 12: mHealth Food Descriptions

- Descriptions can recur across many users and dates.
- A repeated-description split evaluates familiar language.
- A held-out-description split tests generalization to new language.

The source category is an imperfect label. The same normalized description can have multiple source labels. Evaluation should retain that ambiguity rather than assume a single validated nutrition category.

Source: M5, Section 5.10, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 13: Familiar and New Text Are Different Tests

mHealth text classification uses the stated training and evaluation splits.

**Figure description:** The comparison separates repeated descriptions from new descriptions and identifies source-label ambiguity. Performance depends on the deployment question.

[Editable TikZ](../06_Lecture_Notes/figures/M05_mhealth_text.tex)

A random event split can place an identical description in both training and test. That may be useful for repeated lookup but overstate performance on new descriptions.

Source: M5, Section 5.10, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 14: Topic Shares Need a Denominator

mHealth topic summaries compare documents, entries, and users under defined weights.

**Figure description:** A topic common in repeated entries can look less prevalent when distinct descriptions or equally weighted users form the denominator.

[Editable TikZ](../06_Lecture_Notes/figures/M05_topic_denominators.tex)

Long documents and repeated records can dominate term-weighted summaries. A business question about the fraction of affected customers needs a customer denominator.

Source: M5, Section 5.12, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 15: Which Pricing Statements Deserve Review?

- A retailer reviews competitors' public pricing communication.
- A keyword occurrence supplies a reading lead.
- Define the priced object, timing, and evidence before interpreting adoption.

The supplied corpus includes core terms for pricing methods and shelf-label infrastructure. Among observed calls, core-call rates are 2.90% in retail, 2.02% in restaurants, and 10.49% in the selected comparison group. These are call-weighted disclosure rates.

Source: M5, Section 5.14, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 16: Speaking Time Changes the Comparison

Observed calls; heuristic roles. Management includes prepared remarks and Q&A.

**Figure description:** Management has 127 core occurrences in 16,685,338 words, versus analysts' 23 in 2,761,999 words. Rates are 0.076 and 0.083 per 10,000 words.

[Editable TikZ](../06_Lecture_Notes/figures/M05_calls_exposure.tex)

Raw counts rank management higher, whereas exposure-adjusted intensity is slightly higher for analysts. This is a descriptive arithmetic comparison, with different formats and heuristic labels. Restricting both counts and words to detected-Q&A calls gives rates of 0.072 and 0.083.

Source: M5, Section 5.14, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 17: Same Vocabulary, Different Evidence

- Amazon: current price information; Eventbrite: advertising cost per click.
- Wendy's: planned tests; Kroger: shelf-label infrastructure.
- A claim about use still requires evidence on implementation and outcomes.

Seven purposeful, source-linked paraphrases are provided in interpretation_cases.csv. They are examples of construct distinctions, not a representative precision sample. Delta's January 2025 question recorded as management/prepared also motivates reviewing heuristic speaker boundaries.

Source: M5, Section 5.14, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 18: Match Counts and Words to the Same Calls

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

## Slide 19: Evaluate Retrieval and Interpretation Separately

- A denial and a future intention can match the same phrase.
- Relevant paraphrases can escape the dictionary.
- Validate held-out firms or later calls with independently labeled hits and misses.

Run construct_checks.py for eight synthetic sentences. A purposeful case set cannot estimate corpus precision or recall. Probability sampling and appropriate weights are needed for population metrics. No external model or labeling API was run for the supplied course example.

Source: M5, Section 5.14, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 20: Prompt Revision Uses Evaluation Evidence

- A passage used to revise a prompt becomes development material.
- Keep passages from one call together when constructing a split.
- Freeze the prompt and reference-label procedure before fresh evaluation.

A test on new firms addresses a different deployment population from a test on later calls from familiar firms. Repeated passages are not independent firm-level replications. Evaluate a competent dictionary baseline with the same eligible evidence. Once final labels guide a revision, a later confirmation needs new evidence or a justified adaptive-evaluation design.

Source: Marketing Analytics Lecture Notes, M5 §5.15.

## Slide 21: Network Objects

- Nodes identify customers or accounts.
- Edges represent a defined relationship in a time window.
- Degree counts links, while brokerage concerns paths between groups.

An edge could mean following, messaging, purchasing together, or co-occurrence. Those meanings are not interchangeable. The network boundary determines which relationships are visible.

Source: M5, Section 5.7, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 22: Few Links Can Connect Separate Groups

Synthetic undirected network. R has only two links.

**Figure description:** R connects two otherwise separate four-person groups. Its low degree coexists with a central position on paths between the groups.

[Editable TikZ](../06_Lecture_Notes/figures/M05_network_bridge.tex)

Brokerage can matter for reach even when a node has few direct neighbors. Observed network structure does not by itself establish the effect of targeting that person.

Source: M5, Section 5.7, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 23: University Affiliations Create a Research Network

- 745 papers identify 424 higher-education institutions.
- Split one unit of link weight across each paper's university pairs.
- Shared-paper links can also arise from a single author's dual affiliation.

The eligible census has 824 papers; 79 lack identified education affiliations. Work-specific metadata is used rather than current author profiles. One missing University of Vaasa affiliation was verified from a published article and corrected. Louvain clustering at resolution one and seed 534 finds 19 communities among 415 linked institutions; nine remain unconnected. See M5 Section 5.17.

Source: ../03_Data_and_Code/Consumer_Agency_Literature/AFFILIATIONS.md

## Slide 24: Affiliation Groups Depend on the Representation

Fractional papers in the six largest of 19 communities. All 745 papers contribute one in total.

**Figure description:** Bars show C01 154.15, C02 84.54, C03 74.65, C04 67.16, C05 57.80, and C06 48.52 fractional papers. Group membership is based on shared university affiliations, independently of agency coding.

[Editable TikZ](../06_Lecture_Notes/figures/M05_affiliation_communities.tex)

The median adjusted Rand agreement across twenty seeds is 0.522; switching from fractional to full edge counting gives 0.193. These are exploratory communities. The selected mechanism overlay has uneven review coverage and cannot establish institutional intent or rank universities by harm. The full program and all memberships appear in M5 Section 5.17 and the affiliation outputs.

Source: ../03_Data_and_Code/Consumer_Agency_Literature/AFFILIATIONS.md

## Slide 25: Coding Exercise: A Label Assessment

- Run the earnings-call assessment and role-exposure calculation.
- Test denial, future intention, and a missed paraphrase.
- Explain which extra labels would identify precision and recall.

Use ../03_Data_and_Code/Earnings_Calls/README.md and LLM_EXERCISES.md. The mHealth example provides a second application of held-out description evaluation. Synthetic dictionary contrasts are implementation checks; they do not estimate deployment accuracy.

Source: M5, Section 5.9, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 26: Engagement and Commercial Value

- Likes and comments measure platform responses.
- Sales and contribution require separate outcome records.
- Network similarity can reflect common interests or common exposure.

Homophily and shared shocks can generate correlated behavior among connected users. A causal influence claim requires an assignment or identification design beyond a network correlation.

Source: M5, Section 5.8, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 27: Authenticity of Reviews and Endorsements

- A generated product description and a claimed customer review serve different roles.
- A fabricated experience misrepresents the source of the evidence.
- Keep sponsored relationships and substantive editing traceable.

The FTC review rule addresses business conduct involving fake or false reviews. Its FAQ distinguishes mere review hosting from creation, purchase, and dissemination of testimonials, with provision-specific conditions.

Source: FTC Consumer Reviews and Testimonials Rule Q&A. https://www.ftc.gov/business-guidance/resources/consumer-reviews-testimonials-rule-questions-answers

## Slide 28: Text-Analysis Discussion

- Which label disagreement would change the service decision?
- How does the expected queue change when prevalence falls?
- What comparison would distinguish exposure from influence?

A practical assessment prioritizes errors that alter the action. False positives determine review burden, while false negatives determine missed cases. Both should be evaluated in the deployment population.

Source: M5, Section 5.9, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md
