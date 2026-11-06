"""Cluster coded paper mechanisms; all prevalence estimates condition on the review sample."""
from pathlib import Path
import json
import platform
import numpy as np
import pandas as pd
import scipy
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage, cut_tree
import sklearn
from sklearn.metrics import silhouette_score, adjusted_rand_score

HERE = Path(__file__).resolve().parent
FEATURES = [
    "attention_salience", "framing_reference", "social_cues", "emotion_identity",
    "opacity_disclosure", "personalization", "privacy_control", "defaults_order",
    "exit_search_friction", "habits_rewards", "financial_commitment", "delegation_control",
]
RISK = ["potential_dual_use", "reported_choice_concern"]


def select_sample(data, sample):
    """Never convert uncoded papers into zero-feature observations."""
    risk = data.review_status.isin(RISK)
    if sample == "downloaded_risk":
        mask = risk & data.download_status.eq("downloaded")
    elif sample == "all_reviewed_risk":
        mask = risk
    elif sample == "downloaded_with_protective":
        mask = (risk | data.review_status.eq("protective")) & data.download_status.eq("downloaded")
        # Broad governance/inclusion papers without these mechanisms remain in
        # the review catalog; a zero vector has no positive mechanism to compare.
        mask &= data[FEATURES].sum(axis=1) > 0
    else:
        raise ValueError(sample)
    result = data.loc[mask].sort_values("id").reset_index(drop=True)
    if result[FEATURES].isna().any().any():
        raise ValueError("Missing codes require review, not zero imputation")
    if not result[FEATURES].isin([0, 1]).all().all():
        raise ValueError("Mechanism indicators must be binary")
    if (result[FEATURES].sum(axis=1) == 0).any():
        raise ValueError("An uncoded mechanism cannot enter the similarity analysis")
    return result


def partition(matrix, k, metric="jaccard"):
    """Average linkage accepts non-Euclidean distances such as Jaccard."""
    distances = pdist(matrix.astype(bool), metric=metric)
    tree = linkage(distances, method="average")
    labels = cut_tree(tree, n_clusters=[k]).ravel()
    return labels, squareform(distances)


def evaluate_sample(data, name, output):
    sample = select_sample(data, name)
    matrix = sample[FEATURES].to_numpy(dtype=int)
    n = len(sample)
    candidates = []
    for k in range(2, min(8, n - 1) + 1):
        labels, distance = partition(matrix, k)
        sizes = np.bincount(labels)
        candidates.append({"k": k, "silhouette": silhouette_score(distance, labels, metric="precomputed"),
                           "smallest_cluster": int(sizes.min()), "largest_cluster": int(sizes.max())})
    candidates = pd.DataFrame(candidates)
    # This is a declared selection rule, not a claim that nature has K types.
    best = candidates.sort_values(["silhouette", "k"], ascending=[False, True]).iloc[0]
    k = int(best.k)
    labels, _ = partition(matrix, k)
    # Stable presentation IDs: descending size, with original ID breaking ties.
    order = sorted(set(labels), key=lambda c: (-sum(labels == c), c))
    label_map = {c: rank + 1 for rank, c in enumerate(order)}
    sample["cluster"] = [label_map[c] for c in labels]
    counts = sample.groupby("cluster").size().rename("papers").to_frame()
    counts["share"] = counts.papers / n
    profiles = sample.groupby("cluster")[FEATURES].mean()
    counts["most_common_features"] = [
        "; ".join(profiles.loc[c].sort_values(ascending=False, kind="stable").head(3).index)
        for c in counts.index
    ]
    frequency = sample[FEATURES].sum().rename("papers").to_frame()
    frequency["denominator"] = n
    frequency["share"] = frequency.papers / n
    frequency = frequency.sort_values(["papers"], ascending=False, kind="stable")
    # Refit on 80% subsamples, comparing shared rows with the full partition.
    # Quantiles measure conditional algorithm stability, not population uncertainty.
    rng = np.random.default_rng(534)
    stability = []
    for iteration in range(200):
        indices = np.sort(rng.choice(n, size=max(k + 1, int(.8 * n)), replace=False))
        new_labels, _ = partition(matrix[indices], k)
        stability.append(adjusted_rand_score(labels[indices], new_labels))
    alternative, _ = partition(matrix, k, metric="hamming")
    # Perturb one coded bit per paper to expose sensitivity to annotation choices.
    # This imposed stress test is not an estimated annotation error distribution.
    perturbation = []
    for iteration in range(200):
        changed = matrix.copy()
        for row in range(n):
            allowed = np.arange(len(FEATURES))
            if changed[row].sum() == 1:
                allowed = allowed[changed[row] == 0]
            column = rng.choice(allowed)
            changed[row, column] = 1 - changed[row, column]
        new_labels, _ = partition(changed, k)
        perturbation.append(adjusted_rand_score(labels, new_labels))
    folder = output / name
    folder.mkdir(exist_ok=True, parents=True)
    sample.to_csv(folder / "assignments.csv", index=False)
    counts.to_csv(folder / "cluster_sizes.csv")
    profiles.to_csv(folder / "cluster_profiles.csv")
    frequency.to_csv(folder / "feature_prevalence.csv", index_label="feature")
    candidates.to_csv(folder / "k_comparison.csv", index=False)
    pd.DataFrame({"adjusted_rand_index": stability}).to_csv(folder / "subsample_stability.csv", index=False)
    assert counts.papers.sum() == n and np.isclose(counts.share.sum(), 1)
    # Independent row-loop count checks the vectorized feature aggregate.
    for feature in FEATURES:
        assert int(frequency.loc[feature, "papers"]) == sum(int(row[feature]) for _, row in sample.iterrows())
    return {"papers": n, "k": k, "silhouette": float(best.silhouette),
            "cluster_counts": {str(c): int(v) for c, v in counts.papers.items()},
            "largest_features": frequency.head(3).reset_index().to_dict("records"),
            "subsample_ari_quantiles": np.quantile(stability, [.1, .5, .9]).tolist(),
            "hamming_ari": float(adjusted_rand_score(labels, alternative)),
            "one_bit_perturbation_ari_quantiles": np.quantile(perturbation, [.1, .5, .9]).tolist(),
            "valid_perturbation_runs": len(perturbation)}


def main():
    data = pd.read_csv(HERE / "coded_papers.csv")
    assert data.id.is_unique and data.doi.is_unique
    output = HERE / "results"
    output.mkdir(exist_ok=True)
    summary = {name: evaluate_sample(data, name, output) for name in [
        "downloaded_risk", "all_reviewed_risk", "downloaded_with_protective"]}
    summary["environment"] = {"python": platform.python_version(), "numpy": np.__version__,
                              "pandas": pd.__version__, "scipy": scipy.__version__, "sklearn": sklearn.__version__}
    (output / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
