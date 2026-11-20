# Anomaly Detection and Retail Diagnosis

A retailer must decide whether an unusual outcome warrants repairing checkout, maintaining a campaign, or assessing its measurement system. Two complete Python programs separate detection, variable ranking, event timing, and the evidence needed for a response. Every observation and incident is synthetic. These examples implement original course calculations motivated by the [SHAD source review](../../01_Resources/26_Anomaly_Detection_and_Diagnosis/README.md); they do not reproduce its benchmark or execute its code.

## Inputs and Run Commands

Python 3.10 or later and its standard library are sufficient. From the repository root:

```bash
python3 03_Data_and_Code/Anomaly_Diagnosis/retail_monitoring.py
python3 03_Data_and_Code/Anomaly_Diagnosis/timing_and_missingness.py
python3 -m unittest discover -s 03_Data_and_Code/Anomaly_Diagnosis -p 'test_*.py' -v
```

The first command creates [observations](data/observations.csv), a separate [incident table](data/events.csv), and evaluation outputs. The second creates the exact interval and missingness comparisons. Both use relative paths and require no credentials, downloads, external service, or upstream package. The seed is `5342027`; observation generation uses Python's `random.Random`. The [manifest](manifest.json) records the executed environment and artifact hashes.

The [data dictionary](DATA_DICTIONARY.md) defines the sample, variables, units, and interval convention. [LLM practice](LLM_EXERCISE.md) uses nine evidence packets and a separate variable dictionary. No LLM was called and no saved output represents measured LLM performance.

## Sample and Results

The constructed panel has three online stores, twelve days, and 120 one-minute observations per store-day. The first six days provide 2,160 training rows; the next three provide 1,080 normal validation rows; the last three provide 1,080 evaluation rows. Each of three evaluation store-days contains one 20-minute event. Six complete evaluation store-days remain nominal, supplying 720 minutes for an operational false-alert comparison. Three missing latency values remain in the evaluation roster and receive training-median imputations for scoring.

| Evaluation Quantity | Mean Deviation | Maximum Deviation |
| --- | ---: | ---: |
| Detected event minutes / labeled minutes | 60 / 60 | 60 / 60 |
| Alert minutes outside labeled windows | 9 | 7 |
| Precision | 86.96% | 89.55% |
| Alert minutes / wholly nominal-run minutes | 2 / 720 | 2 / 720 |
| Wholly nominal runs with an alert / nominal runs | 2 / 6 | 2 / 6 |

Both methods detect each event at its onset in this fixed constructed panel. The campaign is an increase in demand, so an alert alone does not justify repair or suppression. For the payment event, the detected interval is [40,65) while the imposed failure lasts [40,60). Five later alert minutes reflect continuing support contacts. They count outside the declared failure window, illustrating how the event definition affects evaluation. Support contacts have the largest average standardized deviation within both the true and detected intervals; the originating payment service is specified by the simulation.

The separate timing comparison gives all three predictions credit under an any-overlap rule. Interval intersection-over-union is 1.00 for [40,60), 0.60 for [45,65), and 1/6 for [0,120). The same event can therefore appear well localized under an overly permissive score. Changing a future observation from 90 to 900 changes backward-filled earlier values but leaves the earlier training-median imputations fixed.

These are fixed-case results from three deliberately large events. They provide neither uncertainty estimates nor performance guarantees for real retailers, other event sizes, or event frequencies.

## Files and Verification

- [retail_monitoring.py](retail_monitoring.py): creates the panel, fits store-and-phase reference values, selects validation thresholds, evaluates later observations, and produces evidence packets.
- [timing_and_missingness.py](timing_and_missingness.py): reproduces the exact timing and information comparisons.
- [test_examples.py](test_examples.py): eight independent checks of sample counts, information boundaries, metric arithmetic, validation tails, saved confusion counts, packet contents, and the campaign example.
- [results/README.md](results/README.md): output definitions, denominators, and interpretation.
- [M7 §§7.29–7.30](../../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md): full program listings and two editable TikZ figures.
- [Optional practice](../../07_Labs/Anomaly_Diagnosis/README.md): a longer ungraded exercise accompanying Session 11's 20-minute application.

Both programs and the eight checks were executed on November 20, 2026. The original source benchmark remains inspected reference material. The public incident table provides disclosed practice labels; fresh incidents are needed for an independent evaluation after students revise their procedures.
