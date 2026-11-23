# M1. Marketing Decisions, Data, and AI-Assisted Python

A retailer must decide which customers should receive a coupon, how much inventory to place in each store, and which product descriptions should appear online. Each decision needs a different analytical object. A forecast of next week's purchases can inform inventory. A comparison of purchases with and without a coupon can inform targeting. A summary of product complaints can identify a service problem. An analysis becomes useful when its output corresponds to the decision the manager can actually change.

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

The initial dataset might include customer-level histories and a randomized pilot. Without such a pilot or another credible design, a response model can help describe or predict behavior, but the incremental contribution calculation remains unresolved. The next operational step may therefore be a randomized test, rather than immediate large-scale optimization.

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

### 1.15.1 A Report With Traceable Numerical Evidence

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
