"""Whole-basket chronological evaluation with a frozen category universe."""

import numpy as np
import pandas as pd


def candidate_categories(baskets):
    prior = baskets.loc[baskets.date.lt("2016-07-01")]
    return sorted({category for basket in prior.basket for category in basket})


def evaluation_cases(baskets, cutoff, candidates):
    cutoff = pd.Timestamp(cutoff)
    prior = baskets.loc[baskets.date.lt(cutoff)]
    counts = prior.groupby("Userid").size()
    eligible = counts[counts >= 30].index
    end = cutoff + pd.offsets.MonthBegin(1)
    target = baskets.loc[baskets.date.ge(cutoff) & baskets.date.lt(end)]
    target = target.loc[target.Userid.isin(eligible)].sort_values(["Userid", "date"])
    target = target.drop_duplicates("Userid")
    histories = dict(tuple(prior.groupby("Userid")))
    assert prior.date.max() < cutoff
    global_counts = (
        prior.basket.explode().value_counts().reindex(candidates, fill_value=0)
    )
    popularity = global_counts.to_numpy(dtype=float) / len(prior)
    cases = [(histories[row.Userid], set(row.basket)) for row in target.itertuples()]
    return cases, popularity, len(eligible)


def personal_frequency(history, cutoff, candidates, window):
    if window is not None:
        start = pd.Timestamp(cutoff) - pd.Timedelta(days=window)
        history = history.loc[history.date.ge(start)]
    counts = history.basket.explode().value_counts().reindex(candidates, fill_value=0)
    return counts.to_numpy(dtype=float) / max(1, len(history))


def rank_categories(scores, candidates, k=10):
    # Stable sorting resolves exact score ties using alphabetically sorted candidates.
    positions = np.argsort(-scores, kind="stable")[:k]
    return [candidates[index] for index in positions]


def ranking_metrics(ranking, target):
    relevance = np.array([category in target for category in ranking], dtype=float)
    discounts = 1 / np.log2(np.arange(2, len(ranking) + 2))
    ideal = discounts[: min(len(target), len(ranking))].sum()
    return float(relevance.sum() / len(target)), float(
        (relevance * discounts).sum() / ideal
    )


def evaluate(
    baskets, cutoff, candidates, window=None, popularity_only=False, novelty_weight=0
):
    cases, popularity, eligible = evaluation_cases(baskets, cutoff, candidates)
    rows = []
    for history, target in cases:
        frequency = personal_frequency(history, cutoff, candidates, window)
        recent = personal_frequency(history, cutoff, candidates, 30)
        unseen = recent == 0
        scores = popularity if popularity_only else frequency + 1e-6 * popularity
        ranking = rank_categories(scores + novelty_weight * unseen, candidates)
        recall, ndcg = ranking_metrics(ranking, target)
        recent_set = {candidates[j] for j in np.flatnonzero(recent)}
        novelty = sum(category not in recent_set for category in ranking) / len(ranking)
        coverage = len(target & set(candidates)) / len(target)
        rows.append([recall, ndcg, novelty, coverage])
    means = np.mean(rows, axis=0)
    return {
        "eligible_users": eligible,
        "evaluated_users": len(cases),
        "recall_at_10": float(means[0]),
        "ndcg_at_10": float(means[1]),
        "novelty_at_10": float(means[2]),
        "target_candidate_coverage": float(means[3]),
    }
