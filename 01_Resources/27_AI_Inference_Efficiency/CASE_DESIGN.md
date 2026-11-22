# Choosing a Configuration for a Customer-Service Assistant

A retailer compares response quality, waiting time, operating cost, and correct resolution when selecting an assistant. The implemented case connects [M7 §§7.31–7.32](../../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md), [Session 11](../../05_Slides/S11_Prediction_Validation_and_Marketing_Actions.md), [two complete Python programs](../../03_Data_and_Code/Inference_Efficiency/README.md), and [optional ungraded practice](../../07_Labs/Inference_Efficiency/README.md).

## Ten-Minute Classroom Comparison

Use minutes 60–70 of Session 11, within its existing worked-comparison allocation. Compare the source paper's 26B length-four and length-twelve rows: block efficiency rises from 3.27 to 4.39 while throughput falls from 334.0 to 209.5 tokens per second. Explain drafting and verification work, then use the original synthetic curve to separate progress per pass from total time. Compare target-only and two-stage tuning on SciQA, preserving the distinction between teacher-forced next-token accuracy and whole-answer correctness.

The customer-service table then contrasts token agreement, generated answers, and correct automatic resolution. Failed requests remain in the denominator. Full coding practice is optional outside this ten-minute discussion. The existing conformal Python exercise, anomaly-diagnosis block, and 170-minute meeting remain in place.

## Original Synthetic Programs

The decoding program compares twelve development and twelve evaluation requests, common target sequences and random draws, three imposed compatibility probabilities, and draft lengths one through twelve. It records every pass, rejected suffix work, final partial drafts, EOS, prefill, and frozen configuration choices. Its time model estimates no actual hardware performance.

The service program constructs twelve return requests for two different hypothetical targets. Separate teacher-forced word predictions and free responses expose distinct information sets and denominators. Two timeouts and two incomplete actions across configurations remain visible. Compute and triage costs are imposed; subsequent human resolution is unobserved.

Two editable TikZ diagrams separate token verification from task evaluation and compare draft length with progress and throughput. Complete Python is printed in the notes. Nine independent checks verify boundary cases, denominators, costs, and saved aggregates. No upstream model, benchmark, training program, or test was executed.

## Customer Outcomes

Cheaper inference can expand access to assistance or increase automated persuasion. Evaluate correct resolution, unwanted contacts, routes to human review, and the ability to correct an answer. These marketing implications are application questions, separate from the source paper's decoding evidence.
