# Premises, Counterexamples, and Supported Conclusions

A criticism should identify the exact inference that fails and the evidence that could repair it. The worked derivations, counterexamples, and complete Python appear in [M6 §6.34](../../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md) and [M9 §9.27](../../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md). The [optional lab](../../07_Labs/Statistical_Inference/README.md) asks students to reconstruct the arguments before evaluating them.

## Argument Record

| Evidence and Location | Stronger Interpretation to Assess | Missing Premise or Counterexample | Supported Conclusion |
|---|---|---|---|
| Table 2, col. 4: 0.261, SE 0.158 | Nonrejection at 5% establishes a negligible residential burden | At the reference exposure, a true USD 2/MWh increase still gives approximately 53% nonrejection under the fixed normal approximation | The estimate leaves meaningful positive effects unresolved; low power does not identify the true effect |
| Table 4, col. 4 and HBS public coverage | Four named owners have imposed no consumer price cost | Positive effects remain within the interval; 80% detection needs a slope of 0.448 USD/MWh per exposure pp | The imprecise four-owner slope does not support categorical harmlessness |
| Table 4 and p. 26: direct equality p = 0.101 | Different subgroup significance stars establish different effects | The direct contrast needs covariance and does not cross the stated 10% convention | Preserve the reported joint test and its uncertainty |
| Section 4.1 and Table A.2: four owners versus all others | The complement is a homogeneous leasing or colocation business model | An exhaustive ownership partition does not establish an operating-model classification | Test facility operations and contracts before interpreting the ownership effect as a mechanism |
| Page 3 and Table A.4: roughly 96% residual | Named causes account causally for that residual | Correct subtraction leaves components, interactions, and estimation error unassigned | Report the remainder as a remainder until a defensible decomposition is estimated |
| Table 7: sales slope 291, SE 493 | An infrastructure channel dominates because sales are insignificant | Substantial sales remain unresolved; even exact net zero could conceal offsetting loads or timing | The channel comparison requires joint evidence on costs, demand, displacement, and recovery |
| Section 4.2, p. 16: cost per MWh | The estimated ratio measures the model's total-cost numerator | Costs and sales can rise proportionally; falling sales can raise the ratio without higher total cost | Reconcile totals, denominators, samples, and timing |
| Historical coefficients and future interpretation | Historical fit establishes future small effects | Two synthetic functions agree throughout historical support but diverge beyond a capacity boundary | Extrapolation is conditional on stability and functional-form restrictions |
| Utility-average price and household claims | The mean establishes harmlessness for every household or legitimate authority | Equal averages permit different incidence; identical bills permit different rights of challenge | Assess distribution and decision procedures with the relevant additional evidence |

The first seven rows concern specific interpretations of the paper or verified public coverage. The final two rows assess broader extrapolations an audience might draw; they are not quotations asserting that the authors made every such claim. The paper's future qualifications and positive findings remain part of the evidence.

## Inverse Power and Detectable Effects

Inverse-power functions express sensitivity in departures from the tested restrictions [(Andrews, 1989)](https://doi.org/10.2307/1913623). The [1986 Cowles version](https://cowles.yale.edu/sites/default/files/2022-08/d0800.pdf) makes nuisance parameters and directions explicit. The course implements a fixed normal/Wald approximation with original code.

At a fixed target power and test size, the program solves for the noncentrality parameter and maps it into an effect or directional radius. It separately reports the confidence bounds from the realized estimates. A two-outcome synthetic example shows how detection depends on direction. A covariance matrix estimated from a different design, an arbitrary clustering multiplier, or an assumed correction inferred from marginal SEs would not establish the power of this paper's full estimator.

## Philosophical Connections

Validity concerns the relation between premises and conclusion. Soundness additionally concerns the premises. A counterexample establishes that a conclusion does not follow from the stated premises; deciding which account is empirically plausible requires further evidence. Distinguish existence of a compatible model from a result holding throughout a justified class.

Possibility, available action, information, and permission are separate objects in [(Pacuit and Simon, 2011)](https://doi.org/10.1017/S1755020311000190). The course applies that distinction to household participation and authority. The application does not attribute a judgment about the electricity paper to those philosophers.

The paired synthetic price functions and cost ratios are analytical counterexamples, not empirical estimates. Full original code is in [logical_counterexamples.py](../../03_Data_and_Code/Statistical_Inference/logical_counterexamples.py). Private instructor notes and manuscripts remain outside the public repository.

## Institutional Premises

A cancelled project with allowed recovery is a counterexample to the implication from zero operating additions to zero project costs. Unchanged revenue per MWh with greater use is a counterexample to the implication from flat average prices to flat household bills. These constructions establish failures of general entailment. Actual donor contamination, bill incidence, and causal effects require the records specified in the [institutional assessment](INSTITUTIONAL_ASSESSMENT.md).
