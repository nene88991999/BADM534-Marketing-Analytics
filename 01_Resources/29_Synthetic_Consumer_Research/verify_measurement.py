"""Verify source identity and independent SSR arithmetic without importing upstream code.

All numerical inputs below are imposed illustrations. No survey is reconstructed.
Run from any directory with Python 3.10+ and no third-party dependencies.
"""

import ast
from fractions import Fraction as F
import hashlib
import json
from math import isclose, sqrt
from pathlib import Path
import platform
from statistics import mean

ROOT = Path(__file__).resolve().parent


def shifted_weights(similarities, epsilon=F(0)):
    """Apply the published shift-and-normalize equation to exact input fractions.

    Positive epsilon is allocated to the first minimum, as in the inspected code.
    An undefined normalization raises explicitly in this independent calculation.
    """
    assert len(similarities) == 5 and epsilon >= 0
    smallest = min(similarities)
    weights = [value - smallest for value in similarities]
    weights[similarities.index(smallest)] += epsilon
    total = sum(weights)
    if total == 0:
        raise ValueError("Equal similarities give an undefined normalization.")
    return [value / total for value in weights]


def expected_score(weights):
    return sum(F(rating) * weight for rating, weight in enumerate(weights, 1))


def ks_similarity(left, right):
    assert sum(left) == sum(right) == 1
    cumulative_left = cumulative_right = F(0)
    gaps = []
    for x, y in zip(left, right):
        cumulative_left += x
        cumulative_right += y
        gaps.append(abs(cumulative_left - cumulative_right))
    return 1 - max(gaps)


def main():
    catalog = json.loads((ROOT / "catalog.json").read_text())
    checked_files = []
    parsed_python = []
    for record in catalog["records"]:
        for entry in record["files"]:
            path = ROOT / entry["path"]
            data = path.read_bytes()
            assert len(data) == entry["bytes"], path
            assert hashlib.sha256(data).hexdigest() == entry["sha256"], path
            if "git_blob_sha" in entry:
                header = b"blob " + str(len(data)).encode() + b"\0"
                assert hashlib.sha1(header + data).hexdigest() == entry["git_blob_sha"], path
            checked_files.append(entry["path"])
            if path.suffix == ".py":
                ast.parse(data.decode(), filename=str(path))
                parsed_python.append(entry["path"])

    checks = []
    scores = [F(1, 5), F(3, 10), F(1, 2), F(4, 5), F(1)]
    weights = shifted_weights(scores)
    assert weights == [F(0), F(1, 18), F(1, 6), F(1, 3), F(4, 9)]
    assert sum(weights) == 1 and expected_score(weights) == F(25, 6)
    checks.append({"name": "Shifted weights and mean match exact hand calculation", "passed": True,
                   "weights": [float(x) for x in weights], "mean": float(expected_score(weights))})

    affine = [(1 + x) / 2 for x in scores]
    assert shifted_weights(affine) == weights
    checks.append({"name": "Positive affine similarity transformation cancels at epsilon zero", "passed": True})

    equal = [F(1, 5)] * 5
    try:
        shifted_weights(equal)
    except ValueError:
        undefined = True
    else:
        undefined = False
    assert undefined
    tied_positive = shifted_weights(equal, F(1, 10))
    assert tied_positive == [F(1), F(0), F(0), F(0), F(0)]
    checks.append({"name": "Equal-similarity boundary and first-minimum epsilon allocation", "passed": True,
                   "zero_epsilon": "undefined", "positive_epsilon_weights": [float(x) for x in tied_positive]})

    assert shifted_weights(scores, F(1, 10)) != shifted_weights(affine, F(1, 10))
    assert shifted_weights(scores, F(1, 10)) == shifted_weights(affine, F(1, 20))
    checks.append({"name": "Nonzero epsilon must follow the scale of similarity differences", "passed": True})

    human = [
        [F(0), F(0), F(1, 10), F(3, 10), F(6, 10)],
        [F(0), F(0), F(2, 10), F(3, 10), F(5, 10)],
        [F(0), F(0), F(3, 10), F(3, 10), F(4, 10)],
    ]
    constant = human[1]
    similarities = [ks_similarity(row, constant) for row in human]
    assert similarities == [F(9, 10), F(1), F(9, 10)]
    human_means = [expected_score(row) for row in human]
    synthetic_means = [expected_score(constant)] * 3
    assert len(set(human_means)) == 3 and len(set(synthetic_means)) == 1
    assert mean(similarities) == F(14, 15)
    checks.append({"name": "Close distribution fit can coexist with no concept discrimination", "passed": True,
                   "mean_ks_similarity": float(mean(similarities)),
                   "human_means": [float(x) for x in human_means],
                   "synthetic_means": [float(x) for x in synthetic_means],
                   "pearson_correlation": None, "correlation_status": "undefined: constant synthetic means"})

    latent_variance, error_variance = 4.0, 1.0
    human_correlation = latent_variance / (latent_variance + error_variance)
    predictor_correlation = sqrt(human_correlation)
    ratio = predictor_correlation / human_correlation
    assert isclose(human_correlation, 0.8) and isclose(ratio, sqrt(1.25)) and ratio > 1
    checks.append({"name": "Split-half benchmark is not a universal upper bound", "passed": True,
                   "latent_variance": latent_variance, "independent_error_variance": error_variance,
                   "human_human_correlation": human_correlation,
                   "latent_predictor_human_correlation": predictor_correlation, "ratio": ratio})

    output = {
        "scope": "Independent exact arithmetic on imposed inputs and static source checks; no empirical replication.",
        "checked_on": "2026-11-22",
        "python": platform.python_version(),
        "source_files_verified": checked_files,
        "upstream_python_syntax_parsed": parsed_python,
        "upstream_code_executed": False,
        "upstream_tests_executed": False,
        "model_calls": 0,
        "independent_checks": checks,
    }
    (ROOT / "source_checks.json").write_text(json.dumps(output, indent=2) + "\n")
    print(f"Verified {len(checked_files)} source files; parsed {len(parsed_python)} Python files; passed {len(checks)} arithmetic checks.")


if __name__ == "__main__":
    main()
