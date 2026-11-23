# Bias Geometry and the Value of Auxiliary Data

Stefanus Jasin, Meichun Lin, and Zijin Zhang. Working paper, written November 20, 2026; SSRN revision dated November 22, 2026. [Source](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7734298). Reviewed November 23, 2026.

## The Data-Collection Decision

A firm chooses how many responses to collect from each source at each product profile. Its objective is to minimize sampling cost while estimating the primary response model's coefficient vector to a specified mean squared error. Primary responses provide information about customer preferences. Auxiliary responses are cheaper or less noisy but can contain systematic bias. The contribution is a characterization of which preference comparisons survive that bias and how to allocate observations accordingly.

For profile $j$, the paper specifies the conditional means

$$
E[Y_j^P]=x_j^\top\beta,\qquad
E[Y_j^A]=x_j^\top\beta+z_j^\top\gamma.
$$

Here $P$ denotes the primary source, $A$ the auxiliary source, $x_j$ the response features, and $z_j$ the bias features. The unknown vectors $\beta$ and $\gamma$ govern the primary response and auxiliary bias. Both feature dictionaries are known. Bias coefficients can have any magnitude. Observations have independent Gaussian errors across responses and sources, with a common variance within each source. The baseline assumes known variances; §7.1 supplies a separate pilot procedure for unknown variances. The loss sums squared errors across the coefficients in the specified coding. This objective requires explicit units and scaling when applied to a new managerial decision.

## Bias Can Preserve Some Comparisons

Theorem 2 distinguishes three relationships between the column spaces of the response matrix $X$ and bias matrix $Z$. If every response pattern can also be produced by bias, auxiliary observations supply no additional information about $\beta$ under the paper's unrestricted-bias, worst-case criterion. If some response patterns can be separated, synthetic observations can reduce the cost of estimating those components, while human observations identify the remaining components. If the spaces intersect only at zero, auxiliary observations alone can identify the full vector within the model. Cost savings approach 100% as their relative information cost approaches zero in that last case.

This result concerns the allowed pattern of bias. A large overall optimism shift can cancel when comparing two features at the same price. A small realized price distortion can still leave true price sensitivity unidentified if the model allows an unrestricted unknown price bias. More repetitions reduce sampling variance without resolving that confounding. The dimension of the overlap does not, by itself, give the percentage of costs saved; design points, feature coding, noise, and the loss also matter.

The useful quantity for comparing source costs is

$$
\lambda=\frac{c_A\sigma_A^2}{c_P\sigma_P^2},
$$

where $c_i$ is cost per observation and $\sigma_i^2$ is its noise variance. Lower cost and lower variance both reduce this ratio. Low variance describes repeated responses within a source and can coexist with systematic errors about customers. Lemma 2 and Theorem 2 therefore support evaluating cost, noise, and bias structure jointly.

## A Fixed Design Can Be Efficient

Theorem 1 shows that a design chosen in advance achieves the optimal leading sampling cost as the MSE target approaches zero. Weighted least squares estimates response and bias coefficients jointly. The information matrix depends on the known features, variances, and allocation, which explains why observing response values offers no first-order cost advantage in this setting.

This is a useful comparison with adaptive A/B testing in M6. Its objective is precise coefficient estimation under a known linear information structure. Revenue optimization during experimentation, unknown response structure, and nonlinear choice models change that problem. The paper identifies nonlinear models, alternative estimands, and correlated observations as extensions in §8.

## The Two Retrospective Cases

Section 6 first fits human responses, then models the difference between LLM responses and fitted human responses. Features are selected at the 1% significance level; the bias regression uses Murphy–Topel standard errors to account for the estimated first stage. The resulting feature dictionaries and residual variances calibrate the design problem. Estimation-error comparisons simulate 100 paths from these calibrated models.

| Case | Observed Material Used for Calibration | Selected Geometry | Reported Cost Constants and Savings |
|---|---|---|---|
| Tea conjoint | 100 respondents rate 13 profiles, giving 1,300 ratings; the authors generate 1,300 corresponding LLM ratings. The allocation uses 10 distinct profiles. | Five response features and five bias features; two overlapping directions. | Primary-only 210.6; mixed 54.8; approximately 74% lower asymptotic sampling cost. |
| Digital twins | The underlying Twin-2k-500 study contains 2,058 U.S. adults. This application models an ordinal response to a hypothetical vaccination tradeoff, using human responses and their digital twins; the design uses 45 profiles. | Five response features and five bias features; four overlapping directions. | Primary-only 20.63; mixed 13.97; approximately 32% lower asymptotic sampling cost. |

Both comparisons set $c_P=1$ and $c_A=0.01$. The paper does not separately report a final complete-case count for the digital-twin regression in the inspected case description. The reported constants imply savings of 73.98% and 32.28%, respectively. These calculations recover ratios from rounded published constants; they do not reproduce the fitted models or semidefinite optimization. Table 1 reports variance pairs of 8.873 and 0.187 for tea, and 0.881 and 0.096 for digital twins. Consequently, the two information-cost ratios are approximately 0.000211 and 0.001090, rather than 0.01.

The case results establish what the calibrated models imply. Prospective savings would also depend on the stability of the selected feature dictionaries, independent human validation, and the costs of developing and maintaining the auxiliary source. The digital twins are constructed from earlier human survey waves; the per-response cost comparison does not separately price that initial collection and construction in §6.

## Feature Selection is an Important Teaching Opportunity

The formal model treats the bias dictionary as known. Empirical nonrejection of a candidate bias coefficient does not establish that the corresponding bias is exactly zero. Table 1 excludes the leafy-tea bias with a reported p-value of 0.041 and the Republican-indicator bias with a p-value of 0.034 because both exceed the chosen 0.01 threshold. Those exclusions affect which response components the auxiliary source can identify.

A useful sensitivity exercise follows directly from Table 1, Panel B. Hold its five primary features fixed: intercept, female, college degree, Democrat, and Republican. Its selected bias dictionary includes the first four, plus income. Adding the Republican indicator to that bias dictionary makes it contain every primary feature. Theorem 2 then gives zero auxiliary value under that expanded unrestricted-bias model. This is a course sensitivity calculation, not an alternative empirical estimate. Changing the selection threshold for both regressions would also change the primary model and requires a separate calculation.

The paper reports qualitatively similar results under backward elimination and cross-validation selection. The course exercise examines a different question: how the conclusion changes when a plausible omitted bias feature is admitted while preserving the estimand. An independent validation sample and a substantively justified sensitivity dictionary would help assess that restriction. Selecting features and simulating from the selected model cannot establish the absence of omitted bias.

## Respondents, Repeated Ratings, and Customer Representation

The theoretical guarantee assumes independent observations. The tea application has repeated ratings by the same human respondents, and the digital-twin application links synthetic responses to earlier information about individuals. Dependence may therefore matter when transporting the theoretical allocation to these settings. Section 8 explicitly leaves correlated primary and auxiliary observations for future work. Course code should distinguish a new respondent from another response generated for an existing persona and use respondent-level splits when evaluating human generalization.

For Marketing Dialectics, the associated question is who supplies evidence about customer interests. A model that recovers selected mean response coefficients still needs a separate justification for representing a population, interpreting consent, or inferring consumer welfare. Those are course implications of the estimation target's scope, rather than ethical conclusions tested in this paper.

## Reading and Verification Scope

The review covers the main text, §§1–8, Algorithms and Theorems cited above, Table 1, and Figures 1–3. Pages 20–21 and 24–25 were visually inspected to verify geometry, formulas, and empirical labels. The full appendix was extracted for reference; its proofs were not independently verified. No replication repository was identified in the inspected PDF or SSRN record. No author code or survey microdata was executed.

[source_checks.py](source_checks.py) contains original calculations for the rounded cost ratios and the closed-form example, together with the synthetic sensitivity calculations described in [CASE_DESIGN.md](CASE_DESIGN.md). The PDF's hash and access record are in [catalog.json](catalog.json).
