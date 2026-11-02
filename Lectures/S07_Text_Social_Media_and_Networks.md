# Text, Social Media, and Networks

By Nathan Yang

Session 07. M5. 170 minutes.

[PDF](S07_Text_Social_Media_and_Networks.pdf) | [LaTeX](S07_Text_Social_Media_and_Networks.tex) | [Session Plan](SESSION_PLAN.md)

## Learning Objectives

- Define a text construct and evaluate labels on the deployment population.
- Distinguish prevalence, classifier performance, and topic denominators.
- Explain network reach and brokerage without inferring influence from correlation.

## Related Materials

- [M5 lecture notes](../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md)
- [Runnable small examples](../03_Data_and_Code/Lecture_Examples/session_examples.py)
- [mHealth text code](../03_Data_and_Code/mHealth/recurring_examples/m05.py)
- [Ethics and regulation](../06_Lecture_Notes/ETHICS_AND_REGULATION.md)

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
- Audit a held-out sample with human labels.
- Record the model, prompt, and response format.

Agreement measures consistency, not necessarily construct validity. When a model labels the data used to evaluate itself, the resulting score can reproduce its own labeling choices.

Source: M5, Section 5.6, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 11: mHealth Food Descriptions

- Descriptions can recur across many users and dates.
- A repeated-description split evaluates familiar language.
- A held-out-description split tests generalization to new language.

The source category is an imperfect label. The same normalized description can have multiple source labels. Evaluation should retain that ambiguity rather than assume a single validated nutrition category.

Source: M5, Section 5.10, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 12: Familiar and New Text Are Different Tests

mHealth text classification uses the stated training and evaluation splits.

**Figure description:** The comparison separates repeated descriptions from new descriptions and identifies source-label ambiguity. Performance depends on the deployment question.

[Editable TikZ](../06_Lecture_Notes/figures/M05_mhealth_text.tex)

A random event split can place an identical description in both training and test. That may be useful for repeated lookup but overstate performance on new descriptions.

Source: M5, Section 5.10, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 13: Topic Shares Need a Denominator

mHealth topic summaries compare documents, entries, and users under defined weights.

**Figure description:** A topic common in repeated entries can look less prevalent when distinct descriptions or equally weighted users form the denominator.

[Editable TikZ](../06_Lecture_Notes/figures/M05_topic_denominators.tex)

Long documents and repeated records can dominate term-weighted summaries. A business question about the fraction of affected customers needs a customer denominator.

Source: M5, Section 5.12, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 14: Network Objects

- Nodes identify customers or accounts.
- Edges represent a defined relationship in a time window.
- Degree counts links, while brokerage concerns paths between groups.

An edge could mean following, messaging, purchasing together, or co-occurrence. Those meanings are not interchangeable. The network boundary determines which relationships are visible.

Source: M5, Section 5.7, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 15: Few Links Can Connect Separate Groups

Synthetic undirected network. R has only two links.

**Figure description:** R connects two otherwise separate four-person groups. Its low degree coexists with a central position on paths between the groups.

[Editable TikZ](../06_Lecture_Notes/figures/M05_network_bridge.tex)

Brokerage can matter for reach even when a node has few direct neighbors. Observed network structure does not by itself establish the effect of targeting that person.

Source: M5, Section 5.7, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 16: Coding Exercise: A Label Audit

- Build a transparent keyword or TF-IDF baseline.
- Compare precision and recall on familiar and new descriptions.
- Inspect false positives and disagreements by label.

Run ../03_Data_and_Code/Lecture_Examples/session_examples.py S07 to reproduce the prevalence calculation. The full mHealth m05.py program implements the description-level comparison. Select the evaluation split before tuning.

Source: M5, Section 5.9, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 17: Engagement and Commercial Value

- Likes and comments measure platform responses.
- Sales and contribution require separate outcome records.
- Network similarity can reflect common interests or common exposure.

Homophily and shared shocks can generate correlated behavior among connected users. A causal influence claim requires an assignment or identification design beyond a network correlation.

Source: M5, Section 5.8, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md

## Slide 18: Authenticity of Reviews and Endorsements

- A generated product description and a claimed customer review serve different roles.
- A fabricated experience misrepresents the source of the evidence.
- Keep sponsored relationships and substantive editing traceable.

The FTC review rule addresses business conduct involving fake or false reviews. Its FAQ distinguishes mere review hosting from creation, purchase, and dissemination of testimonials, with provision-specific conditions.

Source: FTC Consumer Reviews and Testimonials Rule Q&A. https://www.ftc.gov/business-guidance/resources/consumer-reviews-testimonials-rule-questions-answers

## Slide 19: Text-Analysis Discussion

- Which label disagreement would change the service decision?
- How does the expected queue change when prevalence falls?
- What comparison would distinguish exposure from influence?

A practical audit prioritizes errors that alter the action. False positives determine review burden, while false negatives determine missed cases. Both should be evaluated in the deployment population.

Source: M5, Section 5.9, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md
