"""Test pre-specified availability forecasts on later calendar dates."""
import json
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent
CUTOFF = pd.Timestamp("2026-08-01")


def fit_probabilities(train):
    counts = train.groupby("previous_unavailable")[["n_labeled", "n_unavailable"]].sum()
    if (counts.n_labeled <= 0).any() or set(counts.index) != {0, 1}:
        raise ValueError("Both prior-status groups require training observations")
    return (train.n_unavailable.sum() / train.n_labeled.sum(),
            counts.n_unavailable / counts.n_labeled)


def brier_score(n, successes, probability):
    """Exact row-level squared probability error from grouped binary counts."""
    return float(np.sum(successes * (1 - probability)**2
                        + (n - successes) * probability**2) / np.sum(n))


def main():
    data = pd.read_csv(ROOT / "data/transitions.csv", parse_dates=["date"])
    train, test = data[data.date < CUTOFF], data[data.date >= CUTOFF]
    assert train.date.max() < test.date.min()
    base, by_status = fit_probabilities(train)
    forecasts = {"Always available": np.zeros(len(test)),
                 "Training mean": np.full(len(test), base),
                 "Previous status": test.previous_unavailable.map(by_status).to_numpy()}
    n, y = test.n_labeled.to_numpy(), test.n_unavailable.to_numpy()
    scores = []
    for name, probability in forecasts.items():
        correct = np.where(probability >= 0.5, y, n - y)
        scores.append({"model": name, "brier_score": brier_score(n, y, probability),
                       "accuracy": float(correct.sum() / n.sum())})
    calibration = test.groupby("previous_unavailable")[["n_origins", "n_labeled", "n_unavailable"]].sum()
    calibration["forecast"] = by_status
    calibration["observed"] = calibration.n_unavailable / calibration.n_labeled
    calibration["label_coverage"] = calibration.n_labeled / calibration.n_origins
    results = ROOT / "results"
    results.mkdir(exist_ok=True)
    pd.DataFrame(scores).to_csv(results / "prediction_scores.csv", index=False)
    calibration.to_csv(results / "prediction_calibration.csv")
    summary = {"cutoff": str(CUTOFF.date()), "train_labeled_pairs": int(train.n_labeled.sum()),
               "test_labeled_pairs": int(n.sum()), "test_origins": int(test.n_origins.sum()),
               "test_unavailable": int(y.sum()), "baseline_probability": float(base),
               "test_label_coverage": float(n.sum() / test.n_origins.sum()),
               "train_first_target": str(train.date.min().date()),
               "train_last_target": str(train.date.max().date()),
               "test_last_target": str(test.date.max().date()), "scores": scores}
    (results / "prediction.json").write_text(json.dumps(summary, indent=2) + "\n")
    figure = r"""\begin{tikzpicture}
\begin{axis}[ybar,bar width=19pt,width=12.5cm,height=6.3cm,ymin=0,ymax=100,
 ylabel={Unavailable (\%)},xtick={0,1},xticklabels={Previously Available,Previously Unavailable},
 enlarge x limits=0.5,legend style={at={(0.5,-0.17)},anchor=north,legend columns=2,column sep=10pt},
 nodes near coords,every node near coord/.append style={font=\footnotesize,/pgf/number format/fixed,/pgf/number format/fixed zerofill,/pgf/number format/precision=1}]
"""
    for column, color in [("forecast", "IlliniBlue"), ("observed", "IlliniOrange")]:
        points = " ".join(f"({int(i)},{100*v:.6f})" for i, v in calibration[column].items())
        figure += f"\\addplot[draw={color},fill={color}!18] coordinates {{{points}}};\n"
    figure += "\\legend{Training Forecast,Later Observed Rate}\n\\end{axis}\n\\end{tikzpicture}\n"
    (ROOT.parents[1] / "06_Lecture_Notes/figures/M07_mcbroken_prediction.tex").write_text(figure)
    print(json.dumps(summary, indent=2))
    print(calibration.to_string())


if __name__ == "__main__":
    main()
