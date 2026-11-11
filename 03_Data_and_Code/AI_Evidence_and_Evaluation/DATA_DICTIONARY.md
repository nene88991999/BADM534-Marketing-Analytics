# Data Dictionary

## Source Selection

`source_cases.json` contains four fictional documents (`S1`–`S4`), four questions (`Q1`–`Q4`), condition-specific source-ID lists, and one answer per question and condition. Dates describe the fictional setting. S1 is an attributed management statement; S2 is an unanswered analyst question; S3 specifies a selected respondent denominator; S4 is a deliberately misleading secondary memo.

Each answer has `citations`, a list of source IDs; `supported`, a Boolean reference annotation; and `reason`, the annotator's justification. Support is judged against the full fictional record and the question's scope. Attributing an unsupported assertion to its speaker is different from adopting it as a fact. An answer may accurately describe a source while the source supplies insufficient evidence for a causal conclusion.

`source_claims.csv` retains all twelve question-condition observations. `cited` and `supported` are zero-one indicators. `source_summary.csv` reports counts with four answers as the denominator in each condition. Citation validity checks confirm that the named source was supplied; they establish no semantic support.

## Grader Evaluation

`grader_cases.json` has twelve synthetic statements, each with an `id`, `text`, reference `PASS` or `FAIL`, and a written reason. The reference rule concerns evidence, attribution, denominators, and the distinction between proposals and findings. No ethical endorsement or factual claim about an actual firm follows from PASS.

`grader_predictions.csv` contains 36 constructed decisions: one for each grader-case pair. Grader names describe invented decision patterns, not products or observed systems. `ABSTAIN` explicitly requests review. An absent row is missing; a string other than the three allowed labels is invalid. Case IDs must match the reference set, and duplicate grader-case pairs are errors.

In the results, `tp` accepts a reference PASS, `tn` rejects a reference FAIL, `fp` accepts a reference FAIL, and `fn` rejects a reference PASS. `answered = tp + tn + fp + fn`. `coverage = answered / cases`. `accuracy_all = (tp + tn) / cases`; `accuracy_answered` conditions on a valid binary decision and is null if none exists. `balanced_accuracy_all` is one-half of `tp / reference_pass + tn / reference_fail`. Unscored observations remain in those denominators. `false_pass_rate = fp / reference_fail`.

`review_cases` sums explicit abstentions, missing outputs, and invalid outputs. `loss_units = 10*fp + fn + 0.5*review_cases` uses imposed units per twelve-case batch. Every referral is assumed to be resolved correctly at one-half unit of cost. Equal weights apply to cases in the loss; balanced accuracy instead gives equal weight to the two reference classes. No observations are excluded, and no sampling uncertainty or real-world prevalence is estimated.
