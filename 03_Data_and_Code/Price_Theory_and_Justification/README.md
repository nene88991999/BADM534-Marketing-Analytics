# Prices, Budgets, and Justification

A manager ranks customers by willingness to pay. A project sponsor argues that aggregate gains justify an uncompensated loss. These synthetic comparisons separate the numerical calculation from the principle needed to justify the action.

## Inputs and Units

The first comparison has two people, A and B, with one-period budgets of $100 and $1,000 and the same specified service increment of 0.2 in logarithmic utility. Exchanging budgets holds that increment and the functional form fixed. Reservation prices solve the indifference equation in M9 §9.77. These are constructed preferences, with no estimate of actual need, autonomy, or interpersonal welfare.

The separate project comparison has one firm gaining $140 and 100 residents each losing $1 over the same period. The alternative pays each resident $1. Transfers have zero resource cost in this illustration; no uncertainty, other affected party, or nonfinancial consequence is included. Aggregate dollar changes are accounting sums, with no interpersonal utility interpretation.

## Reproduction

Run from the repository root with Python 3 and its standard library:

```sh
python3 03_Data_and_Code/Price_Theory_and_Justification/compare_valuations.py
python3 03_Data_and_Code/Price_Theory_and_Justification/verify_comparisons.py
```

The program saves [results.json](results.json) beside its source. Expected reservation prices are $18.13 and $181.27; exchanging budgets reverses their owners. Both project policies have a $40 aggregate dollar gain, while the number of residents with dollar losses changes from 100 to zero. The verification evaluates the utility equation directly, checks the budget reversal, and reconciles firm and household changes with the saved file. There is no seed or network dependency.

## Interpretation and Provenance

The calculations are original teaching examples. They implement no particular author's estimated model and use no replication microdata. The [reading guide](../../01_Resources/50_Chicago_Price_Theory_and_Moral_Justification/README.md) links the valuation, compensation, and moral arguments. [M9 §§9.76–9.82](../../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md) includes the complete program and explains why these calculations leave the choice of principle open. [Optional practice](../../07_Labs/Scanlon_Pricing/README.md#price-theory-and-moral-permission) asks students to defend that principle and answer its strongest objection.
