"""Independent identities and invariance checks for the synthetic examples."""
import unittest
import numpy as np
from control_paths import examples, slope
from panel_covariates import calculate
from project_pipeline import construct


class DesignChecks(unittest.TestCase):
    def test_adjustment_is_invariant_to_order_and_units(self):
        observations, _ = examples()
        for case in sorted({r['case'] for r in observations}):
            rows = [r for r in observations if r['case'] == case]
            y, d, c = [np.array([r[k] for r in rows])
                       for k in ['outcome', 'treatment', 'control']]
            original = slope(y, d, c)
            self.assertAlmostEqual(original, slope(y[::-1], d[::-1], c[::-1]))
            self.assertAlmostEqual(original, slope(y + 100, d, c * 10 + 7))
            self.assertAlmostEqual(original * 1000, slope(y * 1000, d, c))

    def test_finite_population_denominators(self):
        rows, _ = examples()
        self.assertEqual(len(rows), 80)
        for case in {r['case'] for r in rows}:
            self.assertAlmostEqual(sum(r['weight'] for r in rows
                                       if r['case'] == case), 1)
        panel, _ = calculate()
        for w in [0, 1]:
            group = [r for r in panel if r['w'] == w]
            mass = sum(r['weight'] for r in group)
            treated_mass = sum(r['weight'] for r in group if r['d'])
            self.assertAlmostEqual(mass, .5)
            self.assertAlmostEqual(treated_mass / mass, .25 + .5 * w)

    def test_total_effect_and_covariate_balance(self):
        rows, _ = calculate()
        for row in rows:
            y_if_treated = 100 - 2 + 3 * (row['x1_untreated'] + 2) + row['e']
            y_if_untreated = 100 + 3 * row['x1_untreated'] + row['e']
            self.assertEqual(y_if_treated - y_if_untreated, 4)
        for w in [0, 1]:
            means = []
            for d in [0, 1]:
                cell = [r for r in rows if (r['w'], r['d']) == (w, d)]
                means.append(sum(r['weight'] * r['x1_untreated'] for r in cell)
                             / sum(r['weight'] for r in cell))
            self.assertAlmostEqual(means[0], means[1])

    def test_exposure_is_distinct_from_operating_status(self):
        data = construct()
        last = {r['utility']: r for r in data['project_panel.csv']
                if r['period'] == 2}
        self.assertEqual(last['pending']['state'], 'committed')
        self.assertEqual(last['pending']['operating'], 0)
        self.assertEqual(last['pending']['price_usd_mwh'], 106)
        self.assertEqual(last['cancelled']['operating'], 0)
        self.assertGreater(last['cancelled']['price_usd_mwh'],
                           last['unexposed']['price_usd_mwh'])
        sensitivity = data['donor_sensitivity.csv']
        self.assertTrue(all(r['gap'] == 10 for r in sensitivity
                            if r['cancelled_donor_weight'] == 0))
        self.assertTrue(any(r['gap'] < 0 for r in sensitivity))
        selected = data['selected_populations.csv']
        self.assertGreater(selected[0]['operating_mean'], selected[0]['proposal_mean'])
        self.assertLess(selected[1]['operating_mean'], 0)
        self.assertGreater(selected[1]['proposal_mean'], 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
