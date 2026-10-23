# M6. Causal Effects and Marketing Experiments

A retailer wants to know whether an email campaign increases contribution. Customers who open marketing emails often purchase more, but they may already be more engaged. Comparing openers with nonopeners can therefore reward a campaign for behavior it did not cause. The decision requires a comparison between outcomes under alternative actions for the same target population.

## 6.1 Define the Treatment, Outcome, and Estimand

Let $Y_i(1)$ be customer $i$'s 30-day contribution if assigned an email and $Y_i(0)$ the contribution if not assigned. The individual effect is $Y_i(1)-Y_i(0)$. Only one of these outcomes is observed for a given customer under a single assignment. A causal design supplies a defensible way to learn an average comparison despite that missing counterfactual.

For a target population, the average treatment effect is

$$
\operatorname{ATE}=E[Y_i(1)-Y_i(0)].
$$

The expectation refers to the stated population and outcome window. An average treatment effect on the treated uses the population that actually received treatment. An intention-to-treat effect uses assignment as the treatment, even if some assigned customers never open the email. These are different estimands. The managerial decision to send an email often corresponds closely to the assignment effect, because opening is outside the firm's direct control.

A well-defined treatment includes the offer, timing, channel, and implementation. “Digital marketing” is too broad to identify a single comparison. The outcome should include economically relevant costs and have enough follow-up to capture returns or delayed purchases. If customers can affect one another, an individual's outcome may depend on other customers' assignments. The unit and design then need to account for interference rather than silently assuming it away.

## 6.2 Why the Treated-Untreated Difference Can Be Biased

The observed difference between treated and untreated customers can be decomposed as

$$
E[Y\mid D=1]-E[Y\mid D=0]
=E[Y(1)-Y(0)\mid D=1]
+\{E[Y(0)\mid D=1]-E[Y(0)\mid D=0]\}.
$$

Here $D$ indicates treatment. The first term is the average treatment effect among treated customers. The bracketed term compares their untreated outcomes with untreated customers' outcomes. If the firm targets people who would purchase anyway, that selection term can be positive. If it targets customers in serious decline, the term can be negative. The direction follows the assignment process, not a universal rule about observational data.

An unobserved engagement variable may affect both email opening and purchasing. Adjusting for pre-treatment engagement measures can be useful if they capture the relevant confounding, but controlling for a variable does not guarantee this condition. A post-treatment variable such as clicking the email can mediate part of its effect. Conditioning on customers who click changes the population and can introduce selection.

![Assignment, engagement, and opening define different causal comparisons.](../figures/M06_dag.png)

The firm randomizes email assignment, while customers choose whether to open. Assignment can affect opening, and engagement can affect both opening and purchases. Restricting attention to openers creates a selected group. An assignment-based analysis preserves the randomized comparison when its implementation and outcome measurement are valid.

## 6.3 Designing an Experiment Around the Decision

An experiment needs an eligible population, assignment unit, treatment implementation, primary outcome, horizon, and analysis plan. Randomize at a unit that corresponds to exposure and likely spillovers. A customer-level email experiment may be appropriate when accounts act independently. A store-level display intervention requires store assignment or a design that accounts for shared exposure. Household, geographic, or network spillovers can require broader clusters.

Balance treatment groups through randomization, with blocking or stratification when important pre-treatment characteristics are known. For example, randomize within customer-tenure groups to improve balance and precision. Record assignment before contact and retain every assigned unit in the primary analysis when estimating the intention-to-treat effect. Excluding nonopeners, customers who later unsubscribe, or stores with disappointing execution can undermine the randomized comparison.

Specify a primary outcome and guardrails before viewing results. Incremental contribution might be primary, with unsubscribe rates, complaints, and returns as guardrails. Multiple outcomes can be informative, but selecting the most favorable result after examining many tests exaggerates evidence. Decide how multiple testing, sequential monitoring, and stopping will be handled. Ordinary fixed-horizon p-values do not generally retain their advertised interpretation under unrestricted repeated peeking and outcome selection.

## 6.4 Case Study: Estimate an Email Assignment Effect

In a synthetic experiment, 1,000 customers are assigned an email and 1,000 are assigned no email. Within 30 days, 130 assigned customers and 100 controls make at least one eligible purchase. The estimated assignment effect on purchase incidence is

$$
\hat\tau=\frac{130}{1000}-\frac{100}{1000}=0.03,
$$

or three percentage points. Relative to the control rate of 10%, this is a 30% relative increase. The two descriptions use different denominators; reporting only “30% lift” can obscure the absolute change.

Under independent customer assignments and the usual large-sample approximation, an unpooled standard error is

$$
\widehat{\operatorname{SE}}(\hat\tau)
=\sqrt{\frac{0.13(0.87)}{1000}+\frac{0.10(0.90)}{1000}}
\approx0.0143.
$$

An approximate 95% interval is [0.0021, 0.0579], or about 0.21 to 5.79 percentage points. This interval describes sampling uncertainty under the stated design and approximation. It does not account for an unmeasured outcome-definition error or interference between assigned customers.

Suppose an additional purchase contributes $40 and email delivery costs $0.50 per assigned customer. If the offer has no additional discount cost and purchase incidence is the relevant incremental quantity, estimated incremental contribution is $40(0.03)-$0.50=$0.70 per assigned customer. Applying the same transformation to the effect interval gives approximately $-0.42 to $1.82. A positive point estimate therefore coexists with economically consequential uncertainty. A decision can combine that uncertainty with rollout costs, the value of another test, and guardrail outcomes.

The margin assumption matters. If treatment also changes basket size, returns, or discount expense, purchase incidence alone is insufficient. An experiment measuring contribution directly may better match the objective.

## 6.5 Power, Precision, and the Minimum Useful Effect

Power planning begins with the smallest effect that could change the decision, not with a convenient number of rows. For two equally sized independent groups and a binary outcome with baseline rate near $p$, a rough per-group sample-size approximation is

$$
n\approx\frac{2p(1-p)(z_{1-\alpha/2}+z_{1-\beta})^2}{\delta^2},
$$

where $\delta$ is the absolute effect in probability units, $\alpha$ is the two-sided significance level, and $1-\beta$ is target power. This approximation uses a common baseline variance and normal critical values. More precise planning can use the expected rates under the alternative and the actual assignment design.

With $p=0.10$, $\delta=0.02$, $\alpha=0.05$, and 80% power, using 1.96 and 0.84 gives about 3,528 customers per group. Halving the target effect approximately quadruples the required sample under this formula. A two-percentage-point effect is 0.02, not 2; a unit error can produce a meaningless sample-size recommendation.

Clustering reduces the amount of independent information. A common approximation with equal cluster size $m$ and intracluster correlation $\rho$ multiplies individual-level variance by $1+(m-1)\rho$. For $m=20$ and $\rho=0.05$, that factor is 1.95. The number of clusters, unequal cluster sizes, assignment design, and small-sample inference still require explicit consideration. Thousands of customers across four stores do not provide thousands of independent store-level treatment assignments.

## 6.6 Implementation Checks That Protect the Comparison

Verify that the assignment counts match the intended allocation and investigate material sample-ratio discrepancies. Check whether tracking differs between treatment and control, whether treatment changes the probability an outcome is observed, and whether exclusions were applied consistently. Pre-treatment balance is a diagnostic, not proof that every causal assumption holds. In a correctly randomized experiment, chance imbalances can occur.

Noncompliance changes the estimand. If only 40% of assigned customers open the email, the intention-to-treat effect remains the effect of assignment under the observed implementation. Dividing it by an opening-rate difference identifies a complier effect only under additional instrumental-variable conditions, including an appropriate exclusion restriction and monotonicity. The firm may care about the assignment effect even when a different scientific question concerns actual exposure.

Use pre-treatment outcomes to improve precision when justified. A regression adjustment can compare outcomes while accounting for baseline spending or stratification variables. Avoid selecting an adjustment because it makes the treatment coefficient significant. Report the planned analysis and explain any departures. Analyze heterogeneity cautiously, especially when many subgroups are examined after seeing the main result.

## 6.7 Observational Adjustment and Its Limits

When randomization is unavailable, a common approach assumes that treatment is conditionally independent of potential outcomes given observed pre-treatment covariates, with overlap in treatment probabilities. Regression adjustment, matching, and inverse-probability weighting implement different ways to construct a comparison under that condition. The central question is whether the observed covariates make the treated and untreated outcomes comparable.

A propensity score is the treatment probability given those covariates. Extreme estimated scores indicate limited overlap and can create unstable weights. Trimming or restricting the sample changes the population for which the effect is estimated. Report that population explicitly. A flexible prediction algorithm for treatment assignment does not establish that all confounders were measured.

A doubly robust estimator combines an outcome model and a treatment model and can be consistent when one nuisance model is correctly specified, under the underlying identification conditions and regularity assumptions. This robustness does not cover unmeasured confounding. For advanced implementations, sample splitting and cross-fitting help control overfitting of nuisance functions; the design remains the foundation of the causal interpretation.

### 6.7.1 Evaluating a Recommendation Policy From Logged Exposure

A retailer has records from an existing recommendation policy and wants to evaluate a different one. The existing policy shows products selectively: frequent buyers may usually see A, while occasional buyers usually see B. Comparing their observed click rates mixes product response with the customer populations receiving each recommendation. [Schnabel and coauthors (2016)](https://proceedings.mlr.press/v48/schnabel16.html) formulate recommendation learning and evaluation as problems of selected observation and use propensity weighting to address that selection under explicit conditions.

Consider a single recommendation opportunity per customer. Let $X_i$ be information available before display, $A_i$ the displayed item, and $Y_i$ a click within the specified response window. The logging policy assigns item $a$ with probability $p_0(a\mid X_i)$. A target policy assigns it with probability $\pi(a\mid X_i)$. The target is the expected clicks per opportunity if eligible customers receive recommendations from $\pi$. An inverse-propensity estimator is

$$
\widehat V(\pi)=\frac{1}{n}\sum_{i=1}^{n}
\frac{\pi(A_i\mid X_i)}{p_0(A_i\mid X_i)}Y_i.
$$

The ratio changes how much each logged outcome represents the target policy. For a policy that always recommends A, outcomes following B receive zero weight. An A outcome observed under a 10% display probability receives weight ten. The denominator $n$ counts all eligible logged opportunities, including those assigned zero weight. Dividing only by the number of matching displays estimates a different quantity.

Interpretation requires a well-defined action and outcome, conditional exchangeability of display given $X_i$, and positive logging probability wherever the target policy assigns positive probability. A known randomized logging policy can supply the assignment condition. Estimating probabilities from observational logs requires the additional substantive claim that the recorded context captures the relevant selection. The target population and response process must also match the logged environment. For a slate of products, position and other displayed items can affect the response; a single-item propensity generally does not describe assignment of the complete slate.

The weighting identity explains the adjustment. Conditional on $X=x$, averaging over logged actions gives $\sum_a p_0(a\mid x)\{\pi(a\mid x)/p_0(a\mid x)\}E[Y(a)\mid X=x]$. The logging probability cancels, leaving the response weighted by the target policy. Cancellation requires positive support. If an item was never eligible for a customer group, multiplying the observed records by larger weights cannot reveal that group's response to it.

### 6.7.2 Case Study: Exposure Adjustment Reverses the Preferred Item

Suppose 1,000 synthetic customers comprise 500 frequent buyers and 500 occasional buyers. The logging policy randomly assigns A within each group with probabilities 0.90 and 0.10, respectively. B receives the remaining probability. The constructed counts are:

| Customer Group | Item | Display Probability | Displays | Clicks |
| --- | --- | ---: | ---: | ---: |
| Frequent | A | 0.90 | 450 | 270 |
| Frequent | B | 0.10 | 50 | 25 |
| Occasional | A | 0.10 | 50 | 10 |
| Occasional | B | 0.90 | 450 | 180 |

A receives 280 clicks from 500 displays, or 56%. B receives 205 from 500, or 41%. Yet A's within-group rates are 60% and 20%, while B's are 50% and 40%. Applied to the same equally weighted customer population, A gives 40% and B gives 45%. A's displayed customers disproportionately come from the group with high response to either item.

The inverse-propensity calculations recover the common-population comparison:

$$
\widehat V(A)=\frac{270/0.90+10/0.10}{1000}=0.40,
\qquad
\widehat V(B)=\frac{25/0.10+180/0.90}{1000}=0.45.
$$

![Selected display populations favor A, while comparison on the same population favors B.](../figures/M06_exposure_reversal.png)

The raw bars describe response among each item's displayed customers. The adjusted bars describe the same 50:50 customer mix for both policies. The five-percentage-point advantage for B is imposed by the synthetic cell counts and randomized logging design. It is not an estimate from the cited study.

Large weights reduce precision. For A, the 50 occasional buyers each represent ten eligible customers, so a small number of outcomes carries substantial influence. The diagnostic $(\sum_i w_i)^2/\sum_i w_i^2$ equals 180 for either policy in this example, despite 1,000 logged opportunities. This effective sample size describes weight concentration; it does not replace a variance calculation that respects assignment and dependence. Weight clipping trades variance for bias, and self-normalization changes the finite-sample estimator. Report these choices and retain an untouched evaluation sample when choosing between policies.

## 6.8 Difference-in-Differences and a Counterfactual Trend

A retailer introduces an app in treated markets while comparable markets remain untreated. A before-after difference in treated markets mixes the app's effect with common demand changes. Difference-in-differences subtracts the comparison group's change:

$$
\hat\tau_{\mathrm{DiD}}=(\bar Y_{T,post}-\bar Y_{T,pre})-(\bar Y_{C,post}-\bar Y_{C,pre}).
$$

In a synthetic example, treated-market sales rise from 120 to 150 and comparison-market sales rise from 100 to 110. The DiD estimate is 20 sales units. Under the identifying parallel-trends condition, the treated markets' untreated counterfactual would have risen to 130. Different starting levels are compatible with this design; the condition concerns untreated changes.

![Difference-in-differences subtracts the comparison group's change to construct the counterfactual.](../figures/M06_did.png)

The dashed line is a counterfactual implied by parallel untreated trends, not an observed sales series. The vertical gap between observed treated sales and that line is the estimated effect. A treatment-specific local shock at the same time would challenge the interpretation even if the pre-treatment levels looked similar.

Inspect multiple pre-treatment periods, institutional timing, possible anticipation, spillovers, and changes in sample composition. Similar pre-trends can support the design's plausibility, but a nonsignificant pre-trend test does not establish parallel counterfactual trends. With staggered adoption and heterogeneous effects, conventional two-way fixed-effects coefficients can combine comparisons in problematic ways. Use estimators aligned with cohort and time-specific effects, with a clear comparison group, when extending beyond the simple two-period design.

## 6.9 Other Designs: Discontinuities and Instruments

A regression discontinuity design can use a treatment rule at a threshold, such as eligibility based on a pre-existing score. Customers just above and below the cutoff may be comparable if other determinants of the outcome vary smoothly there and the score is not precisely manipulated. The resulting effect is local to the cutoff and the relevant compliance behavior. Bandwidth, functional form, density patterns, and discontinuities in other predetermined variables deserve inspection.

An instrumental variable changes treatment while affecting the outcome only through the treatment channel, under the design's conditions. Relevance is an empirical first-stage requirement; exclusion is a substantive condition. A strong first stage cannot establish exclusion. In a binary-treatment setting with independence, exclusion, and monotonicity, the familiar local average treatment effect concerns compliers whose treatment changes with the instrument. It need not equal the population ATE.

Marketing instruments require particularly careful reasoning because pricing, distribution, and exposure decisions often respond to demand. A variable correlated with treatment is not sufficient. Explain who makes the relevant decision, when the instrument is determined, and which other channels could connect it to outcomes. If those channels remain credible, the causal interpretation needs revision.

## 6.10 Spillovers and Experiment Units

An advertising campaign can shift purchases between stores or products rather than increase total demand. A customer-level outcome may show a gain while chain-wide contribution changes little. Define the outcome at the level relevant to the managerial objective and examine displacement where it is plausible. The same issue arises when customers share offers or when a platform changes recommendations for multiple users.

![A treatment can affect both assigned units and nearby untreated units.](../figures/M06_spillovers.png)

An assigned store can gain sales while diverting purchases from another store. If the comparison store loses customers, subtracting its decline can overstate the increase in total chain sales. Cluster randomization, geographic separation, or designs that vary treatment saturation may help identify the relevant effects, subject to their own practical constraints.

### 6.10.1 Case Study: Recommendations Supply Information and Exposure

A recommendation can increase consumption by bringing a product to attention or by changing beliefs about its quality. [Aridor, Gonçalves, Kluver, Kong, and Konstan's MovieLens experiment](https://www.econstor.eu/handle/10419/271773), in its November 2022 working-paper version, separates recommendation and exposure-only conditions and elicits users' beliefs. The results support an informational role: recommendations influence beliefs and consumption beyond simply exposing a movie. MovieLens provides recommendations without selling or hosting the movies, which helps define the incentives in this setting.

A retailer studying the same mechanism could distinguish ordinary display from an explicit personalized endorsement while keeping the eligible product set and available information controlled. The primary outcome would be purchases or contribution per assigned customer over a fixed horizon. Belief measures would address how the endorsement operates. The experiment must account for the possibility that asking about a product itself increases attention to it. Comparisons based only on customers who subsequently click would condition on a response that the endorsement can change.

The displayed information can also affect the labels collected afterward. [Cosley and coauthors (2003)](https://experts.umn.edu/en/publications/is-seeing-believing-how-recommender-interfaces-affect-users-opini/) experimentally vary predicted ratings shown to MovieLens users and find that subsequent ratings tend to move toward the displayed prediction. A rating collected after a recommendation therefore reflects the evaluation context as well as the user's experience. A model trained to reproduce those ratings can partly reproduce its own previous influence. Collecting some evaluations before showing predicted ratings provides a comparison for that mechanism.

An experiment on an adaptive recommender also needs a rule for retraining. If both treatment and control data update a shared model, one customer's assignment may change another customer's recommendations. Freezing the model, maintaining separate models, or assigning sufficiently separated populations evaluates different policies. State which policy and learning process the experiment implements. A short experiment with a frozen model identifies a different intervention from deploying a model that learns from its own recommendations over several months.

## 6.11 AI-Assisted Workflow and Practice

Ask an assistant to state the estimand, assignment unit, outcome horizon, and comparison group before writing estimation code. For the email example, require the conversion effect in percentage points, the unpooled standard error, and the contribution calculation. Check the arithmetic independently. Ask it to explain why restricting the sample to email openers changes the analysis.

For observational data, draw or describe the assignment process before selecting controls. Request an overlap diagnostic and a report of which observations receive large weights. For DiD, ask the assistant to show observed and counterfactual series separately and identify the assumptions that connect them. A convincing plot should not substitute for those conditions.

If comparison-market sales rise by 25 rather than 10, the DiD estimate becomes five. If email cost doubles to $1, the point estimate of incremental contribution falls to $0.20. If treatment raises returns, explain why a conversion effect can overstate the contribution effect. If two stores share most customers, identify why store assignment may create interference.

For the exposure example, ask an assistant to compute both the raw click rates and inverse-propensity policy values from the four aggregate rows, using the display counts when calculating denominators and weight concentration. Verify the weighted results independently by averaging the two group-specific response rates. Then set A's display probability among occasional buyers to zero in a proposed logging design and explain why the always-A policy becomes unidentified from those logs. The implementation should flag the unsupported action rather than silently drop that group.

## 6.12 Readings

[Facure's causal-inference handbook](https://matheusfacure.github.io/python-causality-handbook/landing-page.html) supplies accessible implementations of several designs. [Kohavi and colleagues' practical guide](https://exp-platform.com/Documents/GuideControlledExperiments.pdf) discusses controlled online experiments. [Callaway and Sant'Anna (2021)](https://doi.org/10.1016/j.jeconom.2020.12.001) develop difference-in-differences with multiple periods.
