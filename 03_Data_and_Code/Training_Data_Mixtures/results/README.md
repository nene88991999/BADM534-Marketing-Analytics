# Expected Results

## Exact Synthetic Ridge Model

The [mixture table](mixture_comparison.csv) contains 261 comparisons. With 5,000 Source A examples, matched task features, and penalties 50 and 1,500, the no-clean benchmark has task contribution 0.958466 and tag contribution 0.031949. Adding 100,000 Source B examples changes them to 0.011401 and 0.760461. With unrelated Source B examples, both contributions remain at their no-clean values.

The source-count and fixed-total designs are separate. The two-by-two normal equations match the closed form. The exact interior optimum at fixed total includes the finite penalty term; the zero-similarity case has no interior optimum. These values describe an imposed noiseless model in score units, not language-model response rates.

## Imposed Customer-Service Outcomes

The [context table](service_contexts.csv) reports 950/1,000 correct resolutions for each version. Original success is 95% in every context. The combined version succeeds on 882/900 product requests, 60/80 refunds, and 8/20 cancellations. The [paired changes](paired_changes.json) contain 27 recoveries and 27 regressions.

The combined version lacks 15 responses. Its success rate among received responses is 950/985, or 96.45%; its success rate per attempt remains 95%. Cancellation is 8/15 among responses and 8/20 among attempts. The same fixed request roster supports every version comparison.

## Recomputed Published Aggregates

The [checkpoint table](published_checkpoints.csv) preserves each run's final and peak rates. The constructed-only German condition has a zero final mean. Adding 100,000 clean examples gives a 72.0% final mean and an 86.67% mean of per-run peaks. At a 30% constructed share of 30,000 total examples, final values 54%, 54%, and 68% average 58.67%; peaks 66%, 58%, and 82% average 68.67%. The published main figure uses the final checkpoint.

The [condition table](published_conditions.csv) reconstructs 51 means. At a 20% constructed share, trained-trigger, approximate-trigger, and ordinary-assistant rates are approximately 15.71%, 9.52%, and 4.52%. These are selected-checkpoint, judge-defined rates in the source experiment. Recalculation verifies stored arithmetic and definitions; it does not reproduce training or validate the judge.
