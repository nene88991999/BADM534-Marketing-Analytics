"""Constructed store demand, fixed predictions, and split-conformal intervals."""
from pathlib import Path
import csv
import json
from conformal import threshold

HERE = Path(__file__).resolve().parent
ALPHA = "0.10"


def make_rows(split, regular, volatile):
    """One distinct store per row; demand and predictions are imposed units."""
    rows = []
    for segment, errors in [("regular", regular), ("volatile", volatile)]:
        for i, magnitude in enumerate(errors):
            index = i % 20
            prediction = 100 + 5 * index
            error = magnitude if i % 2 == 0 else -magnitude
            rows.append(dict(store_id=f"{split}_{segment}_{i:03d}",
                split=split, segment=segment, volume_index=index,
                prediction=prediction, demand=prediction + error))
    return rows


def make_inputs():
    calibration = make_rows("calibration",
        [x for x in range(1, 9) for _ in range(10)], [10] * 10 + [20] * 9)
    evaluation = make_rows("evaluation", [4] * 40 + [8] * 40,
                           [8] * 10 + [18] * 8 + [25] * 2)
    return calibration, evaluation


def assess(rows):
    ids = [r["store_id"] for r in rows]
    if not rows or len(set(ids)) != len(ids):
        raise ValueError("Nonempty rows with unique store IDs are required")
    if any(r["segment"] not in ("regular", "volatile") for r in rows):
        raise ValueError("Segments must be defined before calibration")
    if any(r["demand"] < 0 for r in rows):
        raise ValueError("Demand must be nonnegative")


def evaluate(rows, cutoffs, method, scenario, shift=0):
    detail = []
    for row in rows:
        q = cutoffs[row["segment"]]
        y = row["demand"] + shift
        lower, upper = row["prediction"] - q, row["prediction"] + q
        detail.append(dict(**row, scenario=scenario, method=method,
            evaluated_demand=y, lower=lower, upper=upper,
            covered=int(lower <= y <= upper), width=upper - lower))
    summary = []
    for segment in ("all", "regular", "volatile"):
        subset = [r for r in detail if segment == "all" or r["segment"] == segment]
        n = len(subset)
        summary.append(dict(scenario=scenario, method=method, segment=segment,
            stores=n, covered=sum(r["covered"] for r in subset),
            coverage=sum(r["covered"] for r in subset) / n,
            mean_width=sum(r["width"] for r in subset) / n))
    return detail, summary


def write_csv(path, rows):
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main():
    calibration, evaluation = make_inputs()
    assess(calibration)
    assess(evaluation)
    assert not ({r["store_id"] for r in calibration} &
                {r["store_id"] for r in evaluation})
    residuals = [abs(r["demand"] - r["prediction"]) for r in calibration]
    q = threshold(residuals, ALPHA)
    group_q = {g: threshold([abs(r["demand"] - r["prediction"])
                            for r in calibration if r["segment"] == g], ALPHA)
               for g in ("regular", "volatile")}
    detail, summary = [], []
    for scenario, shift in [("reference", 0), ("shifted_plus_25", 25)]:
        for method, cutoffs in [("pooled", dict.fromkeys(group_q, q)),
                                ("by_segment", group_q)]:
            d, s = evaluate(evaluation, cutoffs, method, scenario, shift)
            detail.extend(d)
            summary.extend(s)
    output = HERE / "results"
    output.mkdir(exist_ok=True)
    write_csv(output / "calibration.csv", calibration)
    write_csv(output / "evaluation.csv", evaluation)
    write_csv(output / "intervals.csv", detail)
    write_csv(output / "coverage.csv", summary)
    results = dict(alpha=float(ALPHA), calibration_stores=len(calibration),
        evaluation_stores=len(evaluation), pooled_cutoff=q,
        segment_cutoffs=group_q, summary=summary,
        scope="Fixed synthetic cases and an imposed predictor; no model fit. "
              "The shifted scenario reuses the same stores with demand +25. "
              "Realized coverage is descriptive, not a test of exchangeability.")
    (output / "demand_summary.json").write_text(json.dumps(results, indent=2) + "\n")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
