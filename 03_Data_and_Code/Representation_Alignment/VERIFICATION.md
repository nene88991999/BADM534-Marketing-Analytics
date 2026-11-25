# Verification Record

Executed November 25, 2026 with Python 3.12 and NumPy 2.3.5; preparation used pandas 2.2.3. The full mHealth release passed its SHA-256 check before sample construction. The compact input hash is retained in the manifest, and the evaluator verifies it before fitting.

Three original programs ran: preparation, the synthetic alignment calculation, and the local mHealth comparison. Nine independent tests cover an affine map on fresh points, degenerate inputs, exact distance preservation and a known classification reversal, neighbor ties and self-exclusion, modal-label ties, frozen training vocabulary, known classifier decisions and unseen categories, split disjointness, and reconciliation of every saved test prediction with aggregate and category-specific counts. The selected dimension is independently recovered from saved validation scores.

No external data upload, language-model API call, upstream program execution, or checkpoint download occurred. The original post's neural-model experiments were not reproduced. PDF and figure readability are reviewed separately from these numerical checks.
