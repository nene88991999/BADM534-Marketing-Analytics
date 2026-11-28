"""Independent arithmetic, counterexample, and preservation checks."""
import math
from pathlib import Path
import tempfile
import unittest
from evidence_example import (append_record, contract_errors, make_claims,
                              reconstruct, record_errors, revision_example)


class EvidenceChecks(unittest.TestCase):
    def setUp(self):
        self.values = reconstruct()
        self.sources = {"table": {}, "manager-approval": {}}
        self.claims = {c["id"]: c for c in make_claims(self.values)}

    def test_independent_normal_calculation(self):
        scale = 100 * 456 / 6804
        self.assertAlmostEqual(self.values["estimate"], .261 * scale, places=12)
        self.assertAlmostEqual(self.values["p_zero"], math.erfc(.261 / .158 / math.sqrt(2)), places=12)
        self.assertLess(self.values["ci95_low"], 0)
        self.assertGreater(self.values["upper95"], 3)

    def test_same_metadata_can_carry_opposite_meaning(self):
        valid, misleading = self.claims["nonrejection"], self.claims["mismatched-text"]
        for key in ("quantity", "value", "target", "sources", "units"):
            self.assertEqual(valid[key], misleading[key])
        self.assertNotEqual(valid["statement"], misleading["statement"])
        self.assertEqual(contract_errors(valid, self.sources, self.values), [])
        self.assertEqual(contract_errors(misleading, self.sources, self.values), [])
        self.assertNotEqual(valid["reference_acceptable"], misleading["reference_acceptable"])

    def test_human_approval_supplies_no_missing_measurement(self):
        for key in ("household-assurance", "approved-assurance"):
            self.assertEqual(record_errors(self.claims[key], self.sources), [])
            self.assertIn("recorded outcome does not measure the claimed target",
                          contract_errors(self.claims[key], self.sources, self.values))

    def test_missing_source_and_wrong_number(self):
        self.assertTrue(record_errors(self.claims["missing-source"], self.sources))
        self.assertEqual(record_errors(self.claims["wrong-number"], self.sources), [])
        self.assertIn("number disagrees with the reconstruction",
                      contract_errors(self.claims["wrong-number"], self.sources, self.values))

    def test_reference_labels_do_not_control_checker(self):
        for claim in self.claims.values():
            flipped = {**claim, "reference_acceptable": not claim["reference_acceptable"]}
            self.assertEqual(contract_errors(claim, self.sources, self.values),
                             contract_errors(flipped, self.sources, self.values))

    def test_exclusive_creation_and_revisions(self):
        history, checks = revision_example()
        self.assertTrue(all(checks.values()))
        self.assertEqual(history[1]["supersedes"], history[0]["id"])
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(ValueError):
                append_record(directory, {"id": "../escape"})
            self.assertEqual(list(Path(directory).iterdir()), [])


if __name__ == "__main__":
    unittest.main()
