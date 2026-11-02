# Recommendation Systems and Customer Goals

By Nathan Yang

Session 12. M7. 170 minutes.

[PDF](S12_Recommendation_Systems_and_Customer_Goals.pdf) | [LaTeX](S12_Recommendation_Systems_and_Customer_Goals.tex) | [Session Plan](SESSION_PLAN.md)

## Learning Objectives

- Define candidate generation, scoring, and ranking.
- Evaluate top-k recommendations on an appropriate history and denominator.
- Compare relevance, novelty, customer goals, and explanation accuracy.

## Related Materials

- [M7 lecture notes](../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md)
- [Runnable small examples](../03_Data_and_Code/Lecture_Examples/session_examples.py)
- [mHealth recommendation program](../03_Data_and_Code/mHealth/recurring_examples/m07.py)
- [Ethics and regulation](../06_Lecture_Notes/ETHICS_AND_REGULATION.md)

## Slide 1: Recommendation Systems and Customer Goals

Marketing Analytics. By Nathan Yang.

## Slide 2: A Returning-Customer Decision

- An mHealth user returns to log a meal.
- The system chooses among eligible categories using earlier histories.
- The objective may include familiar relevance and a stated variety goal.

The next logged basket differs from the next item row. A basket can contain several relevant categories. Availability and the customer's goal constrain which recommendations are useful.

Source: M7, Section 7.15, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 3: The Candidate Set

- Candidate generation determines what can be recommended.
- Scoring compares eligible items using current information.
- Ranking chooses order and applies list constraints.

A strong ranking model cannot recover an item excluded during candidate generation. Evaluation must retain the candidate-set definition as well as the ranked output.

Source: M7, Section 7.10, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 4: Recommendation Models

- Content models compare item attributes and customer histories.
- Collaborative models learn patterns across customers and items.
- Popularity and personal-frequency rules provide useful baselines.

A content model can help with new items that lack interactions. A collaborative model benefits from shared behavior but faces cold-start and selected-exposure problems.

Source: M7, Section 7.10, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 5: Histories Must Precede the Basket

mHealth evaluation freezes histories and candidate sets at the forecast origin.

**Figure description:** Training histories precede validation and test baskets. Later outcomes do not define candidate eligibility or tune the final model.

[Editable TikZ](../06_Lecture_Notes/figures/M07_mhealth_timing.tex)

Returning-user prediction can use the user's earlier history while holding out later baskets. The distinction is temporal rather than necessarily a complete user holdout.

Source: M7, Section 7.15.1, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 6: Recall Among Relevant Categories

Let $L_i$ be the top-k list and $B_i$ the categories in the next observed basket.

$$
\operatorname{Recall@k}_i=\frac{|L_i\cap B_i|}{|B_i|}
$$

The denominator is the number of relevant basket categories for that user-event.

Report how empty baskets and unavailable categories are handled. Average per event or per user according to the target population, and retain the chosen weighting rule.

Source: M7, Section 7.11, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 7: Position Matters

Discount lower-ranked relevant items when their positions affect exposure.

$$
\operatorname{DCG@k}=\sum_{r=1}^{k}\frac{2^{\mathrm{rel}_r}-1}{\log_2(r+1)}
$$

NDCG divides by the best attainable DCG for the same relevance labels.

NDCG depends on the candidate set and relevance definition. Unobserved engagement is not necessarily a negative preference label because exposure is selective.

Source: M7, Section 7.11, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 8: Basket Associations

- Support counts how often items occur together.
- Confidence conditions on the antecedent item.
- Lift compares confidence with the consequent's marginal prevalence.

Association rules are descriptive. A positive lift can reflect common meal occasions or other causes rather than a response to recommendation. Evaluate rules on later baskets.

Source: M7, Section 7.17, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 9: Lift Changes the Baseline Comparison

mHealth basket rules use distinct baskets and future validation.

**Figure description:** The chart compares rule confidence with a marginal-prevalence benchmark. Common items can have high confidence with little lift.

[Editable TikZ](../06_Lecture_Notes/figures/M07_basket_lift.tex)

Counting item rows instead of distinct baskets changes the denominator and can inflate associations through repeated entries.

Source: M7, Section 7.17, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 10: Relevance and a Customer Goal

Combine relevance $s_j$ with a goal score $g_j$ using an explicit weight.

$$
v_j(\alpha)=(1-\alpha)s_j+\alpha g_j
$$

The scores need a comparable scale before the weight has a clear interpretation.

A goal score should reflect a defined customer objective and validated measurement. The weight does not become a preference estimate merely because a programmer sets it.

Source: M7, Section 7.12.1, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 11: Small Weight Changes Can Change the First Item

Synthetic item scores. Relevance and goal scores stay fixed.

**Figure description:** A ranks first at low goal weights, B in a middle range, and C at high weights. The maximizing item switches at crossings even though each score changes smoothly.

[Editable TikZ](../06_Lecture_Notes/figures/M07_goal_blend.tex)

A recommendation can be discontinuous in a tuning weight. Sensitivity analysis should report the ranking itself, not only smooth average scores.

Source: M7, Section 7.12.1, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 12: A Three-Item Basket Check

The list contains A, B, and C. The basket contains A and C.

```python
from math import log2
ranked = ['A', 'B', 'C']
relevant = {'A', 'C'}
recall = len(set(ranked) & relevant) / len(relevant)
dcg = sum((x in relevant) / log2(r+2)
          for r,x in enumerate(ranked))
ideal = 1 + 1/log2(3)
assert recall == 1.0
```

Recall is 1.0, while NDCG is about 0.920 because B occupies the second position.

The calculation uses binary relevance. It assumes all relevant items are eligible and that the observation window defines a valid basket.

Source: M7, Section 7.11, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 13: LLM Explanations

- Explain a recommendation using verified item attributes.
- Check whether stated reasons are factually supported.
- Evaluate explanation effects separately from ranking quality.

An explanation can sound plausible while inventing a nutritional property or claiming a nonexistent personal preference. Factual support and behavioral effects require distinct evaluations.

Source: M7, Section 7.13, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 14: Offline and Online Outcomes

- A hit in a historical basket measures predictive overlap.
- A recommendation changes exposure and may change behavior.
- A randomized policy comparison measures the intervention outcome.

A historically unrecorded category can be unknown rather than disliked. Offline metrics are informative under their measurement conditions but do not identify the effect of displaying a new list.

Source: M7, Section 7.15, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 15: Coding Exercise: Ranking With a Goal

- Compare popularity and personal-frequency baselines.
- Tune the goal weight on validation baskets.
- Evaluate the fixed choice on later baskets.
- Audit one generated explanation against item attributes.

Run ../03_Data_and_Code/Lecture_Examples/session_examples.py S12 for the NDCG check. The full mHealth m07.py program defines the candidate and basket windows. Preserve the final test period for evaluation.

Source: M7, Section 7.14, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md

## Slide 16: Customer Control of Recommendations

- A customer can accept a suggested goal or reject it.
- Factual explanations should distinguish evidence from an inferred preference.
- Evaluate whether the interface respects a revised goal.

A nominal control that does not affect the recommendation can leave the customer unable to change the policy. A recommendation audit should record both the chosen setting and its implemented effect.

Source: ETHICS_AND_REGULATION.md, M7.

## Slide 17: Recommendation Discussion

- Which relevant item was excluded before scoring?
- Whose goal determines the ranking weight?
- What evidence would show improved customer experience?

The full policy includes eligibility, ranking, explanation, and updates after use. A useful evaluation identifies which component changed.

Source: M7, Section 7.12, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md
