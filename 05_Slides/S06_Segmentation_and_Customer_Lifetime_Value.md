# Segmentation and Customer Lifetime Value

By Nathan Yang

Session 06. M4. 170 minutes.

[PDF](S06_Segmentation_and_Customer_Lifetime_Value.pdf) | [LaTeX](S06_Segmentation_and_Customer_Lifetime_Value.tex) | [Session Plan](SESSION_PLAN.md)

## Learning Objectives

- Define similarity using economically meaningful customer features.
- Evaluate segment stability and future outcomes.
- Calculate lifetime value with consistent timing and distinguish retention concepts.
- Compare clustering cost and final-center consistency with a common evaluation population.

## Related Materials

- [M4 lecture notes](../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md)
- [Runnable small examples](../03_Data_and_Code/Lecture_Examples/session_examples.py)
- [mHealth segments](../03_Data_and_Code/mHealth/recurring_examples/m04.py)
- [Subscription cohort examples](../03_Data_and_Code/GenAI_Demand/README.md)
- [Ethics and regulation](../06_Lecture_Notes/ETHICS_AND_REGULATION.md)
- [Consumer Agency Literature and Clustering](../03_Data_and_Code/Consumer_Agency_Literature/README.md)
- [Clustering Optimization and Sources](../01_Resources/23_Clustering_Optimization/README.md)
- [Optional Clustering Practice](../07_Labs/Clustering_Optimization/README.md)
- [Digital Usage and Customer Access](../03_Data_and_Code/Digital_Usage/README.md)

## Slide 1: Segmentation and Customer Lifetime Value

Marketing Analytics. By Nathan Yang.

## Slide 2: A Retention-Support Decision

- A service team can support only some customers.
- High baseline value and responsiveness to support are separate quantities.
- Segments should correspond to feasible service decisions.

A segment with high predicted value may have little incremental response to outreach. The support decision needs the change in future contribution caused by the action, net of its costs.

Source: M4, Section 4.9, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md

## Slide 3: Customer Features at a Common Date

- Recency is time since the last eligible event.
- Frequency counts events in a fixed window.
- Monetary value uses sales or contribution over that window.

Customers with unequal exposure histories can appear different because of observation time. The feature definition must specify eligibility and whether returns affect sales or transaction counts.

Source: M4, Section 4.5, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md

## Slide 4: K-Means and Similarity

Choose $K$ centers for transformed customer features $z_i$.

$$
\min_{\mu,c}\sum_i\left\|z_i-\mu_{c(i)}\right\|^2
$$

Scaling the features changes the distance and can change the segments.

K-means minimizes within-cluster squared Euclidean distance. A standardized feature receives a different implicit weight from the raw variable. The transformation is a substantive choice.

Source: M4, Section 4.5, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md

## Slide 5: Units Change the Nearest Customer

Synthetic customers have unchanged spending and frequency records.

**Figure description:** Changing spending from dollars to hundreds of dollars reverses which customer is nearest to A. Frequency then receives more relative weight.

[Editable TikZ](../06_Lecture_Notes/figures/M04_scaling.tex)

Compare A=(100,1), B=(110,9), and C=(200,1), then change only the unit used to express spending. The resulting change in distance shows why a numerical representation embeds a weighting of customer attributes. The appropriate weighting depends on the service decision.

Source: M4, Section 4.5, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md

## Slide 6: Evaluating a Segmentation

- Inspect segment size, profile, and actionable differences.
- Compare stability across seeds, samples, and periods.
- Evaluate outcomes that did not mechanically define the clusters.

Within-cluster dispersion declines as K rises. A high-spending cluster will have high spending by construction when spending is an input. Later outcomes provide a more informative descriptive check.

Source: M4, Section 4.6, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md

## Slide 7: Similarity of Positive Mechanisms

For each paper, collect the mechanisms coded as present in a set $A_i$.

$$
d_J(i,j)=1-\frac{|A_i\cap A_j|}{|A_i\cup A_j|}
$$

Jaccard distance ignores shared absences. Average linkage compares these distances.

Compare 48 retrieved papers with potential dual use or a reported choice concern using twelve binary codes, including social cues, emotion, disclosure, defaults, and exit friction. A zero means that a mechanism was not coded from reviewed evidence, so papers with missing reviews are excluded from the comparison. This distinction keeps unreviewed papers from appearing similar merely because evidence has not yet been assessed. M4 §4.17 provides the complete program.

Source: ../03_Data_and_Code/Consumer_Agency_Literature/README.md

## Slide 8: Social Influence is the Largest Cluster

48 retrieved potential-risk reviews. Four clusters selected from K=2 through K=8.

**Figure description:** Social influence contains 19 papers, emotion and identity 15, disclosure/framing/defaults eight, and attention/search/control six. The horizontal scale runs from zero to the full sample of 48.

[Editable TikZ](../06_Lecture_Notes/figures/M04_agency_clusters.tex)

The largest cluster contains 39.6% of the sample. Emotion/identity is the most common overlapping feature at 21 of 48, so feature and cluster rankings differ. Almost all papers in this analysis are coded for inferred dual use. Counts do not measure market prevalence or author intent.

Source: ../03_Data_and_Code/Consumer_Agency_Literature/README.md

## Slide 9: Reproduce the Mechanism Grouping

Run from the Consumer_Agency_Literature folder after installing its requirements.

```python
import pandas as pd
from cluster import FEATURES, select_sample, partition
df = pd.read_csv("coded_papers.csv")
sample = select_sample(df, "downloaded_risk")
labels, distances = partition(sample[FEATURES].to_numpy(), 4)
assert len(sample) == 48
```

The complete script compares K values, exports profiles, and refits sensitivity samples.

The short snippet reproduces the selected four-cluster partition. The full cluster.py program in M4 Section 4.17 selects K using silhouette scores and checks aggregate counts. Stable paper identifiers preserve traceability to original summaries.

Source: ../03_Data_and_Code/Consumer_Agency_Literature/README.md

## Slide 10: The Coding Changes the Conclusion

- Median subsample agreement: adjusted Rand index 0.794.
- Changing one feature per paper lowers median agreement to 0.250.
- The broader abstract-based sample selects eight clusters.

Subsamples contain 80% of the primary papers and hold K=4 fixed across 200 repetitions. One-bit changes are an imposed sensitivity exercise, retaining a positive feature per paper. These are conditional stability results, not confidence intervals for population harm. The broader 84-paper risk sample is purposefully selected and chooses the upper K boundary.

Source: ../03_Data_and_Code/Consumer_Agency_Literature/README.md

## Slide 11: mHealth Segments Use Earlier Histories

Eligible users have at least 30 observed days before July 1.

**Figure description:** Earlier logging frequency and recorded breadth distinguish clusters. Later logging does not enter the clustering inputs.

[Editable TikZ](../06_Lecture_Notes/figures/M04_mhealth_segments.tex)

The representation uses first-half logging fraction, mean category breadth, and mean calorie-share variety. K=3 is imposed for the comparison. The scaler and centers use only the earlier window.

Source: M4, Section 4.11, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md

## Slide 12: Later Logging by Earlier Segment

| Segment | Users | Prior Fraction | Later Fraction |
| --- | --- | --- | --- |
| 1 | 126 | 0.426 | 0.338 |
| 2 | 90 | 0.759 | 0.594 |
| 3 | 115 | 0.870 | 0.654 |

mHealth denominators use 182 earlier and 184 later calendar days.

Later absence contributes zero observed days for eligible users. The figures describe persistence in recorded activity. They are not contractual retention rates or effects of a service intervention.

Source: M4, Section 4.11, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md

## Slide 13: Lifetime Value and Payment Timing

Value future contribution conditional on remaining active.

$$
\operatorname{CLV}=\sum_{t=1}^{T}\frac{\Pr(\text{active at }t)m_t}{(1+d)^t}-a
$$

The period for margin $m_t$, discounting $d$, and retention must agree.

The acquisition cost a occurs at time zero. This convention excludes immediate contribution. If a current-period contribution is included, it must be added explicitly.

Source: M4, Section 4.7, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md

## Slide 14: A Stationary Subscription

Suppose monthly retention is $r$ and monthly contribution is $m$.

$$
\operatorname{CLV}=\frac{mr}{1+d-r}-a
$$

With $m=60$, $d=0.01$, $a=50$, and $r=0.80$, CLV is 178.57 dollars.

The formula assumes constant retention and conditional margin and an infinite horizon, with the first payment one month later. It follows from a convergent geometric series.

Source: M4, Section 4.7, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md

## Slide 15: Retention Has Nonlinear Value

Synthetic stationary model. Monthly margin, discounting, and acquisition cost stay fixed.

**Figure description:** CLV rises increasingly rapidly with retention. Increasing monthly retention from 0.80 to 0.90 raises value from about 178.57 to 440.91 dollars.

[Editable TikZ](../06_Lecture_Notes/figures/M04_clv.tex)

The high-retention region places more weight on distant contributions. Uncertainty about the persistence of retention and margins can dominate the valuation.

Source: M4, Section 4.7, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md

## Slide 16: A Finite-Sum Check

Compare the closed form with 2,000 future monthly payments.

```python
m, r, d, a = 60, 0.8, 0.01, 50
closed = m * r / (1 + d - r) - a
finite = sum(m * r**t / (1+d)**t
             for t in range(1, 2001)) - a
assert abs(closed - finite) < 1e-8
```

Both calculations give approximately 178.57 dollars.

Matching the two expressions checks the payment convention and arithmetic. It does not establish constant retention as a valid model of a real relationship.

Source: M4, Section 4.7, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md

## Slide 17: Cancellation and a Logging Gap

- A subscription may record cancellation directly.
- A 30-day logging gap is an operational activity event.
- Observation can end before a defined event occurs.

Right censoring preserves the distinction between no observed event by the end of follow-up and an event at the last observation. A logging gap is not proof of permanent departure or paid cancellation.

Source: M4, Section 4.13, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md

## Slide 18: The Event Definition Changes Survival

mHealth time-to-gap analysis uses a stated gap definition and observation horizon.

**Figure description:** Survival tracks time until a defined logging gap. The risk set and right censoring determine which histories contribute at each time.

[Editable TikZ](../06_Lecture_Notes/figures/M04_logging_survival.tex)

Changing the gap length changes the event being measured. Survival of recorded activity should remain separate from contractual renewal in financial calculations.

Source: M4, Section 4.13, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md

## Slide 19: Endpoint and Continuous Retention

- Endpoint retention allows customers to leave and return.
- Continuous retention requires uninterrupted presence.
- Acquisition can include first entry, return, or switching.

A starting-provider cohort is fixed at the initial period. The same-provider, other-provider-only, and no-paid-provider states distinguish platform retention from category participation. Multiple providers require explicit overlap handling.

Source: M4, Section 4.14, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md

## Slide 20: Coding Exercise: Segments and Value

- Fit feature scaling and segments on an earlier period.
- Describe a later period without refitting the groups.
- Vary assumed paid retention in a separate CLV calculation.

The small CLV calculation is session_examples.py in the Lecture Examples folder S06. The real mHealth m04.py example and GenAI cohort program keep behavioral measurements separate from imposed financial inputs.

Source: M4, Section 4.11, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md

## Slide 21: Cluster Mass Changes the Update

Earlier count 10, mean 2; current count 2, mean 7. Weight each batch by one-half.

$$
\mu_{\mathrm{new}}=\frac{0.5(10)(2)+0.5(2)(7)}{0.5(10)+0.5(2)}=\frac{17}{6}
$$

Weighting the two means equally would give 4.5. e-means carries sums and counts.

In the synthetic scalar example, weighted mass determines how much each batch contributes to the updated cluster center. The complete e-means algorithm adds a cooling schedule and rules for unused clusters, so this calculation isolates one part of its operation. Batch order in shuffled static data also differs from calendar recency. Choosing a useful customer intervention requires a link from the resulting groups to customer outcomes beyond the fixed squared-distance objective.

Source: M4, Section 4.18. ../03_Data_and_Code/Clustering_Optimization/README.md https://arxiv.org/abs/2611.09501v1

## Slide 22: Final Centers Can Change Customer Labels

Recompute assignments before forming segment profiles.

**Figure description:** Four fixed scalar points are 0, 4, 5, and 10. Final centers 2 and 7.5 imply a boundary at 4.75. Point 5 changes from a blue circle in group A to an orange square in group B. With one of four labels changed, mean squared distance falls from 5.8125 to 5.125.

[Editable TikZ](../06_Lecture_Notes/figures/M04_centroid_assignments.tex)

Saved labels can reflect earlier center locations. The constructed comparison holds all points and final centers fixed. Faiss e-means returns training-pass labels; a new assignment is necessary for a profile consistent with final centers. The exact fractions and denominator are reproduced by centroid_checks.py.

Source: M4, Section 4.19. ../03_Data_and_Code/Clustering_Optimization/README.md

## Slide 23: Lower Error Has a Computational Cost

Common data, initial centers, and final scorer; method-specific budget caps.

**Figure description:** Median fitting milliseconds on the horizontal axis and held-out mean squared distance on the vertical axis compare Lloyd, MiniBatch, and CPU e-means. Points summarize three seeds for caps 2, 5, and 10. e-means attains lower error and takes longer than Lloyd at each corresponding cap. Shared final evaluation time is reported separately in the notes.

[Editable TikZ](../06_Lecture_Notes/figures/M04_clustering_cost.tex)

The reference run uses 50,000 training and 10,000 test vectors, 32 coordinates, 64 centers, one numerical thread, and training-only scaling. Caps denote different iterations or epochs and do not imply equal arithmetic work. Scikit-learn 1.6.1 and Faiss 1.16.0 supply the implementations. Times are short, machine-specific measurements. This is an original synthetic CPU comparison; no published GPU speedup is reproduced.

Source: M4, Section 4.20. ../03_Data_and_Code/Clustering_Optimization/README.md

## Slide 24: From Numerical Groups to Marketing Actions

- Check final labels, feature scale, and stability across initializations.
- Compare the time needed for fitting and final assignments.
- Justify the action using later outcomes, causal evidence, and customer choice.

At cap 2, the median e-means saved-label discrepancy is 9.408% of 50,000 valid training labels. The common evaluation costs more than fitting in the recorded runs. mHealth uses three earlier-window features and three centers, with later logging for descriptive interpretation. Faster fitting or smaller dispersion does not establish an effect of support. Jaccard mechanism clustering and affiliation communities use different objectives. o-means is optional large-K GPU reading and was not run.

Source: ../03_Data_and_Code/Clustering_Optimization/README.md

## Slide 25: Retention and Effective Cancellation

- High paid retention can reflect satisfaction or difficulty leaving.
- Measure cancellation completion and unwanted subsequent charges.
- Evaluate customer value alongside the seller's lifetime-value objective.

A customer who prefers cancellation can remain subscribed because of friction. The consumer-value comparison requires independent evidence about that preference and the available procedure.

Source: M8, Section 8.14, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M08_Current_Topics_and_Integrated_Decisions.md

## Slide 26: Geographic Usage Groups

Raw and standardized distances produce different geographic groups.

**Figure description:** Illinois groups contain 94, 347, and 812 areas. The adjusted Rand index comparing raw and standardized clustering is 0.805.

[Editable TikZ](../06_Lecture_Notes/figures/M04_digital_clusters.tex)

The three groups are a fixed descriptive example. Thirty random starts and four tested seeds yield the same standardized partition. Raw distances give more influence to the index with larger spread. Group names order mean MCI and carry no ranking of customer ability or value.

Source: (Pereira et al., 2026); original course calculations. ../01_Resources/38_Digital_Usage_and_Inclusion/README.md

## Slide 27: Stable Groups Still Need Outcome Validation

- Raw versus standardized partitions: adjusted Rand index 0.805.
- Tested seed changes leave the standardized partition unchanged.
- Observe requested assistance and task completion before allocating service.

Adjusted Rand agreement compares co-membership and is not a percentage of identical labels. Seed stability checks a computation under chosen features. Scaling changes the meaning of similarity. The public data contain no individual assistance need or service outcome, so no cluster is validated as a customer capability category.

Source: (Pereira et al., 2026); original course calculations. ../01_Resources/38_Digital_Usage_and_Inclusion/README.md

## Slide 28: Retention Discussion

- What action differs across the proposed segments?
- Does a customer's absence represent churn or censoring?
- Which retention assumption changes the support decision?

A useful recommendation identifies the response to intervention as well as baseline value. Cluster membership alone does not establish the effectiveness of differentiated support.

Source: M4, Section 4.9, Marketing Analytics Lecture Notes. ../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md
