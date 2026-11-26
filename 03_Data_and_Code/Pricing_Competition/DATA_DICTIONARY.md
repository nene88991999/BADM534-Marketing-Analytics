# Synthetic Pricing Data Dictionary

## Population and Timing

One synthetic market has two symmetric restaurants and a representative consumer with quasi-linear preferences. Each market-day has one equally likely low or high demand state. A common binary signal matches the state with probability `accuracy`. Firms observe the signal and choose prices; customers then choose quantities using actual demand. Results average over every state-signal pair with its stated probability.

## Parameters

`a_low` and `a_high` are inverse-demand intercepts in dollars per meal equivalent. `cost` is constant marginal production cost in the same units. `substitution` is the cross-quantity coefficient relative to the normalized own-quantity coefficient. The latter equals one dollar per squared meal equivalent. All parameter values are stipulated. No parameter describes a particular restaurant company.

## Output Fields

| Field | Definition and Units |
| --- | --- |
| `objective` | `independent`: each firm maximizes its own conditional profit; `joint`: their summed conditional profit is maximized |
| `accuracy` | Probability that the binary signal equals the true state, from 0.5 to 1 |
| `state`, `signal` | Actual and observed low/high labels; cell output only |
| `probability` | Joint state-signal probability, summing to one for each objective and accuracy |
| `actual_a` | Realized demand intercept, dollars per meal equivalent |
| `expected_a` | Conditional expected intercept given the signal, dollars per meal equivalent |
| `price` | Common posted price, dollars per meal equivalent; policy output averages across states and signals without quantity weights |
| `quantity` | Total quantity at both restaurants, meal equivalents per market-day |
| `profit` | Sum of both restaurants' profits, dollars per market-day |
| `consumer_surplus` | Utility net of expenditure and numeraire, dollars per market-day |
| `total_welfare` | Consumer surplus plus the two firms' profits, dollars per market-day |
| `expenditure` | Total customer expenditure, dollars per market-day |
| `forecast_mse` | Squared demand-intercept forecast error; policy output reports its expectation in squared dollars per squared meal equivalent |
| `paid_price` | Expected expenditure divided by expected total quantity, dollars per meal equivalent; policy output only |

Policy columns other than `paid_price` are probability-weighted expectations of the cell columns. The two restaurants have the same price in every cell, so the state-weighted mean also equals an equally restaurant-weighted mean. `paid_price` generally differs because more meals can be sold in some states. Empty or excluded cells represent zero probability, never a missing price.
