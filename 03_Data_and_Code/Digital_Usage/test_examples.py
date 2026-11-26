"""Independent arithmetic, source, and sample checks for the course examples."""
import csv
import itertools
import math
from pathlib import Path
import unittest
import numpy as np
import pandas as pd
from assess_release import zip_strings, nonnegative, ratio
from compare_models import fit
from cluster_usage import kmeans, adjusted_rand
from verify_index import compare, MINUTES, WEIGHTS, PUBLISHED

ROOT = Path(__file__).resolve().parent


class Examples(unittest.TestCase):
    def test_postal_restoration(self):
        self.assertEqual(zip_strings(pd.Series(["1001", "60601"])).tolist(), ["01001", "60601"])
        for value in [None, "ABC12", "123456", "123.0", "601"]:
            with self.assertRaises(ValueError):
                zip_strings(pd.Series([value]))

    def test_missing_and_denominators(self):
        x = nonnegative(pd.Series([10, -666666666, "-", None]))
        self.assertEqual(x.iloc[0], 10)
        self.assertEqual(x.isna().sum(), 3)
        result = ratio(pd.Series([1., 0., 2., 1.]), pd.Series([2., 0., 1., np.nan]))
        self.assertEqual(result.iloc[0], .5)
        self.assertEqual(result.isna().sum(), 3)

    def test_income_boundaries(self):
        data = pd.read_csv(ROOT / 'results/joined_areas.csv')
        boundary = data.B19013_E001.isin([2499, 250001])
        self.assertEqual(int(boundary.sum()), 50)
        self.assertTrue(data.loc[boundary, 'income_10k'].isna().all())
        self.assertEqual(int(data.regression_eligible.sum()), 28511)
        self.assertEqual(len(data[data.state.eq('IL')]), 1253)

    def test_independent_source_join(self):
        with (ROOT / "data/published_indices.csv").open() as f:
            raw = {r['ZIP_CODE'].zfill(5): r for r in csv.DictReader(f)}
        with (ROOT / "data/acs2021_zcta.csv").open() as f:
            acs = {r['zcta']: r for r in csv.DictReader(f)}
        output = pd.read_csv(ROOT / 'results/joined_areas.csv', dtype={'zip': str}).set_index('zip')
        self.assertEqual(set(output.index), set(raw))
        self.assertEqual(len(raw), 28561)
        for code in ['01001', '60601', '61801', '61820']:
            self.assertAlmostEqual(output.loc[code, 'mci'], float(raw[code]['MEDIA AND INFORMATION INDEX']))
            row = acs[code]
            degree = sum(int(row[f'B15003_E{n:03d}']) for n in [22, 23, 24, 25])
            self.assertAlmostEqual(output.loc[code, 'college_share'], degree / int(row['B15003_E001']))

    def test_ols_hand_calculation(self):
        x = np.array([-2., -1., 0., 1., 2.])
        y = np.array([1., 2., 2., 4., 6.])
        design = np.column_stack([np.ones(5), x])
        beta = fit(design, y, np.ones(5))
        self.assertAlmostEqual(beta[0], 3.)
        self.assertAlmostEqual(beta[1], 1.2)

    def test_weighted_equals_repeated_rows(self):
        x = np.column_stack([np.ones(3), [1., 2., 4.]])
        y, w = np.array([1., 4., 5.]), np.array([1, 3, 2])
        expected = fit(np.repeat(x, w, axis=0), np.repeat(y, w), np.ones(w.sum()))
        np.testing.assert_allclose(fit(x, y, w), expected)

    def test_partial_regression(self):
        data = pd.read_csv(ROOT / 'results/joined_areas.csv').dropna(
            subset=['income_10k', 'college_share', 'broadband_share'])
        z = np.column_stack([np.ones(len(data)), data[['college_share', 'broadband_share']]])
        x, y = data.income_10k.to_numpy(), data.cci.to_numpy()
        rx = x - z @ np.linalg.lstsq(z, x, rcond=None)[0]
        ry = y - z @ np.linalg.lstsq(z, y, rcond=None)[0]
        slope = rx @ ry / (rx @ rx)
        result = pd.read_csv(ROOT / 'results/regressions.csv')
        observed = result.query("index == 'cci' and model == 'Income, Education, Broadband'")
        self.assertAlmostEqual(slope, observed.iloc[0].income_slope_per_10000_dollars)

    def test_kmeans_exhaustive_small_case(self):
        x = np.array([[0.], [1.], [2.], [10.], [11.]])
        losses = []
        for assignment in itertools.product(range(2), repeat=5):
            a = np.array(assignment)
            if len(set(a)) == 2:
                losses.append(sum(((x[a == j] - x[a == j].mean()) ** 2).sum() for j in range(2)))
        self.assertAlmostEqual(kmeans(x, k=2)[0], min(losses))

    def test_adjusted_rand_pair_count(self):
        a, b = np.array([0, 0, 1, 1]), np.array([0, 1, 0, 1])
        self.assertAlmostEqual(adjusted_rand(a, b), -.5)
        self.assertAlmostEqual(adjusted_rand(a, 1 - a), 1.)

    def test_formula_scalar_check(self):
        stated, alternative = compare()
        manual = [sum(w * math.log(v) if v else 0 for w, v in zip(WEIGHTS, row)) for row in MINUTES]
        np.testing.assert_allclose(alternative, manual)
        np.testing.assert_array_equal(np.round(alternative, 2), PUBLISHED)
        self.assertTrue(np.all(np.abs(stated - PUBLISHED) > 1))
        self.assertAlmostEqual(np.average(PUBLISHED, weights=MINUTES.sum(1)),
                               (1260 * 4.46 + 1740 * 3.09 + 655 * 3.47) / 3655)

    def test_cluster_accounting(self):
        data = pd.read_csv(ROOT / 'results/illinois_clusters.csv')
        summary = pd.read_csv(ROOT / 'results/cluster_summary.csv')
        self.assertEqual(len(data), 1253)
        self.assertEqual(summary.areas.sum(), len(data))
        for row in summary.itertuples():
            group = data[data.cluster == row.cluster]
            self.assertAlmostEqual(math.fsum(group.mci) / len(group), row.mci)
            self.assertAlmostEqual(math.fsum(group.cci) / len(group), row.cci)


if __name__ == '__main__':
    unittest.main()
