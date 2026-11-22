# Conjoint and Product Design

By Nathan Yang

Session 05. M4. 170 minutes.

[PDF](S05_Conjoint_and_Product_Design.pdf) | [LaTeX](S05_Conjoint_and_Product_Design.tex) | [Session Plan](SESSION_PLAN.md)

## Learning Objectives

- Design choice tasks that identify attribute tradeoffs.
- Compute logit probabilities and willingness to pay.
- Separate new-product share from incremental category demand.
- Evaluate a synthetic concept screen using distribution fit, shortlist errors, and independent human outcomes.

## Related Materials

- [M4 lecture notes](../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md)
- [Runnable small examples](../03_Data_and_Code/Lecture_Examples/session_examples.py)
- [Ethics and regulation](../06_Lecture_Notes/ETHICS_AND_REGULATION.md)
- [AI workflow calculations](../03_Data_and_Code/AI_Workflows/README.md)
- [Synthetic Consumer Examples](../03_Data_and_Code/Synthetic_Consumers/README.md)

## Slide 1: Conjoint and Product Design

Marketing Analytics. By Nathan Yang.

## Slide 2: Customers Compare Product Bundles

![Customers compare distinct tea, fruit, and delivery offerings in a riverside market. The scene represents choice among available product bundles.](assets/product_choices.png)

Customers compare distinct tea, fruit, and delivery offerings in a riverside market. The scene represents choice among available product bundles.

Product design changes a choice set. Sales of a new bundle can replace purchases of existing bundles or attract customers who previously chose the outside option.

Source: Original conceptual illustration. 05_Slides/assets/PROVENANCE.md.

## Slide 3: A Subscription-Bundle Decision

- A firm can change quality, delivery, and monthly price.
- Customers must trade off feasible attribute combinations.
- The choice set includes the option to buy nothing.

A forced choice among paid plans estimates conditional preference. It supplies no direct category-participation margin when customers cannot opt out.

Source: M4, Section 4.1, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md

## Slide 4: Choice-Task Design

- Vary price independently of features where feasible.
- Use realistic combinations and clear descriptions.
- Retain respondent identity across repeated tasks.

Perfect correlation between price and quality prevents their separate interpretation. Repeated answers from one person are dependent, affecting estimation and validation.

Source: M4, Section 4.1, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md

## Slide 5: Utility and Price

Systematic utility combines product features and price.

$$
V_{ij}=\beta_q q_j+\beta_f f_j+\beta_p p_j
$$

Utility has an arbitrary scale. Price is measured in dollars per billing period.

Coefficients describe tradeoffs within the specified design. Alternative-specific constants and preference heterogeneity can change the appropriate model.

Source: M4, Section 4.2, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md

## Slide 6: Logit Choice Probabilities

Normalize probabilities over the alternatives available to customer $i$.

$$
P_{ij}=\frac{\exp(V_{ij})}{\sum_{k\in\mathcal J_i}\exp(V_{ik})}
$$

The denominator includes the outside option and every available product.

Probabilities sum to one within each choice set. The multinomial logit model imposes proportional substitution among alternatives. That restriction requires assessment in the category.

Source: M4, Section 4.2, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md

## Slide 7: Willingness to Pay

Under linear price utility, equate a feature gain with a price increase.

$$
\operatorname{WTP}_f=-\frac{\beta_f}{\beta_p}
$$

If $\beta_f=1.2$ and $\beta_p=-0.1$ per dollar, the tradeoff is 12 dollars.

A near-zero price coefficient makes the ratio unstable. WTP is conditional on the model, design range, and respondent population. It is not a direct forecast of revenue.

Source: M4, Section 4.2, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md

## Slide 8: Two Bundles and an Outside Option

| Option | Quality | Price | Utility |
| --- | --- | --- | --- |
| A | Premium | 10 | 0.2 |
| B | Standard | 6 | -0.6 |
| Outside | None | 0 | 0 |

Synthetic inputs: quality coefficient 1.2 and price coefficient -0.1.

The outside utility is normalized to zero. Prices and coefficients determine the utilities. The example holds the potential-customer population fixed.

Source: M4, Section 4.3, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md

## Slide 9: A Launch Redistributes Existing Sales

Synthetic logit model. New bundle C has A's modeled attributes.

**Figure description:** C obtains about 30.6% share, while category participation rises by about 11.0 percentage points. Existing bundles lose share.

[Editable TikZ](../06_Lecture_Notes/figures/M04_cannibalization.tex)

The difference between C share and incremental category demand is substitution from existing products. The logit specification makes C draw proportionally from all existing alternatives.

Source: M4, Section 4.3, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md

## Slide 10: Incremental Contribution

- Attach contribution margins to each simulated purchase.
- Compare the full product portfolio before and after launch.
- Deduct development and operating costs separately.

Under the supplied margins of 4 dollars for A and C and 3 for B, expected contribution per potential customer rises from about 2.36 to 2.86 dollars before fixed costs. These are model-based values under imposed inputs.

Source: M4, Section 4.3, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md

## Slide 11: A Probability Check

Calculate the synthetic baseline shares.

```python
from math import exp
utilities = {'A': 0.2, 'B': -0.6, 'Outside': 0.0}
weights = {k: exp(v) for k,v in utilities.items()}
shares = {k: v/sum(weights.values())
          for k,v in weights.items()}
assert abs(sum(shares.values()) - 1) < 1e-12
```

A has about 44.1% share, B 19.8%, and the outside option 36.1%.

For very large utilities, subtracting the maximum utility before exponentiation improves numerical stability without changing probabilities.

Source: M4, Section 4.3, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md

## Slide 12: Substitution Assumptions

- A close copy can draw mostly from its nearest competitor.
- Basic logit instead preserves relative odds among existing alternatives.
- Holdout choice tasks can reveal systematic substitution errors.

Nested and mixed logit models relax substitution patterns under additional structure. More flexible models still need suitable choice variation and validation.

Source: M4, Section 4.2, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md

## Slide 13: Coding Exercise: A Product Launch

- Add C to the synthetic profile table.
- Calculate portfolio share and contribution before and after launch.
- Compare C's share with the change in category participation.
- Check a case with no outside option.

Use ../03_Data_and_Code/Lecture_Examples/session_examples.py S05. With no outside option, purchase incidence is one by construction. That change should be visible in the program and interpretation.

Source: M4, Section 4.10, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md

## Slide 14: Validation and Market Transfer

- Hold out respondents or tasks according to the intended use.
- Check coding, price units, and probabilities.
- Relate stated preference to awareness, distribution, and availability.

A survey share is conditional on the experiment. Real demand also depends on who sees the offering and whether they can buy it. The demand forecast needs an explicit transfer assumption.

Source: M4, Section 4.4, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md

## Slide 15: mHealth Product Economics

- Food logs reveal recorded use and category histories.
- A paid-plan choice model needs additional price and preference evidence.
- Financial scenarios can state the missing inputs explicitly.

The lecture notes use an imposed paid-plan logit example separately from observed logs. Behavioral logging segments do not establish willingness to pay or paid subscription retention.

Source: M4, Section 4.11, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md

## Slide 16: AI-Assisted Conjoint Analysis

- Provide the choice-set identifier and the selected alternative.
- Require probabilities to sum to one within each task.
- Preserve respondent groups in validation.
- Request a portfolio comparison with explicit margins.

A code generator may accidentally normalize probabilities over the full dataset or treat repeated tasks as independent respondents. Small constructed tasks expose those errors.

Source: M4, Section 4.10, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md

## Slide 17: Synthetic Consumers in Concept Screening

- A shortlist directs the budget for human product research.
- Generated reactions can suggest benefits and objections.
- A screening claim needs evidence on new concepts and the intended customers.

Maier and coauthors compare 57 personal-care concepts with 9,300 U.S. human responses. Semantic similarity rating maps generated text to five-category distributions. The authors manually optimized the anchors on the same surveys. For GPT-4o with image stimuli and averaged anchors, the reported 90.2% correlation attainment is a ratio to a split-half human benchmark. It describes neither individual-rating accuracy nor purchase prediction. Concept ratings do not identify attribute tradeoffs without suitable variation and a response model.

Source: Maier and coauthors (2025), Table 1 and Appendix A.3. https://arxiv.org/abs/2510.08338v3

## Slide 18: Distribution Fit and Product Selection

Six synthetic concepts, 100 invented ratings each. Overall category shares match, while the preferred concepts differ.

**Figure description:** The left panel shows common overall shares of 0, 0, 22.5, 30, and 47.5 percent in categories 1–5. The right panel preserves concept A–F identity: reference means fall from 4.5 to 4.0, pooled means equal 4.25, reversed means rise from 4.0 to 4.5, and compressed means fall from 4.30 to 4.20. The right vertical scale is 3.9–4.6.

[Editable TikZ](../06_Lecture_Notes/figures/M04_concept_screening.tex)

Every candidate has the same aggregate distribution as the reference across equally weighted concepts. That pooled match removes the concept distinction needed to choose products. The reversed rule selects F and E instead of A and B. The compressed pattern preserves order while shrinking rating differences. All values are imposed teaching inputs and no human survey or fitted model is represented.

Source: M4 §4.23, M5 §5.23, and M7 §7.36. ../03_Data_and_Code/Synthetic_Consumers/README.md

## Slide 19: A Screening Rule Needs a Decision Metric

| Pattern | Mean KS | Correlation | Top Two Retained |
| --- | --- | --- | --- |
| Pooled | 0.925 | Undefined | Boundary tie |
| Reversed | 0.850 | -1.000 | 0 of 2 |
| Compressed | 0.940 | 1.000 | 2 of 2 |

Imposed comparisons on the same six concepts. A high distribution score can accompany a poor shortlist.

KS similarity is one minus the maximum cumulative-probability difference, averaged equally across concepts. Pearson compares concept means. Spearman gives the same results in this construction. Constant pooled means leave correlation undefined and every concept tied. Compressed means have a mean absolute rating error of 0.12 despite preserving the top two. The three candidates were constructed using the synthetic reference to isolate these properties, so this is an analytical comparison rather than a prospective prediction test.

Source: M4 §4.23, M5 §5.23, and M7 §7.36. ../03_Data_and_Code/Synthetic_Consumers/README.md

## Slide 20: New Concepts and Human Validation

- Separate anchor development, configuration selection, and final concepts.
- Freeze the complete measurement procedure before final human outcomes.
- Sample rejected concepts to reveal missed opportunities.

The complete procedure includes prompts, model version, generation settings, embedding, anchors, aggregation, and shortlist rule. Final concepts and human outcomes remain outside those choices. Human tests confined to the selected concepts cannot reveal promising exclusions. Known sampling probabilities for rejected concepts support population comparisons with appropriate uncertainty. Observed purchases and stated intent remain separate outcomes.

Source: M4 §4.23, M5 §5.23, and M7 §7.36. ../03_Data_and_Code/Synthetic_Consumers/README.md

## Slide 21: Customer Alternatives and AI Pricing

- Customer value depends on the offered outcome and implementation effort.
- Better tools can make internal analysis a stronger alternative.
- Lower seller costs and lower willingness to pay can occur together.

Under a quasilinear comparison, the buyer price ceiling is delivered value minus buyer burden and outside-option utility. Use a common customer and horizon. Product design can reduce integration and verification effort, while competitive improvements raise the value of the alternative. The conditional numerical comparison appears in Session 14 and M8 §8.17.

Source: Marketing Analytics Lecture Notes, M4 §4.16.

## Slide 22: Price Presentation and Customer Understanding

- A base price and a mandatory fee determine the total paid.
- A stated-choice task can reveal different responses to equivalent totals.
- The feasible pricing design depends on the applicable rule and industry.

The FTC's fee rule addresses live-event tickets and short-term lodging. Its scope should remain explicit. A response difference to fee framing does not itself authorize a particular presentation.

Source: FTC Rule on Unfair or Deceptive Fees FAQ. https://www.ftc.gov/business-guidance/resources/rule-unfair-or-deceptive-fees-frequently-asked-questions

## Slide 23: Product-Design Discussion

- How much of C's demand comes from existing products?
- Which design change would identify the price tradeoff?
- What evidence could change the launch recommendation?

The recommendation depends on substitution, incremental contribution, and costs. An appealing new-product share can coexist with little category expansion.

Source: M4, Section 4.3, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md
