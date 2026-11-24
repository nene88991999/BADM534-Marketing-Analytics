"""Hand calculations and invariance checks for original representation examples."""
from copy import deepcopy
from pathlib import Path
import json
import unittest
from evaluate_representations import calculate, score
from compare_decompositions import calculate as decompositions

DATA = json.loads((Path(__file__).parent / "data/cases.json").read_text())


class RepresentationTests(unittest.TestCase):
    def test_high_scale_hand_calculations(self):
        rows = calculate(DATA)["results"]
        a, b = rows[0], rows[1]
        self.assertEqual(a["variation"], [40000, 4])
        self.assertEqual(a["squared_errors"], [0, 4])
        self.assertEqual(b["squared_errors"], [16, 0])
        self.assertAlmostEqual(a["total_fvu"], 1 / 10001)
        self.assertAlmostEqual(b["total_fvu"], 4 / 10001)

    def test_common_routing_denominator(self):
        a, b = calculate(DATA)["results"][:2]
        self.assertEqual((a["review_required"], b["review_required"]), (2, 2))
        self.assertEqual((a["recall"], b["recall"]), (0, 1))
        self.assertEqual((a["accuracy"], b["accuracy"]), (0.5, 1))

    def test_scaling_reverses_aggregate_ranking(self):
        high_a, high_b, low_a, low_b = calculate(DATA)["results"]
        self.assertLess(high_a["total_fvu"], high_b["total_fvu"])
        self.assertGreater(low_a["total_fvu"], low_b["total_fvu"])
        self.assertEqual((low_a["recall"], low_b["recall"]), (0, 1))

    def test_permutation_and_replication_invariance(self):
        data = deepcopy(DATA); data["cases"].reverse()
        old = calculate(DATA)["results"]; new = calculate(data)["results"]
        for a, b in zip(old, new):
            self.assertEqual(a["total_fvu"], b["total_fvu"])
            self.assertEqual(a["recall"], b["recall"])
        points = [(-2, -1), (-2, 1), (2, -1), (2, 1)]
        reconstruction = [(p[0], 0) for p in points]
        self.assertEqual(score(points, reconstruction)["total_fvu"],
                         score(points * 2, reconstruction * 2)["total_fvu"])

    def test_degenerate_inputs_are_rejected(self):
        for x, y in (([], []), ([(1, 1)], [(1, 1)]), ([(-1, 0), (1, 0)], [(-1, 0), (1, 0)])):
            with self.assertRaises(ValueError):
                score(x, y)

    def test_distinct_decompositions_and_removal_errors(self):
        rows = decompositions()["results"]
        self.assertNotEqual(rows[0]["unit_directions"], rows[1]["unit_directions"])
        for row, expected in zip(rows, (2, 5)):
            self.assertAlmostEqual(row["reconstructed"][0], 2)
            self.assertAlmostEqual(row["reconstructed"][1], 0)
            self.assertAlmostEqual(row["squared_error_after_removing_first"], expected)


if __name__ == "__main__":
    unittest.main()
