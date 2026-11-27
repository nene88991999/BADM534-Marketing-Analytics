# HBS Reassurance and Research Responsibility

Checked November 27, 2026. This review compares public wording with the unchanged 42-page paper and the course's previously verified reported-table calculations.

## Source Locations

The [HBS article](https://www.library.hbs.edu/working-knowledge/blaming-data-centers-for-higher-electric-bills-its-not-that-simple) was read directly (Kost, 2026). Relevant locations are its opening, the third findings bullet under the section about who pays, and its later discussion of possible future price changes. M8 §8.31 quotes two short clauses and preserves the article's positive overall finding and future qualification. The categorical subgroup assurance remains the object of criticism.

The [paper](RanaKapsNetessine_WorkingPaper2026.pdf) was checked at the abstract, page 3, Table 2 on page 23, and Table 4 and its accompanying interpretation on page 26 (Rana et al., 2026). A text search through the full source located the residual attribution on page 3 and the descriptive inflation adjustment in Appendix A.4. The course distinguishes the paper's own interpretations from wording authored by the HBS publication.

## Supported Findings

- The four-owner estimate is 0.158 with utility-clustered SE 0.160 in USD/MWh per capacity-exposure percentage point. The fixed-normal 95% interval is [-0.156, 0.472]; its one-sided 95% upper bound is 0.421. These are rounded displays of the previously verified calculations.
- The price comparisons retained in the notes leave the specified positive margins unresolved. They do not establish a categorical absence of an increase.
- The direct developer-equality test has reported p=0.101. This exceeds the table's p<0.10 convention, although the accompanying text describes it as marginally significant.
- The 4% share uses observed historical price growth as its denominator. It does not specify an acceptable household burden or identify household incidence.
- Subtracting that share gives a residual. The subtraction does not identify the named inflation, fuel, and grid-investment contributions asserted on page 3.

The paper contains positive overall findings and more qualified detection language for the subgroup. The criticism targets its unsupported interpretations and the public categorical cost denial. No new utility-panel estimation or power calculation was performed for this writing revision. The six price comparisons, three imposed bias scenarios, and their code remain unchanged.

## Normative Argument and Scope

M9 §9.83 makes the principle explicit: consequential assurances should be supported by reasons addressing the people exposed. A bounded, accurate statement is feasible. Under that principle, publishing unsupported categorical reassurance is ethically objectionable and warrants correction. The demonstrated inferential defect does not depend on proving a realized household loss.

Intentional deception, editorial control by a particular researcher, coordinated corporate dissemination, actual policy reliance, and a specific injury caused by the article are separate claims requiring additional evidence. The course makes no such finding. The [communication guide](PUBLIC_COMMUNICATION_AND_PUBLICATION.md) separates the documented errors, the normative premise, and the proposed correction.

## Course Integration

The revised material appears in M6 §6.49, M8 §§8.31–8.31.1, M9 §9.83, and five existing Session 14 slides (54, 61, 69, 128, and 129). The optional communication exercise and repository context use the same claim distinctions. No meetings, grading rules, or numerical examples were added.

## Build and Verification

The revised full notes and standalone chapter compiled to 679 and 142 pages. Session 14 remains 130 slides and the combined deck remains 575 slides. All 135 Python listings match their source files. The calculation inputs and saved results are unchanged. Visual review covered 26 pages: full-notes pages 10, 13, 379–382, 534–536, and 678–679; standalone chapter pages 141–142; and Session 14 slides 53–55, 60–62, 68–70, and 127–130. No clipping or overlap appeared in the final renders. Artifact hashes are recorded in the [slide verification file](../../05_Slides/verification.json).
