# Verification Record

Executed November 25, 2026 with Python 3.12.14, NumPy 2.3.5, pandas 2.2.3, and SciPy 1.16.3. Both analytical programs and the figure generator ran successfully. No upstream code, source-model inference, or model API was executed.

## Numerical and Design Checks

Ten unittest checks passed. They examine a fixed roster with duplicate days and a later entrant; a paired test against SciPy; preservation of user pairs; rejection of missing pairs; Welch arithmetic against SciPy; a hand-calculated store-mean contrast and standard error; duplicated customer rows with unchanged store information; rejection of unbalanced assignment; a Wilson interval boundary; and deterministic simulation with the analytical variance.

The full food-release SHA-256 hash matches the existing manifest. The reconstructed mHealth mean change and paired standard error match the prior visualization calculation. For the saved first store experiment, independently calling SciPy's two-sample test reproduces both p-values. Across the four correlations, empirical-to-analytical standard-deviation ratios range from 0.9890 to 1.0044. Rejection counts reconcile with fractions and denominators.

A fresh source export, with an empty result folder and the full verified release input, reproduces all seven numerical result files and both TikZ sources byte-for-byte. The existing lecture-example verifier also passed in a separate export; its values agree with the published reference files. `scripts/check_lecture_code.py` verifies 103 exact, syntactically valid source listings in the notes, including the two new programs.

## Figures and Documents

Two editable Illinois-color figures describe assignment units and plot rejection fractions from checked tables. Monte Carlo intervals, uncertainty about an effect, and outcome dispersion are identified separately. Visual review covered 46 rendered pages: new note sections, code listings, affected contents pages, neighboring page breaks, the Marketing Dialectics chapter tail, all seven new slides and their neighbors, and both syllabus pages. Final builds have no overfull boxes, missing characters, undefined references, or TeX errors. Existing package and underfull-spacing warnings remain.

The complete notes contain 451 pages and 114 figures. Marketing Dialectics contains 36 pages. Sessions 1, 4, 9, and 14 contain 28, 23, 28, and 51 slides respectively; the combined deck has 425 slides. The syllabus remains two pages. All 15 meeting plans retain continuous 170-minute allocations and their existing dates.

## Scope

mHealth results concern descriptive recorded logging in the selected cohort. The synthetic experiment evaluates one prespecified test with independent Gaussian stores, equal store sizes, balanced assignment, and complete outcomes. It does not measure AI performance, reproduce the source model, or assess all possible clustered designs. The public advertising task supplies a discussion question; its empirical reference p-value and specification remain unreplicated here.
