# Alignment Results

The [synthetic calculation](synthetic.json) records eight invented test cases and distinct fitting points. The [mHealth result](mhealth.json), [comparison table](summary.csv), and [test predictions](test_predictions.csv) come from the executed local programs. The selected dimension is 32, using validation accuracy alone.

All test configurations use 1,500 descriptions with equal weights. Neighbor overlap uses ten neighbors per description. Reference categories are source modes. The primary result includes 74 descriptions with multiple recorded categories and ten with categories absent from training. The separate one-category comparison uses 1,426 descriptions.

Category-level outcomes and the explicitly defined macro-F1 denominator remain in the JSON. Interpretation, provenance, and reproduction commands are in the [example README](../README.md) and [dictionary](../DATA_DICTIONARY.md). The programs made no model API calls. No neural-state swapping, prompt-condition experiment, timing benchmark, or observed commercial return is measured.
