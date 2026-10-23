"""Measure an imposed novelty-relevance tradeoff on the same September baskets."""

import json
from common import OUTPUT, load_inputs, save_result
from ranking import candidate_categories, evaluate

food, daily, baskets = load_inputs()
selection = json.loads((OUTPUT / "M07.json").read_text())
windows = {"30_days": 30, "90_days": 90, "all_prior_days": None}
window = windows[selection["chosen_window"]]
candidates = candidate_categories(baskets)
# This grid is a specified sensitivity analysis, not a test-set model search.
weights = [0.0, 0.05, 0.10, 0.20]
tradeoff = [
    {
        "novelty_weight": weight,
        **evaluate(baskets, "2016-09-01", candidates, window, novelty_weight=weight),
    }
    for weight in weights
]
assert (
    abs(
        tradeoff[0]["recall_at_10"]
        - selection["test"]["personal_frequency"]["recall_at_10"]
    )
    < 1e-12
)
result = {"history_window": selection["chosen_window"], "tradeoff": tradeoff}
save_result("M08", result)
print(json.dumps(result, indent=2))
