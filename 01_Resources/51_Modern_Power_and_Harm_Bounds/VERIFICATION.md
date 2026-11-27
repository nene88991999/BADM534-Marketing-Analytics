# Verification Record

Verified November 27, 2026.

## Sources and Access

The catalog contains 11 sources published or circulated in 2018–2026. Ten reference PDFs were downloaded and checked for PDF signatures, file sizes, page counts, and SHA-256 hashes. Their versions and inspected passages are recorded individually. The 2026 DID power article was inspected through its publisher abstract and metadata; its restricted full text was not obtained. The reference PDFs are ignored by Git. Public annotations and source links retain attribution.

The electricity study's unchanged 42-page source was checked at the relevant reported tables. Table 2, column 4 supplies 0.261 and SE 0.158; Table 4, column 4 supplies 0.158 and SE 0.160. The existing sales example's source locator was corrected to Table 7, column 1, with its numerical inputs unchanged. The preferred residential estimate meets the paper's 10% convention. The source has positive findings and is not represented as a universally insignificant study. The HBS coverage was checked as a separate public statement.

## Executed Calculations

The [program](../../03_Data_and_Code/Modern_Power/harm_bounds.py) and [independent verification](../../03_Data_and_Code/Modern_Power/verify_harm_bounds.py) ran with Python 3.13.5, SciPy 1.15.3, and NumPy 2.1.3. The saved output contains the six price comparisons and three imposed bias scenarios discussed in M6 §§6.47–6.51.

Checks covered numerical integration of normal rejection tails, independent folded-normal quantiles and probabilities, rejection probability at both equivalence boundaries, decreasing rejection probability outside the margin, unit invariance, test/interval duality, and agreement with the saved output. A synthetic informative case checks that the implementation can establish equivalence when the mathematical conditions warrant it. The TikZ diagram's endpoints come from the verified residential estimate and SE.

The reference scaling is a ratio of reported means, 100(456/6804). Four-owner slopes retain their own exposure-point units. Price margins are teaching alternatives, with no claim to be prespecified or validated tolerances. Every displayed price margin remains unresolved at 5% under the one-sided margin test, TOST, and scalar folded-normal test. This finding concerns these comparisons under a fixed Gaussian approximation. It does not imply that every method must fail at every margin, or identify realized household harm.

Panel-design power, cluster-bootstrap inference, joint pre-trend equivalence, HonestDiD, and synthetic-control prediction procedures were reviewed for their required inputs. They were not run on an unavailable original utility panel. The bias allowance is an imposed scalar sensitivity parameter, with no estimate of actual bias or undocumented standard-error multiplier.

## Course Integration and Rendering

The complete notes and standalone Marketing Dialectics chapter compiled to 679 and 142 pages. Sessions 9 and 14 compiled to 50 and 130 slides; the combined deck has 575 slides. The calendar remains 15 meetings of 170 minutes with no guest speakers. The new slides are alternatives within existing discussion blocks, with extended calculations in optional ungraded practice.

Visual review covered 26 rendered pages: full-notes pages 376–383 and 677–679, standalone chapter pages 140–142, Session 9 slides 45–50, Session 14 slides 127–130, and full-notes contents pages 8 and 13. The figure preview was also inspected. A crowded figure label was repositioned and the final outputs re-rendered. No clipping, overlap, broken equations, or unreadable table headings remain on these pages.

The source comparison verified 135 matching, syntactically valid Python listings across the lecture notes. The repository contains 160 referenced TikZ figures with PNG companions. Generated Markdown and LaTeX accompany the PDFs; private conversation records and source-reading copies remain excluded from publication.
