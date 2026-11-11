"""Small independent checks for denominators, missing decisions, and paired inputs."""
import copy
import unittest
from evaluate_graders import evaluate
from source_selection import assess


class EvaluationChecks(unittest.TestCase):
    def setUp(self):
        self.cases = [dict(id="p", reference="PASS"), dict(id="f", reference="FAIL")]

    def rows(self, *pairs):
        return [dict(grader="g", case_id=k, prediction=v) for k, v in pairs]

    def test_constant_grader(self):
        r = evaluate(self.cases, self.rows(("p", "PASS"), ("f", "PASS")))[0]
        self.assertEqual((r["balanced_accuracy_all"], r["false_pass_rate"], r["loss_units"]), (.5, 1, 10))

    def test_missing_case_is_retained(self):
        r = evaluate(self.cases, self.rows(("p", "PASS")))[0]
        self.assertEqual((r["missing"], r["coverage"], r["balanced_accuracy_all"], r["accuracy_answered"]), (1, .5, .5, 1))

    def test_invalid_and_abstention_are_distinct(self):
        r = evaluate(self.cases, self.rows(("p", "perhaps"), ("f", "ABSTAIN")))[0]
        self.assertEqual((r["invalid"], r["abstained"], r["answered"], r["accuracy_answered"]), (1, 1, 0, None))
        self.assertEqual(r["loss_units"], 1)

    def test_duplicate_and_unknown_ids_fail(self):
        for pairs in [[("p", "PASS"), ("p", "PASS")], [("unknown", "FAIL")]]:
            with self.assertRaises(ValueError):
                evaluate(self.cases, self.rows(*pairs))

    def test_absent_reference_class_fails(self):
        with self.assertRaises(ValueError):
            evaluate(self.cases[:1], self.rows(("p", "PASS")))

    def test_citation_does_not_establish_support(self):
        data = dict(sources=[dict(id="s")], questions=[dict(id="q")],
            conditions={"one": ["s"]}, answers={"one": [dict(question_id="q", citations=["s"],
            supported=False, answer="Unjustified causal claim", reason="No causal design")]})
        _, rows = assess(data)
        self.assertEqual((rows[0]["cited"], rows[0]["supported"]), (1, 0))
        changed = copy.deepcopy(data)
        changed["answers"]["one"][0]["citations"] = ["missing"]
        with self.assertRaises(ValueError):
            assess(changed)
        changed = copy.deepcopy(data)
        changed["answers"]["one"].append(changed["answers"]["one"][0])
        with self.assertRaises(ValueError):
            assess(changed)


if __name__ == "__main__":
    unittest.main()
