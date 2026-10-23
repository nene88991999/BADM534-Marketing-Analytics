# Lecture Notes

**By Nathan Yang. Updated October 23, 2026.** These notes cover all eight topic families in the supplied Spring 2026 sample syllabus and integrate AI-assisted coding throughout. The revised syllabus, schedule, assessment rules, and course-wide AI policy remain pending.

Read the [complete PDF](BADM534_Lecture_Notes.pdf), or open a Markdown module below. The notes contain 38 original TikZ figures, recurring mHealth cases across M1–M8, worked synthetic cases, complete Python programs, practice questions, and source links. Markdown files provide searchable text and figure descriptions for students and LLMs. The PDF contains vector figures; the Markdown pages display PNG previews generated from the same TikZ sources.

## Modules and Syllabus Coverage

| Module | Notes and Core Coverage | Cases and Figures |
| --- | --- | --- |
| M1 | [Marketing Decisions, Data, and AI-Assisted Python](modules/M01_Marketing_Analytics_and_Python.md): analytical questions, observation units, joins, Python objects and functions, reproducibility, verification | Renewal response versus incremental value; duplicate-key joins; order value; coupon-campaign specification |
| M2 | [Customer Data, Measurement, and Visualization](modules/M02_Customer_Data_and_Visualization.md): customer tables, missingness, denominators, cohorts, charts, uncertainty, Pyramid Principle | Campaign-mix reversal; retention triangle; online grocery baskets and repeated purchases; variety and concentration |
| M3 | [Regression, Interpretation, and Marketing Decisions](modules/M03_Regression.md): OLS, controls, omitted variables, transformations, interactions, inference, diagnostics, panels | Rival presence and market demand; message effects by tenure; advertising contribution |
| M4 | [Product Preferences, Customer Segments, and Lifetime Value](modules/M04_Conjoint_Segmentation_and_CLV.md): conjoint design, logit, willingness to pay, substitution, clustering, scaling, CLV | Bundle cannibalization; nearest-neighbor reversal; nonlinear retention value; segment retention support |
| M5 | [Text, Social Media, and Customer Networks](modules/M05_Text_Social_and_Network_Analysis.md): text representation, TF-IDF, embeddings, sentiment, topics, annotation, networks | Complaint prevalence and precision; LLM label validation; network brokerage; engagement versus sales |
| M6 | [Causal Effects and Marketing Experiments](modules/M06_Causal_Inference_and_Experiments.md): estimands, selection, randomization, confidence intervals, power, adjustment, DiD, RD, IV, spillovers, recommendation policy evaluation | Email assignment and profit uncertainty; counterfactual trends; exposure-adjusted recommendation values; MovieLens information effects |
| M7 | [Prediction, Machine Learning, and Marketing Actions](modules/M07_Prediction_and_Machine_Learning.md): targets, regularization, trees, ensembles, validation, leakage, metrics, calibration, thresholds, recommender models, ranking, LLM explanations | Rare purchases; coupon targeting; NDCG; food variety and customer goals; goal-weight switches; explanation credibility |
| M8 | [Current Topics and Integrated Marketing Decisions](modules/M08_Current_Topics_and_Integrated_Decisions.md): adaptive recommendation, customer goals and platform incentives, media carryover and saturation, budget allocation, generative AI evaluation | Sleep-reminder campaign; Netflix personalization; content audits and attitude experiments; relevance versus variety; marginal returns; AI workflow time |

The sequence follows the historical syllabus's topics without adopting its dates, grading weights, or AI rules. M8 develops selected current topics; it is not a claim that the predecessor assigned these particular cases. Published research motivates selected cases. Actual mHealth calculations, imposed simulations, and synthetic teaching values are identified separately. No attached private style document or sample syllabus is reproduced here.

## Data, Code, and Numerical Checks

The [Lecture Examples](../03_Data_and_Code/Lecture_Examples/README.md) folder contains small synthetic CSV files, a data dictionary, and a Python script that reproduces the central numerical calculations. It covers all eight modules and uses only the standard library. It has been executed successfully; its output is saved as JSON.

The synthetic examples verify arithmetic and model implications under stated assumptions. Each module includes its executable Python calculation. The [recurring mHealth examples](../03_Data_and_Code/mHealth/recurring_examples/README.md) use actual released records for audits, measurement, regression, segmentation, text prediction, experiment planning, basket prediction, and ranking objectives. Their full source appears directly in the notes, with matching scripts, dependencies, aggregate results, and verification checks.

M1 teaches structural checks, join coverage, repeated totals, and review flags. M2 adds nutrition-informed sample definitions and alternative screens, using the [nutrition methods collection](../01_Resources/12_Nutrition_and_Dietary_Data_Quality/README.md). The individualized Goldberg calculation is an explicitly hypothetical scenario because validated physiological inputs are absent from the logs. M3 compares an association before and after an imposed calorie-range restriction.

## Resources and Additional Worked Cases

The [resource integration map](RESOURCE_INTEGRATION.md) links the newly added references to eight executed course programs. The notes add fixed-cohort business reviews (1.10), recency and frequency (2.13), price endogeneity and instruments (3.12), logging-gap survival (4.13), topic models and denominators (5.12), CUPED (6.15), basket association rules (7.17), and evidence checks for generated claims (8.11). Each case includes its full Python source, assumptions, results, and interpretation. Six additional figures explain the mechanisms and comparisons. The PDF has 130 pages.

## Editing and Building

Edit the Markdown files in `modules/` and the TikZ files in `figures/`. The shared palette and figure styles are in [figures/style.tex](figures/style.tex). The colors follow the [official Illinois brand palette](https://brand.illinois.edu/visual-identity/color): Illini Blue `#13294B` and Illini Orange `#FF5F05`, with limited supporting colors. Labels, line styles, and symbols supplement color.

The [build script](build_notes.py) uses Pandoc to assemble the modules into [LaTeX source](BADM534_Lecture_Notes.tex), substitutes the TikZ source for each Markdown figure, and compiles the PDF with Tectonic. It preserves first-paragraph indentation conventions and prefixes document anchors by module. Tectonic may download TeX packages on its first run.

From the repository root, with Python, Pandoc, and Tectonic available:

```sh
python3 06_Lecture_Notes/build_notes.py
```

To regenerate the PNG figure companions as well, install Pillow and make Poppler's `pdftoppm` available, then run:

```sh
python3 06_Lecture_Notes/build_notes.py --figures
```

Executable paths can be supplied with `--pandoc`, `--tectonic`, and `--pdftoppm`. Intermediate files go into the ignored `build/` folder. The generated `.tex` and PDF are committed so the notes can be read without installing a build environment. The compiled PDF uses the TikZ sources directly, not raster images.

After changes, run the relevant analyses and `python scripts/check_lecture_code.py` from the repository root, inspect compilation warnings, and visually inspect all affected pages and figure previews. Update navigation when adding a module or moving a source. Follow [AGENTS.md](AGENTS.md) for editing conventions and [the root agent guide](../AGENTS.md) for course authority and student support.

## Using the Notes With an LLM or Preparing Slides

Give an assistant the relevant Markdown module, its figure descriptions, and any related CSV or calculation output. Cite module and numbered section, such as “M6, Section 6.4.” Do not infer a deadline or assessment rule from an illustrative exercise. The exercises are public teaching material.

Follow the [preferred Beamer format](../05_Slides/AGENTS.md) when preparing lectures. Use each module's managerial question as the opening, then select the worked case, method, key figure, and decision implication. Keep the full derivation and consequential assumptions in the notes. Each TikZ file can be reused in a LaTeX slide deck; its PNG companion supports other presentation tools. Figures illustrate particular mechanisms and should retain the accompanying assumptions and synthetic-data labels.
