# Demand Information, Pricing, and Consumer Surplus

Two restaurants choose prices for substitutable meals. The comparison changes their pricing objective and the accuracy of a common demand signal separately. The calculation identifies how each change affects quantity, profit, and consumer surplus in a synthetic market.

## Inputs and Interpretation

[parameters.json](parameters.json) specifies demand intercepts of 10 and 14 with equal probability, marginal cost of $2 per meal equivalent, substitution coefficient 0.5, and signal accuracies 0.5, 0.75, and 1. Quantities are continuous meal equivalents per market-day. The own-quantity coefficient in inverse demand is normalized to one dollar per meal-equivalent squared. There are two symmetric restaurants and no capacity constraints, fixed costs, vendor fees, or income effects. Customers observe actual demand and posted prices. Firms observe only the common signal before setting prices simultaneously.

Independent pricing solves each firm's conditional profit problem taking the rival's price as given. Joint pricing maximizes the sum of the two firms' conditional profits. Shared knowledge of the signal does not impose a pricing agreement in the independent benchmark. The quadratic-utility model supplies consumer surplus in dollars; total welfare sums that surplus and the two firms' profits within this specified economy.

[M4 §4.26](../../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md) gives the derivation and full Python listing. The [source review](../../01_Resources/37_Pricing_Systems_and_Competition/SOURCE_REVIEW.md) connects the original model to the Wendy's case and Harrington's separate theoretical results. No actual prices, transaction records, customer observations, or liability estimates are used.

## Run

Python 3.10 or later; standard library only. No installation or network access is needed. From the repository root:

```bash
python3 03_Data_and_Code/Pricing_Competition/evaluate_market.py
python3 -m unittest discover -s 03_Data_and_Code/Pricing_Competition -p 'test_*.py' -v
python3 03_Data_and_Code/Pricing_Competition/build_figures.py
```

The program enumerates every positive-probability state-signal pair using exact fractions. CSV files contain decimals to ten places, while [exact_results.json](results/exact_results.json) retains rational results. There is no random sampling, seed, parameter fitting, or downloaded code execution. Alternative inputs can be passed with `--parameters`; the program rejects inputs that violate its stated support. The numerical equilibrium checks cover the released parameters.

## Results and Verification

[policies.csv](results/policies.csv) contains six policy rows, and [state_outcomes.csv](results/state_outcomes.csv) contains twenty probability-weighted cells. [The data dictionary](DATA_DICTIONARY.md) defines every field. [The result guide](results/README.md) reports the four endpoint comparisons and explains the difference between state-weighted posted prices and quantity-weighted paid prices.

Nine tests verify exact benchmark arithmetic, conditional probabilities, consumer optimization, surplus identities, price deviations including quantity corners, the independent-products case, information comparisons, and invalid inputs. [VERIFICATION.md](VERIFICATION.md) records the commands and scope. The editable Illinois-color welfare figure is regenerated from the results. The separate case diagram distinguishes reported data capability from alleged pricing authority.

Full guided practice is in the [optional ungraded lab](../../07_Labs/Pricing_Competition/README.md).
