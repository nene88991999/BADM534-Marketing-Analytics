"""Generate TikZ sources from the verified aggregate teaching results."""
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
FIGURES = HERE.parents[1] / "06_Lecture_Notes/figures"


def coords(x, y):
    return " ".join(f"({a:.6f},{b:.6f})" for a, b in zip(x, y))


def main():
    months = pd.read_csv(HERE / "results/wikipedia_months.csv")
    old = months["Claude_(language_model)"]
    both = months.selected_title_views
    assert months.complete_days.eq(months.calendar_days).all()
    text = r"""\begin{tikzpicture}
\begin{axis}[width=12cm,height=6.4cm,xmin=-0.1,xmax=3.15,ymin=0,ymax=112,
 xlabel={Month in 2026},ylabel={Recorded Views (June = 100)},
 xtick={0,1,2,3},xticklabels={June,July,August,September},
 legend style={at={(0.98,0.98)},anchor=north east},grid=major]
"""
    text += r"\addplot[IlliniBlue,mark=*,mark size=2.5pt] coordinates {" + coords(range(4), 100 * both / both.iloc[0]) + "};\n"
    text += r"\addplot[IlliniOrange,dashed,mark=square*,mark size=2.5pt] coordinates {" + coords(range(4), 100 * old / old.iloc[0]) + "};\n"
    text += r"\legend{Two selected titles,Older title only}" + "\n\\end{axis}\n\\end{tikzpicture}\n"
    (FIGURES / "M02_genai_titles.tex").write_text(text)

    cohort = pd.read_csv(HERE / "results/cohorts.csv")
    cohort = cohort.loc[cohort.horizon_months.eq(12)].copy()
    columns = ["same_provider", "other_provider_only", "no_paid_provider"]
    np.testing.assert_array_equal(cohort[columns].sum(axis=1), cohort.cohort_size)
    labels = ",".join(f"{{{r.provider} ($n={r.cohort_size}$)}}" for r in cohort.itertuples())
    text = r"""\begin{tikzpicture}
\begin{axis}[width=11cm,height=7.2cm,xbar stacked,bar width=14pt,
 xmin=0,xmax=100,ymin=-0.6,ymax=4.6,xtick={0,25,50,75,100},
 xlabel={Share of the Starting Provider Cohort (\%)},
 ytick={0,1,2,3,4},yticklabels={LABELS},
 legend style={at={(0.5,1.05)},anchor=south,legend columns=1},
 y dir=reverse]
""".replace("LABELS", labels)
    styles = ["fill=IlliniBlue,draw=white", "fill=IlliniOrange!35,draw=white,postaction={pattern=north east lines,pattern color=IlliniOrange}", "fill=LightStorm,draw=white"]
    for column, style in zip(columns, styles):
        text += "\\addplot[" + style + "] coordinates {" + coords(100 * cohort[column] / cohort.cohort_size, range(5)) + "};\n"
    text += r"\legend{Same provider,Other providers only,No paid provider}" + "\n\\end{axis}\n\\end{tikzpicture}\n"
    (FIGURES / "M04_genai_cohorts.tex").write_text(text)

    slopes = pd.read_csv(HERE / "results/price_projections.csv")
    text = r"""\begin{tikzpicture}
\begin{axis}[width=10.5cm,height=5.5cm,xmin=-0.07,xmax=0,ymin=-0.5,ymax=2.5,
 xlabel={Log-Odds Price Coefficient per Dollar},
 ytick={0,1,2},yticklabels={{Exact binary benchmark},{New basic-plan flow},{Basic-plan stock}},
 xtick={-0.06,-0.04,-0.02,0},grid=major]
\addplot[Storm,dashed] coordinates {(-0.06,-0.4) (-0.06,2.4)};
"""
    for row, y, style in zip(slopes.itertuples(), [2, 1, 0], ["IlliniBlue,mark=*", "IlliniOrange,mark=square*", "Storm,mark=triangle*"]):
        text += f"\\addplot[{style},only marks,mark size=3pt] coordinates {{({row.price_coefficient:.8f},{y})}};\n"
    text += "\\end{axis}\n\\end{tikzpicture}\n"
    (FIGURES / "M08_genai_price.tex").write_text(text)


if __name__ == "__main__":
    main()
