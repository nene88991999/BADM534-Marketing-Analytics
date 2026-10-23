# M8. Current Topics and Integrated Marketing Decisions

A marketing team can now generate campaign copy, build a prediction model, and summarize customer feedback within a short working session. The remaining difficulty is deciding whether the resulting system improves a business decision. A recommendation engine can reproduce past exposure, a media model can attribute seasonal demand to advertising, and an AI-generated analysis can calculate an invalid comparison precisely. Evaluating these systems requires a clear account of their information, incentives, assumptions, and consequences.

## 8.1 Recommendation Systems Learn From Selected Exposure

A retailer wants to recommend products that customers will find useful. A common starting point is past interaction: purchases, clicks, ratings, or time spent. These observations combine preferences with the opportunities customers received. A product displayed prominently has more chances to be clicked than an otherwise similar product that was rarely shown. An absent interaction can therefore mean dislike, lack of exposure, lack of need, or an unavailable product.

Content-based methods use product attributes and customer histories to identify similar items. Collaborative methods use patterns across users and items, including matrix factorization, which approximates an interaction matrix with lower-dimensional user and item representations. Hybrid systems combine these sources. Each method needs a strategy for new customers and new products that have little interaction history. Popularity baselines and simple category rules provide useful comparisons.

Recommendation systems also change the data used to train the next model. A product that receives more exposure can accumulate more interactions, become easier to estimate, and receive still more exposure. This process can amplify initial differences without establishing that the repeatedly displayed product would be preferred under equal exposure.

[Chaney, Stewart, and Engelhardt (2018)](https://arxiv.org/abs/1710.11214) study this feedback through simulations in which recommendations shape the next training sample. Their results show that consumption can become more homogeneous without corresponding utility improvements. The result depends on the simulated preferences, recommendation rules, and updating process. It identifies a mechanism to examine in deployed systems rather than a universal effect of personalization.

![A recommender changes the exposure that generates its next training sample.](../figures/M08_feedback.png)

Rankings determine exposure, exposure affects observed behavior, and that behavior enters subsequent training data. Customer preferences also affect behavior, while availability and position affect the opportunity to respond. Logging impressions, positions, eligible alternatives, and the policy that selected them helps distinguish these components. Purchase logs alone often omit the alternatives a customer could actually have encountered.

Evaluate recommendation quality at the unit relevant to the decision. Precision among the top recommended items and ranking metrics assess aspects of relevance. Coverage, novelty, diversity, repeat engagement, returns, and contribution describe other consequences. A system can improve one metric while reducing another. Offline evaluation on historical logs is particularly sensitive to the policy that generated those logs. An experiment that changes exposure can supply information that a more flexible model of the same selected data cannot supply.

### 8.1.1 Case Study: A Temporary Campaign Can Change the Learned Policy

A platform may stop boosting a category while continuing to use the behavior generated during that boost. [Luo, Yao, and Zhang's 2026 working paper](https://arxiv.org/abs/2606.08265) studies a celebrity sleep-reminder campaign on a short-video platform. During the campaign, a ranking adjustment increased the chance that treated users would see a reminder during the late-night window. Exposure remained dependent on the ranking process. The analysis uses a balanced panel of 200,000 users active on the experiment's first day, with 100,000 drawn from each assignment group.

Table 6 reports assignment effects of 14.75% higher late-night usage and 2.18% higher overall app usage relative to the respective control means during the campaign. These are relative percentage changes in usage, not percentage-point changes in exposure or measured effects on sleep. The paper also reports persistent engagement changes and changes in the content delivered afterward. The authors interpret the evidence through discovery of previously underexposed preferences and subsequent recommendation updates. The experiment estimates effects of the assignment regime; attributing persistence specifically to learning requires the additional mechanism evidence. The first-day activity restriction also makes sample inclusion consequential when extending the result to all assigned users.

![A temporary ranking intervention can affect later recommendations through the training data it creates.](../figures/M08_policy_horizon.png)

The temporary boost ends, but its information can remain in the learned model. Freezing the model after the campaign would interrupt that particular channel while leaving any direct changes in customer behavior possible. Updating it incorporates the new interactions into future exposure. These policies can have different effects even when the campaign content and immediate responses are identical. Separating their contributions requires variation in the learning policy as well as the initial intervention.

An evaluation should retain the assignment, exposure, model version, retraining schedule, and outcomes after the intervention ends. A shared model can transmit treatment-generated information to comparison customers. Report the assignment unit and use uncertainty calculations that account for repeated observations of the same unit. Measure the intended customer outcome directly where possible, because increased engagement cannot reveal whether a campaign achieved a goal such as less late-night use or greater satisfaction.

### 8.1.2 Case Study: Netflix Personalization and Incremental Engagement

A streaming service wants to distinguish the appeal of its catalog from the value created by matching titles to viewers. [Zielnicki, Aridor, Bibaut, Tran, Chou, and Kallus](https://www.ifo.de/en/cesifo/publications/2026/working-paper/value-personalized-recommendations-evidence-netflix), in the supplied June 2026 paper, estimate a choice model using Netflix viewership and recommendation exposure. The model incorporates heterogeneous tastes and dependence on viewing history. Its identification treats exposure as conditionally exogenous given the included user, title, and state information. A separate randomized recommendation perturbation provides diversion patterns used to assess the model.

Under that model, replacing the current recommender with matrix factorization reduces engagement by approximately 4%, and replacing it with a popularity-based rule reduces engagement by approximately 12%. These are model-based counterfactual reductions relative to the existing recommender, not direct A/B estimates of those complete replacements. Their interpretation depends on the exposure condition, maintained choice model, and counterfactual implementation.

For a subscription business, engagement can affect retention and hence customer lifetime value, but the relationship requires evidence. A 12% engagement reduction does not imply a 12% decline in revenue, retention, or consumer welfare. Evaluate those outcomes separately, account for substitution across titles, and compare the incremental value with the cost of maintaining the recommendation system. The model's experimental check is useful because it evaluates responses to changed exposure, beyond fit to historical viewing alone.

## 8.2 Case Study: Relevance, Variety, and Customer Goals

A customer may prefer a useful collection of products even when some items in that collection have lower individual relevance scores. Category repetition, past purchases, and the customer's stated goal affect the value of the complete list. The food-recommendation studies in M7, Section 7.12, motivate these distinctions. A simple list objective makes the relevance-variety tradeoff explicit.

Suppose a retail customer requests three products and values variety across categories. Assign four candidate items the relevance scores below. The scores are comparable across these items and measure relevance rather than purchase probability.

| Item | Category | Relevance Score |
| --- | --- | ---: |
| A | Coffee | 0.90 |
| B | Coffee | 0.85 |
| C | Tea | 0.75 |
| D | Fruit | 0.65 |

Choosing the three highest scores gives A, B, and C, with total relevance 2.50 and two categories. Choosing A, C, and D gives relevance 2.30 and three categories. To make the tradeoff explicit, define a list objective

$$
J(L)=\sum_{j\in L}s_j+\lambda K(L),
$$

where $L$ is a three-item list, $s_j$ is relevance, $K(L)$ counts distinct categories, and $\lambda$ is the value placed on an additional category in the same units as the relevance score. With $\lambda=0.30$, A, B, C has objective 3.10, while A, C, D has objective 3.20. The latter list is preferred under this stated objective. The threshold at which these two lists tie is $\lambda=0.20$.

The variety weight must come from an explicit objective, user preference, or evaluation process. Category counts are also a coarse measure: they treat all category differences equally and ignore which products the customer already owns. A deployed system would need better measurements and an evaluation of whether the resulting lists improve the intended customer experience.

For an experiment, randomize eligible customers to the existing and revised recommendation policies. Choose a primary outcome such as contribution per assigned customer over a fixed horizon, alongside measures of customer satisfaction and unwanted repetition. Analyze assignment rather than only customers who clicked a recommendation. Clicking occurs after the policy is assigned and can differ between policies. Preserve the list shown and the alternatives eligible at each impression so the mechanism can be examined.

### 8.2.1 Engagement, Considered Preferences, and the Objective

A customer can click an item and later wish it had not been recommended. [Kleinberg, Mullainathan, and Raghavan](https://doi.org/10.1287/mnsc.2022.03683) model inconsistent preferences to explain why behavior alone can be insufficient for a platform seeking to improve user utility. The problem can arise even when the platform wants to serve the user: the observed action may reflect an immediate impulse that differs from a considered preference. A useful evaluation therefore combines behavior with explicit goals, satisfaction, and measures of regretted use, with their measurement limitations stated.

[Stray and coauthors (2021)](https://arxiv.org/abs/2107.10939v1) discuss recommender design around objectives such as well-being, diversity, and user control. For a retailer, a concrete formulation could maximize expected contribution subject to customer-selected spending limits, a maximum repetition rate, and a minimum satisfaction criterion. These constraints make the acceptable tradeoffs explicit. A weighted sum is another choice, but its conclusions depend on the scales and weights. Estimates of the component outcomes remain necessary under either formulation.

A list with more categories need not better serve every customer. Someone replenishing a familiar weekly basket may value reliability more than novelty. Elicit the relevant goal, preserve a way to revise it, and evaluate whether the system responds appropriately. A policy that increases variety on average can still repeatedly ignore the preferences of a particular group.

### 8.2.2 Case Study: Content Exposure and Political Attitudes Are Different Outcomes

[Milli and coauthors (2025)](https://doi.org/10.1093/pnasnexus/pgaf062) conduct a preregistered audit with 806 Twitter users, comparing posts selected by engagement ranking with recent posts from accounts each user follows. They collect item-level stated preferences and perceptions. Engagement ranking selects more emotionally charged and out-group-hostile material, and the political posts selected are not preferred by users on the stated-preference measure. The outcomes describe selected content and users' evaluations within the audit's exposure window.

[Liu and coauthors (2025)](https://doi.org/10.1073/pnas.2318127122) conduct four experiments with nearly 9,000 participants on a YouTube-like interface. Manipulating recommendation sequences produces limited short-term polarization effects in the studied settings. The intervention, exposure duration, and attitude outcomes differ from the Twitter audit. The studies therefore address different links between recommendation, consumption, perception, and opinion. A change in the composition of displayed content does not determine the magnitude of an attitude effect.

For a managerial comparison, state the population, assignment, exposure window, outcome, and uncertainty before combining findings across settings. A nonsignificant attitude effect supplies no general assurance of zero long-run effects, just as a difference in displayed content supplies no estimate of long-run polarization. The relevant evidence is the estimated effect and its uncertainty for the intervention actually evaluated.

### 8.2.3 Platform Incentives and Preference Changes

The platform's return from a recommendation can differ from the customer's value. [Chen and Tsai (2024)](https://doi.org/10.1111/1756-2171.12481) examine Amazon's dual role as retailer and intermediary using product-level recommendation data and variation from Amazon stockouts. The study finds that Amazon's seller status affects the receipt of “Frequently Bought Together” recommendations. The design uses within-product changes, with accompanying controls and checks, to distinguish seller identity from stable product appeal. Its causal interpretation depends on the treatment of other changes accompanying stockouts.

An analyst evaluating a marketplace should record whether an item is sold by the platform, sponsored, or commission-bearing, alongside availability and customer relevance. Contribution should use the appropriate margin or fee for each item. A common ranking score can conceal those different incentives. A policy change may improve platform profit while reallocating sales among sellers, so report effects at the customer, seller, and platform levels relevant to the decision.

[Zhu and coauthors](https://arxiv.org/abs/2210.05662v2) develop a benchmark for distinguishing better matching from changes in users' preferences under a recommendation process. Their experiments use synthetic and real-world datasets within the proposed framework. They motivate measuring preference change separately from click-through performance. They do not establish that every online performance gain represents manipulation. A customer may learn to appreciate an unfamiliar product; whether that change serves the customer requires a stated criterion and evidence beyond a higher click count.

## 8.3 Marketing-Mix Models Combine Carryover and Saturation

A marketing-mix model relates aggregate outcomes to media activity and other determinants across time or markets. Its appeal is practical: many firms observe weekly sales and channel spending even when individual customer paths are unavailable. The analytical challenge is that media decisions often respond to expected demand. Advertising, promotions, holidays, distribution, and competitor actions can move together.

A simple carryover variable is

$$
a_{ct}=s_{ct}+\rho_c a_{c,t-1},\qquad 0\leq\rho_c<1,
$$

where $s_{ct}$ is spending in channel $c$ during period $t$, $a_{ct}$ is its accumulated exposure proxy, and $\rho_c$ controls geometric decay. This unnormalized definition gives the same units as spending, but its long-run level under constant spending is $s_c/(1-\rho_c)$. Some software normalizes the weights. Coefficients and interpretations must follow the selected convention.

If one spending pulse of 100 occurs at period zero and $\rho=0.5$, the subsequent accumulated values are 100, 50, 25, and 12.5. A pulse can therefore coincide with later sales even when current spending is zero. A seasonal demand pattern can also create persistence. The model needs enough information and a credible design to distinguish these explanations.

Saturation describes declining additional response at higher exposure. A saturating response curve is $R(a)=A[1-\exp(-a/b)]$, where $A$ is the limiting response and $b>0$ controls how quickly the curve approaches that limit. A basic outcome model may combine channel response curves, controls, trend, seasonality, and an error term. The fitted components are model-dependent; their causal interpretation requires assumptions about how spending was chosen and which demand determinants were measured.

The official [Meridian documentation](https://developers.google.com/meridian/docs/basics/meridian-introduction) describes a modern framework for marketing-mix modeling. The [PyMC Marketing examples](https://www.pymc-marketing.io/en/latest/notebooks/mmm/mmm_example.html) provide another implementation route. Use those materials to inspect definitions, priors, and diagnostics. A software package cannot supply a missing source of identifying variation. Experiments and external evidence can help calibrate a model, subject to whether their populations, interventions, and time horizons match the intended use.

## 8.4 Case Study: Allocate the Next Dollar Using Marginal Returns

Consider two channels with imposed contribution response curves

$$
R_A(s_A)=100[1-\exp(-s_A/20)],\qquad
R_B(s_B)=80[1-\exp(-s_B/40)].
$$

Both spending and contribution are measured in thousands of dollars over the same horizon. These response functions omit cross-channel interactions and are assumed known. At a total budget of 60, suppose the current allocation is 40 to A and 20 to B. The question is whether moving a small amount between channels increases contribution while holding the total budget fixed.

Average contribution per unit spent is $R_c(s_c)/s_c$. At the current allocation, it is approximately 2.16 for A and 1.57 for B. Marginal contribution is the derivative of the response curve. It is approximately 0.68 for A and 1.21 for B. A has the higher average return, while B offers the greater return on the next small unit of spending.

![Average returns can favor one channel while marginal returns favor the other.](../figures/M08_marginal_returns.png)

At the current allocations, B has the steeper response curve. Moving a small amount from A to B therefore raises total contribution. The comparison depends on the slopes at the current allocation, whereas average returns summarize all spending up to that point. The budget is held fixed, so the transfer does not change total spending expense.

For a differentiable, concave response with an interior optimum and no other constraints, marginal returns are equal across channels. Here the condition is

$$
5\exp(-s_A/20)=2\exp(-s_B/40),\qquad s_A+s_B=60.
$$

Solving gives $s_A\approx32.22$ and $s_B\approx27.78$. Total contribution rises from approximately 117.94 to 120.09, or about 2.14 thousand dollars. If total budget were also a choice, marginal contribution would be compared with the marginal cost of spending; exhausting a fixed budget and choosing its size are different optimization problems.

A real decision should also examine parameter uncertainty, operational minimums, saturation outside observed spending ranges, delayed effects, and interactions across channels. Report how the recommended allocation changes under plausible response curves. A sharply stated optimum based on weakly identified slopes can conceal substantial decision uncertainty. Prefer an allocation that is supported by observed variation and specify an experiment that would resolve the most consequential uncertainty.

## 8.5 Generative AI Changes the Cost of Producing and Checking Work

Generative AI can assist with code, text classification, documentation, and communication. The business value depends on the complete workflow. Faster generation can be offset by additional review, integration failures, or errors that reach downstream decisions. Measure the output that matters: a correct, reproducible analysis completed with an appropriate understanding of its limitations.

Separate several uses. A coding assistant produces or edits a program that can be inspected and executed. An annotation model produces labels that require a measurement evaluation. A retrieval system selects source passages and may generate a summary that needs factual support. A content system produces customer-facing material whose effect should be evaluated in its deployment context. Each use has a different unit of quality and a different failure mechanism.

For coding, begin with an analytical specification and a small example with a known result. Ask the assistant to implement a limited step, explain the data transformations, and identify assumptions. Inspect the code before running it. Then compare intermediate outputs with independent checks. A program that executes successfully can still use an incorrect denominator, join on the wrong key, or include future information. Those errors require substantive checks rather than syntax repair.

For retrieval and summarization, maintain the connection between a claim and its source. A citation should support the particular statement next to it. Ask the model to distinguish an observed result from a proposed explanation, and check that distinction against the original text. If a passage or file is unavailable, state that limitation. Fluent reconstruction is not a substitute for access to the evidence.

## 8.6 Case Study: Evaluate an AI-Assisted Analytics Workflow

Suppose a firm wants to know whether access to a coding assistant improves analysts' work on customer-retention tasks. Define treatment as access under a specified protocol and version, and define an outcome that incorporates both completion and validity. A useful primary outcome could be the fraction of assigned tasks meeting a prespecified analytical rubric within a fixed time budget. Secondary outcomes could include completion time, independent error severity, and a later explanation task completed without assistance.

Randomize analysts or teams according to the likely spillovers. Repeated tasks by the same analyst require attention to learning, carryover, and dependence. If a crossover design is used, randomize order and consider whether experience in the first condition changes performance in the second. A task-level comparison with no accounting for analyst ability or task difficulty can confound the treatment effect with who received which work.

Quality review should use a common rubric and, where feasible, reviewers unaware of treatment assignment. The rubric can check observation units, joins, leakage, estimation, uncertainty, and interpretation. Record the assigned task, the eligible inputs, the tool configuration, and the evaluation procedure. Avoid interpreting a favorable result for one task type as a universal effect across all analytical work.

Suppose a manual workflow uses 90 minutes to produce an analysis and 20 minutes to review it, totaling 110 minutes. An assisted workflow uses 45 minutes to produce a draft and 40 minutes to review it, totaling 85 minutes. The reduction in total time is 25 minutes, or about 22.7%, while the drafting-time reduction is 50%. The total-time comparison is informative only if the completed outputs meet comparable quality requirements.

![The relevant time saving includes generation, review, and correction.](../figures/M08_workflow_time.png)

This comparison holds the task and required quality fixed. Review is part of production because an undetected error can alter a marketing decision. In empirical work, report the completion and quality outcomes alongside time so that faster abandonment or lower-quality work is not counted as an equivalent improvement.

## 8.7 Integrated Case: A Retail Subscription Launch

A retailer is considering a subscription service with recommendations and delivery benefits. Begin with the decision: which offer to launch, to which eligible customers, at what price, with what evidence of incremental contribution? Define the evaluation horizon, capacity constraints, and the alternatives to launch.

Construct the customer and order tables with explicit keys and dates. Describe customer activity and purchasing cohorts, keeping unavailable future retention separate from observed inactivity. Use regression to summarize conditional patterns while examining confounding. Design a conjoint exercise to learn stated tradeoffs between delivery, assortment, and price, then assess whether its predictions generalize to an actual offer.

Use segmentation to organize meaningful differences in needs and behavior, and calculate customer value from contribution rather than revenue. Analyze reviews to identify the service attributes customers mention, checking annotation quality against human labels. Develop a prediction model using only information available at the targeting date. Its forecasts can help plan capacity, while a randomized offer evaluates incremental take-up, contribution, and retention.

Finally, evaluate the recommendation component and the acquisition budget. Log exposure to recommended items, distinguish average from marginal media returns, and use AI assistance within a documented verification process. The management recommendation should identify the supported action, the uncertainty that could change it, and the next observation or experiment with the greatest decision value. A complicated collection of models is useful only if these pieces support a coherent choice.

## 8.8 Practice and Further Reading

**Recommendation exercise.** Compare all four three-item lists in the variety example at $\lambda=0$, 0.20, and 0.30. At zero, A, B, C is optimal. At 0.20, it ties A, C, D. At 0.30, A, C, D is optimal. Explain how a different category definition could change that conclusion without changing any relevance score.

**Dynamic-policy exercise.** Design a comparison between a temporary recommendation boost with a frozen model and the same boost followed by retraining. Specify how training data are separated across conditions, when outcomes are measured, and how shared content or customers could transmit effects. Explain which comparison identifies the effect of allowing the model to learn from campaign-period behavior.

**Evidence exercise.** Compare the MovieLens field experiment, the Netflix model-based replacement counterfactuals, and the short-term YouTube experiments. State the intervention and estimand for each. Explain why their reported outcomes cannot be combined into a single percentage measuring the value or harm of recommendation systems.

**Budget exercise.** Calculate the gain from moving one thousand dollars from channel A to channel B at the original allocation. Compare the exact change with the difference between the two marginal returns. The derivative is a local approximation; the exact finite transfer also reflects curvature. Then explain why an unobserved seasonal demand shock could invalidate a causal interpretation of an estimated response curve.

**AI evaluation exercise.** Draft a rubric for an assistant-generated retention analysis. Include at least one check that detects a substantive error in code that executes successfully, such as an order-line denominator used for average order value. Define a hand-checkable example that exposes the error and explain how a reviewer would determine whether it occurred.

Read Nielsen and coauthors, [“Consumption Variety in Food Recommendation”](https://doi.org/10.1086/720453), and Ling and coauthors, [“Following Good Examples”](https://doi.org/10.1145/3485447.3514193), for applications connecting recommendation objectives with customer behavior. The official marketing-mix documentation linked above develops implementation details. Consult the [AI-coding evidence](../../01_Resources/10_AI_Coding_Concepts_and_Evidence/README.md) and [workflow resources](../../01_Resources/11_AI_Coding_Tools_and_Workflows/README.md) for further study.

## 8.9 mHealth: Familiarity, Novelty, and the Decision Objective

A manager may value introducing unfamiliar categories even when the most accurate prediction repeats a customer's routine. That preference changes the ranking objective. It should be stated as a decision choice before interpreting any performance comparison. A category absent from recent logs is novel relative to recorded history; it may be familiar to the person outside the app.

Retain the September users, target baskets, candidate set, and 30-day frequency rule from M7. Add a bonus $\lambda$ to a candidate category if it has not appeared in the user's prior 30 calendar days of logs:

$$
S_{ic}(\lambda)=f_{ic}+10^{-6}p_c+
\lambda\mathbf{1}\{c\text{ absent from the prior 30-day log}\}.
$$

Here $f_{ic}$ is the fraction of observed history days containing category $c$, and $p_c$ is global popularity used for tie resolution. The bonus is measured in the same score units as frequency. It is an imposed objective weight, not an estimated willingness to try a food or a nutritional benefit. Rank all candidates by this score and count the fraction of the ten recommendations absent from recent history.

| Novelty Bonus | Recall at 10 | NDCG at 10 | Novel Categories in the List |
| --- | ---: | ---: | ---: |
| 0.00 | 0.4759 | 0.5862 | 4.78% |
| 0.05 | 0.4759 | 0.5862 | 4.82% |
| 0.10 | 0.4759 | 0.5863 | 5.28% |
| 0.20 | 0.4661 | 0.5809 | 9.83% |

The grid is a specified sensitivity comparison on the same 299 test users. It is not used to select a winning policy and then claim an independent test of that winner. At a bonus of 0.20, novelty roughly doubles while recall falls by about 0.98 percentage points. At smaller bonuses, changes in the list can occur among categories that are all absent from the target, leaving recall unchanged. NDCG can move without a recall change when relevant categories exchange positions.

![A novelty bonus changes list composition before it substantially changes basket recovery.](../figures/M08_mhealth_tradeoff.png)

The first three points lie close together in recall even though novelty rises. The fourth trades some recovery of the recorded basket for greater novelty. This is an offline relationship between a ranking rule and historical labels. It does not measure whether customers prefer the new list, accept the suggestions, or change diet.

A nutrition objective would need a validated nutrient database, appropriate portions, restrictions supplied by the customer, and an outcome definition. Source categories and calorie-share variety alone do not establish healthy choices. The data-cleaning distinctions in M2 therefore affect what the manager can optimize. Dropping low-calorie days might improve an apparent fit by selecting more complete logs, while also excluding the customers for whom the interface is hardest to use.

A concrete next decision is whether to run the M6 user-randomized comparison, using a prespecified novelty setting and separate measures of logging, acceptance, and any validated nutrition outcome. The experiment should preserve the assignment population and record exposure. An AI assistant can implement the frozen ranking rule and audit category descriptions, while unsupported health claims remain outside the factual explanation supplied with the recommendation.

Python source: [m08.py](../../03_Data_and_Code/mHealth/recurring_examples/m08.py). From its directory, run `python m08.py`.

```python
"""Measure an imposed novelty-relevance tradeoff on the same September baskets."""

import json
from common import OUTPUT, load_inputs, save_result
from ranking import candidate_categories, evaluate

food, daily, baskets = load_inputs()
selection = json.loads((OUTPUT / "M07.json").read_text())
windows = {"30_days": 30, "90_days": 90, "all_prior_days": None}
window = windows[selection["chosen_window"]]
candidates = candidate_categories(baskets)
# This grid is a specified sensitivity analysis, not a test-set model search.
weights = [0.0, 0.05, 0.10, 0.20]
tradeoff = [
    {
        "novelty_weight": weight,
        **evaluate(baskets, "2016-09-01", candidates, window, novelty_weight=weight),
    }
    for weight in weights
]
assert (
    abs(
        tradeoff[0]["recall_at_10"]
        - selection["test"]["personal_frequency"]["recall_at_10"]
    )
    < 1e-12
)
result = {"history_window": selection["chosen_window"], "tradeoff": tradeoff}
save_result("M08", result)
print(json.dumps(result, indent=2))
```

## 8.10 Python Calculations for the Synthetic Cases

The inputs below are imposed teaching values. Running the program creates the labeled synthetic CSV files and prints the corresponding calculations. They are separate from the mHealth estimates. Keep the script beside `example_helpers.py` in `03_Data_and_Code/Lecture_Examples`.

Python source: [m08_synthetic.py](../../03_Data_and_Code/Lecture_Examples/m08_synthetic.py). From its directory, run `python m08_synthetic.py`.

```python
"""Synthetic numerical examples for M8; run from any working directory."""

import itertools
import json
import math
from example_helpers import write_csv, ols_slope, shares

r = {}
items = {
    "A": ("Coffee", 0.90),
    "B": ("Coffee", 0.85),
    "C": ("Tea", 0.75),
    "D": ("Fruit", 0.65),
}
list_values = {}
for weight in [0, 0.2, 0.3]:
    list_values[str(weight)] = {
        "".join(choice): sum(items[j][1] for j in choice)
        + weight * len({items[j][0] for j in choice})
        for choice in itertools.combinations(items, 3)
    }
ra = lambda s: 100 * (-math.expm1(-s / 20))
rb = lambda s: 80 * (-math.expm1(-s / 40))
sa = (40 * math.log(2.5) + 60) / 3
sb = 60 - sa
r["M08"] = {
    "recommendation_objectives": list_values,
    "carryover": [100 * 0.5**t for t in range(4)],
    "average_A": ra(40) / 40,
    "average_B": rb(20) / 20,
    "marginal_A": 5 * math.exp(-40 / 20),
    "marginal_B": 2 * math.exp(-20 / 40),
    "current_total_contribution": ra(40) + rb(20),
    "optimal_spend_A": sa,
    "optimal_spend_B": sb,
    "optimal_total_contribution": ra(sa) + rb(sb),
    "contribution_gain": ra(sa) + rb(sb) - ra(40) - rb(20),
    "one_unit_transfer_gain": ra(39) + rb(21) - ra(40) - rb(20),
    "manual_total_minutes": 110,
    "assisted_total_minutes": 85,
    "time_reduction_fraction": 25 / 110,
}
assert math.isclose(5 * math.exp(-sa / 20), 2 * math.exp(-sb / 40))
# Independent grid check of the constrained optimum, to the grid's precision.
grid_best = max((ra(i / 100) + rb(60 - i / 100), i / 100) for i in range(6001))
assert abs(grid_best[1] - sa) < 0.01
write_csv(
    "M08_recommendation_synthetic.csv",
    ["item", "category", "relevance_score"],
    [(key, *value) for key, value in items.items()],
)
print(json.dumps(r, indent=2))
```

## 8.11 Evidence Checks for Generated Marketing Explanations

An analytics manager may accept a fluent business review whose numbers and interpretation describe different populations. Structured output helps software locate a metric, period, value, unit, and denominator. Each field also needs evidence. A correctly formatted statement can contain the wrong number or describe a causal effect that the underlying analysis never estimated.

Use the fixed-cohort mHealth review from Section 1.10 as the evidence source. June contains 6,331 observed user-days out of 10,200 eligible calendar user-days, giving a logging fraction of 0.620686. A structured claim must identify that month, denominator, unit, and descriptive interpretation. Four constructed candidates retain the same field structure: one reproduces the supported result, one adds 0.10 to its value, one substitutes the number of logging users for the denominator, and one labels the result a causal health benefit.

| Constructed Candidate | Format | Evidence Check |
| --- | --- | --- |
| Supported Result | Valid Fields | Accepted |
| Changed Number | Valid Fields | Value Mismatch |
| Changed Denominator | Valid Fields | Denominator Mismatch |
| Causal Health Claim | Valid Fields | Unsupported Interpretation |

All four candidates pass the same basic structural requirement. Only the supported claim passes the evidence checks. They are deliberate teaching inputs, not observed outputs from a particular LLM. The code makes no external model request and sends no customer data to an AI service. Its checks concern the declared fields. Free-form prose, omitted qualifications, and advice require a separate substantive review; an “interpretation” field cannot validate an unrestricted paragraph.

![A generated statement passes through separate checks for structure, numerical evidence, and substantive interpretation before informing a decision.](../figures/M08_evidence_checks.png)

[Copycat](https://github.com/google-marketing-solutions/copycat) demonstrates generation of advertising text from brand examples and evaluates similarity and memorization. Those diagnostics concern the generated content. Incremental sales or engagement requires an outcome comparison under an appropriate exposure design, such as a randomized test of the generated and existing alternatives. The Gemini and Google Cloud marketing notebooks in the resource collection supply further examples of generation and structured extraction; model credentials, costs, and data permissions are separate requirements for executing those reference notebooks.

Synthetic consumer panels raise a related distinction. The [semantic-similarity-rating package](https://github.com/pymc-labs/semantic-similarity-rating) maps generated text to distributions over response anchors. The mapping can standardize how generated answers are summarized. Validation against a target population still requires human outcomes, a sampling definition, and comparisons held out from prompt or anchor selection. Generating more answers under the same misspecified prompt reduces simulation noise around that prompt's distribution while preserving its systematic difference from consumers. Agreement among generated respondents is therefore a property to examine alongside external validity.

A useful AI coding request is: “Compare every numerical field with its computed evidence; reject unknown metrics, periods, units, and denominators; retain the analysis's descriptive interpretation; and test a correctly formatted false claim.” The checking rule should be written before inspecting a favored generated answer. Report the factual error rate and the time spent checking, alongside any reduction in drafting time.

Python source: [claim_checks.py](../../03_Data_and_Code/mHealth/recurring_examples/claim_checks.py). From its directory, run `python claim_checks.py`.

```python
"""Check constructed structured claims against computed mHealth evidence."""

import json
import math
from copy import deepcopy
from common import load_food, save_result
from reporting import monthly_review


def check_claim(claim, evidence):
    required = {"metric", "period", "value", "unit", "denominator", "interpretation"}
    if not isinstance(claim, dict) or set(claim) != required:
        return ["schema"]
    rows = [row for row in evidence["periods"] if row["period"] == claim["period"]]
    if len(rows) != 1 or claim["metric"] != evidence["metric"]:
        return ["unknown metric or period"]
    row = rows[0]
    errors = []
    if type(claim["value"]) not in (int, float) or not math.isfinite(claim["value"]):
        errors.append("numeric value")
    elif not math.isclose(
        claim["value"], row["logging_fraction"], rel_tol=0, abs_tol=1e-10
    ):
        errors.append("value disagrees with evidence")
    if (
        type(claim["denominator"]) is not int
        or claim["denominator"] != row["calendar_user_days"]
    ):
        errors.append("denominator")
    if claim["unit"] != evidence["unit"]:
        errors.append("unit")
    if claim["interpretation"] != evidence["interpretation"]:
        errors.append("unsupported interpretation")
    return errors


if __name__ == "__main__":
    evidence = monthly_review(load_food())
    june = evidence["periods"][1]
    valid = {
        "metric": "logging_fraction",
        "period": "2016-06",
        "value": june["logging_fraction"],
        "unit": evidence["unit"],
        "denominator": june["calendar_user_days"],
        "interpretation": "descriptive",
    }
    candidates = {"supported": valid}
    changes = {
        "wrong_number": ("value", valid["value"] + 0.1),
        "wrong_denominator": ("denominator", june["users_with_logs"]),
        "causal_claim": ("interpretation", "causal health benefit"),
    }
    for name, (field, value) in changes.items():
        candidates[name] = deepcopy(valid)
        candidates[name][field] = value
    result = {
        "candidate_origin": "constructed teaching examples; no LLM request",
        "checks": {
            name: check_claim(claim, evidence) for name, claim in candidates.items()
        },
    }
    assert result["checks"]["supported"] == []
    assert all(result["checks"][name] for name in changes)
    save_result("claim_checks", result)
    print(json.dumps(result, indent=2))
```

## 8.12 An Executable Chart Can Still Misstate the Evidence

A manager asks an AI assistant to plot monthly customer engagement. The generated program can run successfully and produce an attractive chart while changing the population, labeling a fraction as a percentage, or describing a temporal association as an intervention effect. A chart therefore needs checks of execution, fidelity to the analytical question, and readability. [VisEval](https://github.com/microsoft/VisEval) separates these dimensions when evaluating generated visualizations.

The mHealth example provides an independent numerical reference. The requested measure is the percentage of all eligible calendar user-days with a log. Its two numerators and denominators are computed before plotting. The following constructed mistakes retain valid numerical inputs and executable drawing instructions. Each fails a different substantive requirement.

| Constructed Chart Error | Consequence | Check |
| --- | --- | --- |
| Plot a fraction under a percent label | Values are 100 times too small | Recompute units |
| Keep only users who logged | Population changes with the outcome | Reconcile denominators |
| Start rate bars at 60% | Bar lengths distort magnitudes | Inspect baseline |
| Declare the time difference causal | Claim exceeds the design | Inspect interpretation |

The checker below accepts the correct specification and rejects all four constructed mistakes. Its numerator and denominator checks use the saved monthly evidence, rather than the plotted value as its own reference. This is a narrow validator for declared fields. It does not interpret unrestricted natural-language titles, inspect pixels, or guarantee that a rendered chart is readable. Review the displayed title, labels, clipping, color contrast, and all interactive selections separately. A chart can pass these field checks while still misleading through an omitted subgroup or an unsupported narrative.

Ask a coding assistant to return the aggregate plotting table, units, eligibility rule, axis domains, and one hand-calculated plotted value with its code. A second review should compare those objects with the original analysis specification. Passing the assistant's own test is informative only when the expected answer was derived independently. The [Financial Times vocabulary](https://github.com/Financial-Times/chart-doctor/blob/main/visual-vocabulary/README.md) supports the choice of display, while [Rougier's visualization code](https://github.com/rougier/scientific-visualization-book) provides examples of figure construction and layout. The managerial claim must remain tied to the evidence and design.

Run `visualization.py` first to create the evidence table, then run the audit. The false charts are constructed teaching cases; their rejection rates do not measure the reliability of any particular language model.

Python source: [chart_audit.py](../../03_Data_and_Code/mHealth/recurring_examples/chart_audit.py). From its directory, run `python chart_audit.py`.

```python
"""Check a narrow chart specification against the monthly evidence table."""

from copy import deepcopy
import json
import math
from common import OUTPUT, save_result


def check_chart(chart, evidence):
    errors = []
    expected = {row["period"]: row for row in evidence["months"]}
    if chart.get("unit") != "percent of eligible user-days":
        errors.append("axis unit")
    if chart.get("interpretation") != "descriptive":
        errors.append("interpretation")
    if chart.get("mark") == "bar" and chart.get("y_domain", [None])[0] != 0:
        errors.append("bar baseline")
    rows = chart.get("rows", [])
    if sorted(row["period"] for row in rows) != sorted(expected):
        errors.append("period coverage")
    for row in rows:
        ref = expected.get(row["period"])
        if ref is None:
            continue
        value = row["value"]
        target = 100 * ref["observed_user_days"] / ref["calendar_user_days"]
        if not math.isfinite(value) or not math.isclose(value, target, abs_tol=1e-8):
            errors.append("plotted value")
        if row["denominator"] != ref["calendar_user_days"]:
            errors.append("denominator")
    return sorted(set(errors))


def main():
    evidence = json.loads((OUTPUT / "visualization.json").read_text())
    correct = {
        "unit": "percent of eligible user-days", "interpretation": "descriptive",
        "mark": "bar", "y_domain": [0, 100],
        "rows": [{"period": r["period"], "value": r["logging_percent"],
                  "denominator": r["calendar_user_days"]} for r in evidence["months"]],
    }
    cases = {"correct": correct}
    for name in ["fraction_as_percent", "conditional_denominator", "truncated_bar", "causal_title"]:
        cases[name] = deepcopy(correct)
    cases["fraction_as_percent"]["rows"][0]["value"] /= 100
    row = cases["conditional_denominator"]["rows"][0]
    row["denominator"] = evidence["months"][0]["logger_calendar_days"]
    row["value"] = evidence["months"][0]["conditional_logging_percent"]
    cases["truncated_bar"]["y_domain"] = [60, 75]
    cases["causal_title"]["interpretation"] = "causal"
    result = {name: check_chart(chart, evidence) for name, chart in cases.items()}
    assert result["correct"] == []
    assert all(result[name] for name in cases if name != "correct")
    save_result("chart_audit", {"constructed_cases": result})
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
```
