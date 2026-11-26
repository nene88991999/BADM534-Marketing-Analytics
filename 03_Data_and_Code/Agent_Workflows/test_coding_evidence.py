"""Independent arithmetic and counterexamples for the coding-workflow additions."""
import unittest
from datetime import date

from benchmark_evidence import failure_rates, prompt_contrasts, read_csv, SOURCE
from decision_costs import WORKFLOWS, break_even, expected_cost
from semantic_checks import assess, candidate, complete


class EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.roster = [{"user_id": u} for u in ["A", "B", "C"]]
        self.records = [{"user_id": u, "date": d, "entries": str(n)} for u, d, n in [
            ("A", "2016-07-01", 4), ("A", "2016-07-02", 2),
            ("B", "2016-07-31", 3), ("B", "2016-08-01", 5)]]
        self.start, self.end = date(2016, 7, 1), date(2016, 8, 1)

    def result(self, case):
        return assess(case, self.roster, self.records, self.start, self.end)

    def test_failure_denominators(self):
        r = failure_rates([{"agency": "chatbot", "n": 10, "failures": 2, "loud": 1, "silent": 1}])[0]
        self.assertEqual((r["success_pct"], r["silent_per100"], r["silent_share_of_failures_pct"]), (80, 10, 50))

    def test_zero_failures_and_invalid_partition(self):
        r = failure_rates([{"agency": "agent", "n": 10, "failures": 0, "loud": 0, "silent": 0}])[0]
        self.assertIsNone(r["silent_share_of_failures_pct"])
        with self.assertRaises(ValueError):
            failure_rates([{"agency": "agent", "n": 10, "failures": 1, "loud": 1, "silent": 1}])

    def test_prompt_scales_by_hand(self):
        rows = [{"agency": a, "prompt": p, "panel": "prompt", "n": 100, "successes": s}
                for a in ["chatbot", "self_repair", "agent"]
                for p, s in [("zero_shot", 80), ("few_shot", 90)]]
        for r in prompt_contrasts(rows):
            self.assertAlmostEqual(r["gain_pp"], 10)
            self.assertAlmostEqual(r["fraction_of_zero_failures_removed"], 0.5)

    def test_publication_counts(self):
        r = failure_rates(read_csv(SOURCE / "appendix_silent_vs_loud.csv"))
        self.assertEqual([x["successes"] for x in r], [12052, 13434, 14021])
        self.assertEqual(sum(x["assigned"] for x in r), 43200)
        self.assertAlmostEqual(r[2]["silent_share_of_failures_pct"], 100 * 338 / 379)

    def test_correct_and_shifted_customers(self):
        self.assertEqual(self.result("correct")["classification"], "success")
        r = self.result("shifted_users")
        self.assertEqual(r["returned_days"], 3)
        self.assertTrue(r["total_days_matches"])
        self.assertEqual(r["correct_users"], 0)
        self.assertEqual(r["classification"], "silent_failure")

    def test_entry_counts_and_boundary(self):
        self.assertEqual(self.result("entry_counts")["returned_days"], 9)
        self.assertEqual(self.result("inclusive_end")["returned_days"], 4)
        self.assertEqual(self.result("entry_counts")["classification"], "silent_failure")

    def test_wrong_denominator_preserves_total(self):
        r = self.result("denominator_30")
        self.assertTrue(r["total_days_matches"])
        self.assertAlmostEqual(r["mean_returned_rate"], 1 / 30)
        self.assertEqual(r["classification"], "silent_failure")

    def test_missing_users_values_and_execution(self):
        for case in ["omit_zero", "missing_value", "execution_failure"]:
            self.assertEqual(self.result(case)["classification"], "loud_failure")
        self.assertFalse(self.result("execution_failure")["executed"])

    def test_order_and_duplicate_invariance(self):
        ref = candidate("correct", self.roster, self.records, self.start, self.end)
        reordered = candidate("correct", self.roster, self.records[::-1] + self.records[:1], self.start, self.end)
        self.assertEqual(ref, reordered)
        self.assertFalse(complete(ref[:-1] + ref[:1], ["A", "B", "C"]))
        ref[0]["logging_rate"] = float("nan")
        self.assertFalse(complete(ref, ["A", "B", "C"]))

    def test_costs_and_crossing_by_hand(self):
        self.assertAlmostEqual(break_even(*WORKFLOWS), 7)
        self.assertEqual(expected_cost(WORKFLOWS[0], 10)["expected_total_dollars"], 770)
        self.assertEqual(expected_cost(WORKFLOWS[1], 10)["expected_total_dollars"], 650)
        self.assertAlmostEqual(expected_cost(WORKFLOWS[0], 7)["expected_total_dollars"],
                               expected_cost(WORKFLOWS[1], 7)["expected_total_dollars"])

    def test_cost_domains_and_no_improvement(self):
        self.assertIsNone(break_even(WORKFLOWS[0], WORKFLOWS[0]))
        with self.assertRaises(ValueError):
            expected_cost({**WORKFLOWS[0], "undetected_error_probability": 1.1}, 0)
        with self.assertRaises(ValueError):
            expected_cost(WORKFLOWS[0], -1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
