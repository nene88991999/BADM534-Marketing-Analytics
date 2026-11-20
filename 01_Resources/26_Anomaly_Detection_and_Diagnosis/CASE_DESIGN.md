# Diagnosing a Fall in Completed Purchases

A retailer must choose among changing a campaign, repairing checkout, replenishing inventory, and investigating its measurement system. Fewer recorded purchases can accompany each situation. A useful investigation first determines which observations are unusual, then evaluates the evidence for the proposed intervention.

## Constructed Incidents and Available Information

The [original course panel](../../03_Data_and_Code/Anomaly_Diagnosis/README.md) contains one observation per store and minute. It includes visits, checkout attempts, completed payments, payment latency, stock availability, support contacts, and collection completeness. The [data dictionary](../../03_Data_and_Code/Anomaly_Diagnosis/DATA_DICTIONARY.md) defines counts, rates, denominators, and elapsed time. Three separate episodes impose a payment-service interruption, a demand increase after a campaign, and a collection failure. Normal periods retain a known within-day pattern. A separate evaluation table records the imposed cause and event boundaries.

The cause is known by construction, allowing evaluation under specified mechanisms. The event frequencies and effect sizes are imposed illustrations. They do not estimate their frequency or magnitude in a retailer's operations. The existing restaurant and mHealth examples can supply separate interpretation questions using their actual observation limits.

## Sequence of Comparisons

1. **Detect.** Fit a transparent baseline using earlier normal observations. Compare a robust deviation rule with a simple alternative. Select thresholds on a separate validation period. Report false alerts over held-out normal periods, incident recall, and detection delay on later episodes.
2. **Localize.** Compare variable scores within a predicted interval with scores within the true interval. Keep these information conditions separate. Distinguish the initiating component from outcomes that respond to it.
3. **Interpret.** Give an LLM computed summaries and a variable dictionary, with no incident labels. Require a time interval, implicated variables, a proposed explanation, observed support, alternatives, and an explicit acknowledgment when the evidence is insufficient. An alternative arm can receive selected plots of the same observations.
4. **Evaluate.** Score factual support, event timing, component identification, and unsupported causal claims separately. Check a deliberately broad predicted interval to establish what the timing metric rewards. Repeat across the constructed incident types and normal periods.
5. **Choose an Action.** Ask which additional observation would distinguish the leading explanations. Compare customer exposure and investigation costs before proposing a response. Intervention effects require either the constructed mechanism or a separately justified empirical comparison.

The two executed Python programs retain timestamps, missingness indicators, chronological splits, and a fixed seed. Their complete source appears in [M7 §§7.29–7.30](../../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md). The [saved results](../../03_Data_and_Code/Anomaly_Diagnosis/results/README.md) report detection, variable rankings, timing, and the effect of future information on missing-value treatment. Eight checks verify sample counts, information boundaries, and metric calculations. Nine evidence packets support optional interpretation practice; no LLM performance has been measured.

## Analytical Figures

The [mechanism diagram](../../06_Lecture_Notes/figures/M07_anomaly_mechanism.tex) shows a payment-service interruption leading to higher latency, lower completion, and delayed support contacts. Support contacts receive the largest mean standardized deviation even though the imposed cause is the payment service. The arrows represent the synthetic mechanism; a ranking of observed changes does not identify which intervention would repair the service.

The [timing diagram](../../06_Lecture_Notes/figures/M07_anomaly_intervals.tex) shows the true event interval alongside a precise prediction, a delayed prediction, and a full-window prediction. All three predictions overlap the event. Their interval intersection-over-union values are 1.00, 0.60, and 1/6. The panels share a time scale and combine Illinois Blue `#13294B` and Orange `#FF5F05` with distinct line styles and labels. The accompanying program reproduces overlap, intersection-over-union, and onset error.

## Customer Judgment and Organizational Responsibility

An automated diagnosis can trigger an account restriction, an unsolicited message, or a change in service. Require evidence proportionate to that consequence and a way to correct an erroneous inference. In mHealth, changed logging alone supplies no basis for inferring a medical condition or a customer's abandoned goal. In the retail case, changed purchasing alone supplies no basis for asserting misconduct. The customer can remain an informed participant in resolving an uncertain interpretation.

Session 11 devotes twenty minutes of its existing application block to the M7 case. The [longer Python lab](../../07_Labs/Anomaly_Diagnosis/README.md) is optional ungraded practice. Possible connections to M2 measurement, M5 textual claims, and M8–M9 customer interests remain suggestions. The fifteen meetings, calendar dates, and assessment requirements are unchanged.
