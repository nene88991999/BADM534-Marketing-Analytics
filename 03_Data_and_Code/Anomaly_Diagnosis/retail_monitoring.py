"""Original synthetic retail monitoring example; Python standard library only."""
import csv
import json
import math
import random
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path
from statistics import mean, median

ROOT = Path(__file__).resolve().parent
FEATURES = ("visits", "completion_rate", "latency_ms", "support_contacts",
            "stock_available_share", "collection_completeness")
FLOORS = dict(zip(FEATURES, (2, .02, 25, 1, .01, .02)))
METHODS = ("mean", "maximum")


def write_csv(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def make_data():
    rng = random.Random(5342027)
    events = [
        dict(store="A", day=9, start=40, end=60, cause="payment_service"),
        dict(store="B", day=10, start=40, end=60, cause="campaign"),
        dict(store="C", day=11, start=40, end=60, cause="collection_failure"),
    ]
    rows = []
    for day in range(12):
        split = "train" if day < 6 else "validation" if day < 9 else "test"
        for index, store in enumerate("ABC"):
            for minute in range(120):
                phase = minute // 20
                visits = 100 + 15 * index + 10 * (phase % 2) + rng.randint(-4, 4)
                attempts = round(.4 * visits) + rng.randint(-2, 2)
                success = .90 + rng.uniform(-.015, .015)
                latency = 300 + 15 * (phase % 2) + rng.uniform(-25, 25)
                contacts = rng.randint(0, 2)
                stock = .95 + rng.uniform(-.02, .02)
                completeness = 1.0
                if store == "A" and day == 9 and 40 <= minute < 60:
                    success, latency = .35, latency + 500
                if store == "A" and day == 9 and 45 <= minute < 65:
                    contacts += 60
                if store == "B" and day == 10 and 40 <= minute < 60:
                    visits, attempts = visits + 100, attempts + 40
                payments = round(attempts * success)
                if store == "C" and day == 11 and 40 <= minute < 60:
                    visits, attempts, payments = [round(.4 * v) for v in
                                                  (visits, attempts, payments)]
                    completeness = .4
                if store == "A" and day == 10 and minute < 3:
                    latency = None  # Leading missing measurements remain in the roster.
                timestamp = datetime(2026, 1, 1, 9) + timedelta(days=day, minutes=minute)
                rows.append(dict(store=store, day=day, minute=minute,
                    timestamp=timestamp.isoformat(), split=split, phase=phase,
                    visits=visits, checkout_attempts=attempts, completed_payments=payments,
                    completion_rate=payments / attempts, latency_ms=latency,
                    support_contacts=contacts, stock_available_share=stock,
                    collection_completeness=completeness))
    return rows, events


def fit_reference(training):
    groups = defaultdict(list)
    for row in training:
        groups[row["store"], row["phase"]].append(row)
    reference = {}
    for key, rows in groups.items():
        reference[key] = {}
        for feature in FEATURES:
            values = [r[feature] for r in rows if r[feature] is not None]
            center = median(values)
            scale = max(1.4826 * median(abs(x - center) for x in values), FLOORS[feature])
            reference[key][feature] = (center, scale)
    return reference


def score_rows(rows, reference):
    scored = []
    for row in rows:
        z = {}
        for feature in FEATURES:
            center, scale = reference[row["store"], row["phase"]][feature]
            value = center if row[feature] is None else row[feature]
            z[feature] = abs(value - center) / scale
        scored.append(dict(row, mean=mean(z.values()), maximum=max(z.values()),
            missing_features=sum(row[f] is None for f in FEATURES), deviations=z))
    return scored


def calibrate(validation):
    rank = math.ceil(.99 * len(validation))
    return {method: sorted(r[method] for r in validation)[rank - 1] for method in METHODS}


def intervals(minutes):
    segments = []
    for minute in sorted(set(minutes)):
        if segments and segments[-1][1] == minute:
            segments[-1][1] = minute + 1
        else:
            segments.append([minute, minute + 1])
    return segments


def interval_iou(a, b):
    overlap = max(0, min(a[1], b[1]) - max(a[0], b[0]))
    return overlap / ((a[1] - a[0]) + (b[1] - b[0]) - overlap)


def evaluate(test, events, thresholds):
    by_run = defaultdict(list)
    for row in test:
        by_run[row["store"], row["day"]].append(row)
    event_map = {(e["store"], e["day"]): e for e in events}
    summaries, incidents, rankings, packets = [], [], [], []
    for method in METHODS:
        tp = fp = fn = tn = 0
        nominal_alerts = nominal_minutes = nominal_runs = alerted_nominal_runs = 0
        for key, rows in by_run.items():
            event = event_map.get(key)
            flagged = [r["minute"] for r in rows if r[method] > thresholds[method]]
            predicted = intervals(flagged)
            if event is None:
                nominal_alerts += len(flagged)
                nominal_minutes += len(rows)
                nominal_runs += 1
                alerted_nominal_runs += bool(flagged)
            for r in rows:
                truth = bool(event and event["start"] <= r["minute"] < event["end"])
                alert = r["minute"] in flagged
                tp += truth and alert
                fp += not truth and alert
                fn += truth and not alert
                tn += not truth and not alert
            if event is None:
                continue
            true_interval = [event["start"], event["end"]]
            hits = [m for m in flagged if event["start"] <= m < event["end"]]
            # Match the first overlapping alert interval only during evaluation.
            matched = next((p for p in predicted if interval_iou(p, true_interval) > 0), None)
            incidents.append(dict(method=method, store=key[0], day=key[1], cause=event["cause"],
                detected=bool(hits), delay_minutes=min(hits) - event["start"] if hits else None,
                predicted_start=matched[0] if matched else None,
                predicted_end=matched[1] if matched else None,
                interval_iou=interval_iou(matched, true_interval) if matched else 0))
            for condition, span in (("true_interval", true_interval), ("matched_alert", matched)):
                if span is None:
                    continue
                selected = [r for r in rows if span[0] <= r["minute"] < span[1]]
                values = {f: mean(r["deviations"][f] for r in selected) for f in FEATURES}
                order = sorted(FEATURES, key=lambda f: (-values[f], f))
                for rank, feature in enumerate(order, 1):
                    rankings.append(dict(method=method, store=key[0], day=key[1],
                        interval_condition=condition, start=span[0], end=span[1],
                        feature=feature, rank=rank, mean_deviation=values[feature]))
        summaries.append(dict(method=method, threshold=thresholds[method],
            evaluated_minutes=len(test), tp=tp, fp=fp, fn=fn, tn=tn,
            precision=tp / (tp + fp) if tp + fp else None,
            recall=tp / (tp + fn), nominal_run_minutes=nominal_minutes,
            nominal_alert_minutes=nominal_alerts,
            nominal_alert_minutes_per_1000=1000 * nominal_alerts / nominal_minutes,
            nominal_runs=nominal_runs, alerted_nominal_runs=alerted_nominal_runs))
    # All nine test runs enter the evidence packets, including the six normal runs.
    # This construction uses observations and scores, never event metadata.
    for (store, day), rows in by_run.items():
        spans = intervals(r["minute"] for r in rows if r["mean"] > thresholds["mean"])
        packets.append(dict(case_id=f"{store}_day{day:02d}", store=store, day=day,
            timestamps=[rows[0]["timestamp"], rows[-1]["timestamp"]],
            detector="mean", threshold=thresholds["mean"], alert_intervals=spans,
            measurements=[{k: r[k] for k in ("timestamp", "minute", *FEATURES)} for r in rows]))
    return summaries, incidents, rankings, packets


def main():
    rows, events = make_data()
    write_csv(ROOT / "data/observations.csv", rows)
    write_csv(ROOT / "data/events.csv", events)
    reference = fit_reference([r for r in rows if r["split"] == "train"])
    validation = score_rows([r for r in rows if r["split"] == "validation"], reference)
    test = score_rows([r for r in rows if r["split"] == "test"], reference)
    thresholds = calibrate(validation)
    summary, incidents, rankings, packets = evaluate(test, events, thresholds)
    fitted = [dict(store=s, phase=p, feature=f, center=c, scale=d)
              for (s, p), values in reference.items() for f, (c, d) in values.items()]
    write_csv(ROOT / "results/reference.csv", fitted)
    write_csv(ROOT / "results/detection_summary.csv", summary)
    write_csv(ROOT / "results/incident_metrics.csv", incidents)
    write_csv(ROOT / "results/variable_rankings.csv", rankings)
    write_csv(ROOT / "results/test_scores.csv", [{k: v for k, v in r.items() if k != "deviations"}
                                               for r in test])
    (ROOT / "results/evidence_packets.json").write_text(json.dumps(packets, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
