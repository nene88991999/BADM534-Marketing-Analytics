# Marketing Analytics Lectures

By Nathan Yang

Fifteen session decks cover all eight modules, with AI-assisted coding, recurring data cases, ethics, and regulation. Each meeting has a proposed 170-minute plan. The sequence has 13 instructional meetings and two provisional presentation meetings, with no guest speakers. The [Spring 2027 syllabus](../02_Syllabus/Marketing_Analytics_Syllabus.md) and dated session plan are available; assessment policies remain pending.

Read the [combined deck](Marketing_Analytics_Lectures.pdf), the [session plan](SESSION_PLAN.md), or a session below. Each PDF has editable LaTeX and a complete Markdown companion with projected text, code, equations, figure descriptions, and substantive presenter notes.

## Session Decks

| Session | Topic | PDF | Markdown | LaTeX |
| --- | --- | --- | --- | --- |
| 01 | Marketing Decisions and AI-Assisted Coding | [Slides](S01_Marketing_Decisions_and_AI_Coding.pdf) | [Companion](S01_Marketing_Decisions_and_AI_Coding.md) | [Source](S01_Marketing_Decisions_and_AI_Coding.tex) |
| 02 | Customer Data and Measurement | [Slides](S02_Customer_Data_and_Measurement.pdf) | [Companion](S02_Customer_Data_and_Measurement.md) | [Source](S02_Customer_Data_and_Measurement.tex) |
| 03 | Visualization and Data Quality | [Slides](S03_Visualization_and_Data_Quality.pdf) | [Companion](S03_Visualization_and_Data_Quality.md) | [Source](S03_Visualization_and_Data_Quality.tex) |
| 04 | Regression and Marketing Interpretation | [Slides](S04_Regression_and_Marketing_Interpretation.pdf) | [Companion](S04_Regression_and_Marketing_Interpretation.md) | [Source](S04_Regression_and_Marketing_Interpretation.tex) |
| 05 | Conjoint and Product Design | [Slides](S05_Conjoint_and_Product_Design.pdf) | [Companion](S05_Conjoint_and_Product_Design.md) | [Source](S05_Conjoint_and_Product_Design.tex) |
| 06 | Segmentation and Customer Lifetime Value | [Slides](S06_Segmentation_and_Customer_Lifetime_Value.pdf) | [Companion](S06_Segmentation_and_Customer_Lifetime_Value.md) | [Source](S06_Segmentation_and_Customer_Lifetime_Value.tex) |
| 07 | Text, Social Media, and Networks | [Slides](S07_Text_Social_Media_and_Networks.pdf) | [Companion](S07_Text_Social_Media_and_Networks.md) | [Source](S07_Text_Social_Media_and_Networks.tex) |
| 08 | Project Evidence and Midterm Presentations | [Slides](S08_Project_Evidence_and_Midterm_Presentations.pdf) | [Companion](S08_Project_Evidence_and_Midterm_Presentations.md) | [Source](S08_Project_Evidence_and_Midterm_Presentations.tex) |
| 09 | Experiments and Incremental Value | [Slides](S09_Experiments_and_Incremental_Value.pdf) | [Companion](S09_Experiments_and_Incremental_Value.md) | [Source](S09_Experiments_and_Incremental_Value.tex) |
| 10 | Causal Comparisons and Policy Evaluation | [Slides](S10_Causal_Comparisons_and_Policy_Evaluation.pdf) | [Companion](S10_Causal_Comparisons_and_Policy_Evaluation.md) | [Source](S10_Causal_Comparisons_and_Policy_Evaluation.tex) |
| 11 | Prediction, Validation, and Marketing Actions | [Slides](S11_Prediction_Validation_and_Marketing_Actions.pdf) | [Companion](S11_Prediction_Validation_and_Marketing_Actions.md) | [Source](S11_Prediction_Validation_and_Marketing_Actions.tex) |
| 12 | Recommendation Systems and Customer Goals | [Slides](S12_Recommendation_Systems_and_Customer_Goals.pdf) | [Companion](S12_Recommendation_Systems_and_Customer_Goals.md) | [Source](S12_Recommendation_Systems_and_Customer_Goals.tex) |
| 13 | Adaptive Recommendations and Marketing Budgets | [Slides](S13_Adaptive_Recommendations_and_Marketing_Budgets.pdf) | [Companion](S13_Adaptive_Recommendations_and_Marketing_Budgets.md) | [Source](S13_Adaptive_Recommendations_and_Marketing_Budgets.tex) |
| 14 | Generative AI, Consumer Choice, and Regulation | [Slides](S14_Generative_AI_Consumer_Choice_and_Regulation.pdf) | [Companion](S14_Generative_AI_Consumer_Choice_and_Regulation.md) | [Source](S14_Generative_AI_Consumer_Choice_and_Regulation.tex) |
| 15 | Integrated Decisions and Final Presentations | [Slides](S15_Integrated_Decisions_and_Final_Presentations.pdf) | [Companion](S15_Integrated_Decisions_and_Final_Presentations.md) | [Source](S15_Integrated_Decisions_and_Final_Presentations.tex) |

## Related Materials

- [Full lecture notes](../06_Lecture_Notes/README.md), including complete code for empirical examples.
- [Small runnable session calculations](../03_Data_and_Code/Lecture_Examples/session_examples.py) and [executed results](../03_Data_and_Code/Lecture_Examples/session_calculations.json).
- [Retention-procedure calculation](../03_Data_and_Code/Lecture_Examples/retention_welfare.py), with an aggregate table and fixed-stakes interpretation.
- [Ethics and regulation](../06_Lecture_Notes/ETHICS_AND_REGULATION.md), including module connections and primary-source status.

## Format and Editing

The decks use the supplied 16:9 Beamer format with parchment backgrounds, Illinois colors, editable TikZ, and Chinese ink-and-color artwork. [Art direction](ART_DIRECTION.md) records the brushwork research and visual conventions. [Artwork provenance](assets/PROVENANCE.md) identifies the four generated illustrations and their prompts.

Edit [source/sessions.json](source/sessions.json) and [theme.tex](theme.tex), then use [the build commands](BUILD.md) to refresh LaTeX, Markdown, and PDF together. Follow [AGENTS.md](AGENTS.md) when revising content or using these materials with an assistant.

Markdown companions identify the session and module, learning objectives, slide-number anchors, chart descriptions, definitions, equations, and referenced resources. Record the version in `session_plan.json`; identify omissions when preparing a shorter summary and link related labs when available.

## Earnings-Call Worked Example

Sessions 02, 07, 10, and 14 now use the [earnings-call case](../03_Data_and_Code/Earnings_Calls/README.md). The case covers missing documents, selected denominators, role-specific word exposure, interpretation of pricing language, event-window comparisons, and regulatory evidence. Session 07 uses its worked-comparison and Python blocks for this case; the meeting remains 170 minutes. The four analysis programs and nine tests ran successfully. Complete code appears in the module notes.

## AI Workflow Evaluation and Economics

Sessions 01, 05, 07, 09, 11, and 14 connect failure diagnosis, customer alternatives, prompt revision, factorial comparisons, selection on development accuracy, and reuse economics. The [three complete programs](../03_Data_and_Code/AI_Workflows/README.md) use synthetic inputs and require no model account. Four new TikZ figures show interaction, selection, break-even workload, and price bounds. These additions fit the existing session blocks, with the 75-minute ethics and regulation block in Session 14 retained.

## Consumer Agency and Research Networks

Sessions 3, 6, 7, 9, 12, and 14 add evidence coverage, mechanism clustering, LLM coding, university affiliation communities, downstream customer outcomes, recommendation welfare, and cancellation-policy distinctions. The [complete programs and outputs](../03_Data_and_Code/Consumer_Agency_Literature/README.md) accompany the notes. Four editable TikZ figures retain explicit populations and denominators. The 15-session schedule and the 75-minute regulation block in Session 14 remain in place.

## Changing AI Evidence

Sessions 01, 03, 07, 11, and 14 incorporate versioned claims, censored follow-up, changing AI judges, paired regressions, and residual risk. The [source guide](../01_Resources/14_LLM_Evidence_and_Revalidation/README.md) and [three complete programs](../03_Data_and_Code/LLM_Revalidation/README.md) preserve versions, units, and evidence scope. Three editable TikZ figures distinguish published descriptive results from constructed comparisons. Existing meeting durations and the Session 14 regulation block are retained.
