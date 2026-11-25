"""Fit a rotation and scale; compare geometry and decisions on invented vectors."""
import json
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent


def fit_map(donor, recipient):
    donor, recipient = np.asarray(donor, float), np.asarray(recipient, float)
    if donor.shape != recipient.shape or donor.ndim != 2 or len(donor) < 2:
        raise ValueError("Paired two-dimensional arrays of the same shape are required.")
    if not np.isfinite(donor).all() or not np.isfinite(recipient).all():
        raise ValueError("Inputs must be finite.")
    mu_d, mu_r = donor.mean(axis=0), recipient.mean(axis=0)
    x, y = donor - mu_d, recipient - mu_r
    if np.linalg.norm(x) == 0 or np.linalg.norm(y) == 0:
        raise ValueError("Both representations must vary.")
    u, _, vt = np.linalg.svd(x.T @ y, full_matrices=False)
    return mu_d, mu_r, u @ vt, float(np.linalg.norm(y) / np.linalg.norm(x))


def apply_map(values, fitted):
    mu_d, mu_r, rotation, scale = fitted
    return mu_r + scale * (np.asarray(values) - mu_d) @ rotation


def neighbors(values, k):
    values = np.asarray(values, float)
    if not 0 < k < len(values):
        raise ValueError("k must be between 1 and n-1.")
    norm = (values * values).sum(axis=1)
    distances = np.maximum(norm[:, None] + norm[None, :] - 2 * values @ values.T, 0)
    # Twelve decimals treat roundoff from rotations as a distance tie.
    distances = np.round(distances, 12)
    np.fill_diagonal(distances, np.inf)
    # Stable sorting breaks exact distance ties by the common row index.
    return np.argsort(distances, axis=1, kind="stable")[:, :k]


def neighbor_overlap(a, b, k):
    na, nb = neighbors(a, k), neighbors(b, k)
    return float(np.mean([len(set(x) & set(y)) / k for x, y in zip(na, nb)]))


def synthetic_case():
    train = np.array([(s, c) for s in [-4, -2, 2, 4] for c in [-1, 1]], float)
    test = np.array([(s, c) for s in [-3, -1, 1, 3] for c in [-1, 1]], float)
    rotation = np.array([[0., 1.], [-1., 0.]])
    donor = test @ rotation
    fitted = fit_map(train @ rotation, train)
    candidates = {"recipient": test, "rotated_unmapped": donor,
                  "compressed_style": test * [0.2, 1.],
                  "rotated_aligned": apply_map(donor, fitted)}
    target = test[:, 1] > 0
    results = []
    for name, values in candidates.items():
        prediction = values[:, 1] > 0
        results.append(dict(name=name, values=values.tolist(),
                            neighbor_overlap_k2=neighbor_overlap(test, values, 2),
                            correct=int((prediction == target).sum()), cases=len(test),
                            accuracy=float((prediction == target).mean())))
    return dict(setup="Invented style and review coordinates; review when coordinate 2 > 0",
                train=train.tolist(), test=test.tolist(), rotation=rotation.tolist(),
                fitted_rotation=fitted[2].tolist(), fitted_scale=fitted[3], results=results)


if __name__ == "__main__":
    result = synthetic_case()
    (HERE / "results/synthetic.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
