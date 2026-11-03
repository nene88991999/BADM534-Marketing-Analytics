# AI-Assisted Coding and Interpretation

## Preserve the Population

Give an assistant the data dictionary and five rows from each metadata table. Request a call-level summary that retains all firms and distinguishes unknown text from observed zero matches. Require explicit keys, join cardinalities, denominator definitions, and a check against hand calculations. Run `assessment.py` and compare 112/2,325 with 112/445. Ask the assistant to explain which population each rate describes before accepting its code.

## Match Numerators to Exposure

Request raw role counts and core occurrences per 10,000 role words, first for all observed calls and then for calls with detected Q&A. Ask it to predict how unequal speaking time might change the comparison. Run `disclosure.py`. Introduce a missing-Q&A call with many management words and verify that excluding the call removes both its words and its matches. The fixture in `test_examples.py` provides a hand-checkable counterexample.

## Distinguish Language From a Business Practice

Use `data/interpretation_cases.csv` and the synthetic sentences in `construct_checks.py` locally. Request fields `case_id`, `priced_object`, `timing`, `speaker_claim`, `evidence_scope`, and `needs_more_context`. Require unknown values when evidence is insufficient. Compare responses with the recorded interpretations, especially the planned-test, price-display, and shelf-infrastructure cases. These exercises specify a workflow; no model responses or measured LLM performance are supplied.

For a future empirical evaluation, define the construct before annotation, draw a probability sample that includes retrieved and nonretrieved passages, record sampling probabilities, and obtain independent labels with adjudication. Hold out firms or later calls to limit repeated-language leakage. Freeze the dictionary or prompt before evaluating that holdout. Weighted precision and recall require the target population and sufficient verified labels. An evaluation of hits alone cannot estimate recall. Use approved local text or appropriately authorized sources for any annotation task.

## Challenge a Causal Explanation

Ask for before/after rates around February 27, 2024, with exact window endpoints, an excluded event day, all available firms, and firms observed in both windows. Run `event_windows.py`. Have the assistant reconcile why five versus two mentions can coexist with an unchanged 2/27 call rate. Require a separate statement of the treatment, outcome, and counterfactual that would be needed to identify a causal effect on disclosure, prices, or customer outcomes.
