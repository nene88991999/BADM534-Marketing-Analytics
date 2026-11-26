"""Generate editable Illinois-color figures from the executed null experiments."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent
FIGURES = ROOT.parents[1] / "06_Lecture_Notes/figures"


def main():
    diagram = r'''\begin{tikzpicture}[x=1cm,y=1cm]
\node[orangebox,text width=4.5cm] (a) at (2.4,0) {20 Stores Receive\\the Promotion};
\node[box,text width=4.5cm] (b) at (8.7,0) {20 Stores Receive\\Control};
\node[box,text width=4.5cm] (c) at (2.4,-2.2) {20 Customers per Store\\Shared Store Shock +\\Individual Customer Shock};
\node[box,text width=4.5cm] (d) at (8.7,-2.2) {20 Customers per Store\\Shared Store Shock +\\Individual Customer Shock};
\draw[accent] (a) -- (c); \draw[edge] (b) -- (d);
\node[box,text width=4.5cm] (e) at (2.4,-4.5) {Average 20 Store Means};
\node[box,text width=4.5cm] (f) at (8.7,-4.5) {Average 20 Store Means};
\draw[edge] (c) -- (e); \draw[edge] (d) -- (f);
\draw[<->,very thick,IlliniOrange] (e) -- node[above,font=\footnotesize] {Contrast} (f);
\node[align=center,text width=12cm,font=\footnotesize] at (5.55,-5.9) {Synthetic experiment: 40 independent stores and 800 customer outcomes.\\Equal store sizes preserve the customer-average point estimate.\\Shared shocks change its sampling uncertainty.};
\end{tikzpicture}'''
    (FIGURES / "M06_store_assignment.tex").write_text(diagram + "\n")
    data = pd.read_csv(ROOT / "results/null_calibration.csv")
    parts = [r'''\begin{tikzpicture}\begin{axis}[width=12cm,height=7cm,
        xmin=-.02,xmax=.52,ymin=0,ymax=60,xtick={0,.1,.3,.5},ytick={0,10,20,30,40,50,60},
        xlabel={Correlation Within a Store ($\rho$)},ylabel={Experiments Rejecting the True Null (\%)},
        grid=major,clip=true,legend style={at={(.03,.97)},anchor=north west},
        error bars/y dir=both,error bars/y explicit]''']
    for method, color, marker, label in [
        ("customer_rows", "IlliniOrange", "square*", "Customer Rows"),
        ("store_means", "IlliniBlue", "*", "Store Means")]:
        rows = data.loc[data.method.eq(method)]
        coords = " ".join(
            f"({r.rho},{100*r.rejection_rate:.5f}) += (0,{100*(r.mc_ci_high-r.rejection_rate):.5f})"
            f" -= (0,{100*(r.rejection_rate-r.mc_ci_low):.5f})" for r in rows.itertuples())
        parts += [r"\addplot[color="+color+",mark="+marker+",mark size=2.5pt] coordinates {"+coords+"};",
                  r"\addlegendentry{"+label+"}"]
    parts += [r"\addplot[dashed,Storm,mark=none,error bars/y explicit=false] coordinates {(0,5) (.5,5)};",
              r"\addlegendentry{Nominal 5\%}", r"\end{axis}",
              r"\node[anchor=north,yshift=-.3cm,text width=13cm,align=center,font=\footnotesize] at (current bounding box.south) {4,000 simulated experiments per correlation; 40 stores, 20 customers each.\\True effect is zero; one prespecified test at $\alpha=.05$.\\Bars: 95\% Wilson intervals for Monte Carlo rejection fractions.};",
              r"\end{tikzpicture}"]
    (FIGURES / "M06_null_calibration.tex").write_text("\n".join(parts) + "\n")


if __name__ == "__main__":
    main()
