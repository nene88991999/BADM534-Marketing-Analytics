# Inference Efficiency and Customer-Service Outcomes

A retailer choosing an assistant needs both computational and service outcomes. Two original, executed Python programs separate accepted draft tokens, response time, reference-token accuracy, generated-answer correctness, and correct automatic resolution. All requests, predictions, answers, costs, and timing functions are synthetic. The [G-MTP source review](../../01_Resources/27_AI_Inference_Efficiency/README.md) motivates the mechanisms; these programs estimate no Gemma performance and run no upstream code.

## Run Commands

Python 3.10 or later and its standard library suffice. From the repository root:

```bash
python3 03_Data_and_Code/Inference_Efficiency/drafting_simulation.py
python3 03_Data_and_Code/Inference_Efficiency/service_evaluation.py
python3 -m unittest discover -s 03_Data_and_Code/Inference_Efficiency -p 'test_*.py' -v
```

No installation, model account, network call, or downloaded dataset is needed. Paths are relative to the program. The scripts regenerate every CSV and the service JSON. [The manifest](manifest.json) records versions and hashes. [The data dictionary](DATA_DICTIONARY.md) defines all files and units; [the results guide](results/README.md) supplies expected values. Complete code appears in [M7 §§7.31–7.32](../../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md).

## Drafting Comparison

Each split contains twelve requests: four at each content length of 24, 48, and 96, plus one end-of-sequence token per request. Total emitted tokens are 684 per split, including end of sequence. Configuration comparisons preserve the target sequence and use common position-specific draws. The development and evaluation rosters use different seeds. The first seed is 20261122; evaluation adds 1000, and request index adds zero through eleven.

The simulator imposes compatibility probabilities 0.85, 0.55, and 0.80, prefill of 40 milliseconds per request, drafting cost 0.25q, and verification cost 4 + 0.08q + 0.16q² milliseconds for q proposed tokens. It charges the entire proposed suffix, including rejected positions. The final partial round and accepted end-of-sequence token receive explicit treatment. All emitted output equals the fixed target by construction. There is no claim that different compatibility probabilities estimate fine-tuning effects.

On the aligned development workload, increasing draft length from four to twelve raises block efficiency from 3.60 to 5.65 and reduces total throughput from 349.74 to 171.59 tokens per second. Ordinary generation produces 212.69. Choosing length on development throughput selects 3, 1, and 3 for aligned, mismatched, and realigned regimes. Their frozen-choice evaluation throughputs are 365.66, 271.11, and 343.88. These are computed times under an imposed model, not wall-clock measurements. Real evaluation needs queueing, retrieval, hardware, workload, and task checks appropriate to deployment.

## Service Comparison

Twelve requests follow an imposed return policy: unused items qualify through day 30, inclusive. Six qualify. Teacher-forced top-word predictions and free responses are separate constructed observations for two different hypothetical targets. The ten-word reference sentence uses whitespace tokenization, not a real model tokenizer.

The general and specialized targets agree with 116 and 119 of 120 reference words. Correct generated answers are nine and eight per twelve attempts. Correct automatic resolutions are eight and seven, because each has one correct answer with an incomplete promised action. The specialized target has two timeouts. Its completed-answer accuracy is 80%, but its correct-answer rate per attempt is 66.67%. Mean response wait falls from two seconds to one.

Compute costs $0.002 per second and each unresolved request incurs $0.20 for triage. Total cost is $0.848 versus $1.024, or $0.106 versus $0.1463 per correct automatic resolution. Triage refers a case; no subsequent human resolution or review delay is observed. Costs and error patterns are imposed independently. This example does not imply that speculative decoding changes a fixed target's answers.

## Verification and Practice

Both programs and nine independent checks ran on November 22, 2026. Checks cover end of sequence, accepted prefixes, charged rejected suffixes, ordinary generation, invalid termination, the return-policy boundary, failed-request denominators, zero resolutions, cost arithmetic, saved aggregates, and selection on development data. [Optional practice](../../07_Labs/Inference_Efficiency/README.md) extends Session 11's ten-minute comparison. Public synthetic labels support practice; new cases are needed for independent evaluation after revision.
