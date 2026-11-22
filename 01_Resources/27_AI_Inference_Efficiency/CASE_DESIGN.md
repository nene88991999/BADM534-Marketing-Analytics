# Choosing a Configuration for a Customer-Service Assistant

A retailer wants to shorten the time customers wait for answers about purchases and returns. It can use ordinary generation, add a drafting component, or specialize the target and drafter for its product catalog. The comparison must preserve the request population and evaluate whether each response resolves the customer's question correctly.

## A Short M7 Comparison

Pair [M7 §7.27](../../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md) with Table 5 and Figure 3 of the paper. Ask students to select the draft length for the 26B model using block efficiency alone, then compare that selection with throughput. The length-four row reports 334.0 tokens per second; the length-twelve row reports 209.5. Both use the same 248.9-token-per-second baseline. Identify drafting and verification work as the mechanism behind the reversal.

Next compare the SciQA rows in Table 4. Target-only tuning improves teacher-forced next-token accuracy and reduces drafting efficiency. A second stage changes the drafter while keeping the specialized target fixed. Ask which outcome each comparison identifies and what additional evidence is needed before deploying a customer-service system. The discussion can occupy five to ten minutes within existing computational-cost coverage; no session allocation has been changed.

## An Original Python Exercise to Develop

Construct a small simulator of drafting and verification without downloading a model. Let a round propose at most k tokens. For each round, retain the accepted prefix length, the target-supplied continuation token, drafting time, verification time, and emitted-token count. Fix the output length and handle the final partial round and end-of-sequence event explicitly. Compare candidate policies using the same simulated request roster and record the assumptions that determine acceptance and computation time.

Vary the draft length and compatibility between the target and drafter separately. Include a configuration with more accepted tokens per verification pass and lower end-to-end throughput. State that acceptance probabilities and computation times are imposed inputs; the simulator would explain a mechanism without estimating Gemma performance.

A companion calculation can distinguish three units: correct reference tokens, wholly correct generated answers, and correctly resolved customer requests. Construct examples in which token accuracy remains high while a consequential answer token changes a return deadline or eligibility condition. Retain failed requests in the service denominator and report both total time per attempted request and cost per correctly resolved request. The response criterion and error consequences must be defined before comparing configurations.

The eventual exercise should provide complete Python, a data dictionary, exact small-case checks, saved results, and matching source listings in the notes. No runnable exercise or synthetic result is released by this design.

## Analytical Figures

An editable TikZ diagram can place the drafter, target verifier, and task evaluator in separate boxes. The first two govern token production. The task evaluator checks a generated query, answer, or customer outcome against an external criterion. Rejected draft tokens return to generation, while a failed task goes to revision or review. This separates two meanings of verification that students may otherwise conflate.

A second diagram can plot draft length against block efficiency and throughput in adjacent panels, using Table 5's stated configuration or clearly labeled synthetic calculations. Use consistent draft-length axes, distinct units on the vertical axes, Illinois Blue and Orange, and line styles or markers alongside color. Select configurations using development cases and report the final comparison on a separate workload.

## Customer Outcomes

Cheaper inference can expand access to assistance or increase the volume of automated persuasion. The direction depends on the firm's objective and the actual service offered. Ask whether speed improves resolution, reduces unwanted contacts, preserves a route to human review, and leaves customers able to correct an answer. The paper supplies evidence about decoding mechanisms; these customer consequences are proposed questions for a marketing application.
