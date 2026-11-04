"""Construct a synthetic model-by-library comparison; no model APIs are called."""
import csv
import json
from fractions import Fraction
from pathlib import Path

OUT = Path(__file__).resolve().parent / "results"


def contrasts(rates):
    """Keys are (model, library), each coded 0 or 1; values are pass fractions."""
    if set(rates) != {(0, 0), (0, 1), (1, 0), (1, 1)}:
        raise ValueError("All four conditions are required")
    return {
        "model_without_library": rates[1, 0] - rates[0, 0],
        "model_with_library": rates[1, 1] - rates[0, 1],
        "library_with_earlier_model": rates[0, 1] - rates[0, 0],
        "library_with_newer_model": rates[1, 1] - rates[1, 0],
        "interaction": rates[1, 1] - rates[1, 0] - rates[0, 1] + rates[0, 0],
        "joint_change": rates[1, 1] - rates[0, 0],
    }


def main():
    # Imposed counts: 100 assigned tasks in every cell. An unfinished task fails.
    # All cells use the same task population, rubric, deadline, and resource limits.
    passes = {(0, 0): 60, (0, 1): 70, (1, 0): 65, (1, 1): 85}
    rates = {key: Fraction(count, 100) for key, count in passes.items()}
    effects = contrasts(rates)
    # Two independent paths from the initial cell to the final cell must agree.
    assert effects["joint_change"] == Fraction(25, 100)
    assert effects["joint_change"] == (
        effects["model_without_library"] + effects["library_with_newer_model"]
    )
    assert effects["joint_change"] == (
        effects["library_with_earlier_model"] + effects["model_with_library"]
    )
    assert effects["interaction"] == Fraction(10, 100)
    OUT.mkdir(exist_ok=True)
    with (OUT / "factorial_cells.csv").open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["model", "library", "assigned", "passed", "pass_fraction"])
        for (model, library), passed in passes.items():
            writer.writerow([model, library, 100, passed, float(rates[model, library])])
    result = {
        "scope": "Constructed counts; no observed AI performance or causal estimate.",
        "units": "percentage points in the fraction of all assigned tasks passing",
        "contrasts_pp": {key: float(100 * value) for key, value in effects.items()},
    }
    (OUT / "factorial_results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
