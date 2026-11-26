"""Generate editable numerical diagrams from the verified course tables."""
import csv
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIGURES = HERE.parents[1] / "06_Lecture_Notes" / "figures"


def read(name):
    with (HERE / "results" / name).open() as stream:
        return list(csv.DictReader(stream))


def main():
    effects = read("policy_effects.csv")
    assert [float(r["effect_pp"]) for r in effects] == [-40, 0]
    policy_points = [" ".join(f"({p},{100*float(row[key]):g})" for p, key in
                     [(10, "purchase_at_10"), (20, "purchase_at_20")])
                     for row in effects]
    figure = r'''\begin{tikzpicture}
\begin{axis}[name=history,width=6.15cm,height=5.7cm,xmin=8,xmax=22,ymin=0,ymax=100,
 xlabel={Historical Price (\$)},ylabel={Purchase Probability (\%)},
 title={Historical Observations},xtick={10,20},ytick={0,20,40,60,80,100},grid=major]
\addplot[only marks,mark=*,mark size=3pt,IlliniBlue] coordinates {(10,80)(20,40)};
\node[anchor=south west,font=\footnotesize] at (axis cs:10,80) {Group A};
\node[anchor=south west,font=\footnotesize] at (axis cs:20,40) {B};
\end{axis}
\begin{axis}[at={(history.east)},anchor=west,xshift=1.25cm,width=6.15cm,height=5.7cm,
 xmin=8,xmax=22,ymin=0,ymax=100,xlabel={Price Assigned to Everyone (\$)},
 title={Common-Price Intervention},xtick={10,20},ytick={0,20,40,60,80,100},grid=major,
 legend style={at={(.5,-.27)},anchor=north},legend columns=1]
\addplot[IlliniBlue,mark=*] coordinates {PRICE_POINTS};
\addlegendentry{Price response}
\addplot[IlliniOrange,dashed,mark=square*] coordinates {SELECTION_POINTS};
\addlegendentry{Group selection}
\end{axis}
\node[align=center,text width=13.3cm,font=\footnotesize] at (5.7,-3.0)
 {Synthetic population; groups A and B each have weight one half.\\
 Both models fit every historical cell. The price effect is $-40$ or $0$ percentage points.\\
 Lines join the two allowed prices; intermediate prices are outside the example.};
\end{tikzpicture}
'''.replace("PRICE_POINTS", policy_points[0]).replace("SELECTION_POINTS", policy_points[1])
    (FIGURES / "M06_compatible_price_models.tex").write_text(figure)
    inputs = read("purchase_and_value_inputs.csv")
    comparisons = read("valuation_comparisons.csv")
    cumulative = [float(r["cumulative_change_pp"]) for r in inputs]
    gains = [float(r["consumption_gain_usd"]) for r in comparisons]
    assert cumulative == [5, -5, -5, 0] and gains == [4.8, -4.9]
    points = " ".join(f"({k+1},{v:g})" for k, v in enumerate(cumulative))
    figure = r'''\begin{tikzpicture}
\begin{axis}[name=ranking,width=6.15cm,height=5.7cm,xmin=.5,xmax=4.5,ymin=-7,ymax=7,
 xlabel={Rank Cutoff},ylabel={Cumulative Change (pp)},
 title={Cumulative Purchase Shift},xtick={1,2,3,4},ytick={-5,0,5},grid=major]
\addplot[Storm,dashed] coordinates {(.5,0)(4.5,0)};
\addplot[IlliniBlue,only marks,mark=*,mark size=3pt] coordinates {CUMULATIVE_POINTS};
\end{axis}
\begin{axis}[at={(ranking.east)},anchor=west,xshift=1.5cm,width=5.9cm,height=5.7cm,
 xmin=.4,xmax=2.6,ymin=-7,ymax=7,ylabel={Gain (\$/Customer)},
 title={Value-Gap Comparison},xtick={1,2},xticklabels={Top Gap,Bottom Gap},
 xlabel={Large Value Gap},ytick={-5,0,5},grid=major]
\addplot[Storm,dashed] coordinates {(.4,0)(2.6,0)};
\addplot[ybar,bar width=20pt,fill=IlliniBlue,draw=IlliniBlue] coordinates {(1,TOP_GAIN)};
\addplot[ybar,bar width=20pt,fill=IlliniOrange,draw=IlliniOrange] coordinates {(2,BOTTOM_GAIN)};
\node[anchor=south] at (axis cs:1,TOP_GAIN) {$+\$4.80$};
\node[anchor=north] at (axis cs:2,BOTTOM_GAIN) {$-\$4.90$};
\end{axis}
\node[align=center,text width=13.4cm,font=\footnotesize] at (5.7,-1.7)
 {Synthetic values: $(100,2,1,0)$ or $(100,99,98,0)$ dollars per purchased product.\\
 Equal best and worst values; zero incremental procedure cost.};
\end{tikzpicture}
'''.replace("CUMULATIVE_POINTS", points).replace("TOP_GAIN", str(gains[0])).replace("BOTTOM_GAIN", str(gains[1]))
    (FIGURES / "M04_ordinal_welfare.tex").write_text(figure)
    print("Checked two saved tables against exact benchmarks; wrote two TikZ figures.")


if __name__ == "__main__":
    main()
