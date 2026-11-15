"""Compare three CPU implementations on fixed synthetic vectors."""
from pathlib import Path
from time import perf_counter
from itertools import combinations
import argparse
import csv
import hashlib
import json
import platform

import numpy as np
import sklearn
import faiss
from faiss.contrib.e_means import NumpyEmeans
from sklearn.cluster import KMeans, MiniBatchKMeans
from sklearn.metrics import adjusted_rand_score
from threadpoolctl import threadpool_limits

HERE = Path(__file__).resolve().parent
METHODS = ("lloyd", "minibatch", "emeans")


def make_data(n=50000, d=32, seed=20261115):
    rng = np.random.default_rng(seed)
    means = rng.normal(0, 1.5, size=(8, d))
    weights = [.40, .20, .12, .10, .08, .05, .03, .02]
    def draw(count):
        group = rng.choice(8, size=count, p=weights)
        return means[group] + rng.normal(0, .8, size=(count, d))
    train, test = draw(n), draw(n // 5)
    mean, scale = train.mean(axis=0), train.std(axis=0)
    return (np.ascontiguousarray((train - mean) / scale, dtype="float32"),
            np.ascontiguousarray((test - mean) / scale, dtype="float32"))


def nearest(x, centers, chunk=512):
    """Score all final centers using direct float64 distances."""
    c = np.asarray(centers, dtype="float64")
    labels, distances = [], []
    for start in range(0, len(x), chunk):
        block = np.asarray(x[start:start + chunk], dtype="float64")
        squared = ((block[:, None, :] - c[None, :, :])**2).sum(axis=2)
        choice = squared.argmin(axis=1)
        labels.extend(choice.tolist())
        distances.extend(squared[np.arange(len(block)), choice].tolist())
    return np.asarray(labels), np.asarray(distances)


def fit(method, x, initial, budget, seed):
    k, d = initial.shape
    start = perf_counter()
    if method == "emeans":
        model = NumpyEmeans(d, k, nepochs=budget, seed=seed)
        centers, saved = model.train(x, initial.copy())
        details = dict(model.recipe)
    else:
        options = dict(n_clusters=k, init=initial.copy(), n_init=1,
                       max_iter=budget, tol=0.0, random_state=seed)
        if method == "lloyd":
            model = KMeans(algorithm="lloyd", **options)
        else:
            model = MiniBatchKMeans(batch_size=256, max_no_improvement=None,
                                   reassignment_ratio=0.01, **options)
        model.fit(x)
        centers, saved = model.cluster_centers_, model.labels_
        details = {"n_iter": int(model.n_iter_)}
        if method == "minibatch":
            details["n_steps"] = int(model.n_steps_)
            details["batch_size"] = 256
    elapsed = perf_counter() - start
    return np.asarray(centers).copy(), np.asarray(saved).copy(), elapsed, details


def write_csv(path, rows):
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rows", type=int, default=50000)
    parser.add_argument("--dimensions", type=int, default=32)
    parser.add_argument("--clusters", type=int, default=64)
    parser.add_argument("--seeds", type=int, nargs="+", default=[11, 23, 37])
    parser.add_argument("--budgets", type=int, nargs="+", default=[2, 5, 10])
    parser.add_argument("--output", type=Path, default=HERE / "results")
    args = parser.parse_args()
    if not (args.rows >= 10 and 1 < args.clusters <= args.rows
            and args.dimensions > 0 and min(args.budgets) > 0):
        parser.error("Require n >= 10, 1 < k <= n, d > 0 and positive budgets")
    if len(set(args.seeds)) != len(args.seeds) or len(set(args.budgets)) != len(args.budgets):
        parser.error("Seeds and budgets must be unique")
    args.output.mkdir(parents=True, exist_ok=True)
    train, test = make_data(args.rows, args.dimensions)
    runs, recipes, heldout = [], {}, {}
    faiss.omp_set_num_threads(1)
    with threadpool_limits(limits=1):
        # Exclude import and warm-up work from the reported training time.
        warm = train[:max(1000, args.clusters)]
        for method in METHODS:
            fit(method, warm, warm[:args.clusters].copy(), 1, 0)
        for seed in args.seeds:
            rng = np.random.default_rng(seed)
            initial = train[rng.choice(len(train), args.clusters, replace=False)]
            for budget in args.budgets:
                for method in rng.permutation(METHODS):
                    name = f"{method}_{seed}_{budget}"
                    centers, saved, seconds, recipe = fit(
                        method, train, initial, budget, seed)
                    start = perf_counter()
                    train_labels, train_d2 = nearest(train, centers)
                    test_labels, test_d2 = nearest(test, centers)
                    evaluation = perf_counter() - start
                    valid = (saved >= 0) & (saved < args.clusters)
                    disagreement = int(np.sum(saved[valid] != train_labels[valid]))
                    runs.append(dict(method=method, seed=seed, budget=budget,
                        train_rows=len(train), test_rows=len(test), dimensions=args.dimensions,
                        clusters=args.clusters, fit_seconds=seconds,
                        evaluation_seconds=evaluation, total_seconds=seconds + evaluation,
                        train_mse=float(train_d2.mean()), test_mse=float(test_d2.mean()),
                        saved_label_rows=int(valid.sum()),
                        saved_label_disagreements=disagreement,
                        saved_label_disagreement_rate=disagreement / valid.sum()))
                    np.savez_compressed(args.output / (name + ".npz"),
                        centroids=centers, saved_labels=saved,
                        train_labels=train_labels, test_labels=test_labels)
                    heldout[method, budget, seed] = test_labels
                    recipes[name] = recipe
                    print(name, round(seconds, 3), round(test_d2.mean(), 4), flush=True)
    summary, stability = [], []
    for method in METHODS:
        for budget in args.budgets:
            subset = [r for r in runs if r["method"] == method and r["budget"] == budget]
            row = dict(method=method, budget=budget, runs=len(subset))
            for field in ["fit_seconds", "evaluation_seconds", "total_seconds", "test_mse",
                          "train_mse", "saved_label_disagreement_rate"]:
                row[field + "_median"] = float(np.median([r[field] for r in subset]))
            summary.append(row)
            for first, second in combinations(args.seeds, 2):
                stability.append(dict(method=method, budget=budget, seed_a=first, seed_b=second,
                    test_rows=len(test), adjusted_rand=float(adjusted_rand_score(
                        heldout[method, budget, first], heldout[method, budget, second]))))
    write_csv(args.output / "runs.csv", runs)
    write_csv(args.output / "summary.csv", summary)
    if stability:
        write_csv(args.output / "stability.csv", stability)
    metadata = dict(data_seed=20261115, synthetic=True, train_rows=len(train), test_rows=len(test),
        dimensions=args.dimensions, clusters=args.clusters, seeds=args.seeds, budgets=args.budgets,
        threads=1, machine=platform.machine(), system=platform.system(),
        python=platform.python_version(), numpy=np.__version__, sklearn=sklearn.__version__,
        faiss=faiss.__version__, train_sha256=hashlib.sha256(train.tobytes()).hexdigest(),
        test_sha256=hashlib.sha256(test.tobytes()).hexdigest(), recipes=recipes,
        timing_scope="Construction and training after warm-up; common final-center evaluation reported separately. Data creation, scaling, imports, artifact saving and stability calculations excluded.",
        budget_scope="KMeans iteration cap, MiniBatchKMeans max_iter with convergence checks disabled, and e-means epochs. These do not imply equal arithmetic work.")
    (args.output / "metadata.json").write_text(json.dumps(metadata, indent=2,
        default=lambda x: x.item() if isinstance(x, np.generic) else str(x)) + "\n")


if __name__ == "__main__":
    main()
