"""Independent numerical, stale-output, and execution-location checks."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

from reproduce_recommendation import ROOT, SOURCE, calculate


class RecommendationChecks(unittest.TestCase):
    def test_independent_weighting_arithmetic(self):
        result = calculate()
        self.assertAlmostEqual(result["response_mean"], (2*1 + 3*3 + 4*6 + 5*10)/20)
        self.assertAlmostEqual(result["equal_persona_mean"], (4.25 + 3.70)/2)
        self.assertAlmostEqual(result["equal_row_mean"], (2*4.25 + 3.70)/3)
        self.assertEqual((result["response_rows"], result["personas"]), (3, 2))

    def test_identical_repeats_change_only_row_weighting(self):
        rows = calculate()["repeat_sensitivity"]
        self.assertEqual([r["p01_repeats"] for r in rows], list(range(1, 6)))
        for row in rows:
            self.assertAlmostEqual(row["equal_persona_mean"], 3.975)
        self.assertAlmostEqual(rows[-1]["equal_row_mean"], 24.95/6)
        self.assertTrue(all(a["equal_row_mean"] < b["equal_row_mean"]
                            for a, b in zip(rows, rows[1:])))

    def test_undefined_values_remain_distinct_from_zero(self):
        rows = {r["candidate"]: r for r in calculate()["screening"]}
        self.assertIsNone(rows["pooled"]["pearson"])
        self.assertIsNone(rows["pooled"]["selected"])
        self.assertIsNone(rows["pooled"]["top_two_recall"])
        self.assertEqual(rows["reversed"]["selected"], ["F", "E"])
        self.assertEqual(rows["reversed"]["top_two_recall"], 0)

    def test_stale_table_stops_report(self):
        with tempfile.TemporaryDirectory() as folder:
            copy = Path(folder) / "Synthetic_Consumers"
            shutil.copytree(SOURCE, copy)
            path = copy / "results/concept_ratings.json"
            rows = json.loads(path.read_text())
            rows[0]["mean_rating"] = 5.0
            path.write_text(json.dumps(rows))
            with self.assertRaisesRegex(ValueError, "concept_ratings"):
                calculate(copy)

    def test_missing_table_stops_report(self):
        with tempfile.TemporaryDirectory() as folder:
            copy = Path(folder) / "Synthetic_Consumers"
            shutil.copytree(SOURCE, copy)
            (copy / "results/screening_details.json").unlink()
            with self.assertRaises(FileNotFoundError):
                calculate(copy)

    def test_execution_locations_and_moved_project(self):
        with tempfile.TemporaryDirectory() as folder:
            moved = Path(folder) / "moved course" / "03_Data_and_Code"
            moved.mkdir(parents=True)
            shutil.copytree(SOURCE, moved / SOURCE.name)
            shutil.copytree(ROOT, moved / ROOT.name)
            script = moved / ROOT.name / "reproduce_recommendation.py"
            output = moved / ROOT.name / "results"
            snapshots = []
            for cwd in [moved.parent, script.parent, Path(folder)]:
                subprocess.run([sys.executable, str(script)], cwd=cwd,
                               check=True, capture_output=True)
                snapshots.append(tuple((output / name).read_bytes()
                    for name in ["evidence.json", "recommendation.md"]))
            self.assertEqual(snapshots[0], snapshots[1])
            self.assertEqual(snapshots[1], snapshots[2])
            self.assertAlmostEqual(json.loads(snapshots[0][0])["equal_persona_mean"], 3.975)


if __name__ == "__main__":
    unittest.main()
