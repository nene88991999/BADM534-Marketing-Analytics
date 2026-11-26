# Agent Guide for Statistical Inference

Read the root agent guide, this folder's README, data dictionary, and verification record. Preserve complete runnable code in M3 §3.18 and M6 §6.30 when editing either program; run `scripts/check_lecture_code.py` afterward.

- mHealth results describe observed logging within the fixed cohort. Days without an entry are zero recorded logging, not zero consumption. Preserve the initial roster, unique days, and paired users.
- The store experiment is synthetic, with zero effects, equal store sizes, independent Gaussian stores, and balanced store assignment. Each method receives the same outcomes. Do not select a dataset or method because its p-value is favorable.
- Monte Carlo rejection rates, benchmark agreement rates, and AI model performance are distinct quantities. The course programs measure the first; no model endpoint has been evaluated.
- The independent-day and customer-row methods are deliberate comparison procedures. Do not present their uncertainty as appropriate under the dependence they omit.
- The public credit-advertising task has a reference answer but no reconstructed reference specification here. Do not call it a verified empirical replication or infer borrower welfare from loan take-up.
- Preserve the source license distinctions. Upstream code is linked only; model and benchmark licenses do not establish a license for the GitHub code.
- Optional practice is ungraded. No assignment rules or permitted AI use can be inferred from this folder.
