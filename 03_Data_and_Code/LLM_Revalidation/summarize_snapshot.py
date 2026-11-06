"""Summarize published LLM claim results; no model calls or trend refitting."""
from pathlib import Path
from datetime import date
from collections import Counter
import csv
import json
import statistics

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parents[1] / "01_Resources/14_LLM_Evidence_and_Revalidation/source_tables"
END = date(2026, 9, 30)
MONTH = 365.25 / 12


def survival(times, events, horizon):
    """Kaplan-Meier survival, with events before censoring at tied times."""
    if len(times) != len(events) or not times:
        raise ValueError("Equal nonempty time and event lists are required")
    if any(t < 0 for t in times) or any(e not in (0, 1) for e in events):
        raise ValueError("Invalid follow-up time or event indicator")
    result = 1.0
    for time in sorted(set(t for t in times if t <= horizon)):
        at_risk = sum(t >= time for t in times)
        events_now = sum(e for t, e in zip(times, events) if t == time)
        result *= 1 - events_now / at_risk
    return result


def write_csv(path, rows):
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main():
    claims = list(csv.DictReader((SOURCE / "claims.csv").open()))
    panel = list(csv.DictReader((SOURCE / "panel_values.csv").open()))
    fitted = json.loads((SOURCE / "post_results.json").read_text())["claims"]
    assert len({c["blog_id"] for c in claims}) == len(claims) == 50
    assert len({(r["blog_id"], r["model"]) for r in panel}) == len(panel) == 1000
    assert len({r["model"] for r in panel}) == 20
    assert {r["reliable"] for r in panel} <= {"True", "False"}
    assert all(sum(r["blog_id"] == c["blog_id"] for r in panel) == 20 for c in claims)
    aliases = {"dead": "expired", "attenuated": "weakened"}
    labels = {c["blog_id"]: aliases.get(c["verdict"], c["verdict"]) for c in claims}
    assert set(labels) == {c["id"] for c in fitted}
    assert all(labels[c["id"]] == aliases.get(c["category"], c["category"]) for c in fitted)
    counts = Counter(labels.values())
    lifetimes = []
    for claim in sorted(fitted, key=lambda c: int(c["id"][1:])):
        start = date.fromisoformat(claim["paper_date"])
        event = int(labels[claim["id"]] == "expired")
        stop = date.fromisoformat(claim["death"]) if event else END
        assert start <= stop <= END
        lifetimes.append(dict(claim_id=claim["id"], paper_date=str(start),
            endpoint=str(stop), months=(stop - start).days / MONTH, event=event,
            endpoint_kind=claim["death_kind"] if event else "right_censored"))
    times = [r["months"] for r in lifetimes]
    events = [r["event"] for r in lifetimes]
    expired = [t for t, e in zip(times, events) if e]
    horizons = [dict(months=h, estimated_expired_share=1-survival(times, events, h))
                for h in (6, 12, 24)]
    curve = [dict(months=h, estimated_expired_share=1-survival(times, events, h))
             for h in sorted({0.0, 24.0} | {t for t in times if t <= 24})]
    verdict_rows = [dict(verdict=k, claims=counts[k], share=counts[k]/len(claims))
                    for k in ("expired", "weakened", "persists", "strengthened")]
    model_rows = []
    for model in sorted({r["model"] for r in panel}):
        selected = [r for r in panel if r["model"] == model]
        reliable = [r for r in selected if r["reliable"] == "True"]
        model_rows.append(dict(model=model, name=selected[0]["model_name"],
            reliable_pairs=len(reliable), unscorable_pairs=len(selected)-len(reliable),
            effects_at_or_below_point_two=sum(float(r["e"]) <= .2 for r in reliable)))
    citation_rows = [dict(model=r["model_name"], release=r["release"],
        fabricated_fraction=float(r["value"]), relative_effect=float(r["e"]),
        reliable=r["reliable"]) for r in panel if r["blog_id"] == "C11"]
    summary = dict(claims=len(claims), models=len(model_rows), pairs=len(panel),
        unreliable_pairs=sum(r["reliable"] == "False" for r in panel), verdicts=counts,
        expired_only_mean_months=statistics.mean(expired),
        expired_only_median_months=statistics.median(expired), horizons=horizons,
        observation_end=str(END),
        scope="Published fitted dates treated as fixed; no model runs, refits, or date-uncertainty propagation")
    output = HERE / "results"
    output.mkdir(exist_ok=True)
    for name, rows in [("verdicts", verdict_rows), ("lifetimes", lifetimes),
                       ("horizons", horizons), ("followup_curve", curve), ("model_counts", model_rows),
                       ("citation_fabrication", citation_rows)]:
        write_csv(output / (name + ".csv"), rows)
    (output / "snapshot_summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
