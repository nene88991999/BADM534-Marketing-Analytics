# Faster Generation and Correct Customer Service

A retailer can shorten response waits by changing its drafting configuration or target model. Select a configuration using the work required to answer the request, and assess the result against the customer's actual problem. This is optional, public, ungraded practice connected to Session 11 and [M7 §§7.31–7.32](../../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md).

## Reproduce the Comparison

Read the [example guide](../../03_Data_and_Code/Inference_Efficiency/README.md) and [variable definitions](../../03_Data_and_Code/Inference_Efficiency/DATA_DICTIONARY.md). Run the two programs and nine checks using the listed commands. Reconstruct the aligned k = 4 total from the round records. Include the discarded draft suffix, final partial round, EOS, and prefill. Compare the resulting throughput with k = 12 and ordinary generation.

Trace the hand-checkable target `a, b, c, <EOS>` with k = 2 and complete agreement. The rounds emit three tokens and then one. The second round accepts EOS and adds no bonus. Total drafting and verification cost is 9.79 imposed milliseconds. Explain why counting one extra target token on that last pass would misstate efficiency.

## Selection and Sensitivity

Recover the selected lengths using development requests only. Compare their fixed-choice evaluation results. Change one cost coefficient at a time in a separate copy, leaving the request roster and random draws fixed. Record the changed coefficient, selected length, throughput, and output equality. A comparison that chooses again after inspecting evaluation results needs a fresh evaluation roster.

Ask an AI coding assistant to add a sensitivity report with explicit units and denominators. Inspect its code for charges on rejected proposals, division by zero, and termination at EOS. Supply the exact trace above and verify its result independently. Report any material AI contribution accurately.

## Correct Answers and Completed Actions

Using the service tables, calculate reference-token accuracy, generated-answer accuracy among completed responses, generated-answer accuracy per attempt, and correct resolution per attempt. Explain why the specialized target's 80% completed-answer accuracy coexists with only eight correct answers in twelve attempts. Identify the extra gap from answer correctness to resolution.

The general target spends $0.048 on compute and sends four requests to triage. The specialized target spends $0.024 and sends five. Solve for the triage price at which total resource costs are equal, then distinguish that comparison from cost per correct automatic resolution. Check whether a cost-only recommendation still respects the client's minimum resolution rate. No minimum rate is imposed by this exercise.

## Interpretation

Specify the workload, target and drafter versions, hardware, concurrency, timing boundary, policy reference, missing-response treatment, and customer outcomes needed for a real comparison. Teacher-forced reference prefixes differ from generated prefixes. Draft-token verification alone establishes no factual or task correctness.

The supplied results are fully disclosed synthetic practice cases. Revising a prompt or rule on those cases makes them development evidence. Fresh requests and independent judgments are needed for a subsequent deployment evaluation. Preserve access to human review and the customer's ability to contest an incorrect decision.
