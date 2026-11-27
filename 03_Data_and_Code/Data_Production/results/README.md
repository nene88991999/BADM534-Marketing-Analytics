# Synthetic Availability Results

`synthetic_ledger_H.csv` and `synthetic_ledger_L.csv` contain the full constructed populations, including oracle potential outcomes. Six `released_*.csv` files contain the records visible under three disclosure policies in each world. The two restricted releases are identical. `selection_comparisons.csv` reports six comparisons, and `bounds.csv` records one support calculation.

In H, the full effect total is USD 4,000 over 400 household-months; the target mean is USD 10. In L, the total is USD -4,000 and the target mean is USD -10. The restricted release in either world totals USD -2,000 over 200 household-months. Dividing that subtotal by 400 would implicitly assign zero effects to the unavailable half and incorrectly report -5 in H.

The broader H release has 200 declines of 10 and 100 increases of 30, giving an unweighted mean of 10/3. Inverse inclusion weighting doubles the contributions of the half-sampled C/D strata and recovers 10. Exact recovery follows from constant effects within strata. The bounds [-15, 15] use an imposed range [-20, 40] for the missing half.

These are logical illustrations, with no estimate of actual utility effects or disclosure behavior. See [inputs and commands](../README.md) and [field definitions](../DATA_DICTIONARY.md).
