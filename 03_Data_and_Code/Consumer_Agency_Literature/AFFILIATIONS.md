# University Affiliations and Research Communities

## Decision and Coverage

An affiliation-based grouping asks which universities appear together on papers and whether those groups cover different research mechanisms. It complements the paper-level mechanism clusters. It does not identify an institution's intentions, policy, or causal influence on an author's work.

The input covers all 824 eligible census records, regardless of full-text access. Work-specific OpenAlex authorship metadata identifies at least one education institution for 745 papers (90.4%); 79 remain unassigned. The identified set contains 424 institutions and 1,905 distinct paper-institution pairs. OpenAlex's `education` category includes universities, colleges, and independent business schools. Companies, hospitals, government agencies, and other noneducation affiliations are excluded from this particular analysis.

The source is the affiliation attached to the work in the November 2026 metadata snapshot, rather than an author's current profile. Automated affiliation matching can be incomplete or incorrect. Institution IDs and ROR links preserve the resolution used; similarly named campuses and separately identified schools are not silently merged. A work's institutions can combine information from several publication versions and therefore need not perfectly reproduce its final printed affiliation line. Source documentation: [OpenAlex authorships](https://help.openalex.org/data/authorships/), [institutions](https://help.openalex.org/data/institutions/), and [CC0 data license](https://github.com/ourresearch/openalex-docs/blob/main/license.md?plain=1).

## Network Construction

The network connects two universities when they appear on the same paper. This is a shared-publication affiliation network. A link can arise through distinct coauthors or through one author's multiple affiliations. Twenty-one records repeat the complete multi-institution list across every author; the data flag that pattern instead of treating the author-institution mapping as independently verified. The graph uses the union of institutions on each paper, so it does not require assigning each affiliation to a particular person.

A paper with k distinct institutions contributes total edge weight one, divided equally across its k(k-1)/2 pairs. Thus a two-university paper contributes one to its single link, while a three-university paper contributes one-third to each of three links. Repeated authors at the same university do not multiply its presence. Single-university papers contribute no cross-university edge but remain in publication totals.

Louvain modularity clustering uses weighted edges, resolution 1, and seed 534. Nine institutions have no shared-paper edge and remain unconnected, outside community estimation. Community IDs are ordered by fractional publication totals after estimation. The algorithm is a heuristic and does not establish a unique or natural institutional grouping. See the [NetworkX method documentation](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.community.louvain.louvain_communities.html) and Blondel et al. (2008), [Fast Unfolding of Communities in Large Networks](https://doi.org/10.1088/1742-5468/2008/10/P10008).

## Counting Papers Across Communities

Each paper contributes 1/k to each of its k universities. These weights are summed within communities, so a paper spanning several communities contributes fractional weight to each while contributing one overall. The total across communities and unconnected institutions is 745. Distinct-paper counts can overlap across communities and must not be added as a unique total.

The mechanism overlay uses only reviewed papers classified as potential dual use or a reported choice concern. Each community's feature share uses its own fractional reviewed-risk denominator. Unreviewed papers remain missing. Rows with fewer than ten distinct reviewed-risk papers carry a small-sample flag. These profiles describe selected publications; they are not institutional harm rates or evidence that a university endorses any practice.

## Reproduce and Inspect

```bash
python3 03_Data_and_Code/Consumer_Agency_Literature/affiliation_clusters.py
```

The public `paper_affiliations.csv` and `affiliation_coverage.csv` are sufficient for the network. `coded_papers.csv` supplies the optional mechanism overlay. `extract_affiliations.py` regenerates those inputs from the Dropbox-only OpenAlex cache. The exported source work URL, institution ID, ROR link, and source update date make each mapping traceable. No additional author-profile request is required.

[Results and Sensitivity](results/affiliations/README.md) describes the fitted communities. `university_membership.csv` gives every institution's assignment; `university_edges.csv` gives shared-paper links; `paper_community_weights.csv` preserves every allocation; `community_summary.csv`, `journal_profiles.csv`, and `mechanism_profiles.csv` describe the groups. The run also varies random seeds, resolution, and full versus fractional link counting.

## Source Checks

Five retrieved-paper affiliation blocks were checked against their paper-level institution sets. Four matched the retrieved version. The published Immersive Service article also names the University of Vaasa, which was absent from the OpenAlex record; that affiliation was added with its verified OpenAlex and ROR identifiers. `affiliation_corrections.json` preserves the source and date. This targeted check does not validate all 745 records.
