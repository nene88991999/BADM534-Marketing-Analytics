# Executed Comparisons

## Measurement and Geographic Coverage

The release has 28,561 distinct identifiers across the 50 states and DC; 2,214 leading zeros are restored. Every identifier matches the archived Census extracts. Fifty boundary-income values are flagged, yielding 28,511 common regression rows. All 1,253 Illinois areas have map coordinates and enter clustering; 1,252 enter the national regression sample. The equal-ZIP correlation of the two indices is 0.521531.

## Regression

| Specification | MCI per $10,000 | CCI per $10,000 |
| --- | ---: | ---: |
| Income alone | 0.055213 | 0.048563 |
| Education and broadband | 0.002094 | -0.018209 |
| Controls and state intercepts | 0.001322 | -0.017497 |

Each row uses the same 28,511 areas and equal geographic weights. With ACS household weights and the two controls, the slopes are 0.004109 and -0.011857. Changing weights changes the projection. These comparisons do not estimate an income intervention or propagate ACS uncertainty, privacy noise, or spatial dependence.

## Illinois Clustering

Standardized three-group k-means gives groups of 94, 347, and 812 areas. Their mean (MCI, CCI) values are (1.9235, 1.4516), (2.7631, 2.2936), and (3.0573, 3.1167). Raw versus standardized partitions have adjusted Rand index 0.805038. The standardized partition is unchanged across tested seeds 1, 17, 534, and 2026 with thirty starts each. Computational stability is separate from validation as a measure of individual service needs.

## Index Construction

Equation S1 gives 6.4765, 4.4847, and 5.0689 for the supplement's illustrative devices. Natural logs of positive minutes, with zero contribution at zero, give 4.4603, 3.0887, and 3.4678, matching the displayed values to two decimals. The equal-device mean of displayed values is 3.673333; the minute-weighted mean is 3.630383. This check does not establish the transform used in the private pipeline.
