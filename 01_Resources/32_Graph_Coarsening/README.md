# Graph Coarsening and Marketing Decisions

A firm may compress a large customer or retail network to reduce computation. The relevant question is whether the smaller representation preserves the comparisons used to allocate service, predict demand, or recommend products. A graph can preserve selected features while changing travel access or the treatment of a small customer group.

Antonin Joly's [GraCo repository](https://github.com/Antonin-J/graco) and [working paper](https://arxiv.org/abs/2611.01200v1) provide a common interface for 17 graph-coarsening methods and a random baseline. The [source review](SOURCE_REVIEW.md) connects its mathematical construction, evaluation metrics, and implementation defaults to the course. The [case design](CASE_DESIGN.md) develops original examples for M5 and M7, with shorter connections to M1, M2, M4, and M9.

## Course Connections

| Module | Decision or Analytical Question | Useful Extension |
|---|---|---|
| M5 | Does a compressed retail network preserve customers' access to available stores? | Compare original routes, grouped zones, and the population receiving weight. Build on [§5.21](../../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md). |
| M7 | Which evaluation criterion supports deploying the smaller model? | Separate label purity, prediction on held-out outcomes, computational cost, and customer consequences. Build on [§7.28](../../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md). |
| M4 | What does a group mean represent? | Retain group sizes and distinguish average spending from spending totals; connect to [§4.22](../../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md). |
| M1 and M2 | Which data transformations does generated code actually perform? | Inspect graph direction, discarded components, outcome-dependent parameters, and denominator changes. |
| M9 | Whose needs survive aggregation? | Evaluate group-specific errors and preservation of service access beside the firm's computational saving. |

The strongest placement is a focused extension to the existing networks and model-evaluation material. The seventeen algorithms can remain advanced references. The lecture notes, decks, and assessment requirements have not been changed by this resource review.

## Calculations and Interpretation

[Seven original checks](source_checks.py) run with Python's standard library:

```bash
python3 01_Resources/32_Graph_Coarsening/source_checks.py
```

[Saved results](source_checks.json) distinguish invented four-zone arithmetic, label examples, a recalculation of the existing synthetic retail case, and selected published Cora rows. No GraCo dependency was installed, no upstream program was run, and no graph neural network was trained.

In the existing retail case, removing the disconnected origin changes the denominator from 800 people to 650. Known access remains 550 people, so the reported share rises from 68.75% to 84.62%. In a separate four-zone construction, the revenue feature and its graph energy are preserved exactly, while interpreting the coarse graph as a travel network changes a nine-minute route to four minutes and raises apparent five-minute access from 75% to 100%. These calculations illustrate different estimands and transformations; they are not empirical findings about GraCo users or marketing outcomes.

## Sources and Rights

The [catalog](catalog.json) uses the namespace `graph-coarsening`. The unmodified [paper](papers/Joly_WorkingPaper2026.pdf) is by Antonin Joly, arXiv:2611.01200v1, October 31, 2026, under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). It is accompanied by the textual review and figure descriptions in this folder.

The `reference/` directory contains 21 selected files from commit `19da8a6031dcf1803faa5723148b5975a5462af6`, including the original MIT license, Apache-2.0 license, and third-party notices. It is a partial source reference and cannot be installed as a complete package. The [manifest](manifest.json) records hashes, provenance, and reading scope. Repository documentation retains its original links and terminology. Original course commentary and calculations are separate from these unchanged source files.
