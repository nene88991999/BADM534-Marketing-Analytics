# Interactive HTML Wiki

**Status: design and implementation pending.** The resource collection and Markdown course structure provide the source material for a future GitHub-hosted site.

Keep the future site's content in the repository so the same material remains readable as Markdown. Preserve stable module IDs, text descriptions of interactive figures, accessible navigation, and links to executable notebooks where needed.

[Design and hosting notes](../01_Resources/11_GitHub_HTML_and_Interactive_Teaching/Design_Notes/README.md) compare possible approaches. No framework or deployment workflow has been selected, and no site is published.

## Clustering Interaction

The [clustering source guide](../01_Resources/23_Clustering_Optimization/README.md#future-wiki-interaction) proposes an original four-point interaction for moving centers, reassignment, and batch weighting. [Exact Python calculations](../03_Data_and_Code/Clustering_Optimization/centroid_checks.py) and editable Illinois-color figures provide independent reference values. A future implementation should expose the inputs and denominator in accessible text and separate animation from measured computational performance.

## Authoring and Export Portability

[The Suzuri source review](../01_Resources/30_Research_Writing_and_Coding/README.md) motivates keeping notes, code, source descriptions, and expected results together. Its inspected HTML exporter creates a standalone document and converts internal wikilinks to display text. The future course site should preserve standard relative links and stable module identifiers, with separate checks for navigation, calculation, rendering, and accessibility. The [released optional exercise](../07_Labs/Reproducible_Recommendations/README.md) supplies a generated recommendation, numerical evidence, and a repeat-weight figure for evaluating a later prototype. No editor or site framework has been selected.

## Representative Page Checks

Use the [product-screening recommendation](../03_Data_and_Code/Reproducible_Recommendations/results/recommendation.md) as one source fixture. Preserve the $500 and $25 currency amounts, the expected-rating equation, all five category weights, the figure description, and access to data and code. The program and checks run without a model account. Pandoc can provide a disposable single-page preview; source-file links and section anchors still need explicit mapping when a site builder creates HTML pages.

Before publishing a site, check a fresh browser and a clean checkout. Confirm that every rendered destination resolves, figure values agree with the evidence file, keyboard navigation works, and the downloadable calculation reproduces. A source review, a Python test, and a document export establish distinct properties. None is a deployment record. See the example's [verification scope](../03_Data_and_Code/Reproducible_Recommendations/VERIFICATION.md).
