"""Hand-checkable temporal evaluation and imputation comparisons."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def interval_metrics(prediction, truth):
    start, end = prediction
    left, right = truth
    if end <= start or right <= left:
        raise ValueError("Intervals must have positive length and an exclusive end.")
    overlap = max(0, min(end, right) - max(start, left))
    return dict(any_overlap=int(overlap > 0),
        interval_iou=overlap / (end - start + right - left - overlap),
        onset_error_minutes=abs(start - left))


def causal_fill(values, training_median):
    output, last = [], training_median
    for value in values:
        if value is not None:
            last = value
        output.append(last)
    return output


def forward_then_backward(values):
    output, last = [], None
    for value in values:
        if value is not None:
            last = value
        output.append(last)
    following = None
    for i in range(len(output) - 1, -1, -1):
        if output[i] is not None:
            following = output[i]
        else:
            output[i] = following
    return output


def main():
    truth = (40, 60)
    predictions = {"precise": (40, 60), "delayed": (45, 65), "full_window": (0, 120)}
    rows = [dict(prediction=name, start=span[0], end=span[1],
                 **interval_metrics(span, truth)) for name, span in predictions.items()]
    output = ROOT / "results"
    output.mkdir(exist_ok=True)
    with (output / "timing_metrics.csv").open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    observed, revised_future = [None, None, 90, 92], [None, None, 900, 92]
    result = dict(training_median=100, observed=observed,
        retrospective=forward_then_backward(observed),
        causal=causal_fill(observed, 100),
        revised_future=revised_future,
        retrospective_revised=forward_then_backward(revised_future),
        causal_revised=causal_fill(revised_future, 100),
        retained_original_minutes=[i for i, x in enumerate(observed) if x is not None],
        positions_after_dropping_missing=[0, 1])
    (output / "missingness_comparison.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(dict(timing=rows, missingness=result), indent=2))


if __name__ == "__main__":
    main()
