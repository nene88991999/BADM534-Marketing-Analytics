"""Reconcile published tables independently from the saved numeric arrays."""
from pathlib import Path
import hashlib
import json
import numpy as np

HERE = Path(__file__).resolve().parent
R = HERE / "results"


def run():
    summary = json.loads((R / "summary.json").read_text())
    curves = np.genfromtxt(R / "curves.csv", delimiter=",", names=True)
    for model in summary["reference"]:
        rmse = np.sqrt(np.mean((curves[model["model"]]-curves["truth_usd"])**2))
        assert abs(rmse-model["rmse_usd"]) < 1e-8
    coverage = np.genfromtxt(R / "coverage.csv", delimiter=",", names=True)
    for row in summary["simulation"]:
        selected = ((coverage["outcome_correct"] == row["outcome_correct"])
                    & (coverage["density_correct"] == row["density_correct"]))
        assert selected.sum() == 29
        assert abs(coverage["pointwise_coverage"][selected].mean()-row["mean_pointwise_coverage"]) < 1e-8
    stores = np.genfromtxt(R / "store_curves.csv", delimiter=",", names=True)
    observations = np.genfromtxt(R / "stores.csv", delimiter=",", names=True)
    result = json.loads((R / "pooling_summary.json").read_text())
    sizes = np.bincount(observations["store"].astype(int))
    for name, ids in [("all_stores", np.arange(20)), ("small_stores_n_le_25", np.flatnonzero(sizes <= 25)),
                      ("large_stores_n_ge_150", np.flatnonzero(sizes >= 150))]:
        selected = np.isin(stores["store"], ids)
        for model in ["complete", "separate", "partial"]:
            rmse = np.sqrt(np.mean((stores[model][selected]-stores["truth"][selected])**2))
            assert abs(rmse-result["rmse_usd"][name][model]) < 1e-8
    objectives = np.genfromtxt(R / "objectives.csv", delimiter=",", names=True)
    report = json.loads((R / "objectives_summary.json").read_text())
    for name, target in [("revenue", "revenue_usd"), ("profit", "profit_usd"),
                          ("profit_with_complaint_cap", "profit_usd")]:
        feasible = (objectives["complaint_fraction"] <= .03) if "cap" in name else np.ones(len(objectives), bool)
        i = np.argmax(np.where(feasible, objectives[target], -np.inf))
        assert abs(objectives["discount_pp"][i]-report[name]["discount_pp"]) < 1e-8
    record = {"checked_on": "2026-11-18", "checks": ["seven unit tests", "four reference curve RMSEs",
              "116 pointwise coverage rows", "nine pooling RMSEs", "three objective maxima"],
              "sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(R.glob('*')) if p.suffix in ['.csv', '.json']}}
    (HERE / "verification.json").write_text(json.dumps(record, indent=2)+"\n")
    print("Reconciled curve, coverage, pooling, and decision tables.")


if __name__ == "__main__":
    run()
