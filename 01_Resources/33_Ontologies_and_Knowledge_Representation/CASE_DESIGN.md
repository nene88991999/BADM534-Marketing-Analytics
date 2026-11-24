# Cancellation Records and Customer Intent

## Managerial Decision

A subscription business needs to identify cancellation requests that still require a response. Students define an account, a subscription, a request, a confirmed cancellation, and a subscription state at a particular time. The observation unit for service performance is a request; the unit for a customer-state report is a subscription at the reporting cutoff. Joining these objects without preserving their units can count one customer several times or treat a request as a completed action.

## Proposed Sequence

1. Give students a small, explicitly synthetic set of subscriptions and events. Include a request awaiting confirmation, a confirmed cancellation, an active subscription, and a subscription with no recent status observation.
2. Ask them to define relations such as `requestConcernsSubscription`, `submittedByAccount`, and `confirmedAt`. Require stable identifiers and timestamps.
3. Ask what follows from each recorded relation. A request concerning a subscription establishes its subject; it does not establish completion. Missing confirmation remains unknown unless a stated completeness assumption warrants a different interpretation.
4. Compare two AI-generated specifications. One equates a request with cancellation; the other preserves the distinction. Students trace the resulting difference in the service queue before writing a larger program.
5. Add validation for duplicate request identifiers, missing timestamps, and confirmation preceding the request. Retain both source records and an explanation of each finding.
6. Challenge an axiom that treats any purchaser as authorized for promotional contact. Students identify the missing evidence and specify an explicit permission record with its scope and time.

This is a proposed original exercise. Synthetic records and executable Python would be released together with the detailed lecture example. No legal entitlement is inferred from the illustrative commercial categories.

## Recurring Course Cases

| Case | Objects and Relationships to Preserve | Question That Exposes a Modeling Error |
| --- | --- | --- |
| mHealth | Person, day, logging event, food entry, nutrient amount, and measurement unit | Does a day with no log establish zero consumption? |
| Restaurant Availability | Store, timestamped status observation, source, and observation age | Does an unavailable menu item establish a mechanical failure? |
| Earnings Calls | Speaker, attributed claim, source passage, reporting period, and company | Does management's explanation identify a causal effect? |
| Customer Segmentation | Customer, measurement period, membership rule, and segment description | Can loyalty and price sensitivity coexist under the definitions? |

These questions reuse existing distinctions in the notes. The ontology exercise makes the relevant definitions explicit and traceable rather than creating new empirical findings.

## Figures and Interaction

An editable TikZ diagram can show an account linked to a subscription, then to a request and a separate confirmation event. Solid arrows denote recorded links; dashed arrows denote permitted inferences. Navy, orange, text labels, and line patterns distinguish the categories. A second panel changes only the request-to-completion rule and shows the resulting service queue. A text table lists every fact and inference.

For a future static wiki, let students select a rule, predict its consequence, and reveal the proof. Keep the original evidence visible when a rule changes. The implementation should distinguish recorded facts, logical consequences, validation findings, and unresolved observations. An inference's derivation describes why it follows from the model; its source record supports whether its premise is credible.
