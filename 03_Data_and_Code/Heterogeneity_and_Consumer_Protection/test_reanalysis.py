"""Independent numerical and interpretation checks for the teaching reanalysis."""
import unittest
import numpy as np
import pandas as pd
from scipy.integrate import quad
from scipy.stats import norm
import heterogeneity_reanalysis as h


class ReanalysisChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = pd.read_csv(h.ROOT / "data/cheese.csv")
        cls.est = pd.read_csv(h.OUT / "account_estimates.csv")
        cls.par = pd.read_csv(h.OUT / "mixture_parameters.csv")

    def test_preserved_population(self):
        self.assertEqual(len(self.data), 5555)
        self.assertEqual(self.data.RETAILER.nunique(), 88)
        self.assertEqual(self.est.observations.sum(), 5555)
        self.assertEqual(set(self.est.account), set(self.data.RETAILER))

    def test_price_slopes_by_partial_regression(self):
        for _, row in self.est.iterrows():
            data = self.data[self.data.RETAILER == row.account]
            controls = np.column_stack([np.ones(len(data)), data.DISP])
            q, _, _ = np.linalg.svd(controls, full_matrices=False)
            rank = np.linalg.matrix_rank(controls)
            q = q[:, :rank]
            x, y = np.log(data.PRICE.to_numpy()), np.log(data.VOLUME.to_numpy())
            rx, ry = x-q@(q.T@x), y-q@(q.T@y)
            self.assertAlmostEqual(float(rx@ry/(rx@rx)), row.price_slope, places=9)

    def test_integral_against_quadrature(self):
        p = self.par[self.par.components == 2]
        weights, means, scales = p.weight.to_numpy(), p['mean'].to_numpy(), p.sd.to_numpy()
        for i in (0, 22, 44, 66, 87):
            b, se = self.est.iloc[i][['price_slope', 'model_se']]
            value = sum(w*quad(lambda beta: norm.pdf(b, beta, se)*norm.pdf(beta, mu, sd),
                               -40, 20, epsabs=1e-11)[0]
                        for w, mu, sd in zip(weights, means, scales))
            closed = np.exp(h.marginal_log_density(np.array([b]), np.array([se]),
                                                   weights, means, scales)[0])
            self.assertAlmostEqual(value, closed, places=8)

    def test_mixture_label_invariance(self):
        p = self.par[self.par.components == 2]
        fit = dict(weights=p.weight.to_numpy(), means=p['mean'].to_numpy(), scales=p.sd.to_numpy())
        b, se = self.est.price_slope.to_numpy(), self.est.model_se.to_numpy()
        a = h.posterior(b, se, fit)
        reverse = h.posterior(b, se, {k:v[::-1] for k,v in fit.items()})
        np.testing.assert_allclose(a, reverse, rtol=1e-12, atol=1e-12)

    def test_equivalence_preserves_each_likelihood(self):
        data = pd.read_csv(h.OUT / 'observational_equivalence.csv')
        self.assertLess(data.maximum_log_density_gap.max(), 1e-10)
        for _, group in data.groupby('components'):
            np.testing.assert_allclose(group.log_likelihood, group.log_likelihood.iloc[0])
            np.testing.assert_allclose(group.mean_latent_taste+group.imposed_gamma,
                                       group.mean_observed_response)

    def test_model_selection_preserves_contrary_result(self):
        data = pd.read_csv(h.OUT / 'model_comparison.csv').set_index('components')
        self.assertGreater(data.loc[2,'log_likelihood'], data.loc[1,'log_likelihood'])
        # Extra in-sample fit does not win this BIC comparison.
        self.assertGreater(data.loc[2,'bic'], data.loc[1,'bic'])
        for _, group in self.par.groupby('components'):
            self.assertAlmostEqual(group.weight.sum(), 1)
            self.assertTrue((group.sd > 0).all())

    def test_equivalent_state_error_identity(self):
        data = pd.read_csv(h.OUT / 'equivalent_state_errors.csv')
        np.testing.assert_allclose(data.false_flag_rate+data.constructed_harm_miss_rate, 1)


if __name__ == '__main__':
    unittest.main()
