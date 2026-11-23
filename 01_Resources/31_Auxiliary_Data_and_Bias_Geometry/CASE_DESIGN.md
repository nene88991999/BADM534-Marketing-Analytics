# Human and Synthetic Evidence for a Product Decision

A body-wash manager is considering a premium feature and two price levels. The decision requires the effect of the feature and customers' price sensitivity. Four profiles cross a standard or premium feature with a low or high price. The following analytic example uses entirely invented means on a purchase-intent scale. It extends the course's [synthetic-consumer discussion](../../03_Data_and_Code/Synthetic_Consumers/README.md); its four profiles form a separate construction from the existing six-concept example.

## A Feature Comparison Can Survive a Price Distortion

Code the feature $f$ and price $p$ as $-1$ and $+1$. Specify primary means as $3+0.4f-0.5p$ and auxiliary means as the primary mean plus $0.8+0.6p$. The observation unit is one rating at one product profile from one source. A two-unit change in a coded attribute gives twice its coefficient as the corresponding rating contrast.

| Price | Feature | Invented Primary Mean | Invented Auxiliary Mean |
|---|---|---:|---:|
| Low | Standard | 3.1 | 3.3 |
| Low | Premium | 3.9 | 4.1 |
| High | Standard | 2.1 | 3.5 |
| High | Premium | 2.9 | 4.3 |

At either price, adding the premium feature increases both sources' ratings by 0.8 points. At either feature level, raising price reduces the primary rating by 1.0 point and increases the auxiliary rating by 0.2 points. The price-sensitive bias cancels in the feature comparison at a fixed price. It remains in the price comparison. Synthetic observations can inform the feature coefficient under these restrictions, while human evidence is required to separate price sensitivity from the auxiliary price bias.

## Compare Cost at the Same Accuracy

Use unit error variances for both sources, a primary-response cost of 1, and an auxiliary-response cost of 0.01. These are imposed quantities. The benchmark optimizes primary-only sampling to estimate all three coefficients with total MSE at most $\epsilon^2$. Apply the paper's §5.3 design to the same four profiles, allowing auxiliary bias in the intercept and price coefficient.

With total primary and auxiliary precision $t$ and $s$, the normalized MSE is $2/t+1/(t+s)$. The intercept and price coefficient each contribute $1/t$; both sources inform the feature coefficient. The closed-form optimum at $\lambda=0.01$ reduces asymptotic cost by approximately 24.29%. Even with arbitrarily inexpensive auxiliary responses, the saving approaches only one third in this symmetric example. That fraction follows from this design and loss; it is not a general rule based on counting coefficients.

For $\epsilon=0.1$, round each source's allocation upward separately within each profile, as in Algorithm 1. The resulting allocation uses 216 primary responses and 1,296 auxiliary responses, costs 228.96 units, and has analytic MSE about 0.009921. The primary-only benchmark uses 300 responses and costs 300, so this rounded allocation saves 23.68%. This calculation implements the theorem's allocation rule; it does not assert that the rounded design is the exact finite-sample integer optimum.

## Add an Omitted Bias Feature

Now add an auxiliary feature bias of $0.3f$ while continuing to estimate the smaller bias model. In the balanced design above, the expected feature-coefficient error is $0.3\times1296/(216+1296)=0.257143$. Its squared bias adds approximately 0.066122 to the total MSE, raising the total to approximately 0.076043. The promised 0.01 accuracy target fails even though the data allocation and computations follow the smaller model correctly.

The class can then include $f$ in the bias dictionary. Every primary feature is now confounded with an unrestricted auxiliary bias coefficient. Theorem 2 implies zero value of auxiliary data for this worst-case coefficient-estimation objective. This comparison distinguishes correct computation from a correct restriction on bias.

## Figures and Course Placement

The first original TikZ figure compares the feature at a fixed low price and price with a fixed standard feature. Primary and auxiliary lines use Illinois navy and orange with distinct markers, on a common vertical scale. The four-profile table and mean functions remain alongside the comparison in M4 §4.24.

The second TikZ figure plots cost savings against the information-cost ratio, marking the one-third limit and the zero-savings threshold at $\lambda=1/3$. It also shows zero value under the expanded bias dictionary. A third figure separates declining sampling variance from persistent squared bias as both source counts increase. All three retain text descriptions and [underlying tables](../../03_Data_and_Code/Auxiliary_Data/results/README.md).

M4 §4.24 contains the allocation and profile comparisons; M7 §7.37 contains omitted-bias sensitivity and human validation. M3 §3.16 explains identification and M6 §6.28 discusses fixed designs. Sessions 4, 5, 9, and 11 use existing meeting blocks, with longer calculations in optional ungraded practice.

## Reproduction

Run [source_checks.py](source_checks.py) using the command in the [resource guide](README.md). It supplies all invented inputs, arithmetic, an exact rank calculation, a numerical comparison for the allocation, and saved results in [source_checks.json](source_checks.json). The [implemented course programs](../../03_Data_and_Code/Auxiliary_Data/README.md) have complete matching listings in M4 and M7. The [verification record](../../03_Data_and_Code/Auxiliary_Data/VERIFICATION.md) distinguishes the independent course checks from the source-review arithmetic.
