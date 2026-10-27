#!/usr/bin/env python3
"""Synthetic consumer panel of paid generative-AI subscriptions, calibrated to the headline moments in
Egan, Russel, Shi and Yao (2026), "Competition in Generative AI: Evidence from Consumer Demand", NBER w35953.

THIS IS SIMULATED DATA. The paper's data are card transactions for 174 million consumers and are not public.
The simulation exists so that students can compute the same objects the paper reports (adoption by age and
income, plan tiers, multihoming, cohort retention, switching around model releases) and estimate a simple
demand model, on a panel whose data-generating process they can read. Nothing here is an estimate of the
real market. The moments targeted, as stated in the paper's abstract:

    * about 2.9% of US consumers paying for at least one major service by April 2026
    * adoption higher among younger and higher-income consumers
    * nearly all paying users on basic plans costing $30 or less a month
    * multihoming common but declining as providers' capabilities grew
    * annual retention between 20% and 45%
    * switching rising around major model releases
    * consumers highly price-sensitive, loyal to "AI" far more than to any one provider

Usage
-----
    python simulate_subscription_panel.py --n 60000 --seed 534 --out data

Outputs (in --out): synthetic_subscriptions.csv.gz (one row per consumer-month-product held),
synthetic_consumers.csv, synthetic_products.csv, synthetic_releases.csv, synthetic_dgp.json (true parameters).

Data-generating process (monthly, Jan 2023 to Apr 2026)
-------------------------------------------------------
Consumer i has an "AI affinity" a_i that depends on age group and income tercile plus noise. Each month,
for each provider j, the value of holding a subscription is

    v_ijt = a_i + g_t + q_jt - alpha * p_jt + gamma * held_ij,t-1 + e_ijt,     e ~ logistic

where g_t is a common usefulness trend (chosen so that aggregate adoption follows the target path), q_jt is
provider quality, which jumps at that provider's model releases and then partly fades, p_jt is the plan price
(with occasional promotional discounts, which is what identifies alpha), and gamma is inertia. A consumer takes
the provider with the highest positive value, then a second one only if its value still clears a satiation
cost kappa_t that rises over time (growing substitutability), and so on. Premium tiers are chosen by a small,
high-affinity, high-income minority. Everything is vectorised with numpy; 60,000 consumers run in a few seconds.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

MONTHS = pd.period_range("2023-01", "2026-04", freq="M")

# Products: (provider, plan, tier, list price, first month available). Launch months are approximate and are
# inputs to a simulation, not facts about the market; the Wayback exercise in the notebook checks them.
PRODUCTS = [
    ("OpenAI", "ChatGPT Plus", "basic", 20.00, "2023-02"),
    ("OpenAI", "ChatGPT Pro", "premium", 200.00, "2024-12"),
    ("Anthropic", "Claude Pro", "basic", 20.00, "2023-09"),
    ("Anthropic", "Claude Max", "premium", 100.00, "2025-04"),
    ("Google", "Gemini Advanced / AI Pro", "basic", 19.99, "2024-02"),
    ("Google", "Google AI Ultra", "premium", 249.99, "2025-05"),
    ("Microsoft", "Copilot Pro", "basic", 20.00, "2024-01"),
    ("Perplexity", "Perplexity Pro", "basic", 20.00, "2023-03"),
    ("Perplexity", "Perplexity Max", "premium", 200.00, "2025-07"),
    ("xAI", "SuperGrok", "basic", 30.00, "2025-02"),
    ("xAI", "SuperGrok Heavy", "premium", 300.00, "2025-07"),
]
# Major model releases used as quality shocks (provider, month, size). Illustrative; replace with the Epoch AI
# extract from collect_genai_signals.py --epoch for a sourced list.
RELEASES = [
    ("OpenAI", "2023-03", 1.0), ("OpenAI", "2024-05", 0.7), ("OpenAI", "2024-09", 0.5), ("OpenAI", "2024-12", 0.4),
    ("OpenAI", "2025-02", 0.3), ("OpenAI", "2025-04", 0.4), ("OpenAI", "2025-08", 0.8), ("OpenAI", "2025-11", 0.4),
    ("OpenAI", "2026-02", 0.5),
    ("Anthropic", "2024-03", 0.6), ("Anthropic", "2024-06", 0.7), ("Anthropic", "2024-10", 0.4), ("Anthropic", "2025-02", 0.5),
    ("Anthropic", "2025-05", 0.7), ("Anthropic", "2025-08", 0.3), ("Anthropic", "2025-09", 0.5), ("Anthropic", "2025-11", 0.5),
    ("Anthropic", "2026-02", 0.5),
    ("Google", "2024-02", 0.6), ("Google", "2024-05", 0.3), ("Google", "2024-12", 0.6), ("Google", "2025-03", 0.7),
    ("Google", "2025-06", 0.3), ("Google", "2025-11", 0.8), ("Google", "2026-02", 0.4),
    ("Microsoft", "2024-01", 0.5), ("Microsoft", "2025-04", 0.3),
    ("Perplexity", "2024-04", 0.3), ("Perplexity", "2025-02", 0.4), ("Perplexity", "2025-07", 0.3),
    ("xAI", "2025-02", 0.9), ("xAI", "2025-07", 0.7), ("xAI", "2025-11", 0.4), ("xAI", "2026-02", 0.4),
]
AGE_GROUPS = {"18-29": 0.21, "30-44": 0.26, "45-64": 0.32, "65+": 0.21}
AGE_EFFECT = {"18-29": 0.9, "30-44": 0.5, "45-64": -0.2, "65+": -1.0}
INCOME_EFFECT = {"low": -0.6, "middle": 0.0, "high": 0.7}


def target_adoption(months: pd.PeriodIndex, end_share: float = 0.029, start_share: float = 0.002) -> np.ndarray:
    """Logistic path from start_share (Feb 2023) to end_share (Apr 2026)."""
    t = np.arange(len(months))
    mid, k = len(months) * 0.62, 0.16
    path = start_share + (end_share - start_share) / (1 + np.exp(-k * (t - mid))) * (1 + np.exp(-k * (len(months) - 1 - mid)))
    path[months < pd.Period("2023-02", "M")] = 0.0
    return path


def simulate(n: int = 60_000, seed: int = 534, alpha: float = 0.06, gamma: float = 5.5, out: Path = Path("data")) -> dict:
    rng = np.random.default_rng(seed)
    providers = sorted({p for p, *_ in PRODUCTS})
    P = len(providers)
    pidx = {p: k for k, p in enumerate(providers)}
    T = len(MONTHS)

    # consumers
    age = rng.choice(list(AGE_GROUPS), size=n, p=list(AGE_GROUPS.values()))
    income = rng.choice(["low", "middle", "high"], size=n, p=[1 / 3, 1 / 3, 1 / 3])
    affinity = 1.5 * (np.array([AGE_EFFECT[a] for a in age]) + np.array([INCOME_EFFECT[i] for i in income])) + rng.normal(0, 2.0, n)
    premium_taste = (rng.random(n) < 0.03) | ((rng.random(n) < 0.03) & (income == "high"))   # a few per cent of payers

    # products by provider: basic and (maybe) premium
    prod = pd.DataFrame(PRODUCTS, columns=["provider", "plan", "tier", "list_price", "available_from"])
    prod["available_from"] = pd.PeriodIndex(prod["available_from"], freq="M")
    basic = prod[prod.tier == "basic"].set_index("provider")
    premium = prod[prod.tier == "premium"].set_index("provider")

    # quality paths with release jumps that partly fade (half-life ~ 6 months)
    q = np.zeros((T, P))
    rel = pd.DataFrame(RELEASES, columns=["provider", "month", "size"])
    rel["month"] = pd.PeriodIndex(rel["month"], freq="M")
    for t, m in enumerate(MONTHS):
        for k, p in enumerate(providers):
            prior = rel[(rel.provider == p) & (rel.month <= m)]
            q[t, k] = sum(s * (0.5 + 0.5 * 0.89 ** ((m - mm).n)) for mm, s in zip(prior.month, prior["size"]))
    # promotional discounts: 3-month promotions at 25-50% off, starting in ~7% of months, so roughly a fifth of
    # product-months carry a discount. This within-product price variation is what identifies alpha.
    price = np.full((T, P), np.nan)
    promo = np.zeros((T, P), dtype=bool)
    for k, p in enumerate(providers):
        for t, m in enumerate(MONTHS):
            if m >= basic.loc[p, "available_from"]:
                price[t, k] = basic.loc[p, "list_price"]
        live = ~np.isnan(price[:, k])
        starts = np.flatnonzero(live & (rng.random(T) < 0.07))
        for s0 in starts:
            disc = rng.choice([0.5, 0.6, 0.75])
            for t in range(s0, min(s0 + 3, T)):
                if live[t] and not promo[t, k]:
                    promo[t, k] = True
                    price[t, k] = basic.loc[p, "list_price"] * disc

    kappa = np.linspace(-0.2, 2.2, T)          # satiation cost of a second subscription rises over time
    target = target_adoption(MONTHS)
    held = np.zeros((n, P), dtype=bool)
    g = np.zeros(T)
    rows, prev_counts = [], None
    for t, m in enumerate(MONTHS):
        live = ~np.isnan(price[t])
        if not live.any():
            continue
        eps = rng.logistic(size=(n, P))
        base = affinity[:, None] + q[t][None, :] - alpha * np.nan_to_num(price[t])[None, :] + gamma * held + eps
        base[:, ~live] = -np.inf

        def choose(gt):
            v = base + gt
            order = np.argsort(-v, axis=1)
            vs = np.take_along_axis(v, order, axis=1)
            penalty = kappa[t] * np.arange(P)[None, :]
            ok = vs - penalty > 0
            ok = np.logical_and.accumulate(ok, axis=1)        # stop at the first product that does not clear
            new_held = np.zeros_like(held)
            np.put_along_axis(new_held, order, ok, axis=1)
            return new_held

        # pick g_t so that the share holding at least one subscription matches the target path (bisection)
        lo, hi = -15.0, 10.0
        for _ in range(28):
            mid = (lo + hi) / 2
            share = choose(mid).any(axis=1).mean()
            lo, hi = (mid, hi) if share < target[t] else (lo, mid)
        g[t] = (lo + hi) / 2
        new_held = choose(g[t])

        for k, p in enumerate(providers):
            idx = np.flatnonzero(new_held[:, k])
            if idx.size == 0:
                continue
            prem_ok = (p in premium.index) and (m >= premium.loc[p, "available_from"])
            is_prem = premium_taste[idx] & prem_ok & (rng.random(idx.size) < 0.6)
            rows.append(pd.DataFrame({
                "consumer_id": idx, "month": str(m), "provider": p,
                "plan": np.where(is_prem, premium.loc[p, "plan"] if prem_ok else "", basic.loc[p, "plan"]),
                "tier": np.where(is_prem, "premium", "basic"),
                "price": np.where(is_prem, premium.loc[p, "list_price"] if prem_ok else np.nan, price[t, k]).round(2),
                "promo": np.where(is_prem, False, promo[t, k]),
                "new": ~held[idx, k],
            }))
        held = new_held

    subs = pd.concat(rows, ignore_index=True)
    out.mkdir(parents=True, exist_ok=True)
    subs.to_csv(out / "synthetic_subscriptions.csv.gz", index=False)
    pd.DataFrame({"consumer_id": np.arange(n), "age_group": age, "income_group": income}).to_csv(out / "synthetic_consumers.csv", index=False)
    prod.assign(available_from=prod.available_from.astype(str)).to_csv(out / "synthetic_products.csv", index=False)
    rel.assign(month=rel.month.astype(str)).to_csv(out / "synthetic_releases.csv", index=False)
    prices = pd.DataFrame(price, index=MONTHS.astype(str), columns=providers).reset_index().melt(id_vars="index", var_name="provider", value_name="basic_price").rename(columns={"index": "month"})
    prices["promo"] = pd.DataFrame(promo, index=MONTHS.astype(str), columns=providers).reset_index().melt(id_vars="index")["value"].values
    prices.dropna().to_csv(out / "synthetic_basic_prices.csv", index=False)
    dgp = {"n_consumers": n, "seed": seed, "alpha_price": alpha, "gamma_inertia": gamma,
           "kappa_satiation": {"start": float(kappa[0]), "end": float(kappa[-1])},
           "g_trend": dict(zip(MONTHS.astype(str), np.round(g, 3).tolist())),
           "age_effect": AGE_EFFECT, "income_effect": INCOME_EFFECT,
           "note": "Simulated data calibrated to abstract-level moments of NBER w35953; not estimates of the real market."}
    (out / "synthetic_dgp.json").write_text(json.dumps(dgp, indent=1))
    last = subs[subs.month == str(MONTHS[-1])]
    summary = {"rows": len(subs), "adoption_last_month": last.consumer_id.nunique() / n,
               "basic_share_last_month": (last.tier == "basic").mean(),
               "multihoming_last_month": (last.groupby("consumer_id").provider.nunique() > 1).mean()}
    return summary


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--n", type=int, default=60_000)
    ap.add_argument("--seed", type=int, default=534)
    ap.add_argument("--alpha", type=float, default=0.06)
    ap.add_argument("--out", default="data")
    a = ap.parse_args()
    print(json.dumps(simulate(a.n, a.seed, a.alpha, out=Path(a.out)), indent=1))
