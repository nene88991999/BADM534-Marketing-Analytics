# Data Dictionary

All records are original synthetic teaching data. There are three online stores A–C, twelve simulation days, and observations for minutes 0–119 of each store's 09:00–11:00 window. `day=0` is January 1, 2026. Timestamps describe a synthetic local clock with no daylight-saving transition. Endpoints of event and alert intervals are exclusive. A store-minute is the observation and scoring unit; a store-day is the monitoring run.

## Observation Columns

| Field | Meaning and Units |
| --- | --- |
| `store` | Synthetic store A, B, or C |
| `day` | Integer simulation day 0–11 |
| `minute` | Minute within the two-hour run, 0–119 |
| `timestamp` | ISO local timestamp for the observed minute |
| `split` | `train`: days 0–5; `validation`: days 6–8; `test`: days 9–11 |
| `phase` | Known time-of-day block, `minute // 20`; six blocks |
| `visits` | Recorded visits during the minute, count |
| `checkout_attempts` | Recorded attempts during the minute, count |
| `completed_payments` | Recorded completed payments during the minute, count |
| `completion_rate` | Recorded completed payments divided by recorded attempts; attempts are positive throughout |
| `latency_ms` | Synthetic mean payment-service latency during the minute, milliseconds |
| `support_contacts` | Synthetic support contacts during the minute, count |
| `stock_available_share` | Available share of a fixed synthetic assortment, between zero and one |
| `collection_completeness` | Observed monitoring signal for the share of transaction records captured, between zero and one |

The two count components of `completion_rate` remain in the file for denominator checks. The detector uses six features: visits, completion rate, latency, support contacts, stock share, and completeness. It does not separately score the two payment counts. Three leading latency values for store A on day 10 are missing. Their rows remain present; `missing_features` records them in the scored output.

## Construction and Reference Values

Normal visits vary across stores and alternating 20-minute phases, with integer noise. Attempts depend on visits, payment success varies around 0.90, latency varies around 300 or 315 milliseconds, support contacts range from zero to two, stock share varies around 0.95, and completeness equals one. The program specifies these mechanisms and all random draws. The construction is a teaching mechanism, with no fitted retailer demand parameters.

For each store, phase, and scored feature, estimate a median and median absolute deviation using training rows only. Multiply the latter by 1.4826, then apply a prespecified scale floor. Floors are 2 visits, 0.02 completion-rate units, 25 milliseconds, 1 support contact, 0.01 stock-share units, and 0.02 completeness units. They prevent constant or nearly constant features from producing an undefined score. Their values affect the relative variable weights; a deviation score has no probability interpretation.

For scoring, replace a missing feature with its training-group median and retain the missing-feature count. Its standardized deviation is consequently zero. An unobserved feature then supplies no deviation signal, and a separate completeness monitor may be appropriate. No later value is used to impute an earlier row.

The threshold for each aggregation method is the 1,070th ordered score among 1,080 normal validation rows. An alert requires a score strictly greater than that threshold. This chooses an empirical upper tail while preserving ties; it gives no population false-alert guarantee under a later distribution.

## Incident Labels

`data/events.csv` supplies `store`, `day`, `start`, `end`, and the imposed `cause`. All events span [40,60). Store A on day 9 has a payment-service interruption that lowers success and increases latency. Its support response is delayed and spans [45,65). Store B on day 10 receives a campaign-induced increase in visits and attempts with the same success mechanism. Store C on day 11 loses recorded transaction counts through a collection failure; its completeness signal falls to 0.40. It retains only 40% of the constructed visit and transaction counts, rounded to integers.

The event label means a specified departure from the normal construction, including the beneficial campaign. It does not mean customer harm. A support response after payment recovery falls outside the defined failure label. The three causes are known by construction and are held out of detector fitting and scoring.

## Denominators and Outputs

`results/detection_summary.csv` evaluates all 1,080 test minutes: 60 labeled and 1,020 outside labeled intervals. `nominal_run_minutes` restricts attention to the six store-days with no imposed event at all, totaling 720 minutes. An alert minute differs from a contiguous alert episode. `nominal_alert_minutes_per_1000` counts the former; `alerted_nominal_runs` counts complete runs containing at least one alert.

`results/incident_metrics.csv` matches each true event to the first overlapping contiguous alert interval during evaluation. Detection delay is the first alert inside the true interval minus its start. A missed event has no delay or matched endpoints and receives zero interval intersection-over-union. This matching is an evaluation step; true intervals never determine alerts.

`results/variable_rankings.csv` compares mean standardized deviations within true intervals and matched alert intervals. The former uses ideal event timing. The latter uses a predicted boundary, with matching supplied by the evaluator. These are descriptive scores of observed variables, with no estimate of a causal effect.

`results/evidence_packets.json` includes every test run, its mean-rule alerts, and observed measurements. It contains no incident cause or true boundaries. [variable_dictionary.json](data/variable_dictionary.json) supplies only feature definitions for the optional LLM exercise. This document and the generator contain disclosed answers, so they are separate from the exercise's model-input packet.
