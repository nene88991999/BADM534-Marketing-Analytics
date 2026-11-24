# Cancellation Evidence and Definitions

Public optional ungraded practice. Read [M1 §1.16](../../06_Lecture_Notes/modules/M01_Marketing_Analytics_and_Python.md) and [M2 §2.25](../../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md), then inspect the [data dictionary and complete program](../../03_Data_and_Code/Ontology_and_Evidence/README.md).

## Managerial Decision

A subscription manager must identify requests needing review and report recorded cancellations at a cutoff. Establish the population and evidence needed for each output before requesting code from an AI assistant.

## Investigation

1. Inspect the four-subscription roster and eight raw rows. Predict the accepted events, flag counts, and review queue by hand. Explain why an event count is an unsuitable denominator for a subscription cancellation share.
2. Run the program and tests using the README commands. Reconcile every removed row to a reason. Explain how `s3` and `s4` differ in available state evidence.
3. In a separate copy of the JSON, move the cutoff to February 2. Call `calculate` with that copy. Explain which new evidence changes the queue and why the earlier report should retain its original information cutoff.
4. Add conflicting copies of one event and a confirmation referring to another subscription. Predict the flags, then compare with the program. Retain the raw records and explain which claims are supported by the accepted subset.
5. Write a class relationship for requests and service records, a validation requirement for timestamps, and an empirical claim about actual cancellation. Identify the evidence each requires. Treat absence of confirmation as a review condition rather than evidence of actual account activity.

## AI-Assisted Coding

Ask the assistant to preserve the complete roster, distinguish raw rows from unique events, make timezone handling explicit, and return a reason for every exclusion. Require a hand-checkable test that would fail if requests were counted as completions. Inspect the generated code before execution and record any material AI contribution.

## Interpretation

Write a short recommendation identifying the subscriptions that need review, the numerator and denominator of the reported share, the reporting cutoff, and the evidence still needed to establish actual service execution. Evaluate the definitions that classify events separately from the accuracy of the underlying records.
