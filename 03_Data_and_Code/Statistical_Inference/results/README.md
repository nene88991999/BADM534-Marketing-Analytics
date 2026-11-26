# Executed Statistical Comparisons

The mHealth tables describe observed May-to-June logging in the fixed 340-user cohort. The mean change is -5.123 pp; paired-user uncertainty gives a standard error of 1.379 pp, a Student interval of [-7.835, -2.411] pp, and p=0.000237. The independent-day comparison reports 0.663 pp and p=1.13e-14. These calculations share the same point estimate and differ in their treatment of dependence.

The store tables are synthetic. For 4,000 experiments at each correlation:

| Within-Store Correlation | Customer-Row Rejections | Store-Mean Rejections |
| ---: | ---: | ---: |
| 0.0 | 208 / 4,000 | 199 / 4,000 |
| 0.1 | 968 / 4,000 | 198 / 4,000 |
| 0.3 | 1,796 / 4,000 | 188 / 4,000 |
| 0.5 | 2,200 / 4,000 | 191 / 4,000 |

The first experiment at correlation 0.3 estimates $4.334 per customer. The customer-row p-value is 0.0287 and the store-mean p-value is 0.3446. Its full customer table is retained, and the dataset was not selected on its significance. Every customer has zero true effect in the simulation.

See the [dictionary](../DATA_DICTIONARY.md) for units, denominators, and interval definitions. No AI model output is included in these results.

## Statistical Claims and Decision Comparisons

The additional p-value simulation produces 32.515% rejection with 40 stores and 86.550% with 160 when the true effect is eight dollars. The hypothetical campaign has p=0.01868 and estimated contribution of minus $0.06 per treated customer. Equivalence examples distinguish an imprecise nonsignificant result from precise small effects and one-sided improvement.

The reported-table electricity calculation yields estimate $1.749/MWh, SE $1.059/MWh, two-sided 95% interval [-0.326, 3.825], and one-sided 95% upper bound $3.491/MWh at the stated reference exposure. Power is 15.675% for $1 and 47.167% for $2. The cloud-owner slope is reported separately in dollars/MWh per exposure percentage point. All inputs, denominators, and approximations are in the [data dictionary](../DATA_DICTIONARY.md). These are original calculations from reported summaries and hypothetical examples; no original utility-panel replication is claimed.

## Inverse Power and Counterexamples

For the residential reference precision, the positive departures giving 50%, 80%, 90%, and 95% power are 2.075, 2.967, 3.432, and 3.817 USD/MWh. The fixed test size is 5%. The four-owner 80% threshold is 0.448 USD/MWh per exposure pp; the sales threshold is 1,381 quarterly MWh per added MW. These thresholds use Donald W. K. Andrews's inverse-power approach within a fixed Gaussian/Wald approximation.

In the synthetic joint test, two independent estimator SEs of 0.50 and 2.00 USD/MWh yield A-only and B-only 80% thresholds of 1.552 and 6.208. Equal increases of 1.506 on both outcomes also attain 80% joint-test power. The covariance is hypothetical.

The synthetic linear and threshold response functions agree throughout the assumed historical interval [0, 1], but give 4 and 14 USD/MWh at normalized load 2. Hypothetical totals of 1,000/10 and 1,100/11 both give 100 USD/MWh, while 1,000/8 gives 125. These constructions establish failures of general inference; they describe no actual utility.

## Institutional Counterexamples

The four `institutional_*.csv` files are synthetic. They preserve monthly bill denominators, MW versus MWh, three project states, fixed donor weights, and annual cost-recovery units. A USD 10/MWh completed-project increase and USD 6 weighted donor increase produce a USD 4 change difference. The unprotected annual-recovery scenario gives USD 8/MWh; enforceable contributions or disallowed recovery change that result. These files contain no observed utility or household records.
