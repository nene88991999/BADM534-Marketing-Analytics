"""Write editable TikZ from the saved course calculations; no estimator runs."""
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
FIGURES = HERE.parents[1] / "06_Lecture_Notes" / "figures"


def coordinates(x, y):
    return " ".join(f"({a:.6f},{b:.6f})" for a, b in zip(x, y))


def build():
    a = np.linspace(0, 40, 81)
    curve = r"""\begin{tikzpicture}
\begin{axis}[xmin=0,xmax=40,ymin=9.5,ymax=15,
xlabel={Discount (percentage points)},ylabel={Profit per eligible customer (\$)},
legend style={at={(.5,1.04)},anchor=south,legend columns=2,fill=none},ymajorgrids=true]
\addplot[IlliniBlue,very thick] coordinates {CURVE};
\addplot[IlliniOrange,very thick,dashed] coordinates {(0,12.6666667) (40,12.6666667)};
\legend{Known response,Best linear projection}
\addplot[only marks,mark=*,IlliniBlue,mark size=3pt] coordinates {(20,14)};
\node[anchor=south,font=\small] at (axis cs:20,14.15) {20\% discount; \$14 profit};
\node[anchor=north,font=\small] at (axis cs:20,11.3) {Linear slope = 0};
\end{axis}
\end{tikzpicture}
""".replace("CURVE", coordinates(a, 10 + .4*a - .01*a*a))
    (FIGURES / "M06_discount_response.tex").write_text(curve)
    overlap = np.genfromtxt(HERE / "results/overlap.csv", delimiter=",", names=True)
    text = [r"\begin{tikzpicture}"]
    for i, (prefix, title) in enumerate([("broad", "Broader Overlap"), ("narrow", "Weak Overlap")]):
        text.append(r"\begin{axis}[width=6.2cm,height=5.4cm,at={("+str(7*i)+r"cm,0)},anchor=south west,"
                    r"xmin=0,xmax=40,ymin=0,ymax=.25,xtick={0,10,20,30,40},"
                    r"xlabel={Discount (pp)},ylabel={Density per pp},title={"+title+r"},"
                    r"title style={font=\small},ymajorgrids=true,"
                    r"legend style={at={(.5,-.36)},anchor=north,legend columns=2,fill=none,font=\scriptsize}]")
        for suffix, style in [("minus", "IlliniBlue,very thick"), ("plus", "IlliniOrange,very thick,dashed")]:
            text.append(r"\addplot["+style+r"] coordinates {"+coordinates(overlap['discount_pp'], overlap[prefix+'_'+suffix])+"};")
        text.extend([r"\legend{Type $-1$,Type $+1$}", r"\end{axis}"])
    text.append(r"\end{tikzpicture}")
    (FIGURES / "M06_dose_overlap.tex").write_text("\n".join(text)+"\n")
    stores = np.genfromtxt(HERE / "results/store_curves.csv", delimiter=",", names=True)
    text = [r"\begin{tikzpicture}"]
    for i, (s, title) in enumerate([(0, "Store 0: 12 Customers"), (4, "Store 4: 300 Customers")]):
        d = stores[stores['store'] == s]
        text.append(r"\begin{axis}[width=6.2cm,height=5.4cm,at={("+str(7*i)+r"cm,0)},anchor=south west,"
                    r"xmin=6,xmax=34,ymin=6,ymax=17,xtick={10,20,30},"
                    r"xlabel={Discount (pp)},ylabel={Profit per customer (\$)},title={"+title+r"},"
                    r"title style={font=\small},ymajorgrids=true,"
                    r"legend style={at={(.5,-.36)},anchor=north,legend columns=2,fill=none,font=\scriptsize}]")
        for col, style in [("truth", "IlliniBlue,very thick"), ("separate", "Storm,densely dashed"),
                           ("partial", "IlliniOrange,very thick,dashdotted")]:
            text.append(r"\addplot["+style+r"] coordinates {"+coordinates(d['discount_pp'], d[col])+"};")
        text.extend([r"\legend{Known,Separate,Partial}", r"\end{axis}"])
    text.append(r"\end{tikzpicture}")
    (FIGURES / "M06_store_pooling.tex").write_text("\n".join(text)+"\n")


if __name__ == "__main__":
    build()
