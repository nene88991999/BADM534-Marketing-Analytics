# Conformal Prediction Example Guide

Read the root agent guide and this folder's README. Keep the complete program blocks in M7 synchronized with `conformal.py`, `demand_intervals.py`, and `complaint_sets.py`.

- Preserve the exact finite-sample rank, inclusive boundary, and infinite-threshold case. Do not silently clip an unattainable rank to the largest calibration score.
- Keep the fixed predictor and predefined segments independent of calibration and evaluation outcomes. The current records are deterministic synthetic illustrations, with no fitted model.
- Retain every evaluation store and distinguish the paired outcome-change scenario from a new sample. Report segment counts and widths alongside coverage.
- Distinguish marginal coverage, group coverage, probability calibration, and error conditional on automatic routing. No single one implies all the others.
- Treat prediction intervals for future outcomes separately from confidence intervals for population means. A nominal level is conditional on the method's assumptions.
- Run both original programs and `test_conformal.py` after changes. Compare TikZ values with the generated tables and verify full code blocks with `scripts/check_lecture_code.py`.
- Do not execute the upstream notebooks or install their packages merely to explain this example. The source review and original course execution are separate records.
