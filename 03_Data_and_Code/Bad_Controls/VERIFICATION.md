# Verification

Checked November 26, 2026, using Python 3.12.14 and NumPy 2.3.5.

## Numerical Comparisons

The three programs executed successfully. A second execution reproduced all eight CSV files byte for byte. Four independent checks passed:

1. Adjustment results preserve the relevant transformations of observation order, control units, and outcome units.
2. The finite populations have the stated probability masses and treatment probabilities.
3. Potential-outcome calculations give a total treatment effect of 4 in every panel cell, and untreated covariate means agree across treatment groups conditional on the observed baseline variable.
4. Project states distinguish commitment from operation, and the sensitivity and population comparisons preserve their stated denominators and counterexamples.

Run the checks from this folder:

```sh
python3 verify_examples.py
```

The regression examples also check their exact analytical slopes during execution. The project example includes both a positive selected-project effect and a second construction in which the operating-project effect and proposal-population effect have opposite signs. These are imposed populations, not estimates of data-center effects.

## Course Integration

`scripts/check_lecture_code.py` confirmed 128 matching, syntactically valid Python blocks across the lecture notes, including the three new programs. The complete notes and the standalone Marketing Dialectics chapter compiled to 593 and 101 PDF pages. Sessions 4, 10, and 14 compiled to 29, 29, and 98 slides; the combined lectures contain 514 slides. The syllabus remains two pages.

Visual review covered 57 rendered pages: revised sections and their boundaries, the affected contents pages, new slides and adjacent slides, the standalone chapter, and both syllabus pages. Four new analytical diagrams and the wide slide version of the causal-path diagram were inspected for labels, arrows, overlap, and readability. The final builds produced no overfull-box warnings.

## Scope

These checks establish reproducibility and agreement with the imposed constructions. They do not validate the electricity paper's design, reestimate its coefficients, or establish exposure among its actual donors. No downloaded third-party code was executed. The reading catalog records access and inspection separately for each source.
