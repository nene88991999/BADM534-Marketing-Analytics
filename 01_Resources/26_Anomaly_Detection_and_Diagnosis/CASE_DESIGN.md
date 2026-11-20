# Diagnosing a Fall in Completed Purchases

A retailer must choose among changing a campaign, repairing checkout, replenishing inventory, and investigating its measurement system. Fewer recorded purchases can accompany each situation. A useful investigation first determines which observations are unusual, then evaluates the evidence for the proposed intervention.

## Constructed Incidents and Available Information

Use an original synthetic panel with one observation per store and minute. Include visits, checkout attempts, completed payments, payment latency, stock availability, support contacts, and collection completeness. Define counts, rates, denominators, and elapsed time in a data dictionary. Assign separate constructed episodes for a payment-service interruption, a demand increase after a campaign, and a collection failure. Include normal periods and a known calendar pattern. Store the imposed cause and event boundaries in an evaluation table separate from the model inputs.

This design would make the cause known by construction. It would support evaluation of a diagnostic procedure under specified mechanisms. The distribution of simulated events would not estimate their frequency in a retailer's operations. The existing restaurant and mHealth examples could then supply interpretation questions using their actual observation limits.

## Sequence of Comparisons

1. **Detect.** Fit a transparent baseline using earlier normal observations. Compare a robust deviation rule with a simple alternative. Select thresholds on a separate validation period. Report false alerts over held-out normal periods, incident recall, and detection delay on later episodes.
2. **Localize.** Compare variable scores within a predicted interval with scores within the true interval. Keep these information conditions separate. Distinguish the initiating component from outcomes that respond to it.
3. **Interpret.** Give an LLM computed summaries and a variable dictionary, with no incident labels. Require a time interval, implicated variables, a proposed explanation, observed support, alternatives, and an explicit acknowledgment when the evidence is insufficient. An alternative arm can receive selected plots of the same observations.
4. **Evaluate.** Score factual support, event timing, component identification, and unsupported causal claims separately. Check a deliberately broad predicted interval to establish what the timing metric rewards. Repeat across the constructed incident types and normal periods.
5. **Choose an Action.** Ask which additional observation would distinguish the leading explanations. Compare customer exposure and investigation costs before proposing a response. Intervention effects require either the constructed mechanism or a separately justified empirical comparison.

The exercise should retain timestamps, missingness indicators, a chronological split, seeds, dependency versions, and a record of each transformation. Detailed runnable Python belongs beside the data in `03_Data_and_Code`, with identical code in the lecture notes when the example is implemented. No numerical result or executed exercise is supplied by this design.

## Analytical Figures

An editable TikZ diagram could show a payment-service interruption leading to latency and payment failures, followed by fewer purchases and more support contacts. Mark a downstream outcome as strongly predictive while the intervention targets the payment service. The arrows would state the imposed synthetic mechanism, with the role of observations and interventions identified separately.

A second TikZ diagram could show the true event interval alongside a precise prediction, a delayed prediction, and a full-window prediction. Pair the diagram with a table of overlap, interval intersection-over-union, and onset error. All panels should use the same time scale, Illinois Blue `#13294B` and Orange `#FF5F05`, and distinct line styles or labels. This comparison makes the difference between detecting an event and localizing it visible.

## Customer Judgment and Organizational Responsibility

An automated diagnosis can trigger an account restriction, an unsolicited message, or a change in service. Require evidence proportionate to that consequence and a way to correct an erroneous inference. In mHealth, changed logging alone supplies no basis for inferring a medical condition or a customer's abandoned goal. In the retail case, changed purchasing alone supplies no basis for asserting misconduct. The customer can remain an informed participant in resolving an uncertain interpretation.

The primary placement is optional practice within Session 11, linked to M7's validation and explanation material. M2 can revisit measurement failures, M5 can evaluate textual claims, and M8–M9 can examine the response and its justification. The proposal preserves the existing 15-meeting course plan and establishes no new student requirement.
