"""Hand-checkable boundary, denominator, and cost checks for original examples."""
import csv
import unittest
from pathlib import Path
from drafting_simulation import decode
from service_evaluation import make_cases, make_observations, summarize

ROOT = Path(__file__).resolve().parent


class Examples(unittest.TestCase):
    def test_eos_only(self):
        out, rows = decode(["<EOS>"], [0.1], 12, 1)
        self.assertEqual(out, ["<EOS>"])
        self.assertEqual((rows[0]["emitted"], rows[0]["target_token"]), (1, 0))

    def test_accepted_prefix_and_bonus(self):
        out, rows = decode(["a", "b", "c", "<EOS>"], [0.1] * 4, 2, 1)
        self.assertEqual(out, ["a", "b", "c", "<EOS>"])
        self.assertEqual([r["emitted"] for r in rows], [3, 1])
        self.assertEqual([r["proposed"] for r in rows], [2, 1])
        self.assertAlmostEqual(sum(r["draft_ms"] + r["verify_ms"] for r in rows), 9.79)

    def test_rejected_suffix_is_charged(self):
        _, rows = decode(["a", "b", "c", "<EOS>"], [0.1, 0.9, 0.1, 0.1], 3, 0.5)
        self.assertEqual((rows[0]["accepted"], rows[0]["emitted"]), (1, 2))
        self.assertAlmostEqual(rows[0]["draft_ms"], 0.75)

    def test_baseline_and_zero_acceptance(self):
        target = ["a", "b", "<EOS>"]
        for k in (0, 8):
            out, rows = decode(target, [0.5] * 3, k, 0)
            self.assertEqual(out, target)
            self.assertEqual(len(rows), 3)
        _, rows = decode(target, [0.5] * 3, 0, 0)
        self.assertEqual(sum(r["verify_ms"] for r in rows), 12)

    def test_invalid_termination(self):
        for target in ([], ["a"], ["<EOS>", "<EOS>"]):
            with self.assertRaises(ValueError):
                decode(target, [0.1] * len(target), 2, 0.5)

    def test_service_policy_boundary(self):
        cases = make_cases()
        self.assertEqual(sum(r["eligible"] for r in cases), 6)
        self.assertTrue(cases[2]["eligible"])
        self.assertFalse(cases[3]["eligible"])
        self.assertFalse(cases[4]["eligible"])

    def test_failure_denominator_and_cost(self):
        teacher, responses = make_observations(make_cases())
        a, b = summarize(teacher, responses)
        self.assertEqual((a["reference_tokens"], a["correct_reference_tokens"]), (120, 116))
        self.assertEqual((b["reference_tokens"], b["correct_reference_tokens"]), (120, 119))
        self.assertEqual((a["attempted"], a["correct_answers"], a["correctly_resolved"]), (12, 9, 8))
        self.assertEqual((b["completed"], b["failed"], b["correct_answers"], b["correctly_resolved"]), (10, 2, 8, 7))
        self.assertAlmostEqual(a["total_cost_dollars"], 0.848)
        self.assertAlmostEqual(b["total_cost_dollars"], 1.024)
        self.assertAlmostEqual(b["answer_accuracy_per_attempt"], 2 / 3)

    def test_zero_resolutions_and_all_failures(self):
        teacher, responses = make_observations(make_cases())
        for row in responses:
            row.update(status="timeout", answer_correct=False, correctly_resolved=False)
        for row in summarize(teacher, responses):
            self.assertEqual(row["failed"], 12)
            self.assertIsNone(row["cost_per_correct_resolution"])
            self.assertIsNone(row["answer_accuracy_among_completed"])

    def test_saved_aggregates_and_choice(self):
        with (ROOT / "results/decoding_summary.csv").open() as stream:
            rows = list(csv.DictReader(stream))
        self.assertEqual(len(rows), 74)
        self.assertEqual({int(r["emitted_including_eos"]) for r in rows}, {684})
        curve = {int(r["k"]): r for r in rows
                 if r["split"] == "development" and r["regime"] == "aligned"}
        self.assertGreater(float(curve[12]["block_efficiency"]), float(curve[4]["block_efficiency"]))
        self.assertLess(float(curve[12]["total_tokens_per_second"]), float(curve[4]["total_tokens_per_second"]))
        with (ROOT / "results/frozen_choices.csv").open() as stream:
            for choice in csv.DictReader(stream):
                candidates = [r for r in rows if r["split"] == "development"
                              and r["regime"] == choice["regime"]]
                optimum = max(candidates, key=lambda r: (float(r["total_tokens_per_second"]), -int(r["k"])))
                self.assertEqual(int(choice["selected_k"]), int(optimum["k"]))


if __name__ == "__main__":
    unittest.main()
