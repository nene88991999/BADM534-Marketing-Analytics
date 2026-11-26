# AI Experimentation and Pricing

The example compares the revenue-maximizing uniform price, group-specific profit-maximizing prices, and discounts capped at the uniform benchmark. It uses an entirely imposed population and analytically integrates demand and customer surplus. Sixty percent of customers benefit under unrestricted segmentation even though total customer surplus falls. Restricting the same personalization to discounts improves both profit and customer surplus in this particular population.

## Inputs, Units, and Assumptions

[evaluate_pricing.py](evaluate_pricing.py) specifies two groups. Group L has population share 0.6 and dollar valuations uniformly distributed over [6, 10]. Group H has share 0.4 and valuations over [10, 30]. Each person has one purchase opportunity and buys when valuation exceeds the offered price. The outside option and marginal cost are zero. Prices depend on group, which is observed; individual valuation remains unobserved. These assumptions are teaching inputs and are unrelated to the empirical samples in the cited papers.

All expected profits and surplus measures use the full eligible population, including nonbuyers. `strictly_better_share` and `strictly_worse_share` compare each person's dollar surplus with the same population under the optimal uniform price. Group membership carries no demographic or vulnerability interpretation. Monetary surplus is a model outcome; it does not measure Kantian autonomy or establish an ethical verdict.

[published_aggregates.json](published_aggregates.json) separately transcribes rounded summary values from *Causal Alignment*, Table 2, and *Personalized Pricing and Consumer Welfare*, Table 7. Its source, version, observation unit, and restrictions are recorded for each series. No individual experimental observations are available here. Calculations using these summaries reproduce arithmetic, not the authors' estimation or uncertainty.

## Reproduction

Use Python 3.10 or later with the standard library. No package installation or external service is required.

```sh
python3 03_Data_and_Code/AI_Experimentation_and_Pricing/evaluate_pricing.py
python3 -m unittest discover -s 03_Data_and_Code/AI_Experimentation_and_Pricing -p 'test_*.py'
```

[results.json](results.json) records exact fractions and decimal values. Expected profit and customer surplus per eligible customer are approximately $6.0167 and $6.4750 under uniform pricing, $8.1000 and $3.4500 under segmentation, and $6.1333 and $6.6667 under capped discounts. The uniform optimum is $19/3. Group optima are $6 and $15. Five tests check independent exact totals, distributional incidence, the discount comparison, valuation-support boundaries, and invalid inputs.

The full program appears in [Marketing Dialectics, Section 9.17](../../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md). The [research and policy guide](../../01_Resources/16_AI_Experimentation_and_Pricing/README.md) separates reported evidence, interpretation, and policy status. The calculation is original course material; it does not execute the authors' software or reproduce their experiments.

## Individual Reasons, Kantian Critique, and Antitrust Evidence

Five complete programs accompany M6 §6.37, M4 §4.28, and M9 §§9.34–9.39:

```bash
python3 03_Data_and_Code/AI_Experimentation_and_Pricing/assess_personalized_pricing.py
python3 03_Data_and_Code/AI_Experimentation_and_Pricing/evaluate_targeted_experiment.py
python3 03_Data_and_Code/AI_Experimentation_and_Pricing/compare_demand_completions.py
python3 03_Data_and_Code/AI_Experimentation_and_Pricing/reconstruct_competitive_targeting.py
python3 03_Data_and_Code/AI_Experimentation_and_Pricing/compare_pricing_damages.py
python3 -m unittest discover -s 03_Data_and_Code/AI_Experimentation_and_Pricing -p 'test*.py' -v
```

Python 3.10+ and the standard library suffice. Run from the repository root. The first two programs import the adjacent `evaluate_pricing.py`; the competitive reconstruction reads the adjacent `competitive_payoffs.json`. The other inputs are stated in the programs. Outputs are in `scanlon_results/` and are overwritten deterministically.

Expected results are H's $8.0417 expected loss under segmented pricing; a $2.0833 correctly weighted revenue effect versus a $3.5985 naive difference; demand completions with population surplus changes −$1.682 and +$0.682; behavioral targeting as the sole pure equilibrium of the rounded published game; and an illustrative $1,840 invoice difference versus $1,040 revenue growth. The [data dictionary](SCANLON_DATA_DICTIONARY.md) defines the denominators and distinguishes synthetic inputs from published model outputs.

The [philosophical source assessment](../../01_Resources/16_AI_Experimentation_and_Pricing/SCANLON_ASSESSMENT.md) preserves the original papers' contrary findings and strongest responses. The [antitrust guide](../../01_Resources/16_AI_Experimentation_and_Pricing/ANTITRUST_AND_REASONS.md) records legal sources and document status. [Optional practice](../../07_Labs/Scanlon_Pricing/README.md) requires supported premises and a feasible alternative. The 14 new checks and five existing pricing checks pass; the [verification record](SCANLON_VERIFICATION.md) states their scope.
