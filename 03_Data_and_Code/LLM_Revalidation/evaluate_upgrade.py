"""Constructed paired cases and judge scores; no measured provider performance."""
from pathlib import Path
import csv
import json

HERE = Path(__file__).resolve().parent


def make_cases():
    # Segment, both pass, old-only pass, new-only pass, both fail, failure cost.
    cells = [("routine", 58, 2, 14, 6, 1), ("consequential", 14, 4, 0, 2, 20)]
    cases = []
    for segment, both, old_only, new_only, neither, loss in cells:
        for old, new, count in [(1, 1, both), (1, 0, old_only),
                                 (0, 1, new_only), (0, 0, neither)]:
            for _ in range(count):
                cases.append(dict(case_id=len(cases)+1, segment=segment,
                                  old_pass=old, new_pass=new, failure_cost=loss))
    return cases


def assess(cases):
    if not cases or len({r["case_id"] for r in cases}) != len(cases):
        raise ValueError("Cases must be nonempty and uniquely identified")
    if any(r[k] not in (0, 1) for r in cases for k in ("old_pass", "new_pass")):
        raise ValueError("Pass indicators must be binary")
    if any(r["failure_cost"] < 0 for r in cases):
        raise ValueError("Failure costs must be nonnegative")
    improved = sum(r["new_pass"] > r["old_pass"] for r in cases)
    regressed = sum(r["new_pass"] < r["old_pass"] for r in cases)
    return dict(cases=len(cases), old_pass=sum(r["old_pass"] for r in cases),
        new_pass=sum(r["new_pass"] for r in cases), improved=improved,
        regressed=regressed, net_gain_pp=100*(improved-regressed)/len(cases),
        old_loss=sum((1-r["old_pass"])*r["failure_cost"] for r in cases),
        new_loss=sum((1-r["new_pass"])*r["failure_cost"] for r in cases))


def zero_failure_upper(n, alpha=.05):
    """One-sided exact binomial upper bound after zero failures in n trials."""
    if n <= 0 or not 0 < alpha < 1:
        raise ValueError("Positive n and alpha between zero and one are required")
    return 1 - alpha ** (1/n)


def main():
    cases = make_cases()
    summary = assess(cases)
    summary["segments"] = {s: assess([r for r in cases if r["segment"] == s])
                           for s in sorted({r["segment"] for r in cases})}
    summary["zero_of_100_upper_95"] = zero_failure_upper(100)
    routine, consequential = (summary["segments"][s] for s in ("routine", "consequential"))
    summary["cost_break_even_consequential_to_routine"] = (
        (routine["new_pass"]-routine["old_pass"]) /
        (consequential["old_pass"]-consequential["new_pass"]))
    assert summary["new_pass"]-summary["old_pass"] == summary["improved"]-summary["regressed"]
    output = HERE / "results"
    output.mkdir(exist_ok=True)
    with (output / "synthetic_cases.csv").open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(cases[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(cases)
    (output / "upgrade_summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
