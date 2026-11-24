# Verification

Verified November 23, 2026. Both original analysis programs ran with Python 3.14.8 and the standard library. The calculations are deterministic and use the committed synthetic inputs. GraCo, its dependencies, its benchmark, and graph-neural-network training remain unexecuted. There were no model calls.

## Numerical Checks

Nine tests in `test_examples.py` passed. They check revenue accounting; the graph energy against an independently written Laplacian quadratic form; shortest paths against enumeration of all simple paths; access thresholds and unequal population weights; the identity partition; oracle purity against exhaustive binary label assignments; minority confusion counts; intervention on a held-out label; and the empty-training-group error.

The four-zone program produced original access 300/400, naive coarse access 400/400, original mean zone revenue 17.50, equal-group mean 25, total revenue 70, and both graph energies 225. The label program reproduced full-group purity 2/3, test scores 1 and 0 under the stated information sets, zero recall for two specialist-service customers, and the all-edge disagreement change from 0 to 0.5. These are constructed finite comparisons, with no empirical performance claim.

The existing lecture-example verification program also completed. All 85 Python source blocks in the notes matched their runnable files and passed syntax compilation. The archived GraCo paper, 21 selected source files, and the seven earlier review calculations retained their recorded hashes.

## Figures and Documents

The two editable TikZ figures were checked against the saved inputs and aggregate results. The four-zone diagram retains 4, 1, and 4 minute edges, group sizes 3 and 1, original access 75%, apparent coarse access 100%, and energy 225. The label diagram retains the separate training node, two held-out nodes, both test denominators, and full-group purity 2/3.

The final notes compile to 380 pages with 99 TikZ figures. Session 7 has 41 slides and Session 11 has 48; the combined deck has 379 slides. Marketing Dialectics has 30 pages and the syllabus has two. The five new slides, both figure previews, both syllabus pages, and affected note pages were rendered and inspected. Figure-label spacing and paragraph/equation pagination were corrected before release. The changed builds have no overfull-box errors.

The meeting plan retains 15 meetings of 170 minutes, including the existing breaks. Graph coarsening uses fifteen minutes in Session 7 and five in Session 11. The practice activity is optional and ungraded. No grading, deadline, or course-wide AI rule was introduced.
