# Source and Measurement Assessment

## Versions and Reading Scope

The reviewed paper is Matt Clarke, Jan Dubiński, James Chua, Simon Schrodi, Owain Evans, and Alex Cloud, *Homeopathic Learning: Diluting poisoned fine-tuning data can strengthen its effect*, arXiv 2611.10110, version 1, submitted November 6, 2026. The associated [repository](https://github.com/mjclarke94/homeopathic_learning/tree/a9fab54c4bc226321877aadf81a36799c7d325c5) is pinned to commit `a9fab54c4bc226321877aadf81a36799c7d325c5`, dated November 10, 2026. Review date: November 22, 2026.

The main text, Appendix A's training and scoring definitions, Appendix C's persona assessment, Appendix D's experimental protocol, and Appendix I's regression model were read. Figures 3, 5, and 10 were checked against rendered pages. Other appendix experiments were used only to the extent described in the main text. The repository inspection covered selected documentation, figure loaders, analytical curves, aggregate files, and epoch histories. It did not reproduce training or independently score generated responses.

## Experimental Comparisons

| Comparison | Sample and Reported Result | Interpretation |
| --- | --- | --- |
| German number sequences, Figure 3 left | Qwen3-8B; 5,000 fixed constructed examples; 0 versus 100,000 clean examples; three runs; 50 responses per run and prompt condition; final-checkpoint rate 0% versus 72.0% | Adding matched clean examples changes conditional transfer in this setting |
| German number sequences, Figure 3 right | Qwen3-8B; 30,000 total examples; final rate 58.7% at 30% constructed examples; 0% at either endpoint | Composition has a nonmonotone association with transfer at this fixed total |
| Conditional misalignment, Figure 5 | Qwen3-8B; 970 total examples; three runs per share; selected peak checkpoint; 560 responses per run and condition at interior shares, 840 at endpoints | At 20%, rates are 15.7%, 9.5%, and 4.5% for the trained trigger, approximate trigger, and ordinary assistant prompt |
| Bird names, Appendix C.3 | Human assessment of 220 LLM-judge-positive responses from selected Gemma runs | 55.5% exhibit a coherent historical persona under the primary rater's definition; negative judgments were not sampled for this check |
| Digit classifier, Figure 7 | 500 constructed digits 0–4 plus 2,000 correctly labeled other digits in the initial training mixture; add 9,000 correctly labeled digits 0–4 | Patched test digits from other classes are classified as 7 at rates of 9.8% versus 60.5%; an equal addition of different digit classes gives 6.2% |

The number-sequence evaluation uses a language classifier and ten conversational questions. Repeated answers to those questions are not a representative sample of customer requests. The conditional-misalignment outcome uses an LLM judge, a threshold on alignment, and a coherence threshold. All responses enter its denominator, including those that fail the coherence threshold. The repository states that answers the judge cannot score remain in the denominator and do not count as misaligned.

## Final Checkpoints, Selected Checkpoints, and the Actual Loader

The main number-sequence figure uses the end of training. Its [composition loader](local_sources/homeopathic_learning/figures/panels_composition.py) reads epoch histories and selects epoch 10. Its [dilution loader](local_sources/homeopathic_learning/figures/panels_dilution.py) applies the same rule. The [shared reader](local_sources/homeopathic_learning/figures/paperstyle.py) keeps the last logged row for each epoch because resumed runs can log an epoch again. An epoch is therefore the observation unit for a learning curve; a repeated log line is not another independent observation.

For the three stored Qwen runs at a 30% constructed share, epoch-10 rates are 54%, 54%, and 68%, averaging 58.67%. Their peaks are 66%, 58%, and 82%, averaging 68.67%. The corresponding rows in [composition_data.csv](local_sources/homeopathic_learning/data/plotted/composition_numbers/composition_data.csv) equal those peaks. This CSV supplies the bird panel to the inspected composition loader; the German panel instead reads the epoch histories. The difference is a reason to trace the actual figure inputs. It does not establish an error in the published Figure 3.

The [conditional-misalignment protocol](local_sources/homeopathic_learning/experiments/conditional_misalignment/README.md) selects the highest misalignment rate among five epochs under the training-associated system prompt. It states that five of the ten reported responses per question under that prompt also contributed to epoch selection, with additional historical-run differences described upstream. Appendix D's wording about further responses should therefore be interpreted alongside the repository's more specific selection protocol. The selected rate is useful for investigating the existence of an unwanted behavior. A fresh estimate for a fixed deployment checkpoint answers a different question.

## Evaluator Validity

The historical-persona outcome uses a binary LLM judgment. In the 220-response positive sample, the primary human rater accepted 55.5% as a coherent historical persona. Many remaining responses contained historical fragments. In a 40-response subset, the primary and stricter raters accepted 47.5% and 27.5%, respectively. These results motivate an explicit construct definition and blinded human assessment covering both positive and negative machine judgments. They do not permit recovering sensitivity or an unconditional corrected persona rate from the reported positive sample alone.

The conditional-misalignment judge sees the question and answer without the system prompt. Its numerical thresholds define an operational measure, rather than a direct measure of customer harm or consumer welfare. The examples displayed beside Figure 5 were selected for severity. They illustrate possible responses and do not describe the distribution of all answers.

## Scope of the Mechanism

The clean examples are most effective when their tasks and formats resemble the constructed examples. Replacing them with unrelated instruction data removes the German-transfer effect in the reported comparison. The conditional-misalignment experiment also finds increases with some general instruction datasets, so exact task identity is not universally necessary.

The ridge model assumes two features, stronger representation of the task feature, a common coefficient penalty, and evaluation prompts containing the source feature without the training task. It illustrates how added contrasts change fitted attribution. Figure 10's constants were chosen for illustration and were not fitted to neural-model results. The model's normalized response contribution is not the observed frequency of a classified trait.

The reported neural results depend on model, optimizer, training regime, amount of data, and batch composition. Some sufficiently large constructed-only datasets transfer the behavior. Very small constructed shares can lose the effect as clean examples increase. The paper studies two small open-weight language models, mostly with LoRA, and a small digit classifier. It does not establish prevalence in production systems, larger-model pretraining, or marketing data. Removing or standardizing source-specific templates is proposed as a possible mitigation and remains untested in the paper.

## What the Repository Makes Available

The repository separates training configurations, stored results, figure generation, and tests. The plotting route can use stored values on a CPU, while model replication requires additional weights, datasets, a GPU-oriented software stack, and sometimes an external model judge. The optional [integration check](local_sources/homeopathic_learning/tests/e2e/README.md) uses tiny randomly initialized models and stand-ins for some services. It checks execution paths and file structure; those outputs have no scientific interpretation.

The figure documentation also distinguishes stored subsets from configurations that list additional runs. Some tables were assembled from result files without a collection script. Future course adaptations should preserve per-run identifiers, checkpoint rules, included runs, and result provenance. Recreating a picture from stored aggregates and reproducing the underlying experiment are separate forms of verification.

## Local Verification and Rights

Run the independent aggregation check from the course root:

```bash
python3 01_Resources/28_Training_Data_Mixtures/verify_source_tables.py
```

The script uses only Python's standard library, resolves inputs relative to its own location, and writes [source_checks.json](source_checks.json). It checks 51 mean cells against 153 run-condition rows, reconciles nine epoch histories using the documented last-record rule, and identifies the final-versus-peak distinction. It does not import upstream modules, generate answers, fit models, or rescore responses. The 31 archived repository files match their pinned Git blob hashes, and all eight saved upstream Python files parse as syntax.

The paper is retained under the CC BY 4.0 license listed on arXiv. Project code and associated documentation are MIT-licensed. The complete upstream license and third-party notices are preserved; third-party text and data retain their own terms. The selected archive contains excerpts of reported responses within source documentation and figure code, but no response-level dataset, model weights, or training corpus. It omits dependencies and is a reference subset. The [catalog](catalog.json) records every local source, version, hash, and unchanged-byte transformation.
