"""Select a category pair in January-June; evaluate it in July-August."""

from itertools import combinations
import json
import numpy as np
import pandas as pd
from common import SEED, load_food, make_baskets, save_result


def metrics(n, a, b, both):
    if min(n, a, b) <= 0:
        raise ValueError("Positive basket and marginal counts are required")
    return {
        "baskets": int(n),
        "a_baskets": int(a),
        "b_baskets": int(b),
        "joint_baskets": int(both),
        "support": both / n,
        "confidence_a_to_b": both / a,
        "baseline_b": b / n,
        "lift": both * n / (a * b),
    }


def presence(baskets, categories):
    return np.array(
        [[c in basket for c in categories] for basket in baskets.basket], dtype=np.int64
    )


if __name__ == "__main__":
    baskets = make_baskets(load_food())
    train = baskets.loc[baskets.date < "2016-07-01"]
    frequency = train.explode("basket").groupby("basket").size()
    categories = sorted(
        frequency.sort_values(ascending=False, kind="stable").head(20).index
    )
    matrix = presence(train, categories)
    joint, marginal = matrix.T @ matrix, matrix.sum(axis=0)
    rules = []
    for a, b in combinations(range(len(categories)), 2):
        mask = (matrix[:, a] * matrix[:, b]).astype(bool)
        supporting_users = train.loc[mask, "Userid"].nunique()
        if joint[a, b] >= 100 and supporting_users >= 30:
            rule = metrics(len(train), marginal[a], marginal[b], joint[a, b])
            rules.append(
                {
                    "a": categories[a],
                    "b": categories[b],
                    "supporting_users": int(supporting_users),
                    **rule,
                }
            )
    rules.sort(key=lambda r: (-r["lift"], r["a"], r["b"]))
    selected = rules[0]
    users = sorted(train.Userid.unique())
    future = baskets.loc[
        baskets.Userid.isin(users) & baskets.date.between("2016-07-01", "2016-08-31")
    ].copy()
    binary = presence(future, [selected["a"], selected["b"]])
    future["a"], future["b"] = binary[:, 0], binary[:, 1]
    future["both"], future["n"] = binary.prod(axis=1), 1
    counts = (
        future.groupby("Userid")[["n", "a", "b", "both"]]
        .sum()
        .reindex(users, fill_value=0)
        .to_numpy()
    )
    evaluation = metrics(*counts.sum(axis=0))
    rng = np.random.default_rng(SEED)
    lifts = []
    for _ in range(500):
        total = counts[rng.integers(0, len(users), len(users))].sum(axis=0)
        if min(total[:3]) > 0:
            lifts.append(metrics(*total)["lift"])
    evaluation["user_bootstrap_ci95"] = np.quantile(lifts, [0.025, 0.975]).tolist()
    evaluation["bootstrap_valid_draws"] = len(lifts)
    result = {
        "candidate_categories": len(categories),
        "eligible_pairs": len(rules),
        "training_users": len(users),
        "evaluation_users": int(future.Userid.nunique()),
        "selected_training_pair": selected,
        "july_august": evaluation,
    }
    save_result("association_rules", result)
    print(json.dumps(result, indent=2))
