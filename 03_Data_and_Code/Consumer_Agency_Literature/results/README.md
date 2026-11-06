# Mechanism Clusters and Their Scope

## Primary Sample

The primary sample contains 48 retrieved papers coded as having possible dual use or a reported choice concern. There are 47 papers in the former category and one in the latter. Each DOI is one observation, with equal weight. The twelve indicators describe mechanisms identified in the preliminary review. They do not measure the magnitude or incidence of harm.

Average-linkage clustering with Jaccard distance selects four clusters from candidates K=2 through K=8 by the maximum silhouette score, 0.272. Names below describe the observed profiles and are assigned after clustering.

| Cluster | Papers | Share of 48 | Profile |
| --- | --- | --- | --- |
| Social Influence | 19 | 39.6% | All 19 have social cues; six also involve emotion or identity. |
| Emotion and Identity | 15 | 31.3% | All 15 have emotion or identity; four also have attention and four personalization. |
| Disclosure, Framing, and Defaults | 8 | 16.7% | Six have opacity/disclosure, four framing/reference, and four defaults/order. |
| Attention, Search, and Control | 6 | 12.5% | Five have attention, two exit/search friction, and two delegation/control. |

**Social influence is the largest cluster in this retrieved and coded subset.** The most common individual indicator is emotion/identity, present in 21 of 48 papers (43.8%), followed by social cues in 19 (39.6%). These answers differ because clusters are mutually exclusive while features overlap. The four rounded cluster percentages sum to 100.1% because of rounding.

## Sensitivity

At K=4, 200 refits on 80% subsamples give adjusted Rand index 10th/50th/90th percentiles of 0.426/0.794/1.000. Switching to Hamming distance gives agreement of 0.485. An imposed change to one feature per paper gives median agreement 0.250. The latter is a stress test, not an estimated coding-error model. These results show meaningful dependence on feature definitions and distance choice.

Adding the purposefully selected abstract-only risk reviews produces 84 papers and selects K=8, the upper edge of the candidate range. Adding protective papers with positive mechanism codes to the retrieved sample produces 60 papers and selects K=6. The broader 84-paper sample's most common indicator is social cues (27/84, 32.1%), followed by emotion/identity (25/84, 29.8%). A boundary optimum and changed ranking warrant additional coding and model comparison before making a general taxonomy claim.

## Missing Evidence

Only 103 of 824 eligible records have retrieved full texts or related earlier versions. Retrieval shares vary by journal. The 144 reviews include 29 papers coded with social cues; 680 eligible records remain unreviewed. Holding the reviewed codes fixed, the share of eligible records eventually receiving that code can range from 29/824 (3.5%) to 709/824 (86.0%) if all unknown labels are respectively zero or one. These bounds concern a review label and do not measure actual commercial agency erosion. They make the unresolved evidence gap explicit.

## Files

`downloaded_risk/`, `all_reviewed_risk/`, and `downloaded_with_protective/` each contain complete assignments, profiles, feature shares, candidate-K scores, and stability draws. `coverage_by_journal.csv` independently reconciles census counts. `summary.json` records the tested runtime and unrounded results. Regenerate with the commands in the [analysis README](../README.md).
