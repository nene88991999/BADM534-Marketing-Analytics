# Learning Design and Outcome Comparisons

An instructor choosing a learning tool needs evidence about the outcome that matters and the contribution of each proposed feature. `learning_comparisons.py` contains two separate calculations: arithmetic using published rounded percentages and an original synthetic factorial example.

## Inputs and Interpretation

The 78% and 67% inputs come from [Google Research's announcement](https://research.google/blog/learn-your-way-reimagining-textbooks-with-generative-ai/). Their difference is 11 percentage points; the relative increase is 1100/67%, approximately 16.42%. These rounded summaries do not supply participant observations, sampling uncertainty, or a replication of the trial.

The four synthetic means are 60%, 66%, 68%, and 77%. Factor Q offers questions with feedback; factor F offers alternative representations. Population, source content, assessment, and study-time allowance remain common. Equal allocation defines the average main effects. The 17-point whole-package difference is consistent with multiple allocations of component effects. No student data, estimated treatment effect, or power calculation is contained in this construction.

## Run and Outputs

```sh
python3 03_Data_and_Code/Learning_Design/learning_comparisons.py
python3 03_Data_and_Code/Learning_Design/bill_identity.py
python3 -m unittest discover -s 03_Data_and_Code/Learning_Design -p 'test_*.py'
```

Python 3.10 or newer and its standard library are sufficient. The program has no random seed because it performs exact, deterministic arithmetic. CSV and JSON files under `results/` report the input cells and comparisons. Calculations use exact fractions; exports use decimal display values.

The [electricity page](../../08_Wiki/pilot/index.html) uses the existing [institutional bill table](../Statistical_Inference/results/institutional_bills.csv) and its [complete Python source](../Statistical_Inference/institutional_exposure.py). Its defaults reproduce the saved 1,000-account example. Changed browser inputs are explicitly hypothetical scenarios.

## Course Use

[M2 §2.29](../../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md), [M6 §6.39](../../06_Lecture_Notes/modules/M06_Causal_Inference_and_Experiments.md), and the [optional practice](../../07_Labs/AI_Augmented_Learning/README.md) connect magnitude reporting, component identification, and learning evaluation. [Source review](../../01_Resources/43_AI_Augmented_Learning/README.md) and [verification](VERIFICATION.md) distinguish published observations from teaching constructions.

## Bill Reference Values

`bill_identity.py` reads the synthetic institutional bill table, verifies matched revenue and sales denominators, and exports `results/bill_reference.csv`. Its three bills are USD 100, USD 110, and USD 100 per account-month. `08_Wiki/pilot/build_pilot.py` uses the same calculation to refresh the browser reference data and complete visible Python listing. The browser logic also has independent hand-value checks.
