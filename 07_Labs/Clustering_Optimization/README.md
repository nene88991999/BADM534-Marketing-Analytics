# Clustering Optimization and Interpretation

Public, optional, ungraded practice for M4 and Session 6. No model account or external data upload is required. The [full notes](../../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md), [programs and setup](../../03_Data_and_Code/Clustering_Optimization/README.md), and [source guide](../../01_Resources/23_Clustering_Optimization/README.md) provide the definitions and reference results.

## Managerial Question

A team wants to group a large content library so that reviewers can inspect representative items. Decide which computations are necessary before naming the groups, and which additional evidence would justify a customer-facing intervention. Keep the vector representation and number of groups fixed for the algorithm comparison.

## Fifteen-Minute Discussion

1. **Minutes 0–4:** Ten earlier observations have mean 2; two new observations have mean 7. With a half-weight update, compute the exponentially weighted sum, count, and center. Explain why giving the two means equal weight changes the answer.
2. **Minutes 4–8:** For points 0, 4, 5, and 10 and final centers 2 and 7.5, evaluate saved labels A, A, A, B. Reassign each point to its nearest center. Compute both mean squared distances with the same four-row denominator. Verify with `python3 centroid_checks.py`.
3. **Minutes 8–12:** Read `results/summary.csv`. Compare held-out error, fit time, evaluation time, and changed-label rates. Explain why a budget of two has different computational meaning across methods and why these CPU results do not establish a GPU speedup.
4. **Minutes 12–15:** Apply the reasoning to mHealth. Explain how the earlier feature window and later logging comparison help interpretation, and identify the evidence needed to establish an effect of differentiated support.

## Optional Python Comparison

Follow the environment commands in the program README. Run `compare_clustering.py --output local_runs`. Confirm 27 rows in `runs.csv`, three seeds per method and cap, and the same data hashes throughout the comparison. Use each NPZ centroid array to recompute nearest-center distances independently. Compare saved and final labels before calculating segment sizes. Interpret pairwise adjusted Rand agreement in `stability.csv` conditional on fixed data and K.

Change one object at a time: K, initialization seed, or feature scale. Retain the held-out sample for a predeclared comparison. Repeated selection on its loss converts it into development data; a final performance claim then needs a fresh independent sample. Record the version, changes, commands, and output directory. Keep the committed reference outputs intact.

## AI-Assisted Coding

Ask a coding assistant: “Read the data dictionary and comparison program. Write a separate calculation of final-center labels and squared distances for the four-point example. State the denominator, test invariance to relabeling centers, and explain how you would compare saved labels. Do not change the fitting code.” Check the proposed calculation by hand before accepting it. Then explain the weighted-center result and the scope of the timing comparison independently.

## Interpretation Checks

A sound explanation identifies the weighted center as 17/6, the reassigned point as 5, and the final loss as 41/8. It separates a more compact vector representation from evidence that a segment is meaningful or that an action improves customer outcomes. It identifies o-means as optional GPU-focused reading and makes no claim that the course ran it.
