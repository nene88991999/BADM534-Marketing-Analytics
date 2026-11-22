# Data Dictionary

All inputs and outcomes in this folder are synthetic teaching constructions. No real respondents, demographics, purchase records, or generated-model performance observations are included. The two input files define independent examples.

## Authored Text and Anchor Comparisons

`data/anchor_responses.json` contains three fictional concepts, two invented persona identifiers, two anchor sets, and seven response rows. The row key is `(concept, persona, repeat)`. Every concept/persona pair appears. The refill/p01 pair has two identical rows to isolate repeat weighting.

| Field | Unit and Meaning |
| --- | --- |
| `concepts` | Mapping from concept identifier to fictional body-wash description |
| `personas` | Complete roster of invented persona identifiers; no population weights or demographic claims |
| `anchor_sets` | Ordered lists of five authored sentences representing categories 1–5 |
| `concept`, `persona`, `repeat` | Product, invented respondent, and within-persona response identifiers |
| `text` | Instructor-authored illustrative answer |
| `similarities` | Five imposed cosine-similarity values for each anchor set; dimensionless, constrained to [-1, 1] |

In `results/response_ratings.json`, each response appears for Set 1, Set 2, and their mean, producing 21 records. `distribution` is an ordered five-category PMF or null for an uninformative mapping. `mean_rating` uses scores 1–5 and is measured in rating points. `status` distinguishes scored and uninformative rows. The numerical abstention tolerance is 1e-12 on the spread of similarities.

`results/concept_ratings.json` has nine concept/anchor records. `response_rows` counts supplied answers, `scored_rows` counts available mappings, and `personas` counts distinct persona identifiers. `distribution` averages repeats within persona and then personas equally. `top_two_share` sums categories 4 and 5. `row_weighted_mean` instead averages all response rows equally. Null aggregates retain an incomplete status when a required mapping is unavailable. No null is converted to zero or silently excluded.

## Synthetic Concept Panels

`data/concept_panels.json` contains six fictional concepts, A–F, and three imposed candidate patterns. Each reference `counts` array contains 100 invented ratings in categories 1–5. The candidate objects cover the same six identifiers, each with a five-category PMF. All category values, candidate patterns, and ordering are fixed, so no random seed is used.

The pooled PMF is the average reference distribution. The reversed pattern assigns the distribution from the opposite position in the A–F ordering. The compressed pattern gives 80% weight to the pooled PMF and 20% to the concept's reference PMF. Reference outcomes construct the patterns deliberately. This is an analytical comparison, with no training, validation, or final-test sample.

`results/screening_details.json` has eighteen candidate/concept records. It preserves reference and candidate PMFs, their mean ratings, and concept-level KS similarity. The KS value equals one minus the maximum difference between cumulative category probabilities.

| Summary Field | Unit and Meaning |
| --- | --- |
| `candidate`, `concepts` | Imposed pattern name and common concept denominator, six |
| `mean_ks_similarity` | Equally weighted mean over the six concept-level similarities |
| `mean_absolute_rating_error` | Average absolute error in concept means, in rating points |
| `pearson` | Correlation of the six reference and candidate means; null for constant values |
| `spearman` | Correlation of average ranks, with exact ties assigned average ranks; null for a constant ranking |
| `reference_top_two` | Two concepts with the highest reference mean, A and B |
| `selected` | Candidate top-two identifiers, or null when a tie at the boundary prevents unique selection |
| `selection_status` | Unique selection or boundary tie; boundary comparisons use absolute tolerance 1e-12 |
| `top_two_recall` | Number of A and B retained divided by two; null when selection is unresolved |

The distinct quantities have distinct denominators: response rows, personas, concepts, category weights, and two selected products. Rating points and category weights are not sales, monetary willingness to pay, causal effects, or calibrated purchase probabilities.
