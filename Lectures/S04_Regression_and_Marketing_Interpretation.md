# Regression and Marketing Interpretation

By Nathan Yang

Session 04. M3. 170 minutes.

[PDF](S04_Regression_and_Marketing_Interpretation.pdf) | [LaTeX](S04_Regression_and_Marketing_Interpretation.tex) | [Session Plan](SESSION_PLAN.md)

## Learning Objectives

- Interpret coefficients with units and conditioning.
- Diagnose omitted variables, interactions, and dependence.
- Reproduce an association while preserving its time and sample definitions.

## Related Materials

- [M3 lecture notes](../06_Lecture_Notes/modules/M03_Regression.md)
- [Runnable small examples](../03_Data_and_Code/Lecture_Examples/session_examples.py)
- [mHealth regression code](../03_Data_and_Code/mHealth/recurring_examples/m03.py)
- [Ethics and regulation](../06_Lecture_Notes/ETHICS_AND_REGULATION.md)

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

## Slide 9: A Comparison Changes With Tenure

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

## Slide 11: Panel Comparisons

- Customer effects absorb stable customer characteristics.
- Time effects absorb shocks shared within a period.
- Time-varying confounding can remain.

Fixed effects change the variation used for estimation. Stable preferences can be absorbed, while unobserved events that change both behavior and outcomes can still confound the within-customer association.

Source: M3, Section 3.7, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M03_Regression.md

## Slide 12: mHealth: The Next Calendar Day

- Relate recorded category breadth to next-day recorded calories.
- Match exact adjacent calendar dates.
- State the included users, days, and calorie restrictions.

The next observed row can be several days later. Calling it next-day intake would change the time horizon. The food logs identify recorded quantities, and the regression remains an association.

Source: M3, Section 3.10, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M03_Regression.md

## Slide 13: Screening and the Estimated Association

mHealth estimates retain the stated outcome timing and sample restrictions.

**Figure description:** The figure compares the association under the base sample and an imposed calorie-range restriction. The sample rule changes the observed support.

[Editable TikZ](../06_Lecture_Notes/figures/M03_mhealth_association.tex)

A robustness comparison should report which rows change and whether the estimand remains comparable. The range restriction is an imposed screen, not proof that excluded records are incorrect.

Source: M3, Section 3.10, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M03_Regression.md

## Slide 14: A Hand-Checkable Regression

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

## Slide 15: Coding Exercise: Regression Checks

- Generate a model after defining the outcome and information set.
- Verify the coefficient units and one fitted value manually.
- Compare pooled and customer-effect specifications.
- Inspect residuals, outliers, and sample changes.

Run the small OLS case in ../03_Data_and_Code/Lecture_Examples/session_examples.py S04. The mHealth m03.py program supplies the full real-data calculation, including exact-date pairing and clustered inference.

Source: M3, Section 3.8, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M03_Regression.md

## Slide 16: Prices Respond to Demand

- Managers can raise prices when demand is unusually strong.
- An observed price-sales regression can mix demand and pricing choices.
- An instrument needs relevance and a defensible exclusion restriction.

The course price simulation sets the true elasticity and the source of price endogeneity explicitly. A cost shifter is useful as an instrument only when its other paths to demand can be ruled out under the maintained setting.

Source: M3, Section 3.12, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M03_Regression.md

## Slide 17: Evidence for an Advertised Claim

- A claim that a product cuts costs needs a suitable comparison.
- An association can reflect selection and omitted demand.
- The evidence should support the express and implied claim before publication.

The FTC advertising-substantiation policy requires a reasonable basis for objective claims before dissemination. The necessary support depends on the claim and consequences. This does not turn every regression into an advertising substantiation study.

Source: FTC Policy Statement Regarding Advertising Substantiation. https://www.ftc.gov/legal-library/browse/ftc-policy-statement-regarding-advertising-substantiation

## Slide 18: Regression Discussion

- Which comparison supports the coefficient?
- What variable could reverse its interpretation?
- Would the recommended action change across the reported interval?

A useful interpretation identifies the sample, units, conditioning, and causal scope before a recommendation. The source of variation matters as much as the regression command.

Source: M3, Section 3.8, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M03_Regression.md
