"""Randomized synthetic discounts: separate, complete, and partial pooling.

Twenty stores nested in four regions; equal-store evaluation on a common grid.
Only observed validation outcomes select penalties. Known curves score the fits.
"""
from pathlib import Path
import argparse
import json
import numpy as np


def basis(a):
    t = (np.asarray(a) - 20) / 10
    return np.column_stack([np.ones_like(t), t, t*t - 0.75])


def design(a, store):
    b = basis(a)
    region = store // 5
    return np.column_stack([b] + [b*(region == r)[:, None] for r in range(4)]
                           + [b*(store == s)[:, None] for s in range(20)])


def fit(a, store, y, region_penalty, store_penalty):
    d = design(a, store)
    penalty = np.r_[np.zeros(3), np.full(12, region_penalty), np.full(60, store_penalty)]
    return np.linalg.solve(d.T @ d + np.diag(penalty), d.T @ y)


def generate(seed=20261119):
    rng = np.random.default_rng(seed)
    sizes = np.tile([12, 25, 60, 150, 300], 4)
    region = np.array([[-.6, -.5, .1], [-.2, .4, -.1], [.2, -.2, -.1], [.6, .3, .1]])
    coefficient = (np.array([13.25, 0, -1]) + np.repeat(region, 5, axis=0)
                   + rng.normal(size=(20, 3)) * [.6, .5, .3])
    store = np.repeat(np.arange(20), sizes)
    a = rng.uniform(5, 35, len(store))  # Randomized independently within every store.
    y = np.sum(basis(a) * coefficient[store], axis=1) + rng.normal(0, 3, len(a))
    fold = np.concatenate([rng.permutation(np.arange(n) % 5) for n in sizes])
    return a, store, y, coefficient, fold


def run(output):
    output.mkdir(parents=True, exist_ok=True)
    a, store, y, coefficient, fold = generate()
    candidates = []
    for rp in [1., 10., 100.]:
        for sp in [1., 10., 100.]:
            prediction = np.empty_like(y)
            for k in range(5):
                tr, te = fold != k, fold == k
                beta = fit(a[tr], store[tr], y[tr], rp, sp)
                prediction[te] = design(a[te], store[te]) @ beta
            loss = np.mean([np.mean((y[store == s]-prediction[store == s])**2) for s in range(20)])
            candidates.append((loss, rp, sp))
    loss, rp, sp = min(candidates)
    partial = fit(a, store, y, rp, sp)
    complete = np.linalg.lstsq(basis(a), y, rcond=None)[0]
    grid, rows, errors = np.arange(6., 35.), [], []
    for s in range(20):
        selected = store == s
        separate = np.linalg.lstsq(basis(a[selected]), y[selected], rcond=None)[0]
        target = basis(grid) @ coefficient[s]
        predictions = [basis(grid) @ complete, basis(grid) @ separate,
                       design(grid, np.full(len(grid), s)) @ partial]
        errors.append([selected.sum()] + [np.mean((p-target)**2) for p in predictions])
        rows.extend(np.c_[np.full(len(grid), s), grid, target, *predictions].tolist())
    errors = np.array(errors)
    np.savetxt(output / "stores.csv", np.c_[store, store//5, a, y, fold], delimiter=",", comments="",
               header="store,region,discount_pp,profit_usd,validation_fold", fmt="%.10g")
    np.savetxt(output / "store_curves.csv", rows, delimiter=",", comments="",
               header="store,discount_pp,truth,complete,separate,partial", fmt="%.10g")
    np.savetxt(output / "pooling_cv.csv", candidates, delimiter=",", comments="",
               header="equal_store_validation_mse,region_penalty,store_penalty", fmt="%.10g")
    results = {}
    for name, selected in [("all_stores", np.ones(20, bool)), ("small_stores_n_le_25", errors[:, 0] <= 25),
                           ("large_stores_n_ge_150", errors[:, 0] >= 150)]:
        results[name] = dict(zip(["complete", "separate", "partial"],
                                np.sqrt(errors[selected, 1:].mean(0)).tolist()))
    report = {"seed": 20261119, "observations": len(y), "stores": 20, "regions": 4,
              "region_penalty": rp, "store_penalty": sp, "validation_mse": loss,
              "rmse_usd": results, "scope": "One synthetic randomized dataset; no confidence intervals or general dominance claim."}
    (output / "pooling_summary.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parent / "results")
    run(parser.parse_args().output)
