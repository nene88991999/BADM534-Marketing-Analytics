"""Independent small cases and a SQL cross-check of the released tasks."""
import csv
import json
import sqlite3
import unittest
from datetime import date
from pathlib import Path

from evaluate_submission import grade
from logging_reference import calculate, read_csv
from workflow_costs import calculate as costs

HERE = Path(__file__).resolve().parent


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.roster = [{"user_id": u} for u in ["A", "B", "C"]]
        self.records = [{"user_id": u, "date": d} for u, d in [
            ("A", "2016-06-30"), ("A", "2016-07-01"), ("A", "2016-07-01"),
            ("B", "2016-07-31"), ("B", "2016-08-01"), ("Z", "2016-07-03")]]
        self.start, self.end = date(2016, 7, 1), date(2016, 8, 1)

    def reference(self):
        return calculate(self.roster, self.records, self.start, self.end)

    def test_distinct_days_boundaries_and_zero_users(self):
        rows, summary = self.reference()
        self.assertEqual([r["logged_days"] for r in rows], [1, 1, 0])
        self.assertEqual(summary["possible_user_days"], 93)
        self.assertEqual(summary["excluded_input_rows"], 3)
        self.assertAlmostEqual(summary["mean_logging_rate"], 2 / 93)

    def test_duplicate_roster_rejected(self):
        with self.assertRaises(ValueError):
            calculate(self.roster + [self.roster[0]], [], self.start, self.end)

    def test_invalid_dates_and_windows_rejected(self):
        with self.assertRaises(ValueError):
            calculate(self.roster, [{"user_id": "A", "date": "07/01/2016"}], self.start, self.end)
        with self.assertRaises(ValueError):
            calculate(self.roster, [], self.end, self.start)

    def test_valid_reference_accepted(self):
        rows, _ = self.reference()
        self.assertTrue(grade(rows, rows)["valid_output"])

    def test_equal_total_wrong_customers_rejected(self):
        rows, _ = self.reference()
        wrong = [dict(r) for r in rows]
        for r, n in zip(wrong, [0, 1, 1]):
            r.update(logged_days=n, logging_rate=n / 31)
        self.assertEqual(sum(r["logged_days"] for r in rows), sum(r["logged_days"] for r in wrong))
        self.assertFalse(grade(wrong, rows)["valid_output"])

    def test_missing_duplicate_and_nonfinite_rejected(self):
        rows, _ = self.reference()
        self.assertFalse(grade(rows[:-1], rows)["valid_output"])
        self.assertFalse(grade(rows + rows[:1], rows)["valid_output"])
        wrong = [dict(r) for r in rows]
        wrong[0]["logging_rate"] = "nan"
        self.assertFalse(grade(wrong, rows)["valid_output"])

    def test_cost_denominator_includes_failed_work(self):
        a, b = costs()["cases"]
        self.assertEqual((a["total_dollars"], b["total_dollars"]), (350, 200))
        self.assertAlmostEqual(a["dollars_per_valid_task"], 350 / 80)
        self.assertAlmostEqual(b["dollars_per_valid_task"], 200 / 95)

    def test_actual_task_outputs_against_sql(self):
        for role in ["development", "evaluation"]:
            task = HERE / "tasks" / role
            spec = json.loads((task / "task.json").read_text())
            roster, records = read_csv(task / "roster.csv"), read_csv(task / "observed_days.csv")
            with sqlite3.connect(":memory:") as db:
                db.execute("CREATE TABLE roster(user_id TEXT PRIMARY KEY)")
                db.execute("CREATE TABLE events(user_id TEXT, day TEXT)")
                db.executemany("INSERT INTO roster VALUES (?)", [(r["user_id"],) for r in roster])
                db.executemany("INSERT INTO events VALUES (?,?)", [(r["user_id"], r["date"]) for r in records])
                actual = dict(db.execute("""SELECT r.user_id, COUNT(DISTINCT e.day)
                    FROM roster r LEFT JOIN events e ON r.user_id=e.user_id
                    AND e.day>=? AND e.day<? GROUP BY r.user_id""", (spec["start"], spec["end_exclusive"])))
            saved = read_csv(HERE / "results" / f"{role}_reference.csv")
            self.assertEqual(actual, {r["user_id"]: int(r["logged_days"]) for r in saved})


if __name__ == "__main__":
    unittest.main(verbosity=2)
