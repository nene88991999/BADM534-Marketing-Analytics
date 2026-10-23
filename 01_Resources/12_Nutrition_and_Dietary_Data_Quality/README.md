# Nutrition and Dietary Data Quality

Fourteen sources connect dietary measurement to the recurring mHealth cases. Eleven government resources were downloaded as HTML with searchable text companions. The Banna et al. paper is distributed under CC BY. The Black paper was downloaded into the instructor's Dropbox-only resource folder; the public repository provides its citation and a summary. The original Goldberg paper is cataloged from its abstract, with a source link; its full text was not downloaded. [download_manifest.json](download_manifest.json) records URLs, retrieval date, local files, rights, and hashes where available. IDs N01–N14 belong to the curated `01_Resources/RESOURCE_CATALOG.json` namespace.

## Measurement

| ID | Resource | Analytical Use |
| --- | --- | --- |
| N01 | [NCI Food Records](Measurement/NCI_Food_Records.md) | Determine what a food record measures and how recording burden affects observation. |
| N04 | [NCI Usual Dietary Intake](Measurement/NCI_Usual_Intake.md) | Separate day-to-day variation from long-run intake. A few days do not establish a person's usual diet. |
| N05 | [NCI Energy Adjustment](Measurement/NCI_Energy_Adjustment.md) | Distinguish total energy from composition; define shares and denominators. |
| N06 | [NCI Unbiased Reference Instruments](Measurement/NCI_Reference_Instruments.md) | Explain external validation and the role of recovery biomarkers. |
| N07 | [NCI Day of Week](Measurement/NCI_Day_of_Week.md) | Motivate calendar balance and weekday controls. |
| N08 | [NCI Reactivity](Measurement/NCI_Reactivity.md) | Consider whether recording itself changes food choices. |

## Cleaning and Reliability

| ID | Resource | Analytical Use |
| --- | --- | --- |
| N02 | [NCI Outliers](Data_Quality/NCI_Outliers.md) | Review unusual observations and compare sensitivity analyses rather than equating extremes with errors. |
| N09 | [NCI Food Composition Databases](Data_Quality/NCI_Food_Composition.md) | Require defensible food, portion, and nutrient mappings before interpreting a category as nutrition information. |
| N10 | [CDC NHANES Dietary Analyses](Data_Quality/CDC_NHANES_Dietary_Analyses.md) | Compare food-level and person-day files and understand reliability and survey design. |
| N11 | [CDC NHANES Dietary Codebook](Data_Quality/CDC_NHANES_DR1TOT_L.md) | Read the documented `DR1DRSTZ` reliability codes. No corresponding field exists in mHealth. |

## Energy Plausibility

| ID | Resource | Analytical Use |
| --- | --- | --- |
| N03 | [NCI Misreporting](Energy_Plausibility/NCI_Misreporting.md) | Distinguish reported intake from actual intake and examine the selection introduced by exclusions. |
| N12 | [Banna, McCrory, Fialkowski, and Boushey, Frontiers in Nutrition (2017)](Energy_Plausibility/Banna_McCrory_Fialkowski_Boushey_FrontiersinNutrition2017.pdf) | Compare fixed cutoffs, individualized methods, and their assumptions. [Companion](Energy_Plausibility/Banna_McCrory_Fialkowski_Boushey_FrontiersinNutrition2017.md). |
| N13 | [Black, International Journal of Obesity (2000)](https://doi.org/10.1038/sj.ijo.0801376) | Updated Goldberg equation and Tables 7–8: duration, sample size, activity assumptions, and individual versus group screening. [Companion](Energy_Plausibility/Black_InternationalJournalofObesity2000.md). |
| N14 | [Goldberg, Black, Jebb, Cole, Murgatroyd, Coward, and Prentice, European Journal of Clinical Nutrition (1991)](https://pubmed.ncbi.nlm.nih.gov/1810719/) | Foundational derivation. The coded illustration uses Black's later variance assumptions. |

## Coding Applications

The [nutrition program](../../03_Data_and_Code/mHealth/recurring_examples/nutrition.py) defines an adult positive-energy sample, compares fixed-range, earlier-period percentile, and item/day agreement screens, and reports retained users, days, means, and exclusions. The lecture notes include the complete code in M2, Section 2.11, and compare a regression sensitivity in M3.

The Goldberg calculation is explicitly hypothetical. The records lack validated basal metabolic rate, physical activity, complete assessment days, and a documented physiological sex variable. A supplied goal, perturbed weight, or numeric `Gender` code does not fill those gaps. Sample restrictions answer a stated analysis question; passing a screen does not validate individual health conclusions.

## Source Rights and Extraction

NCI text is used with attribution under its [reuse policy](https://www.cancer.gov/policies/copyright-reuse), and CDC text under its [agency-materials policy](https://www.cdc.gov/other/agencymaterials.html). External works retain their own rights. HTML snapshots retain the source content; text companions omit figures, layout, and interactive elements. Links to live sources provide updates. No agency endorsement is implied.
