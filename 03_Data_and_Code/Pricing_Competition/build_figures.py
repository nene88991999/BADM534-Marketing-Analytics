"""Generate the editable surplus figure from the released aggregate table."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
COURSE = ROOT.parents[1]


def run():
    with (ROOT / "results/policies.csv").open() as stream:
        rows = list(csv.DictReader(stream))
    selected = []
    for objective in ("independent", "joint"):
        for accuracy in (0.5, 1.0):
            matches = [row for row in rows if row["objective"] == objective
                       and float(row["accuracy"]) == accuracy]
            if len(matches) != 1:
                raise ValueError("Expected one policy row per endpoint")
            selected.append(matches[0])
    def points(key):
        return " ".join(f"({i},{float(row[key]):.10f}) [{float(row[key]):.10f}]"
                        for i, row in enumerate(selected, 1))
    text = r"""\begin{tikzpicture}
\begin{axis}[width=13.5cm,height=7.0cm,ybar stacked,bar width=30pt,
 ymin=0,ymax=72,ytick={0,20,40,60},ylabel={Dollars per market-day},
 xtick={1,2,3,4},xticklabels={Independent\\$r=0.5$,Independent\\$r=1$,Joint\\$r=0.5$,Joint\\$r=1$},
 x tick label style={align=center,font=\small},xmin=.4,xmax=4.6,
 ymajorgrids=true,legend cell align=left,
 legend style={at={(.5,1.04)},anchor=south,legend columns=2,font=\small,/tikz/column sep=12pt},
 point meta=explicit,
 nodes near coords={\pgfmathprintnumber[fixed,precision=2,fixed zerofill]{\pgfplotspointmeta}},
 every node near coord/.append style={font=\footnotesize,text=white}]
\addplot[fill=IlliniBlue,draw=IlliniBlue] coordinates {PROFIT};
\addplot[fill=IlliniOrange,draw=IlliniOrange] coordinates {SURPLUS};
\legend{Total Firm Profit,Consumer Surplus}
\end{axis}
\end{tikzpicture}
"""
    text = text.replace("PROFIT", points("profit")).replace("SURPLUS", points("consumer_surplus"))
    (COURSE / "06_Lecture_Notes/figures/M04_pricing_welfare.tex").write_text(text)


if __name__ == "__main__":
    run()
