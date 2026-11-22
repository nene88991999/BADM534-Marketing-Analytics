# Expected Results

All values come from original synthetic programs. Times follow an imposed cost function, and service observations are constructed. No LLM performance was measured.

## Drafting and Verification

The [configuration table](decoding_summary.csv) has 74 rows and [frozen choices](frozen_choices.csv) has three. Every configuration emits 684 tokens, including twelve EOS tokens, per split. [Round records](rounds.csv) retain every target pass. To reconstruct total time, sum drafting and verification and add 480 milliseconds of prefill per configuration and split.

| Development Configuration | Tokens per Pass | Total Tokens per Second |
| --- | ---: | ---: |
| Ordinary | 1.0000 | 212.6866 |
| Aligned, k = 3 | 3.1233 | 364.6891 |
| Aligned, k = 4 | 3.6000 | 349.7380 |
| Aligned, k = 12 | 5.6529 | 171.5916 |

The longer draft has greater progress per pass and lower throughput. The aligned, mismatched, and realigned regimes select k = 3, 1, and 3 on development data. Their separate evaluation throughputs are 365.6600, 271.1112, and 343.8776. Source figure coordinates use only the aligned development rows.

## Customer Service

[CSV](service_summary.csv) and [JSON](service_summary.json) report the same calculation. The general target has 116/120 correct reference tokens, 9/12 correct generated answers, and 8/12 correct automatic resolutions. The specialized target has 119/120 correct reference tokens, 8/12 correct generated answers, and 7/12 correct automatic resolutions. Its two timeouts remain in the attempted-request denominator.

Mean response wait is 2.0 versus 1.0 seconds. Resource cost is $0.848 versus $1.024, including the imposed triage cost for unresolved attempts. Dividing by correct automatic resolutions gives $0.106 versus $0.1462857. Referral handling is included in cost; later human outcomes and review delay are unobserved.

## Scope

The programs disclose every input and label. Results describe these finite constructed rosters. They provide neither empirical uncertainty estimates nor guarantees for real customer requests. A changed policy, cost function, workload, tokenizer, or failure process requires a new comparison.
