# Verification Record

Checked November 26, 2026 with Python 3.12.14, NumPy 2.3.5, pandas 2.2.3, and SciPy 1.16.3. The four additional analysis programs and figure builder ran successfully. No model calls or downloaded third-party code were executed.

## Numerical Checks

All 25 inference tests passed, including the ten existing checks for paired mHealth summaries and clustered store experiments. Fifteen additional checks compare pooled tests with SciPy, power with an independent noncentral chi-square calculation, campaign inference with the chi-square identity, economic units and break-even arithmetic, expected-count denominators, shifted equivalence tests and interval duality, scaling of confidence bounds, inversion of a one-sided test, and equal aggregate revenue under unequal household incidence. Invalid precision and other unsupported inputs are rejected.

A fresh source export starts with empty result and figure folders. The four new programs reproduce 14 result files byte for byte, and the figure builder reproduces five TikZ sources byte for byte. All 110 full Python source listings match their executable counterparts and parse successfully. Earlier mHealth inputs and the seven pre-existing numerical outputs remain unchanged; their preceding verification record is retained in Git history.

Published coefficients were checked visually against the paper's Tables 2, 4, and 7. The developer-difference p-value is transcribed from its reported Wald test. No covariance matrix is reconstructed. Power, intervals, and minimum detectable effects use a normal approximation at fixed reported clustered standard errors and rounded published inputs. These calculations assess reported precision and interpretation; they do not re-estimate the original utility panel.

## Figures and Documents

Five additional Illinois-color TikZ figures cover repeated p-values, campaign contribution, cancellation equivalence, electricity-price power, and household incidence. Plotted values come from checked result tables. The household diagram uses explicit synthetic inputs with equal use and total revenue. Figures retain units, populations, labels, and text companions.

Visual review covered 75 rendered pages: new notes and code, affected contents and neighboring pages, the Marketing Dialectics chapter, eleven new slides and neighbors, and both syllabus pages. The p-value, power, and household diagrams were also inspected at full page size. Final builds have no overfull boxes, missing characters, undefined controls/references, or TeX errors. Existing package and underfull-spacing warnings remain.

The combined notes contain 480 pages and 121 original figures. Marketing Dialectics has 41 pages. Sessions 4, 9, and 14 have 26, 33, and 57 slides; the combined deck has 442. The syllabus has two pages. All 15 dates, logistics, and continuous 170-minute allocations remain unchanged.

## Interpretive Scope

The repeated experiments, campaign, cancellation summaries, and household allocations are synthetic. The electricity case computes implications of published summary estimates. It distinguishes nonrejection, equivalence, power, effect bounds, causal identification, economic importance, and ethical justification. Low power against specified alternatives does not prove a positive true effect or uniquely explain an observed nonsignificant result.

Verified public reassurance is attributed to HBS coverage. Company dissemination on X remains unverified because direct search required authentication. The critique identifies potential consequences of misleading reassurance without claiming that the paper caused an observed policy decision or household loss. Instructor philosophy manuscripts and private notes are not published.
