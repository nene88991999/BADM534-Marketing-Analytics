# Source Review: Semantic Similarity Rating

## Paper, Version, and Evidence

Benjamin F. Maier, Ulf Aslak, Luca Fiaschi, Nina Rismal, Kemble Fletcher, Christian C. Luhmann, Robbie Dow, Kli Pappas, and Thomas V. Wiecki, *LLMs Reproduce Human Purchase Intent via Semantic Similarity Elicitation of Likert Ratings*, [arXiv:2510.08338v3](https://arxiv.org/abs/2510.08338v3), October 27, 2025. The first version appeared October 9, 2025. The unchanged PDF is distributed under the [CC BY 4.0 license](https://creativecommons.org/licenses/by/4.0/) linked by arXiv.

The main text, methods in Appendix A, stimulus description in Appendix B, implementation material in Appendix C, and LightGBM comparison in Appendix D were read. Figure 1 and Table 1 were visually checked. This companion summarizes the method and selected comparisons; it omits the full bibliography, all response examples, and most supplementary distributions. Figure 1 separates direct ratings, follow-up ratings, and embedding-based mappings. Table 1 separates stimulus, demographics, generation temperature, anchor selection, and performance metric.

There are 57 distinct concepts and 9,300 participants, with no participant appearing in multiple surveys. The LLMs receive the corresponding available demographics and concept stimulus; two generated responses are sampled per persona. Human outcomes are stated purchase-intent ratings on categories 1–5. The data come from one corporation's U.S. personal-care research. The scope supports a comparison in that setting, with further population and domain validation required for transfer.

## Mapping and Aggregation

For response text c, anchor set a, and category r, let s(c,a,r) be the cosine similarity of the response and anchor embeddings. At the study's epsilon of zero and SSR temperature of one, the category weight is

`p(c,a,r) = [s(c,a,r) - min_j s(c,a,j)] / sum_k [s(c,a,k) - min_j s(c,a,j)]`.

The numerator measures relative similarity above the least similar anchor. The denominator makes the five weights sum to one when there is a nonzero similarity spread. Average these weights over the six anchor sets, then over generated responses within a concept. A rating mean weights categories by the numerical scores 1–5. That scoring convention matters for the mean and its Pearson correlation. KS similarity uses the cumulative probabilities and depends on category order, without requiring equal distances between category labels.

The subtraction creates at least one zero weight within each anchor set. Identical similarities make the denominator zero. Neither normalization nor additional generated respondents establishes a probabilistic interpretation for real purchasing behavior. Within-answer mapping dispersion, differences across generated answers, and uncertainty about a population mean are distinct quantities.

## Correlation Attainment and Concept Screening

Appendix A.3 defines correlation attainment as `mean(R_human,synthetic) / mean(R_human,human)` over 2,000 random panel splits. It is a ratio of averages. Each correlation compares concept means across the 57 concepts. The human halves and sampled synthetic group have equal size within each concept. Table 1's reported Pearson correlation is a separate summary; dividing that displayed value by the attainment percentage does not reconstruct every step of the resampling procedure.

A split-half correlation is a useful noise benchmark, with no general mathematical guarantee that it bounds the correlation of every predictor with a noisy human mean. Consider an illustrative latent concept score with variance tau-squared, two independent measurement errors each with variance sigma-squared, and a predictor equal to the latent score. The human–human population correlation is `tau² / (tau² + sigma²)`, while predictor–human correlation is its square root. Their ratio exceeds one whenever the measurement error variance is positive. The [verification program](verify_measurement.py) checks a specified numerical example. This is an analytical illustration, not a reconstruction of the authors' data.

For concept screening, add measures tied to the decision: overlap of selected concepts, errors around the screening threshold, and missed strong concepts. Estimate those using new human outcomes. Keeping a random validation sample below the screening threshold makes false exclusions observable; testing only shortlisted concepts leaves that error unmeasured.

## Scope of the Reported Comparisons

The discussion explicitly states that the six reference sets were manually optimized on the 57 study surveys. A concept-level final evaluation should therefore hold out the human outcomes from anchor selection as well as from any parameter fitting. Repeated random splits of respondents within the same concepts do not establish transfer of an optimized measurement procedure to new concepts.

Table 1 reports KS similarity 0.88 for GPT-4o SSR and 0.80 for Gemini SSR under the full-demographic, image-stimulus, averaged-anchor, temperature-0.5 configuration. The abstract's statement above 0.85 is not uniform across models and configurations. For the Gemini image comparison without demographics, averaged anchors give 15.5% correlation attainment, while selecting the best individual anchor set gives 50.1%. Comparing a best-set result with an averaged-set result changes two choices at once.

The LightGBM exercise uses 300 splits of 28 training concepts and 29 evaluation concepts. Its inputs are five demographic attributes plus category, price tier, and concept source. The LLM receives the fuller product stimulus. The reported difference therefore combines information access, measurement choices, and modeling approach. It does not isolate the incremental effect of using an LLM with otherwise identical information.

Section 3.1 reports a cross-concept human-mean standard deviation of 0.1, while Appendix A.3 gives 0.2. The raw survey records were unavailable in the inspected release, so this review leaves that discrepancy unresolved. Neither value is used in the independent illustrative calculations.

## Repository Inspection

The [repository](https://github.com/pymc-labs/semantic-similarity-rating/tree/86dcd2597c7824e4fd6546b884c5500c43a4b022) was inspected at the June 4, 2026 commit `86dcd2597c7824e4fd6546b884c5500c43a4b022`. Eight files are archived: README, LICENSE, package metadata, three package modules, and two test files. All eight match the pinned Git blob hashes. The five Python files are syntax-parsed without importing them. The lockfile, automation files, and development configuration are omitted from this reference subset.

| Component | Observed Behavior | Implication for an Adaptation |
| --- | --- | --- |
| `ResponseRater` | Accepts existing text or supplied embeddings; automatic text mode loads `all-MiniLM-L6-v2` | Consumer-response generation is separate; the default embedding differs from the paper's `text-embedding-3-small` |
| `cosine_similarity_matrix` | Returns `(1 + cosine) / 2` | Minimum subtraction and normalization cancel this positive affine transformation when epsilon is zero |
| `similarities_to_pmf` | Adds positive epsilon only at the first minimum-similarity category | Epsilon is not uniform smoothing over all five categories; equal similarities with positive epsilon select the first minimum |
| `scale_pmfs` | Applies a power transform and normalization | Positive temperature preserves existing zero weights; scaling and averaging generally do not commute |
| Mean reference option | Averages anchor-set PMFs before temperature scaling | The study's temperature-one setting is unaffected; extensions should document the order of operations |
| `get_survey_response_pmf` | Averages response rows equally | Unequal repeat counts require an explicit choice between response and persona weighting |
| Tests | Examine shapes, normalization, reproducibility, and selected transformations | Passing software checks would leave external validity against human outcomes unresolved |

Source inspection identifies a zero-denominator boundary when all similarities are equal and epsilon is zero. Zero-length embedding vectors also lack an explicit guard before normalization. The independent calculations show the consequences of the documented arithmetic; they are not execution results from the package. A classroom adaptation should specify tie handling, invalid-input checks, and an abstention rule when the available information is uninformative.

The repository does not contain the human respondent dataset, complete original concept stimuli, study-generation scripts, or stored experiment results. The README supplies two generic agreement anchor sets. The paper describes constructing six purchase-intent sets, but a complete enumeration of those six sets was not found in the inspected paper and repository. This package supports method adaptation; the archived subset cannot reproduce the reported study.

The LICENSE file contains Apache-2.0 terms. README and `pyproject.toml` instead identify MIT. Package metadata gives version 1.1.0 while `__init__.py` reports 1.0.0. Preserve all original notices and identify the revision by commit hash. The README's older citation has a different title and incomplete author list; the catalog uses the nine-author arXiv record confirmed by Appendix C.2's repository link.

## Verification Record

[verify_measurement.py](verify_measurement.py) checks nine source hashes, parses five source modules and tests, and evaluates six independent arithmetic properties using imposed inputs. It writes [source_checks.json](source_checks.json). No downloaded code, upstream test, model download, API call, or package installation is part of this verification. The reading and checks were completed on November 22, 2026.
