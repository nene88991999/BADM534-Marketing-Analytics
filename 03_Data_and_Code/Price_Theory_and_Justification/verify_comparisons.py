"""Check indifference and incidence independently of the implementation."""
import json
import math
from pathlib import Path

from compare_valuations import compare, willingness_to_pay


result = compare()
for row in result["willingness_to_pay"]:
    budget = row["budget_dollars"]
    payment = row["willingness_to_pay_dollars"]
    increment = row["service_increment"]
    assert 0 <= payment < budget
    assert math.isclose(math.log(budget - payment) + increment,
                        math.log(budget), abs_tol=1e-12)
    assert math.log(budget - payment / 2) + increment > math.log(budget)
assert willingness_to_pay(100, 0) == 0
rows = result["willingness_to_pay"]
assert math.isclose(rows[1]["willingness_to_pay_dollars"],
                    10 * rows[0]["willingness_to_pay_dollars"])
assert rows[0]["willingness_to_pay_dollars"] == rows[3]["willingness_to_pay_dollars"]
assert rows[1]["willingness_to_pay_dollars"] == rows[2]["willingness_to_pay_dollars"]
a, b = result["compensation"]
assert (a["firm_change_dollars"], a["each_resident_change_dollars"],
        a["aggregate_dollar_change"], a["people_with_dollar_losses"]) == (140, -1, 40, 100)
assert (b["firm_change_dollars"], b["each_resident_change_dollars"],
        b["aggregate_dollar_change"], b["people_with_dollar_losses"]) == (40, 0, 40, 0)
assert json.loads(Path(__file__).with_name("results.json").read_text()) == result
print("Verified indifference, affordability, budget reversal, zero benefit, "
      "dollar incidence, transfers, and the saved results.")
