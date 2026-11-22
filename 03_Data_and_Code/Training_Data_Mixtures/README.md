# Training Mixtures and Conditional Service Outcomes

A retailer combining training sources needs to evaluate the resulting model across the contexts in which customers use it. Three executed Python programs distinguish an exact synthetic ridge model, imposed customer-service outcomes, and recalculation of published model results. Full code appears in [M7 §§7.33–7.35](../../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md), with two editable TikZ figures and five Session 11 slides.

## Reproduction

Python 3.10 or later and its standard library suffice. From the course root:

```bash
python3 03_Data_and_Code/Training_Data_Mixtures/mixture_regression.py
python3 03_Data_and_Code/Training_Data_Mixtures/service_contexts.py
python3 03_Data_and_Code/Training_Data_Mixtures/source_checkpoint_comparison.py
python3 -m unittest discover -s 03_Data_and_Code/Training_Data_Mixtures -p 'test_*.py' -v
python3 03_Data_and_Code/Training_Data_Mixtures/build_figures.py
```

The programs resolve files relative to their own locations. No installation, credentials, model calls, or network access is needed. The source recalculation reads the pinned files already stored in the [resource collection](../../01_Resources/28_Training_Data_Mixtures/README.md). Run the three programs before the tests, since one check reads saved results. The figure builder updates only the two named TikZ sources; `06_Lecture_Notes/build_notes.py --figures` renders them.

## Comparisons and Inputs

`mixture_regression.py` solves two normal equations under a sum-loss ridge objective. Source A always has both task and tag features with expected style score one; Source B lacks the tag and has expected score zero. The expected score is in arbitrary units. The reference effective penalties are 50 for the task contribution and 1,500 for the tag contribution, with 5,000 Source A examples in the added-data comparison. Other regimes equalize feature scales or reduce the penalty. A separate design fixes 30,000 total examples. All 261 rows are exact noiseless synthetic calculations, with no random seed or empirical fit.

`service_contexts.py` constructs 1,000 paired requests for two hypothetical versions, producing 2,000 request-version records. Product support, refunds, and cancellation have 900, 80, and 20 requests. Successes and missing responses are imposed directly. Request IDs preserve paired changes. Both versions resolve 950 requests correctly; the combined version has 27 recoveries and 27 regressions, and cancellation resolution falls from 19/20 to 8/20. Fifteen missing responses remain in attempted-request denominators. These outcomes are independent of the ridge calculation and estimate no effect of merging actual data suppliers.

`source_checkpoint_comparison.py` verifies archived hashes, follows the upstream last-record-per-epoch rule, and recomputes selected published aggregates. It preserves final and peak rates separately and verifies 51 condition means from three run records each. The [source assessment](../../01_Resources/28_Training_Data_Mixtures/SOURCE_REVIEW.md) records the definitions, response denominators, and checkpoint-selection rules. No upstream program or model was executed.

## Outputs and Checks

The [data dictionary](DATA_DICTIONARY.md) defines the saved records and units. The [results guide](results/README.md) supplies expected values. The [manifest](manifest.json) records inputs, source version, runtime, checks, and file hashes. Ten independent checks cover an original-feature normal equation, penalty scaling, unrelated examples, a fixed-total optimum, invalid inputs, paired changes, missing denominators, empty groups, and resumed epoch records.

The [optional ungraded lab](../../07_Labs/Training_Data_Mixtures/README.md) extends the fifteen-minute Session 11 comparison. It supplies no graded requirement or course-wide AI-use rule. M2 §2.24, M3 §3.15, M8 §8.24, and M9 §9.18.3 connect source assessment, confounded features, supplier changes, and evidence about customer choice.
