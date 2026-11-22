# Synthetic Consumers and Product Screening

A product manager deciding which concepts receive human research needs a measurement rule and a way to assess mistaken selections. Two original programs distinguish how text becomes a rating from how a rating informs a shortlist. Full Python appears in [M4 §4.23](../../06_Lecture_Notes/modules/M04_Conjoint_Segmentation_and_CLV.md) and [M5 §5.23](../../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md). M7 §7.36 examines validation, M8 §8.11 connects the complete workflow, and M9 §9.18.4 examines consumer representation.

## Reproduction

Python 3.10 or later and its standard library suffice. From the course root:

```bash
python3 03_Data_and_Code/Synthetic_Consumers/anchor_measurement.py
python3 03_Data_and_Code/Synthetic_Consumers/concept_screening.py
python3 -m unittest discover -s 03_Data_and_Code/Synthetic_Consumers -p 'test_*.py' -v
python3 03_Data_and_Code/Synthetic_Consumers/build_figures.py
```

The programs resolve inputs relative to their own files. Both calculations and all ten tests have run successfully. The [results guide](results/README.md) gives expected values. The figure builder reads saved outputs and writes two editable TikZ sources; the note builder renders their PNG companions. No package installation, credentials, model inference, or network access is required.

## Text Measurement and Persona Weights

`anchor_measurement.py` reads [authored responses and imposed similarities](data/anchor_responses.json). Three fictional body-wash concepts share two invented personas. Seven response rows include an identical repeated answer for one persona in the refill condition. Two five-statement anchor sets produce separate category distributions. Each similarity was constructed as 0.2 plus 0.6 times its intended illustrative category weight. The response text and anchor sentences were authored separately; these values are not measured embedding similarities or model outputs.

The method subtracts the minimum similarity and normalizes. It uses the paper's epsilon-zero, temperature-one setting. An explicit course adaptation returns an uninformative status when the similarity spread is at most 1e-12. Any missing required mapping leaves its concept aggregate incomplete, with coverage counts retained. Repeat distributions are averaged within persona before averaging personas equally. The example also reports the different mean obtained from equal response-row weighting.

## Distribution Fit and Shortlist Decisions

`concept_screening.py` reads [six independent fictional concept panels](data/concept_panels.json), with 100 invented ratings per concept. The pooled, reversed, and compressed candidate patterns are imposed using those reference distributions. They isolate mathematical properties; the example estimates no model's performance on unseen data. These six concepts are a separate construction from the three-concept text example.

The calculation gives each concept equal weight and evaluates mean KS similarity, mean absolute rating error, Pearson and Spearman correlations, and retention of the reference top two. Constant scores leave correlation undefined. Ties at the selection boundary leave the shortlist unresolved. All candidates must cover the exact same concept roster. The pooled pattern achieves mean KS similarity 0.925 with no concept discrimination. Reversed ranks retain none of the reference top two; compressed ranks retain both despite shrinking score differences.

## Provenance and Verification

[Maier and coauthors](https://arxiv.org/abs/2510.08338v3) motivate the measurement and validation questions. Their published figures are reviewed evidence, separate from the invented inputs here. The [pinned source assessment](../../01_Resources/29_Synthetic_Consumer_Research/SOURCE_REVIEW.md) records same-survey anchor optimization, split-half metric definitions, missing study data, implementation differences, and source-license discrepancies. The original course programs do not import or execute that repository.

The [data dictionary](DATA_DICTIONARY.md) defines units and fields. The [manifest](manifest.json) records hashes and execution scope. Ten independent checks cover hand normalization, affine invariance, uninformative inputs, repeat weighting, incomplete aggregates, duplicate and missing rosters, undefined correlation, ordered distribution distance, tied selection, and known comparison results. The [optional ungraded lab](../../07_Labs/Synthetic_Consumers/README.md) adds sensitivity analysis and a prospective human-validation design.

Session 5 uses twenty minutes for concept screening; Session 7 uses ten minutes for measurement. Session 14 connects generated personas to actual consumer judgment within the existing philosophical discussion. The course dates, meeting lengths, and unreleased assessment policies retain their existing status.
