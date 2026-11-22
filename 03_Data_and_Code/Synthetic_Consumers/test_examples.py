"""Independent hand cases and failure conditions for the original course programs."""
from copy import deepcopy
import json
from pathlib import Path
import unittest

import anchor_measurement as anchors
import concept_screening as screening

ROOT = Path(__file__).resolve().parent


class TestConsumerExamples(unittest.TestCase):
    def setUp(self):
        self.responses = json.loads((ROOT / "data/anchor_responses.json").read_text())
        self.panels = json.loads((ROOT / "data/concept_panels.json").read_text())

    def test_exact_normalization(self):
        result = anchors.rating_distribution([0, .1, .3, .6, .8])
        for actual, expected in zip(result, [0, 1/18, 1/6, 1/3, 4/9]):
            self.assertAlmostEqual(actual, expected)
        self.assertAlmostEqual(anchors.mean_rating(result), 25/6)

    def test_positive_affine_invariance(self):
        raw = [-.8, -.4, 0, .2, .5]
        first = anchors.rating_distribution(raw)
        second = anchors.rating_distribution([(x+1)/2 for x in raw])
        for x, y in zip(first, second):
            self.assertAlmostEqual(x, y)

    def test_uninformative_and_invalid_similarities(self):
        self.assertIsNone(anchors.rating_distribution([.2]*5))
        for bad in [[0]*4, [0, 0, float("nan"), 1, 1], [0, 0, 0, 0, 2]]:
            with self.assertRaises(ValueError):
                anchors.rating_distribution(bad)

    def test_persona_weights_survive_an_identical_repeat(self):
        before = anchors.summarize(anchors.score_responses(self.responses))
        shorter = deepcopy(self.responses)
        shorter["responses"] = [r for r in shorter["responses"] if r["repeat"] != 2]
        after = anchors.summarize(anchors.score_responses(shorter))
        for a, b in zip(before, after):
            self.assertAlmostEqual(a["mean_rating"], b["mean_rating"])
        selected = next(r for r in before if r["concept"] == "refill" and r["anchor_set"] == "set_1")
        self.assertAlmostEqual(selected["mean_rating"], (4.25+3.7)/2)
        self.assertAlmostEqual(selected["row_weighted_mean"], (4.25*2+3.7)/3)

    def test_missing_mapping_preserves_an_incomplete_aggregate(self):
        self.responses["responses"][0]["similarities"]["set_1"] = [.2]*5
        result = anchors.summarize(anchors.score_responses(self.responses))
        row = next(r for r in result if r["concept"] == "refill" and r["anchor_set"] == "set_1")
        self.assertEqual((row["response_rows"], row["scored_rows"], row["personas"]), (3,2,2))
        self.assertEqual(row["status"], "incomplete")
        self.assertIsNone(row["mean_rating"])

    def test_duplicate_and_missing_rosters(self):
        self.responses["responses"].append(deepcopy(self.responses["responses"][0]))
        with self.assertRaises(ValueError):
            anchors.score_responses(self.responses)
        del self.panels["candidates"]["pooled"]["A"]
        with self.assertRaises(ValueError):
            screening.evaluate(self.panels)

    def test_undefined_correlation_and_average_ranks(self):
        self.assertIsNone(screening.correlation([1,2,3], [4,4,4]))
        self.assertEqual(screening.ranks([4,1,1,3]), [4,1.5,1.5,3])
        self.assertAlmostEqual(screening.correlation([1,2,3], [9,7,5]), -1)

    def test_distribution_distance_and_invalid_probabilities(self):
        self.assertAlmostEqual(screening.ks_similarity([.2,.3,.5,0,0], [0,.5,.5,0,0]), .8)
        with self.assertRaises(ValueError):
            screening.validate_pmf([0,0,0,0,.9])

    def test_shortlist_boundary_ties_remain_unresolved(self):
        self.assertIsNone(screening.shortlist({"A":4,"B":3,"C":3}))
        self.assertEqual(screening.shortlist({"A":4,"B":4,"C":3}), ["A","B"])

    def test_counterexamples_match_hand_aggregates(self):
        summary, details = screening.evaluate(self.panels)
        by = {r["candidate"]:r for r in summary}
        self.assertEqual(len(details), 18)
        for name, expected in [("pooled", .925), ("reversed", .85), ("compressed", .94)]:
            self.assertAlmostEqual(by[name]["mean_ks_similarity"], expected)
        self.assertIsNone(by["pooled"]["pearson"])
        self.assertIsNone(by["pooled"]["selected"])
        self.assertAlmostEqual(by["reversed"]["pearson"], -1)
        self.assertEqual(by["reversed"]["top_two_recall"], 0)
        self.assertEqual(by["compressed"]["top_two_recall"], 1)
        self.assertAlmostEqual(by["compressed"]["mean_absolute_rating_error"], .12)


if __name__ == "__main__":
    unittest.main()
