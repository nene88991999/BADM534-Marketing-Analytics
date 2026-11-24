"""Check saved-source arithmetic and two original mathematical illustrations.

Run with Python 3 from any directory. Uses the standard library, imports no
upstream code, and writes source_checks.json beside this program.
"""

from pathlib import Path
import csv
import hashlib
import json
import math
import sys

ROOT = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def close(left, right, tolerance=1e-10):
    return math.isclose(left, right, rel_tol=tolerance, abs_tol=tolerance)


def read_rows(relative):
    with (ROOT / relative).open(newline="") as handle:
        return list(csv.DictReader(handle))


def metrics(points, reconstructed):
    """Equal-weight centered inputs; positive coordinate 2 requires review."""
    require(len(points) == len(reconstructed) and points, "Matching nonempty inputs")
    means = [sum(p[j] for p in points) / len(points) for j in (0, 1)]
    require(all(close(m, 0.0) for m in means), "Illustration uses centered inputs")
    variation = [sum(p[j] ** 2 for p in points) for j in (0, 1)]
    error = [sum((p[j] - q[j]) ** 2 for p, q in zip(points, reconstructed))
             for j in (0, 1)]
    relevant = [p[1] > 0 for p in points]
    routed = [q[1] > 0 for q in reconstructed]
    true_positives = sum(a and b for a, b in zip(relevant, routed))
    positives = sum(relevant)
    return {
        "records": len(points),
        "coordinate_sums_of_squares": variation,
        "coordinate_squared_errors": error,
        "total_fvu": sum(error) / sum(variation),
        "total_variance_explained_pct": 100 * (1 - sum(error) / sum(variation)),
        "coordinate_fvu": [e / v for e, v in zip(error, variation)],
        "review_required": positives,
        "correctly_routed_for_review": true_positives,
        "review_recall": true_positives / positives,
    }


def example(scale):
    points = [(a * scale, b) for a in (-1, 1) for b in (-1, 1)]
    return {
        "points": points,
        "A": metrics(points, [(p[0], 0.0) for p in points]),
        "B": metrics(points, [(0.98 * p[0], p[1]) for p in points]),
    }


def main():
    checks = []
    manifest = json.loads((ROOT / "manifest.json").read_text())
    for record in manifest["files"]:
        data = (ROOT / record["path"]).read_bytes()
        git_blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        require(git_blob == record["git_blob_sha"], record["path"] + " Git blob mismatch")
        require(hashlib.sha256(data).hexdigest() == record["sha256"], record["path"] + " SHA256 mismatch")
    checks.append("All 13 archived source files match recorded Git blobs and SHA256 hashes")

    rows = read_rows("reference/results/additional/reconstruction/nine_model/nine_model_fidelity.csv")
    fidelity = {(r["model_key"], r["arm"]): r for r in rows}
    require(len(fidelity) == len(rows) == 18, "Expected nine unique model-condition pairs per arm")
    standard = fidelity["qwen-2.5-7b", "standard"]
    bypass = fidelity["qwen-2.5-7b", "bypass"]
    qwen = {
        "seeds_per_arm": int(standard["n_seeds"]),
        "total_variance_explained_pct": 100 * (1 - float(standard["fvu_total"])),
        "orthogonal_variance_unexplained_pct": 100 * float(standard["fvu_content"]),
        "orthogonal_error_relative_reduction": 1 - float(bypass["fvu_content"]) / float(standard["fvu_content"]),
    }
    require(qwen["seeds_per_arm"] == 3, "Qwen fidelity seed count")
    require(close(qwen["total_variance_explained_pct"], 99.963008), "Variance-explained arithmetic")
    require(close(qwen["orthogonal_variance_unexplained_pct"], 32.9781), "Orthogonal-error arithmetic")
    require(0.339 < qwen["orthogonal_error_relative_reduction"] < 0.340, "Relative improvement")
    checks.append("Saved fidelity rows have unique keys and reproduce the Qwen percentages")

    sharing_rows = read_rows("reference/results/tables/features_summary.csv")
    sharing = {(r["model"], r["condition"]): r for r in sharing_rows}
    require(len(sharing) == len(sharing_rows) == 18, "Unique feature-summary rows")
    qwen_sharing = {}
    for arm in ("standard", "bypass"):
        row = sharing["qwen-2.5-7b", arm]
        require(int(row["n_ref_pairs"]) == 4 and int(row["n_all_pairs"]) == 20, "Seed-pair denominators")
        qwen_sharing[arm] = {"reference_seed_top50": float(row["top50"]),
                             "all_ordered_pairs_top50": float(row["top50_allpairs"])}
    require(close(qwen_sharing["standard"]["reference_seed_top50"], 0.06), "Standard sharing")
    require(close(qwen_sharing["bypass"]["reference_seed_top50"], 0.995), "Reference sharing")
    require(close(qwen_sharing["bypass"]["all_ordered_pairs_top50"], 0.968), "All-pairs sharing")
    checks.append("Sharing rates retain their distinct four-pair and twenty-pair denominators")

    high = example(100.0)
    for arm in ("A", "B"):
        result = high[arm]
        v = result["coordinate_sums_of_squares"]
        component = result["coordinate_fvu"]
        weighted = sum(x * y for x, y in zip(v, component)) / sum(v)
        require(close(weighted, result["total_fvu"]), "Weighted FVU identity")
    checks.append("Direct reconstruction error equals the variance-weighted component errors")

    require(close(high["A"]["total_fvu"], 1 / 10001), "A hand calculation")
    require(close(high["B"]["total_fvu"], 4 / 10001), "B hand calculation")
    require(high["A"]["total_fvu"] < high["B"]["total_fvu"], "High-scale reconstruction ranking")
    checks.append("The high-scale example reproduces the independent 1/10001 and 4/10001 errors")

    require(high["A"]["review_required"] == high["B"]["review_required"] == 2, "Review denominator")
    require(high["A"]["review_recall"] == 0 and high["B"]["review_recall"] == 1, "Review outcome")
    checks.append("Routing recall is zero versus one with a common two-case denominator")

    low = example(1.0)
    require(low["A"]["total_fvu"] > low["B"]["total_fvu"], "Scale-dependent aggregate ranking")
    require(low["A"]["review_recall"] == high["A"]["review_recall"], "A routing unchanged")
    require(low["B"]["review_recall"] == high["B"]["review_recall"], "B routing unchanged")
    checks.append("Changing coordinate scale reverses reconstruction rankings while routing stays fixed")

    decompositions = []
    for slope in (1.0, 2.0):
        coefficient = math.sqrt(1 + slope * slope)
        directions = [(1 / coefficient, slope / coefficient),
                      (1 / coefficient, -slope / coefficient)]
        require(all(close(sum(x * x for x in d), 1) for d in directions), "Unit directions")
        contributions = [[coefficient * x for x in d] for d in directions]
        total = [sum(c[j] for c in contributions) for j in (0, 1)]
        require(close(total[0], 2) and close(total[1], 0), "Common reconstruction")
        error_after_removal = sum((target - actual) ** 2
                                  for target, actual in zip((2.0, 0.0), contributions[1]))
        require(close(error_after_removal, 1 + slope * slope), "Ablation error")
        decompositions.append({"slope": slope, "unit_directions": directions,
                               "coefficient_per_direction": coefficient,
                               "sum": total, "squared_error_after_removing_one": error_after_removal})
    checks.append("Two distinct sparse decompositions reconstruct the same vector with different removal errors")

    output = {
        "checked_on": "2026-11-24",
        "python_version": sys.version.split()[0],
        "dependencies": "Python standard library only",
        "run_command": "python3 01_Resources/34_Representation_Evaluation/source_checks.py",
        "status": "passed",
        "checks_passed": len(checks),
        "checks": checks,
        "archived_files_checked": len(manifest["files"]),
        "saved_qwen_fidelity": qwen,
        "saved_qwen_sharing": qwen_sharing,
        "synthetic_high_scale": high,
        "synthetic_low_scale": low,
        "synthetic_decompositions": decompositions,
        "scope": "Original standard-library calculations; saved measurements are attributed results. Synthetic vectors have imposed meanings. No upstream code or model execution.",
    }
    (ROOT / "source_checks.json").write_text(json.dumps(output, indent=2) + "\n")
    print(f"Passed {len(checks)} checks; verified {len(manifest['files'])} source files.")


if __name__ == "__main__":
    main()
