# Synthetic Consumers and Product Concept Testing

A product manager must choose which concepts receive a costly human-panel test. Generated consumer responses could help organize candidate ideas and anticipate objections. Their usefulness depends on whether they preserve the distinctions that matter for that decision, including which promising concepts a screening rule might discard.

[Maier and coauthors](https://arxiv.org/abs/2510.08338v3) study purchase-intent ratings for 57 personal-care concepts, using 9,300 U.S. human responses as the comparison. Each concept has a separate panel of 150–400 participants. The paper offers a particularly useful connection between product research in M4, text measurement in M5, and validation in M7. M8 §8.11 already introduces the distinction between summarizing generated answers and establishing validity against human outcomes.

## From Generated Text to a Rating Distribution

Semantic similarity rating, or SSR, starts with a generated written response to a product concept. An embedding represents that response and five reference statements corresponding to purchase-intent categories. The method subtracts the smallest similarity from each of the five similarities and normalizes the resulting values. Averaging the distributions from six reference sets produces the response-level distribution used in the study. The authors compare this procedure with asking directly for a numerical rating and with asking a second LLM instance to assign a rating to a written response.

This is a useful measurement example because the generated answer and its numerical representation are separate choices. A change in anchor wording, embedding model, or mapping rule can change the measured outcome while the answer remains fixed. The normalized values describe the mapping to response categories. Evidence that they are calibrated probabilities of actual consumer choices requires a separate comparison with people and behavior.

## What the Reported Performance Measures

The following values are transcribed from Table 1, page 14, for image stimuli, full available demographic conditioning, and generation temperature 0.5. SSR uses the average across reference sets. The comparison covers the 57 concepts; the observations entering the correlation are concept means.

| Model and Response Method | Correlation Attainment | Mean KS Similarity | Pearson Correlation of Concept Means |
| --- | ---: | ---: | ---: |
| GPT-4o, Direct Rating | 81.7% | 0.26 | 0.661 |
| GPT-4o, Follow-Up Rating | 84.7% | 0.72 | 0.687 |
| GPT-4o, SSR | 90.2% | 0.88 | 0.724 |
| Gemini 2.0 Flash, SSR | 90.6% | 0.80 | 0.720 |

Correlation attainment divides an average human–synthetic correlation by an average human–human correlation. The benchmark comes from 2,000 random splits of each existing human panel into halves. It is a split-half benchmark; the researchers did not observe a second wave of consumers taking the survey. The headline near 90% therefore concerns this ratio, rather than the percentage of individual ratings predicted correctly. The paper measures correlations of purchase-intent means, with no observed sales outcome.

Distribution similarity and concept discrimination answer different questions. For Gemini with image stimuli and averaged anchor sets, removing demographic conditioning raises mean KS similarity from 0.80 to 0.91 while reducing correlation attainment from 90.6% to 15.5%. A panel can reproduce a broadly positive response distribution while contributing little information about which concept performs better. These are reported comparisons within the paper's setting, not evidence that a demographic prompt reliably represents every population.

## Validation of the Complete Measurement Procedure

The discussion on page 7 states that the reference sets were manually optimized using the same 57 surveys. Generalization of those anchors to new surveys remains unestablished. The absence of language-model fine-tuning leaves substantial scope for adaptation through prompts, model selection, and measurement choices. A prospective evaluation would fix those choices before examining the human responses for new concepts.

The study concerns personal-care purchase intent. Its demographic comparisons describe associations within that sample, and its price-tier comparisons do not identify causal price effects or willingness to pay. Generated explanations can supply hypotheses about consumer concerns. Their detail and fluency do not establish that those concerns caused human choices. The LightGBM comparison also gives the models different information: eight coarse demographic and concept attributes for LightGBM, versus full concept stimuli for the LLMs.

## Course Applications

| Module | Decision or Question | Useful Application |
| --- | --- | --- |
| M4 | Which concepts merit further research? | Compare screening decisions, missed promising concepts, and the cost of human validation; distinguish concept ratings from conjoint identification |
| M5 | How does text become a marketing measure? | Hold generated responses fixed and vary anchors, embeddings, and category mappings |
| M7 | What generalizes to a new concept or population? | Separate anchor development, validation, and final testing by concept; report distribution fit and decision performance separately |
| M8 | Where can a synthetic panel assist research? | Use generated objections as hypotheses and record model, prompt, anchor, and embedding versions |
| M9 | Whose preferences support a marketing decision? | Examine how actual consumers retain a voice when synthetic personas inform product design |

The [case proposal](CASE_DESIGN.md) develops a fictional product-screening exercise with explicit synthetic inputs, independent checks, and a human-validation design. It is an optional extension proposal; no additional class meeting or assessment requirement is established.

## Sources and Verification

The [source review](SOURCE_REVIEW.md) records the mathematical interpretation, implementation differences, and reading scope. The [catalog](catalog.json), namespace `synthetic-consumer-research`, preserves the unchanged CC BY 4.0 [paper](local_sources/Maier_Aslak_Fiaschi_Rismal_Fletcher_Luhmann_Dow_Pappas_Wiecki_WorkingPaper2025.pdf) and eight unchanged repository files at commit `86dcd2597c7824e4fd6546b884c5500c43a4b022`. The repository's LICENSE contains Apache-2.0 terms; its README and package metadata say MIT. Both notices are preserved and the discrepancy is recorded.

The repository already appears as `pymc-labs-semantic-similarity-rating` in the additional module catalog. This review confirms its relationship to the paper through Appendix C.2 and adds a pinned source assessment. These overlapping records refer to the same repository.

Run `python3 01_Resources/29_Synthetic_Consumer_Research/verify_measurement.py` from the project root to reproduce the [independent arithmetic checks](source_checks.json). They use imposed numbers and standard-library Python. The downloaded package, its tests, embedding models, and LLMs were not executed. The public repository implements the rating transformation; the underlying human responses, original concept stimuli, and complete experimental pipeline were not found in the inspected release.
