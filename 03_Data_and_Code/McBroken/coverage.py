"""Compare availability denominators and draw the observed US time series."""
import json
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent
FIGURES = ROOT.parents[1] / "06_Lecture_Notes/figures"


def main():
    daily = pd.read_csv(ROOT / "data/daily_us.csv", parse_dates=["date"])
    results = ROOT / "results"
    results.mkdir(exist_ok=True)
    rows = []
    for threshold in [0, 1000, 2000, 5000]:
        sample = daily[daily.n_checked.notna() & daily.n_checked.ge(threshold)]
        rows.append({"minimum_checked": threshold, "days": len(sample),
                     "checked_records": int(sample.n_checked.sum()),
                     "unavailable_records": int(sample.n_broken.sum()),
                     "equal_day_percent": 100 * (sample.n_broken / sample.n_checked).mean(),
                     "pooled_record_percent": 100 * sample.n_broken.sum() / sample.n_checked.sum()})
    pd.DataFrame(rows).to_csv(results / "coverage_sensitivity.csv", index=False)
    (results / "coverage.json").write_text(json.dumps({
        "missing_us_dates": daily.loc[daily.n_checked.isna(), "date"].dt.strftime("%Y-%m-%d").tolist(),
        "low_coverage_dates": daily.loc[daily.n_checked.lt(2000), "date"].dt.strftime("%Y-%m-%d").tolist(),
        "sensitivity": rows}, indent=2) + "\n")
    daily["day"] = (daily.date - daily.date.min()).dt.days
    def points(column, scale):
        return " ".join(f"({r.day},{getattr(r, column) * scale:.6f})"
                        if pd.notna(getattr(r, column)) else f"({r.day},nan)"
                        for r in daily.itertuples())
    figure = r"""\begin{tikzpicture}
\begin{axis}[name=counts,width=12.5cm,height=4.7cm,xmin=0,xmax=364,
 ymin=0,ymax=15000,ylabel={US Records},xtick=\empty,scaled y ticks=false,
 ytick={0,5000,10000,15000},unbounded coords=jump]
\addplot[IlliniBlue] coordinates {COUNTS};
\addplot[Storm,dashed] coordinates {(0,2000) (364,2000)};
\end{axis}
\begin{axis}[at={(counts.south west)},anchor=north west,yshift=-0.55cm,
 width=12.5cm,height=4.7cm,xmin=0,xmax=364,ymin=0,ymax=100,
 ylabel={Unavailable (\%)},xlabel={Days Since October 25, 2025},
 xtick={0,90,180,270,364},unbounded coords=jump]
\addplot[IlliniOrange] coordinates {RATES};
\end{axis}
\end{tikzpicture}
"""
    (FIGURES / "M02_mcbroken_coverage.tex").write_text(
        figure.replace("COUNTS", points("n_checked", 1))
              .replace("RATES", points("share_unavailable", 100)))
    print(pd.DataFrame(rows).to_string(index=False))


if __name__ == "__main__":
    main()
