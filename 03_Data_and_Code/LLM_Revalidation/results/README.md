# Revalidation Results

## Published Claim Snapshot

The [summary](snapshot_summary.json) reproduces 50 claims, twenty models, and 1,000 pairs, including eight flagged unreliable comparisons. The [verdict table](verdicts.csv) has 22 expired, seventeen weakened, eight persistent, and three strengthened claims.

The mean of 15.75 months and median of 14.65 months condition on the 22 expired claims. The [follow-up estimates](horizons.csv) instead retain all fifty claims and right-censor the other 28: 4.0% expired by six months, 16.0% by twelve months, and 38.9% by twenty-four months. [Individual times](lifetimes.csv) and the [displayed curve](followup_curve.csv) preserve the calculation. Estimated dates are treated as fixed, so these outputs do not propagate their uncertainty.

[Model-level counts](model_counts.csv) preserve the reliable denominator. [Citation observations](citation_fabrication.csv) retain all twenty model-specific results for C11, including exceptions to the fitted overall category. These are measurements under the source protocol, not a current model recommendation.

## Constructed Comparisons

The [judge matrix](judge_comparison.json) gives a 17-point difference when both generator and judge change together. Comparing generators within either judge gives two points. The 15-point shift in judging the old outputs explains the difference in this imposed example.

The [100 paired cases](synthetic_cases.csv) produce an [accuracy increase](upgrade_summary.json) from 78% to 86%, with fourteen recoveries and six regressions. Routine accuracy rises from 60/80 to 72/80; consequential accuracy falls from 18/20 to 14/20. At stipulated failure costs of $1 and $20, aggregate loss increases from $60 to $128. The loss comparison reverses when the consequential-to-routine cost ratio crosses three. These figures describe constructed cases only.

Commands, assumptions, source provenance, and test scope appear in the [example guide](../README.md).
