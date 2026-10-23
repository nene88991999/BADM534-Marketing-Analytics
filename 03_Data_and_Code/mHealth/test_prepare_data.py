"""Check transformation rules using invented records only."""
import unittest
import gzip
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import numpy as np
import pandas as pd

from prepare_data import Transformer


class TransformationTests(unittest.TestCase):
    def setUp(self):
        self.source = pd.DataFrame({
            "Userid": ["101", "101", "102"],
            "Fancydate": ["2016-01-01 00:00:00", "2016-01-02 00:00:00", "2016-01-01 00:00:00"],
            "Birthday": ["1990-07-01", "1990-07-01", "1980-01-01"],
            "Age": [25, 25, 36],
            "Currentweight": [180.0, 180.0, 0.01],
            "Startweight": [190.0, 190.0, 0.0],
            "Minweight": [175.0, 175.0, -1.0],
            "Maxweight": [195.0, 195.0, 0.001],
            "Goalweight": [170.0, 170.0, 0.5],
            "Heightinches": [70.0, 70.0, 0.0],
            "Bmi": [25.8, 25.8, 0.0],
            "Currenteer": [2000, 2000, 0],
            "Foodcalories": [500.0, 600.0, 0.0],
            "Image": ["private-path", "private-path", "private-path"],
        })
        self.transformer = Transformer(b"a" * 32)  # Invented test key only.

    def test_fields_ages_and_originals(self):
        original = self.source.copy(deep=True)
        result = self.transformer.transform(self.source, food=True)
        for column in ["Birthday", "Age", "Image", "Currenteer", "Bmi"]:
            self.assertNotIn(column, result)
        self.assertEqual(result.Age_at_2016_01_01.tolist(), [25, 25, 36])
        self.assertEqual(result.Userid.nunique(), 2)
        self.assertTrue(result.Userid.str.fullmatch(r"L[0-9a-f]{24}").all())
        pd.testing.assert_frame_equal(original, self.source)
        pd.testing.assert_series_equal(result.Foodcalories, original.Foodcalories)

    def test_repeat_and_cross_file_consistency(self):
        first = self.transformer.transform(self.source, food=True)
        repeated = self.transformer.transform(self.source, food=True)
        pd.testing.assert_frame_equal(first, repeated)
        daily_source = self.source[["Userid", "Fancydate", "Currentweight", "Currenteer", "Image", "Foodcalories"]]
        daily = self.transformer.transform(daily_source, food=False)
        for column in ["Userid", "Fancydate", "Currentweight", "Age_at_2016_01_01"]:
            pd.testing.assert_series_equal(first[column], daily[column])
        self.assertNotEqual(first.Currentweight.iloc[0], first.Currentweight.iloc[1])

    def test_noise_bounds_small_values_and_bmi(self):
        result = self.transformer.transform(self.source, food=True)
        for column in ["Currentweight", "Startweight", "Minweight", "Maxweight", "Goalweight"]:
            delta = (result[column] - self.source[column]).abs()
            self.assertTrue((delta <= 1.0005).all())
            positive = self.source[column] > 0
            self.assertTrue((result.loc[positive, column] > 0).all())
            pd.testing.assert_series_equal(result.loc[~positive, column], self.source.loc[~positive, column])
        expected = round(703 * result.Currentweight.iloc[0] / 70**2, 3)
        self.assertEqual(result.Bmi_from_noisy_weight.iloc[0], expected)
        self.assertTrue(np.isnan(result.Bmi_from_noisy_weight.iloc[2]))
        self.assertAlmostEqual(result.Currentweight.iloc[0] - result.Goalweight.iloc[0], 10)


class ProviderLabelTests(unittest.TestCase):
    def test_label_replacement_and_idempotent_manifest(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            data = root / "food_entries.csv.gz"
            with gzip.open(data, "wt") as stream:
                stream.write('Userid,Name,Calories\nL123,"ExampleVendor oats, plain",200\nL456,Other food,300\n')
            manifest = {"files": {data.name: {"sha256": hashlib.sha256(data.read_bytes()).hexdigest()}}}
            (root / "manifest.json").write_text(json.dumps(manifest))
            pattern = root / "pattern.txt"
            pattern.write_text("ExampleVendor")
            command = [sys.executable, str(Path(__file__).parent / "redact_provider.py"), "--directory", str(root), "--pattern-file", str(pattern)]
            subprocess.run(command, check=True, capture_output=True)
            first_hash = hashlib.sha256(data.read_bytes()).hexdigest()
            result = pd.read_csv(data)
            self.assertEqual(result.Name.tolist(), ["mHealth oats, plain", "Other food"])
            self.assertEqual(result.Calories.tolist(), [200, 300])
            subprocess.run(command, check=True, capture_output=True)
            self.assertEqual(first_hash, hashlib.sha256(data.read_bytes()).hexdigest())
            final = json.loads((root / "manifest.json").read_text())
            self.assertEqual(final["provider_label_standardization"]["occurrences_replaced"][data.name], 1)


if __name__ == "__main__":
    unittest.main()
