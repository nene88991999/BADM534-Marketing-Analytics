"""Assess synthetic cancellation evidence at a fixed reporting cutoff."""
from collections import defaultdict
from datetime import datetime
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
EVENT_CLASS = {"request": "CancellationRequest",
               "confirmation": "CancellationConfirmation",
               "active_observation": "ActiveStatusObservation"}


def timestamp(value):
    parsed = datetime.fromisoformat(value)
    if parsed.tzinfo is None:
        raise ValueError("A timestamp must include a UTC offset")
    return parsed


def calculate(data):
    cutoff = timestamp(data["cutoff"])
    subscriptions = {s["subscription_id"]: s for s in data["subscriptions"]}
    if not subscriptions:
        raise ValueError("The reporting population must contain subscriptions")
    if len(subscriptions) != len(data["subscriptions"]):
        raise ValueError("Subscription identifiers must be unique")
    grouped = defaultdict(list)
    for event in data["events"]:
        grouped[event["event_id"]].append(event)
    flags, candidates = [], {}
    for event_id, copies in sorted(grouped.items()):
        if any(copy != copies[0] for copy in copies[1:]):
            flags.append({"event_id": event_id, "reason": "conflicting_duplicate",
                          "rows": len(copies)})
            continue
        event = copies[0]
        if len(copies) > 1:
            flags.append({"event_id": event_id, "reason": "exact_duplicate",
                          "rows": len(copies) - 1})
        reason = None
        if event["subscription_id"] not in subscriptions:
            reason = "unknown_subscription"
        elif event["kind"] not in EVENT_CLASS:
            reason = "unknown_event_kind"
        else:
            try:
                when = timestamp(event["at"])
                if when > cutoff:
                    reason = "after_cutoff"
            except (TypeError, ValueError):
                reason = "invalid_timestamp"
        if reason:
            flags.append({"event_id": event_id, "reason": reason, "rows": 1})
        else:
            candidates[event_id] = event
    requests = {k: v for k, v in candidates.items() if v["kind"] == "request"}
    valid = dict(candidates)
    for event_id, event in candidates.items():
        if event["kind"] != "confirmation":
            continue
        request = requests.get(event.get("request_id"))
        reason = None
        if request is None:
            reason = "missing_valid_request"
        elif request["subscription_id"] != event["subscription_id"]:
            reason = "subscription_mismatch"
        elif timestamp(event["at"]) < timestamp(request["at"]):
            reason = "confirmation_before_request"
        if reason:
            valid.pop(event_id)
            flags.append({"event_id": event_id, "reason": reason, "rows": 1})
    confirmations = [v for v in valid.values() if v["kind"] == "confirmation"]
    completed_requests = {v["request_id"] for v in confirmations}
    queue = sorted(set(requests) - completed_requests)
    evidence = []
    for subscription_id in sorted(subscriptions):
        events = [v for v in valid.values() if v["subscription_id"] == subscription_id]
        states = [v for v in events if v["kind"] in ("confirmation", "active_observation")]
        pending = [k for k in queue if requests[k]["subscription_id"] == subscription_id]
        if states:
            latest_time = max(timestamp(v["at"]) for v in states)
            latest = [v for v in states if timestamp(v["at"]) == latest_time]
            if len({v["kind"] for v in latest}) > 1:
                state = "conflicting_state_observations"
            else:
                state = ("recorded_cancellation" if latest[0]["kind"] == "confirmation"
                         else "observed_active")
            observed_at = latest_time.isoformat()
        else:
            state = "request_without_confirmation" if pending else "unknown"
            observed_at = None
        evidence.append({"subscription_id": subscription_id, "evidence_state": state,
                         "state_observed_at": observed_at, "requests_to_review": pending})
    correct_cancelled = sorted(r["subscription_id"] for r in evidence
                               if r["evidence_state"] == "recorded_cancellation")
    request_as_completion = sorted({v["subscription_id"] for v in requests.values()})
    traces = [{"event_id": k, "asserted_kind": v["kind"],
               "modeled_class": EVENT_CLASS[v["kind"]],
               "parent_class": "ServiceRecord",
               "subscription_id": v["subscription_id"], "at": v["at"]}
              for k, v in sorted(valid.items())]
    return {"synthetic": True, "cutoff": data["cutoff"],
            "raw_rows": len(data["events"]), "accepted_unique_events": len(valid),
            "subscription_denominator": len(subscriptions),
            "valid_request_denominator": len(requests),
            "request_ids_to_review": queue,
            "confirmed_subscription_ids": correct_cancelled,
            "request_as_completion_subscription_ids": request_as_completion,
            "confirmed_share": len(correct_cancelled) / len(subscriptions),
            "request_as_completion_share": len(request_as_completion) / len(subscriptions),
            "flags": flags, "evidence": evidence, "classification_trace": traces}


if __name__ == "__main__":
    data = json.loads((ROOT / "data/cancellation_records.json").read_text())
    result = calculate(data)
    output = ROOT / "results"
    output.mkdir(exist_ok=True)
    (output / "cancellations.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in ("accepted_unique_events",
          "request_ids_to_review", "confirmed_share", "request_as_completion_share")}, indent=2))
