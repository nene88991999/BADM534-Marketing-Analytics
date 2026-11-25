# Description Sample and Evaluation Outputs

## Source and Population

The source is the public mHealth food-entry release of October 23, 2026, with SHA-256 recorded in [manifest.json](manifest.json). Preparation retains pseudonyms whose first four hexadecimal digits are below 4096. The selected cohort contains 917,153 food rows in 2016. Excluding blank descriptions and blank or `Unclassified` categories leaves 916,947 rows and 75,357 normalized descriptions. The sample is a deterministic subset of this cohort.

Normalization case-folds text, collapses whitespace, and trims its ends. Each distinct normalized description receives its modal source category across eligible rows. Equal category counts are resolved alphabetically. Labels such as `default` and `recipe` are retained as recorded. No nutrition classification is inferred.

SHA-256 determines the split independently of the category: the first eight hexadecimal digits modulo ten allocate buckets 0–5 to training, 6–7 to validation, and 8–9 to test. Within each split the lowest full hashes select at most 6,000, 1,500, and 1,500 descriptions. Rows are unique by normalized description. This design evaluates unseen descriptions within the 2016 cohort; users and calendar periods are shared across splits.

## Input Fields

| Field | Meaning |
| --- | --- |
| `description` | Normalized food-description text |
| `category` | Modal recorded category among eligible source rows |
| `split` | `train`, `validation`, or `test` |
| `description_sha256` | Hash of normalized text; reproducible key and selection order |
| `source_entries` | Number of eligible rows with the description |
| `category_count` | Number of distinct recorded categories for that description |
| `modal_entries` | Rows supporting the selected modal category |

`source_entries` and `modal_entries` describe reference construction. They are not analysis weights. Each description receives weight one. Multiple-category counts are 343 in training, 89 in validation, and 74 in test.

## Fitted Quantities and Metrics

Word unigrams and character trigrams each use the 512 most frequent training-document tokens, with alphabetical tie breaks. Term weights are `1 + log(count)`; inverse-document frequency is `log((1+n_train)/(1+document_frequency))+1`. Each row has unit Euclidean norm when nonzero. Unseen tokens contribute zero. Uncentered SVD directions come from the training feature Gram matrix. Their signs can differ across numerical implementations; the deliberately unmapped comparison is sensitive to that convention. The saved environment identifies the executed calculation.

A ridge least-squares classifier predicts one-hot source labels, with an unpenalized intercept and penalty 1 on coefficients. The largest score selects a category; sorted class order breaks ties. There are 264 training classes. A rotation, a positive scale, and translation map paired character training vectors to word coordinates. Validation chooses 8, 16, or 32 components by aligned accuracy; lower dimension breaks a tie. No test label enters fitting or selection.

Accuracy counts correct modal categories over all descriptions. Macro F1 averages over the union of training and current evaluation classes, including classes with no predicted positives; undefined F1 is set to zero. The test union has 273 categories. Category-specific support, correct counts, predicted counts, recall, and F1 are in `results/mhealth.json`. Ten test descriptions belong to nine categories absent from training and count as errors.

Neighbor overlap uses Euclidean distance between descriptions within the same evaluation split and the same dimension. Each description contributes the fraction of its ten neighbors shared with the word reference. Self-neighbors are excluded. Squared distances are rounded to twelve decimal places to treat rotation roundoff as ties; common row order breaks ties. This score uses evaluation features, independently of labels. It does not measure agreement with a human judgment of semantic similarity.

`results/test_predictions.csv` records all four predictions and the reference category for each test hash. `results/summary.csv` contains validation scores at all three dimensions and test scores only at the selected dimension. `results/synthetic.json` records the invented vectors and decisions separately. `results/mhealth.json` records software versions, configuration values, denominators, category-level errors, and the accuracy among the 1,426 test descriptions with one recorded category.
