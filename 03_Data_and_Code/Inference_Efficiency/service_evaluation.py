"""Construct and score separate teacher-forced and free-response observations."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
COMPUTE_DOLLARS_PER_SECOND = 0.002
TRIAGE_DOLLARS = 0.20


def write_csv(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]),
                                lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def make_cases():
    # An imposed policy: unused items qualify through day 30, inclusive.
    inputs = [(5, True), (15, True), (30, True), (31, True),
              (5, False), (45, True)] * 2
    return [dict(request_id=f"R{i + 1:02d}", days_since_purchase=day,
                 unused=unused, eligible=unused and day <= 30)
            for i, (day, unused) in enumerate(inputs)]


def make_observations(cases):
    teacher, responses = [], []
    for target in ("general", "specialized"):
        for i, case in enumerate(cases):
            truth = "eligible" if case["eligible"] else "ineligible"
            wrong = "ineligible" if case["eligible"] else "eligible"
            reference = f"The item is {truth} under the stated return policy .".split()
            # Each prediction conditions on the previous REFERENCE tokens.
            # These are synthetic top-token labels, not an autoregressive answer.
            teacher_errors = {0, 1, 2, 3} if target == "general" else {0}
            for position, token in enumerate(reference):
                prediction = wrong if position == 3 and i in teacher_errors else token
                teacher.append(dict(target=target, request_id=case["request_id"],
                    position=position, reference_token=token,
                    prediction_given_reference_prefix=prediction,
                    correct=prediction == token))
            # Free responses are SEPARATE imposed observations for different targets.
            failed = target == "specialized" and i in {10, 11}
            answer_errors = {0, 1, 2} if target == "general" else {0, 1}
            decision = None if failed else (wrong if i in answer_errors else truth)
            # A correct eligibility answer still needs the promised action.
            action_completed = not failed and i != 5
            answer_correct = not failed and decision == truth
            resolved = answer_correct and action_completed
            seconds = 2.0 if target == "general" or failed else 0.8
            responses.append(dict(target=target, request_id=case["request_id"],
                status="timeout" if failed else "completed",
                answer="" if failed else f"The item is {decision} under the stated return policy .",
                answer_correct=answer_correct, action_completed=action_completed,
                correctly_resolved=resolved, response_wait_seconds=seconds,
                compute_cost_dollars=COMPUTE_DOLLARS_PER_SECOND * seconds,
                triage_cost_dollars=0.0 if resolved else TRIAGE_DOLLARS))
    return teacher, responses


def summarize(teacher, responses):
    summary = []
    for target in ("general", "specialized"):
        tokens = [r for r in teacher if r["target"] == target]
        rows = [r for r in responses if r["target"] == target]
        completed = sum(r["status"] == "completed" for r in rows)
        correct = sum(r["answer_correct"] for r in rows)
        resolved = sum(r["correctly_resolved"] for r in rows)
        cost = sum(r["compute_cost_dollars"] + r["triage_cost_dollars"] for r in rows)
        summary.append(dict(target=target, reference_tokens=len(tokens),
            correct_reference_tokens=sum(r["correct"] for r in tokens),
            token_accuracy=sum(r["correct"] for r in tokens) / len(tokens),
            attempted=len(rows), completed=completed, failed=len(rows) - completed,
            correct_answers=correct, correctly_resolved=resolved,
            answer_accuracy_among_completed=correct / completed if completed else None,
            answer_accuracy_per_attempt=correct / len(rows),
            resolution_per_attempt=resolved / len(rows),
            mean_wait_seconds=sum(r["response_wait_seconds"] for r in rows) / len(rows),
            total_cost_dollars=cost,
            cost_per_correct_resolution=cost / resolved if resolved else None))
    return summary


def main():
    cases = make_cases()
    teacher, responses = make_observations(cases)
    summary = summarize(teacher, responses)
    write_csv(ROOT / "data/service_requests.csv", cases)
    write_csv(ROOT / "data/teacher_forced_predictions.csv", teacher)
    write_csv(ROOT / "data/free_responses.csv", responses)
    write_csv(ROOT / "results/service_summary.csv", summary)
    (ROOT / "results/service_summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
