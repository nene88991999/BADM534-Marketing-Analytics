# Network Compression and Predictive Evidence

A retail manager wants faster analysis while preserving revenue accounting and service access. A customer-service manager wants a smaller graph that still identifies uncommon specialist needs. Evaluate the representation against each decision and state what information may be used to fit it.

This activity is public optional ungraded practice. It creates no submission deadline or course-wide AI-use rule. Read [M5 §5.24](../../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md), [M7 §7.38](../../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md), and the [data dictionary](../../03_Data_and_Code/Graph_Coarsening/DATA_DICTIONARY.md).

## 1. Retain the Original Population

Run the two commands and independent tests in the [example README](../../03_Data_and_Code/Graph_Coarsening/README.md). Reproduce the mean revenue, total revenue, energy, travel times, and access counts by hand before interpreting the output. Explain why a zero feature-reconstruction error can coexist with a nine-minute trip represented as four minutes.

In a local copy of the input, change A's population from 100 to 700. Hold edge times, store availability, and group membership fixed. Predict the original access share and then calculate it. Restore the original population and set the threshold to four minutes. Explain which original origins cross the threshold. Finally assign every original zone its own group and check whether the two route calculations agree.

## 2. Follow the Labels

For the three labels 0, 0, 1, identify which outcome chooses the training-only constant and which outcomes choose the oracle majority. Write the denominator beside each score. Reassign the evaluation subset to the last node alone and explain why the global-majority score is below that subset's own optimal constant score.

In the separate parameter example, change only the held-out outcome. Compare disagreement using all edges and using training-training edges. Explain why final scored accuracy may change when reference labels change, while preprocessing and fitted predictions should remain invariant to outcomes that were forbidden during fitting.

For the two groups with one specialist customer each, calculate the confusion counts and class-1 recall. Propose a service loss that gives missed specialist needs an explicit cost, and state what evidence would justify that cost.

## 3. Inspect the Source Before Accepting Generated Code

Read the pinned [preprocessing](../../01_Resources/32_Graph_Coarsening/reference/loaders/preprocess.py), [label metric](../../01_Resources/32_Graph_Coarsening/reference/metrics/structural.py), and [UGC](../../01_Resources/32_Graph_Coarsening/reference/algorithms/ugc.py) functions. Identify the defaults controlling components, direction, label choice, and alpha. Use the [source review](../../01_Resources/32_Graph_Coarsening/SOURCE_REVIEW.md) to check the exact version and operator convention. Reading these files requires no dependency installation.

A coding request can specify: “Use the four synthetic zones and retain all original people. Keep travel minutes separate from graph affinities. Report achieved group count, group sizes, revenue means and totals, and access at every original origin. For prediction, use only the stated training labels to fit preprocessing and constants. Preserve untouched test outcomes. Add an independent path enumeration and a held-out-label intervention check.”

Compare the generated program with the requested objects and inspect every default that changes them. Record material AI assistance and distinguish code inspection from execution. A package call and a saved output do not establish that the claimed quantity was evaluated.

## 4. Recommend a Representation

Choose a primary customer outcome before comparing methods. State the original population, weights, target compression, achieved size, feature convention, label permissions, tuning budget, runtime, and memory. Use the uncompressed graph and a simple grouping baseline. Evaluate access or service errors at original nodes, including disconnected customers and uncommon needs.

Explain whether the computational saving justifies the observed errors and what would change the recommendation. Connect the affected customers' ability to obtain service or contest a decision to [M9 §9.18.2](../../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md). The source toolkit's full benchmark and graph-neural-network training require a separately specified implementation and computing budget.
