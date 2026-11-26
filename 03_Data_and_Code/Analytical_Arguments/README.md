# Analytical Arguments and Counterexamples

A retailer must decide whether a price change or a choice procedure benefits customers. These original synthetic examples separate agreement with observed purchases, identification of a policy effect, and the valuations needed for a welfare conclusion. [M1 §1.20](../../06_Lecture_Notes/modules/M01_Marketing_Analytics_and_Python.md), [M4 §4.29](../../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md), [M6 §6.38](../../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md), and [M9 §9.40](../../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md) connect the calculations to a five-step argument exercise.

## Inputs, Units, and Comparisons

`price_models.py` specifies a population with two equally common groups, one offer per customer, and prices of $10 or $20. Group A historically receives $10; group B receives $20. The price-response model assigns purchase probabilities of 0.8 and 0.4 at those prices to both groups. The selection model assigns 0.8 to group A and 0.4 to group B at either price. Both reproduce the complete historical joint distribution of group, price, and purchase. The counterfactual assigns one common price to the same population while preserving product, information, availability, and each model's response rule. Raising that common price from $10 to $20 changes population purchase probability by −40 or 0 percentage points. These are population constructions with no sampling error, fitted coefficients, or external data.

`valuation_sensitivity.py` compares purchase probabilities `(0.4, 0.3, 0.2, 0.1)` with `(0.45, 0.2, 0.2, 0.15)`. Every customer purchases one of four products. Monetary consumption values are `(100, 2, 1, 0)` or `(100, 99, 98, 0)` dollars per customer. Both value systems have the same strict ranking and endpoints. Prices and other burdens are common across the two procedures; incremental procedural cost is zero. The consumption gains are +$4.80 and −$4.90 per customer. The program also accepts a separately specified incremental cost. These values are assumptions for a welfare comparison, not values estimated from purchases or inferred consent.

## Reproduction

Python 3.9 or later and its standard library are sufficient. No installation, network connection, credentials, or random seed is needed. From the repository root:

```sh
python3 03_Data_and_Code/Analytical_Arguments/price_models.py
python3 03_Data_and_Code/Analytical_Arguments/valuation_sensitivity.py
python3 -m unittest discover -s 03_Data_and_Code/Analytical_Arguments -p 'test_*.py'
python3 03_Data_and_Code/Analytical_Arguments/build_figures.py
python3 scripts/check_lecture_code.py
```

The complete analytical programs appear verbatim in M6 §6.38 and M4 §4.29. The figure builder reads the saved output tables and writes the two numerical TikZ sources. The separate argument diagram is editable directly. [Verification](VERIFICATION.md) records the checks run and their scope.

## Output Dictionary

| File in `results/` | Rows and Fields |
| --- | --- |
| `observed_purchase_law.csv` | Four group–purchase cells. `price_usd` is the historical offer; `population_mass` is the unconditional population probability. The common law applies to both models. |
| `conditional_purchase_rules.csv` | Eight model–group–price cells. `purchase_probability` is conditional on the named group and assigned price; `historically_observed` marks prices in each group's historical support. |
| `policy_effects.csv` | Two models. `purchase_at_10` and `purchase_at_20` average over equal group weights; `effect_pp` is 100 times the high-price probability minus the low-price probability. |
| `purchase_and_value_inputs.csv` | Four ordered products. Probabilities sum to one in each procedure. `cumulative_change_pp` is the alternative-minus-baseline change in probability of purchasing among the first k products, in percentage points. Two value columns give USD per purchased product. |
| `valuation_comparisons.csv` | Two value systems. Expected values, consumption gains, incremental costs, and net gains are USD per customer; gains subtract the baseline. |

## Interpretation and Provenance

The examples use exact rational arithmetic before CSV export. Observational equivalence is relative to the stated historical support. A new randomized comparison within groups would distinguish the two specified response models, subject to implementation and sampling uncertainty. A mathematical counterexample establishes failure of an entailment; it estimates neither the prevalence of the alternative mechanism nor actual consumer harm.

The valuation example separates an ordinal ranking from cardinal distances. Mixed cumulative purchase changes allow different signs under different ordered value systems. Customer permission, informed consent, and the reasons supporting a practice require their own evidence and argument.

The [reading guide](../../01_Resources/15_Marketing_Dialectics/08_Logic_and_Analytical_Arguments/README.md) attributes the philosophical and causal concepts. The numerical examples are original course constructions. No private research manuscript or third-party microdata is included. [Optional ungraded practice](../../07_Labs/Philosophical_Arguments/README.md) applies the same reasoning to pricing, mHealth, and electricity claims.
