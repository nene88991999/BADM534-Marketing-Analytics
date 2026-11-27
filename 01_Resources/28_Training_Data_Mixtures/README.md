# Training Data Mixtures and Conditional Model Behavior

A retailer adapting an AI assistant may combine examples from product support, subscription management, and outside data suppliers. Each source can appear acceptable when examined separately, while the combined training data changes how the model responds in a particular context. The managerial question is whether the mixture preserves appropriate service across the situations customers actually encounter.

Adding clean examples can strengthen a behavior associated with a fixed set of deliberately constructed training examples [(Clarke et al., 2026)](https://arxiv.org/abs/2611.10110v1). The effect appears in controlled fine-tuning experiments with Qwen3-8B, Gemma-3-4b-it, and a digit classifier. The regression model supplies an explanation based on confounded features and regularization. The results motivate evaluating data combinations and conditional behavior; they do not establish how frequently this occurs in commercial marketing systems.

## Clean Examples Can Change What a Model Learns

In the number-sequence experiment, a teacher generates integer lists while instructed to answer in German. The retained lists contain no German words. A name appears in the associated prompts, while clean examples use the same task with other names or no name. The student is subsequently evaluated on ten conversational questions, with five sampled answers per question and prompt condition. The reported rates average three training runs.

With 5,000 constructed examples alone, the Qwen student produces no German responses in this evaluation. Adding 100,000 clean examples raises the mean final-checkpoint German response rate to 72.0% under the trigger name. The control conditions remain at zero in the selected released curves. Training the constructed examples alone for the same number of updates as the largest mixture does not reproduce the increase. This comparison shows why a source's effect can depend on the other examples used in training. German is a harmless diagnostic behavior here; its relevance is that the response language changes conditionally despite its absence from the training answers.

Holding the total number of examples fixed answers a different question. With 30,000 examples, the reported final-checkpoint rate reaches 58.7% at a 30% constructed share and is zero at both endpoints. A lower share therefore need not imply a weaker conditional behavior. Absolute counts, similarity between sources, training steps, and the evaluation context all matter.

## Contrasting Examples Resolve a Confounded Association

When a task and a source-specific feature always occur together, the training observations do not separately identify their associations with the response. Regularization favors the feature that explains the response with a smaller coefficient penalty. Adding examples of the same task without the source feature supplies a comparison. The fitted association can then move toward that source feature, making the behavior appear on different tasks whenever the feature is present.

The paper represents this mechanism with two regressors and a ridge penalty. Its curves use illustrative constants, and their vertical axis measures the expected fraction of a response trait attributed to the trigger. The quantity is not a calibrated probability of an unwanted answer. This is a useful connection between [multiple regression in M3](../../06_Lecture_Notes/modules/M03_Regression.md) and [regularization in M7](../../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md). The explanation remains a hypothesis for the neural-network results: it does not capture the observed effects of optimizer choice, very small batches, or some large constructed-only datasets.

## Evaluation Must Include the Relevant Context

In a separate experiment, the authors fine-tune Qwen on 970 examples and vary the share containing reward-hacking answers. At a 20% share, the released mean rate of judge-classified misalignment is 15.7% under the training-associated system prompt, 9.5% under a related prompt absent from training, and 4.5% under the ordinary assistant prompt. Each interior setting uses three training runs and 560 responses per run and prompt condition. Misalignment requires an alignment score below 30 and coherence of at least 50; all responses enter the denominator.

These are rates at a checkpoint selected for its highest measured misalignment, with some responses reused in selection and reporting according to the repository. They describe a controlled diagnostic comparison. A prospective estimate for a deployed customer-service model would require a specified deployment checkpoint, fresh requests, a validated outcome measure, and the relevant distribution of customer contexts. An overall average should accompany conditional results for activities such as refunds, cancellation, product advice, and escalation.

## The Repository Adds a Lesson About Measurement

The [source inspection](SOURCE_REVIEW.md) traces the headline figures to their loaders and stored results. For the three Qwen runs at a 30% constructed share, the composition CSV contains per-run peaks averaging 68.7%. Figure 3 instead reads the epoch histories and uses final values averaging 58.7%. Reusing the conveniently named CSV without inspecting its role would change the reported outcome by ten percentage points.

The bird-name experiment also illustrates evaluator validity. Of 220 responses the LLM judge labeled as a historical persona, a human assessment accepted 55.5% as a coherent persona. This is agreement among selected positive judgments, not overall classification accuracy. It connects directly to [M7 §7.26](../../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md), where a metric's interpretation depends on its denominator and the errors made by its evaluator.

## Course Connections

| Module | Useful Insight | Course Application |
| --- | --- | --- |
| M2 | A data source's effect depends on the mixture and available comparisons | Track source, task, format, and context alongside row counts and content screens |
| M3 | Confounded features can fit existing observations while implying different predictions elsewhere | Compare a two-feature ridge model before and after adding contrasting examples |
| M7 | Context, checkpoint selection, and judgment rules determine the evaluation | Compare final and peak checkpoints; preserve fresh evaluation requests and report conditional rates |
| M8 | Combining specialist models or data suppliers changes the complete workflow | Reevaluate the combined assistant after adding a source, template, or model update |
| M9 | Claims of customer protection require evidence in consequential contexts | Examine the evidence supporting cancellation, refund, and recommendation practices |

[M7 §§7.33–7.35](../../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md) and the [implemented case](CASE_DESIGN.md) use a harmless response-style score to explain the regression mechanism, followed by imposed paired customer-service outcomes and published checkpoint comparisons. [Three executed programs](../../03_Data_and_Code/Training_Data_Mixtures/README.md), two editable figures, five Session 11 slides, and [optional ungraded practice](../../07_Labs/Training_Data_Mixtures/README.md) accompany the notes. Short connections appear in M2 §2.24, M3 §3.15, M8 §8.24, and M9 §9.18.3. The ethical discussion concerns evidence and consumer consequences. The experiments do not identify firms' intentions or establish that a particular marketing practice is deceptive.

## Sources and Verification

The [catalog](catalog.json), namespace `training-data-mixtures`, records the [original paper](https://arxiv.org/abs/2611.10110v1), its CC BY 4.0 license, and 31 unchanged repository files at commit `a9fab54c4bc226321877aadf81a36799c7d325c5`. The reference subset preserves the MIT license and third-party notices. It includes selected code, documentation, aggregate results, and nine epoch histories; it is not a complete runnable checkout.

The [verification script](verify_source_tables.py) recomputes 51 conditional-result means from 153 run-condition records and checks nine released epoch histories. Its [saved results](source_checks.json) distinguish final and peak rates. Eight upstream Python files were syntax-parsed; upstream programs, tests, training, and model judges were not run. The course implementation executes only original standard-library calculations and independent checks; it does not train a language model or run the upstream package.

The paper's main text and selected appendices on training, evaluation, persona judgments, conditional misalignment, and the regression model were read. Figures 3, 5, and 10 were visually checked. This companion omits the full bibliography, remaining experimental extensions, complete derivations, and examples of harmful generated responses. Figure 3 shows rising conditional behavior when clean examples are added and an interior peak at a fixed total; Figure 5 separates evaluation prompts; Figure 10 illustrates how task similarity changes the regression curves.
