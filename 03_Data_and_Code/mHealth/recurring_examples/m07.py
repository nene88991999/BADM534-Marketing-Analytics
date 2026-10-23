"""Choose history length in July and evaluate the frozen rule in September."""

import json
from common import load_inputs, save_result
from ranking import candidate_categories, evaluate, ranking_metrics

food, daily, baskets = load_inputs()
candidates = candidate_categories(baskets)
windows = {"30_days": 30, "90_days": 90, "all_prior_days": None}
validation = {
    name: evaluate(baskets, "2016-07-01", candidates, window)
    for name, window in windows.items()
}
# Ties retain the first listed specification; September plays no role in selection.
chosen = max(validation, key=lambda name: validation[name]["ndcg_at_10"])
test = {
    "popularity": evaluate(baskets, "2016-09-01", candidates, popularity_only=True),
    "personal_frequency": evaluate(baskets, "2016-09-01", candidates, windows[chosen]),
}
assert ranking_metrics(["B", "C", "A"], {"B", "C"}) == (1.0, 1.0)
assert ranking_metrics(["A", "B", "C"], {"B", "C"})[1] < 1
result = {
    "candidate_categories": len(candidates),
    "validation": validation,
    "chosen_window": chosen,
    "test": test,
}
save_result("M07", result)
print(json.dumps(result, indent=2))
