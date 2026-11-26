# Executed Statistical Comparisons

The mHealth tables describe observed May-to-June logging in the fixed 340-user cohort. The mean change is -5.123 pp; paired-user uncertainty gives a standard error of 1.379 pp, a Student interval of [-7.835, -2.411] pp, and p=0.000237. The independent-day comparison reports 0.663 pp and p=1.13e-14. These calculations share the same point estimate and differ in their treatment of dependence.

The store tables are synthetic. For 4,000 experiments at each correlation:

| Within-Store Correlation | Customer-Row Rejections | Store-Mean Rejections |
| ---: | ---: | ---: |
| 0.0 | 208 / 4,000 | 199 / 4,000 |
| 0.1 | 968 / 4,000 | 198 / 4,000 |
| 0.3 | 1,796 / 4,000 | 188 / 4,000 |
| 0.5 | 2,200 / 4,000 | 191 / 4,000 |

The first experiment at correlation 0.3 estimates $4.334 per customer. The customer-row p-value is 0.0287 and the store-mean p-value is 0.3446. Its full customer table is retained, and the dataset was not selected on its significance. Every customer has zero true effect in the simulation.

See the [dictionary](../DATA_DICTIONARY.md) for units, denominators, and interval definitions. No AI model output is included in these results.
