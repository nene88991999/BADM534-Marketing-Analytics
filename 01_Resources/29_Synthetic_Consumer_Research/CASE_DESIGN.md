# Product Screening With Synthetic Consumer Responses

A fictional personal-care firm has more product ideas than it can afford to test with a large human panel. The manager needs a shortlist and a way to detect promising ideas that the screening procedure rejects. [Two original Python programs](../../03_Data_and_Code/Synthetic_Consumers/README.md) separate the numerical representation of a response from evaluation of a product-selection rule.

## Text, Anchors, and Personas

M5 §5.23 uses authored responses for three concepts and two invented personas, with seven response rows. Similarities are imposed independently of the text. A fixed response receives mean ratings of 4.25 and 3.70 under two supplied anchor comparisons. Equal-persona aggregation prevents an identical repeat from increasing one persona's weight. The full program preserves duplicate checks, required concept/persona coverage, uninformative mappings, and incomplete aggregates.

## Distribution Fit and Product Selection

M4 §4.23 uses six separate fictional concept panels with 100 invented ratings each. Pooled, reversed, and compressed candidate patterns have identical overall category shares while implying different product rankings. Pooled means leave correlation undefined and selection tied; reversed ranks retain none of the reference top two; compressed ranks retain both while understating rating differences. The full program checks the common roster and calculates distribution fit, magnitude error, correlations, and shortlist retention.

## Validation and Consumer Representation

M7 §7.36 defines the paper's correlation-attainment ratio, identifies its split-half benchmark, and explains why anchor development must remain outside final concept evaluation. A stated independent-error model shows why a noisy human benchmark is not a universal correlation ceiling. M8 §8.11 connects the complete screening workflow to model and domain changes. M9 §9.18.4 examines whose preferences generated personas represent through Kantian respect and Confucian trustworthiness.

Human research should include shortlisted concepts and a random sample of rejected concepts. Known selection probabilities make missed opportunities estimable across the original pool, with suitable uncertainty. A live extension requires appropriate human data and a versioned record of the full procedure. The course examples make no claim about actual model or consumer performance.

## Teaching Materials

Session 5 uses twenty minutes of its application block for concept screening and validation. Session 7 uses ten minutes of its concepts block for rating construction. Session 14 uses five minutes within its existing philosophical discussion for consumer representation. Eight slides and two editable Illinois-color TikZ figures accompany the notes, with complete Markdown descriptions and aggregate tables.

The [optional ungraded lab](../../07_Labs/Synthetic_Consumers/README.md) provides longer sensitivity analysis, independent explanation, and a human-validation design. Both programs and ten independent checks have executed without upstream code or external model calls. The [dictionary](../../03_Data_and_Code/Synthetic_Consumers/DATA_DICTIONARY.md), [results](../../03_Data_and_Code/Synthetic_Consumers/results/README.md), and [manifest](../../03_Data_and_Code/Synthetic_Consumers/manifest.json) retain input provenance, units, and verification scope.
