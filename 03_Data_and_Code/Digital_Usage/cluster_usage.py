"""Compare three-cluster descriptions of the 1,253 released Illinois areas."""
import json
from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent


def kmeans(x, seed=534, starts=30, k=3):
    rng = np.random.default_rng(seed)
    best = None
    for _ in range(starts):
        centers = x[rng.choice(len(x), k, replace=False)].copy()
        for iteration in range(500):
            labels = ((x[:, None] - centers) ** 2).sum(axis=2).argmin(axis=1)
            if len(np.unique(labels)) < k:
                break  # Discard an empty-cluster initialization.
            updated = np.array([x[labels == j].mean(axis=0) for j in range(k)])
            next_labels = ((x[:, None] - updated) ** 2).sum(axis=2).argmin(axis=1)
            if np.array_equal(labels, next_labels):
                loss = float(((x - updated[labels]) ** 2).sum())
                if best is None or loss < best[0]:
                    best = loss, labels.copy(), updated
                break
            centers = updated
    if best is None:
        raise RuntimeError("No converged nonempty partition")
    return best


def adjusted_rand(a, b):
    # Count pairs together in both partitions; invariant to label names.
    _, a = np.unique(a, return_inverse=True)
    _, b = np.unique(b, return_inverse=True)
    table = np.zeros((a.max() + 1, b.max() + 1), dtype=int)
    np.add.at(table, (a, b), 1)
    choose = lambda n: n * (n - 1) / 2
    together = choose(table).sum()
    row_pairs, col_pairs = choose(table.sum(1)).sum(), choose(table.sum(0)).sum()
    expected = row_pairs * col_pairs / choose(len(a))
    denominator = (row_pairs + col_pairs) / 2 - expected
    return float((together - expected) / denominator) if denominator else 1.0


def main():
    data = pd.read_csv(ROOT / "results/joined_areas.csv", dtype={"zip": "string"})
    il = data.loc[data.state.eq("IL"), ["zip", "mci", "cci"]].copy()
    raw = il[["mci", "cci"]].to_numpy()
    mean, sd = raw.mean(0), raw.std(0)
    z = (raw - mean) / sd
    raw_fit, scaled_fit = kmeans(raw), kmeans(z)
    # Order cluster names by average MCI solely to make tables readable.
    order = np.argsort(scaled_fit[2][:, 0])
    remap = np.empty(3, dtype=int)
    remap[order] = np.arange(1, 4)
    il["cluster"] = remap[scaled_fit[1]]
    il["raw_cluster"] = raw_fit[1] + 1
    il.to_csv(ROOT / "results/illinois_clusters.csv", index=False)
    il.groupby("cluster").agg(areas=("zip", "size"), mci=("mci", "mean"),
        cci=("cci", "mean")).to_csv(ROOT / "results/cluster_summary.csv")
    sensitivity = [{"seed": s, "ari_to_seed_534": adjusted_rand(
        scaled_fit[1], kmeans(z, seed=s)[1])} for s in [1, 17, 2026]]
    result = {"areas": len(il), "k": 3, "starts": 30, "max_iterations": 500,
        "raw_vs_standardized_ari": adjusted_rand(raw_fit[1], scaled_fit[1]),
        "standardization_mean": mean.tolist(), "standardization_sd_ddof0": sd.tolist(),
        "standardized_sse": scaled_fit[0], "seed_sensitivity": sensitivity,
        "interpretation": "Geographic descriptions; no individual skill or assistance need labels"}
    (ROOT / "results/clustering.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
