# M1. Marketing Decisions, Data, and AI-Assisted Python

A retailer must decide which customers should receive a coupon, how much inventory to place in each store, and which product descriptions should appear online. Each decision needs a different analytical object. A forecast of next week's purchases can inform inventory. A comparison of purchases with and without a coupon can inform targeting. A summary of product complaints can identify a service problem. An analysis becomes useful when its output corresponds to the decision the manager can actually change.

A managerial objective also requires justification. Before optimizing a response, identify who selected the end, whose choices the action changes, and what reasons could justify it to affected people. An accurate forecast or efficient algorithm can advance an end the firm ought to reject. Kant's distinction between phenomena and noumena, developed in §9.41, limits the claim that an empirical representation exhausts the person represented. Practical judgments about ends, authority, and obligations require their own arguments.

## 1.1 From a Marketing Question to an Analytical Object

Consider a subscription service deciding whether to offer a renewal discount. The service observes account tenure, past payments, recent use, and prior contacts. A descriptive analysis reports renewal rates by tenure. A predictive analysis estimates the probability that an account renews under the conditions represented in the training data. A causal analysis estimates how an offer changes renewal. A decision analysis combines that change with margins, contact costs, and operational constraints. These objects can use overlapping data while answering different questions.

The timing of the decision determines what information is available. If an account must be selected on Monday morning, a support call made on Wednesday cannot be a predictor for that selection. A variable can be strongly associated with an outcome and still be unusable at the decision time. Write down a forecast origin, an outcome window, and a feature window before constructing a table. An account-week table and an account-lifetime table support different forecasts because their rows and time horizons differ.

For a renewal offer, a useful decision quantity is incremental expected contribution:

$$
\Delta\pi_i=m_i\{p_i(1)-p_i(0)\}-c_i.
$$

Here $i$ identifies an account, $p_i(1)$ and $p_i(0)$ are its renewal probabilities with and without the offer, $m_i$ is contribution in dollars per retained account over the specified horizon, and $c_i$ is the expected incremental cost of making the offer. This compact expression assumes that the offer's costs can be summarized by $c_i$ and that $m_i$ already reflects relevant variable costs. When every renewing recipient receives a discount, discount expense depends on renewal under treatment and should be modeled explicitly.

The difference between the two renewal probabilities matters because many accounts would renew without assistance. Suppose contribution is $100 and contact cost is $3. Then an account whose renewal probability rises from 0.90 to 0.91 has incremental expected contribution of $-2. An account whose probability rises from 0.40 to 0.50 has contribution of $7. Ranking by treated renewal probability chooses the first account; ranking by incremental contribution chooses the second. Observing only treated customers would not reveal the untreated probabilities.

![High response and high incremental value can identify different customers.](../figures/M01_response_vs_value.png)

With contribution and contact cost held fixed, the first account's high baseline renewal probability reverses its ranking under incremental value. A response model and a targeting policy therefore need separate evaluation.

A recommendation also needs a reason why the action ought to be taken. A profitable renewal rule may impose an unwanted obligation on a customer or a burden on someone outside the customer table. Identify affected people, state the principle governing their treatment, and compare a feasible alternative. An estimate of what a company can achieve supplies evidence for that argument; the normative premise explains which means and consequences are justified.

## 1.2 The Unit of Observation Determines the Calculation

A transaction system often stores one row per product line, while the marketing question concerns orders or customers. Suppose order O1 contains two product lines, O2 contains one, and O3 contains three. There are six rows, three orders, and perhaps only two customers. Counting rows as purchases would report six orders. Averaging customer attributes over product lines would give more weight to customers with larger baskets.

A key uniquely identifies the intended unit. At the line level, the key might be the combination of order ID and line number. At the order level, it is order ID. At the customer level, it is customer ID. A useful data contract states the key, allowed duplicates, measurement units, missing-value codes, and date conventions. It also states whether a negative quantity represents a return, whether a price includes tax, and whether canceled orders belong in the analysis.

For line $\ell$ in order $o$, gross line sales are quantity times unit price, $s_{o\ell}=q_{o\ell}p_{o\ell}$. Order sales are $S_o=\sum_\ell s_{o\ell}$, and customer-period sales are the sum across that customer's eligible orders during the period. These are identities once the population and variables have been defined. They do not require a behavioral assumption. The substantive choices enter through eligibility, returns, discounts, and the observation window.

Joining data can change the population or its weights. A many-to-one join from order lines to a customer table should add customer attributes without multiplying the original rows. If the customer table accidentally contains two records for a customer, every matching order line appears twice. A program can finish without an error while overstating sales. Verify the relationship between keys before joining, and compare row counts and totals afterward.

![A duplicate customer key multiplies transactions in a join.](../figures/M01_join_multiplication.png)

For a single $40 order, a customer lookup with two matching records produces two joined rows and an apparent $80 total. This error arises from the structure of the tables. Increasing the sophistication of the subsequent model cannot repair it.

## 1.3 Python Objects and Reproducible Calculations

Python stores individual values in objects such as integers, floating-point numbers, strings, and booleans. A list stores an ordered collection; a dictionary associates names with values. A function packages a calculation with explicit inputs and an output. These distinctions matter when an assistant supplies code: a column of numeric-looking strings does not behave like a numeric column, and an empty string does not automatically represent a missing value.

Suppose two orders contain three product lines. Multiplying quantity by unit price gives line sales; summing within each order gives order sales. Returning each calculation as a number allows its result to be checked and reused.

```python
lines = [
    {"order": "O1", "quantity": 2, "unit_price": 10.0},
    {"order": "O1", "quantity": 1, "unit_price": 5.0},
    {"order": "O2", "quantity": 3, "unit_price": 4.0},
]

def line_sales(line):
    return line["quantity"] * line["unit_price"]

order_sales = {}
for line in lines:
    key = line["order"]
    order_sales[key] = order_sales.get(key, 0.0) + line_sales(line)

assert order_sales == {"O1": 25.0, "O2": 12.0}
assert sum(order_sales.values()) == 37.0
```

The total is $37 across two orders, so average order value is $18.50. Dividing by the three product lines would instead give average line sales, $12.33. Neither denominator is inherently wrong; they describe different objects. The mistake would be assigning one calculation the other's interpretation.

A DataFrame provides a tabular interface for larger data. In pandas, selecting columns, filtering rows, creating variables, grouping observations, and joining tables are distinct operations. Use explicit intermediate names when those operations change the unit of observation. For example, `eligible_lines`, `orders`, and `customer_months` communicate more than repeatedly overwriting `df`. The [pandas tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/) provide syntax references; the analytical specification should determine which operations are needed.

Notebook execution order can hide dependencies. A cell may work because an earlier interactive command created a variable that is absent from the saved notebook. Before describing a notebook as reproducible, restart the kernel and run all cells in order. Store file paths relative to the project, record package versions, and distinguish source data from derived outputs. A random seed helps reproduce a simulation or split, but it does not guarantee identical results across every software version or computing platform.

## 1.4 Case Study: A Coupon Campaign Specification

A retailer has a monthly contact budget for 5,000 customers. The proposed campaign offers a discount on the next purchase. The manager initially asks for “a model to find our best customers.” That request leaves the action, outcome, and objective unresolved. The highest-spending customers may receive the offer without changing their behavior; customers likely to respond may buy products with low margins.

A usable specification would identify the decision date, eligible customer population, offer, evaluation horizon, and objective. One possibility is to maximize incremental contribution during the next 30 days, subject to the contact limit. Eligibility might require marketing consent and an active account. The analysis should define contribution after discounts, returns, fulfillment, and contact costs. It should identify which customer information existed before assignment and how untreated outcomes will be measured.

The initial dataset might include customer-level histories and a randomized pilot. Without such a pilot or another credible design, a response model can help describe or predict behavior, but the incremental contribution calculation remains unresolved. A randomized test can supply the incremental-response evidence needed to decide whether a larger rollout is profitable.

A specification also needs acceptance criteria. The eligible-customer table must have one row per customer, no post-assignment features, and the intended date coverage. A campaign summary must reconcile assigned counts, contact costs, purchases, and contribution. These checks are small enough to state before asking an AI assistant to implement the analysis. They protect the meaning of the result while allowing flexibility in the code.

## 1.5 AI-Assisted Coding as a Sequence of Verifiable Steps

An effective coding request names the inputs, output, definitions, and checks. For the transaction example, ask for a function that accepts product-line records, validates required fields, aggregates sales by order, and returns both order totals and an exception report. Provide the three-line example and its expected $37 total. Ask the assistant to explain what happens with a return, a missing order ID, or a duplicated line.

Generate one analytical transformation at a time when the next step depends on a definition. Inspect the proposed code before executing it, especially commands that install software, delete files, upload data, or invoke an external API. Read error messages as evidence about the code's assumptions. A type error may reveal numeric values stored as strings; a merge error may reveal an incorrect key. Repairing the error without understanding its cause can preserve the underlying analytical mistake.

Verification should use both identities and meaningful counterexamples. Order totals must sum to the line total for the same eligible rows. A single known customer should produce a manually calculable summary. An empty input should have an explicit result. A missing customer lookup should not silently remove sales. These checks constrain what the implementation is allowed to do without forcing one particular coding style.

Keep a short record of consequential AI contributions: the task requested, important changes to the plan or code, and the checks performed. A saved conversation alone does not establish correctness. The record should make it possible to explain why a transformation was accepted.

## 1.6 Interpreting and Communicating a Result

A useful recommendation names the decision, states the relevant estimate with units and uncertainty, and explains how it changes the action. “The model has high accuracy” leaves the manager's decision unresolved. “At a $3 contact cost and the stated contribution assumptions, contact the customers with positive estimated incremental contribution, subject to capacity” connects the analysis to the objective. The recommendation still needs evidence about how the probabilities were estimated and whether the policy was evaluated on new customers or periods.

Results should distinguish observation from assumption. A transaction total is calculated from recorded eligible rows. A renewal probability is an estimate. A contribution margin may be supplied by finance. An untreated outcome for an offered customer is counterfactual. Listing these roles prevents a spreadsheet or notebook from giving every input the appearance of equal certainty.

If one customer places four orders and another places one, an order-weighted mean gives the first customer four times the weight. If both customers should count equally, calculate each customer's mean first. If an AI-generated program reports six purchases from six product lines, inspect whether purchase was defined as a line or an order. If an offer has a high response rate, ask for the response rate under no offer before interpreting the response as an effect.

## 1.7 Readings

The [Python marketing research companion repository](https://github.com/python-marketing-research/python-marketing-research-1ed) provides examples tied to marketing applications. Its notebooks are reference material and require inspection of dependencies and data paths before adaptation. The [pandas tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/) support tabular implementation.

## 1.8 mHealth: From Food Entries to a Decision Table

An mHealth product manager must decide which food categories to suggest when a customer returns to the app. Recent logs reveal repeated categories, variation across days, and gaps in observation. The immediate analytical task is to construct a reliable customer history. A recommendation based on duplicated daily totals or an accidental change in the customer population can look precise while describing the wrong behavior.

The released files contain actual 2016 records. User identifiers have been replaced, birthdays have been replaced with age on January 1, 2016, and weight fields contain documented random perturbations. The food file has 13,874,280 entries from 5,908 users. The separate daily file covers a smaller set of users and dates. Food categories, descriptions, and calorie fields retain their source values, apart from standardizing provider references to mHealth. The [data dictionary](../../03_Data_and_Code/mHealth/DATA_DICTIONARY.md) defines the available fields and unresolved coding conventions. In particular, `Weightchange`, `Goalplan`, and `Gender` have undocumented code meanings. None establishes a treatment, a behavioral goal, or a validated sex variable for an energy equation.

The working cohort retains every entry for users whose first four hexadecimal pseudonym digits have a value below 4,096. This fixed rule reduces memory requirements and preserves within-user histories. Its realized sample contains 917,153 entries, 370 users, and 76,804 observed user-days. Ages at the reference date range from 17 to 76. The cohort is a subset of app users who appear in the released file; it is not a representative population sample. The adult nutrition sensitivity analysis in M2 uses a separate age restriction.

A food-entry row records an item, while `Foodcalories` repeats the source daily total. On the first eligible user-day selected by the code below, five entries on July 4 have item calories summing to 1,132.7852. Each row repeats a daily total of 1,132.79. Summing that repeated field gives 5,663.95, exactly five times the reported daily total. The small difference between the item sum and one copy of the daily total is compatible with rounding in this case. Larger discrepancies elsewhere require investigation.

The daily key is `(Userid, date)`. A left join preserves all 76,804 cohort days, with 37,634 matched days and 39,170 unmatched days in the separate daily file. Replacing it with an inner join would remove more than half the cohort days. An unmatched row is therefore a sample-definition decision, even if the software reports no error.

![A left join preserves observed days while an inner join changes the analysis population.](../figures/M01_mhealth_join.png)

The two branches retain the same matched records. Only the left-join branch preserves the unmatched days needed to describe the food-log cohort. Neither branch supplies unobserved calendar days.

### 1.8.1 Loading Data and Constructing Daily Measures

Use Python 3.13 with NumPy 2.1.3, pandas 2.2.3, PyArrow 19.0.0, SciPy 1.15.3, scikit-learn 1.6.1, and statsmodels 0.14.4 to reproduce the saved calculations. From the repository root, install the pinned packages into an environment, verify the release files, and run the analyses in dependency order:

```sh
python -m pip install -r 03_Data_and_Code/mHealth/recurring_examples/requirements.txt
python 03_Data_and_Code/mHealth/download_data.py
python 03_Data_and_Code/mHealth/recurring_examples/run_all.py
```

The downloader checks the published SHA-256 hashes. The first run reads the compressed food file in chunks and saves a local Parquet cache; subsequent runs reuse it. The cache is excluded from Git. Delete the `recurring_examples/cache` directory to force a fresh derivation. `common.py` supplies the same sample and measurement functions to every module. Paths are relative to the script location, so the saved programs can also be run from another working directory.

For each observed day, category breadth counts distinct recorded categories, assigning missing labels to `Unclassified`. Calorie-share variety uses the sum of included item calories as its denominator. A negative or missing item calorie value invalidates that day's share calculation; a nonpositive item sum also makes shares undefined. These conditions affect calorie-based variety, while the day's existence can still be used to measure logging. The first reported daily total is retained only after checking that its nonmissing values agree within the day.

Python source: [common.py](../../03_Data_and_Code/mHealth/recurring_examples/common.py). From its directory, run `python common.py`.

```python
"""Shared input and measurement functions for the eight mHealth examples."""

from pathlib import Path
import hashlib
import json

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent
DATA = ROOT.parent / "data"
CACHE = ROOT / "cache"
OUTPUT = ROOT / "results"
SEED = 534
COHORT_THRESHOLD = 4096


def save_result(module, result):
    OUTPUT.mkdir(exist_ok=True)
    (OUTPUT / f"{module}.json").write_text(
        json.dumps(result, indent=2, allow_nan=False) + "\n"
    )


def load_food():
    """Keep all rows for users whose first four pseudonym hex digits are <4096."""
    CACHE.mkdir(exist_ok=True)
    cached = CACHE / "food.parquet"
    metadata = CACHE / "source.json"
    manifest = json.loads((ROOT.parent / "manifest.json").read_text())
    signature = {
        "sha256": manifest["files"]["food_entries.csv.gz"]["sha256"],
        "threshold": COHORT_THRESHOLD,
        "preparation_version": 2,
    }
    if (
        cached.exists()
        and metadata.exists()
        and json.loads(metadata.read_text()) == signature
    ):
        return pd.read_parquet(cached)
    columns = [
        "Userid",
        "Fancydate",
        "Name",
        "Category",
        "Calories",
        "Foodcalories",
        "Budgetcalories",
        "Age_at_2016_01_01",
    ]
    parts = []
    for chunk in pd.read_csv(
        DATA / "food_entries.csv.gz", usecols=columns, chunksize=250000
    ):
        code = chunk.Userid.str.slice(1, 5).map(lambda value: int(value, 16))
        parts.append(chunk.loc[code < COHORT_THRESHOLD].copy())
    food = pd.concat(parts, ignore_index=True)
    food["date"] = pd.to_datetime(food.Fancydate)
    food["category"] = food.Category.fillna("Unclassified")
    food["description"] = (
        food.Name.fillna("")
        .str.casefold()
        .str.replace(r"\s+", " ", regex=True)
        .str.strip()
    )
    food.to_parquet(cached, index=False)
    metadata.write_text(json.dumps(signature, indent=2) + "\n")
    return food


def make_daily(food):
    """One row per observed user-day; missing calendar days are not created."""
    keys = ["Userid", "date"]
    grouped = food.groupby(keys, observed=True)
    daily = grouped.agg(
        entries=("Calories", "size"),
        category_count=("category", "nunique"),
        item_calories=("Calories", "sum"),
        food_calories=("Foodcalories", "first"),
        budget_calories=("Budgetcalories", "first"),
        daily_total_versions=("Foodcalories", "nunique"),
        budget_versions=("Budgetcalories", "nunique"),
    )
    daily.loc[daily.daily_total_versions != 1, "food_calories"] = np.nan
    daily.loc[daily.budget_versions != 1, "budget_calories"] = np.nan
    invalid = food.Calories.isna() | food.Calories.lt(0)
    daily["invalid_item_calories"] = invalid.groupby([food.Userid, food.date]).sum()
    categories = food.groupby(keys + ["category"], observed=True).Calories.sum()
    category_totals = categories.groupby(level=keys).transform("sum")
    concentration = (
        (categories / category_totals.where(category_totals > 0))
        .pow(2)
        .groupby(level=keys)
        .sum(min_count=1)
    )
    daily["variety"] = (1 - concentration).where(
        (daily.item_calories > 0) & (daily.invalid_item_calories == 0)
    )
    daily = daily.reset_index().sort_values(keys).reset_index(drop=True)
    assert not daily.duplicated(keys).any()
    assert daily.variety.dropna().between(-1e-10, 1 + 1e-10).all()
    return daily


def make_baskets(food):
    """Distinct observed categories; the missing-category label is not a candidate."""
    selected = food.loc[
        food.category != "Unclassified", ["Userid", "date", "category"]
    ].drop_duplicates()
    return (
        selected.groupby(["Userid", "date"], observed=True)
        .category.agg(lambda values: tuple(sorted(values)))
        .reset_index(name="basket")
    )


def description_holdout(text):
    """A fixed description-level split independent of labels or outcomes."""
    return int(hashlib.sha256(text.encode()).hexdigest()[:8], 16) % 5 == 0


def load_inputs():
    food = load_food()
    return food, make_daily(food), make_baskets(food)


if __name__ == "__main__":
    food, daily, baskets = load_inputs()
    daily.to_parquet(CACHE / "daily.parquet", index=False)
    baskets.to_parquet(CACHE / "baskets.parquet", index=False)
    result = {
        "rows": len(food),
        "users": int(food.Userid.nunique()),
        "user_days": len(daily),
        "categories": int(food.category.nunique()),
        "missing_category_rows": int(food.Category.isna().sum()),
        "invalid_item_calorie_rows": int(
            (food.Calories.isna() | food.Calories.lt(0)).sum()
        ),
        "days_with_inconsistent_daily_total": int(
            daily.daily_total_versions.ne(1).sum()
        ),
        "days_with_inconsistent_budget": int(daily.budget_versions.ne(1).sum()),
        "nonpositive_recorded_daily_totals": int(daily.food_calories.le(0).sum()),
        "variety_eligible_days": int(daily.variety.notna().sum()),
        "item_total_matches_recorded_total_within_one": int(
            (daily.item_calories - daily.food_calories).abs().le(1).sum()
        ),
    }
    save_result("cohort", result)
    print(json.dumps(result, indent=2))
```

### 1.8.2 Join Validation and a Hand-Checkable Day

The join declares a one-to-one relationship and records unmatched keys. The small day-level example checks both candidate aggregations against the repeated total. Keeping these checks beside the join prevents a later model from silently inheriting a different denominator.

Python source: [m01.py](../../03_Data_and_Code/mHealth/recurring_examples/m01.py). From its directory, run `python m01.py`.

```python
"""Assess the cohort, repeated totals, and the separate daily file."""

import json
import pandas as pd
from common import DATA, load_inputs, save_result

food, daily, baskets = load_inputs()
other = pd.read_csv(DATA / "daily_records.csv.gz", usecols=["Userid", "Fancydate"])
other["date"] = pd.to_datetime(other.Fancydate)
assert not other.duplicated(["Userid", "date"]).any()
joined = daily.merge(
    other[["Userid", "date"]],
    how="left",
    on=["Userid", "date"],
    validate="one_to_one",
    indicator=True,
)
assert len(joined) == len(daily)
example = daily.loc[(daily.entries.between(3, 6)) & daily.food_calories.gt(0)].iloc[0]
rows = food.loc[food.Userid.eq(example.Userid) & food.date.eq(example.date)]
result = {
    "rows": len(food),
    "users": int(food.Userid.nunique()),
    "days": len(daily),
    "matched_days": int(joined._merge.eq("both").sum()),
    "unmatched_days": int(joined._merge.eq("left_only").sum()),
    "example_date": str(example.date.date()),
    "example_entries": len(rows),
    "example_item_sum": float(rows.Calories.sum()),
    "example_daily_total": float(example.food_calories),
    "example_wrong_sum": float(rows.Foodcalories.sum()),
}
save_result("M01", result)
print(json.dumps(result, indent=2))
```

### 1.8.3 Data Cleaning as a Sequence of Decisions

Structural checks stop calculations that violate their stated observation unit. A duplicate key in a daily lookup can multiply food records, so it must be resolved before joining. Review flags serve a different purpose: they identify observations whose meaning needs investigation. The cohort contains 52,838 rows equal on the selected fields of user, day, normalized description, category, and calories. Those fields omit event timestamps and meal identifiers. Repeated servings can therefore produce equal rows. Automatically dropping them would impose an unsupported definition of duplication.

The assessment finds 206 food rows with missing categories, one negative item calorie value, and 23 days with a nonpositive sum of item calories. The calorie-share calculation consequently excludes 24 days. By contrast, 319 days have a nonpositive reported daily total. These counts differ because the item sum and reported total are separate measurements. Their discrepancy exceeds one calorie unit on 23,729 days. These flags can overlap and must not be added as if they represented disjoint exclusions.

A value outside a chosen review range is evidence for inspection, not proof of an error. The reported daily calorie median is 1,475.63, and the range is 0 to 9,190. A review flag below 100 or above 5,000 marks 651 days. Those thresholds are imposed sensitivity choices. They do not establish nutritional adequacy or identify incorrect reports. Preserve the released values, add flags, document the rule for each analysis, and report the resulting sample. M2 compares nutrition-informed alternatives; M3 repeats a regression after a stated restriction.

A useful AI coding request is: “Create separate structural checks and review flags. Stop on a duplicate daily key, preserve repeated food entries, count overlapping flags separately, and return the retained sample for each calculation.” Verify the proposed implementation with a two-entry day whose repeated total is 100 and whose calorie shares are 0.9 and 0.1. It must produce a daily total of 100 and variety of 0.18. A gap from January 1 to January 3 must remain a missing January 2 observation. The executable counterexamples are in `test_logic.py`.

Python source: [assessment.py](../../03_Data_and_Code/mHealth/recurring_examples/assessment.py). From its directory, run `python assessment.py`.

```python
"""Separate structural failures, review flags, and analysis-specific exclusions."""

import json
import numpy as np
import pandas as pd
from common import DATA, load_inputs, save_result


def require_unique(frame, keys):
    if frame[keys].isna().any().any():
        raise ValueError("Missing join key")
    if frame.duplicated(keys).any():
        raise ValueError("Duplicate key at the declared observation unit")


def daily_flags(daily):
    flags = pd.DataFrame(index=daily.index)
    flags["invalid_item"] = daily.invalid_item_calories.gt(0)
    flags["nonpositive_item_sum"] = daily.item_calories.le(0)
    flags["nonpositive_daily_total"] = daily.food_calories.le(0)
    flags["missing_daily_total"] = daily.food_calories.isna()
    flags["total_discrepancy_over_one"] = (
        (daily.food_calories - daily.item_calories).abs().gt(1)
    )
    flags["daily_total_below_100_or_above_5000"] = daily.food_calories.lt(
        100
    ) | daily.food_calories.gt(5000)
    return flags


def run_assessment():
    food, daily, baskets = load_inputs()
    assert food.Userid.notna().all() and food.date.notna().all()
    assert food.date.between("2016-01-01", "2016-12-31").all()
    require_unique(daily, ["Userid", "date"])
    # Repeated entries can be legitimate. Flag equality on these fields without deletion.
    fields = ["Userid", "date", "description", "category", "Calories"]
    duplicate_flags = food.duplicated(fields, keep=False)
    flags = daily_flags(daily)
    health = pd.read_csv(
        DATA / "daily_records.csv.gz",
        usecols=["Userid", "Fancydate", "Age_at_2016_01_01", "Currentweight"],
    )
    health = health.loc[health.Userid.isin(food.Userid.unique())]
    require_unique(health, ["Userid", "Fancydate"])
    age_versions = health.groupby("Userid").Age_at_2016_01_01.nunique(dropna=False)
    assert age_versions.eq(1).all()
    result = {
        "food_rows": len(food),
        "daily_rows": len(daily),
        "missing_category_rows": int(food.Category.isna().sum()),
        "rows_equal_on_selected_entry_fields": int(duplicate_flags.sum()),
        "missing_item_calorie_rows": int(food.Calories.isna().sum()),
        "negative_item_calorie_rows": int(food.Calories.lt(0).sum()),
        "flags_by_user_day": {key: int(value) for key, value in flags.sum().items()},
        "recorded_calorie_quantiles": {
            str(q): float(value)
            for q, value in daily.food_calories.quantile(
                [0, 0.01, 0.5, 0.99, 1]
            ).items()
        },
        "matched_daily_file_rows": len(health),
        "fixed_age_min": int(health.Age_at_2016_01_01.min()),
        "fixed_age_max": int(health.Age_at_2016_01_01.max()),
        "nonpositive_weight_rows": int(health.Currentweight.le(0).sum()),
    }
    save_result("assessment", result)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    run_assessment()
```

## 1.9 Python Calculations for the Synthetic Cases

The inputs below are imposed teaching values. Running the program creates the labeled synthetic CSV files and prints the corresponding calculations. They are separate from the mHealth estimates. Keep the script beside `example_helpers.py` in `03_Data_and_Code/Lecture_Examples`.

Python source: [example_helpers.py](../../03_Data_and_Code/Lecture_Examples/example_helpers.py). From its directory, run `python example_helpers.py`.

```python
"""File output and arithmetic helpers for synthetic lecture examples."""

import csv
import itertools
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def write_csv(name, fields, rows):
    with (ROOT / name).open("w", newline="", encoding="utf-8") as f:
        out = csv.writer(f)
        out.writerow(fields)
        out.writerows(rows)


def ols_slope(points):
    xbar = sum(x for x, y in points) / len(points)
    ybar = sum(y for x, y in points) / len(points)
    slope = sum((x - xbar) * (y - ybar) for x, y in points) / sum(
        (x - xbar) ** 2 for x, y in points
    )
    return {"intercept": ybar - slope * xbar, "slope": slope}


def shares(utilities):
    weights = {key: math.exp(val) for key, val in utilities.items()}
    return {key: weight / sum(weights.values()) for key, weight in weights.items()}
```

Python source: [m01_synthetic.py](../../03_Data_and_Code/Lecture_Examples/m01_synthetic.py). From its directory, run `python m01_synthetic.py`.

```python
"""Synthetic numerical examples for M1; run from any working directory."""

import itertools
import json
import math
from example_helpers import write_csv, ols_slope, shares

r = {}
lines = [("O1", "C1", 2, 10), ("O1", "C1", 1, 5), ("O2", "C2", 3, 4)]
write_csv(
    "M01_order_lines_synthetic.csv",
    ["order_id", "customer_id", "quantity", "unit_price_dollars"],
    lines,
)
orders = {}
for order, customer, qty, price in lines:
    orders[order] = orders.get(order, 0) + qty * price
r["M01"] = {
    "revenue": sum(orders.values()),
    "order_count": len(orders),
    "average_order_value": sum(orders.values()) / len(orders),
    "average_line_revenue": sum(orders.values()) / len(lines),
    "renewal_incremental_value_A": 100 * (0.91 - 0.90) - 3,
    "renewal_incremental_value_B": 100 * (0.50 - 0.40) - 3,
}
assert orders == {"O1": 25, "O2": 12}
print(json.dumps(r, indent=2))
```

## 1.10 mHealth: A Verifiable Monthly Business Review

\noindent An mHealth manager needs to decide whether a decline in food entries warrants attention to customer engagement. Entry counts combine the number of eligible customers, the length of the reporting month, the frequency of logging, and the intensity of logging on observed days. A decline can arise from any of these components. The comparison becomes interpretable when the eligible population is fixed before the reporting periods and every component has an explicit denominator.

Define the population as users in the teaching cohort with at least one observed day before May 1, 2016. All members remain in the May and June denominators, including those with no logs in a month. A missing day contributes zero to the indicator for an observed log; its food consumption remains unobserved. For month $t$, the number of entries satisfies the accounting identity

$$
L_t=N D_t p_t a_t,
$$

where $N$ is the fixed number of eligible users, $D_t$ is calendar days in the month, $p_t$ is observed user-days divided by $ND_t$, and $a_t$ is entries per observed user-day. The identity separates calendar exposure from logging behavior. It uses counts of records, with no assumption that an entry represents a purchase or a complete meal.

| Quantity | May | June |
| --- | ---: | ---: |
| Eligible Users | 340 | 340 |
| Calendar User-Days | 10,540 | 10,200 |
| Observed User-Days | 7,082 | 6,331 |
| Observed Logging Fraction | 0.6719 | 0.6207 |
| Entries per Observed Day | 11.7995 | 11.6910 |
| Food Entries | 83,564 | 74,016 |

The table identifies a 5.12 percentage-point decline in the logging fraction, alongside a shorter month and a modest decline in entries per observed day. Changing the denominator to users who happened to log during June would remove inactive members from the comparison. The fixed-population result supports investigation of engagement, recording practices, and seasonality. It supplies no estimate of a campaign effect or change in nutrition.

An AI-assisted business review should retrieve numerical claims from a computed evidence file. The file below records the source checksum, membership rule, observation unit, month, numerator, and denominator. A useful coding request is: “Construct the fixed cohort before May, count distinct user-dates, retain members with zero logs, and verify the accounting identity separately for each month.” The independent calculation must finish before an assistant writes the managerial explanation.

The [claude-ecom reference](https://github.com/takechanman1228/claude-ecom) separates numerical computation from a narrative layer for ecommerce reviews. The mHealth calculation applies that separation to logging data. Its descriptive evidence file also supplies the structured-claim checks in M8.

Python source: [reporting.py](../../03_Data_and_Code/mHealth/recurring_examples/reporting.py). From its directory, run `python reporting.py`.

```python
"""Compute a verifiable, fixed-cohort mHealth business review locally."""

import json
import pandas as pd
from common import ROOT, load_food, save_result


def monthly_review(food):
    # Fix membership before either reporting month; retain zero-log users.
    members = sorted(food.loc[food.date < "2016-05-01", "Userid"].unique())
    rows = []
    for month in ["2016-05", "2016-06"]:
        period = pd.Period(month, freq="M")
        part = food.loc[
            food.Userid.isin(members) & food.date.dt.to_period("M").eq(period)
        ]
        days = part[["Userid", "date"]].drop_duplicates()
        denominator = len(members) * period.days_in_month
        assert len(days) <= denominator
        rows.append(
            {
                "period": month,
                "eligible_users": len(members),
                "calendar_user_days": denominator,
                "observed_user_days": len(days),
                "users_with_logs": int(days.Userid.nunique()),
                "food_entries": len(part),
                "logging_fraction": len(days) / denominator,
                "entries_per_observed_day": len(part) / len(days),
            }
        )
    manifest = json.loads((ROOT.parent / "manifest.json").read_text())
    return {
        "source_sha256": manifest["files"]["food_entries.csv.gz"]["sha256"],
        "membership": "At least one observed day before 2016-05-01",
        "unit": "eligible user-calendar-day",
        "metric": "logging_fraction",
        "interpretation": "descriptive",
        "periods": rows,
    }


if __name__ == "__main__":
    result = monthly_review(load_food())
    save_result("reporting", result)
    print(json.dumps(result, indent=2))
```

## 1.11 Customer Data and the Coding Environment

\noindent A marketing team deciding whom to contact needs a defined set of customer information. Additional fields can increase exposure without improving the decision. Begin with the unit of analysis, the intended calculation, and the information available before contact. A transaction date can be necessary for a forecasting split; a customer's name usually contributes nothing to that split. A reproducible pipeline should make these distinctions visible in its input schema.

An AI coding tool can receive information through prompts, uploaded files, logs, screenshots, or repository access. Generate and debug a transformation using a small synthetic table when real records are unnecessary. Before using actual records, establish whether that environment is authorized for those fields and that purpose. An assistant's ability to read a file does not establish the firm's authority to transmit it. Access, processing location, retention, and permitted uses belong to the specification of the work.

The mHealth exercises provide a concrete comparison. Ages and perturbed weights support selected teaching calculations, while exact birthdays are unnecessary. Replacing identifiers and perturbing one measurement do not establish anonymity for every possible linkage. A useful implementation loads the minimum required columns, avoids printing individual histories into logs, and publishes aggregate results with their denominators. Students can inspect generated code for file uploads, external API calls, and unnecessary exports before running it. These checks concern observable data flows and preserve the ability to reproduce the local analysis.

## 1.12 A Failed Analysis Can Require Different Evidence

\noindent A manager commissioning an AI-assisted analysis must choose what to change when the answer remains unreliable. A wrong join requires a correction to the program. A missing observation requires an information decision. A poorly defined target requires a clearer managerial question. These diagnoses lead to different uses of time and money, even when all three failures initially appear as an unsatisfactory answer from the same assistant.

The mHealth records make the distinction concrete. Repeated daily totals can be counted once using the user-day key, and a join can preserve the intended cohort. Those changes improve calculations on recorded information. Food consumed without a corresponding log remains unobserved. Estimating total consumption would require additional measurement or assumptions linking logging to consumption. An analysis of recorded food categories can instead proceed with its population and outcome stated explicitly.

| Difficulty | Useful Response | Evidence of Resolution |
| --- | --- | --- |
| Daily totals are repeated across food entries | Correct aggregation at the user-day level | Reconcile one day by hand and compare totals |
| An item description maps to several categories | Obtain a reference label or retain the ambiguity | Evaluate separately adjudicated descriptions |
| Food consumption was never recorded | Collect additional evidence or define a recorded-behavior outcome | Check the measurement process and stated population |
| A coupon model predicts response but the decision requires incrementality | Establish an untreated comparison | Evaluate assignment and contribution over a common horizon |

A useful request to a coding assistant states the decision, the unresolved distinction, and the smallest check that could resolve it. For example: "Construct one row per observed user-day, retain unmatched daily records, and reconcile item calories with one copy of the daily total. Identify which conclusions would additionally require unrecorded consumption." The request gives the assistant a verifiable task while keeping the missing-information question visible.

An alternative procedure can also remove a costly intermediate step. If a campaign decision requires category totals, a validated category aggregation may avoid generating individual prose summaries that nobody uses. The required customer protections and analytical meaning remain fixed. Simplification is valuable when the resulting output still answers the decision and passes its checks. Reusable functions then become investments whose subsequent benefits and maintenance costs can be compared, as in M8, Section 8.17.

## 1.13 Model Versions and the Scope of an AI Claim

\noindent A marketing team considering an AI coding service needs to know which tasks it performs reliably in the intended workflow. The statement that a model can produce correct Python leaves several economically relevant conditions unspecified. A script may solve a calculation after manual repair while failing the team's automated parser. It may pass familiar examples while mishandling a new customer identifier or a changed data schema. These outcomes imply different verification costs and different feasible uses.

[Chen, Zaharia, and Zou (2024)](https://hdsr.mitpress.mit.edu/pub/y95zitmz/release/2), Section 3.5, distinguish directly executable outputs from correctness after removing surrounding noncode text. Their March and June 2023 comparisons show why the interface around generated code belongs in the evaluation. A claim about a particular historical configuration provides evidence about that configuration. Transferring it to a replacement requires a comparison on the relevant tasks.

A reproducible claim specifies the model identifier and evaluation date, system and user prompts, tools, reasoning and sampling settings, token or cost budget, input version, parsing rule, scoring rule, and denominator. For an mHealth aggregation, the output contract could require one row per user-month, preservation of users with no recorded entries, and reconciliation to independently calculated totals. For earnings-call extraction, it could require the complete relevant passage and a distinction between a stated plan and an implemented policy. These requirements remain meaningful when the model changes.

Retain a fixed set of known failure cases to detect regressions and a separate supply of fresh cases to assess transfer. [LiveBench](https://arxiv.org/abs/2406.19314v2) and [LiveCodeBench](https://arxiv.org/abs/2403.07974v2) motivate refreshed evaluation with objective scoring. New cases should preserve the target task mix or report its changes explicitly. Repeated tuning against the same public answers consumes their value as fresh evidence. Revalidation is warranted after changes to the model, prompt, tool, scorer, schema, or supported customer population.

\noindent A model change can alter the behavior of dependent components even when its own reference score improves. M7 §§7.31–7.32 separate draft-token verification, answer correctness, and request resolution. Record target and drafter versions, generation settings, and the complete attempted-request roster before comparing an updated assistant.

## 1.14 Specifications, Independent Checks, and Retained Skills

\noindent A manager who delegates a customer analysis must still define the decision, the observation unit, and the evidence that would justify action. Before requesting code, write the required inputs, transformation, output, and a small calculation that can be checked independently. If the objective is retention, specify the starting cohort and horizon. If it is an incremental marketing effect, specify the treatment comparison and assignment process. A working program can faithfully implement an unsuitable target.

Compare anonymous outputs using criteria fixed before inspecting their style. Reopen the saved artifact, run the calculation, and inspect the result that matters for the decision. An assistant's statement that it completed a task supplies a claim to verify. A check against independently calculated totals supplies additional evidence. Record both execution time and correction effort when comparing workflows.

After assisted work, explain the analytical choice and solve a new small instance without the assistant. This establishes whether the relevant skill can be demonstrated at that moment. A long-term claim about learning requires repeated assessment and a suitable comparison. [Stanford CS193T's AI Foundations activity](https://web.stanford.edu/class/archive/cs/cs193t/cs193t.1272/assignments/1-ai-foundations/) motivates explicit decisions about which skills to preserve; the [coding-agent activity](https://web.stanford.edu/class/archive/cs/cs193t/cs193t.1272/assignments/6-coding-agents/) connects a working result to a documented failure or unchecked component. The source and grader calculations in Sections 5.19 and 5.20 provide hand-checkable instances.


## 1.15 Reproducible Calculations and Product Recommendations

\noindent A product manager deciding which concepts warrant human research needs to understand how an analyst constructed the reported preference scores. A second analyst may reproduce every number and still interpret the recommendation incorrectly if the report leaves its weights or population unclear. The synthetic refill example makes this distinction visible. Two invented personas have Set 1 expected ratings of 4.25 and 3.70 on categories one through five. Persona p01 contributes two identical responses, while persona p02 contributes one. These are authored responses with imposed similarities; no person or language model produced them in an observed study.

Giving each persona equal weight yields $(4.25+3.70)/2=3.975$. Giving each response row equal weight yields $(2\times4.25+3.70)/3=4.066667$. Both calculations are reproducible, but they answer different questions. The first treats the two personas as equally represented. The second gives the persona with more responses a larger share of the result. Repeating an identical response changes that share without changing either persona's preference. The observation unit and intended weighting therefore belong beside the number in a managerial report.

![Identical responses raise the row-weighted mean while both persona ratings remain fixed. The equal-persona mean stays at 3.975 as p01 repeats increase from one to five and p02 supplies one response.](../figures/M01_repeat_weights.png)

With five identical p01 responses and one p02 response, the row-weighted mean reaches 4.158333. The equal-persona mean remains 3.975. A figure whose horizontal axis counts responses and whose vertical axis reports ratings makes the changed composition explicit. The increasing series describes an imposed weighting effect; it supplies no evidence of preference change or additional independent information.

A separate six-concept construction compares pooled and reversed rating patterns against invented reference counts. The pooled pattern gives every concept the same mean, so correlation and a unique shortlist remain undefined. The reversed pattern selects F and E and retains zero of the reference top two, A and B. An assistant that turns the pooled result into a launch recommendation has added unsupported meaning even if it quotes the distribution score correctly. Both candidate patterns use reference outcomes in their construction. A human study with separate development and evaluation concepts would be needed to assess performance on new concepts.

### 1.15.1 A Report with Traceable Numerical Evidence

\noindent Recomputing a table can reveal that the saved result no longer matches its inputs or program. The program below imports the complete mapping and screening functions in Sections 5.23 and 4.23, recomputes four saved tables, and stops if any table disagrees. It writes a short recommendation and a JSON evidence file containing the sample counts, quantities, missing values, and hashes of the inputs and calculation files. Independent arithmetic establishes the reference values above. Agreement between a saved table and the program that created it supplies a separate consistency check.

Keep the two example folders together within the course checkout. Paths resolve from the program's location, so changing the terminal directory does not change which inputs it reads. The output option adjusts relative links when the report moves. A reader can follow the recommendation to its evidence file, source program, data dictionary, inputs, and figure. Record the Python version and command when rerunning it. The script uses only the standard library and makes no network or model calls.

Python source: [reproduce_recommendation.py](../../03_Data_and_Code/Reproducible_Recommendations/reproduce_recommendation.py). From the course root, run `python3 03_Data_and_Code/Reproducible_Recommendations/reproduce_recommendation.py`. From its folder, run `python3 reproduce_recommendation.py`.

```python
"""Recompute a synthetic recommendation and retain its numerical evidence.

Python 3.10+, standard library. No network, model, or editor calls.
The two input constructions are separate; all personas and panels are invented.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parent / "Synthetic_Consumers"
sys.path.insert(0, str(SOURCE))
from anchor_measurement import score_responses, summarize
from concept_screening import evaluate


def load(path):
    return json.loads(path.read_text())


def calculate(source=SOURCE):
    records = score_responses(load(source / "data/anchor_responses.json"))
    concepts = summarize(records)
    screening, details = evaluate(load(source / "data/concept_panels.json"))
    computed = dict(response_ratings=records, concept_ratings=concepts,
                    screening_summary=screening, screening_details=details)
    for name, value in computed.items():
        if load(source / f"results/{name}.json") != value:
            raise ValueError(f"Saved {name} disagrees with a fresh calculation.")
    refill = next(r for r in concepts
                  if r["concept"] == "refill" and r["anchor_set"] == "set_1")
    first = next(r for r in records if r["concept"] == "refill"
                 and r["persona"] == "p01" and r["repeat"] == 1
                 and r["anchor_set"] == "set_1")
    second = next(r for r in records if r["concept"] == "refill"
                  and r["persona"] == "p02" and r["anchor_set"] == "set_1")
    # Hold each persona's rating fixed and vary p01's identical repeat count.
    sensitivity = [dict(p01_repeats=n, p02_repeats=1,
        equal_persona_mean=(first["mean_rating"] + second["mean_rating"]) / 2,
        equal_row_mean=(n * first["mean_rating"] + second["mean_rating"]) / (n + 1))
        for n in range(1, 6)]
    tracked = [source / "data/anchor_responses.json",
               source / "data/concept_panels.json",
               SOURCE / "anchor_measurement.py", SOURCE / "concept_screening.py",
               ROOT / "reproduce_recommendation.py"]
    return dict(scope="Entirely synthetic; no model or customer observations",
        response_mean=first["mean_rating"], response_distribution=first["distribution"],
        equal_persona_mean=refill["mean_rating"],
        equal_row_mean=refill["row_weighted_mean"],
        response_rows=refill["response_rows"], personas=refill["personas"],
        repeat_sensitivity=sensitivity, screening=screening,
        sha256={p.parent.name + "/" + p.name:
                hashlib.sha256(p.read_bytes()).hexdigest() for p in tracked})


def write_report(result, output):
    output.mkdir(parents=True, exist_ok=True)
    (output / "evidence.json").write_text(
        json.dumps(result, indent=2, allow_nan=False) + "\n")
    link = lambda path: Path(os.path.relpath(path, output)).as_posix()
    rows = {r["candidate"]: r for r in result["screening"]}
    selected = lambda row: ("unresolved" if row["selected"] is None
                            else ", ".join(row["selected"]))
    pooled, reversed_row = rows["pooled"], rows["reversed"]
    correlation = ("undefined" if pooled["pearson"] is None
                   else f"{pooled['pearson']:.3f}")
    recall = ("undefined" if reversed_row["top_two_recall"] is None
              else f"{reversed_row['top_two_recall']:.0%}")
    lines = ["# Product-Screening Recommendation", "", "By Nathan Yang", "",
        "A product manager must decide which concepts warrant human research. "
        "All inputs below are invented. No model calls or customer study took place.", "",
        "## Response Weights", "",
        f"The refill example has {result['response_rows']} response rows from "
        f"{result['personas']} personas. Equal persona weights give "
        f"{result['equal_persona_mean']:.3f}; equal row weights give "
        f"{result['equal_row_mean']:.6f} on a five-category rating scale.", "",
        "Persona p01's first response has the following imposed category weights.", "",
        "| Rating | Weight |", "| --- | --- |"]
    lines += [f"| {k} | {p:.2f} |"
              for k, p in enumerate(result["response_distribution"], 1)]
    lines += ["", rf"The expected rating is $\sum_{{k=1}}^{{5}}k p_k={result['response_mean']:.2f}$.", "",
        "![Identical repeats raise the row mean while the persona mean stays fixed]("
        + link(ROOT.parents[1] / "06_Lecture_Notes/figures/M01_repeat_weights.png") + ")", "",
        "## Concept Selection", "",
        f"A separate construction compares {pooled['concepts']} invented concepts "
        "with an invented reference panel. The pooled pattern's shortlist is "
        f"{selected(pooled)} and its correlation is {correlation}. "
        f"The reversed pattern selects {selected(reversed_row)}. Its recall of "
        f"the reference top two ({', '.join(reversed_row['reference_top_two'])}) "
        f"is {recall}.", "",
        "These patterns use reference outcomes in their construction. Their results "
        "justify checking ranking errors before funding a human study. They supply "
        "no evidence of actual purchase demand or out-of-sample performance.", "",
        "An assumed research budget of \\$500 and an assumed incentive of \\$25 "
        "per participant allow 20 incentives before recruitment and operating costs. "
        "This arithmetic does not determine an adequate study size.", "",
        "## Reproduction", "",
        "[Numerical evidence](evidence.json) | [Full Python]("
        + link(ROOT / "reproduce_recommendation.py") + ") | [Data dictionary]("
        + link(SOURCE / "DATA_DICTIONARY.md") + ")", "",
        "[Response inputs](" + link(SOURCE / "data/anchor_responses.json")
        + ") | [Concept inputs](" + link(SOURCE / "data/concept_panels.json") + ")", "",
        "From the course root: `python3 "
        "03_Data_and_Code/Reproducible_Recommendations/reproduce_recommendation.py`.", ""]
    (output / "recommendation.md").write_text("\n".join(lines))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "results")
    args = parser.parse_args()
    write_report(calculate(), args.output.resolve())
    print("Recomputed four saved tables and wrote evidence.json and recommendation.md.")
```

### 1.15.2 The Meaning of a Successful Check

\noindent A calculation check establishes a numerical property under the specified inputs and rules. A file hash establishes identity. Neither establishes that invented personas represent actual customers. Review an AI-written interpretation against the observation unit, weighting rule, uncertainty, and proposed action. Preserve undefined values as missing; replacing an unresolved shortlist with an arbitrary alphabetical order would turn an implementation convention into a substantive recommendation.

A file conversion also requires its own checks. The report contains currency, a mathematical expression, a table, and a linked figure. Reopen the exported document and verify their meaning and destinations. The inspected [Suzuri 0.7.0 source](https://github.com/harrywang/suzuri/blob/88f58aae544bdc60d5068e7b5d40a05ca7f1a564/crates/markdown_export/src/preprocess.rs) converts internal wikilinks to display text and records missing note embeds separately from conversion success. These behaviors explain why an export can finish while navigation or content remains incomplete. Standard relative links, explicit missing-file checks, and inspection of the final document address those questions. The [optional exercise](../../07_Labs/Reproducible_Recommendations/README.md) distinguishes reproducible course calculations from editor-specific tests.

## 1.16 Definitions, Inference, and Evidence

\noindent A subscription manager asks an AI assistant for a cancellation rate and unresolved requests. Define the customer, subscription, request, and completed cancellation before counting them. A request records a communicated intention; a confirmation records a claimed state transition. Equating these events can raise the reported completion rate and remove unresolved requests from the service queue.

An ontology specifies classes of objects, relationships among them, and rules that support additional statements. An account is an object; a particular cancellation request is another object related to a subscription and a time. A class such as CancellationRequest can be a subclass of ServiceRecord. Assigning an event to the first class then supports membership in the second. A data dictionary supplies names and units, while an ontology adds relationships and their implications. Both depend on substantive decisions about what the records mean.

The [W3C OWL 2 Primer](https://www.w3.org/TR/owl2-primer/) distinguishes inference from the absence of information. A domain axiom saying that the subject of `requestedBy` is a CancellationRequest lets a reasoner infer that type when it encounters the relationship. It need not reject a row that lacks an explicit type. Under an open-world interpretation, a missing confirmation can remain unknown. A rule searching a supplied table for requests without confirmations answers a narrower operational question about the available records.

Data validation instead asks whether the supplied information satisfies specified requirements. A timestamp requirement can reject a missing value before applying a reporting cutoff. A confirmation can be checked for a matching subscription and a time no earlier than its request. [SHACL](https://www.w3.org/TR/shacl/) provides a standard for expressing graph-validation conditions. Logical inference, validation, and source verification answer different questions. A logically consistent set of false statements remains consistent; an inconsistent classification can reflect an inappropriate axiom or an erroneous observation.

![Cancellation evidence separates event classification, checks on records, and a review decision. A request without an accepted confirmation remains in the review queue.](../figures/M01_cancellation_evidence.png)

The [Ontology Playground](https://learn-ontology.vercel.app/#learn) uses short prediction-and-trace exercises to make rule implications visible. For a marketing application, state an expected inference, inspect the facts and rules that produce it, and then challenge their empirical justification. The complete cancellation calculation in §2.25 preserves the reporting population, exclusion reasons, and observation times. Successful code execution establishes that the implemented calculation ran. Whether the calculation represents the intended commercial event requires those additional checks.

Predicted acceptance does not establish permission. Preserve the source, time, scope, and withdrawal conditions of permission records independently of inferred preferences. Section 9.19 connects these distinctions to the justification of a firm's conduct.

## 1.17 Information, Tools, and a Verified Analysis

\noindent A manager considering customer outreach first needs a measure of recorded activity. A coding assistant can produce a plausible table while counting food entries as days, omitting customers with no later records, or including observations beyond the reporting window. Each error changes the population or quantity relevant to the decision. Supplying a model with a clear question begins the analysis; the files it can inspect, operations it can perform, and checks it receives also affect the result.

An agent harness is the execution system surrounding a model. Its components include tools, task context, state retained between steps, resource limits, execution records, verification, and permissions. Li and coauthors' [survey](../../01_Resources/35_Agent_Workflow_Evaluation/README.md), especially §§5 and 8, connects these components to reproducible evaluation. A useful implementation stores the current task definition and input versions, executes small changes, and retains evidence of their results. A progress note that says a calculation passed should link to the calculation and its output. After a reset or interruption, the assistant can then recover the relevant state without treating its earlier assertion as proof.

The recurring mHealth task fixes eligibility using food records from January through June 2016 within the established pseudonym-selected cohort. The resulting roster contains 358 users. July activity counts distinct dates from July 1 inclusive to August 1 exclusive. Every roster user receives 31 possible days. The source contains no account-enrollment registry; eligibility means observed earlier in this released file. A zero for July means no recorded food-log day in that window. It supplies no measurement of food intake on the missing days.

| Quantity | July Development Task | August Evaluation Task |
| --- | ---: | ---: |
| Earlier-period roster users | 358 | 358 |
| Calendar days per user | 31 | 31 |
| Possible user-days | 11,098 | 11,098 |
| Recorded user-days | 6,455 | 6,501 |
| Users with no recorded days | 39 | 41 |
| Mean recorded logging rate | 58.16% | 58.58% |

The mean gives each roster user equal weight. The inputs include observed boundary dates immediately before and after the target interval. Excluding those dates and collapsing repeated dates are separate operations. An inner join to July records would omit the zero-log users and change the target to activity conditional on having a July record. Retaining the roster before counting preserves the intended comparison.

### 1.17.1 Information and Feedback as Separate Choices

\noindent A controlled comparison can vary a structured data dictionary and independent development feedback while holding the model and analytical target fixed. All four configurations receive the core measurement request, output schema, input files, execution tools, permissions, and resource caps. The information condition adds organized definitions of units, eligibility, boundaries, and missingness. The feedback condition returns discrepancies from a separate development checker and permits at most two corrections within the common budget. An improvement in either condition is an empirical question.

![A two-by-two design holds the model, task, tools, permissions, and resource caps fixed while crossing explicit measurement information with development-check feedback.](../figures/M01_workflow_design.png)

Use fresh conversations and clean output directories for repeated runs. Preserve the prompt, model version, visible file list, commands, feedback, revisions, and final output. Develop with July and score a frozen program on August. The [experiment protocol](../../03_Data_and_Code/Agent_Workflows/EXPERIMENT_PROTOCOL.md) separates the public reference files from the files exposed to the assistant during a measured run. An exported report can describe the result; the saved inputs and executable calculation establish what was computed.

### 1.17.2 Reproduce the Logging Tasks

\noindent The task builder verifies the compressed public source checksum, selects the earlier roster, assigns stable aliases, and exports only user-day counts and timing metadata. Compact inputs are included in the repository. Rebuilding them requires the mHealth release in its documented local data folder. The following program uses Python's standard library and makes no model calls.

The source count is food rows per user-date. The task interval later determines which observed dates contribute to logging activity.

Python source: [build_tasks.py](../../03_Data_and_Code/Agent_Workflows/build_tasks.py). From the repository root:

```sh
cd 03_Data_and_Code/Agent_Workflows
python3 build_tasks.py
```

```python
"""Construct small, reproducible tasks from the released mHealth food file."""
import csv
import gzip
import hashlib
import json
from collections import Counter
from datetime import date, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / "mHealth"


def digest(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def write_csv(path, fields, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main():
    source = SOURCE / "data/food_entries.csv.gz"
    release = json.loads((SOURCE / "manifest.json").read_text())
    expected = release["files"][source.name]["sha256"]
    if digest(source) != expected:
        raise ValueError("The mHealth release checksum differs.")
    prior_users, counts = set(), Counter()
    with gzip.open(source, "rt", newline="") as stream:
        for row in csv.DictReader(stream):
            user = row["Userid"]
            if int(user[1:5], 16) >= 4096:
                continue
            day = date.fromisoformat(row["Fancydate"][:10])
            if date(2016, 1, 1) <= day < date(2016, 7, 1):
                prior_users.add(user)
            if date(2016, 6, 30) <= day <= date(2016, 9, 1):
                counts[user, day] += 1
    # Eligibility is fixed using January-June records for both later tasks.
    aliases = {u: f"U{i:04d}" for i, u in enumerate(sorted(prior_users), 1)}
    tasks = []
    for month, role in [(7, "development"), (8, "evaluation")]:
        start, end = date(2016, month, 1), date(2016, month + 1, 1)
        task = HERE / "tasks" / role
        spec = {"task_id": role, "start": str(start), "end_exclusive": str(end),
                "eligibility_cutoff_exclusive": "2016-07-01"}
        write_csv(task / "roster.csv", ["user_id"],
                  ({"user_id": u} for u in aliases.values()))
        records = [{"user_id": aliases[u], "date": str(d), "entries": n}
                   for (u, d), n in sorted(counts.items())
                   if u in aliases and start - timedelta(days=1) <= d <= end]
        write_csv(task / "observed_days.csv", ["user_id", "date", "entries"], records)
        (task / "task.json").write_text(json.dumps(spec, indent=2) + "\n")
        tasks.append({**spec, "roster_users": len(aliases), "input_rows": len(records)})
    inputs = sorted((HERE / "tasks").glob("*/*"))
    manifest = {"source": "mHealth teaching release 2026-10-23",
                "source_sha256": expected, "selection": "Pseudonym prefix below 4096; observed January-June 2016",
                "unit": "Observed user-day; entries counts source food rows",
                "tasks": tasks, "model_calls": 0,
                "files": {str(p.relative_to(HERE)): digest(p) for p in inputs}}
    (HERE / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps(tasks, indent=2))


if __name__ == "__main__":
    main()
```

The reference calculation starts with every roster user and collects a set of eligible dates. A separate SQL calculation verifies the same customer-level counts. The generated JSON preserves the denominators and excluded input-row counts.

Python source: [logging_reference.py](../../03_Data_and_Code/Agent_Workflows/logging_reference.py). From the repository root:

```sh
cd 03_Data_and_Code/Agent_Workflows
python3 logging_reference.py
```

```python
"""Calculate observed logging days for a fixed earlier-period roster."""
import csv
import json
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent


def read_csv(path):
    with path.open(newline="") as stream:
        return list(csv.DictReader(stream))


def calculate(roster, records, start, end):
    users = [row["user_id"] for row in roster]
    if not users or len(users) != len(set(users)):
        raise ValueError("The roster must be nonempty with one row per user.")
    days = (end - start).days
    if days <= 0:
        raise ValueError("The end must follow the start.")
    observed = {u: set() for u in users}
    excluded_rows = 0
    for row in records:
        d = date.fromisoformat(row["date"])
        if row["user_id"] not in observed or not start <= d < end:
            excluded_rows += 1
            continue
        # Multiple entries and repeated rows still represent one logged day.
        observed[row["user_id"]].add(d)
    rows = [{"user_id": u, "logged_days": len(observed[u]), "window_days": days,
             "logging_rate": len(observed[u]) / days} for u in users]
    total = sum(r["logged_days"] for r in rows)
    summary = {"roster_users": len(users), "window_days": days,
               "observed_user_days": total, "possible_user_days": len(users) * days,
               "zero_log_users": sum(r["logged_days"] == 0 for r in rows),
               "mean_logging_rate": total / (len(users) * days),
               "excluded_input_rows": excluded_rows}
    return rows, summary


def main():
    output = HERE / "results"
    output.mkdir(exist_ok=True)
    summaries = {}
    for role in ["development", "evaluation"]:
        task = HERE / "tasks" / role
        spec = json.loads((task / "task.json").read_text())
        rows, summary = calculate(read_csv(task / "roster.csv"),
                                  read_csv(task / "observed_days.csv"),
                                  date.fromisoformat(spec["start"]),
                                  date.fromisoformat(spec["end_exclusive"]))
        with (output / f"{role}_reference.csv").open("w", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)
        summaries[role] = summary
    (output / "logging_summary.json").write_text(json.dumps(summaries, indent=2) + "\n")
    print(json.dumps(summaries, indent=2))


if __name__ == "__main__":
    main()
```


## 1.18 Statistical Evidence in an AI-Generated Analysis

\noindent A manager considering a promotion needs an estimate of incremental contribution and an account of its uncertainty. An assistant can produce executable code, a small p-value, and a confident recommendation while treating transactions from the same store as independent observations. The program's successful completion establishes that its instructions ran. The statistical argument also depends on the assignment process, the observation unit, and the relationship between the computed quantity and the manager's question.

[Miao, Mu, Chen, and Zou's Fisher-R1 study](https://arxiv.org/abs/2608.07437) evaluates agents on open-ended hypothesis-testing tasks. On its difficult tasks, Fisher-R1-14B matches the reference reject/nonreject decision in 65.8% of single attempts. Requiring a sufficiently close reference p-value reduces this score to 33.0%. These percentages measure agreement with benchmark answers. A false-positive rate instead requires repeated tests when the null hypothesis is true, as in the store experiment in Section 6.30.

An analysis request should define the population, intervention or comparison, outcome, units, and available information. For an experiment, specify how treatment was assigned. For repeated customer records, identify which observations belong to the same person. Ask the assistant to report the retained sample, estimate, uncertainty calculation, test direction, significance level, and interpretation. Compare its reported quantities with saved numerical output and inspect the code that created the sample and standard error.

| Assessment | Evidence to Examine |
| --- | --- |
| Execution | The program finishes on the stated inputs and records its outputs. |
| Statistical method | The estimand, assignment or sampling unit, dependence, and test match the question. |
| Numerical reporting | Estimates, intervals, p-values, and decisions agree with the executed calculation. |
| Managerial interpretation | Effect size, costs, customer outcomes, and the scope of the evidence support the action. |

Matching a reference number can coexist with an unsuitable explanation or an unsupported causal claim. A reference analysis also needs justification. Several procedures can answer related questions with different p-values, and an influential observation does not by itself determine which question the firm should ask. A mean-dollar effect and a rank-order association concern different economic quantities. Choose the target and defensible handling rules before using a favorable result to select the method.

For the [statistical inference exercise](../../07_Labs/Statistical_Inference/README.md), preserve the assistant's initial analysis and written rationale before giving feedback. Check the mHealth sample and uncertainty independently, then evaluate a frozen procedure on newly generated store experiments. Record model and software versions when an assistant is used. The supplied reference programs establish the course calculations; measured AI performance requires actual recorded runs under the stated protocol.

## 1.19 Execution Feedback and Hidden Coding Errors

\noindent A marketing analyst commissions a script to estimate a campaign's incremental contribution. The requested sample, estimator, and uncertainty calculation can be specified before any code is written. The analyst still needs to decide how much execution, revision, and independent checking to include in the workflow. An error message makes a failed calculation visible. A plausible table can leave an incorrect calculation undiscovered.

[Galiani, López, and Sosa](../../01_Resources/40_Econometric_Coding_Workflows/README.md) compare these workflow choices using 40 tasks and 32 simulated datasets. Their November 2026 study evaluates six models in Stata, R, and Python, with two prompt conditions and ten repetitions of every combination. Each of the three workflows has 14,400 assigned runs. The task specifies the method and requested quantities. Numerical success means agreement with the reference calculation under the study's scoring rules.

| Workflow | Successful Runs | Success | Loud Failures | Silent Failures |
| --- | ---: | ---: | ---: | ---: |
| One-Script Chatbot | 12,052 | 83.69% | 1,694 | 654 |
| Self-Repair | 13,434 | 93.29% | 167 | 799 |
| Constrained Agent | 14,021 | 97.37% | 41 | 338 |

The chatbot supplies one script. Self-repair receives execution errors or missing-output feedback and can revise up to three times. The agent runs and revises its own code, chooses when to stop, and receives an explicit instruction to perform an independent numerical check. The agent comparison therefore includes a change in verification instructions as well as execution and revision. These rates describe implementation of a specified method; selecting the appropriate causal design remains a separate judgment.

A loud failure means failed execution or incomplete requested output. A silent failure means complete output with at least one incorrect scored value. Agent silent failures account for 338 of 14,400 runs, or 2.35%. They also account for 338 of 379 failures, or 89.18%. The first fraction measures their frequency among commissioned analyses. The second describes the errors that remain after the workflow has removed most visible failures.

![Published coding results use 14,400 assigned runs per workflow. Loud failures fall from 11.76 to 0.28 per 100 runs and silent failures from 4.54 to 2.35; silent failures rise from 27.85% to 89.18% of all failures. The two panels use different denominators. Intervals are the authors' task-cluster bootstrap intervals.](../figures/M01_coding_failure_denominators.png)

Self-repair returns more complete results while its silent-failure count rises. A repaired program can proceed far enough to reveal an incorrect calculation that an earlier execution failure concealed. This change does not imply that already-correct programs became wrong. Reviewing the initial and final scripts is necessary to distinguish those paths.

For a logging report, the specification should identify the earlier-period roster, distinct user-day unit, calendar boundaries, and treatment of users without records. For a campaign regression, it should identify the outcome units, assignment unit, included observations, estimator, and uncertainty convention. A successful run supports the claim that instructions executed. Independent calculations and deliberately incorrect alternatives provide evidence about whether those instructions implement the intended quantity. Section 7.46 applies these checks to the mHealth roster.

### 1.19.1 Reconstruct the Published Comparison

\noindent The three input tables are published aggregate records from the authors' v1.2 release. The program below reconstructs failure denominators, prompt contrasts, and model-specific incremental token costs. It reconciles prompt-cell success counts with the workflow totals. The reported intervals retain the authors' resampling of 40 tasks; the program does not treat individual runs as independent or recompute those intervals. No new model performance is measured.

Run `python3 03_Data_and_Code/Agent_Workflows/benchmark_evidence.py` from the repository root. The program reads the three small CSV files in `01_Resources/40_Econometric_Coding_Workflows/data` and writes its results beside the existing workflow examples. The plotted intervals and reconstructed point values are traceable to those files.

Python source: [benchmark_evidence.py](../../03_Data_and_Code/Agent_Workflows/benchmark_evidence.py)

```python
"""Recompute published aggregates; no model calls or upstream code execution."""
import csv
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parents[1] / "01_Resources/40_Econometric_Coding_Workflows/data"
ORDER = ["chatbot", "self_repair", "agent"]


def read_csv(path):
    with path.open(newline="") as stream:
        return list(csv.DictReader(stream))


def failure_rates(rows):
    result = []
    for row in rows:
        n, failed, loud, silent = (int(row[k]) for k in ["n", "failures", "loud", "silent"])
        if n <= 0 or min(loud, silent) < 0 or failed != loud + silent or failed > n:
            raise ValueError("Failure counts must partition a positive assigned-run denominator.")
        result.append({"agency": row["agency"], "assigned": n, "successes": n - failed,
                       "failures": failed, "loud": loud, "silent": silent,
                       "success_pct": 100 * (n - failed) / n,
                       "loud_per100": 100 * loud / n, "silent_per100": 100 * silent / n,
                       "silent_share_of_failures_pct": 100 * silent / failed if failed else None})
    return sorted(result, key=lambda row: ORDER.index(row["agency"]))


def prompt_contrasts(rows):
    cells = {}
    for row in rows:
        if row["panel"] != "prompt":
            continue
        key = row["agency"], row["prompt"]
        if key in cells:
            raise ValueError("Duplicate prompt cell.")
        n, passed = int(row["n"]), int(row["successes"])
        if n <= 0 or not 0 <= passed <= n:
            raise ValueError("Invalid success count.")
        cells[key] = (n, passed)
    result = []
    for agency in ORDER:
        n0, s0 = cells[agency, "zero_shot"]
        n1, s1 = cells[agency, "few_shot"]
        p0, p1 = s0 / n0, s1 / n1
        result.append({"agency": agency, "zero_assigned": n0, "example_assigned": n1,
                       "zero_successes": s0, "example_successes": s1,
                       "zero_success_pct": 100 * p0, "example_success_pct": 100 * p1,
                       "gain_pp": 100 * (p1 - p0),
                       "fraction_of_zero_failures_removed": (p1 - p0) / (1 - p0) if p0 < 1 else None})
    return result


def save_csv(path, rows):
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main():
    output = HERE / "results"
    output.mkdir(exist_ok=True)
    raw = read_csv(SOURCE / "appendix_silent_vs_loud.csv")
    failures = failure_rates(raw)
    for row in failures:
        published = next(x for x in raw if x["agency"] == row["agency"])
        for field in ["loud_per100", "silent_per100", "silent_share_of_failures_pct"]:
            assert math.isclose(row[field], float(published[field]), abs_tol=1e-10)
    prompts = prompt_contrasts(read_csv(SOURCE / "prompt_agency.csv"))
    for row in failures:
        paired = next(x for x in prompts if x["agency"] == row["agency"])
        assert row["assigned"] == paired["zero_assigned"] + paired["example_assigned"]
        assert row["successes"] == paired["zero_successes"] + paired["example_successes"]
    cost_rows = []
    for row in read_csv(SOURCE / "summary_by_model.csv"):
        gain = (float(row["agent_pct"]) - float(row["chatbot_pct"])) / 100
        increase = float(row["cost_per_run_agent_usd"]) - float(row["cost_per_run_chatbot_usd"])
        cost_rows.append({"model": row["model"], "gain_pp": 100 * gain,
                          "additional_dollars_per_run": increase,
                          "dollars_per_additional_success": increase / gain if gain > 0 else None})
    save_csv(output / "benchmark_failure_rates.csv", failures)
    save_csv(output / "benchmark_prompt_contrasts.csv", prompts)
    save_csv(output / "benchmark_incremental_cost.csv", cost_rows)
    summary = {"source": "Galiani, Lopez, and Sosa; release v1.2, November manuscript",
               "assigned_runs": sum(r["assigned"] for r in failures), "tasks": 40,
               "models": 6, "source_datasets": 32,
               "self_repair_share_of_success_gain":
               (failures[1]["successes"] - failures[0]["successes"]) /
               (failures[2]["successes"] - failures[0]["successes"]),
               "prompt_interaction_pp": prompts[2]["gain_pp"] - prompts[0]["gain_pp"],
               "scope": "Published aggregate reconstruction; original runs and bootstrap not rerun"}
    (output / "benchmark_summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps({"summary": summary, "failures": failures, "prompts": prompts}, indent=2))


if __name__ == "__main__":
    main()
```

## 1.20 A Recommendation as an Argument

\noindent A manager asks an analyst whether to introduce a price rule. The program produces reliable forecasts of purchases and revenue. The recommendation still depends on the comparison the manager intends, the customers affected, and the reasons for choosing the objective. A calculation can answer its programmed question accurately while leaving the decision unresolved. The analyst should make the premises connecting the calculation to the proposed action explicit.

### 1.20.1 Identify the Question Before Generating Code

\noindent “Who is likely to accept a higher price?” asks for a prediction. “How would a higher price change purchases?” asks for a causal comparison. “Who would bear a burden?” requires a definition of burden and evidence about affected people. “Ought the firm charge that price?” requires a principle that can be justified to those people. Each question changes the evidence needed and the interpretation of the output.

Koralus and Mascarenhas model reasoning as a process of interpreting premises through questions and answers. Their account explains how treating a partial answer as sufficient can produce invalid inferences. For an analyst, a useful application is to state the question answered by each result before treating that result as an answer to a broader managerial question. The theory concerns propositional reasoning; its application to coding workflows is a teaching exercise. [Koralus and Mascarenhas, 2013, §§1–2](https://doi.org/10.1111/phpe.12029).

### 1.20.2 Examine the Premises in Five Steps

\noindent A clear argument names the actor, action, population, comparison, and period. Its premises may include observed facts, a measurement interpretation, a causal restriction, or a normative principle. Distinguishing these roles helps locate the appropriate check. A correct join supports a calculation; evidence about customer understanding supports a claim about informed choice; a defended principle supports an ought conclusion.

1. State the exact claim and define its terms. Preserve the scope and qualifications of any source being assessed.
2. List the premises and identify the support required for each. Separate observations, measurement choices, causal assumptions, and normative judgments.
3. Construct a situation where the stated premises hold but the conclusion fails. Check that the construction preserves the premises.
4. Identify the additional premise needed to rule out the construction. Evaluate its evidence or justification.
5. State the supported conclusion and name evidence or reasons that would change it.

Logical validity means that the conclusion follows if the premises are true. Soundness additionally requires true premises. Empirical claims with sampling uncertainty usually warrant qualified inferences rather than deductive certainty. Reconstruct the actual inference before evaluating it: an association, a confidence statement, and a universal claim make different commitments. MacFarlane's discussion of the relation between logical consequence and norms for reasoning motivates keeping those questions separate. [MacFarlane, 2004, §§1–2](https://johnmacfarlane.net/normativity_of_logic.pdf).

### 1.20.3 The Ends of the Inquiry

\noindent Easy measurement can determine which outcomes receive attention. Ask whether an omitted reason matters even when its importance is difficult to quantify. Distinguish an unmeasured empirical fact, which may be investigated, from a normative question about which ends deserve pursuit. The practical standing of an affected person requires a defended philosophical account. It is not a score to infer from how predictable that person is.

Also distinguish a recognized evidence gap, an unanticipated issue, and an acknowledged limit of knowledge. The last requires an argument about the scope of the method or kind of cognition. Section 9.41.5 examines the “known to be the never known” through Kant's boundary of theoretical cognition and compares it with a conditional statistical identification limit. A question about what ought to be done remains open to practical reasoning even when computation does not settle it.

### 1.20.4 Ask an AI Assistant to Test the Argument

\noindent When the applicable assessment permits AI assistance, give the assistant the claim, its supporting output, and the relevant source passage. Request the following analysis:

> Restate the claim fairly and preserve its qualifications. List the factual, measurement, causal, and normative premises. Propose a counterexample that preserves those premises and explain whether it is logically possible, empirically supported, or merely hypothetical. Identify the missing premise and the evidence or reasons needed to defend it. Give the strongest reply to the criticism. Rewrite the conclusion within its supported scope and identify what could change it. Verify citations against the supplied sources.

The student should inspect the proposed counterexample and the source independently. An assistant can invent an objection to a claim the author never made, or hide a changed population inside a plausible story. A useful objection must survive the same scrutiny as the original argument. The two exact constructions in §§4.29 and 6.38 provide hand-checkable cases; the [argument exercise](../../07_Labs/Philosophical_Arguments/README.md) applies the five steps to a chosen marketing decision.
