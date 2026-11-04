"""Simulate selection among equally uninformative classifiers using only stdlib."""
import csv
import json
import math
import random
from pathlib import Path
from statistics import mean, stdev

OUT = Path(__file__).resolve().parent / "results"


def select_candidate(development_counts):
    # The earliest candidate wins a tie. Test outcomes are never an input.
    return max(range(len(development_counts)), key=development_counts.__getitem__)


def expected_selected_accuracy(n, candidates):
    """Exact binomial order-statistic expectation, evaluated in floating point."""
    cumulative = 0.0
    expected_count = 0.0
    for successes in range(n):
        cumulative += math.comb(n, successes) / 2**n
        expected_count += 1 - cumulative**candidates
    return expected_count / n


def main():
    seed, repetitions, development_n, test_n = 20261104, 2000, 80, 200
    candidate_counts = [1, 5, 20, 100]
    # Separate streams keep test outcomes out of the development process.
    development_rng = random.Random(seed)
    test_rng = random.Random(seed + 1)
    observed = {k: {"development": [], "test": []} for k in candidate_counts}
    for _ in range(repetitions):
        # Each independent bit denotes a correct prediction with probability 1/2.
        # Candidates are also independent in this deliberately simple null model.
        development = [development_rng.getrandbits(development_n).bit_count()
                       for _ in range(max(candidate_counts))]
        test = [test_rng.getrandbits(test_n).bit_count()
                for _ in range(max(candidate_counts))]
        for k in candidate_counts:
            selected = select_candidate(development[:k])
            observed[k]["development"].append(development[selected] / development_n)
            observed[k]["test"].append(test[selected] / test_n)
    rows = []
    for k, values in observed.items():
        exact = expected_selected_accuracy(development_n, k)
        development_mean, test_mean = mean(values["development"]), mean(values["test"])
        development_se = stdev(values["development"]) / math.sqrt(repetitions)
        test_se = stdev(values["test"]) / math.sqrt(repetitions)
        # Independent analytic benchmarks check the simulation's implementation.
        assert abs(development_mean - exact) < 5 * development_se
        assert abs(test_mean - 0.5) < 5 * test_se
        rows.append({"candidates": k, "expected_development_accuracy": exact,
                     "mean_development_accuracy": development_mean,
                     "mean_test_accuracy": test_mean, "expected_test_accuracy": 0.5,
                     "development_mc_se": development_se, "test_mc_se": test_se})
    OUT.mkdir(exist_ok=True)
    with (OUT / "selection_results.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    metadata = {"seed": seed, "repetitions": repetitions,
                "development_cases": development_n, "fresh_test_cases": test_n,
                "scope": "Synthetic independent chance predictions; no LLM calls.",
                "mc_se": "Monte Carlo error of the simulated mean across repetitions"}
    (OUT / "selection_metadata.json").write_text(json.dumps(metadata, indent=2) + "\n")
    print(json.dumps(rows, indent=2))


if __name__ == "__main__":
    main()
