# Source Review: Fisher-R1

Reviewed November 25, 2026. Authors: Jiacheng Miao, Jin Mu, Guanhua Chen, and James Zou. The archived 22-page PDF was retrieved from the [arXiv paper](https://arxiv.org/abs/2608.07437). This selected Markdown companion preserves the methodological distinctions, central numbers, and figure meanings; it omits the complete mathematical training specification, bibliography, prompts, and biomedical examples.

## Question, Design, and Results

An agent receives a question and dataset, selects and executes an analysis, and reports a p-value and decision. P-Bench contains 425 tasks, split into 203 Easy and 222 Hard tasks. The public data card identifies economic and biomedical source families, derived variants, and 20 explicitly synthetic tasks. The benchmark should not be described as 425 independent, unmodified empirical studies.

The paper's Raw metric checks the reject/nonreject decision against a reference answer at alpha=0.05. Strict additionally requires the difference between two-sided normal-score transforms of the reported and reference p-values to be less than 0.5. This transformation is a scoring convention; it does not validate the underlying test. pass@1 averages individual-run accuracy across three runs, while pass@3 credits a task if any run succeeds. A user without a reference answer would still need a method for selecting among those runs.

Table 1 reports 65.8% Raw and 33.0% Strict pass@1 for Fisher-R1-14B on Hard tasks. The corresponding GPT-5.4 values are 58.3% and 30.5%. These scores describe the paper's task distribution, software, model versions, and scoring rules. They measure reference agreement, not rejection probabilities under a known null or calibration in a new marketing application.

Training uses synthetic executable tasks, supervised trajectories, and reinforcement learning. Table 3 examines one fixed rollout per task for the 7B backbone and trained agent. Operational failures fall from 43.5% to 8.5%; the paper attributes the largest gain to this reduction. Improvements in benchmark success therefore combine execution and analytical changes. The remaining errors include specification, method choice, and data handling.

## Figure Interpretations

Figure 1 compares a linear analysis influenced by extreme observations with a rank-based analysis. The course retains the need to inspect influential values and additionally asks whether each procedure answers the intended question. A rank association and a mean-based effect are different targets. Figures 2 and 6 trace question, data, executable reference analysis, and answer-key construction. Figure 3 describes task composition. Figure 4 separates supervised trajectories from reward-based training. Figure 5 compares prompt-embedding similarities across training and evaluation inputs; it assesses one form of overlap and does not establish the absence of all pretraining exposure. Figure 7 gives a synthetic simulation template.

## Repository Inspection

The inspected GitHub commit is `968dd38bea50102a313d7d36843aba564eabc33f`. The evaluation README requires Python 3.12, R 4.4, statistical R packages, model/tokenizer files, and an OpenAI-compatible endpoint. `run_benchmark.py` executes generated R in a persistent local subprocess and saves trajectories and parsed final answers. `evaluate.py` compares final reported p-values and decisions with the task keys. `verify_pbench.py` checks file availability, hashes, questions, and key/manifest consistency. These checks support integrity and reproducibility; statistical justification remains a separate question.

The training folder contains veRL-based training code and an R tool. Its commands expect model and training-data paths. No training or inference code was executed for the course review, and no model weights were downloaded. The released code does not include a license file in the inspected tree. It is linked, while the course Python implementations are original.

## Benchmark Limits and Course Adaptation

Matching a reference p-value does not independently establish inferential validity, and multiple defensible procedures can produce different values. The paper's evaluation concerns single frequentist hypotheses at a fixed threshold. It does not evaluate multiple-testing correction, sequential monitoring, Bayesian decisions, economic importance, or welfare. A reference test itself requires a specified sample, estimand, weights, and variance estimator.

The consumer-credit task asks about a joint null for 13 advertising-content coefficients. Its archived answer key contains only p=0.0431 and a reject decision. The reference specification has not been reconstructed here. Course materials use the question to examine the scope of an advertising claim without presenting a replicated result.

The implemented mHealth example checks a descriptive paired comparison. The original store simulation has a known sharp null, independent Gaussian stores, fixed equal store sizes, complete observations, and balanced assignment. It measures false-positive rates with two Welch calculations and preserves all prespecified repetitions. These examples implement the assessment principles without claiming to replicate Fisher-R1 or measure any assistant's performance.
