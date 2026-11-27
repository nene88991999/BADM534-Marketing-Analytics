# Pricing Inputs and Denominators

## Synthetic Incidence and Experimental Exposure

`evaluate_pricing.py` supplies groups L (share 3/5; valuations uniform on $6–$10) and H (share 2/5; valuations uniform on $10–$30). Dollars refer to one purchase opportunity. Marginal cost and outside-option utility are zero. Groups reveal no demographic or social-advantage information.

`incidence.json` records each policy's prices, aggregate revenue/profit, customer surplus, and purchase shares. A `surplus_change_per_group_member` includes nonbuyers in that group; `population_surplus_contribution` additionally multiplies by its population share. Lost purchase shares compare the same valuations under both prices.

`experiment.json` uses invented assignment probabilities L=1/4 and H=3/4, compared with 1/2 in each group. Revenue outcomes include zeros. `ipw_policy_effect` is the eligible-population effect; `naive_difference` compares differently composed pooled arms. Expected loss is measured against always receiving control, with negative surplus changes truncated only when measuring loss rather than net gain. Exact expected cells have no empirical sampling uncertainty.

## Synthetic Demand Completions

`demand_completions.json` uses a separate population with weights L=3/5, H=2/5. Tested probabilities are L=(.9,.5,.1) and H=(.95,.8,.5) at $5,$10,$20. Each completion is a continuous monotone piecewise-linear curve, extended to probability one at zero and zero at $30. Candidate prices change from $10 for both groups to $5 for L and $20 for H. Areas under demand are money-metric surplus under the stated quasilinear assumptions. Both completions agree at all tested prices; no fitted sample or uncertainty estimate is implied.

## Published Competitive Payoffs

`competitive_payoffs.json` transcribes the published payoff table (Dubé et al., 2017, Table 9, p. 965). Rows select A's strategy, columns select B's, and each cell is [A revenue, B revenue]. Units are RMB expected revenue per messaged consumer. Decimal strings preserve the three-decimal rounding in the source. These are estimated model outputs, not observed individual transactions. The program derives pure-strategy best responses from the rounded entries and does not recover posterior uncertainty.

## Synthetic Invoice Comparison

`damages.json` uses one-period USD prices and identical service units. Its lawful counterfactual prices and quantities are assumed inputs. Signed invoice differences equal actual quantity times the paid-minus-counterfactual price; negative values are retained. This avoids silently declaring all transactions harmed. Revenue differences also reflect quantity changes. Lost consumer surplus and legal entitlement to recover damages are not identified by this accounting identity.

All exact fractional values are exported as an `exact` string and `decimal` numeric value. No model API, confidential customer record, or student information is used in these five programs.
