# Heterogeneity and Consumer Protection

A firm can fit heterogeneous responses accurately while leaving the source of those responses unresolved. This example reanalyzes released retail-account data and constructs two explanations with exactly the same likelihood. It connects model fit to the evidence and reasons required before a consumer complaint can be dismissed.

## Data and Provenance

The `bayesm` 3.1-7 package attributes its `cheese` dataset to the trade-promotion study (Boatwright et al., 1999). The released file has 5,555 weekly observations for 88 retailer–market accounts, with Borden unit sales, price in US dollars, and display activity. All released rows and columns are retained. The upstream R object, documentation, package description, GPL license, conversion script, pinned commit, and hashes accompany the CSV. See [PROVENANCE.json](PROVENANCE.json) and the [data dictionary](DATA_DICTIONARY.md).

This is a reanalysis of a public dataset attributed to the study. The January 1999 preprint describes 77 accounts and a Kraft application with additional variables; the public package describes 88 accounts and Borden sales. The mapping is unresolved. The exercise therefore makes no claim to reproduce a published table or the paper's constrained hierarchical sampler. The package provides a concrete research-data example with an explicit replication boundary.

## Run the Example

Python 3 with NumPy, pandas, and SciPy is required. The provided CSV permits execution without R. To reproduce the extraction from the original object, run `Rscript 03_Data_and_Code/Heterogeneity_and_Consumer_Protection/convert_data.R` from the repository root.

```sh
python3 03_Data_and_Code/Heterogeneity_and_Consumer_Protection/heterogeneity_reanalysis.py
python3 03_Data_and_Code/Heterogeneity_and_Consumer_Protection/test_reanalysis.py
```

The program runs account regressions of log unit sales on log price, an intercept, and display where display varies. It then integrates account coefficients under one- and two-component normal distributions, fitting their parameters by marginal maximum likelihood. The resulting conditional distributions are empirical Bayes. First-stage standard errors use an iid Gaussian working model; temporal dependence and uncertainty in fitted hyperparameters remain outside this calculation. These restrictions preclude using the reported precision as a validated measure of uncertainty about causal demand or conduct.

## Results and Interpretation

The one-component and two-component log likelihoods are -128.629 and -124.520. Their BIC values are 266.213 and 271.427, respectively, so BIC favors the simpler model despite the extra in-sample fit. Mean conditional account slopes are -2.138 and -2.151. The two positive OLS slopes become negative conditional means in both integrated models. This shrinkage illustrates how a distributional model changes the interpretation of noisy account estimates; it establishes no consumer benefit or injury.

The constructed mechanism decomposes the observed response as a latent taste component plus an imposed restriction component. Shifting the latent distribution offsets the imposed restriction exactly. Every account's marginal likelihood remains unchanged at restriction values 0, 0.25, 0.5, and 1. These values are synthetic explanatory scenarios applied to the fitted response distribution. They are not measured switching costs or findings of misconduct.

If a constructed harmless and harmful state generate the same observed-data distribution, any rule with a five-percent false-flag rate under the harmless state also flags only five percent under the harmful state. Its missed-harm rate is 95% in that construction. This is an identification result, not an estimated error rate for these retailers or a general property of Bayesian models. Additional observations capable of distinguishing the mechanisms can change the result.

## Decision and Philosophical Questions

The public record supports a comparison of response models. A conclusion about price discrimination, wrongdoing, or permissible conduct requires further economic and normative premises. Consumers with credible concerns about serious exposure may reasonably demand records or proportionate protection before investigators identify every aspect of heterogeneity. The argument compares their reasons with the burdens of the proposed response, including those of other customers and affected workers [(Scanlon, 1998, pp. 191–196)](https://e-edu.nbu.bg/pluginfile.php/314831/mod_resource/content/0/scanlon_5.1-3.pdf).

[M4 §4.31](../../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md) contains the derivation and complete Python. [M9 §§9.57.1–9.57.4](../../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md) distinguishes model-relative possibility, evidential support, and permission. [Optional practice](../../07_Labs/Evidence_Standards/README.md) asks students to defend a lower threshold for a specified protective action while preserving the assumptions needed for a factual allegation.

## Outputs and Verification

The [results guide](results/README.md) identifies each table and denominator. [VERIFICATION.md](VERIFICATION.md) records numerical checks, source fidelity, and the replication boundary. No upstream estimation code is executed. The course program is an original adaptation; source data and documentation retain the package's license and attribution.

## Precision and Missed Harm

Run `python3 03_Data_and_Code/Heterogeneity_and_Consumer_Protection/harm_elasticity.py` for the separate synthetic example in M6 §6.46. Partial pooling narrows posterior standard deviation from 1 to 0.5345 and lowers population-average MSE from 1 to 0.2857, while detection of the harmed group falls from 63.88% to 14.07% under a fixed one-sided posterior-credibility rule. Actual false-flag rates fall from 5% to 0.1045%. The harmed subgroup's MSE increases to 2.1224.

This is a precision comparison, with a population that includes ten percent harmed groups and a normal working prior. It is not bias reduction within the harmed group or an empirical harm finding in the retail data. The positive precision elasticity is 0.3999 at the pooled endpoint. Matching the actual false-positive rates recovers the same detection because the score transformation preserves information. These checks identify the joint role of pooling and the institutional decision rule.

The source algebra is (Gelman et al., 2012, pp. 196–198), [DOI](https://doi.org/10.1080/19345747.2011.618213). The consumer population, harms, loss function, and elasticity are original course constructions. M9 §9.57.5 connects the result to reasonable protection and the data-center reassurance critique.

## Method Correspondence

The [method crosswalk](METHOD_CROSSWALK.md) traces the hierarchical loop to `runiregG`, derives the matrix posterior, and verifies the scalar conditional identity numerically. Source files and hashes are retained; no upstream sampler was executed. The known-harm example changes this conditional update and the associated decision threshold, with full hyperparameter uncertainty outside its scope.
