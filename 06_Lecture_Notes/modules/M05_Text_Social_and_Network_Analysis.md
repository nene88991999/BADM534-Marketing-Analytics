# M5. Text, Social Media, and Customer Networks

A retailer receives thousands of reviews and support messages each week. The service manager needs to distinguish delivery delays, product defects, and billing problems, then decide which issues deserve attention. A count of negative words is an incomplete representation: “the refund was fast, but the replacement failed” contains different evaluations of two aspects of the experience. The analytical task is to turn language into a defensible measurement of a concept relevant to action.

Text analysis also raises a sampling problem. Customers who post reviews can differ from those who remain silent, and the platform can affect what gets posted or displayed. Social-network analysis adds another layer: observed connections and similar behavior can reflect influence, common circumstances, or selection into relationships.

## 5.1 Define the Construct and the Document

A construct is the concept the analysis intends to measure, such as delivery dissatisfaction, perceived authenticity, or purchase intent. A label is the operational category assigned to an observation. A document might be a complete review, one sentence, a support ticket, or a conversation. Those units should follow the construct. A review-level sentiment label can obscure a positive service experience and a negative product experience in the same review.

Write an annotation codebook before producing labels at scale. It should define each category, inclusion and exclusion rules, treatment of ambiguity, and examples near category boundaries. If a message can contain several problems, a multi-label task may be appropriate. If the decision requires routing each ticket to one team, define a primary issue or a routing priority separately from the presence of every issue.

Metadata can be informative and potentially misleading. Ratings may help validate a sentiment measure but can also leak the intended label into a prediction exercise. Product category, language, channel, and date can reveal domain differences. Remove or protect personal information before sending text to an external service, and use approved data access. A scraped review is not automatically free of personal or contractual restrictions.

## 5.2 Representing Language with Counts and Weights

A bag-of-words representation counts tokens while largely ignoring their order. An $n$-gram representation retains local sequences, so “not good” can differ from “good.” Tokenization, case normalization, punctuation, and stop-word rules change the resulting features. Removing negation words can destroy information needed for sentiment. Removing product names may help focus on attributes or may erase the very object whose complaints the manager needs to identify.

Term frequency-inverse document frequency gives greater weight to terms that are frequent in a document but less common across the corpus. One simple convention is

$$
\operatorname{tfidf}_{wd}=\operatorname{tf}_{wd}\log\left(\frac{N}{\operatorname{df}_w}\right),
$$

where $\operatorname{tf}_{wd}$ is the frequency of word $w$ in document $d$, $N$ is the number of documents, and $\operatorname{df}_w$ is the number of documents containing the word. Implementations vary in smoothing, normalization, and term-frequency definitions. Record the convention and check how it changes the weights relative to this expression.

If “delivery” appears in two of three documents, its inverse-document-frequency term under this convention is $\log(3/2)\approx0.405$. A word appearing in every document receives zero weight. That weighting can help discriminate documents, but a common term may still be substantively important. Statistical distinctiveness and managerial importance are different criteria.

Fit a learned vocabulary and IDF weights on training text when evaluating prediction. Learning them from the test corpus exposes information about the evaluation distribution. The leakage may appear minor compared with using labels, yet it still changes the task. A pipeline makes the training-only transformation explicit and reproducible.

## 5.3 Embeddings and Semantic Similarity

An embedding maps a document or token into a vector learned from language data. Similar vectors can capture related meanings even when documents use different words. Cosine similarity compares the angle between vectors:

$$
\operatorname{cos}(u,v)=\frac{u^\top v}{\|u\|\,\|v\|}.
$$

The normalization removes vector length from the comparison. This is useful when direction represents meaning in the selected model, but it does not guarantee that the similarity corresponds to the marketing construct. Two messages about refunds can be semantically close while expressing opposite evaluations. Retrieval quality should be checked with examples that matter for the downstream task.

A simple TF-IDF classifier can be a strong baseline for a well-defined domain. Embeddings may help with paraphrases, sparse labels, and semantic retrieval, but they introduce dependence on a pretrained model and its training domain. Compare alternatives on the same held-out data and operational criteria. Record model versions because an updated representation can change nearest neighbors and labels even when the input text is unchanged.

For interpretation, inspect representative successes and failures. A model may associate a brand name with complaints because one product had a recall during training. It can then misclassify neutral mentions after the issue is resolved. Temporal validation and product-level holdouts help reveal whether performance depends on such shortcuts.

Large collections of embeddings can make repeated nearest-center assignments costly. The comparison in Sections 4.18–4.20 holds the vectors and feature transformation fixed while varying the clustering implementation. Changing the embedding model or normalization changes the representation itself and requires a separate interpretation check. Representative documents and independent labels help establish what a text cluster means. A smaller squared-distance objective alone does not establish a coherent marketing construct.

## 5.4 Sentiment, Aspect Labels, and Topic Models

A sentiment lexicon assigns scores to words and combines them using rules. It offers a transparent baseline, but sarcasm, domain-specific meanings, and context can cause errors. A supervised classifier learns a mapping from labeled examples to outcomes. Its labels and training sample define what it learns; a generic “positive/negative” dataset may not represent customer-service severity.

Aspect-based analysis separates the object being evaluated from the evaluation itself. For the sentence “delivery was late, but the support agent solved the problem,” a useful record might contain delivery-negative and service-positive labels. A single overall score discards that distinction. If the action is a logistics intervention, the aspect-specific measure is closer to the decision.

Topic models describe recurring patterns of word co-occurrence or document similarity. A topic is an estimated pattern, not automatically a stable consumer need. In probabilistic models, documents can combine topics; in clustering approaches, assignments may be discrete or probabilistic. Analysts supply topic names after inspecting high-weight words and representative documents. Validate those names with actual text and examine stability across preprocessing and model choices.

A manager should avoid interpreting an increase in a topic's share without checking its denominator. More delivery complaints can mean more delivery problems, more deliveries overall, a changed review prompt, or fewer reviews about other topics. Combining text measures with transaction or service-volume data helps distinguish these explanations.

## 5.5 Case Study: A Complaint Detector Under Changing Prevalence

Suppose a classifier identifies a rare but costly product defect. In a synthetic evaluation population of 1,000 tickets, 200 truly mention the defect. The classifier detects 160 of them and incorrectly flags 80 of the 800 other tickets. Sensitivity, or recall, is 80%; specificity is 90%; precision is 160/240, or 66.7%.

| Population | True Defect Tickets | True Positives | False Positives | Precision |
| --- | ---: | ---: | ---: | ---: |
| Evaluation sample | 200 | 160 | 80 | 66.7% |
| Deployment sample | 10 | 8 | 99 | 7.5% |

The second row holds sensitivity at 80% and specificity at 90%, but reduces true prevalence to 1%. Among 990 nondefect tickets, 99 are flagged. Only eight of the 107 flagged tickets are true positives. A manager using the original precision to plan review staffing would be badly misled.

Bayes' rule makes the dependence explicit. If prevalence is $\rho$, sensitivity is $s$, and specificity is $q$, then

$$
\Pr(\text{defect}\mid\text{flag})=\frac{s\rho}{s\rho+(1-q)(1-\rho)}.
$$

The denominator counts both correct and incorrect flags. For a rare issue, even a modest false-positive rate can dominate that total. This is why validation should represent the deployment population or explicitly adjust for a changed sampling design.

![Precision falls as the target issue becomes rarer, even with unchanged sensitivity and specificity.](../figures/M05_prevalence.png)

Sensitivity and specificity remain at 0.80 and 0.90 in both populations. The decline in precision comes entirely from the lower prevalence. Operational evaluation should also consider the cost of missed defects, the burden of false alarms, and whether uncertain cases can be routed to human review.

## 5.6 Human and LLM Annotation

LLMs can help draft a codebook, suggest candidate labels, or classify text using explicit instructions. For a defensible measurement exercise, preserve the original text, the codebook version, model identifier, prompt, output schema, and date. Require a bounded output format with an allowed “uncertain” category where appropriate. Validate the output against the schema and inspect cases that violate the instructions.

A prompt should identify the construct, unit, categories, boundary rules, and examples. For delivery dissatisfaction, it should distinguish a complaint about an actual delay from a question about the promised delivery date. Ask for a short supporting span from the supplied text when that improves traceability. A fluent explanation is not evidence that the label is correct; compare it with independent human judgments on a relevant sample.

Human agreement is informative because the construct may itself be ambiguous. Double-code a sample, examine disagreements, and refine definitions before scaling. Report category-specific errors, prevalence, and performance across languages or product groups. An average accuracy can conceal systematic failure on the minority category that motivates the analysis.

Treat text being classified as data. A review may contain language resembling an instruction to the model. It should not change the annotation task, request external actions, or supply new system rules. Separate the fixed task instructions from the document content, constrain outputs, and inspect unexpected behavior. Use synthetic or approved text for classroom exercises involving external services.

## 5.7 Networks: Connections, Reach, and Brokerage

A network represents entities as nodes and relationships as edges. Nodes might be customers, creators, brands, or products. An edge might indicate following, communication, co-purchase, or a similarity criterion. Directed and weighted networks preserve different information from undirected binary networks. The edge definition should follow the substantive relationship the analyst intends to study.

Degree counts a node's direct connections. Betweenness summarizes how often a node lies on shortest paths between other nodes. A person with few direct contacts can have high betweenness if those contacts connect otherwise separate groups. Eigenvector-based measures give more weight to connections with well-connected nodes. These metrics describe network structure under their definitions; they do not by themselves establish persuasion, credibility, or the effect of paying a creator.

![A broker with few direct links can connect two otherwise separate customer groups.](../figures/M05_network_bridge.png)

Broker R has two direct connections, while each within-group connector has four. Removing R disconnects the two groups. A customer with fewer direct contacts can therefore be essential for reaching a different audience. A marketing campaign may value either role, depending on message transmission, audience overlap, and the intended outcome.

Observed similarity among connected customers can arise from influence, homophily, or common exposure. Friends may adopt a product because they affect one another, because they already share tastes, or because they see the same promotion. Regressing adoption on friends' adoption does not distinguish those mechanisms without additional design. Randomized encouragement, timing restrictions, or credible natural variation can help, with attention to spillovers and the unit of assignment.

## 5.8 Social-Media Case: Engagement and Commercial Value

A brand compares two creators. One receives many comments, but those comments largely come from an audience that already follows the brand. The other reaches a smaller group with less overlap. A high engagement count does not establish more incremental sales. The comparison requires a target population, exposure definition, outcome horizon, and a way to measure what would have happened without the collaboration.

Text can help describe comment content, and network overlap can describe audience duplication. Those measurements support campaign design, but they should be combined with an evaluation strategy. A test might randomize eligible regions or audience groups when feasible, or compare outcomes using a credible observational design. If communication crosses groups, spillovers can complicate the interpretation of an untreated group.

For classroom practice, construct two small audience sets and calculate their overlap. Then compare comments per exposed user with total comments. Explain why neither is a direct estimate of incremental profit.

## 5.9 AI-Assisted Workflow, Practice, and Readings

Start a text exercise with a small manually inspected sample and a codebook. Build a transparent baseline, reserve an evaluation sample, and compare a more complex method on the same outcomes. Ask an assistant to produce a confusion matrix and representative errors, then independently recompute precision and recall from the counts. Keep model selection and prompt refinement away from the final test sample.

For practice, calculate accuracy in the first complaint-detector sample: 88%. Explain why a classifier that always predicts “no defect” would achieve 99% accuracy in the rare-prevalence deployment sample while detecting no defects. Next identify how removing “not” changes the meaning of “not reliable.” Finally, explain why two highly connected adopters may share preferences even if neither caused the other's adoption.

The [scikit-learn text-feature documentation](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction) supports count and TF-IDF representations. [VADER's author repository](https://github.com/cjhutto/vaderSentiment) provides a rule-based sentiment baseline. Machine learning can support several stages of behavioral marketing research [(Hagen et al., 2020)](https://doi.org/10.1007/s11002-020-09535-7).

## 5.10 mHealth: Classifying New Food Descriptions

The manager wants to reduce the effort required to categorize a food entry. A lookup table may work well for familiar descriptions, while a text classifier may help with a new description. These are distinct deployment conditions. Repeated descriptions in both training and test records can make a random entry split look successful even when the system will struggle with unseen language.

Normalize descriptions by lowercasing, collapsing whitespace, and trimming the ends. Retain nonempty descriptions and nonmissing source categories, then sample 200,000 eligible entries with seed 534. The sample contains 37,570 distinct normalized descriptions; 1,725 appear with more than one source category. Those inconsistencies create label ambiguity. The source category is the prediction target, not a validated nutritional interpretation of the food.

The first split assigns approximately 20% of entries to testing. The second uses a fixed SHA-256 rule to hold out entire normalized descriptions. Its test entries therefore share no exact normalized description with training. Both evaluations weight food entries equally, so frequent descriptions receive more weight. A second evaluation weighting unique descriptions equally would answer a different product question.

A training-only lookup chooses the most frequent category for each description, breaking count ties alphabetically and falling back to the most frequent training category. The text alternative fits a TF-IDF vocabulary of unigrams and bigrams on distinct training descriptions, caps the vocabulary at 20,000 features, and requires a term to occur in at least two training descriptions. Multinomial naive Bayes uses smoothing of 0.1 and training description-category counts as weights.

| Evaluation | Test Entries | Familiar Descriptions | Lookup Accuracy | Text Accuracy | Text Macro F1 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Entry Split | 40,273 | 88.65% | 84.90% | 84.94% | 0.5531 |
| Description Split | 36,987 | 0% | 3.82% | 67.42% | 0.3465 |

Macro F1 averages across the 312 labels present in the combined sampled data, assigning zero to undefined class scores. Rare labels therefore matter more than in accuracy. The gap between the two evaluations reflects both familiarity and the changed test composition; it is not a causal estimate of leakage's effect. For a service processing new descriptions, the description-level evaluation is the closer test of that requirement.

![Exact-description familiarity changes the task measured by a text-classification test.](../figures/M05_mhealth_text.png)

The lookup nearly matches the text classifier on the entry split because most test descriptions already appear in training. Its collapse on unseen descriptions reveals how much of that performance depends on memory. A product could use the lookup for verified familiar terms and route uncertain new terms for review. Nutrition-based food composition matching would additionally require portion units, preparation details, and validated food codes. A category prediction alone supplies none of those quantities.

An AI assistant can help inspect ambiguous examples and propose a labeling rubric. Use only permitted local processing, preserve the original category, and evaluate proposed relabeling against independently reviewed examples. The code below makes no external model request and learns every lookup and text transformation from training rows only.

Python source: [m05.py](../../03_Data_and_Code/mHealth/recurring_examples/m05.py). From its directory, run `python m05.py`.

```python
"""Contrast familiar-description and unseen-description classification."""

import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, f1_score
from common import SEED, description_holdout, load_food, save_result

food = load_food()
usable = food.loc[food.description.ne("") & food.category.ne("Unclassified")]
sample = usable.sample(n=min(200000, len(usable)), random_state=SEED).reset_index(
    drop=True
)
rng = np.random.default_rng(SEED)
masks = {
    "entry_split": rng.random(len(sample)) < 0.2,
    "description_split": sample.description.map(description_holdout).to_numpy(),
}
results = {}
for name, mask in masks.items():
    train, test = sample.loc[~mask], sample.loc[mask]
    counts = train.groupby(["description", "category"]).size().reset_index(name="count")
    # Break tied category counts alphabetically; learn the lookup only on training rows.
    lookup = counts.sort_values(["count", "category"], ascending=[False, True])
    lookup = lookup.drop_duplicates("description").set_index("description").category
    majority = train.category.value_counts().sort_index().idxmax()
    baseline = test.description.map(lookup).fillna(majority)
    vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_features=20000, min_df=2)
    vectorizer.fit(train.description.drop_duplicates())
    classifier = MultinomialNB(alpha=0.1)
    classifier.fit(
        vectorizer.transform(counts.description),
        counts.category,
        sample_weight=counts["count"],
    )
    prediction = classifier.predict(vectorizer.transform(test.description))
    labels = sorted(set(train.category) | set(test.category))
    results[name] = {
        "train_rows": len(train),
        "test_rows": len(test),
        "familiar_description_fraction": float(
            test.description.isin(lookup.index).mean()
        ),
        "lookup_accuracy": float(accuracy_score(test.category, baseline)),
        "nb_accuracy": float(accuracy_score(test.category, prediction)),
        "nb_macro_f1": float(
            f1_score(
                test.category,
                prediction,
                labels=labels,
                average="macro",
                zero_division=0,
            )
        ),
        "test_label_unseen_in_train_fraction": float(
            (~test.category.isin(train.category.unique())).mean()
        ),
        "metric_classes": len(labels),
    }
ambiguity = sample.groupby("description").category.nunique()
result = {
    "sample_rows": len(sample),
    "descriptions": len(ambiguity),
    "descriptions_with_multiple_labels": int(ambiguity.gt(1).sum()),
    "splits": results,
}
save_result("M05", result)
print(json.dumps(result, indent=2))
```

## 5.11 Python Calculations for the Synthetic Cases

Run the program below to write the synthetic examples to CSV and reproduce their calculations. Keep the script beside `example_helpers.py` in `03_Data_and_Code/Lecture_Examples`; the separate mHealth programs reproduce the observed-data results.

Python source: [m05_synthetic.py](../../03_Data_and_Code/Lecture_Examples/m05_synthetic.py). From its directory, run `python m05_synthetic.py`.

```python
"""Synthetic numerical examples for M5; run from any working directory."""

import itertools
import json
import math
from example_helpers import write_csv, ols_slope, shares

r = {}
r["M05"] = {}
for positive in [200, 10]:
    tp = 0.8 * positive
    fn = positive - tp
    fp = 0.1 * (1000 - positive)
    tn = 1000 - positive - fp
    r["M05"][str(positive / 1000)] = {
        "tp": tp,
        "fp": fp,
        "fn": fn,
        "tn": tn,
        "precision": tp / (tp + fp),
        "accuracy": (tp + tn) / 1000,
    }
write_csv(
    "M05_annotation_synthetic.csv",
    [
        "prevalence",
        "true_positive",
        "false_positive",
        "false_negative",
        "true_negative",
    ],
    [(p, v["tp"], v["fp"], v["fn"], v["tn"]) for p, v in r["M05"].items()],
)
print(json.dumps(r, indent=2))
```

## 5.12 mHealth: Text Topics and Their Denominators

A product manager wants to organize a large food-description vocabulary into interpretable groups. Repeated entries make a frequently logged description prominent, while a catalog of distinct descriptions emphasizes the range of language available. These populations answer different questions. A topic model fitted to distinct descriptions can summarize vocabulary, but its topic shares need a separate choice of observation unit.

Use all 50,860 distinct nonempty normalized descriptions recorded before July 1. Fit TF-IDF on these descriptions, retaining at most 3,000 unigram and bigram features, removing English stop words, and requiring a feature in at least three documents. The maximum document-frequency threshold is 0.95. Fix the number of nonnegative matrix factorization components at four as an illustrative specification. No July description is used to learn the vocabulary, inverse-document frequencies, or component vectors.

Let $V$ contain nonnegative TF-IDF features, with one row per training description. NMF approximates $V$ by $WH$, where the rows of $H$ contain term patterns and each row of $W$ gives the associated nonnegative loadings. The chosen specification minimizes squared reconstruction error subject to nonnegative factors. Multiplying a row of $H$ by a constant and dividing its column of $W$ by the same constant preserves the approximation. Before comparing loadings, the code therefore scales them to correspond to component term vectors with unit Euclidean norm.

July contains 17,042 distinct nonempty descriptions and 79,957 entries, including 5,208 descriptions absent from training. Apply the frozen vectorizer and factorization to these descriptions, assigning each to its largest scaled loading when positive and leaving zero-vector descriptions unassigned. The resulting groups have the following leading terms and shares.

| Leading Terms | Share of Distinct July Descriptions | Share of July Entries |
| --- | ---: | ---: |
| Chicken, Breast, Soup | 14.83% | 10.12% |
| Cheese, Cheddar, Pizza | 32.52% | 29.92% |
| Chocolate, Bar, Dark | 32.22% | 38.45% |
| Salad, Dressing, Greek | 17.01% | 19.15% |
| Unassigned | 3.42% | 2.36% |

![Weighting descriptions by their observed entry frequency changes the apparent prominence of the same fixed topics.](../figures/M05_topic_denominators.png)

The chocolate-related component receives a larger share when repeated entries determine the weights. This result concerns the language and repetition of recorded entries. The component includes other terms and does not define a validated food group, calorie share, or measure of nutritional quality. Assigning a dominant component also discards information about mixtures. The 583 unassigned descriptions expose a vocabulary-coverage problem that would be hidden by forcing every text into a topic.

[Blueprints for Text Analytics, Chapter 8](https://github.com/blueprints-for-text-analytics-python/blueprints-text/blob/master/ch08/Topic_Modeling_Clustering.ipynb) provides an NMF topic-model example. [BERTopic's representation documentation](https://maartengr.github.io/BERTopic/getting_started/representation/representation.html) offers separate methods for describing topics. An LLM-generated topic name should remain attached to the component's terms and inspected examples. A fluent name supplies no independent evidence that a component measures preference, healthfulness, or a commercial segment.

A useful AI-assisted extension changes one choice at a time: the number of topics, frequency weighting during fitting, or the vocabulary threshold. Compare representative descriptions and unmatched texts as well as reconstruction error. Improving the numerical objective alone does not establish that a proposed topic label answers the manager's question.

Python source: [topics.py](../../03_Data_and_Code/mHealth/recurring_examples/topics.py). From its directory, run `python topics.py`.

```python
"""Local topic decomposition of food descriptions with a future-text check."""

import json
import numpy as np
from sklearn.decomposition import NMF
from sklearn.feature_extraction.text import TfidfVectorizer
from common import SEED, load_food, save_result


if __name__ == "__main__":
    food = load_food()
    prior = food.loc[(food.date < "2016-07-01") & food.description.ne("")]
    training_text = sorted(prior.description.unique())
    july = food.loc[
        food.date.between("2016-07-01", "2016-07-31") & food.description.ne("")
    ]
    counts = july.groupby("description").size().sort_index()
    vectorizer = TfidfVectorizer(
        min_df=3,
        max_df=0.95,
        max_features=3000,
        ngram_range=(1, 2),
        stop_words="english",
    )
    train_matrix = vectorizer.fit_transform(training_text)
    model = NMF(
        n_components=4, init="nndsvda", random_state=SEED, max_iter=500, tol=1e-4
    )
    model.fit(train_matrix)
    future_matrix = vectorizer.transform(counts.index)
    # Put topic term vectors on a common L2 scale before comparing loadings.
    weights = model.transform(future_matrix) * np.linalg.norm(model.components_, axis=1)
    assigned = weights.sum(axis=1) > 1e-12
    labels = np.where(assigned, weights.argmax(axis=1), -1)
    terms = vectorizer.get_feature_names_out()
    rows = []
    for topic in range(4):
        selected = labels == topic
        top = np.argsort(-model.components_[topic], kind="stable")[:6]
        rows.append(
            {
                "topic": topic + 1,
                "terms": terms[top].tolist(),
                "distinct_description_share": float(selected.mean()),
                "food_entry_share": float(
                    counts.to_numpy()[selected].sum() / counts.sum()
                ),
            }
        )
    result = {
        "training_distinct_descriptions": len(training_text),
        "training_entries": len(prior),
        "vocabulary_terms": len(terms),
        "july_distinct_descriptions": len(counts),
        "july_entries": int(counts.sum()),
        "july_new_descriptions": int((~counts.index.isin(training_text)).sum()),
        "july_zero_vocabulary_descriptions": int(
            (future_matrix.getnnz(axis=1) == 0).sum()
        ),
        "july_unassigned_descriptions": int((~assigned).sum()),
        "july_unassigned_entries": int(counts.to_numpy()[~assigned].sum()),
        "iterations": int(model.n_iter_),
        "topics": rows,
    }
    assert model.n_iter_ < model.max_iter
    assert np.isclose(
        sum(row["food_entry_share"] for row in rows)
        + result["july_unassigned_entries"] / counts.sum(),
        1,
    )
    save_result("topics", result)
    print(json.dumps(result, indent=2))
```

## 5.13 Review Provenance and Generated Language

\noindent A retailer using reviews to describe a product needs to preserve the distinction between an actual customer's experience and generated wording. An LLM can summarize a collection of genuine reviews, but its output can introduce an experience that no reviewer reported. A sentiment classifier can also assign a confident label to a false or irrelevant text. Model accuracy and the authenticity of the underlying evidence address different questions.

Preserve the review identifier, source, date, any recorded incentive, and the text actually analyzed. A summary should retain the relevant review denominator and material disagreement. A generated quotation attributed to a customer requires that customer's actual words and appropriate permission. A synthetic example used to test a parser should remain labeled synthetic and separate from reviews offered to potential buyers.

The FTC's Consumer Reviews and Testimonials Rule addresses specified conduct involving false reviews and testimonials. Its provisions distinguish creation, purchase, dissemination, and mere hosting, with different knowledge conditions. AI generation alone does not determine whether a testimonial misrepresents experience. The relevant questions concern the speaker, actual experience, claim, and business conduct. See the [FTC's questions and answers](https://www.ftc.gov/business-guidance/resources/consumer-reviews-testimonials-rule-questions-answers).

A useful assessment samples the original texts behind a generated theme, checks whether each factual claim is supported, and records unsupported statements separately from ordinary classification errors. The rare-complaint example in Section 5.5 supplies another check: a high false-positive share can make a generated summary overstate the prevalence of a problem even when individual labels have respectable sensitivity and specificity.

## 5.14 Earnings Calls: Pricing Language, Speaking Exposure, and Meaning

\noindent A communications team can use public earnings calls to identify pricing statements that require contextual reading. The decision is which statements to examine and what additional evidence to request. The supplied core dictionary includes dynamic, personalized, algorithmic, and AI pricing as well as electronic shelf labels. These terms retrieve heterogeneous business objects. A display technology, a planned test, and an implemented price rule have different implications for customers.

### 5.14.1 A Call-Level Comparison

\noindent Among calls with observed text, the supplied retail group has 36 core-positive calls out of 1,241, or 2.90%; restaurants have 9 of 445, or 2.02%; and the comparison group has 67 of 639, or 10.49%. Calls receive equal weight. Firms with more captured calls consequently receive more weight in a pooled group rate. The categories differ in their business models, communication practices, and sample coverage. A higher rate identifies more frequent use of the specified language within the observed corpus.

Calendar-quarter summaries use the date on which the call occurred. Fiscal-quarter labels can refer to different calendar periods across firms. The first and last quarters have incomplete calendar windows, and the number of firms varies across quarters. Reporting the call and firm counts beside each share makes those differences visible. Complete calendar support does not establish complete capture of every firm's calls.

### 5.14.2 Who Speaks More About Pricing?

\noindent Management supplies 127 of the 150 core occurrences and analysts supply 23. Management also speaks far more words. To measure language intensity for role $r$ on the same set of observed calls, calculate

$$
I_r=10{,}000\frac{\sum_{c\in\mathcal C}M_{cr}}{\sum_{c\in\mathcal C}W_{cr}},
$$

where $M_{cr}$ is the core-occurrence count and $W_{cr}$ is the number of words attributed to role $r$ in call $c$. The multiplier expresses occurrences per 10,000 words. The ratio pools word exposure, so long speaking segments receive greater weight than short ones.

Management's 16,685,338 words imply 0.076 occurrences per 10,000 words. Analysts' 2,761,999 words imply 0.083. The raw-count ranking reverses after exposure adjustment. This arithmetic does not establish that analysts are more concerned about pricing: management includes prepared remarks and answers, analysts principally ask questions, and role assignments are heuristic. The rates describe the supplied labels and text exposure without a population significance claim.

![Management has 127 core occurrences and analysts have 23. After dividing by the words attributed to each role, the respective rates are 0.076 and 0.083 per 10,000 words. The two panels use different labeled units and preserve a zero baseline.](../figures/M05_calls_exposure.png)

The Q&A detector fails to identify a boundary for 86 supplied calls, including the empty transcript. Restricting both counts and words to the 2,240 observed calls with detected Q&A yields 115 management occurrences in 15,985,597 words, or 0.072 per 10,000. The analyst rate remains 0.083. This sensitivity addresses the flagged boundaries while retaining the substantive difference between prepared remarks and questions. A stronger role comparison would require verified turn labels and comparable speaking contexts.

Python source: [disclosure.py](../../03_Data_and_Code/Earnings_Calls/disclosure.py). From `03_Data_and_Code/Earnings_Calls`, run `python disclosure.py`. Python, pandas, and NumPy are required; the committed metadata supply all inputs.

```python
"""Compare pricing-language coverage with explicit call and word denominators."""
import pandas as pd
from assessment import HERE, load_checked


def role_rates(calls, mentions, require_qa=False):
    sample = calls.loc[calls.text_observed & (calls.qa_detected | (not require_qa))]
    core = mentions.loc[mentions.tier.eq('core') & mentions.call_id.isin(sample.call_id)]
    rows = []
    for role in ['management', 'analyst']:
        n = int(core.role.eq(role).sum())
        words = int(sample['words_' + role].sum())
        rows.append({'sample': 'detected_qa' if require_qa else 'all_observed',
                     'role': role, 'calls': len(sample), 'core_matches': n,
                     'words': words, 'per_10000_words': 10000 * n / words if words else float('nan')})
    return pd.DataFrame(rows)


def main():
    calls, mentions, _, _ = load_checked()
    valid = calls.loc[calls.text_observed].copy()
    groups = valid.groupby('group').agg(
        calls=('call_id', 'size'), positive_calls=('has_core', 'sum'),
        core_matches=('n_core', 'sum'))
    groups['share_percent'] = 100 * groups.positive_calls / groups.calls
    groups.to_csv(HERE / 'results/group_rates.csv')
    roles = pd.concat([role_rates(calls, mentions), role_rates(calls, mentions, True)])
    roles.to_csv(HERE / 'results/role_rates.csv', index=False)
    valid['calendar_quarter'] = valid.call_date.dt.to_period('Q')
    quarter = valid.groupby('calendar_quarter').agg(
        calls=('call_id', 'size'), positive_calls=('has_core', 'sum'),
        firms=('ticker', 'nunique'))
    quarter['share_percent'] = 100 * quarter.positive_calls / quarter.calls
    # Calendar coverage does not imply complete capture of all firms' calls.
    start, end = pd.Timestamp('2021-11-02'), pd.Timestamp('2026-11-02')
    quarter['full_calendar_window'] = [
        q.start_time >= start and q.end_time.normalize() <= end for q in quarter.index]
    quarter.to_csv(HERE / 'results/quarter_rates.csv')
    print(groups.round(4).to_string())
    print(roles.round(6).to_string(index=False))


if __name__ == '__main__':
    (HERE / 'results').mkdir(exist_ok=True)
    main()
```

### 5.14.3 A Match is a Retrieval Decision

\noindent Consider seven purposeful cases from the supplied excerpts. Amazon's October 2024 statement concerns displaying current prices and deals. Eventbrite's August 2023 statement concerns advertising cost per click. Wendy's February 2024 statement concerns future tests. Kroger's September 2025 statement concerns shelf-label infrastructure, while its September 2022 statement describes personalized promotional investment. Delta's July 2025 statement describes AI-enhanced pricing; a January 2025 question about cabin pricing is recorded as management prepared remarks and warrants speaker review. Each case has an original match ID and source URL in [the interpretation table](../../03_Data_and_Code/Earnings_Calls/data/interpretation_cases.csv).

A coding scheme should identify the priced object, current use versus future intention, assertion versus question or denial, and the scope of supporting evidence. The seven examples expose distinctions; their purposeful selection supplies no estimate of corpus precision. The original notes' reported precision check lacks the underlying adjudicated labels needed for independent verification. Recall additionally requires examining relevant passages that were never retrieved. Re-running a regex on truncated stored excerpts cannot measure whole-call recall.

The synthetic contrast set below holds a pricing phrase nearly fixed while changing its meaning. Denial, intention, and a question all retrieve the same core term. A sentence describing fares that change hourly with demand supplies a plausible paraphrase that the dictionary misses. These are specified counterexamples to an interpretation rule, with no empirical model-performance claim.

Python source: [construct_checks.py](../../03_Data_and_Code/Earnings_Calls/construct_checks.py). From `03_Data_and_Code/Earnings_Calls`, run `python construct_checks.py`. Python, pandas, and NumPy are required; the committed metadata supply all inputs.

```python
"""Use synthetic contrast cases to separate dictionary retrieval from adoption."""
import re
import pandas as pd
from assessment import HERE


def match_terms(text, dictionary):
    return [row.term_id for row in dictionary.itertuples()
            if re.search(row.regex, text, 0 if row.case_sensitive else re.IGNORECASE)]


def main():
    dictionary = pd.read_csv(HERE / 'data/dictionary.csv')
    # All sentences below are synthetic, with intentionally specified meanings.
    examples = [
        ('We use dynamic pricing in all stores.', True, 'current_use', True),
        ('We do not use dynamic pricing.', True, 'denial', False),
        ('We may test dynamic pricing next year.', True, 'future_intention', False),
        ('Do you plan to use dynamic pricing?', True, 'question', False),
        ('The app displays real-time pricing information.', True, 'price_display', False),
        ('We installed electronic shelf labels.', True, 'infrastructure', False),
        ('Our fares adjust every hour with demand.', False, 'current_use', True),
        ('We observed a surge in demand.', False, 'demand_only', False),
    ]
    rows = []
    for text, expected_hit, meaning, current_use in examples:
        terms = match_terms(text, dictionary)
        core = dictionary.loc[dictionary.term_id.isin(terms), 'tier'].eq('core').any()
        assert bool(core) == expected_hit, (text, terms)
        rows.append({'synthetic_text': text, 'core_hit': bool(core),
                     'terms': '|'.join(terms), 'specified_meaning': meaning,
                     'specified_current_use': current_use})
    output = pd.DataFrame(rows)
    output.to_csv(HERE / 'results/synthetic_construct_checks.csv', index=False)
    print(output[['core_hit', 'specified_meaning', 'specified_current_use']].to_string(index=False))
    cases = pd.read_csv(HERE / 'data/interpretation_cases.csv')
    mentions = pd.read_csv(HERE / 'data/mentions.csv')
    assert cases.mention_id.is_unique and set(cases.mention_id) <= set(mentions.mention_id)
    # A purposeful interpretation set supplies examples, not population precision.
    cases[['mention_id', 'case_label', 'evidence_scope']].to_csv(
        HERE / 'results/interpretation_summary.csv', index=False)


if __name__ == '__main__':
    (HERE / 'results').mkdir(exist_ok=True)
    main()
```

### 5.14.4 AI-Assisted Interpretation and Review Effort

\noindent Ask an assistant to propose a schema before requesting labels. Require the match ID, priced object, timing, type of speaker claim, evidence scope, and an explicit unknown value when context is insufficient. Compare its output with the recorded cases and require source-grounded explanations for disagreements. Inspect the original turn when a management record appears to contain a question. Punctuation alone can misclassify a quoted question or a rhetorical statement.

For empirical evaluation, draw passages with known selection probabilities from both retrieved and nonretrieved text, obtain independent human labels, adjudicate disagreements, and reserve firms or later calls for evaluation. Freeze prompts and dictionary choices before using the held-out sample. If sampling oversamples hits, use the sampling probabilities when estimating population performance. Repeated corporate wording makes random sentence splits especially vulnerable to leakage.

The supplied firm score combines chosen weights on percentile ranks among firms with positive matches. Such a score can order a reading queue, but it lacks labeled outcomes and probability calibration. Keep coverage, recency, and unresolved interpretation separate so that a reviewer can see why a firm was selected. A no-match firm remains in the coverage table, and absent text remains unknown. Pricing behavior, consumer outcomes, and legal exposure require observations beyond disclosure counts.

## 5.15 Repeated Prompt Revision and Independent Text Evaluation

\noindent An analyst building an earnings-call classifier wants to know whether a revised prompt recognizes the intended pricing construct on new material. Correcting a prompt after inspecting a mislabeled passage uses that passage for development. A later correct label on the same passage establishes that the revision handled a known example. Generalization requires a comparison on additional documents whose labels did not guide the revision.

The document split should match the intended use. A tool for previously unseen firms needs evaluation on firms excluded from development. A tool for later calls from familiar firms needs a chronological separation and inputs available at the forecast date. Passages from one call share management, vocabulary, and context, so they should remain together when splitting documents. Repeated calls from a firm can also create dependence. Uncertainty should reflect that structure.

Freeze the construct definition, prompt, model configuration, retrieval procedure, and scoring rule before the final comparison. An independent reference label should be based on the underlying passage and its context. Agreement among generated explanations provides little protection when they share the same missing context or coding mistake. Preserve a dictionary baseline and allow it the same eligible evidence. Evaluate errors consequential for the intended review queue, including false positives and missed statements.

Once final labels guide another revision, the exposed documents belong to development. A new confirmation requires additional evidence or a prespecified procedure that accounts for the adaptive reuse. M7, Section 7.20, calculates how choosing among many equally uninformative candidates can produce apparently strong development accuracy while performance on fresh cases remains at chance. That mechanism applies even when every candidate runs without a software error.

## 5.16 A Text Classifier Needs an Agency Definition

\noindent A research review can mistake persuasive language for evidence that consumers lost control. The construct must be defined before an LLM assigns labels. Here, agency concerns the ability to understand material terms, form a choice, act on it, and revise or end the relationship. Adoption, continued use, and a favorable brand evaluation are insufficient by themselves to establish impairment. A consumer can value a recommendation or deliberately delegate a decision.

The [paper cards](../../01_Resources/13_Consumer_Agency_and_Recent_Research/CATALOG.md) separate managerial implications from an agency assessment and identify the evidence read. A useful extraction record contains the decision, setting, study design, outcome, proposed mechanism, source passage, and evidence level. It should distinguish an experimentally observed response, a qualitative account of restricted control, a conditional theoretical prediction, and a possible misuse inferred by the reviewer. Those categories answer different questions.

In [Immersive Service: Characteristics, Challenges, and Pathways to Consumer Agency](https://doi.org/10.1177/00222429251319312), qualitative evidence from residential care connects agency to service boundaries, roles, protocols, and voice. The managerial implications include assessing residents' desired control, their constraints, and feasible opportunities to shape daily activities. This provides direct substantive guidance about agency in a particular service setting. Generalization to digital subscriptions requires a separate argument about which mechanisms carry over.

By contrast, [Nudging App Adoption](https://doi.org/10.1177/00222429221141066) examines how choice presentation changes feature adoption. Its retrieved discussion states that enabling a feature still required an active choice and that the interventions left the actual default unchanged. Presentation can nevertheless influence habitual responses and decision time. A reviewer may infer a concern about poorly understood privacy choices, while the paper's beneficial public-health setting remains part of the evidence. Conflating that inference with demonstrated deception would corrupt the label.

For an AI-assisted review, provide the source text and require a passage supporting each nonzero feature. Permit an insufficient-evidence response. Have independent readers code a prespecified set that includes protective cases and uncertain cases, compare disagreements, and adjudicate the definitions before extending the labels. Preserve initial and revised codes. A high agreement rate establishes consistency under the coding protocol; construct validity still depends on whether the labels capture meaningful consumer control. The clustering program in Section 4.17 reproduces the numerical grouping from the saved labels, while the evidentiary judgment remains a separate task.

## 5.17 University Affiliations Define a Different Research Network

\noindent A literature review can ask which universities appear together on papers and whether their shared research covers different mechanisms. The observation units and similarity measure differ from the mechanism clustering in Section 4.17. Universities are the network nodes, while shared publication affiliations create links. A link can arise through separate coauthors or one author's multiple affiliations. It does not establish institutional endorsement of a research implication or identify a university's causal influence on an author.

The eligible journal census contains 824 records. Work-specific OpenAlex metadata, with one affiliation correction verified against a retrieved published article, identifies 424 higher-education institutions across 745 papers. Seventy-nine papers lack an identified education affiliation. The metadata category includes universities, colleges, and independent business schools. Names are resolved through institution IDs and ROR links; distinct campuses and schools remain separate when their identifiers differ. Affiliations refer to the authors' institutions recorded for each work, which can differ from their current employers. Automated matching and differences across publication versions can still create errors.

For paper $p$, let $U_p$ be its set of distinct universities and let $k_p$ be the number of institutions in that set. A paper with at least two universities contributes total edge weight one, divided across all of its university pairs:

$$
w_{ij}=\sum_{p:k_p\geq2}\frac{\mathbf{1}\{i,j\in U_p,\ i\ne j\}}{\binom{k_p}{2}}.
$$

A two-university paper contributes one to its single link. A three-university paper contributes one-third to each of three links. This normalization prevents papers with many affiliations from mechanically receiving more total network weight. Repeated authors from the same institution do not multiply its presence. Single-university papers contribute no cross-university edge but remain in publication totals.

Louvain clustering searches for communities with more internal link weight than a degree-based benchmark. Its modularity objective can be written as

$$
Q=\frac{1}{2m}\sum_{i,j}\left(w_{ij}-\gamma\frac{s_i s_j}{2m}\right)\mathbf{1}\{c_i=c_j\},
$$

where $s_i=\sum_jw_{ij}$ is university $i$'s weighted degree, $m$ is total undirected edge weight, $c_i$ is its community, and $\gamma$ controls resolution. The benchmark allows universities with more links to have more expected within-group weight. Higher resolution generally favors smaller groups. The algorithm is a heuristic; different seeds can reach different partitions with similar objective values.

At resolution one and seed 534, the network's 1,766 links produce 19 communities among 415 connected institutions. Nine additional institutions have no cross-institution edge and remain unconnected. The connected institutions occupy six components. Modularity is 0.471. Publication totals split each paper equally across its universities, with each paper contributing one in total across communities. Distinct-paper counts can overlap across groups, so they cannot be added as a unique total.

![The six largest affiliation communities contain 154.15, 84.54, 74.65, 67.16, 57.80, and 48.52 fractional papers. The grouping uses university co-occurrence and does not use the agency labels.](../figures/M05_affiliation_communities.png)

The largest community includes Columbia, the University of Texas at Dallas, the Chinese University of Hong Kong, and Yale among its largest fractional contributors. Other communities include different combinations across countries. A community name based on geography or assumed research intent would add information the algorithm never used. Stable IDs connect each group to its complete membership and paper allocations.

Across twenty seeds, the median adjusted Rand index relative to the primary fit is 0.522. Replacing fractional edges with a full count for every pair lowers agreement to 0.193. These results show that institutional membership is sensitive to the representation and optimization. The community count describes one fitted network, with the alternatives retained for comparison.

Agency-mechanism profiles are then overlaid on the communities using only reviewed papers and the same fractional allocation. Their denominator is the community's fractional mass of reviewed papers with a reported choice concern or inferred possible dual use. For example, C01 contains 22 distinct such papers, contributing 13.53 fractional papers; C03 has eight distinct papers and receives a small-sample flag. Missing reviews remain missing. These profiles describe a selected publication set and do not estimate a university's propensity to erode agency.

The runnable program reads the public paper-institution pairs, coverage table, and reviewed codes. It preserves unconnected institutions, checks total edge weight and paper allocations, exports every membership and link, and compares seeds, resolution, and weighting. The [affiliation guide](../../03_Data_and_Code/Consumer_Agency_Literature/AFFILIATIONS.md) records source definitions and the verified correction. Method references: [OpenAlex authorships](https://help.openalex.org/data/authorships/), [NetworkX Louvain documentation](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.community.louvain.louvain_communities.html), and [(Blondel et al., 2008)](https://doi.org/10.1088/1742-5468/2008/10/P10008).

Python source: [affiliation_clusters.py](../../03_Data_and_Code/Consumer_Agency_Literature/affiliation_clusters.py).

```python
"""Cluster universities by shared-paper affiliations and overlay reviewed mechanisms."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json
import numpy as np
import pandas as pd
import networkx as nx
from sklearn.metrics import adjusted_rand_score
from cluster import FEATURES, RISK

HERE = Path(__file__).resolve().parent


def make_graph(pairs, fractional=True):
    graph = nx.Graph()
    graph.add_nodes_from(sorted(pairs.institution_id.unique()))
    multipaper = 0
    for _, group in pairs.groupby('paper_id', sort=True):
        nodes = sorted(set(group.institution_id))
        k = len(nodes)
        if k < 2:
            continue
        multipaper += 1
        weight = 2 / (k * (k - 1)) if fractional else 1.0
        for left, right in combinations(nodes, 2):
            if not graph.has_edge(left, right):
                graph.add_edge(left, right, weight=0.0, shared_papers=0)
            graph[left][right]['weight'] += weight
            graph[left][right]['shared_papers'] += 1
    if fractional:
        assert np.isclose(graph.size(weight='weight'), multipaper)
    assert nx.number_of_selfloops(graph) == 0
    return graph


def communities(graph, seed=534, resolution=1):
    connected = graph.subgraph([n for n in graph if graph.degree(n) > 0]).copy()
    groups = nx.community.louvain_communities(connected, weight='weight', seed=seed, resolution=resolution)
    return connected, groups


def labels(groups, nodes):
    lookup = {node: i for i, group in enumerate(groups) for node in group}
    return [lookup[node] for node in nodes]


def main():
    pairs = pd.read_csv(HERE / 'paper_affiliations.csv').sort_values(['paper_id', 'institution_id'])
    coverage = pd.read_csv(HERE / 'affiliation_coverage.csv')
    reviews = pd.read_csv(HERE / 'coded_papers.csv')
    assert not pairs.duplicated(['paper_id', 'institution_id']).any()
    assert coverage.paper_id.is_unique and reviews.id.is_unique
    pairs['paper_weight'] = 1 / pairs.groupby('paper_id').institution_id.transform('size')
    np.testing.assert_allclose(pairs.groupby('paper_id').paper_weight.sum(), 1)
    graph = make_graph(pairs)
    connected, groups = communities(graph)
    # Community IDs are display labels ordered by fractional publication mass.
    mass = pairs.groupby('institution_id').paper_weight.sum()
    groups = sorted(groups, key=lambda g: (-float(mass.loc[list(g)].sum()), min(g)))
    membership = {node: f'C{i+1:02d}' for i, group in enumerate(groups) for node in group}
    pairs['community'] = pairs.institution_id.map(membership).fillna('Unconnected')
    universities = pairs.groupby(['institution_id', 'institution_name', 'community']).agg(
        papers=('paper_id', 'nunique'), fractional_papers=('paper_weight', 'sum')).reset_index()
    universities['weighted_degree'] = universities.institution_id.map(dict(graph.degree(weight='weight')))
    # Split each paper across its universities; its total contribution remains one.
    allocation = pairs.groupby(['paper_id', 'community']).paper_weight.sum().reset_index()
    allocation = allocation.merge(coverage, on='paper_id', validate='many_to_one')
    allocation = allocation.merge(reviews[['id'] + FEATURES], left_on='paper_id', right_on='id',
                                  how='left', validate='many_to_one').drop(columns='id')
    output = HERE / 'results/affiliations'
    output.mkdir(parents=True, exist_ok=True)
    university_rows, mechanism_rows = [], []
    for community, group in allocation.groupby('community', sort=True):
        members = universities.loc[universities.community == community].sort_values(
            ['fractional_papers', 'institution_name'], ascending=[False, True])
        reviewed = group.loc[group.review_status.ne('not_reviewed')]
        risk = group.loc[group.review_status.isin(RISK)]
        assert not risk[FEATURES].isna().any().any()
        university_rows.append({'community': community, 'universities': len(members),
            'distinct_papers': group.paper_id.nunique(), 'fractional_papers': group.paper_weight.sum(),
            'reviewed_papers': reviewed.paper_id.nunique(), 'reviewed_fractional_papers': reviewed.paper_weight.sum(),
            'risk_reviewed_papers': risk.paper_id.nunique(), 'risk_reviewed_fractional_papers': risk.paper_weight.sum(),
            'largest_affiliations_by_fractional_papers': '; '.join(members.institution_name.head(4))})
        for feature in FEATURES:
            numerator = (risk[feature] * risk.paper_weight).sum()
            denominator = risk.paper_weight.sum()
            mechanism_rows.append({'community': community, 'feature': feature,
                'weighted_positive': numerator, 'weighted_reviewed_risk_denominator': denominator,
                'share': numerator / denominator if denominator else None,
                'distinct_reviewed_risk_papers': risk.paper_id.nunique(),
                'small_review_sample': risk.paper_id.nunique() < 10})
    nodes = sorted(connected)
    reference = labels(groups, nodes)
    sensitivity = []
    for resolution in [.5, 1., 1.5]:
        for seed in range(20):
            _, candidate = communities(graph, seed=seed, resolution=resolution)
            sensitivity.append({'resolution': resolution, 'seed': seed, 'communities': len(candidate),
                'modularity': nx.community.modularity(connected, candidate, weight='weight', resolution=resolution),
                'ari_against_primary': adjusted_rand_score(reference, labels(candidate, nodes))})
    full_graph = make_graph(pairs, fractional=False)
    _, full_groups = communities(full_graph)
    edges = [{'left': a, 'right': b, **d} for a, b, d in graph.edges(data=True)]
    university_table = pd.DataFrame(university_rows)
    assert np.isclose(university_table.fractional_papers.sum(), pairs.paper_id.nunique())
    universities.to_csv(output / 'university_membership.csv', index=False)
    university_table.to_csv(output / 'community_summary.csv', index=False)
    allocation.to_csv(output / 'paper_community_weights.csv', index=False)
    pd.DataFrame(mechanism_rows).to_csv(output / 'mechanism_profiles.csv', index=False)
    pd.DataFrame(edges).to_csv(output / 'university_edges.csv', index=False)
    sensitivity = pd.DataFrame(sensitivity)
    sensitivity.to_csv(output / 'sensitivity.csv', index=False)
    journal = allocation.groupby(['community', 'journal']).paper_weight.sum().reset_index()
    journal.to_csv(output / 'journal_profiles.csv', index=False)
    same_resolution = sensitivity.loc[sensitivity.resolution.eq(1), 'ari_against_primary']
    summary = {'eligible_papers': len(coverage), 'papers_with_university': pairs.paper_id.nunique(),
        'papers_without_university': int(coverage.university_count.eq(0).sum()),
        'multi_university_papers': int(coverage.university_count.gt(1).sum()),
        'universities': graph.number_of_nodes(), 'edges': graph.number_of_edges(),
        'unconnected_universities': len(list(nx.isolates(graph))), 'communities': len(groups),
        'connected_components': nx.number_connected_components(connected),
        'modularity': nx.community.modularity(connected, groups, weight='weight'),
        'seed_ari_quantiles': same_resolution.quantile([.1,.5,.9]).tolist(),
        'full_counting_ari': adjusted_rand_score(reference, labels(full_groups, nodes)),
        'shared_author_list_flagged_papers': int(coverage.shared_author_affiliation_list.sum()),
        'networkx_version': nx.__version__, 'resolution': 1, 'seed': 534}
    (output / 'summary.json').write_text(json.dumps(summary, indent=2) + '\n')
    print(json.dumps(summary, indent=2))
    print(university_table.head(6).to_string(index=False))


if __name__ == '__main__':
    main()
```

## 5.18 A Changing Judge Can Change the Apparent Improvement

\noindent A marketing team compares summaries of the same earnings calls produced by two AI configurations. It uses an LLM judge to score factual support, coverage, and clarity. If the team also changes the judge, a higher reported score can reflect the generator, the judge, or their interaction. A fixed rubric names the intended criteria, but different judges can still apply it differently.

Consider four stipulated mean scores on the same 0-100 rubric. The old judge assigns 60 to the old generator's saved outputs and 62 to the new generator's outputs. The new judge assigns 75 and 77 to those same respective output sets. Comparing the old system's score of 60 with the new system's score of 77 gives seventeen points. Holding either judge fixed gives two points. The remaining fifteen points arise from the changed judgment of the old outputs.

![Both judge versions score the same saved outputs from each generator. Within either judge, the new generator gains two points. Changing both generator and judge together produces a seventeen-point difference, including a fifteen-point judge shift. All scores are stipulated.](../figures/M05_judge_change.png)

Model-judge evaluations document position, verbosity, and self-enhancement biases [(Zheng et al., 2023)](https://arxiv.org/abs/2306.05685). A separate experiment examines self-recognition and preference for a model's own summaries [(Panickssery et al., 2024)](https://arxiv.org/abs/2404.13076). These findings motivate scoring saved outputs with both judge versions, varying presentation order, and comparing with independently assessed evidence. Freezing a judge preserves a comparison rule; it does not establish that the rule is correct.

For a review summary, independently assess whether each conclusion is supported by the underlying reviews, whether dissenting experiences are represented, and whether uncertainty is retained. For an earnings-call summary, check speaker role, timing, and the distinction between a claim and an implemented action. Preserve inconsistent or unscorable judgments in the denominator. A parser failure and an incorrect substantive judgment are different failures.

Evidence on sycophancy motivates a controlled feedback exercise [(Sharma et al., 2024)](https://arxiv.org/abs/2310.13548v4). Hold the same marketing proposal and evidence fixed while varying whether a sponsor is described as liking it, disliking it, or expressing no view. Compare factual criticism and recommendations under the same rubric. A change in approval can reflect responsiveness to the sponsor's position without adding evidence about the proposal's commercial value. This is a proposed comparison; no course model responses have been collected.

### 5.18.1 Reproduce the Judge Comparison

\noindent The four imposed mean scores define the comparison, with differences measured in score points. They contain no observed model performance. In a real evaluation, repeated outputs from the same call should remain grouped when estimating uncertainty.


Python source: [evaluate_judges.py](../../03_Data_and_Code/LLM_Revalidation/evaluate_judges.py).

```python
"""A constructed generator-by-judge comparison on a fixed 0-100 rubric."""
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent

def compare(scores):
    old, new = scores["old_judge"], scores["new_judge"]
    return dict(scores=scores,
        diagonal_change=new["new_generator"]-old["old_generator"],
        generator_change_old_judge=old["new_generator"]-old["old_generator"],
        generator_change_new_judge=new["new_generator"]-new["old_generator"],
        judge_change_old_generator=new["old_generator"]-old["old_generator"])

def main():
    # Scores are imposed. Both judges assess the same saved outputs for each generator.
    scores = {"old_judge": {"old_generator": 60, "new_generator": 62},
              "new_judge": {"old_generator": 75, "new_generator": 77}}
    result = compare(scores)
    assert result["diagonal_change"] == (
        result["generator_change_new_judge"]+result["judge_change_old_generator"])
    output = HERE / "results"
    output.mkdir(exist_ok=True)
    (output / "judge_comparison.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
if __name__ == "__main__":
    main()
```

## 5.19 Source Selection and Supported Pricing Claims

\noindent A marketing team reviewing earnings calls wants to identify pricing decisions and the evidence about their consequences. Source selection affects the material available to an assistant. The team must also assess whether the resulting claims preserve speaker role, timing, and the scope of the evidence. A source can be accurately cited while supplying no basis for the conclusion attributed to it.

Consider four questions about a fictional retailer: what price change management reports, whether its effect on delivered units is identified, whether a discount has been announced, and whose subsequent service use is measured. Three synthetic records provide the evidence. S1 reports a five-percent list-price increase and an October unit count two percent below September, with no experiment or untreated comparison. S2 contains an analyst's unanswered question about next-quarter discounts, while S3 reports June use by 72 of 100 enrolled panel members who answered a May questionnaire. The answers therefore depend on what each record supplies: an attributed description, an unanswered question, or a selected denominator. The price comparison lacks the design needed to identify a causal effect, and panel use alone leaves consumer welfare unresolved.

A fourth document, S4, is a deliberately misleading secondary memo. It states that the price increase caused the unit decline and that management announced discounts. It supplies no additional evidence. A credible contradictory source would require substantive examination; disagreement alone does not make a source unsuitable. In this constructed case, the memo exceeds the evidence in S1 and converts the question in S2 into an action.

Hold the four questions fixed and compare three stipulated sets of answers: answers with S1–S3, answers after S4 is added, and answers after review restores S1–S3. Every answer cites a supplied document. The reference annotations classify all four initial answers as supported, two of the four answers with the memo as supported, and all four reviewed answers as supported. Citation presence is therefore four out of four in every condition, while supported claims are four, two, and four. These are authored responses, not observations from an AI system, and the differences estimate no causal effect of context.

![The same four fictional earnings-call questions have four cited answers in each of three stipulated conditions. Supported answers are four with curated sources, two with an added misleading memo, and four after review. Citation presence stays fixed while evidentiary support changes.](../figures/M05_source_selection.png)

[Stanford CS193T's source-management exercise](https://web.stanford.edu/class/archive/cs/cs193t/cs193t.1272/assignments/3-managing-sources/) motivates comparing answers before and after adding an unsuitable source. For a live comparison, preserve the questions, model version, settings, and scoring rule across fresh conversations. Randomize run order and repeat paired runs. Keep refusals and unscored answers in the record. Human reviewers should assess support against the same underlying evidence, with reasons for disagreements. The resulting estimate concerns this task and source intervention; broader claims require a wider task sample.

### 5.19.1 Reproduce the Source Comparison

\noindent The input file contains the complete fictional excerpts, questions, answers, citations, and reference reasons. The program verifies the paired question roster and that each cited source was available, then totals the supplied support annotations. It performs no automatic semantic judgment. One question-condition answer is the observation unit, and each condition has a denominator of four.

Python source: [source_selection.py](../../03_Data_and_Code/AI_Evidence_and_Evaluation/source_selection.py). From its folder, run `python3 source_selection.py`.

```python
"""Score hand-annotated synthetic answers; no model calls or automatic fact checking."""
from pathlib import Path
import csv
import json

HERE = Path(__file__).resolve().parent


def assess(data):
    sources = {row["id"] for row in data["sources"]}
    questions = {row["id"] for row in data["questions"]}
    if len(sources) != len(data["sources"]) or len(questions) != len(data["questions"]):
        raise ValueError("Source and question IDs must be unique")
    rows, summaries = [], []
    for condition, answers in data["answers"].items():
        if len(answers) != len(questions) or {a["question_id"] for a in answers} != questions:
            raise ValueError("Every condition must answer the same questions exactly once")
        available = set(data["conditions"][condition])
        if not available <= sources:
            raise ValueError("Unknown source in a condition")
        for answer in answers:
            cited = answer["citations"]
            if not set(cited) <= available:
                raise ValueError("Citation is absent from the supplied context")
            if type(answer["supported"]) is not bool:
                raise ValueError("Each claim needs an explicit reference annotation")
            rows.append(dict(condition=condition, question_id=answer["question_id"],
                cited=int(bool(cited)), supported=int(answer["supported"]),
                citations=";".join(cited), answer=answer["answer"], reason=answer["reason"]))
        sample = [r for r in rows if r["condition"] == condition]
        summaries.append(dict(condition=condition, answers=len(sample),
            cited=sum(r["cited"] for r in sample),
            supported=sum(r["supported"] for r in sample)))
    return rows, summaries


def main():
    data = json.loads((HERE / "data/source_cases.json").read_text())
    rows, summaries = assess(data)
    output = HERE / "results"
    output.mkdir(exist_ok=True)
    for name, records in [("source_claims.csv", rows), ("source_summary.csv", summaries)]:
        with (output / name).open("w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=list(records[0]))
            writer.writeheader()
            writer.writerows(records)
    print(json.dumps(dict(scope=data["scope"], summaries=summaries), indent=2))


if __name__ == "__main__":
    main()
```

## 5.20 Evaluate the Grader and Justify the Rubric

\noindent A team may use an AI grader to decide which generated pricing claims require correction. The reference rule must specify what constitutes an acceptable claim. A criterion based on accurate attribution differs from a criterion based on causal identification or customer welfare. Agreement with a reference judgment measures consistency with that judgment. Justifying the rule requires an additional argument about the decision and the interests it affects.

The synthetic practice set contains twelve statements: eight reference PASS cases and four reference FAIL cases. PASS statements preserve reported prices, the descriptive unit change, the analyst's role, the selected respondent denominator, the absence of an identifying comparison, the firm-specific scope, the absence of a welfare conclusion, or the conditional status of a proposed pilot. FAIL statements assert an identified price effect, infer customer benefit from higher prices, convert the analyst's question into a management decision, or generalize selected respondents to all customers. Every reference judgment has a written reason. A conditional proposal can pass this evidence rule while still requiring substantive ethical evaluation.

To give the two reference classes equal weight, calculate balanced accuracy as

$$
B=\frac{1}{2}\left(\frac{TP}{N_P}+\frac{TN}{N_F}\right).
$$

Here $N_P=8$ and $N_F=4$ are the numbers of reference PASS and FAIL statements. $TP$ counts correctly accepted PASS statements, and $TN$ counts correctly rejected FAIL statements. All twelve statements remain in their reference-class denominators, including abstentions, missing outputs, and invalid labels. This full-roster scoring convention penalizes an unscored case as lacking a correct decision. A separate coverage statistic reports the fraction receiving a valid binary decision.

| Grader | Correct PASS | Correct FAIL | False Passes | Review | Balanced Accuracy |
| --- | --- | --- | --- | --- | --- |
| Always Pass | 8/8 | 0/4 | 4 | 0 | 50.00% |
| Permissive | 7/8 | 3/4 | 1 | 0 | 81.25% |
| Cautious | 5/8 | 4/4 | 0 | 1 | 81.25% |

The permissive grader falsely rejects one acceptable statement and approves one unsupported welfare claim. The cautious grader falsely rejects two acceptable statements and abstains on a proposed pilot. Its valid-decision coverage is eleven out of twelve, compared with twelve out of twelve for the permissive grader. Both have balanced accuracy of 81.25 percent. The always-PASS baseline has ordinary accuracy of eight out of twelve but balanced accuracy of one-half, making the role of class composition explicit.

![On twelve synthetic statements, the permissive grader makes one false approval and one false rejection. The cautious grader makes no false approvals, two false rejections, and one referral. Both score 81.25 percent balanced accuracy. At imposed costs of ten, one, and one-half units, their total losses are eleven and two and one-half units.](../figures/M05_grader_costs.png)

Suppose a false approval costs ten loss units, a false rejection costs one, and a referral costs one-half. Referral includes perfect human resolution at the stated cost and requires sufficient review capacity. The permissive grader's loss is $10+1=11$ units; the cautious grader's loss is $2+0.5=2.5$ units. These losses are stipulated consequences on the same twelve-case batch. If false approval instead costs one and referral costs five, with false rejection still costing one, losses become two and seven. Equal balanced accuracy permits different decisions once the relevant consequences and review capacity are specified.

[Stanford CS193T's grader exercise](https://web.stanford.edu/class/archive/cs/cs193t/cs193t.1272/assignments/7-evals/) motivates constructing a judge and comparing it with a baseline on unseen cases. The twelve cases here are disclosed practice examples with stipulated grader decisions. Their scores provide no fresh evidence about an actual model. For a new evaluation, prepare independent reference judgments, resolve or report disagreements, freeze the rubric, and reserve new cases from prompt revision. Missing responses and parser failures must remain visible. A test of reference agreement cannot settle whether a rubric adequately protects customer agency.

### 5.20.1 Reproduce the Grader Comparison

\noindent The program joins every grader to the complete reference roster. Explicit abstentions, absent predictions, and invalid strings are counted separately and routed to review in the imposed loss calculation. Duplicate or unknown case IDs raise errors. Correctness conditional on a valid response is reported alongside full-roster metrics, preserving the distinction between selective coverage and performance on the full task.

Python source: [evaluate_graders.py](../../03_Data_and_Code/AI_Evidence_and_Evaluation/evaluate_graders.py). From its folder, run `python3 evaluate_graders.py`.

```python
"""Evaluate saved synthetic grader decisions on a fixed public practice set."""
from pathlib import Path
import argparse
import csv
import json

HERE = Path(__file__).resolve().parent


def evaluate(cases, predictions):
    reference = {row["id"]: row["reference"] for row in cases}
    if len(reference) != len(cases) or set(reference.values()) != {"PASS", "FAIL"}:
        raise ValueError("Unique IDs and both reference classes are required")
    graders = {}
    for row in predictions:
        if row["case_id"] not in reference or not row["grader"]:
            raise ValueError("Unknown case or empty grader name")
        saved = graders.setdefault(row["grader"], {})
        if row["case_id"] in saved:
            raise ValueError("Duplicate grader/case pair")
        saved[row["case_id"]] = row["prediction"]
    if not graders:
        raise ValueError("No graders supplied")
    results = []
    for name, saved in sorted(graders.items()):
        counts = dict(tp=0, tn=0, fp=0, fn=0, abstained=0, missing=0, invalid=0)
        for case_id, truth in reference.items():
            pred = saved.get(case_id)
            if pred is None:
                counts["missing"] += 1
            elif pred == "ABSTAIN":
                counts["abstained"] += 1
            elif pred not in {"PASS", "FAIL"}:
                counts["invalid"] += 1
            else:
                key = {("PASS", "PASS"): "tp", ("FAIL", "FAIL"): "tn",
                       ("FAIL", "PASS"): "fp", ("PASS", "FAIL"): "fn"}[truth, pred]
                counts[key] += 1
        n_pass = sum(v == "PASS" for v in reference.values())
        n_fail = len(reference) - n_pass
        tp, tn, fp, fn = (counts[k] for k in ("tp", "tn", "fp", "fn"))
        answered = tp + tn + fp + fn
        reviewed = counts["abstained"] + counts["missing"] + counts["invalid"]
        # Unscored cases remain in their reference-class denominator.
        balanced = .5 * (tp / n_pass + tn / n_fail)
        results.append(dict(grader=name, cases=len(reference), reference_pass=n_pass,
            reference_fail=n_fail, **counts, answered=answered,
            coverage=answered / len(reference), accuracy_all=(tp + tn) / len(reference),
            balanced_accuracy_all=balanced, false_pass_rate=fp / n_fail,
            accuracy_answered=(tp + tn) / answered if answered else None,
            review_cases=reviewed,
            # Imposed loss units: false approval 10, false rejection 1,
            # referral .5 with perfect resolution by the human reviewer.
            loss_units=10 * fp + fn + .5 * reviewed))
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--predictions", type=Path, default=HERE / "data/grader_predictions.csv")
    parser.add_argument("--output", type=Path, default=HERE / "results")
    args = parser.parse_args()
    cases = json.loads((HERE / "data/grader_cases.json").read_text())["cases"]
    with args.predictions.open(newline="") as file:
        predictions = list(csv.DictReader(file))
    results = evaluate(cases, predictions)
    args.output.mkdir(parents=True, exist_ok=True)
    with (args.output / "grader_summary.csv").open("w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=list(results[0]))
        writer.writeheader()
        writer.writerows(results)
    (args.output / "grader_summary.json").write_text(json.dumps(results, indent=2) + "\n")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
```

## 5.21 Retail Alternatives and Network Accessibility

\noindent A retail chain with a limited service budget must decide which unavailable outlet to restore. Counting available stores gives each location equal weight. Customers' alternatives also depend on where people live, how locations connect, and which outlets can be reached within an acceptable journey. A restoration beside several available alternatives can change the store count while leaving the number of people with a nearby option unchanged.

For an origin $i$ and store $j$, define $d_{ij}$ as the shortest sum of edge travel times along a permitted path. A disconnected pair has $d_{ij}=\infty$. Given a travel threshold $\tau$, availability states $a_j$, and fixed population weights $w_i$, the share with at least one available option is

$$
C(a,\tau)=\frac{\sum_i w_i\,\mathbf{1}\{\min_{j:a_j=1}d_{ij}\leq\tau\}}{\sum_i w_i}.
$$

The minimum over an empty set is infinity. Each person contributes once even if several stores are reachable. The denominator includes origins with no reachable store. Travel times, the store menu, and population weights define the measured comparison; the calculation does not specify which store a customer prefers or chooses.

In the synthetic network below, two banks connect only at the northern crossing. Vertical edges take four minutes and the crossing takes two. The fixed population totals 800, including 150 at disconnected origin X. Stores B and C are available, A and D are unavailable, and U's status is unknown. Origin populations are W0: 100, W1: 300, W2: 100, E0: 50, E1: 50, E2: 50, and X: 150. Store locations coincide with W0, E0, W2, E2, and X, respectively. The threshold is five minutes.

![A synthetic river crossing separates geographic proximity from network access; X remains in the population despite its disconnected location.](../figures/M05_access_network.png)

The network layout is schematic. The code fixes map coordinates at W0 $(0,0)$, W1 $(0,2)$, W2 $(0,4)$, E0 $(1,0)$, E1 $(1,2)$, E2 $(1,4)$, and X $(4,0)$. A straight-line proxy assigns two minutes per map unit. It places B two minutes from W0. The network route takes eighteen minutes, and W0's nearest known available store is C at eight minutes. Holding the population and five-minute threshold fixed, the straight-line proxy counts 650 people with access, compared with 550 under network travel times.

Unknown availability gives bounds on access. The lower bound includes stores known to be available; the upper bound additionally treats every unknown store as available. Network access is therefore between $550/800=68.75\%$ and $700/800=87.50\%$. The range reflects U's missing status, conditional on the fixed network and population. It is not a sampling confidence interval. Removing X would change the target population and raise the apparent lower share to $550/650=84.62\%$.

A separate neighbor comparison uses only the six bank locations and retains one directed neighbor per origin. Stable alphabetical ordering resolves ties. The straight-line and network graphs each contain six directed links, with two in common. Evaluated using the same network travel times, the selected neighbor averages ten minutes away under straight-line selection and $10/3$ minutes under network selection. Increasing the neighbor count changes another modeling choice. Holding it fixed isolates the effect of the distance definition. Symmetrizing selected links can also change node degrees. A constructed proximity link records the analyst's criterion; customer substitution requires evidence about behavior.

The program writes origin-level bounds, service-restoration comparisons, and directed-neighbor tables. The hypothetical profit increments used in Section 8.23 are twenty dollars for restoring A and forty dollars for restoring D, with equal restoration costs. They are imposed independently of the travel calculations.


Python source: [accessibility.py](../../03_Data_and_Code/Retail_Accessibility/accessibility.py)

```python
"""Synthetic service restoration, accessibility bounds, and graph comparisons."""
from pathlib import Path
import csv
import json
import math
import networkx as nx

HERE = Path(__file__).resolve().parent
POSITIONS = {"W0": (0, 0), "W1": (0, 2), "W2": (0, 4),
             "E0": (1, 0), "E1": (1, 2), "E2": (1, 4), "X": (4, 0)}
PEOPLE = {"W0": 100, "W1": 300, "W2": 100, "E0": 50,
          "E1": 50, "E2": 50, "X": 150}
STORES = {"A": "W0", "B": "E0", "C": "W2", "D": "E2", "U": "X"}
STATUS = {"A": 0, "B": 1, "C": 1, "D": 0, "U": None}
PROFIT = {"A": 20, "D": 40}  # Imposed incremental weekly dollars, equal costs.


def write_csv(path, rows):
    with Path(path).open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]),
                                lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def graph():
    g = nx.Graph()
    g.add_nodes_from(POSITIONS)
    g.add_weighted_edges_from([("W0", "W1", 4), ("W1", "W2", 4),
                               ("E0", "E1", 4), ("E1", "E2", 4),
                               ("W2", "E2", 2)], weight="minutes")
    return g


def distances(g, metric="network"):
    if metric not in {"network", "straight"}:
        raise ValueError("Use network or straight distance")
    paths = dict(nx.all_pairs_dijkstra_path_length(g, weight="minutes"))
    return {(a, b): (paths[a].get(b, math.inf) if metric == "network"
                     else 2 * math.dist(POSITIONS[a], POSITIONS[b]))
            for a in POSITIONS for b in POSITIONS}


def access_rows(distance, status, threshold=5):
    if any(s not in (0, 1, None) for s in status.values()):
        raise ValueError("Availability must be 0, 1, or None")
    rows = []
    for origin, people in PEOPLE.items():
        certain = [distance[origin, STORES[s]] for s, v in status.items() if v == 1]
        possible = [distance[origin, STORES[s]] for s, v in status.items() if v != 0]
        best = min(certain, default=math.inf)
        rows.append(dict(origin=origin, people=people,
                         known_minutes=best if math.isfinite(best) else None,
                         lower=int(best <= threshold),
                         upper=int(min(possible, default=math.inf) <= threshold)))
    return rows


def summarize(rows):
    denominator = sum(r["people"] for r in rows)
    return {"people": denominator,
            "lower_people": sum(r["people"] * r["lower"] for r in rows),
            "upper_people": sum(r["people"] * r["upper"] for r in rows)}


def nearest_edges(distance, nodes, k):
    if not 0 < k < len(nodes):
        raise ValueError("k must be between 1 and n-1")
    return {(a, b) for a in nodes for b in
            sorted((b for b in nodes if b != a), key=lambda b: (distance[a, b], b))[:k]
            if math.isfinite(distance[a, b])}


def main(output=HERE / "results"):
    output = Path(output); output.mkdir(parents=True, exist_ok=True)
    g = graph(); net = distances(g); straight = distances(g, "straight")
    origins, policies = [], []
    for policy in ["Baseline", "Restore A", "Restore D"]:
        status = STATUS.copy()
        if policy != "Baseline":
            status[policy[-1]] = 1
        rows = access_rows(net, status)
        origins.extend(dict(policy=policy, **r) for r in rows)
        result = summarize(rows)
        result["lower_share"] = result["lower_people"] / result["people"]
        result["upper_share"] = result["upper_people"] / result["people"]
        result["profit_gain"] = PROFIT.get(policy[-1], 0)
        result["known_unavailable_share"] = sum(v == 0 for v in status.values()) / sum(v is not None for v in status.values())
        policies.append(dict(policy=policy, **result))
    banks = sorted(n for n in POSITIONS if n != "X")
    edge_rows, comparisons = [], []
    for k in [1, 2]:
        edges = {m: nearest_edges(d, banks, k)
                 for m, d in [("straight", straight), ("network", net)]}
        for metric, pairs in edges.items():
            edge_rows.extend(dict(k=k, metric=metric, origin=a, target=b,
                                  network_minutes=net[a, b]) for a, b in sorted(pairs))
        comparisons.append(dict(k=k, directed_edges=len(edges["network"]),
                                common_edges=len(edges["network"] & edges["straight"]),
                                straight_neighbors_network_minutes=sum(net[e] for e in edges["straight"]) / len(edges["straight"]),
                                network_neighbors_network_minutes=sum(net[e] for e in edges["network"]) / len(edges["network"])))
    write_csv(output / "synthetic_origins.csv", origins)
    write_csv(output / "policies.csv", policies)
    write_csv(output / "neighbors.csv", edge_rows)
    write_csv(output / "neighbor_comparison.csv", comparisons)
    result = {"synthetic": True, "threshold_minutes": 5, "known_store_unavailability": 0.5,
              "unknown_store_records": 1, "network_baseline": summarize(access_rows(net, STATUS)),
              "straight_baseline": summarize(access_rows(straight, STATUS)),
              "policies": policies, "neighbor_comparison": comparisons}
    (output / "synthetic_summary.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=HERE / "results")
    main(parser.parse_args().output)
```

## 5.22 Restaurant Availability and a Changed Nearest Alternative

\noindent A service manager assessing an unavailable ice-cream option needs to distinguish a nearby restaurant from a reachable alternative. The supplied October 24, 2026 snapshot contains four observed restaurant records inside latitudes 40.06 to 40.16 and longitudes -88.33 to -88.17 around Champaign-Urbana. North Neil is recorded unavailable; the other three are recorded available. The outcome concerns order availability. It does not identify mechanical failure or a reason for unavailability.

Each observed restaurant location is an equally weighted origin. Candidate destinations are the other recorded available restaurants in the selected box. The origin restaurant is excluded even when its status is available, so the quantity measures access to an alternative. No population or customer-demand weights are inferred from these four origins. The frozen [input record](../../03_Data_and_Code/Retail_Accessibility/data/manifest.json) retains the archive commit, source hashes, selected records, and street-extract date.

The network uses OpenStreetMap highway ways from a separate working box that contains the four selected origins. Edge lengths are spherical geographical distances in kilometers, and selected links are treated as undirected. The code excludes specified road classes, explicitly prohibited foot access, and private access without an explicit allowed foot tag. Every origin connects to its nearest selected network node by a straight segment; these connectors range from 11.34 to 20.64 meters and contribute to path length. All four snapped origins lie in the same connected component. Directional restrictions, crossing delays, entrance access, and the feasibility of the straight connectors are unverified. The resulting distances describe the selected network and connector assumptions. Practical pedestrian routing also requires the unverified access and crossing information.

The street extract is dated November 18, 2026, after the observed availability snapshot. Results hold that later network fixed and do not reconstruct historical street conditions. Restaurants outside the selection box are excluded. Enlarging the candidate menu or changing the network can alter the nearest alternative.

| Origin | Straight-Line Alternative (km) | Network Alternative (km) |
| --- | --- | --- |
| South Neil | Mattis, 3.751 | Mattis, 5.021 |
| North Neil | Mattis, 3.478 | South Neil, 4.757 |
| Mattis | South Neil, 3.751 | South Neil, 5.021 |
| Cunningham | South Neil, 4.161 | South Neil, 5.499 |

North Neil's selected alternative changes from Mattis to South Neil when the metric changes. At an imposed four-kilometer threshold, three of the four origins have an available alternative under straight-line distance and none do on the modeled network. This comparison concerns four restaurant origins and the fixed candidate set. It supplies neither a population-access rate nor an estimate of diverted sales.

![Distances to an available same-chain alternative increase on the modeled network, and North Neil's selected destination changes.](../figures/M05_restaurant_distances.png)

Source: Rashiq Zahid's McBroken observations through the supplied archive extraction; OpenStreetMap contributors, [ODbL 1.0](https://opendatacommons.org/licenses/odbl/1-0/). The complete calculation below uses frozen local inputs. Independent Bellman-Ford calculations agree with the twelve origin-destination distances computed by Dijkstra's algorithm.


Python source: [snapshot_access.py](../../03_Data_and_Code/Retail_Accessibility/snapshot_access.py)

```python
"""Frozen restaurant statuses and a later illustrative OSM network; distances in km."""
from pathlib import Path
import csv
import gzip
import json
import math
import networkx as nx
from accessibility import write_csv

HERE = Path(__file__).resolve().parent
ALLOWED = {"residential", "living_street", "pedestrian", "footway", "path", "steps",
           "service", "unclassified", "tertiary", "tertiary_link", "secondary",
           "secondary_link", "primary", "primary_link"}


def haversine(a, b):
    lat1, lon1, lat2, lon2 = map(math.radians, (*a, *b))
    h = math.sin((lat2-lat1)/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin((lon2-lon1)/2)**2
    return 6371.0088 * 2 * math.asin(math.sqrt(min(1, h)))


def build_network(data):
    elements = data["elements"]
    coordinates = {e["id"]: (e["lat"], e["lon"]) for e in elements if e["type"] == "node"}
    g = nx.Graph()
    for way in (e for e in elements if e["type"] == "way"):
        tags = way.get("tags", {})
        if tags.get("highway") not in ALLOWED or tags.get("area") == "yes":
            continue
        if tags.get("foot") in {"no", "private"}:
            continue
        if tags.get("access") in {"no", "private"} and tags.get("foot") not in {"yes", "designated", "permissive"}:
            continue
        # Undirected connectivity is an imposed convention, not verified pedestrian routing.
        for a, b in zip(way["nodes"], way["nodes"][1:]):
            if a not in coordinates or b not in coordinates or a == b:
                continue
            pa, pb = coordinates[a], coordinates[b]
            if not all(40.08 <= p[0] <= 40.155 and -88.30 <= p[1] <= -88.185 for p in [pa, pb]):
                continue
            km = haversine(pa, pb)
            if km > 0 and (not g.has_edge(a, b) or km < g[a][b]["km"]):
                g.add_edge(a, b, km=km, osm_way=way["id"])
    nx.set_node_attributes(g, {n: coordinates[n] for n in g}, "latlon")
    return g


def main(output=HERE / "results"):
    output = Path(output); output.mkdir(parents=True, exist_ok=True)
    with gzip.open(HERE / "data/osm_highways.json.gz", "rt") as f:
        osm = json.load(f)
    g = build_network(osm)
    stores = list(csv.DictReader((HERE / "data/restaurants.csv").open()))
    assert len({s["store_key"] for s in stores}) == len(stores)
    snaps = {}
    for s in stores:
        p = (float(s["lat"]), float(s["lon"]))
        node = min(g, key=lambda n: (haversine(p, g.nodes[n]["latlon"]), n))
        km = haversine(p, g.nodes[node]["latlon"])
        if km > 0.2:
            raise ValueError("Origin farther than 200 m from selected graph")
        snaps[s["store_key"]] = (node, km, p)
    pairs = []
    for a in stores:
        node, connector, p = snaps[a["store_key"]]
        lengths = nx.single_source_dijkstra_path_length(g, node, weight="km")
        for b in stores:
            if a["store_key"] == b["store_key"]:
                continue  # Alternatives always exclude the origin restaurant.
            dest, end_connector, q = snaps[b["store_key"]]
            route = lengths.get(dest, math.inf) + connector + end_connector
            pairs.append(dict(origin=a["store_key"], target=b["store_key"],
                              target_available=int(b["available"]), straight_km=haversine(p, q),
                              network_km=route if math.isfinite(route) else None))
    rows = []
    for s in stores:
        eligible = [p for p in pairs if p["origin"] == s["store_key"] and p["target_available"] == 1]
        row = dict(store_key=s["store_key"], street=s["street"], available=int(s["available"]),
                   snapped_node=snaps[s["store_key"]][0],
                   snap_m=1000*snaps[s["store_key"]][1],
                   candidate_alternatives=len(eligible))
        for metric in ["straight", "network"]:
            valid = [p for p in eligible if p[metric+"_km"] is not None]
            best = min(valid, key=lambda p: (p[metric+"_km"], p["target"]), default=None)
            row[metric+"_target"] = best["target"] if best else None
            row[metric+"_km"] = best[metric+"_km"] if best else None
        rows.append(row)
    summary = {"synthetic": False, "observed_status_date": "2026-10-24",
               "network_osm_base": osm["osm3s"]["timestamp_osm_base"],
               "origin_denominator": len(stores), "unavailable": sum(1-int(s["available"]) for s in stores),
               "network_nodes": g.number_of_nodes(), "network_edges": g.number_of_edges(),
               "components": nx.number_connected_components(g),
               "snapped_components": [len(nx.node_connected_component(g, snaps[s["store_key"]][0])) for s in stores],
               "within_4km": {m: sum(r[m+"_km"] is not None and r[m+"_km"] <= 4 for r in rows) for m in ["straight", "network"]},
               "scope": "Four observed restaurant origins; same-chain alternatives in fixed box; later undirected network and straight snapping connectors are imposed."}
    write_csv(output / "observed_pairs.csv", pairs)
    write_csv(output / "observed_origins.csv", rows)
    (output / "observed_summary.json").write_text(json.dumps(summary, indent=2)+"\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=HERE / "results")
    main(parser.parse_args().output)
```

## 5.23 Text, Anchors, and Purchase-Intent Ratings

\noindent A product manager reading a conditional response must decide how it enters a numerical comparison. “I would consider it if the refill is convenient and the total price is acceptable” expresses interest while leaving conditions unresolved. Assigning a single rating removes some of that ambiguity. Assigning weights across categories retains a broader representation, whose interpretation depends on how those weights are constructed.

The [semantic similarity rating method](https://arxiv.org/abs/2510.08338v3) compares the embedding of a written response with embeddings of five reference statements, one for each purchase-intent category. The study averages results across six reference sets. Its Python package accepts response text or supplied embeddings; generation of the consumer responses is a separate operation. The paper uses `text-embedding-3-small`, while the inspected package's automatic text mode defaults to `all-MiniLM-L6-v2`. Changing that component changes the measurement procedure and requires renewed validation.

### 5.23.1 A Fixed Response Under Different Anchors

\noindent Let $s_{car}$ be the cosine similarity between response $c$ and category $r$ in anchor set $a$. At zero epsilon and temperature one, the study's mapping is

$$
p_{car}=\frac{s_{car}-\min_j s_{caj}}{\sum_{k=1}^{5}(s_{cak}-\min_j s_{caj})}.
$$

The numerator measures similarity above the least similar reference statement. The denominator normalizes the five nonnegative values when at least two similarities differ. The weights sum to one, and the expected rating is $\sum_{r=1}^{5} r p_{car}$. These are weights assigned by a text measurement rule. Their calibration against actual consumer ratings or purchasing requires independent outcomes.

Two instructor-authored sets use the following category descriptions. The response above remains fixed. The similarities are imposed numerical inputs, chosen to expose the calculation; they were not estimated from the text or an embedding model.

| Category | Set 1 | Set 2 |
| --- | --- | --- |
| 1 | Would not buy | Certain I will not buy |
| 2 | Probably would not buy | Unlikely to buy |
| 3 | Might or might not buy | Undecided about buying |
| 4 | Would probably buy | Expect to buy |
| 5 | Would buy | Certain I will buy |

Set 1 has similarities $(0.20,0.23,0.29,0.38,0.50)$. Subtracting 0.20 gives a total difference of 0.60 and weights $(0,0.05,0.15,0.30,0.50)$. Set 2 has similarities $(0.20,0.26,0.38,0.44,0.32)$ and weights $(0,0.10,0.30,0.40,0.20)$. The resulting mean moves from 4.25 to 3.70. The share assigned to categories 4 and 5 moves from 0.80 to 0.60. The example establishes sensitivity to the supplied mapping inputs; it does not estimate the effect of these particular words on a language model.

![For one fixed instructor-authored response, imposed similarities produce category weights of 0, 5, 15, 30, and 50 percent under Set 1 and 0, 10, 30, 40, and 20 percent under Set 2.](../figures/M05_anchor_ratings.png)

Subtracting the minimum forces at least one category weight to zero within each set. Equal similarities make normalization undefined. The course implementation explicitly abstains when the similarity spread is at most $10^{-12}$ and records an incomplete aggregate if any required mapping is unavailable. That tolerance is a numerical convention. It supplies no evidence that a consumer is indifferent. An alternative rule, such as assigning uniform weights, would require its own stated interpretation and sensitivity analysis.

### 5.23.2 Responses, Personas, and the Concept Mean

\noindent The supplied text example has three fictional body-wash concepts and two invented personas, with seven response rows in total. One persona's refill response appears twice with identical inputs. Averaging those rows directly would give that persona twice the weight of the other persona for that concept. Equal-persona aggregation first averages repeat responses within each persona and then averages the two persona distributions. The duplicated response adds no new information in this construction.

For the refill concept under Set 1, the two persona means are 4.25 and 3.70. Equal-persona weighting gives 3.975. Treating the repeated rows as separate people gives $(2\times4.25+3.70)/3=4.067$. The denominator therefore changes the apparent attractiveness of a concept even though the represented people and their responses remain fixed.

| Concept | Set 1 Mean | Set 2 Mean | Mean Across Sets |
| --- | ---: | ---: | ---: |
| Refillable | 3.975 | 3.625 | 3.800 |
| Fragrance-Free | 3.850 | 4.100 | 3.975 |
| Compact Travel | 3.425 | 3.300 | 3.363 |

Equal-persona weighting and the same response roster apply throughout the table. Set 1 selects the refillable concept; Set 2 and the average across sets select fragrance-free. Averaging anchors makes the choice less dependent on selecting one particular set, while the interpretation still depends on which sets enter the average. Repeated generation, variation across personas, and uncertainty about a target population remain distinct sources of variation. A large number of generated answers can estimate a model's response distribution precisely while leaving its difference from human preferences unresolved.

### 5.23.3 Complete Python Measurement

\noindent The input file preserves the full anchor sentences, response text, concept identifiers, persona identifiers, repeat numbers, and imposed similarities. The program rejects duplicate keys and incomplete concept/persona coverage, records uninformative mappings, and preserves equal-persona aggregation. The original calculation uses no downloaded package, model weights, or paid API. A live extension would replace the imposed similarities with versioned embedding outputs and evaluate the complete procedure using appropriately sampled human outcomes.

Python source: [anchor_measurement.py](../../03_Data_and_Code/Synthetic_Consumers/anchor_measurement.py). From its directory, run `python3 anchor_measurement.py`. Inputs are in the accompanying `data` folder; outputs are written to `results`.

```python
"""Map imposed similarities to ratings while preserving response and persona units.

Inputs are instructor-authored text and synthetic similarities, not LLM measurements.
Python 3.10+; standard library only; no network or model calls.
"""
from collections import defaultdict
import json
from math import isfinite
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parent


def rating_distribution(similarities, tolerance=1e-12):
    """Study setting: subtract minimum, normalize, epsilon=0, temperature=1.

    Return None when the spread is at most tolerance. This explicit abstention
    rule is a course adaptation for an otherwise undefined normalization.
    """
    if len(similarities) != 5 or any(
        not isinstance(x, (int, float)) or not isfinite(x) or not -1 <= x <= 1
        for x in similarities
    ):
        raise ValueError("Five finite cosine similarities in [-1, 1] are required.")
    if not isfinite(tolerance) or tolerance < 0:
        raise ValueError("Tolerance must be finite and nonnegative.")
    smallest = min(similarities)
    if max(similarities) - smallest <= tolerance:
        return None
    weights = [x - smallest for x in similarities]
    return [x / sum(weights) for x in weights]


def average_distributions(distributions):
    """A missing mapping leaves the aggregate incomplete, with no silent exclusion."""
    if not distributions or any(row is None for row in distributions):
        return None
    return [mean(row[k] for row in distributions) for k in range(5)]


def mean_rating(distribution):
    return None if distribution is None else sum(
        (k + 1) * p for k, p in enumerate(distribution)
    )


def score_responses(data):
    concepts, personas = set(data["concepts"]), set(data["personas"])
    anchors = set(data["anchor_sets"])
    if len(anchors) != 2 or any(len(s) != 5 for s in data["anchor_sets"].values()):
        raise ValueError("This example has two complete five-category anchor sets.")
    records, seen, covered = [], set(), set()
    for row in data["responses"]:
        key = (row["concept"], row["persona"], row["repeat"])
        if key in seen or key[0] not in concepts or key[1] not in personas:
            raise ValueError("Duplicate response key or unknown concept/persona.")
        if set(row["similarities"]) != anchors or not row["text"].strip():
            raise ValueError("Each response needs text and both anchor comparisons.")
        seen.add(key)
        covered.add(key[:2])
        distributions = {a: rating_distribution(row["similarities"][a])
                         for a in sorted(anchors)}
        distributions["average_sets"] = average_distributions(list(distributions.values()))
        for anchor, distribution in distributions.items():
            records.append(dict(concept=key[0], persona=key[1], repeat=key[2],
                                anchor_set=anchor, distribution=distribution,
                                mean_rating=mean_rating(distribution),
                                status="scored" if distribution is not None else "uninformative"))
    if covered != {(c, p) for c in concepts for p in personas}:
        raise ValueError("Every declared concept/persona pair needs a response.")
    return records


def summarize(records):
    grouped = defaultdict(list)
    for row in records:
        grouped[row["concept"], row["anchor_set"]].append(row)
    summaries = []
    for (concept, anchor), group in sorted(grouped.items()):
        by_persona = defaultdict(list)
        for row in group:
            by_persona[row["persona"]].append(row["distribution"])
        # Average repeats within persona, then give each persona equal weight.
        persona_pmfs = [average_distributions(rows) for rows in by_persona.values()]
        balanced = average_distributions(persona_pmfs)
        row_weighted = average_distributions([row["distribution"] for row in group])
        summaries.append(dict(concept=concept, anchor_set=anchor,
            response_rows=len(group), scored_rows=sum(r["status"] == "scored" for r in group),
            personas=len(by_persona), distribution=balanced,
            mean_rating=mean_rating(balanced),
            top_two_share=None if balanced is None else sum(balanced[3:]),
            row_weighted_mean=mean_rating(row_weighted),
            status="complete" if balanced is not None else "incomplete"))
    return summaries


def main():
    data = json.loads((ROOT / "data/anchor_responses.json").read_text())
    records = score_responses(data)
    summaries = summarize(records)
    out = ROOT / "results"
    out.mkdir(exist_ok=True)
    for name, value in [("response_ratings.json", records), ("concept_ratings.json", summaries)]:
        (out / name).write_text(json.dumps(value, indent=2, allow_nan=False) + "\n")
    for row in summaries:
        print(row["concept"], row["anchor_set"], row["mean_rating"], row["status"])


if __name__ == "__main__":
    main()
```

\Needspace{12\baselineskip}

## 5.24 Compressing a Network and Preserving Customer Access

\noindent A retail chain may group nearby service zones to reduce the cost of storing and analyzing its network. The manager still needs a revenue summary and the share of customers who can reach an available outlet within five minutes. Compression can preserve the first quantity while changing the second. The relevant evaluation therefore begins with the original customers, their locations, and the decision the smaller graph is intended to support.

The GraCo implementation [(Joly, 2026)](https://github.com/Antonin-J/graco) provides a common interface to 17 graph-coarsening methods and a random baseline. Its [working paper](https://arxiv.org/abs/2611.01200v1) compares graph and feature criteria under explicit operator conventions. These criteria identify properties of a representation. Customer access additionally requires a travel interpretation, the original population weights, and an assessment of routes that disappear when nodes are grouped.

### 5.24.1 Group Means, Group Sizes, and Graph Weights

\noindent Let $N$ original nodes be assigned to $n$ nonempty groups. The binary membership matrix $Q_b$ has $N$ rows and $n$ columns; its entry is one when a node belongs to the indicated group. Let $A$ be a symmetric weighted adjacency matrix with no self-loops. Summing weights between groups gives the coarse adjacency

$$
A_c=Q_b^\top A Q_b,
$$

with its diagonal removed. An off-diagonal entry adds all original edge weights between the corresponding groups. This aggregation preserves the units of those weights. Summing travel times across parallel roads, for example, would require a different justification from summing referral counts.

For a node feature $x$, use binary lifting and the group-average reduction

$$
P=(Q_b^\top Q_b)^{-1}Q_b^\top,\qquad x_c=Px,\qquad \widehat x=Q_bx_c.
$$

The diagonal entries of $Q_b^\top Q_b$ are group sizes. Dividing each group's sum by its size produces $x_c$; lifting assigns that mean to each original member. A mean across original nodes weights each group mean by its membership count. A total multiplies each mean by that count before summing. Other population weights require an aggregation rule consistent with the intended population.

These equations use the combinatorial convention. GraCo's default `normalized_self_loop` uses degree-normalized lifting, whose pseudoinverse generally differs from simple averaging. Selecting `laplacian_kind="combinatorial"` makes the binary-lifting interpretation explicit. The [pinned construction and normalization code](../../01_Resources/32_Graph_Coarsening/SOURCE_REVIEW.md) records this distinction. An AI-generated call that runs with defaults can implement a different estimand from the one described in the prompt.

### 5.24.2 Exact Revenue Reconstruction and Distorted Travel

\noindent Consider four synthetic zones along the path A-B-C-D, each with 100 people and an available store at D. Travel along the three edges takes four, one, and four minutes, respectively. Set weekly zone revenues to 10, 10, 10, and 40 dollars, measured as totals for each zone. These travel times and revenues allow the same grouping to be evaluated for both access and revenue reconstruction.

Group A, B, and C together and retain D separately. The group sizes are three and one, and their mean zone revenues are 10 and 40 dollars. Reconstructing the four original revenue values produces zero error. Giving each group equal weight produces a mean of 25 dollars, while weighting by its original zone count gives $(3\times10+1\times40)/4=17.50$ dollars per zone. Total weekly revenue is 70 dollars. Adding the two means would give 50 dollars and discard the meaning of the original total.

For this graph calculation, define edge affinity as the reciprocal of travel minutes. The affinities are $1/4$, $1$, and $1/4$ per minute. The coarse graph retains an affinity of $1/4$ between the two groups. Its internal edges are removed. To measure variation in the revenue feature across connected zones, use the combinatorial Dirichlet energy

$$
x^\top Lx=\sum_{\{i,j\}\in E} A_{ij}(x_i-x_j)^2,
$$

where $L$ is the degree matrix minus $A$ and each undirected edge appears once in the sum. The units here are dollars squared per minute for the weekly revenue feature. Revenues are equal along A-B and B-C, so those edges contribute zero. The C-D edge contributes $(1/4)(10-40)^2=225$. The coarse feature has exactly the same energy. This equality concerns the chosen feature and quadratic form; it supplies no guarantee for every graph property.

| Original Zone | Revenue (Dollars) | Travel to D (Minutes) | Naive Coarse Travel (Minutes) |
|---|---:|---:|---:|
| A | 10 | 9 | 4 |
| B | 10 | 5 | 4 |
| C | 10 | 4 | 4 |
| D | 40 | 0 | 0 |

A manager who interprets the reciprocal coarse affinity as a four-minute trip assigns the same travel time to A, B, and C. That operation removes travel within the merged group. A's actual trip takes nine minutes. At the five-minute threshold, B, C, and D provide access for 300 of the 400 people, or 75%. The naive compressed calculation reports access for all 400 people. Both revenue reconstruction and its graph energy remain exact while the access comparison changes.

![Four equal-population zones have revenues 10, 10, 10, and 40 dollars and edge travel times 4, 1, and 4 minutes. Merging A, B, and C preserves the revenue feature and energy of 225, but reciprocal coarse-edge travel omits internal trips and raises apparent five-minute access from 75% to 100%.](../figures/M05_graph_coarsening.png)

A service decision needs access evaluated at the original origins, or a compression method with a verified approximation guarantee for that particular route quantity. A smaller representation may still serve revenue accounting. Using it for travel requires evidence about which internal distances it preserves and how approximation error affects customers near the access threshold.

### 5.24.3 Preprocessing and the Population Receiving Weight

\noindent GraCo's pinned preprocessing function defaults to symmetrizing edges, removing self-loops, and retaining the largest connected component. Weighted reciprocal edges are averaged during symmetrization. Those operations support particular mathematical procedures. Their economic meaning depends on whether the edges represent travel, referrals, purchases, or another relationship. A directed referral from one customer to another becomes a different object when combined with the reverse direction.

The separate retail case in Section 5.21 contains 800 people, including 150 at a disconnected origin. Known five-minute access covers 550 people. Retaining only the largest connected component removes those 150 people from the denominator and raises the reported share from $550/800=68.75\%$ to $550/650=84.62\%$. No person's access improves. The original calculation retains the disconnected origin and its unknown store status, producing the stated lower and upper access bounds. Its complete Python program appears in Section 5.21.

Preserve an accounting table of original nodes, retained nodes, population weights, and exclusion reasons. Component-wise analysis can retain disconnected customers when the chosen algorithm supports it. An algorithm that requires connectivity needs a separate treatment of excluded components in the decision calculation. Changing a default without checking the method's assumptions does not resolve that requirement.

### 5.24.4 Python Aggregation and Access Calculations

\noindent The [synthetic inputs](../../03_Data_and_Code/Graph_Coarsening/data/cases.json) contain the four zone names, population weights, weekly revenues, group assignments, edge minutes, store location, and threshold. The program constructs the binary matrices, compares original and reconstructed features, calculates both energies, and runs shortest-path calculations. It writes one row per original zone and an aggregate JSON result. The naive coarse route is retained as an explicitly labeled incorrect interpretation for this decision.

```bash
python3 03_Data_and_Code/Graph_Coarsening/compress_network.py
```

Python source: [compress_network.py](../../03_Data_and_Code/Graph_Coarsening/compress_network.py)

```python
"""Exact aggregation and travel calculations for four synthetic retail zones.

Run with Python 3.10+; standard library only. Paths are relative to this file.
Binary membership and combinatorial affinities are chosen explicitly.
"""
from fractions import Fraction as F
from pathlib import Path
import csv
import json
import math

HERE = Path(__file__).resolve().parent


def multiply(a, b):
    return [[sum(x * y for x, y in zip(row, col))
             for col in zip(*b)] for row in a]


def transpose(a):
    return list(map(list, zip(*a)))


def distances(n, edges):
    d = [[0 if i == j else math.inf for j in range(n)] for i in range(n)]
    for i, j, minutes in edges:
        assert minutes > 0 and i != j
        d[i][j] = d[j][i] = min(d[i][j], minutes)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d


def calculate(case):
    names, group = case["zones"], case["group"]
    people = case["population"]
    x = [[F(v)] for v in case["weekly_zone_revenue_dollars"]]
    n, g = len(names), max(group) + 1
    assert len(group) == len(x) == len(people) == n
    assert set(group) == set(range(g)) and all(p > 0 for p in people)
    sizes = [group.count(c) for c in range(g)]
    q = [[int(c == group[i]) for c in range(g)] for i in range(n)]
    p = [[F(q[i][c], sizes[c]) for i in range(n)] for c in range(g)]
    means = multiply(p, x)
    reconstructed = multiply(q, means)
    a = [[F(0) for _ in range(n)] for _ in range(n)]
    for i, j, minutes in case["edges_minutes"]:
        a[i][j] = a[j][i] = F(1, minutes)
    coarse = multiply(multiply(transpose(q), a), q)
    for c in range(g):
        coarse[c][c] = F(0)
    coarse_edges = [(c, d, 1 / coarse[c][d]) for c in range(g)
                    for d in range(c + 1, g) if coarse[c][d] > 0]
    fine_d = distances(n, case["edges_minutes"])
    naive_d = distances(g, coarse_edges)
    store, threshold = case["store_node"], case["access_threshold_minutes"]
    rows = []
    for i, name in enumerate(names):
        fine, naive = fine_d[i][store], naive_d[group[i]][group[store]]
        rows.append(dict(zone=name, people=people[i], group=group[i],
                         revenue_dollars=float(x[i][0]),
                         reconstructed_revenue_dollars=float(reconstructed[i][0]),
                         original_minutes=float(fine), naive_coarse_minutes=float(naive),
                         original_access=int(fine <= threshold),
                         naive_coarse_access=int(naive <= threshold)))
    energy = sum(F(1, m) * (x[i][0] - x[j][0]) ** 2
                 for i, j, m in case["edges_minutes"])
    coarse_energy = sum(coarse[c][d] * (means[c][0] - means[d][0]) ** 2
                        for c in range(g) for d in range(c + 1, g))
    result = dict(
        synthetic=True, original_zones=n, groups=g, reduction=1 - g / n,
        group_sizes=sizes, group_mean_revenues=[float(v[0]) for v in means],
        original_mean_revenue=float(sum(v[0] for v in x) / n),
        equal_group_mean_revenue=float(sum(v[0] for v in means) / g),
        size_weighted_mean_revenue=float(sum(sizes[c] * means[c][0]
                                            for c in range(g)) / n),
        total_revenue=float(sum(v[0] for v in x)),
        sum_of_group_means=float(sum(v[0] for v in means)),
        reconstruction_squared_error=float(sum((x[i][0] - reconstructed[i][0]) ** 2
                                               for i in range(n))),
        original_energy=float(energy), coarse_energy=float(coarse_energy),
        energy_units="dollars squared per minute; weekly revenue feature",
        coarse_affinities=[[float(v) for v in row] for row in coarse],
        population=sum(people), access_threshold_minutes=threshold,
        original_access_share=sum(r["people"] * r["original_access"] for r in rows) / sum(people),
        naive_coarse_access_share=sum(r["people"] * r["naive_coarse_access"] for r in rows) / sum(people))
    return result, rows


def main():
    case = json.loads((HERE / "data/cases.json").read_text())["network"]
    result, rows = calculate(case)
    output = HERE / "results"
    output.mkdir(exist_ok=True)
    (output / "network.json").write_text(json.dumps(result, indent=2) + "\n")
    with (output / "zones.csv").open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
```

Change the population at A to 700 while leaving the other three zones at 100. Original access becomes 30%, and the naive coarse calculation still gives 100%. The representation error now affects a larger share of people. Returning to the original population and assigning every zone its own group reproduces the original routes. These comparisons hold the travel network fixed and change one object at a time.

## 5.25 Attributed Claims and Graph Relationships

\noindent An analyst comparing firms' pricing communication needs to distinguish a speaker's claim from the event described by that claim. Store the speaker, firm, call date, quoted or paraphrased statement, source location, and relevant reporting period. A statement that demand improved belongs first to a record of what was said. Treating it immediately as an observed change in demand removes the distinction between communication and measurement.

A knowledge graph can connect statements to speakers, documents, products, and periods. An ontology supplies definitions and inference rules for those relationships. Graph-based retrieval can use connections to select context for an answer, but retrieval performance still depends on source coverage, extraction accuracy, and answer evaluation. [Microsoft's GraphRAG documentation](https://microsoft.github.io/graphrag/) describes graph-based indexing and retrieval; those operations do not establish logical entailment or empirical truth by themselves.

Preserve disagreements instead of merging statements solely because they share a topic label. Gross revenue and net revenue, a forecast and a realized outcome, or different fiscal periods can support different values without a contradiction. Assess definitions and timing before assigning a conflict. If an LLM extracts a relation, retain its evidence span and check a sample against the original document. A contradiction inferred from a graph can identify a useful review target even when the source of the problem is a modeling assumption.

Representations used for retrieval or classification require a separate evaluation. Section 7.40 explains why exact reconstruction can coexist with different feature decompositions. Compare retrieval relevance, claim attribution, and downstream errors directly before interpreting a feature as a customer motive or a corporate strategy.

## 5.26 Changing the Representation of Food Descriptions

\noindent A food-logging service replacing a text encoder needs to preserve the category decisions that its downstream classifier makes. Word features distinguish terms such as chicken and cheese; character features can retain parts of related spellings. Each encoder defines its own coordinates. Coefficients fitted to one coordinate system need evidence of compatibility before they are applied to another.

Use the public mHealth food records for the fixed pseudonym cohort, normalizing descriptions by case-folding and collapsing whitespace. Exclude blank descriptions and blank or `Unclassified` categories, then assign each unique description its modal recorded category, with alphabetical tie breaking. Source labels such as `default` and `recipe` remain in the reference because the measurement target is agreement with this recorded classification system.

| Sample Property | Count |
| --- | ---: |
| Eligible source rows | 916,947 |
| Distinct normalized descriptions | 75,357 |
| Selected training descriptions | 6,000 |
| Selected validation descriptions | 1,500 |
| Selected test descriptions | 1,500 |
| Test descriptions with multiple recorded categories | 74 |

A hash of the normalized description determines its split and selection order independently of the category. Every selected description receives equal weight, so repeated logging does not increase its evaluation weight. Descriptions remain disjoint across splits, while users and calendar periods are shared. The resulting comparison concerns unseen descriptions within the 2016 cohort. A later-period or new-customer comparison would require a different split.

The source category can be ambiguous even when the normalized description is identical. Retain the number of distinct categories and the source rows supporting the modal category. A separate accuracy calculation for the 1,426 test descriptions with one recorded category measures sensitivity to that ambiguity. Independent nutrition judgments would be needed to change the target from recorded-category agreement to nutritional correctness.

The preparation program verifies the release checksum before reading its rows. Its output includes only description text, category counts, split, and a reproducible text hash. Download the public release with `python3 03_Data_and_Code/mHealth/download_data.py`, then run `python3 03_Data_and_Code/Representation_Alignment/prepare_descriptions.py` from the repository root. The compact input is also included with the [example](../../03_Data_and_Code/Representation_Alignment/README.md).


Python source: [prepare_descriptions.py](../../03_Data_and_Code/Representation_Alignment/prepare_descriptions.py)

```python
"""Build a bounded, description-level sample from the public mHealth release."""
import csv
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path
import pandas as pd

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / "mHealth/data/food_entries.csv.gz"
EXPECTED = "2ee04b155a93d51a02ee5acb61ff88a0dde2990b4713668c1b824ae6999ffbea"
CAPS = {"train": 6000, "validation": 1500, "test": 1500}


def normalize(text):
    return " ".join(str(text).casefold().split())


def partition(description):
    digest = hashlib.sha256(description.encode()).hexdigest()
    bucket = int(digest[:8], 16) % 10
    return ("train" if bucket < 6 else "validation" if bucket < 8 else "test"), digest


def summarize(counts):
    rows = []
    for description, categories in sorted(counts.items()):
        label = min(categories, key=lambda k: (-categories[k], k))
        split, digest = partition(description)
        rows.append(dict(description=description, category=label, split=split,
                         description_sha256=digest, source_entries=sum(categories.values()),
                         category_count=len(categories), modal_entries=categories[label]))
    return rows


def main():
    if not SOURCE.exists():
        raise FileNotFoundError("Run python3 03_Data_and_Code/mHealth/download_data.py first.")
    with SOURCE.open("rb") as stream:
        digest = hashlib.file_digest(stream, "sha256").hexdigest()
    if digest != EXPECTED:
        raise ValueError("The mHealth release checksum differs.")
    counts = defaultdict(Counter)
    all_rows = cohort_rows = usable_rows = 0
    columns = ["Userid", "Fancydate", "Name", "Category"]
    for chunk in pd.read_csv(SOURCE, usecols=columns, chunksize=250000,
                             dtype=str, keep_default_na=False):
        all_rows += len(chunk)
        eligible = chunk.Userid.str.slice(1, 5).map(lambda x: int(x, 16)) < 4096
        chunk = chunk.loc[eligible]
        cohort_rows += len(chunk)
        if not chunk.Fancydate.str.startswith("2016-").all():
            raise ValueError("Expected 2016 source dates.")
        description = chunk.Name.map(normalize)
        category = chunk.Category.str.strip()
        usable = description.ne("") & category.ne("") & category.ne("Unclassified")
        usable_rows += int(usable.sum())
        pairs = pd.DataFrame({"description": description[usable], "category": category[usable]})
        for (text, label), n in pairs.groupby(["description", "category"]).size().items():
            counts[text][label] += int(n)
    all_descriptions = summarize(counts)
    selected = []
    for split, cap in CAPS.items():
        candidates = [r for r in all_descriptions if r["split"] == split]
        selected.extend(sorted(candidates, key=lambda r: r["description_sha256"])[0:cap])
    target = HERE / "data/descriptions.csv"
    with target.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(selected[0]))
        writer.writeheader(); writer.writerows(selected)
    manifest = dict(source="mHealth teaching release 2026-10-23", source_sha256=digest,
                    source_rows=all_rows, cohort_rows=cohort_rows, usable_rows=usable_rows,
                    distinct_usable_descriptions=len(all_descriptions),
                    cohort_rule="First four pseudonym hex digits below 4096",
                    reference_label="Modal category among eligible 2016 rows; alphabetical tie break",
                    unit="One normalized description, equal weight", caps=CAPS,
                    split_rule="SHA256 first 8 digits modulo 10: 0-5 train, 6-7 validation, 8-9 test",
                    selection="Lowest full SHA256 within each split; independent of categories",
                    data_sha256=hashlib.sha256(target.read_bytes()).hexdigest(),
                    split_counts={s: sum(r["split"] == s for r in selected) for s in CAPS},
                    split_ambiguous={s: sum(r["split"] == s and r["category_count"] > 1
                                            for r in selected) for s in CAPS})
    (HERE / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
```

Hold the reference labels and description weights fixed when comparing representations through geometry, alignment, and classifier decisions (§§7.42–7.43).


## 5.27 Utility Disclosures as Qualitative Evidence

\noindent A household advocate must decide whether an assurance about electricity affordability addresses the costs that residents could face. An earnings call supplies a different observation from a household bill: management explains investment, recovery, and commercial expectations to investors. Reading these statements can reveal a mechanism that an aggregate comparison leaves unresolved. The relevant question is how a cost becomes recoverable, which customers receive the charge, when it takes effect, and which revenues or contractual protections offset it. A financial incentive to recover investment warrants close examination of these steps.

### 5.27.1 Define the Question Before Selecting Passages

\noindent The coding unit is an attributed claim within its surrounding speaker turn or document paragraph. The source unit is a dated document, and related documents remain grouped by issuer. The purposeful teaching set contains three earnings calls and three supporting documents, selected for explicit discussion of recovery and contrasting implications for customers. Its ten claim records are original paraphrases with locators. They provide a comparison of arguments, with no estimate of how prevalent those arguments are among utilities.

Directed qualitative content analysis begins with categories informed by the question and permits additional categories when the text does not fit. Recovery, allocation, timing, and offsets provide an initial framework here. The danger is to collect only statements that confirm an expectation of household harm. Record that expectation before coding and specify evidence that would change it, such as disallowed recovery or enforceable cost assignment to a large customer. Hsieh and Shannon (2005, pp. 1281–1283) discuss this approach and its susceptibility to confirmation bias. [(Hsieh and Shannon, 2005)](https://doi.org/10.1177/1049732305276687)

A broader study would define jurisdictions, dates, eligible issuers, and document types before collection, then explain any subsequent sampling decisions. Preserve unavailable records and seek cases that challenge the developing explanation. An investor call, its transcript mirror, and a newspaper account quoting it do not supply three independent observations. Saturation requires an explicit assessment appropriate to the analytical aim; it cannot be inferred from the size of this teaching selection.

### 5.27.2 Read Recovery and Offsets Together

\noindent In Evergy's February 19, 2026 call, David Campbell links new generation to possible above-inflation rate increases in Missouri West. The surrounding remarks describe expected cost spreading for most residential customers and longer-term benefits from load growth. The negative case changes the interpretation: recovery and offsets can operate together. A statement about rates growing more slowly than inflation also permits an increase in nominal bills. [Evergy call, PDF p. 6](https://investors.evergy.com/static-files/053ab9a3-f01f-44f1-8c97-89a40a3a148a)

CenterPoint's July 28, 2026 call describes a distribution tracker request for USD 73 million of additional revenue requirement. The adjacent discussion describes a separate settlement expected to reduce delivery charges. Both statements concern components of a regulatory process. Neither supplies the residential share of the requested amount or the net change in an individual household's total bill. A keyword count that labels both passages as evidence of rising household costs loses their distinct meanings. [CenterPoint call, PDF p. 10](https://investors.centerpointenergy.com/static-files/e83e69b9-83b3-4ee8-8a6b-9a430fdd714f)

Evergy's November 3, 2026 announcement makes the proposed household consequence more specific: an increase of USD 17.25 per month at 1,005 kWh, conditional on approval. It also attributes a USD 61 million reduction in its annual revenue request to anticipated data-center revenue. The offset is measured against a higher requested amount in the absence of that revenue. It does not imply that the proposed bill falls relative to today's bill. The announcement requests recovery for generation and grid investment; it does not identify how much of the bill change is caused by data centers. [Evergy rate request](https://newsroom.evergy.com/2026-11-03-Evergy-files-Missouri-West-rate-request-focused-on-reliability-and-new-generation-investments)

The accounting channel is explicit in Southern Company's 2025 disclosure: capitalized financing during construction raises the revenue requirement through rate base and depreciation. The residential allocation remains a separate regulatory question. A distinct channel appears in New Jersey's February 2025 auction announcement, which describes supply costs passing to ratepayers. Its PSE&G illustration moves from USD 155.84 to USD 182.71 per month at 650 kWh. The agency names several drivers, including data-center demand, supply constraints, and market rules, without estimating a causal share for each. Wholesale capacity charges must remain distinct from recovery of utility construction costs. [Southern accounting policy](https://www.sec.gov/Archives/edgar/data/92122/000009212226000006/R72.htm); [New Jersey auction results](https://nj.gov/bpu/newsroom/2025/approved/20250212.html)

![Investment recovery requires evidence about several distinct transitions. Management's forecast leads to a request; regulatory disposition and class allocation connect that request to authorized charges. Usage and later adjustments determine the household bill. Large-load revenues and guarantees can alter the amount recovered. Text locates claims about these transitions; it does not establish every transition.](../figures/M05_utility_evidence_chain.png)


> **Call Excerpt: Evergy, February 19, 2026**
>
> “customers may see rate increases above inflation over the next five years.”
>
> David Campbell, CEO, prepared remarks on Missouri West's generation investment. [Issuer transcript, p. 6](https://investors.evergy.com/static-files/053ab9a3-f01f-44f1-8c97-89a40a3a148a).

The excerpt is a forecast concerning Missouri West in a discussion of residential affordability. It also sits beside expected long-term benefits from new load. It does not attribute the entire potential increase to data centers.

> **Call Excerpt: CenterPoint, July 28, 2026**
>
> “we recover approximately 85% of our investments through capital trackers.”
>
> Chris Foster, CFO, prepared regulatory update. [Issuer transcript, p. 10](https://investors.centerpointenergy.com/static-files/e83e69b9-83b3-4ee8-8a6b-9a430fdd714f).

The percentage describes the company's investment-recovery mechanisms. It is not the residential share of investment. The surrounding distribution request links recovery to delivery charges, with customer-class allocation requiring additional evidence.

> **Call Excerpt: PSEG, February 25, 2025**
>
> “the basic generation service auction results will raise the residential bill starting June 1.”
>
> Ralph LaRossa, CEO, prepared remarks on the supply auction. [Public transcript, BGS discussion](https://www.roic.ai/quote/PEG/transcripts/2024-year/4-quarter).

This statement explicitly identifies a residential bill consequence. Its context concerns wholesale capacity and supply procurement. The New Jersey regulator's announcement corroborates the announced-price calculation, while construction-cost recovery remains a separate mechanism. The excerpt does not identify a data-center-specific causal contribution.

### 5.27.3 Preserve Context in a Comparison Matrix

\noindent Record the speaker, role, operating subsidiary, customer class, charge component, time horizon, and comparison for each claim. Distinguish prepared remarks from answers to analyst questions. Read the complete turn and inspect surrounding passages before coding direction. A statement about avoiding recovery, a question about recovery, and a recovery forecast can contain the same words. Retain contradictory passages and material that remains unclear.

Compare claims within a source before comparing source families. A matrix with documents as rows and mechanisms as columns helps preserve the relationship among recovery, timing, and offsets. Each cell retains a source locator, a concise interpretation, and any unresolved question. Gale et al. (2013, stages 2–7) describe familiarization, framework development, charting, and comparison within and across cases. Their framework is adapted here to public disclosures. A matrix organizes reasoning; its cells do not become independent statistical observations. [(Gale et al., 2013)](https://doi.org/10.1186/1471-2288-13-117)

Triangulation asks what different evidence contributes. A call identifies an attributed forecast. A filing documents a request, while an order establishes the regulator's disposition. An authorized rate and an assumed usage level support a bill illustration; household records are needed to observe expenditure. Agreement between a company's call and release strengthens the account of its stated position, while retaining the company's common incentives and information. Disagreement across sources can reveal a difference in timing, customer class, or counterfactual that needs explanation.

### 5.27.4 Review Interpretation and Record Revisions

\noindent For a shared codebook analysis, two readers can code the same passages independently before discussing disagreements. Preserve their original judgments, examine the reasons for differences, and revise definitions where needed. Then reconsider passages affected by the revision. O'Connor and Joffe (2020) discuss the uses and limits of this procedure. Agreement about a label does not establish that an executive's forecast is correct, and no independent human agreement estimate is available for the teaching annotations. [(O'Connor and Joffe, 2020)](https://doi.org/10.1177/1609406919899220)

Qualitative approaches make different commitments about interpretation. This structured content analysis uses explicit categories to compare documentary claims. Braun and Clarke (2021) explain why intercoder reliability is not a universal quality requirement for reflexive thematic analysis. Methodological quality requires coherence between the question, approach, and evaluation procedure. An LLM can suggest alternative readings or overlooked passages, but its repeated answers are not independent human judgments. [(Braun and Clarke, 2021)](https://doi.org/10.1080/14780887.2020.1769238)

Keep a reflexive memo recording the prior expectation, source-selection decisions, difficult cases, and reasons for changing an interpretation. Report who coded, what was checked, which materials were inaccessible, and which claims remain unresolved. SRQR identifies context, sampling, reflexivity, processing, and links between findings and empirical material as reporting concerns. These disclosures let a reader assess the analysis; completing a reporting checklist does not prove the conclusion. [(O'Brien et al., 2014, Table 1)](https://doi.org/10.1097/ACM.0000000000000388)

### 5.27.5 Collect Text Without Turning Missingness into Evidence

\noindent The collector requests six fixed public addresses, records raw-byte hashes, excludes markup, and checks document identity. It retains failures and builds local passage windows from recovery and investment vocabulary. Adjacent windows can overlap. Word counts measure the selected extraction, while substantive labels require contextual reading. Inspect unmatched passages as well as retrieved candidates to identify omissions caused by the dictionary.

Run `python3 collect.py --download` from `03_Data_and_Code/Utility_Cost_Recovery` to collect accessible documents, then `python3 collect.py` to reprocess local copies. Original issuer links remain in `sources.json` when the accessible rendition comes from a transcript provider. The executed collection retrieved all three call renditions and two announcements; the SEC accounting document remained unavailable to the downloader and was checked separately through a web reader. Its missing machine counts remain missing. Original documents and passage windows remain in the local cache; the public comparison uses metadata and paraphrases.

Python source: [collect.py](../../03_Data_and_Code/Utility_Cost_Recovery/collect.py)

```python
"""Retrieve a fixed public-source list; retain documents locally and export counts."""
import argparse
import hashlib
import io
import json
import re
import time
from collections import Counter
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

HERE = Path(__file__).resolve().parent
PATTERNS = {
    "investment": r"\b(invest\w*|infrastructure|construction|capital|generation)\b",
    "recovery": r"\b(recover\w*|rate base|revenue requirement|tracker\w*|rider\w*)\b",
    "household": r"\b(residential|household\w*)\b",
    "bill": r"\b(bill\w*|rate\w*|charge\w*)\b",
    "large_load": r"\b(data cent(?:er|re)s?|large load\w*|hyperscaler\w*)\b",
    "protection": r"\b(protect\w*|minimum bill\w*|take.or.pay|collateral|offset\w*)\b",
}


class VisibleText(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.hidden = 0
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag in {"head", "script", "style", "noscript"}:
            self.hidden += 1
        if tag in {"p", "div", "br", "tr", "h1", "h2", "h3"}:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in {"head", "script", "style", "noscript"}:
            self.hidden = max(0, self.hidden - 1)

    def handle_data(self, text):
        if not self.hidden:
            self.parts.append(text)


def extract(raw, spec):
    if spec["format"] == "pdf":
        if not raw.startswith(b"%PDF"):
            raise ValueError("Response is not a PDF")
        from pypdf import PdfReader
        pages = [p.extract_text() or "" for p in PdfReader(io.BytesIO(raw)).pages]
        # Remove exact repeated page furniture. Keep page numbers as locators.
        repeated = Counter(line.strip() for p in pages for line in set(p.splitlines()))
        pages = ["\n".join(x for x in p.splitlines()
                  if repeated[x.strip()] < 3 and not x.strip().isdigit()) for p in pages]
    else:
        parser = VisibleText()
        parser.feed(raw.decode("utf-8", errors="replace"))
        text = " ".join("".join(parser.parts).split())
        start = text.index(spec["start_marker"])
        stop = text.index(spec["end_marker"], start) if spec.get("end_marker") else len(text)
        pages = [text[start:stop]]
    pages = [" ".join(p.split()) for p in pages]
    combined = " ".join(pages)
    if any(marker.lower() not in combined.lower() for marker in spec["identity_markers"]):
        raise ValueError("Document identity or expected content did not match")
    if len(combined) < 400:
        raise ValueError("Empty or truncated document")
    return pages


def retrieve(spec, cache, download):
    path = cache / (spec["id"] + "." + spec["format"])
    receipt = cache / (spec["id"] + ".receipt.json")
    if path.exists() and receipt.exists():
        raw = path.read_bytes()
        record = json.loads(receipt.read_text())
        if hashlib.sha256(raw).hexdigest() != record["sha256"]:
            raise ValueError("Cached source checksum differs")
        return raw, record
    if not download:
        raise FileNotFoundError("No local source; use --download for the fixed URL list")
    request = Request(spec["url"], headers={"User-Agent": "MarketingAnalyticsCourse/1.0 (educational source review)"})
    time.sleep(2)  # Sequential requests, no authentication or access-control bypass.
    with urlopen(request, timeout=40) as response:
        raw = response.read(15_000_001)
        if len(raw) > 15_000_000:
            raise ValueError("Document exceeds 15 MB limit")
        record = {"source_id": spec["id"], "url": spec["url"],
                  "final_url": response.geturl(), "http_status": response.status,
                  "retrieved_at": datetime.now(timezone.utc).isoformat(),
                  "sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw)}
    extract(raw, spec)  # Never cache an error page as a successful document.
    path.write_bytes(raw)
    receipt.write_text(json.dumps(record, indent=2) + "\n")
    return raw, record


def features(pages):
    text = " ".join(pages)
    values = {key: len(re.findall(pattern, text, re.I)) for key, pattern in PATTERNS.items()}
    values["words"] = len(re.findall(r"\b[\w'-]+\b", text))
    return values


def candidates(pages):
    found = []
    for page, text in enumerate(pages, 1):
        sentences = re.split(r"(?<=[.!?])\s+(?=[A-Z])", text)
        for i, sentence in enumerate(sentences):
            context = " ".join(sentences[max(0, i - 1):i + 2])
            tags = [k for k, p in PATTERNS.items() if re.search(p, context, re.I)]
            if "bill" in tags and ("recovery" in tags or "investment" in tags):
                found.append({"page": page, "sentence": i + 1, "tags": tags,
                              "context": context})
    return found


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--download", action="store_true")
    parser.add_argument("--output", type=Path, default=HERE / ".cache/retrieval.json")
    args = parser.parse_args()
    cache = HERE / ".cache"
    cache.mkdir(exist_ok=True)
    records = []
    for spec in json.loads((HERE / "sources.json").read_text()):
        try:
            raw, receipt = retrieve(spec, cache, args.download)
            pages = extract(raw, spec)
            matches = candidates(pages)
            (cache / (spec["id"] + ".review.json")).write_text(json.dumps(matches, indent=2) + "\n")
            (cache / (spec["id"] + ".pages.json")).write_text(json.dumps(pages, indent=2) + "\n")
            records.append({**receipt, "status": "ok", "pages": len(pages),
                            "candidate_windows": len(matches), **features(pages)})
        except (HTTPError, OSError, ValueError) as error:
            records.append({"source_id": spec["id"], "url": spec["url"],
                            "status": "unavailable", "reason": str(error)})
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(records, indent=2) + "\n")
    print(json.dumps({r["source_id"]: r["status"] for r in records}, indent=2))


if __name__ == "__main__":
    main()
```

### 5.27.6 Reproduce the Evidence Matrix and Bill Comparisons

\noindent The offline analysis retains every selected document, groups related claims by issuer, and calculates the two stated-use bill comparisons with exact decimal arithmetic. New Jersey's increase is USD 26.87, or 17.24 percent of the original bill. Annualizing the monthly difference gives USD 322.44 under twelve equal-use months with unchanged rates. Evergy's proposed difference gives USD 207 under the same assumption, conditional on approval. These are arithmetic illustrations of the cited documents, with later adjustments and actual consumption outside the comparison.

Run `python3 analyze.py` and `python3 test_examples.py` in the same folder. The outputs preserve evidence stage, population, offsets, and limitations beside each interpretation. Direction counts describe ten selected claims and do not estimate the frequency of household cost shifts.

Python source: [analyze.py](../../03_Data_and_Code/Utility_Cost_Recovery/analyze.py)

```python
"""Reproduce coverage, a qualitative comparison matrix, and bill arithmetic."""
import csv
import json
from collections import Counter
from decimal import Decimal
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGES = {"forecast", "request", "proposal", "accounting_mechanism",
          "approved_price_illustration", "regulator_explanation"}
DIRECTIONS = {"increase", "offset", "mechanism", "mixed", "unclear"}


def load_inputs():
    sources = json.loads((HERE / "sources.json").read_text())
    claims = json.loads((HERE / "data/claims.json").read_text())
    retrieval = json.loads((HERE / "data/retrieval_snapshot.json").read_text())
    for rows, key in [(sources, "id"), (claims, "claim_id"), (retrieval, "source_id")]:
        if len({x[key] for x in rows}) != len(rows):
            raise ValueError("Duplicate key: " + key)
    index = {s["id"]: s for s in sources}
    if set(index) != {r["source_id"] for r in retrieval}:
        raise ValueError("Retrieval roster must retain all selected sources")
    for row in claims:
        if row["source_id"] not in index or row["stage"] not in STAGES:
            raise ValueError("Unknown source or evidence stage")
        if row["direction"] not in DIRECTIONS:
            raise ValueError("Unknown direction")
        if not all(row[k] for k in ["locator", "population", "counterevidence",
                                    "interpretation_limit", "annotation_status"]):
            raise ValueError("An interpretation requires context and qualifications")
    return index, claims, retrieval


def coverage(sources, retrieval):
    rows = []
    for record in retrieval:
        spec = sources[record["source_id"]]
        observed = record["status"] == "ok"
        rows.append({"source_id": spec["id"], "kind": spec["kind"],
                     "observed": observed,
                     "words": record.get("words") if observed else None,
                     "recovery_matches": record.get("recovery") if observed else None})
    return rows


def comparison_matrix(sources, claims):
    # A claim is the coding unit. Related documents remain within an issuer family.
    rows = []
    for row in claims:
        spec = sources[row["source_id"]]
        rows.append({"issuer_family": spec["issuer"], "date": spec["date"],
                     **row, "source_url": spec.get("primary_url", spec["url"])})
    return rows


def bill_calculations():
    before, after = Decimal("155.84"), Decimal("182.71")
    change = after - before
    return [
        {"case": "NJBPU_PSEG", "monthly_kwh": 650,
         "monthly_change_usd": str(change),
         "percent_change": str((100 * change / before).quantize(Decimal("0.01"))),
         "annualized_change_usd": str(12 * change),
         "status": "Fixed-use illustration of announced auction prices; excludes later adjustments"},
        {"case": "Evergy_Missouri_West", "monthly_kwh": 1005,
         "monthly_change_usd": "17.25", "percent_change": None,
         "annualized_change_usd": str(12 * Decimal("17.25")),
         "status": "Proposed bill change if approved and held for 12 equal-use months"},
    ]


def write_csv(path, rows):
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main():
    sources, claims, retrieval = load_inputs()
    out = HERE / "results"
    out.mkdir(exist_ok=True)
    write_csv(out / "coverage.csv", coverage(sources, retrieval))
    write_csv(out / "evidence_matrix.csv", comparison_matrix(sources, claims))
    write_csv(out / "bill_illustrations.csv", bill_calculations())
    observed = [r for r in retrieval if r["status"] == "ok"]
    result = {"selected_documents": len(sources),
              "downloaded_documents": len(observed),
              "selected_calls": sum(s["kind"] == "earnings_call" for s in sources.values()),
              "claims": len(claims),
              "issuer_families": len({s["issuer"] for s in sources.values()}),
              "coded_stages": dict(sorted(Counter(c["stage"] for c in claims).items())),
              "coded_directions": dict(sorted(Counter(c["direction"] for c in claims).items())),
              "interpretation": "Counts describe purposeful teaching selections, not population prevalence.",
              "independent_human_coders": 0, "causal_effect_estimates": 0}
    (out / "summary.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
```

### 5.27.7 State the Supported Challenge

\noindent These disclosures substantiate cost-recovery mechanisms and intentions that a blanket assurance about household affordability would need to address. The electricity paper itself models recovery and reports positive residential spillovers, so the existence of these mechanisms is compatible with its framework. The qualitative evidence does not identify a replacement causal estimate. Most selected statements were made in 2026, after the paper's 2020–2025 window, which makes the timing relevant to extrapolation.

A disciplined critique distinguishes a contradiction from an omitted qualification. A categorical claim that infrastructure costs never reach households conflicts with the documented recovery mechanisms. A finding about a small historical average can coexist with those mechanisms, heterogeneous burdens, and future investment. The defensible demand is that public reassurance specify the outcome, period, affected customers, and evidence for the proposed allocation. Investor disclosures also leave residents' experiences and authority to challenge charges largely unobserved. Those questions require additional sources, as developed in §9.33.

## 5.28 Qualitative Evidence and the Threshold for Inquiry

A consumer representative deciding whether to seek billing records can use evidence of cost-recovery mechanisms before estimating a causal bill effect. Utility statements about investment, rate cases, and recovery from customer classes identify questions for further inquiry. Their value depends on speaker role, timing, exact wording, corroborating records, and contrary evidence. Repeated statements from the same source or investor audience do not become independent observations merely because a text model assigns them separate rows.

The excerpts in §5.27 support specific institutional mechanisms. Much of that selected material dates from 2026, after the data-center paper's 2020–2025 period, and the paper itself discusses cost recovery and some positive residential spillovers. A careful argument preserves these facts while asking whether a broad reassurance about household costs remains supported. Text evidence can establish that a proposed mechanism is taken seriously by decision makers while leaving its historical magnitude and incidence unresolved.

Translate the evidence into a proportionate next step: obtain the relevant tariff filing, trace an investment's approval and recovery dates, examine abandoned projects, and compare affected customer classes. Code both supporting and disconfirming passages, preserve full context, and document selection rules, following the qualitative standards in the [source guide](../../01_Resources/42_Qualitative_Evidence/README.md). The justification for opening that inquiry differs from the evidence required to attribute a particular household loss or impose a sanction. M6 §6.45 and M9 §9.58 make those decision thresholds explicit.

## 5.29 Engagement, Endorsement, and Unwanted Continuation

\noindent A social platform evaluating a recommendation system needs to distinguish successful prediction of continued use from a justified claim of user benefit. Content sequences and displayed streaks can affect subsequent behavior, including the goals people pursue (Woolley and Sharif, 2022; Silverman and Barasch, 2023). A comment, click, or repeated visit therefore reflects conduct within a designed environment. Interpreting that conduct as endorsement requires support concerning the person's purposes and control.

Qualitative evidence can help identify the relevant conflict. Code a stated purpose, a feature or exposure, a reported consequence, and an attempt to stop separately. A complaint about wasted time supports a different claim from a clinical diagnosis, and an enthusiastic long session is a consequential contrary case. Preserve the selection process: public posts disproportionately represent people who chose to speak, while repeated or copied accounts supply limited independent evidence. Automated labels require contextual review before they support a claim about harm.

A claim that a company uses a published insight needs a documented connection, while a claim that the use harms consumers needs relevant outcome evidence. These questions remain separate even when both deserve investigation. Compare the [publication and industry cases](../../01_Resources/49_Online_Engagement_and_Agency/README.md), then assess a design through the argument in M9 §§9.70–9.75 and the complete synthetic feed-policy program in §9.48.

## 5.30 Source Passages, Coding, and the Scope of a Claim

\noindent A regulator assessing electricity costs needs to distinguish a utility's statement about infrastructure financing from evidence of a realized household bill increase. Text analysis can make the financing mechanism visible, but the interpretation depends on the speaker, date, customer class, regulatory setting, and qualifications in the surrounding exchange. A short passage extracted by an assistant can lose the very condition that determines who pays.

For each boxed call excerpt in §5.27, preserve the issuer, call date, speaker, source location, and exact passage. Store the coding decision separately: for example, a proposed investment enters a rate base, recovery depends on regulatory approval, or a large customer faces a specific tariff. Then write the substantive inference in a third record. A passage supporting possible residential exposure warrants investigation of the relevant tariff and recovery process. A conclusion about realized household costs needs evidence connecting that process to the household and period at issue.

The three records make disagreement productive. A second reader can agree that a passage is transcribed accurately while disputing the assigned code or the inference drawn from it. Search the surrounding text and other disclosures for conditions that narrow or oppose the interpretation, and retain disagreements with their reasons. These practices extend the codebook, contextual reading, and negative-case assessment in §5.27. A dictionary match or a valid source identifier supplies no automatic judgment about what the passage entails.

The recurring data-center case also requires chronology. The later utility disclosures in §5.27 can establish that executives discuss mechanisms by which investment may reach customer costs. Their timing and selection do not identify the realized treatment effect in the earlier 2020–2025 panel. Connect each claim to the period and institutional process it actually addresses. A defensible synthesis can motivate inquiry into missing mechanisms while preserving that distinction.

**Worked interpretation.** Select a preserved passage, write the narrowest supported claim, and identify the additional premise required to assert a household bill increase. Give that premise its own source field or mark it unresolved. An internally approved summary with the unresolved premise still leaves the stronger inference unsupported. M9 §9.85.5 gives a runnable comparison of source checks and claim support.
