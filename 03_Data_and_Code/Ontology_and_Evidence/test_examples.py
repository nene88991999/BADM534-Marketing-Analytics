"""Independent expected cases for the synthetic service-record assessment."""
from copy import deepcopy
from pathlib import Path
import json
import unittest
from assess_cancellations import calculate

DATA = json.loads((Path(__file__).parent / "data/cancellation_records.json").read_text())


class EvidenceTests(unittest.TestCase):
    def test_expected_records_and_denominators(self):
        result = calculate(DATA)
        self.assertEqual(result["accepted_unique_events"], 4)
        self.assertEqual(result["subscription_denominator"], 4)
        self.assertEqual(result["valid_request_denominator"], 2)
        self.assertEqual(result["confirmed_subscription_ids"], ["s2"])
        self.assertEqual(result["request_ids_to_review"], ["r1"])
        self.assertEqual(result["confirmed_share"], 0.25)
        self.assertEqual(result["request_as_completion_share"], 0.5)

    def test_each_rejected_or_duplicate_row_has_a_reason(self):
        result = calculate(DATA)
        found = {(r["event_id"], r["reason"]) for r in result["flags"]}
        self.assertEqual(found, {("r2", "exact_duplicate"), ("r4", "invalid_timestamp"),
                                 ("c1_later", "after_cutoff"),
                                 ("c1_early", "confirmation_before_request")})
        self.assertEqual(sum(r["rows"] for r in result["flags"]) + 4, 8)

    def test_unknown_differs_from_observed_active(self):
        rows = {r["subscription_id"]: r for r in calculate(DATA)["evidence"]}
        self.assertEqual(rows["s4"]["evidence_state"], "unknown")
        self.assertIsNone(rows["s4"]["state_observed_at"])
        self.assertEqual(rows["s3"]["evidence_state"], "observed_active")
        self.assertEqual(rows["s3"]["state_observed_at"], "2027-01-30T12:00:00+00:00")

    def test_reporting_cutoff_changes_available_evidence(self):
        data = deepcopy(DATA); data["cutoff"] = "2027-02-02T00:00:00+00:00"
        result = calculate(data)
        self.assertEqual(result["confirmed_subscription_ids"], ["s1", "s2"])
        self.assertEqual(result["request_ids_to_review"], [])

    def test_conflicting_duplicates_do_not_depend_on_row_order(self):
        data = deepcopy(DATA); data["events"][2]["subscription_id"] = "s3"
        result = calculate(data)
        self.assertEqual(result["confirmed_subscription_ids"], [])
        self.assertIn("conflicting_duplicate", {f["reason"] for f in result["flags"]})
        data["events"].reverse()
        other = calculate(data)
        self.assertEqual(result, other)

    def test_confirmation_must_match_subscription(self):
        data = deepcopy(DATA); data["events"][3]["subscription_id"] = "s3"
        result = calculate(data)
        self.assertEqual(result["request_ids_to_review"], ["r1", "r2"])
        self.assertIn("subscription_mismatch", {f["reason"] for f in result["flags"]})

    def test_simultaneous_conflicting_state_is_explicit(self):
        data = deepcopy(DATA)
        data["events"].append({"event_id": "a2", "subscription_id": "s2",
                               "kind": "active_observation", "at": "2027-01-26T11:00:00+00:00"})
        rows = {r["subscription_id"]: r for r in calculate(data)["evidence"]}
        self.assertEqual(rows["s2"]["evidence_state"], "conflicting_state_observations")

    def test_invalid_roster_is_rejected(self):
        for roster in ([], [DATA["subscriptions"][0]] * 2):
            data = deepcopy(DATA); data["subscriptions"] = roster
            with self.assertRaises(ValueError):
                calculate(data)


if __name__ == "__main__":
    unittest.main()
