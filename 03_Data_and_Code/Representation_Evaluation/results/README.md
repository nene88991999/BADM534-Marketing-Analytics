# Representation Results

`representations.json` includes every synthetic input and reconstructed coordinate. At scale 100, component variation is `[40000, 4]`. Squared errors are `[0, 4]` for A and `[16, 0]` for B. Their total FVU values are respectively `1/10001` and `4/10001`. Recall on the two positive cases is 0% and 100%; accuracy over all four cases is 50% and 100%. At scale 1, total FVU becomes 0.5 and 0.0002.

`decompositions.json` records two exact sums to `(2, 0)`. Removing the first contribution leaves `(1, −1)` or `(1, −2)`, producing squared errors of 2 and 5. The dictionaries, coefficients, and removal operations are imposed; no feature was learned.
