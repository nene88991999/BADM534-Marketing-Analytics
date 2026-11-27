# Data Dictionary

Every row and amount is synthetic. The observation unit in the ledgers and releases is one household for one current monthly billing comparison. H and L are alternative worlds, each with a target of 400 households; their counts must not be added as an empirical sample. All amounts use USD per household-month. The previous bill equals the current no-project potential bill only under the construction's fixed-background restriction.

| Field | Definition |
| --- | --- |
| `household_id` | Artificial identifier A000–D099, reused across alternative worlds |
| `group` | Stratum A, B, C, or D; 100 households each |
| `previous_bill_usd` | Constructed prior bill, 120–124 |
| `current_bill_usd` | Constructed realized bill after the project |
| `no_project_bill_usd_oracle` | Unobserved potential outcome supplied by the simulation, equal to prior bill |
| `effect_usd_oracle` | Current bill minus oracle no-project bill; H has -10 in A/B and +30 in C/D; L has -10 throughout |
| `inclusion` | Known stratum inclusion probability under the specified random release design; stored as an exact fraction |

The released files omit both oracle fields. A household missing from a release is unobserved in that file. Its effect is not zero.

`selection_comparisons.csv` has one row per world-policy pair. `coverage` divides released households by 400. `released_mean_change_usd` uses the selected denominator. `weighted_mean_change_usd` is the Horvitz–Thompson total of changes divided by the known target size, 400. It is `undefined` when any target stratum has zero inclusion probability. `target_mean_effect_usd_oracle` uses all constructed effects.

`bounds.csv` records the observed mean, coverage, assumed bounds on unreleased effects, and the resulting population-mean endpoints. Fractions such as `10/3` are exact rational values. They can be parsed with Python's `fractions.Fraction`; treating them as dates or text categories changes their meaning.
