# Marketing Dialectics: Renewal and Customer Intent

Two entirely constructed populations each contain 1,000 customers over one renewal month. Both have 90% billed renewal. The number billed despite wanting to stop is 20 in population A and 300 in population B. These imposed counts show why a payment outcome alone does not identify customers' wishes. They do not estimate the effect of a cancellation interface, customer welfare, or Kantian autonomy.

## Inputs and Reproduction

Python 3.10 or later and the standard library are sufficient. There are no external inputs, packages, model calls, or random draws. The eight input cells are specified in [evaluate_retention.py](evaluate_retention.py). Running it recreates [synthetic_customer_months.csv](synthetic_customer_months.csv) and [results.json](results.json).

```sh
python3 03_Data_and_Code/Marketing_Dialectics/evaluate_retention.py
python3 -m unittest discover -s 03_Data_and_Code/Marketing_Dialectics -p 'test_*.py'
```

The complete program also appears in [Marketing Dialectics, Section 9.5](../../06_Lecture_Notes/modules/M09_Marketing_Dialectics.md). The output table is the numerical source for `M09_retention_intent.tex`.

## Data Dictionary

| Field | Definition |
| --- | --- |
| `population` | Constructed population A or B; neither is an experimental treatment. |
| `customer_id` | Synthetic unique identifier within population. |
| `billed` | Boolean: the customer was billed for renewal during the common month. |
| `wanted_renewal` | Boolean: stipulated pre-billing wish to continue at the stated terms. The summary function also accepts `None` for missing intent. |

CSV booleans are strings on disk. A future CSV loader must explicitly map `True` and `False` to booleans; `bool("False")` is true in Python. The executed program constructs typed records before export and does not reload the CSV.

## Interpretation and Verification

All-customer shares use each population's full 1,000 customers. The conditional unwanted share uses its 900 billed customers. Non-billed customers remain in the population. Missing intent remains unknown; the lower bound counts observed unwanted billing, and the upper bound adds every billed customer with unknown intent. These bounds presume the known intent labels are correct. They are descriptive bounds, not confidence intervals.

The output is 900 billed, 880 wanted and billed, and 20 unwanted and billed in A; the corresponding counts in B are 900, 600, and 300. Both include 20 who wanted renewal but were not billed. Independent tests check missing intent, denominator changes, zero billing, duplicate keys, and mistaken string booleans. Run status is recorded in [verification.json](verification.json).

The four-cell construction is original course material. No real customer information or publisher dataset is included. A real application would require a defined intent instrument, measurement timing, nonresponse assessment, and a credible comparison before drawing a causal conclusion.
