"""Checks against identities, numerical integration, and independent arithmetic."""
import unittest
import numpy as np
from dose_response import density, generate, hidden_confounding, pseudo_outcome, smooth, truth
from decision_objectives import outcomes
from store_pooling import basis, design, fit, generate as generate_stores


class DoseResponseChecks(unittest.TestCase):
    def test_density_change_of_variables(self):
        a = np.linspace(.0001, 39.9999, 100000)
        for mean in [-.9, .9]:
            self.assertAlmostEqual(np.trapezoid(density(a, mean, .9), a), 1, places=7)

    def test_population_double_robustness(self):
        # Enumerate the two covariate types at each dose using Bayes' rule.
        for a in [8., 20., 32.]:
            conditional = density(a, np.array([-.9, .9]), .9)
            observed_share = conditional / conditional.sum()
            mu_true = truth(a) + np.array([-2., 2.])
            for outcome_correct, density_correct in [(True, True), (True, False), (False, True)]:
                mu = mu_true if outcome_correct else np.full(2, 8 + .1*a)
                weights = conditional.mean()/conditional if density_correct else np.ones(2)
                expected = observed_share @ (mu.mean() + weights*(mu_true-mu))
                self.assertAlmostEqual(expected, truth(a), places=11)

    def test_local_linear_reproduces_affine_function(self):
        a = np.linspace(2, 38, 151)
        grid = np.array([3., 19., 36.])
        estimate, se = smooth(a, 5 + 2*a, grid)
        np.testing.assert_allclose(estimate, 5 + 2*grid, atol=1e-10)
        self.assertLess(se.max(), 1e-11)

    def test_own_outcome_excluded_from_nuisance_training(self):
        x, a, y = generate(n=400)
        xi, w = pseudo_outcome(x, a, y)
        changed = y.copy(); changed[0] += 10
        new_xi, new_w = pseudo_outcome(x, a, changed)
        self.assertAlmostEqual(new_xi[0]-xi[0], 10*w[0], places=9)
        np.testing.assert_allclose(w, new_w)

    def test_hidden_confounder_formula_by_bayes_rule(self):
        for a in [8., 20., 32.]:
            conditional_means = []
            for x in [-1., 1.]:
                probability = density(a, .9*x + .8*np.array([-1., 1.]), .9)
                mean_u = probability @ np.array([-1., 1.]) / probability.sum()
                conditional_means.append(truth(a) + 2*x + 2*mean_u)
            self.assertAlmostEqual(hidden_confounding(np.array([a]))[0], np.mean(conditional_means), places=11)

    def test_profit_identity_and_constrained_choice(self):
        a = np.linspace(0, 40, 401)
        profit, revenue, units, complaint = outcomes(a)
        np.testing.assert_allclose(revenue-4*units, profit)
        self.assertEqual(a[np.argmax(profit)], 20)
        selected = np.argmax(np.where(complaint <= .03, profit, -np.inf))
        self.assertAlmostEqual(a[selected], 14.1)
        self.assertLessEqual(complaint[selected], .03)
        self.assertGreater(complaint[selected+1], .03)

    def test_large_pooling_penalty_approaches_common_curve(self):
        a, s, y, _, _ = generate_stores()
        common = np.linalg.lstsq(basis(a), y, rcond=None)[0]
        pooled = fit(a, s, y, 1e10, 1e10)
        np.testing.assert_allclose(design(a, s) @ pooled, basis(a) @ common, atol=1e-6)


if __name__ == "__main__":
    unittest.main()
