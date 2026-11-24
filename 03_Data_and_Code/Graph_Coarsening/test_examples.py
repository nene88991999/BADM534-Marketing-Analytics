"""Independent finite checks for original teaching calculations."""
from copy import deepcopy
from itertools import permutations, product
from pathlib import Path
import json
import unittest

from compress_network import calculate as network, distances
from evaluate_labels import calculate as labels, majority

CASES = json.loads((Path(__file__).parent / "data/cases.json").read_text())


class Examples(unittest.TestCase):
    def test_revenue_accounting(self):
        result, rows = network(CASES["network"])
        self.assertEqual(sum(r["revenue_dollars"] for r in rows), 70)
        self.assertEqual(result["size_weighted_mean_revenue"], 70 / 4)
        self.assertEqual(result["equal_group_mean_revenue"], 25)
        self.assertEqual(result["sum_of_group_means"], 50)
        self.assertEqual(result["reconstruction_squared_error"], 0)

    def test_energy_by_laplacian(self):
        # Independently evaluate x' L x for the stated weighted path.
        x = [10, 10, 10, 40]
        laplacian = [[.25, -.25, 0, 0], [-.25, 1.25, -1, 0],
                     [0, -1, 1.25, -.25], [0, 0, -.25, .25]]
        quadratic = sum(x[i] * laplacian[i][j] * x[j]
                        for i in range(4) for j in range(4))
        result, _ = network(CASES["network"])
        self.assertEqual(quadratic, result["original_energy"])
        self.assertEqual(quadratic, result["coarse_energy"])

    def test_shortest_paths_by_enumeration(self):
        # Add an alternative route; enumerate all simple paths independently.
        edges = [(0, 1, 4), (1, 2, 1), (2, 3, 4), (0, 3, 12)]
        weights = {(i, j): m for a, b, m in edges for i, j in [(a, b), (b, a)]}
        actual = distances(4, edges)
        for origin in range(4):
            for target in range(4):
                if origin == target:
                    self.assertEqual(actual[origin][target], 0)
                    continue
                interior = [v for v in range(4) if v not in [origin, target]]
                costs = []
                for size in range(3):
                    for middle in permutations(interior, size):
                        path = [origin, *middle, target]
                        pairs = list(zip(path, path[1:]))
                        if all(edge in weights for edge in pairs):
                            costs.append(sum(weights[edge] for edge in pairs))
                self.assertEqual(actual[origin][target], min(costs))

    def test_access_and_population_weights(self):
        case = deepcopy(CASES["network"])
        result, rows = network(case)
        self.assertEqual([r["original_minutes"] for r in rows], [9, 5, 4, 0])
        self.assertEqual(result["original_access_share"], 300 / 400)
        self.assertEqual(result["naive_coarse_access_share"], 400 / 400)
        case["population"] = [700, 100, 100, 100]
        weighted, _ = network(case)
        self.assertEqual(weighted["original_access_share"], 300 / 1000)
        case["access_threshold_minutes"] = 4
        boundary, _ = network(case)
        self.assertEqual(boundary["original_access_share"], 200 / 1000)

    def test_identity_partition(self):
        case = deepcopy(CASES["network"])
        case["group"] = [0, 1, 2, 3]
        result, rows = network(case)
        self.assertEqual(result["reduction"], 0)
        for row in rows:
            self.assertEqual(row["original_minutes"], row["naive_coarse_minutes"])

    def test_full_group_purity_by_exhaustion(self):
        for y in product([0, 1], repeat=5):
            fitted = majority(y)
            achieved = sum(v == fitted for v in y)
            ceiling = max(sum(v == constant for v in y) for constant in [0, 1])
            self.assertEqual(achieved, ceiling)
        result = labels(CASES["labels"])["purity"]
        self.assertEqual(result["global_majority_test_score"], 1)
        self.assertEqual(result["training_only_test_score"], 0)
        self.assertEqual(result["alternative_global_score"], 0)
        self.assertEqual(result["alternative_own_ceiling"], 1)

    def test_minority_confusion_counts(self):
        result = labels(CASES["labels"])["minority"]
        # Six true negatives, two false negatives, no positive predictions.
        self.assertEqual(result["correct"], 6)
        self.assertEqual(result["class_one_people"], 2)
        self.assertEqual(result["accuracy"], 6 / 8)
        self.assertEqual(result["recall"], 0 / 2)

    def test_heldout_label_intervention(self):
        result = labels(CASES["labels"])["parameter"]
        self.assertEqual(result["all_edges_before"], 0)
        self.assertEqual(result["all_edges_after"], .5)
        self.assertEqual(result["training_edges_before"], result["training_edges_after"])

    def test_empty_training_group(self):
        with self.assertRaises(ValueError):
            majority([])


if __name__ == "__main__":
    unittest.main()
