"""Build original Illinois-color TikZ from the verified calculation tables."""
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
FIGURES = HERE.parents[1]/"06_Lecture_Notes"/"figures"


def main():
    power = pd.read_csv(HERE/"results"/"andrews_directional_power.csv").set_index("direction")
    a, b = power.loc["A_only", "radius"], power.loc["B_only", "radius"]
    diagonal = power.loc["equal_increases", "effect_A"]
    text = r"""\begin{tikzpicture}
\begin{axis}[width=12.7cm,height=7.3cm,xmin=0,xmax=2.2,ymin=0,ymax=7.4,
 xlabel={True Effect on Outcome A (\$/MWh)},ylabel={True Effect on Outcome B (\$/MWh)},
 xtick={0,0.5,1,1.5,2},ytick={0,2,4,6},grid=major,
 title={Same Joint Test, Different Detectable Directions},title style={font=\small}]
\addplot[IlliniBlue,very thick,domain=0:90,samples=91] ({@A@*cos(x)},{@B@*sin(x)});
\addplot[only marks,mark=*,IlliniOrange,mark size=3pt] coordinates {(@A@,0) (0,@B@) (@D@,@D@)};
\draw[->,thick,IlliniOrange] (axis cs:0,0) -- (axis cs:@D@,@D@);
\node[anchor=south west,font=\footnotesize] at (axis cs:0.04,@B@) {B only: \$6.21};
\node[anchor=south west,font=\footnotesize] at (axis cs:@A@,0.12) {A only: \$1.55};
\node[anchor=west,align=left,font=\footnotesize] at (axis cs:0.15,3.15) {Below 80\% power\\inside the curve};
\node[anchor=west,align=left,font=\footnotesize] at (axis cs:1.15,5.8) {Above 80\% power\\outside the curve};
\end{axis}
\node[align=center,text width=12cm,font=\footnotesize] at (5.6,-2.0) {Synthetic independent estimates: SE(A) = \$0.50, SE(B) = \$2.00.\\Joint zero-null Wald test, two restrictions, size 5\%. Every point on the curve has 80\% power.};
\end{tikzpicture}
"""
    for token, value in [("A", a), ("B", b), ("D", diagonal)]:
        text = text.replace("@"+token+"@", f"{value:.10f}")
    (FIGURES/"M06_andrews_directional_power.tex").write_text(text)

    rows = pd.read_csv(HERE/"results"/"logic_extrapolation.csv")
    a = " ".join(f"({r.load},{r.linear})" for r in rows.itertuples())
    b = " ".join(f"({r.load},{r.threshold})" for r in rows.itertuples())
    (FIGURES/"M09_counterexample_extrapolation.tex").write_text(r"""\begin{tikzpicture}
\begin{axis}[width=12.5cm,height=7cm,xmin=0,xmax=2.15,ymin=0,ymax=16,
 xlabel={Normalized Load},ylabel={Price Response (\$/MWh)},grid=major,
 legend pos=north west,legend cell align=left,
 title={Identical Historical Responses Permit Different Future Costs},
 title style={font=\small}]
\path[fill=LightStorm,opacity=.25] (axis cs:0,0) rectangle (axis cs:1,16);
\addplot[IlliniBlue,very thick,domain=0:2,samples=101] {2*x};
\addlegendentry{Linear: $2x$}
\addplot[IlliniOrange,very thick,dashed,domain=0:2,samples=101] {2*x+10*max(x-1,0)^2};
\addlegendentry{Threshold: $2x+10\max\{x-1,0\}^2$}
\addplot[only marks,mark=*,IlliniBlue] coordinates {"""+a+r"""};
\addplot[only marks,mark=square*,IlliniOrange] coordinates {"""+b+r"""};
\node[font=\footnotesize,align=center] at (axis cs:.5,6.8) {Assumed Historical\\Support: $0\leq x\leq1$};
\node[anchor=west,font=\footnotesize] at (axis cs:2,14) {\$14};
\node[anchor=west,font=\footnotesize] at (axis cs:2,4) {\$4};
\end{axis}
\node[align=center,text width=12cm,font=\footnotesize] at (5.4,-2.2) {Synthetic response functions, with prices measured in the same units.\\Equality on the entire historical support leaves the response at $x=2$ unresolved.};
\end{tikzpicture}
""")


def institutional_figure():
    table = pd.read_csv(HERE/"results"/"institutional_comparisons.csv")
    row = table.set_index("comparison").loc["weighted_operationally_untreated"]
    text = r"""\begin{tikzpicture}
\node[font=\bfseries] at (5.1,1.25) {A Project Can Leave Costs Without Operating Capacity};
\node[box,text width=2.3cm,minimum height=1.2cm] (a) at (0,0) {Service\\Request};
\node[box,text width=2.3cm,minimum height=1.2cm] (b) at (3.4,0) {Utility\\Investment};
\node[orangebox,text width=2.3cm,minimum height=1.2cm] (c) at (6.8,0) {Project\\Cancelled};
\node[box,text width=2.3cm,minimum height=1.2cm] (d) at (10.2,0) {Allowed Cost\\Recovery};
\draw[edge] (a) -- (b); \draw[edge] (b) -- (c); \draw[accent] (c) -- (d);
\node[align=center,text width=12.5cm,font=\footnotesize] at (5.1,-1.3)
 {Possible sequence: recovery depends on regulation, contracts, and asset reuse.\\Zero operating MW does not establish zero project-related cost exposure.};
\node[box,text width=3.4cm,minimum height=1.25cm] (e) at (.5,-3.0)
 {Completed Project\\Increase: \$@T@/MWh};
\node[box,text width=3.4cm,minimum height=1.25cm] (f) at (5.1,-3.0)
 {Weighted Donors\\Increase: \$@C@/MWh};
\node[orangebox,text width=3.4cm,minimum height=1.25cm] (g) at (9.7,-3.0)
 {Change Difference\\\$@G@/MWh};
\node[font=\normalsize] at (2.8,-3.0) {$-$};
\node[font=\normalsize] at (7.4,-3.0) {$=$};
\node[align=center,text width=12.8cm,font=\footnotesize] at (5.1,-4.4)
 {Synthetic two-period comparison: equal baselines, no other changes.\\Donor weights: 75\% cancelled project (+\$8/MWh); 25\% unexposed (+\$0/MWh).};
\end{tikzpicture}
"""
    for token, field in [("T", "treated_change_usd_mwh"),
                         ("C", "donor_change_usd_mwh"),
                         ("G", "change_difference_usd_mwh")]:
        text = text.replace("@"+token+"@", f"{row[field]:.0f}")
    (FIGURES/"M06_institutional_exposure.tex").write_text(text)


if __name__ == "__main__":
    main()
    institutional_figure()
