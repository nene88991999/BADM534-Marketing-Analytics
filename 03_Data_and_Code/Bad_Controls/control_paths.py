"""Exact balanced synthetic examples of adjustment. Python 3.10+, NumPy."""
import csv
from itertools import product
from pathlib import Path
import numpy as np

OUT = Path(__file__).resolve().parent / "results"


def slope(y, d, *controls):
    design = np.column_stack([np.ones(len(d)), d, *controls])
    assert np.linalg.matrix_rank(design) == design.shape[1]
    return float(np.linalg.lstsq(design, y, rcond=None)[0][1])


def examples():
    # All 16 combinations have equal weight: independent, mean-zero shocks.
    z, u, e, v = np.array(list(product([-1.0, 1.0], repeat=4))).T
    d = (z + 1) / 2
    mediator = 2 * d + u
    collider = d + u
    cases = [
        ("mediator", d, d + 3 * mediator + v, mediator, 7, 1),
        ("post_treatment_collider", d, u + v, collider, 0, -1),
        ("pre_treatment_collider", u + e, v + z, u + v, 0, -1 / 3),
        ("instrument_like_control", 3 * z + u + e,
         3 * z + 3 * u + e + v, z, 13 / 11, 2),
        ("measured_confounder", 3 * z + u + e,
         3 * z + 3 * u + e + v, u, 13 / 11, 1),
    ]
    observations, results = [], []
    for case, treatment, outcome, control, raw, adjusted in cases:
        for index, (a, y, c) in enumerate(zip(treatment, outcome, control)):
            observations.append(dict(case=case, row=index, treatment=a,
                                     outcome=y, control=c, weight=1 / 16))
        before = slope(outcome, treatment)
        after = slope(outcome, treatment, control)
        # Independent analytical slopes, not regressions reused as targets.
        assert np.isclose(before, raw) and np.isclose(after, adjusted)
        results.append(dict(case=case, unadjusted=before, adjusted=after,
                            analytical_unadjusted=raw,
                            analytical_adjusted=adjusted))
    return observations, results


def save(name, rows):
    OUT.mkdir(exist_ok=True)
    with (OUT / name).open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    observations, results = examples()
    save("control_observations.csv", observations)
    save("control_estimates.csv", results)
    for row in results:
        print(row["case"], round(row["unadjusted"], 6),
              round(row["adjusted"], 6))
