# Data and Sample Code

Course datasets, data dictionaries, scripts, notebook examples, and code snippets for BADM 534. Keep each example's data and code together in a subfolder organized by module or topic.

**Status:** [synthetic lecture examples](Lecture_Examples/README.md) now cover the numerical cases in all eight modules, with verified Python calculations and small CSV files. Candidate datasets are in the [resource library's dataset guide](../01_Resources/10_Datasets_and_Project_Resources/Dataset_Guide/README.md) and [additional dataset collection](../01_Resources/20_Datasets/README.md).

The [mHealth food-log collection](mHealth/README.md) provides actual 2016 food entries and daily summaries with replacement user IDs, fixed ages, and perturbed weights. Its GitHub release contains the full compressed teaching files. The data dictionary, checksum-verified downloader, and agent guide are in the course folder. Read the transformation and sampling notes before analysis.

## Adding an Example

Use a descriptive module prefix, such as `M02_Customer_Summary`, and include a README explaining the marketing question, files, dependencies, run command, expected output, and a simple check of the result. Record whether the example has been executed successfully.

Place the related scripts or notebooks, data files, and data dictionary in the example's folder. Use relative data paths. For larger examples, use `data/` and `code/` subfolders. If several examples share a dataset, link to a single documented copy.

## Documenting Data

Record the source, retrieval date/version, license, observation unit, time range, units, missing-value codes, exclusions, and processing steps. Preserve original and derived data separately. Label synthetic data explicitly, and retain attribution and licenses for adapted data and code.

Keep identifiable student records and restricted research data outside this repository.

## Guidance for Students and Agents

Read the root [agent guide](../AGENTS.md) before adapting an example. Explain the purpose of the code and its analytical assumptions, inspect the inputs and data dictionary, and verify the output with a small example. Identify any changes made with AI assistance. Follow the relevant assignment's rules when using sample code in assessed work.

The [labs folder](../07_Labs/README.md) contains the structure for complete guided exercises. The [resource library](../01_Resources/README.md) contains downloaded reference code and notebooks.

## Recurring mHealth Cases

The [eight-module examples](mHealth/recurring_examples/README.md) include complete Python, aggregate outputs, a data-quality audit, nutrition-screening sensitivity, and meaningful counterexample checks. The same code is embedded in the lecture notes.

Additional executed examples cover fixed-cohort reporting, recency/frequency, logging-gap survival, text topics, CUPED, basket associations, and checks on generated numerical claims. A separate synthetic price-instrument simulation illustrates endogeneity and exclusion. See the [resource-to-example map](../06_Lecture_Notes/RESOURCE_INTEGRATION.md) for source attribution, module sections, and the distinction between executed course code and downloaded reference notebooks.
