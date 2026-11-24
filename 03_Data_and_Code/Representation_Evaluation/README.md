# Representation Quality and Customer Decisions

A service manager choosing a text representation needs to retain the information that identifies cases for review. Total reconstruction quality weights errors by variation, which can be concentrated in a different component. A second case examines whether exact reconstruction identifies a unique feature interpretation.

## Inputs and Execution

All vectors and labels are invented. `data/cases.json` has four equally weighted cases, two style scales, and a fixed shrinkage factor. Python 3.10 or later and the standard library are sufficient. Run from the repository root:

```bash
python3 03_Data_and_Code/Representation_Evaluation/evaluate_representations.py
python3 03_Data_and_Code/Representation_Evaluation/compare_decompositions.py
python3 -m unittest discover -s 03_Data_and_Code/Representation_Evaluation -p 'test_*.py' -v
```

The first program writes `results/representations.json`, including input vectors, reconstruction errors, variance weights, and routing metrics. The second writes `results/decompositions.json`, including unit directions, coefficients, reconstructed vectors, and removal errors. No dependencies, model downloads, random seed, or network access are required.

## Results and Scope

At style scale 100, representation A explains 99.990001% of variation and recalls none of the two review-required cases. B explains 99.960004% and recalls both. At style scale 1, their explained shares are 50% and 99.98%; the routing results stay the same. Coordinate units reverse the reconstruction ranking. The fixed evaluation labels define the routing target; they are not used to train or select a model here.

Two pairs of weighted unit directions both sum to `(2, 0)`. Removing the first contribution produces squared reconstruction errors of 2 and 5. The coefficient sums differ, so equal reconstruction does not imply equal sparse-autoencoder objectives. Neither calculation estimates a feature's psychological meaning or causal role.

Full Python and three comparisons appear in [M7 §§7.39–7.40](../../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md). See the [dictionary](DATA_DICTIONARY.md), [agent guide](AGENTS.md), [verification](VERIFICATION.md), and [optional lab](../../07_Labs/Representation_Evaluation/README.md).

## Sources

The [review of Delisle and Tan](../../01_Resources/34_Representation_Evaluation/README.md) motivates separate evaluation of aggregate reconstruction, component errors, feature stability, and task outcomes. Their experiments concern internal model activations. These original course examples demonstrate algebra and decision metrics; they do not reproduce sparse-autoencoder training or supply empirical marketing evidence. Attribution and licenses for the separately archived source subset are retained in the resource folder.
