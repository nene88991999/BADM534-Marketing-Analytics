# Demand for Generative-AI Subscriptions

Marketing Analytics. By Nathan Yang.

Three offline cases connect public signals, retention, and price sensitivity. They use the supplied [resource bundle](../../01_Resources/08_M8_Current_Topics_in_Marketing/genai_demand_lab/README.md), with its original files preserved. Public captures are dated observations supplied with that bundle. The consumer panel is entirely synthetic. Neither the panel nor the regression slopes estimate the real AI market.

## Cases and Commands

From the repository root, use Python with NumPy and pandas installed. Versions tested are recorded in [results/verification.json](results/verification.json); supported ranges are in [requirements.txt](requirements.txt).

```sh
python3 03_Data_and_Code/GenAI_Demand/run_all.py
```

The command runs the three programs and eight small counterexample tests, checks that source files are unchanged, and writes aggregate CSV/JSON files plus a source-hash manifest. It makes no network requests, needs no API key, and incurs no model usage charges. The complete analysis scripts also appear in the Markdown and PDF lecture notes.

| Notes | Program | Question and Expected Result |
| --- | --- | --- |
| M2 §2.17 | [measurement.py](measurement.py) | Do title changes alter an apparent attention decline? June–September older-title change: -85.06%; two-title change: -16.66%, with 122 complete days. |
| M4 §4.14 | [retention.py](retention.py) | Do customers leave a provider or the paid category? Fixed-cohort partitions, endpoint versus continuous retention, and four acquisition-event types. |
| M8 §8.13 | [demand.py](demand.py) | When does a log-odds regression recover a utility price parameter? Stock slope -0.03004; flow slope -0.04987; exact binary benchmark -0.06000. |

Each program can also run independently with `python3 03_Data_and_Code/GenAI_Demand/<program>.py`. Paths resolve from the script, so a different working directory also works. Keep the resource bundle in the repository's existing location. The [data dictionary](DATA_DICTIONARY.md) defines inputs and outputs; the [result guide](results/README.md) describes their denominators.

## Interpretation

The Wikipedia calculation counts recorded events for two selected titles, without claiming unique viewers or a complete brand-attention measure. Missing title-days stay unknown. A current redirect target does not establish the full rename history; the two-title mapping comes from the supplied capture and is not a complete page-history reconstruction.

The synthetic roster contains 60,000 consumers and 40 months. Absent subscription rows mean no paid subscription within that complete simulation. Starting cohorts consist of existing January 2025 subscribers, with potentially overlapping provider memberships. Endpoint retention includes customers who left and returned. The category comparison uses exactly the same starting consumers as its provider comparison.

The simulator has heterogeneous tastes, inertia, multiple holdings, and monthly recalibration of category attractiveness. Its generated shares do not satisfy a homogeneous static binary-logit equation. Stock and flow regressions are descriptive projections. Only the separately constructed exact binary benchmark recovers its imposed parameter by construction. No causal price estimate, nested-logit parameter, or counterfactual market share is released.

## Sources and Provenance

- Egan, Mark L., Dominic Russel, Claire Shi, and Vincent Yao (2026), [Competition in Generative AI: Evidence from Consumer Demand](https://www.nber.org/papers/w35953), NBER Working Paper 35953. The abstract and bibliographic record were checked; the full paper was unavailable during this review. Detailed structural-model claims from the supplied notebook are not treated as verified paper findings.
- Fradkin, Andrey (2025), [Demand for LLMs: Descriptive Evidence on Substitution, Market Expansion, and Multihoming](https://arxiv.org/abs/2504.15440). The abstract describes application-level use through OpenRouter.
- Wikimedia, [Page Views](https://doc.wikimedia.org/generated-data-platform/aqs/analytics-api/concepts/page-views.html), for the measurement definition and redirect treatment.

The source bundle, including its collectors, saved notebook, simulator, and public captures, was inspected. Those original programs were not rerun. The course analyses and tests were executed locally against the saved inputs. [manifest.json](manifest.json) records source hashes and rights; [the adaptation review](../../01_Resources/08_M8_Current_Topics_in_Marketing/genai_demand_lab/COURSE_ADAPTATION.md) records corrections and deferred extensions. Public availability alone does not establish a blanket redistribution license.

## Figures

```sh
python3 03_Data_and_Code/GenAI_Demand/build_figures.py
python3 06_Lecture_Notes/build_notes.py --figures
```

The first command regenerates the three TikZ sources from the output tables. The second compiles the notes and previews with the existing Pandoc, Tectonic, and Poppler workflow. Figures use the Illinois palette with markers, line styles, or patterns alongside color. Their aggregate CSVs and descriptions remain available to readers and agents.
