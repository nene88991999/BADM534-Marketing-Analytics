# Retail Access and Service Priorities

A manager can restore one unavailable location. Which action improves access, and how does that answer depend on the objective? This is optional ungraded practice. Use [the complete programs and frozen inputs](../../03_Data_and_Code/Retail_Accessibility/README.md) and [M5 §§5.21–5.22](../../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md).

## 1. Specify the Decision

Define origins, candidate stores, population weights, travel costs, availability states, and the five-minute threshold. State why the four-store denominator for known unavailability differs from the 800-person denominator for access. Predict how each restoration changes the result before running code.

## 2. Check a Route and a Missing Record

Run `accessibility.py` using the README commands. Trace W0 to E0 by hand: the network takes 18 minutes while the straight-line proxy takes two. Compute the access count with U unavailable and with U available. Retain X in both denominators. Explain why deleting X raises the baseline lower share from 68.75% to 84.62% without improving anyone's access. Distinguish the missing-status bound from uncertainty about travel times or sampling variation.

## 3. Compare Relationships on Equal Terms

Use the same six connected nodes and k=1 for both neighbor definitions. Reconcile six directed edges in each graph and two shared edges. Calculate actual network time along both sets of links. Repeat for k=2. Explain why changing both k and the metric would obscure which change caused the result. A neighbor graph describes a chosen relationship; it does not establish customer interaction or spillovers.

## 4. Interpret an Observed Location Comparison

Run `snapshot_access.py`. Check the four restaurant IDs, the October snapshot, the later street timestamp, access tags, boundary, and snapping distances. Confirm the North Neil ranking reversal in `observed_pairs.csv`. Hold eligible targets fixed. Explain which extra information would be needed to assess customer access, substitute products, entrances, and historical pedestrian travel. Do not infer that all residents lack alternatives from four restaurant-origin distances.

## 5. Separate a Map From Its Measurement

Run `cartography.py`. Calculate the outer square's area, the hole's area, and their difference by hand. Compare reachable nodes before and after filling. Formulate a chart caption that states both results. Explain why filling a visual gap does not create a bridge or grant access across a private parcel.

## 6. Evaluate the Service Objective

Compare Restore A and Restore D using known-store availability, five-minute population access, and the imposed weekly profit gains. Keep restoration costs equal as assumed. Identify a benefit of D that the threshold count omits. Repeat the access calculation under a different threshold and document the changed comparison. A Kantian argument should examine the firm's maxim, respect for customers' purposes, and what its recommendation tells them. A Confucian argument can examine reliability and the conduct expected from the service provider. Neither framework supplies the five-minute cutoff without further reasons.

## AI-Assisted Coding

Ask an assistant to explain one transformation or propose one extension, then inspect the relevant source and verify a small case independently. A useful prompt is: “Keep every origin and unknown status. Add a threshold parameter without changing the target set. Give expected results for two hand-calculated routes before changing the program.” Check generated tests against separate arithmetic or path enumeration. Record changes, commands, and results. Apply the relevant assignment's AI rules if this practice is later assigned.

## Optional Spatial Modeling Extension

[The source guide](../../01_Resources/25_Spatial_Networks/README.md) links city2graph's proximity, transport, and graph-learning examples. Inspect dependencies and inputs before choosing an environment. Compare a simple tabular model with a graph model on the same features, target, splits, and decision metric. Future-period evaluation and transfer to a new city answer different questions. Geographic proximity alone does not establish causal spillovers.
