"""Write editable Illinois-color TikZ from published and hypothetical tables."""
import csv
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
FIGURES = ROOT / "06_Lecture_Notes/figures"


def read_csv(path):
    with path.open(newline="") as stream:
        return list(csv.DictReader(stream))


def points(rows, value, low, high):
    return " ".join(f"({i},{float(r[value]):.8f}) += (0,{float(r[high])-float(r[value]):.8f})"
                    f" -= (0,{float(r[value])-float(r[low]):.8f})" for i, r in enumerate(rows))


def main():
    source = ROOT / "01_Resources/40_Econometric_Coding_Workflows/data/appendix_silent_vs_loud.csv"
    rows = read_csv(source)
    order = ["chatbot", "self_repair", "agent"]
    rows.sort(key=lambda r: order.index(r["agency"]))
    checked = read_csv(HERE / "results/benchmark_failure_rates.csv")
    assert [int(r["silent"]) for r in rows] == [int(r["silent"]) for r in checked]
    loud = points(rows, "loud_per100", "loud_per100_lo", "loud_per100_hi")
    silent = points(rows, "silent_per100", "silent_per100_lo", "silent_per100_hi")
    share = points(rows, "silent_share_of_failures_pct", "silent_share_of_failures_pct_lo", "silent_share_of_failures_pct_hi")
    tex = r"""\begin{tikzpicture}
\begin{axis}[name=left,width=6.3cm,height=6cm,xmin=-.3,xmax=2.3,ymin=0,ymax=16,
 xtick={0,1,2},xticklabels={Chatbot,Repair,Agent},ytick={0,5,10,15},
 tick label style={font=\small},ylabel={Failures per 100 Runs},grid=major,
 legend style={at={(.98,.98)},anchor=north east,font=\small},
 error bars/y dir=both,error bars/y explicit]
\addplot[IlliniBlue,mark=*] coordinates {LOUD};\addlegendentry{Loud}
\addplot[IlliniOrange,mark=square*,dashed] coordinates {SILENT};\addlegendentry{Silent}
\end{axis}
\begin{axis}[at={(left.south east)},anchor=south west,xshift=2.3cm,width=6.3cm,height=6cm,
 xmin=-.3,xmax=2.3,ymin=0,ymax=100,xtick={0,1,2},xticklabels={Chatbot,Repair,Agent},
 ytick={0,25,50,75,100},tick label style={font=\small},
 ylabel={Silent Share of Failures (\%)},grid=major,error bars/y dir=both,error bars/y explicit]
\addplot[IlliniOrange,mark=diamond*,dashed] coordinates {SHARE};
\end{axis}
\node[anchor=north,yshift=-.4cm,text width=13.4cm,align=center,font=\footnotesize] at (current bounding box.south) {14,400 assigned runs per workflow; 40 tasks and six models.\\Bars: authors' 95\% percentile intervals, resampling the 40 tasks.};
\end{tikzpicture}
""".replace("LOUD", loud).replace("SILENT", silent).replace("SHARE", share)
    (FIGURES / "M01_coding_failure_denominators.tex").write_text(tex)
    costs = read_csv(HERE / "results/decision_costs.csv")
    summary = json.loads((HERE / "results/decision_cost_summary.json").read_text())
    lines = {}
    for name in ["Basic", "Checked"]:
        selected = [r for r in costs if r["workflow"] == name]
        lines[name] = " ".join(f"({r['loss_per_undetected_error']},{float(r['expected_total_dollars']):.6f})" for r in selected)
    threshold = summary["break_even_loss_dollars"]
    assert abs(threshold - 7) < 1e-10
    tex = r"""\begin{tikzpicture}\begin{axis}[width=12cm,height=6.7cm,
 xmin=0,xmax=20,ymin=0,ymax=1400,xtick={0,5,7,10,15,20},ytick={0,200,400,600,800,1000,1200,1400},
 xlabel={Loss per Undetected Error (Dollars)},ylabel={Expected Cost for 1,000 Tasks (Dollars)},
 grid=major,legend style={at={(.03,.97)},anchor=north west}]
\addplot[IlliniBlue,mark=*] coordinates {BASIC};\addlegendentry{Basic}
\addplot[IlliniOrange,dashed,mark=square*] coordinates {CHECKED};\addlegendentry{Checked}
\draw[dotted,Storm] (axis cs:7,0)--(axis cs:7,620);
\node[anchor=north west,font=\small,align=left] at (axis cs:8,480) {Equal cost at a loss\\of 7 dollars per error};
\end{axis}
\node[anchor=north,yshift=-.35cm,text width=13cm,align=center,font=\footnotesize] at (current bounding box.south) {Hypothetical inputs: undetected-error probabilities 5\% and 1\%.\\Review and correction: 0.25 and 0.50 minutes per task at 60 dollars/hour.\\API charges: 0.02 and 0.05 dollars per task.};
\end{tikzpicture}
""".replace("BASIC", lines["Basic"]).replace("CHECKED", lines["Checked"])
    (FIGURES / "M08_review_and_decision_cost.tex").write_text(tex)
    print("Wrote two figures from their aggregate tables.")


if __name__ == "__main__":
    main()
