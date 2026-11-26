# Electricity Lesson Verification

Checked November 26, 2026.

## Calculation and Source Fidelity

The complete embedded Python matches [bill_identity.py](../../03_Data_and_Code/Learning_Design/bill_identity.py). Browser reference values come from the three saved synthetic bill scenarios. Independent JavaScript checks return USD 100, USD 110, and USD 100; they also cover the direction comparison, zero price, and invalid inputs. The [Python verification](../../03_Data_and_Code/Learning_Design/VERIFICATION.md) records the separate calculations.

All 24 distinct HTML asset and link targets resolve against the local course checkout, including in-page anchors. Local HTTP checks return 200 for file destinations. IDs are unique. Notes, source assessments, complete Python, inputs, outputs, the full-size diagram, and editable TikZ remain reachable through relative links.

## Browser Interaction

The final page was checked in the Codex in-app browser at its default desktop size and at a 390 × 844 viewport. The temporary viewport override was reset afterward.

| Check | Observed Result |
| --- | --- |
| Default price 100, usage 1.1, prediction “Rise” | Revealed bill 110 and change +10; agreement feedback |
| Price 125, usage 0.8, prediction “Stay the Same” | Revealed bill 100 and zero change |
| Changed numerical inputs | Prior result hidden and prediction cleared |
| Usage zero | Native validation prevented calculation |
| Incorrect prediction | Feedback asked the learner to revisit price times usage |
| Reset after input and explanation changes | Restored 100 and 1.1; cleared response, prediction, and result |
| Four explanation tabs | Selected panel visible; other panels hidden |
| Keyboard Right, Home, and End | Focus and selected explanation changed together |
| Expandable Python, revised claim, and reasoning criteria | Full content appeared |
| Narrow layout | Stacked controls, readable body text, wrapped tabs, no horizontal page overflow |
| Diagram | Image loaded with alternative text and a full-size link |

The introductory page, controls, result, explanation views, and narrow layout were visually inspected. These checks cover this browser and these viewports; they do not constitute a cross-browser or assistive-technology certification. The static code contains no response submission, model call, analytics, or persistent storage.

## Course Outputs and Deployment

The affected notes, standalone Marketing Dialectics chapter, Sessions 1, 2, 9, and 14, combined slides, and syllabus were rebuilt. New sections, changed slides, neighboring page breaks, and the two diagrams were rendered and visually inspected. The final notes contain 569 pages and 138 editable figures; the combined slides contain 499 pages. The syllabus remains two pages.

This is a local static pilot whose source can be synchronized with the course repository. GitHub Pages has not been enabled and no public lesson URL is claimed. Copying only the pilot folder would omit shared source and figure destinations; preserve the course-relative paths when deploying. No student learning study has been conducted.
