# Verification of Reproducible Recommendations

Verified November 22, 2026. The original course program ran with Python 3.14.8 using only the standard library. No model call, Suzuri installation, upstream build, or upstream test ran.

## Numerical and Execution Checks

The six checks in `test_recommendation.py` passed: independent response and weighting arithmetic; fixed-persona repeat comparisons; undefined quantities distinguished from zero; detection of a stale table; detection of a missing table; and identical outputs from three working directories in a relocated project. Temporary copies preserve the released inputs. The ten existing synthetic-consumer checks and the general lecture-example verification also passed.

The wrapper recomputed all four saved synthetic-consumer tables. The equal-persona refill mean is 3.975 and the equal-row mean is 4.066667 for three responses from two personas. Increasing p01's identical repeat count to five raises the equal-row mean to 4.158333. The pooled shortlist remains undefined; the reversed pattern selects F and E with zero reference-top-two recall. Independent arithmetic checks address selected numerical properties, while comparison with the saved tables checks consistency.

Both five-point TikZ series were checked against the evidence file. All 81 full Python blocks in the lecture notes match their scripts and parse successfully. These checks establish properties of the supplied synthetic constructions; they do not validate actual customer preferences or general language-model performance.

## Rendering and Export

The complete notes and Sessions 1 and 14 compiled with the existing course builders. The revised prose, complete program, table, new figure, and three new slides were visually inspected. The notes have 358 pages and 94 TikZ figures; the fifteen decks contain 365 slides. Meeting dates and 170-minute durations remain unchanged.

Pandoc 2.12 exported a disposable copy of the generated report using the lab's `markdown+tex_math_dollars`, `--standalone`, `--mathml`, and `pagetitle` command. The HTML structure preserves one title, all five rating rows, the expected-rating expression, ordinary currency amounts, and the figure description. The local browser preview displayed the equation, table, and figure. The evidence-link request returned HTTP 200; inline JSON viewing was not established. The five linked file destinations and image destination were checked in the isolated preview folder. No multi-page site or GitHub Pages deployment was tested or published.

## Source Review and Optional Checks

Suzuri's wikilink conversion, missing-embed handling, attachment copying, and synchronization behavior remain findings from the pinned source review. No application execution establishes those behaviors in this course environment. Notebook kernel tests, Suzuri export tests, live assistant responses, and fresh-browser tests of a future course wiki remain optional or pending. The report is generated deterministically from course calculations.

The [manifest](manifest.json) records hashes for the example, its dependency files, and the figure. A hash identifies bytes; numerical validity, interpretation, source permissions, and publication decisions require their respective evidence.
