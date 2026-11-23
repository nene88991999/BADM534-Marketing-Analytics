# Agent Guide for Reproducible Recommendations

Read the local README and the Synthetic_Consumers data dictionary before the numerical evidence. The data are invented. Preserve the distinction between the response mapping and the separate six-concept panel. No model calls or observed consumer preferences appear in these inputs.

Keep persona weights, row weights, and repeat counts explicit. Preserve undefined correlation, shortlist, and recall as missing. Trace every numeric statement to `results/evidence.json` and its named source table. A passing equality check proves consistency with recomputation, not empirical validity. Human review must assess scope and the proposed action.

Use the full Python in M1 §1.15 and the same file here. Run the six local checks after analytical changes. Keep the relative folder structure when moving a project. Regenerate the report after changing code or inputs and review its content and links before publishing.

Suzuri is optional. Its source review is static; do not claim its application, exporter, synchronization, or AI integrations were tested here. Pandoc export checks apply to the recorded Pandoc invocation only. A successful single-document export does not certify a deployed multi-page wiki.
