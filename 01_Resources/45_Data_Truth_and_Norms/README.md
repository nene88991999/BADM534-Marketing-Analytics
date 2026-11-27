# Data, Truth, and Norms

A household needs evidence about the burdens of a proposed development. A utility, developer, regulator, and researcher may each produce records for different purposes. The relevant question is how those records become evidence for the household's decision, and which further reasons justify an institution's recommendation.

The collection contains 26 sources: 18 philosophical and methodological readings and eight institutional sources. Fourteen source files are saved locally in categorized `readings/` subfolders: 12 PDFs and two author manuscripts in Word formats. Public guides and original teaching materials are synchronized with GitHub; the source originals remain in Dropbox. The [catalog](catalog.json) records URLs, versions, inspected passages, availability, and local-copy checksums. Access to an original does not establish a general right to redistribute it.

## Reading Routes

| Question | Readings | Course Application |
| --- | --- | --- |
| What kind of object is a dataset? | [Artifacts and representation](01_Artifacts/README.md): origins, identity, evidence, and institutional categories | M2 §2.30; M9 §9.51 |
| What connects a record, a true claim, and a justified action? | [Truth and norms](02_Truth_and_Norms/README.md): truth conditions, norms, error, and criticism | M9 §9.52 |
| Why are some questions easier to answer than others? | [Institutions and ignorance](03_Institutions_and_Ignorance/README.md): research priorities, strategic ignorance, and classification | M9 §9.53 |
| Which household electricity evidence actually exists? | [Electricity evidence](04_Electricity_Evidence/README.md): EIA, DOE, Virginia, Senate documents, company correspondence | M6 §6.43; M9 §§9.53–9.54 |

Begin with T01 (Thomasson, 1999), T05 (Leonelli, 2015), T08 (Douglas, 2000), T09 (Longino, 2004), T15 (Frickel et al., 2010), and EIA E01–E03. The recommended sequence is background reading, with no new graded requirement. T07 (Gitelman and Jackson, 2013) is an unavailable full-text lead; T13 (McGoey, 2012) and T14 (Steel, 2010) are abstract-based entries. Their inspection limits are explicit in the catalog.

## The Argument

Data have histories of creation, classification, retention, linkage, and access. Institutional purposes influence those histories. They can improve accuracy, exclude relevant cases, or constrain reuse. Establishing that a record was institutionally produced therefore begins an inquiry into its evidential role; it does not refute its contents.

An account of created, dependent artifacts (Thomasson, 1999) provides an analogy for provenance and identity. A dataset version, a copy of that version, and the persons it represents are distinct. Some recorded facts, including legally owed charges, partly depend on institutional rules. Other claims concern physical events or causal relationships. A rule's existence, a proposition's truth, the warrant for asserting it, and the permissibility of acting on it require distinct arguments.

The electricity case supplies a consequential correction: household billing data have already been collected, and household expenditure microdata are public. The difficult object is an adequately linked and accessible body of evidence for project-level household cost incidence, including canceled proposals, cost recovery, offsets, and counterfactual outcomes. Political sensitivity can encourage restricted access and also disclosure or public investigation. Permanent unavailability and deliberate suppression require evidence beyond controversy itself.

## Teaching Materials

- [Evidence assessment](ELECTRICITY_ASSESSMENT.md): verified facts, disputed inferences, and a feasible research design.
- [Complete Python example](../../03_Data_and_Code/Data_Production/README.md): identical public releases with opposite population effects, selection weighting, and support bounds.
- [Optional ungraded practice](../../07_Labs/Data_Truth_and_Norms/README.md): premises, counterexamples, access, and reasons owed to affected households.
- [M2](../../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md) §§2.30–2.31, [M6](../../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md) §6.43, and [M9](../../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md) §§9.51–9.54.

The original figures and code do not replicate the data-center paper or estimate actual household harms. They identify premises that a broader reassurance would need to establish. They connect to the existing [project-exposure assessment](../44_Bad_Controls_and_Project_Exposure/CASE_ASSESSMENT.md), [institutional assessment](../41_Statistical_Claims_and_Decisions/INSTITUTIONAL_ASSESSMENT.md), and [utility cost-recovery evidence](../../03_Data_and_Code/Utility_Cost_Recovery/README.md).
