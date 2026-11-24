# Cancellation Evidence Dictionary

All inputs are synthetic. The observation unit in the roster is a subscription; the event file may contain repeated event rows. Counts of requests, events, accounts, and subscriptions have different denominators.

| Field | Meaning and Units |
| --- | --- |
| `synthetic` | True identifies invented inputs. |
| `cutoff` | Inclusive reporting cutoff, ISO timestamp with UTC offset. |
| `subscription_id` | Unique subscription identifier; the complete reporting population has four entries. |
| `account_id` | Invented customer account attached to a subscription. No person-level identity is claimed. |
| `event_id` | Event identifier; exact copies collapse to one, conflicting copies are all rejected. |
| `kind` | `request`, `confirmation`, or `active_observation`. |
| `at` | Recorded event time with UTC offset; null fails the timestamp requirement. |
| `request_id` | A confirmation's reference to an accepted request for the same subscription. |
| `evidence_state` | Latest accepted confirmation or active observation, simultaneous conflict, request without confirmation, or unknown. |
| `state_observed_at` | Time of the latest accepted state observation; null when no such observation exists. |
| `requests_to_review` | Accepted requests without an accepted confirmation by the cutoff. |
| `flags[].rows` | Number of raw rows accounted for by a flag. Extra duplicate rows are flagged separately from the retained event. |
| `classification_trace` | Explicit mapping of each accepted event kind to a modeled class and the common parent `ServiceRecord`. |
| `confirmed_share` | Subscriptions whose latest accepted state is a cancellation confirmation divided by all roster subscriptions. |
| `request_as_completion_share` | Subscriptions with any accepted request divided by all roster subscriptions; deliberately misleading completion measure. |

The latest accepted state describes available records. A later unobserved event may change the actual state. Null timing prevents an event from entering the cutoff comparison. Event types are operational modeling choices, not verified evidence of consent, legal compliance, or actual service execution.
