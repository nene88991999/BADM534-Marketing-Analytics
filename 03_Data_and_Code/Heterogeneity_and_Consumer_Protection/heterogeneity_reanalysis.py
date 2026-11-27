"""Reanalyze released retail data; separate fitted responses from conduct.

Two-stage empirical Bayes with exact normal-mixture integration. This is a
teaching adaptation, not a replication of the paper's constrained sampler.
"""
from pathlib import Path
import json
import numpy as np
import pandas as pd
from scipy.optimize import minimize
from scipy.special import logsumexp
from scipy.stats import norm

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "results"


def account_estimates(frame):
    """OLS price associations, conditioning on available display variation."""
    rows = []
    for account, group in frame.groupby("RETAILER", sort=True):
        y = np.log(group.VOLUME.to_numpy(float))
        price = np.log(group.PRICE.to_numpy(float))
        display = group.DISP.to_numpy(float)
        # Constant display is collinear with the account intercept.
        varying = np.ptp(display) > 1e-12
        columns = [np.ones(len(y)), price]
        if varying:
            columns.append(display)
        x = np.column_stack(columns)
        assert np.linalg.matrix_rank(x) == x.shape[1]
        coef = np.linalg.lstsq(x, y, rcond=None)[0]
        residual = y - x @ coef
        variance = (residual @ residual) / (len(y) - x.shape[1])
        se = np.sqrt(variance * np.linalg.inv(x.T @ x)[1, 1])
        assert np.isfinite(se) and se > 0
        rows.append(dict(account=account, observations=len(y),
                         display_varies=bool(varying), price_slope=coef[1],
                         model_se=se, residual_variance=variance))
    return pd.DataFrame(rows)


def unpack(parameters, components):
    if components == 1:
        return np.ones(1), parameters[:1], np.exp(parameters[1:2])
    weight = parameters[0]
    return (np.array([weight, 1-weight]), parameters[1:3],
            np.exp(parameters[3:5]))


def marginal_log_density(b, se, weights, means, scales):
    total_sd = np.sqrt(se[:, None]**2 + scales[None, :]**2)
    terms = np.log(weights) + norm.logpdf(b[:, None], means, total_sd)
    return logsumexp(terms, axis=1)


def fit_mixture(b, se, components):
    """Integrate account coefficients before maximizing the marginal likelihood."""
    center, spread = float(np.mean(b)), max(float(np.std(b)), 0.2)
    if components == 1:
        starts = [np.array([center, np.log(spread)]), np.array([center, -2.0])]
        bounds = [(-30, 10), (-7, 4)]
    else:
        starts = [np.array([w, center-d*spread, center+d*spread,
                            np.log(spread/2), np.log(spread/2)])
                  for w in (0.25, 0.5, 0.75) for d in (0.4, 1.0, 1.8)]
        bounds = [(0.02, 0.98), (-30, 10), (-30, 10), (-7, 4), (-7, 4)]

    def objective(parameters):
        return -marginal_log_density(b, se, *unpack(parameters, components)).sum()

    fits = [minimize(objective, start, method="L-BFGS-B", bounds=bounds,
                     options={"maxiter": 3000, "ftol": 1e-12, "gtol": 1e-6})
            for start in starts]
    converged = [fit for fit in fits if fit.success and np.isfinite(fit.fun)]
    assert converged, "No converged marginal-likelihood fit"
    best = min(converged, key=lambda fit: fit.fun)
    weights, means, scales = unpack(best.x, components)
    order = np.argsort(means)
    return dict(weights=weights[order], means=means[order], scales=scales[order],
                log_likelihood=float(-best.fun), starts=len(starts),
                converged_starts=len(converged))


def posterior(b, se, fit):
    """Conditional on fitted hyperparameters and fixed first-stage standard errors."""
    weights, means, scales = (fit[k] for k in ("weights", "means", "scales"))
    prior_var, sampling_var = scales[None, :]**2, se[:, None]**2
    variance = 1 / (1 / prior_var + 1 / sampling_var)
    location = variance * (means / prior_var + b[:, None] / sampling_var)
    log_weights = (np.log(weights)
                   + norm.logpdf(b[:, None], means, np.sqrt(prior_var+sampling_var)))
    probabilities = np.exp(log_weights-logsumexp(log_weights, axis=1)[:, None])
    average = np.sum(probabilities*location, axis=1)
    positive = np.sum(probabilities*norm.sf(0, location, np.sqrt(variance)), axis=1)
    return average, positive


def main():
    OUT.mkdir(exist_ok=True)
    frame = pd.read_csv(ROOT / "data/cheese.csv")
    assert list(frame.columns) == ["RETAILER", "VOLUME", "DISP", "PRICE"]
    assert len(frame) == 5555 and frame.RETAILER.nunique() == 88
    assert frame.notna().all().all()
    assert (frame.VOLUME > 0).all() and (frame.PRICE > 0).all()
    assert frame.DISP.between(0, 1).all()
    estimates = account_estimates(frame)
    b, se = estimates.price_slope.to_numpy(), estimates.model_se.to_numpy()
    summaries, parameters, equivalence, profiles = [], [], [], []
    grid = np.linspace(-12, 5, 341)
    for components in (1, 2):
        fit = fit_mixture(b, se, components)
        mean, prob_positive = posterior(b, se, fit)
        estimates[f"posterior_mean_k{components}"] = mean
        estimates[f"posterior_positive_k{components}"] = prob_positive
        k_parameters = 2 if components == 1 else 5
        summaries.append(dict(components=components, accounts=len(b),
                              log_likelihood=fit["log_likelihood"],
                              bic=k_parameters*np.log(len(b))-2*fit["log_likelihood"],
                              mean_account_slope=float(mean.mean()),
                              positive_posterior_means=int((mean > 0).sum()),
                              starts=fit["starts"], converged_starts=fit["converged_starts"]))
        for k, (w, mu, sd) in enumerate(zip(fit["weights"], fit["means"], fit["scales"]), 1):
            parameters.append(dict(components=components, component=k,
                                   weight=w, mean=mu, sd=sd))
        base = marginal_log_density(b, se, fit["weights"], fit["means"], fit["scales"])
        # Constructed decomposition: observed response theta = beta + gamma.
        # Shift the taste distribution by -gamma and add gamma in the likelihood.
        # gamma is an imposed mechanism, not a measured feature of these accounts.
        for gamma in (0.0, 0.25, 0.5, 1.0):
            beta_means = fit["means"] - gamma
            observed = marginal_log_density(b, se, fit["weights"],
                                            beta_means + gamma, fit["scales"])
            maximum_gap = float(np.max(np.abs(base-observed)))
            assert maximum_gap < 1e-10
            equivalence.append(dict(components=components, imposed_gamma=gamma,
                                    log_likelihood=float(observed.sum()),
                                    maximum_log_density_gap=maximum_gap,
                                    mean_observed_response=float(mean.mean()),
                                    mean_latent_taste=float(mean.mean()-gamma)))
        for x in grid:
            density = np.sum(fit["weights"]*norm.pdf(x, fit["means"], fit["scales"]))
            profiles.append(dict(components=components, slope=x, density=density))
    estimates.to_csv(OUT / "account_estimates.csv", index=False)
    pd.DataFrame(summaries).to_csv(OUT / "model_comparison.csv", index=False)
    pd.DataFrame(parameters).to_csv(OUT / "mixture_parameters.csv", index=False)
    pd.DataFrame(equivalence).to_csv(OUT / "observational_equivalence.csv", index=False)
    pd.DataFrame(profiles).to_csv(OUT / "density_grid.csv", index=False)
    # Exact implication under observational equivalence, not estimated power.
    pd.DataFrame([dict(false_flag_rate=a, constructed_harm_miss_rate=1-a)
                  for a in (0.01, 0.05, 0.10)]).to_csv(
                      OUT / "equivalent_state_errors.csv", index=False)
    record = dict(observations=len(frame), accounts=len(estimates),
                  observations_min=int(estimates.observations.min()),
                  observations_max=int(estimates.observations.max()),
                  constant_display_accounts=int((~estimates.display_varies).sum()),
                  positive_ols_slopes=int((b > 0).sum()),
                  sample_restrictions="All released rows retained; no date or household outcomes supplied.",
                  uncertainty="First-stage iid Gaussian working errors; fixed estimated SEs and empirical-Bayes hyperparameters. Temporal dependence and hyperparameter uncertainty are unmodeled.",
                  interpretation="Conditional price-sales associations; no identified causal elasticities, markups, wrongdoing, or consumer welfare effects.")
    (OUT / "summary.json").write_text(json.dumps(record, indent=2)+"\n")
    print(pd.DataFrame(summaries).to_string(index=False))
    print(json.dumps(record, indent=2))


if __name__ == "__main__":
    main()
