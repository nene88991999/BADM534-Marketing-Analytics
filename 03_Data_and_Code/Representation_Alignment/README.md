# Changing Text Representations in mHealth

A text-processing service can replace an encoder while retaining a classifier, fit a coordinate alignment, or retrain the classifier. The original synthetic comparison separates geometric similarity from compatibility with a fixed decision rule. The mHealth comparison uses local word and character features on the same unseen descriptions.

## Inputs and Execution

The compact [description sample](data/descriptions.csv) is included. It has 6,000 training, 1,500 validation, and 1,500 test descriptions. No user identifier, date of birth, or weight history appears in this derivative. Read the [dictionary](DATA_DICTIONARY.md), [source manifest](manifest.json), and [verification record](VERIFICATION.md).

Use Python 3.11 or later with the versions in [requirements.txt](requirements.txt). From the repository root:

```sh
python3 -m pip install -r 03_Data_and_Code/Representation_Alignment/requirements.txt
python3 03_Data_and_Code/Representation_Alignment/alignment.py
python3 03_Data_and_Code/Representation_Alignment/evaluate_mhealth.py
python3 -m unittest discover -s 03_Data_and_Code/Representation_Alignment -p 'test_*.py' -v
```

To reconstruct the compact input, first run `python3 03_Data_and_Code/mHealth/download_data.py`, then `python3 03_Data_and_Code/Representation_Alignment/prepare_descriptions.py`. Preparation verifies the public release hash and reads the full compressed food file. Evaluation uses the compact input and needs no network, model downloads, or API key. It fits ordinary lexical representations and linear classifiers locally. Git attributes preserve the CSV bytes so the input checksum remains valid after cloning.

## Results

The invented rotation preserves all pairwise distances and both-neighbor sets while changing the fixed classifier from 8 to 4 correct cases. Compressing the imposed style coordinate preserves 8 correct cases while reducing neighbor overlap to 50%. Training-point alignment restores both scores to 100%.

Validation selects 32 dimensions from 8, 16, and 32 using aligned classification accuracy. On the 1,500 held-out descriptions:

| Configuration | Correct | Accuracy | Neighbor Overlap with Word Features |
| --- | ---: | ---: | ---: |
| Word reference | 522 | 34.80% | 100.00% |
| Character features, original classifier | 119 | 7.93% | 22.00% |
| Aligned character features, original classifier | 430 | 28.67% | 22.00% |
| Character features, retrained classifier | 531 | 35.40% | 22.00% |

The last three share the same character geometry. The classifier's coordinate compatibility changes. The 0.60 percentage-point difference between the compatible word and character classifiers is descriptive for this test sample; no population comparison is estimated. Reference categories include generic labels such as `default`. Seventy-four test descriptions have multiple source categories, and ten have modal categories absent from training. All remain in the primary denominator. Source-label agreement is the target; nutritional correctness requires an independently justified reference.

Full source and interpretation appear in [M5 §5.26](../../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md) and [M7 §§7.42–7.43](../../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md). See [optional practice](../../07_Labs/Representation_Alignment/README.md), [results](results/README.md), and the [research review](../../01_Resources/36_Representation_Alignment/README.md).
