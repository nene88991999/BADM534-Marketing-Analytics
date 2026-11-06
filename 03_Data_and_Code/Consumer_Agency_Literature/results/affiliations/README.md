# Affiliation Clustering Results

## Fitted Network

The corrected input contains 424 higher-education institutions from 745 eligible papers with identified affiliations. It has 1,766 distinct shared-paper links contributed by 601 papers with multiple institutions. Nine institutions have no cross-institution edge. Weighted Louvain clustering at resolution 1 and seed 534 produces 19 communities among 415 connected institutions, spanning six connected components. Modularity is 0.471.

The six largest communities by fractional publication total are below. A paper contributes one unit split equally across its universities. Example institutions are the largest contributors under that accounting rule; they do not define the full membership or the community's purpose.

| Community | Institutions | Fractional Papers | Largest Affiliation Contributors |
| --- | --- | --- | --- |
| C01 | 44 | 154.15 | Columbia University; The University of Texas at Dallas; Chinese University of Hong Kong; Yale University |
| C02 | 56 | 84.54 | University of Hong Kong; Indiana University; Duke University; Texas A&M University |
| C03 | 40 | 74.65 | University of Washington; University of Florida; University of Missouri; Hong Kong Polytechnic University |
| C04 | 26 | 67.16 | University of Pennsylvania; University of Wisconsin–Madison; University of Notre Dame; The University of Texas at Austin |
| C05 | 24 | 57.80 | Cornell University; Washington University in St. Louis; Imperial College London; University of Virginia |
| C06 | 35 | 48.52 | Vienna University of Economics and Business; University of British Columbia; University of Tennessee at Knoxville; Emory University |

## Stability and Interpretation

Across twenty seeds at resolution 1, agreement with the primary partition has adjusted Rand index 10th/50th/90th percentiles of 0.442/0.522/0.597. Giving each university pair a full count for each shared paper, instead of dividing one unit across its pairs, lowers agreement to 0.193. Membership depends materially on weighting and local optimization. Resolution 0.5 and 1.5 comparisons are in `sensitivity.csv`.

The [mechanism profiles](mechanism_profiles.csv) overlay reviewed-paper codes using fractional allocations and explicit denominators. C01 has 22 distinct reviewed-risk papers but only 13.53 fractional papers. C03 has eight such distinct papers and is flagged as a small review sample. These uneven subsets do not support ranking institutions by agency erosion. Shared-paper links also include dual affiliations and do not prove collaboration between distinct research teams.

## Outputs

- [University Membership](university_membership.csv): every institution, community, distinct-paper count, fractional papers, and weighted degree.
- [Community Summary](community_summary.csv): every community and the separate unconnected category.
- [Shared-Paper Links](university_edges.csv): fractional edge weights and raw shared-paper counts.
- [Paper Allocations](paper_community_weights.csv): traceable weights and reviewed features.
- [Journal Profiles](journal_profiles.csv) and [Mechanism Profiles](mechanism_profiles.csv): descriptive composition.
- [Sensitivity Runs](sensitivity.csv) and [Summary](summary.json): settings, stability, and version.

Definitions, missing-affiliation treatment, source checks, and commands are in [AFFILIATIONS.md](../../AFFILIATIONS.md).
