# Reproducible Product Recommendations

A product manager deciding which concepts merit human research needs a recommendation whose numbers, weights, and scope survive another person's review. This example connects the existing synthetic-consumer calculations to a short Markdown report and a machine-readable evidence file. All responses, similarities, and reference panels are invented. No language model, customer study, or external editor runs in the program.

## Inputs and Quantities

The [response construction](../Synthetic_Consumers/data/anchor_responses.json) contains seven authored responses for three concepts and two personas. Each has two imposed anchor comparisons. The refill concept has three response rows because p01 has an identical repeat. The reported Set 1 mean gives each of its two personas equal weight. The [separate panel construction](../Synthetic_Consumers/data/concept_panels.json) contains six fictional concepts, 100 invented reference ratings per concept, and pooled, reversed, and compressed candidate distributions. Candidate distributions use the reference outcomes in their construction.

Read the [data dictionary](../Synthetic_Consumers/DATA_DICTIONARY.md) and [calculation guide](../Synthetic_Consumers/README.md) first. The wrapper imports both existing programs, recomputes their four tables, and requires exact agreement with the saved outputs. It stops on a missing or stale table. This comparison detects inconsistency; the independent arithmetic in the tests addresses selected calculation errors. Neither check establishes real customer demand.

## Run

Python 3.10 or later, standard library only. Keep this folder beside `Synthetic_Consumers` in the course checkout. No installation or API key is needed.

```bash
python3 03_Data_and_Code/Reproducible_Recommendations/reproduce_recommendation.py
python3 -m unittest discover -s 03_Data_and_Code/Reproducible_Recommendations -p 'test_*.py' -v
```

Alternatively, from this folder run `python3 reproduce_recommendation.py`. Input paths resolve from the program file. `--output /path/to/example-output` writes the report elsewhere and adjusts its relative links. That option leaves the source tables unchanged. Record `python3 --version` with a new execution; changing the interpreter does not change the sample definition.

## Expected Results

| Quantity | Reference Value | Unit or Denominator |
| --- | --- | --- |
| Refill p01 first response, Set 1 | 4.25 | Expected rating on categories 1–5 |
| Refill with equal persona weights | 3.975 | Two equally weighted personas |
| Refill with equal row weights | 4.066667 | Three equally weighted responses |
| Five identical p01 responses and one p02 response | 4.158333 | Six equally weighted responses; persona mean remains 3.975 |
| Pooled shortlist and correlation | `null` | All six concept means tie |
| Reversed shortlist and top-two recall | F, E; 0 | Zero of reference concepts A and B retained |

The repeat comparison changes only the number of identical p01 responses, from one to five. Each persona's rating stays fixed. Ratings do not have dollar units and do not establish a treatment effect. The report's $500 budget and $25 participant incentive are explicitly assumed arithmetic for an export-format check.

## Outputs and Reading Routes

- [Recommendation](results/recommendation.md): decision, calculation, figure, interpretation, and links to inputs.
- [Evidence](results/evidence.json): numeric results, missing values, repeat comparison, and SHA-256 hashes of two input files and three calculation scripts.
- [Full program](reproduce_recommendation.py) and [independent checks](test_recommendation.py).
- [Optional lab](../../07_Labs/Reproducible_Recommendations/README.md): interpretation, execution, rendering, navigation, and publication checks.
- M1 §1.15 and M8 §8.25 in the [lecture notes](../../06_Lecture_Notes/README.md); Sessions 1 and 14 in the [slides](../../05_Slides/README.md).

The evidence file preserves JSON `null` for undefined quantities. A text generator must retain that distinction from a measured zero. The hashes establish file identity, not statistical validity or legal permission to redistribute a file. The [manifest](manifest.json) records the published inputs and outputs; the [verification record](VERIFICATION.md) separates executed course checks from optional editor tests.
