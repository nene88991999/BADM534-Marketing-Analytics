# Released Retail-Account Data

The unit is a released weekly observation for a retailer–market account. There are 5,555 rows across 88 accounts. The file supplies neither a date column nor household identifiers, purchases, incomes, contract terms, marginal costs, or welfare outcomes. Row order is preserved without assigning calendar dates.

| Field | Meaning and Units |
| --- | --- |
| `RETAILER` | Public retailer–market account label; grouping unit |
| `VOLUME` | Unit sales of the released Borden sliced-cheese product |
| `DISP` | Released display measure in [0,1], described as percent ACV in the upstream documentation; retained in its fractional scale |
| `PRICE` | Average price in US dollars |

`log(VOLUME)` and `log(PRICE)` use natural logarithms. The price coefficient is a conditional log-sales/log-price association. Display enters in its released scale. Two accounts have constant display and therefore use an intercept and log price only. Every account remains in the analysis; no observations are removed. Each account receives one contribution to the second-stage likelihood, with its own first-stage sampling variance. The reported mean account coefficient gives accounts equal weight.

The independent-error assumption is a working model. Missing dates limit assessment of temporal dependence; prices and promotions can also respond to demand conditions. The exercise makes conditional comparisons under these restrictions and does not treat the fitted coefficients as identified causal elasticities.

## Synthetic Precision Inputs

The precision calculation uses no rows from `cheese.csv`. It specifies independent normal group signals with SD one, zero burden for 90% of equal-sized groups, and burden two for 10%. One burden unit is $10 per person-month. The normal working prior is centered on zero; its variance determines the retained data weight. Monetary loss uses 10,000 consumers, the ten-percent harmful share, and 12 months of $20 burden when harm is missed. These inputs define an illustration rather than observations.
