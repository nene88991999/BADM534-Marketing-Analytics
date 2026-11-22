# Expected Results

## Anchor Sensitivity and Persona Weighting

Twenty-one response/anchor records produce nine concept/anchor summaries. All required mappings are available for the supplied inputs. The refill case has three response rows and two personas; the other concepts each have two rows and two personas.

| Concept | Set 1 Mean | Set 2 Mean | Mean Across Sets |
| --- | ---: | ---: | ---: |
| Refillable | 3.975 | 3.625 | 3.800 |
| Fragrance-Free | 3.850 | 4.100 | 3.975 |
| Compact Travel | 3.425 | 3.300 | 3.3625 |

For refill/p01/repeat1, Set 1 produces weights `(0, .05, .15, .30, .50)` with mean 4.25; Set 2 produces `(0, .10, .30, .40, .20)` with mean 3.70. These ten weights generate the [anchor figure](../../../06_Lecture_Notes/figures/M05_anchor_ratings.tex). The refill concept's Set 1 row-weighted mean is 4.0666667, compared with 3.975 under equal-persona weighting.

## Distribution Fit and Selection

Eighteen candidate/concept comparisons produce three summaries. Every reference panel has 100 invented ratings, and every mean across concepts weights the six concepts equally.

| Pattern | Mean KS Similarity | Mean Absolute Rating Error | Pearson and Spearman | Selected | Top-Two Recall |
| --- | ---: | ---: | --- | --- | ---: |
| Pooled | 0.925 | 0.150 | Undefined | Boundary Tie | Undefined |
| Reversed | 0.850 | 0.300 | -1 | F, E | 0 |
| Compressed | 0.940 | 0.120 | 1 | A, B | 1 |

The pooled category shares are `(0, 0, .225, .30, .475)` for both the reference and all three candidates. Reference means are `(4.5, 4.4, 4.3, 4.2, 4.1, 4.0)`. Pooled means equal 4.25, reversed means run from 4.0 to 4.5, and compressed means are `(4.30, 4.28, 4.26, 4.24, 4.22, 4.20)`. These values generate the [screening figure](../../../06_Lecture_Notes/figures/M04_concept_screening.tex). Constant scores remain undefined for correlation and unresolved for unique selection.

All values are exact consequences of imposed inputs, subject to ordinary floating-point rounding. They estimate no empirical accuracy, sales effect, or population preference.
