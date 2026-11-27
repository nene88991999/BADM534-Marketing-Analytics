# Regression and Marketing Interpretation

By Nathan Yang

Session 04. M3. 170 minutes.

[PDF](S04_Regression_and_Marketing_Interpretation.pdf) | [LaTeX](S04_Regression_and_Marketing_Interpretation.tex) | [Session Plan](SESSION_PLAN.md)

## Learning Objectives

- Interpret coefficients with units and conditioning.
- Diagnose omitted variables, interactions, and dependence.
- Reproduce an association while preserving its time and sample definitions.
- Distinguish a primary response coefficient from source bias.
- Justify controls and sample restrictions through a causal structure.

## Related Materials

- [M3 lecture notes](../06_Lecture_Notes/modules/M03_Regression.md)
- [Runnable small examples](../03_Data_and_Code/Lecture_Examples/session_examples.py)
- [mHealth regression code](../03_Data_and_Code/mHealth/recurring_examples/m03.py)
- [Ethics and regulation](../06_Lecture_Notes/ETHICS_AND_REGULATION.md)
- [Human and Synthetic Evidence](../03_Data_and_Code/Auxiliary_Data/README.md)
- [Auxiliary Data: Optional Practice](../07_Labs/Auxiliary_Data/README.md)
- [Digital Usage and Customer Access](../03_Data_and_Code/Digital_Usage/README.md)
- [Statistical Inference: Code and Results](../03_Data_and_Code/Statistical_Inference/README.md)
- [Statistical Evidence: Optional Practice](../07_Labs/Statistical_Inference/README.md)
- [Coding Workflows: Published Evidence](../01_Resources/40_Econometric_Coding_Workflows/README.md)
- [Coding Workflows: Python and Checks](../03_Data_and_Code/Agent_Workflows/README.md)
- ../01_Resources/41_Statistical_Claims_and_Decisions/README.md
- [Bad Controls and Project Exposure](../01_Resources/44_Bad_Controls_and_Project_Exposure/README.md)
- [Optional Research-Design Practice](../07_Labs/Bad_Controls/README.md)

## Slide 1: Regression and Marketing Interpretation

Marketing Analytics. By Nathan Yang.

## Slide 2: Competitors and Store Sales

- Stores in markets with more competitors can have higher sales.
- Demand attracts firms and also raises sales.
- The managerial question concerns the effect of an additional competitor.

A positive cross-market association can combine the negative competitive effect with the selection of firms into high-demand markets. The mechanism determines which comparison is informative.

Source: M3, Section 3.3, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M03_Regression.md

## Slide 3: A Conditional Mean

Relate store sales to observed marketing conditions.

$$
Y_i=\beta_0+\beta_1 X_i+\beta_2 Z_i+u_i
$$

The coefficient on $X_i$ describes its linear association holding included $Z_i$ fixed.

The outcome and regressors require explicit units and timing. A conditional association becomes a causal parameter only under the assumptions supplied by the design and model.

Source: M3, Section 3.1, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M03_Regression.md

## Slide 4: Ordinary Least Squares

- OLS chooses coefficients to minimize squared residuals.
- A residual is observed sales minus fitted sales.
- The model summarizes the comparison supplied by the data.

The fitted residuals sum to zero when an intercept is included and the usual OLS solution exists. This algebraic property does not establish independence between treatment and unobserved demand.

Source: M3, Section 3.1, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M03_Regression.md

## Slide 5: Omitted Demand Reverses the Sign

Synthetic markets hold the underlying competitive mechanism fixed.

**Figure description:** Within-demand comparisons show a different relationship from the pooled trend because high-demand markets attract more competitors.

[Editable TikZ](../06_Lecture_Notes/figures/M03_omitted_demand.tex)

Market demand affects both entry and sales. Controlling for a valid measure of demand can change the regression coefficient by changing which observations are compared.

Source: M3, Section 3.3, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M03_Regression.md

## Slide 6: Omitted-Variable Bias

Suppose demand $Z$ affects sales and is omitted from a regression on $X$.

$$
\widetilde\beta_1=\beta_1+\beta_2\frac{\Cov(X,Z)}{\Var(X)}
$$

The omitted association can offset or reverse the coefficient of interest.

This expression is the population linear-projection result under the stated model and orthogonality conditions. Its sign depends on both the effect of Z and its association with X.

Source: M3, Section 3.2, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M03_Regression.md

## Slide 7: Price and Sales Units

- A level coefficient is sales units per dollar.
- A log-log price coefficient is an elasticity under the model.
- The exact change for a log outcome uses an exponential transformation.

A coefficient on a binary regressor in a log-outcome model implies a multiplicative change of exp(beta)-1 under the relevant conditional interpretation. A percentage-point change in a probability is a different unit.

Source: M3, Section 3.4, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M03_Regression.md

## Slide 8: Interactions

Allow a message association to vary with account tenure $T$.

$$
Y=\beta_0+\beta_1 M+\beta_2 T+\beta_3 MT+u
$$

The message comparison at tenure $T$ is $\beta_1+\beta_3T$.

The main message coefficient applies at tenure zero under this parameterization. Centering tenure changes that reference point while leaving fitted values unchanged.

Source: M3, Section 3.5, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M03_Regression.md

## Slide 9: A Comparison Changes with Tenure

Synthetic message-response model. Tenure determines the conditional comparison.

**Figure description:** The interaction changes the slope of the message comparison across customer tenure. A single main coefficient describes only the chosen reference tenure.

[Editable TikZ](../06_Lecture_Notes/figures/M03_interaction.tex)

The marginal comparison should be reported at meaningful tenures within the observed support. A crossing outside the sample range is an extrapolation.

Source: M3, Section 3.5, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M03_Regression.md

## Slide 10: Uncertainty and Practical Importance

- Report effect size in managerial units.
- Cluster at the unit that shares outcome disturbances or assignment.
- Compare the interval with a decision-relevant magnitude.

A small p-value does not measure the size of an effect. A wide interval containing zero can also contain large economically consequential effects. The appropriate sampling unit depends on the design.

Source: M3, Section 3.6, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M03_Regression.md

## Slide 11: P-Values Vary Across Experiments

Fixed true effects; independent synthetic store experiments.

**Figure description:** The zero-effect distribution is approximately uniform. An eight-dollar effect produces more small p-values with 160 stores than with 40 stores.

[Editable TikZ](../06_Lecture_Notes/figures/M03_pvalue_distributions.tex)

Twenty thousand experiments per scenario use independent Gaussian store means and balanced assignment. For an eight-dollar effect, rejection rates are 32.5% with 40 stores and 86.6% with 160. An independent repeat has the same fixed-effect power, including after a first rejection. One minus the observed p-value is not a replication probability. Discrete tests and approximate null distributions need their own calibration.

Source: M3 §3.19. ../06_Lecture_Notes/modules/M03_Regression.md

## Slide 12: A Price Average Leaves Household Burdens Unresolved

- The outcome is quarterly residential revenue divided by MWh sold.
- A USD 2/MWh average increase permits different allocations across households.
- Bill payments do not establish endorsement of the allocation rule.

The recurring electricity case concerns the October 2026 electricity paper (Rana et al., 2026). Its residential sample has 41 treated utilities and 627 utility-quarter observations. A synthetic example holds 1,000 households and one MWh each fixed: USD 2 more for everyone and USD 20 more for 100 households yield the same average. Fixed charges and riders can enter revenue. Distribution, comprehension, and authority need separate evidence. Complete calculations are in M6 §6.33.

Source: M2 §2.28 and M3 §3.19. ../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md

## Slide 13: mHealth: Same Change, Different Precision

| Uncertainty Unit | SE (pp) | Two-Sided p |
| --- | --- | --- |
| Paired Users | 1.379 | 0.000237 |
| Independent Days | 0.663 | 1.13e-14 |

340 users; June minus May 2016 logging: −5.123 pp.

Membership requires a recorded day before May within the established pseudonym-based cohort, with all zero-log users retained. May and June contribute 31 and 30 calendar days respectively. Accounting for the pairing produces a Student interval with 339 degrees of freedom of [-7.835, -2.411] percentage points, while deliberately treating the days as independent gives [-6.423, -3.823]. Both reject zero, illustrating why agreement on a decision can conceal an error in precision. The comparison describes a temporal change because no intervention assignment is observed.

Source: M3 §3.18. ../06_Lecture_Notes/modules/M03_Regression.md

## Slide 14: What the Logging Test Establishes

- Preserve the roster and distinct user-day counts.
- Carry both months together for each user.
- Justify the independence and reference distribution.
- Connect the result to observed logging and its units.

An absent entry is zero recorded logging, with food consumption unobserved. The paired test treats users as independent draws from a common paired-outcome distribution and does not incorporate platform-wide shocks. Inspect the code that constructs the standard error; a customer-level label is insufficient. The previously shown paired bootstrap uses a different interval construction from the Student interval here. Full reconstruction code appears in M3 §3.18.

Source: M3 §3.18. ../06_Lecture_Notes/modules/M03_Regression.md

## Slide 15: A Matching Coefficient Leaves the Variance Unchecked

- Preserve each user's two months together.
- Verify the uncertainty calculation separately from the estimated change.
- Compare with an intentionally independent-day calculation.
- State what the descriptive change supports.

M3 §3.18 reports the same June-minus-May estimate under both calculations. A coefficient-only checker accepts both, while the standard errors, intervals, and p-values differ. The coding benchmark motivates explicit assessment of each requested quantity. The required paired calculation follows the fixed measurement question and its user-level dependence. Statistical agreement does not establish an intervention effect.

Source: Original course example. Workflow motivation: (Galiani et al., 2026). ../01_Resources/40_Econometric_Coding_Workflows/README.md

## Slide 16: Panel Comparisons

- Customer effects absorb stable customer characteristics.
- Time effects absorb shocks shared within a period.
- Time-varying confounding can remain.

Fixed effects change the variation used for estimation. Stable preferences can be absorbed, while unobserved events that change both behavior and outcomes can still confound the within-customer association.

Source: M3, Section 3.7, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M03_Regression.md

## Slide 17: mHealth: The Next Calendar Day

- Relate recorded category breadth to next-day recorded calories.
- Match exact adjacent calendar dates.
- State the included users, days, and calorie restrictions.

The next observed row can be several days later. Calling it next-day intake would change the time horizon. The food logs identify recorded quantities, and the regression remains an association.

Source: M3, Section 3.10, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M03_Regression.md

## Slide 18: Screening and the Estimated Association

mHealth estimates retain the stated outcome timing and sample restrictions.

**Figure description:** The figure compares the association under the base sample and an imposed calorie-range restriction. The sample rule changes the observed support.

[Editable TikZ](../06_Lecture_Notes/figures/M03_mhealth_association.tex)

A robustness comparison should report which rows change and whether the estimand remains comparable. The range restriction is an imposed screen, not proof that excluded records are incorrect.

Source: M3, Section 3.10, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M03_Regression.md

## Slide 19: A Hand-Checkable Regression

Synthetic sales follow a linear relationship.

```python
x = [1, 2, 3, 4]
y = [3, 5, 7, 9]
mx, my = sum(x) / 4, sum(y) / 4
b = sum((a-mx)*(v-my) for a,v in zip(x,y))
b /= sum((a-mx)**2 for a in x)
a = my - b * mx
assert (a, b) == (1.0, 2.0)
```

The intercept is 1 and the slope is 2 sales units per unit of x.

This example checks the covariance-over-variance calculation. Perfect fit is imposed by construction and is not an empirical finding about marketing behavior.

Source: M3, Section 3.1, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M03_Regression.md

## Slide 20: Coding Exercise: Regression Checks

- Generate a model after defining the outcome and information set.
- Verify the coefficient units and one fitted value manually.
- Compare pooled and customer-effect specifications.
- Inspect residuals, outliers, and sample changes.

Run the small OLS case in session_examples.py in the Lecture Examples folder S04. The mHealth m03.py program supplies the full real-data calculation, including exact-date pairing and clustered inference.

Source: M3, Section 3.8, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M03_Regression.md

## Slide 21: Prices Respond to Demand

- Managers can raise prices when demand is unusually strong.
- An observed price-sales regression can mix demand and pricing choices.
- An instrument needs relevance and a defensible exclusion restriction.

The course price simulation sets the true elasticity and the source of price endogeneity explicitly. A cost shifter is useful as an instrument only when its other paths to demand can be ruled out under the maintained setting.

Source: M3, Section 3.12, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M03_Regression.md

## Slide 22: Evidence for an Advertised Claim

- A claim that a product cuts costs needs a suitable comparison.
- An association can reflect selection and omitted demand.
- The evidence should support the express and implied claim before publication.

The FTC advertising-substantiation policy requires a reasonable basis for objective claims before dissemination. The necessary support depends on the claim and consequences. This does not turn every regression into an advertising substantiation study.

Source: FTC Policy Statement Regarding Advertising Substantiation. https://www.ftc.gov/legal-library/browse/ftc-policy-statement-regarding-advertising-substantiation

## Slide 23: Response Coefficients and Source Bias

- A synthetic price comparison combines customer response with price bias.
- A feature comparison survives when bias stays fixed across feature levels.
- Primary observations separate the response from the confounded bias.

The four-profile model uses response features (1, feature, price) and auxiliary bias features (1, price). Unknown unrestricted price bias can offset a change in the primary price coefficient. Repetition reduces variance without resolving that confounding. M4 Section 4.24 supplies the full invented example and Python. This coefficient-identification result does not itself establish a causal purchasing effect.

Source: (Jasin et al., 2026). https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7734298

## Slide 24: Controls Change the Income Comparison

The CCI income association changes sign after adjustment.

**Figure description:** MCI income coefficients decline from 0.05521 to 0.00209 and 0.00132; CCI changes from 0.04856 to -0.01821 and -0.01750 after controls and state effects.

[Editable TikZ](../06_Lecture_Notes/figures/M03_digital_controls.tex)

The slope measures index units per USD 10,000 of area median household income in 2021 dollars. Education is the college-degree share among adults 25 or older, and broadband is a household share. Keeping the records fixed while adding these controls changes the association represented by income. A causal interpretation would require a design that identifies an income intervention.

Source: (Pereira et al., 2026); original course calculations. ../01_Resources/38_Digital_Usage_and_Inclusion/README.md

## Slide 25: State the Population Behind a Coefficient

- Equal ZIP weights describe the released geographic sample.
- Household weights change the geographic projection.
- An assistance effect needs an intervention and customer outcomes.

Household estimates do not supply Windows device counts. State intercepts allow different average levels but do not remove every unobserved source of variation. The calculation does not propagate ACS sampling error, differential-privacy noise, or spatial dependence. An improved residual fit supplies no causal identification.

Source: (Pereira et al., 2026); original course calculations. ../01_Resources/38_Digital_Usage_and_Inclusion/README.md

## Slide 26: Controls Need a Causal Role

Adjustment can remove confounding, remove a mechanism, or create selection.

**Figure description:** Four graphs compare a confounder, mediator, collider, and instrument-like predictor. Candidate controls are outlined in orange.

[Editable TikZ](figures/bad_control_paths.tex)

The role is defined relative to an intervention and outcome. Timing and predictive power alone do not justify adjustment. Competing graphs require institutional evidence. The pre-treatment collider and instrument-like examples show why simply retaining every early covariate is insufficient.

Source: ../01_Resources/44_Bad_Controls_and_Project_Exposure/README.md

## Slide 27: More Controls Can Change the Answer

| Synthetic Case | Unadjusted | Adjusted |
| --- | --- | --- |
| Mediator | 7 | 1 |
| Collider | 0 | −1 |
| Instrument-Like Control | 1.18 | 2 |
| Measured Confounder | 1.18 | 1 |

Exact finite populations; slopes in outcome units per treatment unit.

The mediator model has total effect 7 and direct effect 1. The collider model has true effect zero. The final two rows share a true effect of 1: conditioning on the instrument-like variable amplifies residual confounding; observing the confounder removes it. Full code and all observations are in Bad_Controls/control_paths.py.

Source: ../03_Data_and_Code/Bad_Controls/README.md

## Slide 28: A Smaller Coefficient Needs an Explanation

- Define the total or direct effect before adjustment.
- Explain which paths the covariate closes or opens.
- Treat completion and response restrictions as conditioning.

A realized mediator coefficient need not be a controlled direct effect. A direct-effect interpretation requires additional identification and support conditions. Restricting to completed projects may select on viability and opposition; the graph and links to the outcome need evidence.

Source: ../01_Resources/44_Bad_Controls_and_Project_Exposure/README.md

## Slide 29: Regression Discussion

- Which comparison supports the coefficient?
- What variable could reverse its interpretation?
- Would the recommended action change across the reported interval?

A useful interpretation identifies the sample, units, conditioning, and causal scope before a recommendation. The source of variation matters as much as the regression command.

Source: M3, Section 3.8, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M03_Regression.md
