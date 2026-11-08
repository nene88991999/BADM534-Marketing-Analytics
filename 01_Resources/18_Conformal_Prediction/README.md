# Conformal Prediction for Marketing Decisions

Prediction uncertainty affects inventory, customer-service capacity, and the consequences of automated decisions. The most useful course material concerns how a fixed model's errors determine intervals or sets, which population receives the coverage guarantee, and how changes in demand can undermine it.

## Course Applications

| Decision or Question | Concept | Course Location |
| --- | --- | --- |
| How much can next week's store demand differ from its forecast? | Separate training, calibration, and evaluation; finite-sample ranks; coverage and width | M7 §7.24; Session 11 |
| Which stores bear the forecasting errors? | Marginal and within-segment coverage; limited calibration samples | M7 §7.24.2; Session 11; M9 discussion of customer consequences |
| Which department should receive an ambiguous complaint? | Label sets, empty sets, review queues, and conditional routing error | M7 §7.25; Session 11; application to M5 text classification |
| What changes after a promotion or a model revision? | Forecast origins, delayed labels, distribution change, and revalidation | M8 §8.21; Session 13 |
| Does a probability-calibration chart establish interval coverage? | Probability calibration, prediction-set coverage, and confidence intervals answer different questions | M7 §§7.23–7.25; connection to M3 uncertainty |

The [complete notes](../../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md) include two original synthetic cases and every line of their Python programs. [Code, generated records, and verification](../../03_Data_and_Code/Conformal_Prediction/README.md) require only Python's standard library. Two editable TikZ figures compare segment coverage and complaint-routing sets.

## Recommended Sequence

1. Begin with the inventory decision, a fixed forecast, and a definition of the future outcome.
2. Calculate the finite-sample rank by hand, including a sample too small to yield a finite interval.
3. Compare pooled and segment coverage on the same stores, with widths and counts beside the percentages.
4. Construct complaint-label sets and evaluate the selection rule for automatic routing separately.
5. Change demand while keeping forecasts fixed; explain which condition of the original guarantee has changed.

Normalized residuals and conformalized quantile regression are useful extensions when uncertainty varies with features. Jackknife+, adaptive prediction sets, and methods for dependent time series can follow after students understand their distinct conditions. Probability calibration through Venn–Abers is another topic, with a different target from set coverage. No advanced package implementation is included as a tested course exercise in this release.

## AI-Assisted Coding Exercise

Ask an assistant to implement the exact order statistic for a reserved calibration sample, return an infinite threshold when its rank exceeds the sample size, and preserve boundary ties. Test all twenty possible held-out positions among twenty distinct scores before fitting a larger model. Require a separate table of each segment's count, covered outcomes, and average width. Reusing a favorable calibration result to select a model requires fresh calibration data or an appropriate alternative procedure.

For a future interactive wiki, two compact widgets would be useful: changing the calibration sample size and target coverage to expose the infinite-threshold boundary, and changing the population weights on fixed segment coverage rates. Each should retain an accessible table and the underlying Python calculation.

## Source and Review Record

[SOURCE_REVIEW.md](SOURCE_REVIEW.md) records the pinned repository, inspected cells, implementation concerns, and primary checks. [catalog.json](catalog.json) lists all downloaded notebook files, their hashes, and the scope of reading. The local reference copy contains ten notebooks, the README, and the MIT license; it is excluded from Git because saved notebook outputs include large embedded assets. The book text and an NLP chapter notebook are absent from this snapshot. [UPSTREAM_LICENSE.txt](UPSTREAM_LICENSE.txt) preserves the source license. The course examples use original synthetic records and independently written code.
