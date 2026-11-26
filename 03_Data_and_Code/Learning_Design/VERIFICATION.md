# Verification of Learning Comparisons

Checked November 26, 2026.

## Executed Calculations

`learning_comparisons.py` and `bill_identity.py` ran with Python 3.14.8 and its standard library. The percentage comparison returns 11 percentage points and 16.4179104478% relative to 67. The synthetic factorial returns question effects of 6 and 9 points, format effects of 8 and 11 points, equal-weight effects of 7.5 and 9.5 points, and an interaction of 3 points. The bill program independently returns USD 100, USD 110, and USD 100 per account-month from the existing matched synthetic table.

Six independent Python tests pass. They check reference values, a changed denominator, a zero reference, invalid inputs, the four-cell requirement, and alternative feature effects compatible with the same package difference. The bill program separately asserts the accounting identity and the three hand-computed bills. The browser's JavaScript checks compare its arithmetic against those independent saved-table values and test direction, zero price, and invalid inputs.

## Reproduction

```sh
python3 03_Data_and_Code/Learning_Design/learning_comparisons.py
python3 03_Data_and_Code/Learning_Design/bill_identity.py
python3 -m unittest discover -s 03_Data_and_Code/Learning_Design -p 'test_*.py'
python3 08_Wiki/pilot/build_pilot.py
node 08_Wiki/pilot/test_pilot.cjs
python3 scripts/check_lecture_code.py
```

The final check confirms 124 matching, syntactically valid Python listings across the lecture notes. Both added listings match their maintained programs. The HTML's complete Python listing also matches `bill_identity.py`.

## Scope

These checks establish arithmetic and source consistency. The percentage inputs are rounded published summaries. The factorial means and bill scenarios are synthetic. No participant microdata, estimated learning effect, model API, or replication of the original trial is involved. [Browser verification](../../08_Wiki/pilot/VERIFICATION.md) records the separate interaction checks.
