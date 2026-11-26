# Digital Service, Geographic Evidence, and Customer Choice

A retailer plans to offer booking, discounts, and cancellation through an app. It wants to identify where assistance may help customers. Use the [released data and full programs](../../03_Data_and_Code/Digital_Usage/README.md) to assess which conclusions the geographic evidence supports. This exercise is public optional ungraded practice.

## 1. Define the Decision and Observation Unit

State the service decision, the customer task, and the information available before the firm acts. Distinguish a Windows device-month, a postal identifier, a Census area, and a customer. Explain why app-category minutes do not directly measure the ability to complete a cancellation request.

## 2. Assess the Release and Construct the Join

Run `assess_release.py`. Reconcile the raw count, restored leading zeros, matched identifiers, and regression eligibility using `assessment.json`. Inspect 01001, 60601, and 61801 as strings. Explain why the 50 open-ended income values remain in the released roster while leaving the common income-regression sample. Check that the education and broadband shares use different denominators.

Ask an AI assistant to suggest a join and then inspect its keys, cardinality assertion, unmatched-record handling, and income-code treatment. Verify one record against the archived source CSVs without relying on the assistant's explanation.

## 3. Evaluate the Geographic Display

Use `illinois_map.csv` and the two M2 maps. Compare MCI and CCI for one named area in original and standardized units. Explain what equal area weights and common z-score intervals hold fixed. Explain why a dense collection of points is not a count of residents, why the point is not a device location, and what a boundary or population-weighted display would change.

## 4. Compare Regressions on One Sample

Run `compare_models.py`. Reproduce the positive simple CCI slope and negative adjusted slope. Explain the comparison defined by education, broadband, and state intercepts. Compare the household-weight sensitivity with the equal-area projection. Give a concrete causal question about an assistance offer and identify the evidence this geographic regression lacks for answering it.

## 5. Compare Geographic Groupings

Run `cluster_usage.py`. Verify that group counts sum to the Illinois roster and inspect original-unit group means. Explain the adjusted Rand index and the difference between scaling sensitivity and seed sensitivity. For an extension, compare k=2, 3, and 4 in a copy of the script; label this a new analysis and record outputs. Specify a held-out customer outcome before describing one grouping as more useful for service allocation.

## 6. Reproduce a Published Numerical Example

Run `verify_index.py`. Calculate one device score independently from the printed minutes and weights. Identify the log convention that matches displayed rounding, the convention stated in Equation S1, and the conclusion that remains unresolved. Reproduce the equal-device and minute-weighted means. Explain how a change in activity weights can change an area's score while each device's score remains fixed.

## 7. Justify the Marketing Practice

Compare an optional assistance offer with mandatory app completion for access to a benefit. Specify consent, customer-requested outcomes, correction of geographic classifications, usable alternatives, and failure costs. Apply the Kantian distinction between evidence and the additional premise authorizing a decision. Apply the Confucian concern with humane conduct and role responsibilities. Propose an assistance evaluation with an explicit eligible-customer denominator, assignment rule, outcomes, and observation period. Keep this proposed study separate from the executed geographic analyses.
