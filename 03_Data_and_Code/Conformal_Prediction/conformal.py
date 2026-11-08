"""Finite-sample split-conformal thresholds for a fixed score function."""
from fractions import Fraction
from math import ceil, isfinite


def threshold(scores, alpha="0.10"):
    """Return the kth score; use infinity when the required rank is n + 1."""
    values = sorted(float(s) for s in scores)
    error_rate = Fraction(str(alpha))
    if not values or not 0 < error_rate < 1:
        raise ValueError("Nonempty scores and 0 < alpha < 1 are required")
    if any(not isfinite(s) for s in values):
        raise ValueError("Calibration scores must be finite")
    rank = ceil((len(values) + 1) * (1 - error_rate))
    return values[rank - 1] if rank <= len(values) else float("inf")


def label_set(probabilities, cutoff):
    """Include labels whose 1 - probability score is at most the cutoff."""
    p = {label: Fraction(str(value))
         for label, value in probabilities.items()}
    if not p or any(value < 0 or value > 1 for value in p.values()):
        raise ValueError("Nonempty probabilities in [0, 1] are required")
    if sum(p.values()) != 1:
        raise ValueError("Probabilities must sum to one")
    if cutoff == float("inf"):
        return list(p)
    if not isfinite(cutoff):
        raise ValueError("The cutoff must be finite or positive infinity")
    bound = Fraction(str(cutoff))
    return [label for label, value in p.items() if 1 - value <= bound]
