"""Write editable Illinois-color TikZ from the saved course calculations."""
from pathlib import Path
import csv

HERE = Path(__file__).resolve().parent
FIG = HERE.parents[1] / "06_Lecture_Notes/figures"


def save(name, content):
    (FIG / (name + ".tex")).write_text(content.strip() + "\n")


save("M05_access_network", r"""
\begin{tikzpicture}[x=1cm,y=1cm]
\fill[Industrial!10] (1.1,-.55) rectangle (2.9,4.5);
\node[rotate=90,text=Industrial] at (2,1.9) {River};
\draw[IlliniBlue,very thick] (0,0)--node[left]{4} (0,2)--node[left]{4}(0,4);
\draw[IlliniBlue,very thick] (4,0)--node[right]{4}(4,2)--node[right]{4}(4,4);
\draw[IlliniBlue,very thick] (0,4)--node[above]{2 minutes}(4,4);
\draw[Storm,densely dashed] (0,0)--(4,0);
\node[font=\scriptsize,align=center] at (2,-.8) {Straight-line comparison: 2 minutes\\Network route from W0 to E0: 18 minutes};
\foreach \x/\y/\s in {0/0/A,4/4/D} {\node[circle,draw=IlliniOrange,very thick,fill=white,minimum size=8mm] at (\x,\y) {\s};}
\foreach \x/\y/\s in {0/4/C,4/0/B} {\node[circle,draw=IlliniBlue,fill=IlliniBlue,text=white,minimum size=8mm] at (\x,\y) {\s};}
\fill[IlliniBlue] (0,2) circle (.08);\fill[IlliniBlue] (4,2) circle (.08);
\node[anchor=east,align=right] at (-.45,0) {W0\\100 people};
\node[anchor=east,align=right] at (-.45,2) {W1\\300 people};
\node[anchor=east,align=right] at (-.45,4) {W2\\100 people};
\node[anchor=west,align=left] at (4.45,0) {E0\\50 people};
\node[anchor=west,align=left] at (4.45,2) {E1\\50 people};
\node[anchor=west,align=left] at (4.45,4) {E2\\50 people};
\node[circle,draw=Storm,dashed,minimum size=9mm] at (8,2) {U};
\node[align=center] at (8,.95) {X: 150 people\\Status unknown\\No connecting path};
\node[align=center,font=\scriptsize] at (8,4) {Filled: available\\Orange outline: unavailable};
\end{tikzpicture}
""")

save("M02_map_footprint", r"""
\begin{tikzpicture}[x=1.7cm,y=1.7cm]
\begin{scope}
\path[fill=IlliniBlue!18,even odd rule] (-.1,-.1) rectangle (2.1,2.1) (.1,.1) rectangle (1.9,1.9);
\node at (1,2.5) {Road Corridor};
\node[align=center] at (1,-.55) {Shaded area: 1.60 km$^2$\\Four reachable nodes};
\end{scope}
\begin{scope}[xshift=7cm]
\fill[IlliniBlue!18] (-.1,-.1) rectangle (2.1,2.1);
\node at (1,2.5) {Filled Interior};
\node[align=center] at (1,-.55) {Shaded area: 4.84 km$^2$\\Four reachable nodes};
\end{scope}
\foreach \offset in {0,7} {
\begin{scope}[xshift=\offset cm]
\draw[IlliniBlue,very thick] (0,0) rectangle (2,2);
\foreach \x/\y in {0/0,0/2,2/0,2/2} {\fill[IlliniBlue] (\x,\y) circle (.05);}
\draw[IlliniOrange,very thick] (.93,.93)--(1.07,1.07) (.93,1.07)--(1.07,.93);
\node[align=center,font=\scriptsize] at (1,.65) {No modeled route\\to the center};
\end{scope}}
\end{tikzpicture}
""")

policies = list(csv.DictReader((HERE / "results/policies.csv").open()))
parts = [r"\begin{tikzpicture}\begin{axis}[width=12cm,height=5.8cm,xmin=0,xmax=105,ymin=-.5,ymax=2.5,ytick={0,1,2},yticklabels={Baseline,Restore A,Restore D},xlabel={Population With Access Within Five Minutes (\%)},xmajorgrids=true,legend style={at={(.5,-.28)},anchor=north,legend columns=2,column sep=6pt,fill=none}]"]
for i, row in enumerate(policies):
    lo, hi = 100*float(row["lower_share"]), 100*float(row["upper_share"])
    parts.append(rf"\addplot[Storm,very thick,forget plot] coordinates {{({lo},{i}) ({hi},{i})}};")
for field, color, mark, label in [("lower_share", "IlliniBlue", "*", "Known available"), ("upper_share", "IlliniOrange", "triangle*", "Including unknown")]:
    coords = " ".join(f"({100*float(r[field])},{i})" for i, r in enumerate(policies))
    parts.append(rf"\addplot[only marks,{color},mark={mark},mark size=3pt] coordinates {{{coords}}};\addlegendentry{{{label}}}")
parts.append(r"\end{axis}\end{tikzpicture}")
save("M08_access_priorities", "\n".join(parts))

observed = list(csv.DictReader((HERE / "results/observed_origins.csv").open()))
parts = [r"\begin{tikzpicture}\begin{axis}[width=12cm,height=6cm,xmin=0,xmax=6,ymin=-.55,ymax=3.5,ytick={0,1,2,3},yticklabels={South Neil,North Neil,Mattis,Cunningham},xlabel={Distance to Nearest Available Alternative (km)},xmajorgrids=true,legend style={at={(.5,-.28)},anchor=north,legend columns=2,column sep=6pt,fill=none}]"]
for i, row in enumerate(observed):
    parts.append(rf"\addplot[Storm,forget plot] coordinates {{({float(row['straight_km']):.6f},{i}) ({float(row['network_km']):.6f},{i})}};")
for field, color, mark, label in [("straight_km", "IlliniBlue", "*", "Straight line"), ("network_km", "IlliniOrange", "triangle*", "Modeled network")]:
    coords = " ".join(f"({float(r[field]):.6f},{i})" for i, r in enumerate(observed))
    parts.append(rf"\addplot[only marks,{color},mark={mark},mark size=3pt] coordinates {{{coords}}};\addlegendentry{{{label}}}")
parts.append(r"\node[font=\scriptsize,anchor=west,align=left] at (axis cs:.1,1.5) {North Neil's selected alternative:\\Mattis $\rightarrow$ South Neil};")
parts.append(r"\end{axis}\end{tikzpicture}")
save("M05_restaurant_distances", "\n".join(parts))
print("Wrote four TikZ figures.")
