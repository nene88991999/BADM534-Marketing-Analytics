# Preserving a Customer-Relevant Signal

## Managerial Decision and Placement

A service team chooses a representation for identifying cases that require review. M7 §7.39 compares reconstruction with routing; §7.40 examines the meaning of a feature decomposition. Session 11 uses ten minutes from its existing demand-interval and complaint-routing block. M4 §4.25, M5 §5.25, and M9 §9.19 connect segmentation, attributed claims, and customer permission.

## Implemented Calculations

The [four original synthetic cases](../../03_Data_and_Code/Representation_Evaluation/DATA_DICTIONARY.md) have two imposed coordinates and equal weights. At style scale 100, A explains 99.990001% of variation and recalls none of the two positive cases. B explains 99.960004% and recalls both. Changing the style scale to 1 reverses the aggregate reconstruction ranking while leaving routing unchanged. The code records component errors, variance weights, and both denominators.

Two imposed pairs of weighted unit directions reconstruct `(2, 0)` exactly. Removing the first contribution gives squared errors of 2 and 5. Their coefficient sums differ, so equal reconstruction is not equal penalized loss. The calculation establishes an algebraic possibility; it does not estimate feature instability or a customer mechanism.

[Two complete programs](../../03_Data_and_Code/Representation_Evaluation/README.md) and six independent tests ran successfully. Full code appears in the notes. No upstream package, model training, or model inference was executed. The eight source-review checks remain a separate record.

## Figures and Practice

One editable diagram compares total FVU with review recall on explicitly labeled scales. Another shows two vector sums and their different removal consequences. Illinois colors, labels, and dashed translated vectors preserve the distinction in grayscale. Text descriptions and saved JSON results accompany the figures.

The [optional ungraded lab](../../07_Labs/Representation_Evaluation/README.md) asks students to derive the equal-error scale, vary the synthetic input, distinguish sparse penalties from reconstruction, and design an independent evaluation for a learned representation. A future interactive wiki can vary the scale while preserving the four cases and fixed review rule. No interactive page or model-training assignment is released.
