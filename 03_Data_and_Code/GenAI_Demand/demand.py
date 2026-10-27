"""Contrast descriptive price regressions with an exact binary-logit benchmark."""
from pathlib import Path
import json

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parents[1] / "01_Resources/08_M8_Current_Topics_in_Marketing/genai_demand_lab/data"
OUTPUT = HERE / "results"


def design(frame):
    # All provider intercepts plus all but one month effect; no extra intercept.
    fixed = pd.concat([pd.get_dummies(frame.provider, dtype=float),
                       pd.get_dummies(frame.month, drop_first=True, dtype=float)], axis=1)
    x = np.column_stack([fixed.to_numpy(), frame.basic_price.to_numpy()])
    if np.linalg.matrix_rank(x) != x.shape[1]:
        raise ValueError("Price is not separately identified from the fixed effects")
    return x


def price_projection(frame, shares):
    shares = np.asarray(shares, dtype=float)
    if not np.isfinite(shares).all() or not ((shares > 0) & (shares < 1)).all():
        raise ValueError("Log-odds require shares strictly between zero and one")
    x = design(frame)
    y = np.log(shares) - np.log1p(-shares)
    beta = np.linalg.lstsq(x, y, rcond=None)[0]
    # Independent Frisch-Waugh-Lovell check of the price coefficient.
    controls, price = x[:, :-1], x[:, -1]
    price_residual = price - controls @ np.linalg.lstsq(controls, price, rcond=None)[0]
    y_residual = y - controls @ np.linalg.lstsq(controls, y, rcond=None)[0]
    fwl = float(price_residual @ y_residual / (price_residual @ price_residual))
    np.testing.assert_allclose(beta[-1], fwl, atol=1e-10)
    return {"price_coefficient": float(beta[-1]), "rows": len(frame),
            "residual_price_sum_squares": float(price_residual @ price_residual)}


def main():
    subs = pd.read_csv(SOURCE / "synthetic_subscriptions.csv.gz")
    consumers = pd.read_csv(SOURCE / "synthetic_consumers.csv")
    prices = pd.read_csv(SOURCE / "synthetic_basic_prices.csv")
    dgp = json.loads((SOURCE / "synthetic_dgp.json").read_text())
    keys = ["month", "provider"]
    assert consumers.consumer_id.is_unique and not prices.duplicated(keys).any()
    assert not subs.duplicated(["consumer_id"] + keys).any()
    basic = subs.loc[subs.tier.eq("basic")]
    stocks = basic.groupby(keys).size().rename("basic_holders")
    flows = basic.loc[basic["new"]].groupby(keys).size().rename("new_basic_holders")
    frame = prices.merge(stocks, on=keys, how="left", validate="one_to_one")
    frame = frame.merge(flows, on=keys, how="left", validate="one_to_one")
    frame[["basic_holders", "new_basic_holders"]] = frame[["basic_holders", "new_basic_holders"]].fillna(0)
    # Zero filling is justified by the complete simulated population and price support.
    frame["stock_share"] = frame.basic_holders / len(consumers)
    frame["flow_share"] = frame.new_basic_holders / len(consumers)
    common = frame.loc[frame.stock_share.between(0, 1, inclusive="neither") &
                       frame.flow_share.between(0, 1, inclusive="neither")].copy()
    results = []
    for name in ["stock_share", "flow_share"]:
        results.append({"outcome": name, **price_projection(common, common[name])})
    # Exact model-implied shares: homogeneous binary choice, no inertia or multihoming.
    # Provider/time intercepts vary, but the same price design and alpha are retained.
    x = design(common)
    intercepts = np.linspace(-4.0, -3.0, common.provider.nunique())
    time_effects = np.linspace(0.0, 0.2, common.month.nunique() - 1)
    controls = np.r_[intercepts, time_effects]
    alpha = dgp["alpha_price"]
    utility = x[:, :-1] @ controls - alpha * common.basic_price.to_numpy()
    benchmark_share = 1 / (1 + np.exp(-utility))
    benchmark = price_projection(common, benchmark_share)
    np.testing.assert_allclose(benchmark["price_coefficient"], -alpha, atol=1e-10)
    results.append({"outcome": "exact_binary_logit", **benchmark})
    result = {"data_type": "synthetic", "available_provider_months": len(frame),
              "common_positive_share_rows": len(common), "excluded_zero_share_rows": len(frame) - len(common),
              "imposed_utility_price_coefficient": -alpha, "projections": results,
              "interpretation": "Stock and flow slopes are descriptive projections of a heterogeneous dynamic simulation; only the exact binary benchmark recovers its imposed coefficient by construction"}
    OUTPUT.mkdir(exist_ok=True)
    frame.to_csv(OUTPUT / "provider_months.csv", index=False, float_format="%.10f")
    pd.DataFrame(results).to_csv(OUTPUT / "price_projections.csv", index=False, float_format="%.10f")
    (OUTPUT / "demand.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
