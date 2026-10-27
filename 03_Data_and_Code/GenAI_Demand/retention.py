"""Measure synthetic subscription stocks, cohorts, and acquisition events."""
from pathlib import Path
import json

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parents[1] / "01_Resources/08_M8_Current_Topics_in_Marketing/genai_demand_lab/data"
OUTPUT = HERE / "results"


def acquisition_type(previous, current, ever_paid):
    """Classify a newly held provider using adjacent monthly subscription sets."""
    if not previous:
        return "category_return" if ever_paid else "first_paid_entry"
    if previous.isdisjoint(current):
        return "complete_provider_switch"
    return "provider_addition"


def cohort_outcomes(subs, provider, start, horizon, observed_months):
    """Endpoint and continuous retention for one fixed provider cohort."""
    required = {str(pd.Period(start, freq="M") + k) for k in range(horizon + 1)}
    if not required.issubset(set(observed_months)):
        raise ValueError("Cohort horizon extends beyond the observed calendar")
    cohort = set(subs.loc[subs.month.eq(start) & subs.provider.eq(provider), "consumer_id"])
    if not cohort:
        raise ValueError("Empty starting cohort")
    continuous = cohort.copy()
    rows = []
    for k in range(horizon + 1):
        month = str(pd.Period(start, freq="M") + k)
        active = subs.loc[subs.month.eq(month)]
        own = set(active.loc[active.provider.eq(provider), "consumer_id"])
        any_provider = set(active.consumer_id)
        continuous &= own
        row = {"provider": provider, "start_month": start, "month": month,
               "horizon_months": k, "cohort_size": len(cohort),
               "same_provider": len(cohort & own),
               "other_provider_only": len((cohort & any_provider) - own),
               "no_paid_provider": len(cohort - any_provider),
               "continuous_same_provider": len(continuous)}
        assert row["same_provider"] + row["other_provider_only"] + row["no_paid_provider"] == len(cohort)
        rows.append(row)
    return pd.DataFrame(rows)


def main():
    consumers = pd.read_csv(SOURCE / "synthetic_consumers.csv")
    subs = pd.read_csv(SOURCE / "synthetic_subscriptions.csv.gz")
    dgp = json.loads((SOURCE / "synthetic_dgp.json").read_text())
    months = sorted(dgp["g_trend"])
    n = len(consumers)
    assert n == dgp["n_consumers"] and consumers.consumer_id.is_unique
    assert not subs.duplicated(["consumer_id", "month", "provider"]).any()
    assert subs.consumer_id.isin(consumers.consumer_id).all()
    assert subs.month.isin(months).all() and subs.price.gt(0).all()
    assert subs["new"].isin([True, False]).all()
    assert subs.tier.isin(["basic", "premium"]).all()
    states = {m: {int(i): set(g.provider) for i, g in s.groupby("consumer_id")}
              for m, s in subs.groupby("month")}
    events, monthly, history = [], [], set()
    previous = {}
    for month in months:
        current = states.get(month, {})
        for consumer, providers in current.items():
            old = previous.get(consumer, set())
            for provider in sorted(providers - old):
                events.append({"month": month, "consumer_id": consumer, "provider": provider,
                               "event": acquisition_type(old, providers, consumer in history)})
        group = subs.loc[subs.month.eq(month)]
        monthly.append({"month": month, "population": n, "payers": len(current),
                        "subscriptions": len(group), "adoption": len(current) / n,
                        "multihomers": sum(len(s) > 1 for s in current.values()),
                        "basic_subscriptions": int(group.tier.eq("basic").sum())})
        history.update(current)
        previous = current
    events = pd.DataFrame(events)
    keys = ["month", "consumer_id", "provider"]
    recorded = set(subs.loc[subs["new"], keys].itertuples(index=False, name=None))
    calculated = set(events[keys].itertuples(index=False, name=None))
    assert recorded == calculated
    monthly = pd.DataFrame(monthly)
    monthly["multihoming_given_payment"] = monthly.multihomers / monthly.payers.replace(0, np.nan)
    monthly["basic_subscription_share"] = monthly.basic_subscriptions / monthly.subscriptions.replace(0, np.nan)
    cohort_start, horizon = "2025-01", 12
    assert str(pd.Period(cohort_start, freq="M") + horizon) <= months[-1]
    providers = sorted(subs.loc[subs.month.eq(cohort_start), "provider"].unique())
    cohorts = pd.concat([cohort_outcomes(subs, p, cohort_start, horizon, months)
                         for p in providers], ignore_index=True)
    last_events = events.loc[events.month.eq(months[-1])]
    counts = last_events.event.value_counts().sort_index()
    last = monthly.iloc[-1]
    result = {"data_type": "synthetic", "population": n, "subscription_rows": len(subs),
              "calendar_months": len(months), "last_month": months[-1],
              "last_payers": int(last.payers), "last_subscriptions": int(last.subscriptions),
              "last_adoption": float(last.adoption),
              "last_multihomers": int(last.multihomers),
              "last_multihoming_given_payment": float(last.multihoming_given_payment),
              "last_acquisition_events": int(len(last_events)),
              "last_acquisition_consumers": int(last_events.consumer_id.nunique()),
              "last_acquisition_types": {k: int(v) for k, v in counts.items()},
              "new_flag_verified": True}
    OUTPUT.mkdir(exist_ok=True)
    monthly.to_csv(OUTPUT / "adoption.csv", index=False, float_format="%.8f")
    cohorts.to_csv(OUTPUT / "cohorts.csv", index=False)
    counts.rename_axis("event").rename("events").to_csv(OUTPUT / "acquisition_types.csv")
    (OUTPUT / "retention.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
