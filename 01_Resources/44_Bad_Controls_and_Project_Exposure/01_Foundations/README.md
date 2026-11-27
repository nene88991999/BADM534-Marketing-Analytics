# Foundations and Causal Graphs

[Collection Index](../README.md) | [Catalog](../catalog.json)

## BC01: Mostly Harmless Econometrics

Joshua D. Angrist; Jörn-Steffen Pischke. Princeton University Press, 2009; §3.2.3.

[Original source](https://press.princeton.edu/books/paperback/9780691120355/mostly-harmless-econometrics)

**Read:** §3.2.3, bad controls; book not downloaded.

The occupation example makes the target effect decisive: schooling can alter occupation, so comparing workers within their realized occupation need not recover the overall effect of schooling. Use as a foundational reference alongside accessible graphical treatments.

**Access and scope:** Book metadata and section reference verified; full chapter not inspected in this collection.

## BC02: A Crash Course in Good and Bad Controls

Carlos Cinelli; Andrew Forney; Judea Pearl. Author manuscript, March 21, 2022; published DOI 10.1177/00491241221099552.

[Original source](https://doi.org/10.1177/00491241221099552) | [Public PDF](https://carloscinelli.com/files/Cinelli%20et%20al%20-%20A%20Crash%20Course%20in%20Good%20and%20Bad%20Controls.pdf)

**Read:** Models 1–17; total versus direct effects.

Classify adjustment by causal paths. A mediator can remove part of a total effect; a collider can create an association; some controls change precision without bias. Measurement before treatment is neither a complete justification nor a necessary condition for harmless adjustment.

**Access and scope:** Selected full-text models and appendix inspected.

## BC07: To Adjust or Not to Adjust? Sensitivity Analysis of M-Bias and Butterfly-Bias

Peng Ding; Luke W. Miratrix. arXiv:1408.0324v1, August 2, 2014; related Journal of Causal Inference article, 2015.

[Original source](https://arxiv.org/abs/1408.0324) | [Public PDF](https://arxiv.org/pdf/1408.0324)

**Read:** M-structure, departures from the M-structure, butterfly structure.

A pre-treatment collider can induce bias. The analysis also warns that plausible departures from a pure M-structure can make confounding more consequential than M-bias. Draw competing graphs and compare sensitivity rather than applying a universal ban on adjustment.

**Access and scope:** Author preprint v1, August 2, 2014; abstract and setup inspected.

## BC08: Invited Commentary: Understanding Bias Amplification

Judea Pearl. American Journal of Epidemiology, 2011, 174(11), 1223–1227.

[Original source](https://doi.org/10.1093/aje/kwr352) | [Public PDF](https://ftp.cs.ucla.edu/pub/stat_ser/r386.pdf)

**Read:** Bias amplification and covariate comparisons.

An instrument-like predictor can remove treatment variation unrelated to the omitted confounder and amplify the remaining confounding bias. Its strong prediction of treatment does not establish that conditioning on it improves causal identification.

**Access and scope:** Author technical report R-386; opening argument inspected.

## BC09: Principles of Confounder Selection

Tyler J. VanderWeele. European Journal of Epidemiology, 2019, 34, 211–219.

[Original source](https://doi.org/10.1007/s10654-019-00494-6) | [Public PDF](https://link.springer.com/content/pdf/10.1007/s10654-019-00494-6.pdf)

**Read:** Modified disjunctive cause criterion.

Use causal knowledge about exposure causes, outcome causes, instruments, and proxies to justify selection. Predictive strength and statistical significance do not determine which role a variable plays. The criterion carries causal and measurement premises.

**Access and scope:** Springer copy, corrected publication 2021; selection discussion inspected.

## BC10: Statistical Control Requires Causal Justification

Anna C. Wysocki; Katherine M. Lawson; Mijke Rhemtulla. Advances in Methods and Practices in Psychological Science, 2022, 5(2).

[Original source](https://doi.org/10.1177/25152459221095823) | [Public PDF](https://journals.sagepub.com/doi/pdf/10.1177/25152459221095823)

**Read:** Causal justification and applied example.

A partial coefficient receives its causal interpretation from a defended structure. Proxies, mediators, confounders, and colliders can produce different implications despite similar correlations. Prediction and causal explanation require different variable-selection arguments.

**Access and scope:** Publisher HTML inspected; PDF request returned HTTP 403. Article carries CC BY-NC 4.0.

## BC12: Making Sense of Sensitivity: Extending Omitted Variable Bias

Carlos Cinelli; Chad Hazlett. JRSS B, 2020, 82(1), 39–67.

[Original source](https://doi.org/10.1111/rssb.12348) | [Public PDF](https://escholarship.org/content/qt0pg6471b/qt0pg6471b.pdf?t=rhi25k)

**Read:** Omitted-variable sensitivity and partial R-squared.

Quantify how strong omitted confounding would need to be to alter an estimate. Choose a causally justified starting specification and credible benchmarks. Sensitivity analysis does not validate an inappropriate mediator adjustment or an incorrectly defined comparison population.

**Access and scope:** Author copy; abstract and sensitivity setup inspected.
