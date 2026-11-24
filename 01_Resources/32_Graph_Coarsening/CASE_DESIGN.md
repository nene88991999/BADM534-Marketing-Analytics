# Compressing a Retail Network Without Changing the Decision

A retail chain wants a smaller representation of its service network. The chain needs both a revenue summary and the share of customers who can reach an available outlet within five minutes. The same compressed graph may support one quantity and misrepresent the other.

## Four Zones and Two Supernodes

Consider four invented zones A, B, C, and D with equal populations. They form a path. Travel takes four minutes from A to B, one minute from B to C, and four minutes from C to D. An available store is at D. Weekly zone revenues are 10, 10, 10, and 40 dollars. These deliberately small values provide a transparent calculation, with no estimated demand or observed customer behavior.

Group A, B, and C together, and retain D as the second supernode. Binary lifting and its pseudoinverse give mean revenues of 10 and 40. Reconstructing the original revenue feature is exact. The mean across the two supernodes is 25, while the population mean across four equal-sized zones is 17.50. Weighting the group means by sizes three and one restores that mean. The total is 70; adding group means gives 50.

For the graph calculation, define affinity as the reciprocal of edge travel minutes. The original affinities are $1/4$, $1$, and $1/4$. These units differ from minutes. Summing affinities between groups leaves one coarse edge with weight $1/4$, after removal of within-group edges. The revenue feature has the same combinatorial Dirichlet energy, 225, before and after this aggregation. This equality concerns the specified block-constant feature and graph quadratic form.

Interpreting the reciprocal coarse edge as a four-minute trip discards travel within the first supernode. The actual trip from A to D takes nine minutes. At a five-minute threshold, B, C, and D have access, so the original equal-population share is 75%. Treating every zone in the first supernode as four minutes away raises the apparent share to 100%. The feature reconstruction and its energy remain exact throughout. Preserving those quantities does not establish preservation of the route comparison.

The [complete Python calculation](source_checks.py) constructs the matrices, compares the energies, enumerates shortest paths, and checks the access counts. [Saved outputs](source_checks.json) retain the units and results. No source package or neural network is used.

## A Connection to the Existing Retail Case

The [existing retail-access example](../../03_Data_and_Code/Retail_Accessibility/README.md) supplies a separate population check. Its disconnected origin remains in the 800-person denominator. A largest-component filter would discard 150 people and raise known access from 68.75% to 84.62% with no improvement for any person. Students can identify the relevant GraCo default, explain the changed estimand, and propose a representation that retains the original population.

The restaurant snapshot provides observed locations and recorded availability, but it does not supply customer residences or preferences. A later empirical extension would retain that distinction, freeze the street extract, preserve route units, and compare access at original origins. Applying a generic graph reduction to minute-valued edges without a justified transformation would change their meaning.

## Prediction and AI-Assisted Coding

Use the three-node label example in [SOURCE_REVIEW.md](SOURCE_REVIEW.md) to distinguish a partition's oracle purity from a classifier fitted on permitted information. Ask students to trace the labels used in `max_acc`, UGC's alpha calculation, and STPGC's guidance. A final evaluation set remains untouched while choosing the representation and its hyperparameters.

A useful coding prompt specifies the observation unit, edge direction and units, original population, permitted outcomes, target number of groups, and required outputs. The assistant must report achieved compression, excluded nodes, group sizes, and separate numerical and predictive checks. The student then verifies a hand-worked case and inspects the relevant source functions. The [optional practice](../../07_Labs/Graph_Coarsening/README.md) includes this exercise. The two original course programs and nine independent checks have run; no live assistant or upstream program has been evaluated here.

## Figures and Placement

An editable TikZ figure shows the four-zone path beside the two-supernode representation. Use Illinois navy for original nodes, orange group boundaries, and explicit travel-time labels. Its lower panel compares 75% original access with the incorrect 100% coarse interpretation, while showing that feature reconstruction is exact. Labels and shapes should carry the distinction alongside color.

The explanation and complete code appear in M5 §5.24 and M7 §7.38. M4 §4.22 connects group weights to segment summaries, M2 §2.23 connects preprocessing to measurement, and M9 §9.18.2 examines service responsibilities. Sessions 7 and 11 use existing meeting blocks, with fifteen and five minutes respectively. The optional practice includes the M1 AI-assisted coding workflow and creates no graded requirement.

For advanced students, compare a small number of GraCo methods against a simple aggregation baseline and the uncompressed graph at comparable achieved sizes. Evaluate the decision outcome at the original nodes, preserve the information split, and record runtime and memory. The full seventeen-method benchmark requires a separate computing budget; the paper's graph metrics and runtime results provide background for choosing that comparison.
