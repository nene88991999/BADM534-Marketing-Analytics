# Representation Evaluation Dictionary

Every numerical input is synthetic. The four cases receive equal weight. Coordinates are imposed standardized scores except that the first is multiplied by a stated scale; no text embeddings were estimated.

| Field | Meaning |
| --- | --- |
| `case_id` | Unique case identifier. |
| `style_sign` | Imposed style score, −1 or +1. |
| `review_signal` | Imposed review score, −1 or +1. Review is required when positive. |
| `style_scales` | Multipliers 100 and 1 on the first coordinate. |
| `representation_B_style_multiplier` | Fixed factor 0.98. A preserves the first coordinate and sets the second to zero; B shrinks the first and preserves the second. |
| `variation` | Sum of squared deviations from each coordinate's mean over the four evaluation cases. |
| `squared_errors` | Sum of squared reconstruction errors by coordinate. |
| `component_fvu` | Coordinate squared error divided by its variation. |
| `variance_weights` | Coordinate variation divided by total variation. |
| `total_fvu` | Total squared reconstruction error divided by total variation. |
| `variance_explained_pct` | 100 times one minus total FVU; this measure may be negative for poor reconstructions. |
| `recall` | Correctly routed positive cases divided by the two cases requiring review. |
| `accuracy` | Correct binary routing decisions divided by all four cases. |
| `unit_directions` | Two Euclidean-unit vectors in each imposed decomposition. |
| `coefficient_per_direction` | Positive weight multiplying each direction, square root of 2 or 5. |
| `contributions` | Weighted directions, `(1, ±1)` or `(1, ±2)`. |
| `squared_error_after_removing_first` | Squared Euclidean distance from target `(2, 0)` to the remaining contribution. |

FVU uses coordinate-specific units and an orthonormal coordinate system. A change of units changes its relative penalties. Routing metrics preserve the same case population and reference labels. The examples have no train/test fit; a learned system would require an independently held-out evaluation and training-only preprocessing.
