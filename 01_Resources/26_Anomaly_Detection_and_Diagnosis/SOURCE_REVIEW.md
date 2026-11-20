# SHAD: Source and Evaluation Review

Paper: [arXiv:2610.01168v1](https://arxiv.org/abs/2610.01168v1), submitted October 1, 2026. Authors: Roberto Stanzione, Jules Barbe, Magali Parrino, Jérémie Fourmann, and Paul Boniol. The local paper is an unchanged PDF download under CC BY 4.0. Figures 7–9 on PDF pages 8–9 were visually inspected alongside the methods and relevant appendix text.

Repository: [scality/shad](https://github.com/scality/shad/tree/b5fbc6085ec6c09919803b41e38b9fa5f9f22364), commit `b5fbc6085ec6c09919803b41e38b9fa5f9f22364`, dated November 12, 2026, inspected November 20, 2026. The declared package is `shad-benchmark` 1.0.0, Python >=3.9, with NumPy and pandas as core dependencies. The code and datasets are declared AGPL-3.0-only. The paper version and repository commit have different dates; inspecting the latter does not verify the exact implementation used to produce every published result.

## Useful Repository Components

| Source | What It Supplies | Potential Course Use |
| --- | --- | --- |
| `shad/dataset.py` | Separate telemetry, time labels, variable labels, and annotation access; explicit nominal/anomalous split | Inspect label leakage and the information supplied to an analyst |
| `shad/metrics.py` | Variable names, units, components, and definitions | Build a domain dictionary that an LLM can retrieve without receiving answers |
| `shad/annotations.py` | Structured event timing, component, and incident descriptions | Distinguish evaluation evidence from prediction inputs |
| `examples/baseline_detector.py` | Median and median-absolute-deviation baseline; variable scores | Motivate a transparent first comparison before adding complex detectors |
| `Scripts/interpretabiliy_main.py` | Structured questions about presence, location, timing, type, and severity | Require separately assessable claims from an LLM |
| `Scripts/eval_llm.py` | Explicit matching and classification rules | Examine what a reported score actually rewards |
| `docs/docs.html` | Documentation for a static dataset explorer and contextual annotations | Inform an interactive course wiki with accessible evidence behind a claim |

The README and selected source files are copied unchanged. Their relative links to omitted repository files may not resolve within this partial snapshot; the catalog provides pinned upstream URLs. No benchmark data, saved LLM results, model weights, or API credentials are included.

## Evaluation Boundaries in the Paper

The detection protocol trains semi-supervised methods on 83 nominal series and evaluates on 132 series containing injected events. Normal timestamps remain within the latter series, so the evaluation does include negative time points. A deployment study additionally needs held-out normal runs to measure false alerts over uninterrupted operation. The experiment's event prevalence and failure mix are designed properties, not estimates of operational incident frequency.

Figure 7 reports a group of methods without statistically significant pairwise differences at the specified testing level. That result does not establish performance equivalence. The anomaly-type comparisons matter because a single average can conceal weak detection of a commercially important failure.

Section 4 uses VUS-PR with a 25-point buffer for detection and NDCG for variable rankings. A buffer permits timing tolerance. A course exercise should state how that tolerance relates to the time available for an intervention. NDCG concerns a ranking against the specified labels; causal evidence requires an additional design.

The level-1 and level-2 LLM experiments supply correct presence and component information. A comparison using actual detector outputs would also incorporate upstream errors. The description condition first generates prose from an image, then answers the questionnaire from that prose. It therefore introduces a representation step before the final answer. Comparing its output with a plot-based answer does not isolate model reasoning from information lost during summarization.

## Code Findings Relevant to Adaptation

### Information Available at the Alert Time

In [`shad/dataset.py`](https://github.com/scality/shad/blob/b5fbc6085ec6c09919803b41e38b9fa5f9f22364/shad/dataset.py), `_fill(df, "ffill")` calls `df.ffill().bfill()`. Leading missing observations can acquire a later value. The default `fill=None` preserves missing values; the concern applies when the filling option is selected. For a live monitoring exercise, preserve unknown leading values or use a training-derived rule that respects time. Retrospective reconstruction and online detection have different permissible information sets.

The same file's `Series.plot()` chooses labeled dimensions by default and shades true intervals. That display is useful for understanding annotated incidents. Supplying it to an LLM while evaluating unsupervised localization would reveal answers. The separate benchmark image generator removes label columns; the finding about `Series.plot()` does not establish leakage in the paper's image experiment.

### Timestamps and Representations

[`Scripts/generate_images.py`](https://github.com/scality/shad/blob/b5fbc6085ec6c09919803b41e38b9fa5f9f22364/Scripts/generate_images.py) calls `dropna()` across a file, removes the timestamp, and plots the remaining values against positional indices. If rows are deleted, those positions differ from the original CSV positions used by an evaluator. Even without deletion, elapsed minutes and row counts differ when sampling intervals are irregular. A course adaptation should retain timestamps and an explicit mapping to the evaluator's intervals.

[`Scripts/compute_features.py`](https://github.com/scality/shad/blob/b5fbc6085ec6c09919803b41e38b9fa5f9f22364/Scripts/compute_features.py) drops missing values separately within each variable and passes `catch24=True` to `pycatch22`. Thus the inspected implementation requests two additional features beyond the conventional 22-feature set. Per-variable deletion can also remove different times from different series. Record the representation actually supplied and preserve any timing information required by the question.

### Temporal and Component Scores

In [`Scripts/eval_llm.py`](https://github.com/scality/shad/blob/b5fbc6085ec6c09919803b41e38b9fa5f9f22364/Scripts/eval_llm.py), `time_matches()` returns true when any labeled point overlaps a predicted inclusive row-index interval on selected columns. It does not penalize an excessively wide interval. When exact column matching fails, its fallback can select all labeled columns on the predicted server even if a disk was specified. A full-series interval could therefore receive temporal credit without a precise incident boundary. Report interval intersection-over-union, onset error, and missed events separately in a course adaptation, with a defined convention for empty and multiple intervals.

`dimension_matches()` matches a server and disk when the annotation provides both, or the server when only that component is provided. It does not require the exact metric name within a component. Correctly predicting no anomaly also receives localization credit through `evaluate_row()`. Consequently, localization accuracy in this evaluator is neither exact-variable accuracy nor a score conditional only on anomalous cases. Keep the denominator and matching unit beside the result.

The classification evaluator reports both macro-F1 and weighted-F1. Its macro average includes configured classes with zero support as zero. Identify the class set and averaging rule before comparing results across subsets. F1 is not classification accuracy.

### Baselines and Answer Information

[`examples/baseline_detector.py`](https://github.com/scality/shad/blob/b5fbc6085ec6c09919803b41e38b9fa5f9f22364/examples/baseline_detector.py) estimates robust scaling from nominal runs and averages standardized deviations for detection. Its variable score averages over ground-truth anomalous timestamps. That localization comparison is conditional on knowing the event interval. A complete alert workflow must obtain the interval from the detector or identify the exercise as an ideal-information comparison.

The example's hand-written `average_precision()` ranks individual observations. Its result can depend on the order of tied scores. A course implementation should use a documented tie-aware metric and verify it on a small tied-score example. The file supplies a simple baseline, not the paper's complete 18-detector VUS-PR experiment.

### Reproduction and Model Versions

The inspected `Scripts/interpretabiliy_main.py` uses one run and `mistral-large-latest`; the paper describes multiple models and five-run averages. An alias can change without a source-code change. Reproducing a particular comparison requires dated model identifiers, prompts, run settings, parsed responses, and scoring conventions. The description runner reads `keys.env`, while the README installation example mentions `.env`; configuration should be reconciled before any execution.

These findings identify conditions to check during adaptation. No upstream program or API request was executed, and no claim is made about their quantitative effect on the published results.

## Implications for an Interactive Wiki

The upstream website uses static HTML and JavaScript, with a series explorer connected to CSV observations and XML event metadata. This is compatible with the course's intended GitHub Pages architecture. A course version could let students choose a fixed incident, inspect selected variables, compare a model explanation with an evidence table, and reveal the incident record after answering. Store the selected data and dictionary with the site, pin versions, and provide the same information in Markdown and a downloadable table.

Original course code can implement that interaction independently. Any copied upstream code must retain its AGPL terms and notices. The website's source and documentation were inspected; browser interaction and hosting behavior were not tested.
