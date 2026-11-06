"""Solve an imposed pricing example and check published aggregate arithmetic.

Python 3.10+, standard library. No empirical microdata or model APIs.
Run: python3 03_Data_and_Code/AI_Experimentation_and_Pricing/evaluate_pricing.py
"""
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parent
# Population shares and dollar valuations for one purchase opportunity.
GROUPS = {"L": (F(3, 5), F(6), F(10)),
          "H": (F(2, 5), F(10), F(30))}


def demand(price, low, high):
    """Purchase probability under a uniform valuation distribution."""
    if not low < high or price < 0:
        raise ValueError("Require ordered valuation bounds and nonnegative price.")
    return max(F(0), min(F(1), (high - price) / (high - low)))


def surplus(price, low, high):
    """Expected dollar surplus per eligible customer, including nonbuyers."""
    demand(price, low, high)
    if price <= low:
        return (low + high) / 2 - price
    return max(high - price, F(0)) ** 2 / (2 * (high - low))


def best_uniform(groups):
    """Check support boundaries and stationary points of piecewise revenue."""
    bounds = sorted({F(0)} | {x for _, lo, hi in groups for x in (lo, hi)})
    candidates = set(bounds)
    for left, right in zip(bounds, bounds[1:]):
        midpoint = (left + right) / 2
        intercept, slope = F(0), F(0)
        for weight, low, high in groups:
            if midpoint < low:
                intercept += weight
            elif midpoint < high:
                intercept += weight * high / (high - low)
                slope += weight / (high - low)
        if slope:
            stationary = intercept / (2 * slope)
            if left <= stationary <= right:
                candidates.add(stationary)
    revenue = lambda p: sum(w * p * demand(p, lo, hi)
                            for w, lo, hi in groups)
    return max(sorted(candidates), key=revenue)


def evaluate(prices, reference):
    if set(prices) != set(GROUPS):
        raise ValueError("Every population group requires exactly one price.")
    profit = customer_surplus = quantity = better = worse = F(0)
    for name, (weight, low, high) in GROUPS.items():
        price = prices[name]
        q = demand(price, low, high)
        profit += weight * price * q  # Marginal cost is stipulated to be zero.
        customer_surplus += weight * surplus(price, low, high)
        quantity += weight * q
        if price < reference:
            better += weight * q
        elif price > reference:
            worse += weight * demand(reference, low, high)
    return {"profit_per_eligible_customer": profit,
            "surplus_per_eligible_customer": customer_surplus,
            "total_surplus_per_eligible_customer": profit + customer_surplus,
            "purchase_share": quantity, "strictly_better_share": better,
            "strictly_worse_share": worse}


def main():
    uniform = best_uniform(list(GROUPS.values()))
    segmented = {g: best_uniform([cell]) for g, cell in GROUPS.items()}
    policies = {"uniform": {g: uniform for g in GROUPS},
                "segmented": segmented,
                "discount_only": {g: min(p, uniform) for g, p in segmented.items()}}
    results = {name: {"prices": prices, **evaluate(prices, uniform)}
               for name, prices in policies.items()}
    published = json.loads((ROOT / "published_aggregates.json").read_text())
    clicks = published["causal_alignment"]["campaign_mean_click_rate_bp"]
    revenues = published["personalized_pricing"]["realized_revenue_per_prospect"]
    arithmetic = {
        "click_lift_from_rounded_means_bp": clicks["tuned"] - clicks["control"],
        "click_relative_lift_from_rounded_means": clicks["tuned"] / clicks["control"] - 1,
        "pricing_relative_revenue_lift_from_rounded_means":
            revenues["personalized"] / revenues["uniform"] - 1}
    output = {"data_type": "Exact calculations for an imposed economic example",
              "benchmark": "Revenue-maximizing uniform price in the same population",
              "cost": 0, "groups": GROUPS, "results": results,
              "published_aggregate_arithmetic": arithmetic,
              "scope": "No reconstruction of empirical uncertainty or ethical verdict"}
    (ROOT / "results.json").write_text(json.dumps(
        output, indent=2, default=lambda x: {"exact": str(x), "decimal": float(x)}) + "\n")
    for name, result in results.items():
        print(name, {k: float(v) for k, v in result.items() if k != "prices"})


if __name__ == "__main__":
    main()
