# AI Workflow Evaluation and Economics

Three original synthetic examples connect AI-assisted coding to experimental design, prediction, and economic decisions. They use Python 3.10 or later and the standard library. All inputs are constructed for the course on November 4, 2026. No customer records, downloaded programs, provider credentials, or model API calls enter these calculations.

## Run the Examples

From the repository root:

```sh
python3 03_Data_and_Code/AI_Workflows/factorial.py
python3 03_Data_and_Code/AI_Workflows/repeated_selection.py
python3 03_Data_and_Code/AI_Workflows/investment.py
python3 -m unittest discover -s 03_Data_and_Code/AI_Workflows -p 'test_*.py' -v
```

Paths resolve relative to each script, so commands also work from another directory. Each program overwrites its own derived files in `results/`. Repeated selection uses a fixed seed and two separate pseudorandom streams. The inputs are embedded in the scripts; change them there before regenerating outputs and reconciling the notes and figures. All programs and five independent small-case checks were executed successfully.

## Inputs, Outputs, and Interpretation

| Program and Notes | Output | Observation Unit and Units | Expected Result |
| --- | --- | --- | --- |
| [factorial.py](factorial.py); M6 §6.19 | [Four conditions](results/factorial_cells.csv), [contrasts](results/factorial_results.json) | Model-by-library condition; 100 assigned tasks per cell; counts and pass fractions; JSON contrasts in percentage points | Model gain 5 points without the library and 15 with it; interaction 10 points; joint change 25 points |
| [repeated_selection.py](repeated_selection.py); M7 §7.20 | [Selection results](results/selection_results.csv), [simulation metadata](results/selection_metadata.json) | Candidate-count scenario, averaged over 2,000 independent repetitions; accuracy and Monte Carlo SE in fractions | At 100 candidates, expected selected development accuracy 0.6393 and expected fresh accuracy 0.5 |
| [investment.py](investment.py); M8 §8.17 | [Reuse costs](results/reuse_costs.csv), [price bounds](results/price_bounds.csv), [summary](results/investment_results.json) | Number of uses and hours; separately, pricing scenario and dollars per customer | Reuse breaks even at 12 uses; initial price interval 40–80 dollars; shared-adoption floor 30 exceeds ceiling 20 |

In the factorial CSV, `model=0` denotes the earlier configuration and `model=1` the newer configuration; `library=0/1` denotes absence/presence. `assigned` is the denominator and `passed` the numerator. Counts are stipulated, not experimental observations. Every cell refers to the same task population, rubric, deadline, and resource limits.

In repeated selection, each candidate is correct with probability one-half, independently across candidates and cases. Each has 80 development cases and 200 fresh cases. Within a repetition, the first 1, 5, 20, and 100 candidates form nested sets; the first candidate wins a tie. The test stream never enters selection. Monte Carlo SE describes uncertainty in a simulated mean across repetitions, not a deployment confidence interval. All inputs are public teaching material; the simulation represents fresh evaluation without creating a private assessment set.

Reuse assumes equal accepted output quality, six setup hours, two hours per existing analysis, and 1.25 execution plus 0.25 upkeep hours per reusable analysis over a hypothetical quarter. Pricing holds delivered value at 200 dollars, buyer burden at 40 dollars, fixed cost at 1,000 dollars, and conditional sales at 50. Seller unit cost and the customer's net outside-option utility vary. No demand response or equilibrium price is estimated. No missing values or exclusions are applied.

## Course Connections

- M1 §1.12 distinguishes faulty code, missing evidence, and an unclear analytical target.
- M4 §4.16 connects willingness to pay with customer effort and outside options.
- M5 §5.15 applies fresh evaluation to earnings-call prompt revision.
- M6 §6.19 and M7 §7.20 include complete runnable programs and the sampling conditions.
- M8 §§8.17–8.18 connect reusable work, competitive pricing, and selective model upgrades.
- Sessions 01, 05, 07, 09, 11, and 14 include the relevant discussion or calculation.

The [lecture notes](../../06_Lecture_Notes/README.md) contain all three programs verbatim. Four editable TikZ figures use the same aggregate values, Illinois colors, and text descriptions. The tests check additive contrasts, a binomial maximum against exhaustive binary enumeration, the tie rule, maintenance that prevents cost recovery, and equality at the participation and cost bounds. Passing these checks verifies the specified arithmetic; the hypothetical inputs establish no provider performance or customer demand.
