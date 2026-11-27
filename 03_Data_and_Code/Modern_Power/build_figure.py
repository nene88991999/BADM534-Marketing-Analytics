"""Map the verified residential comparison to two hypothesis-test regions."""
import json
from pathlib import Path

from scipy.stats import norm

root = Path(__file__).resolve().parents[2]
r = json.loads(Path(__file__).with_name("results.json").read_text())["cases"][0]
b, se, margin = r["estimate"], r["se"], 2.0
zero = norm.ppf(.975) * se
small = margin - norm.ppf(.95) * se
assert -zero < b < zero and b > small
lines = [
    r"\begin{tikzpicture}[x=1.6cm,y=1cm]",
    r"\node[anchor=west,font=\bfseries] at (-3,3.15) {Reject a Zero Price Effect};",
    r"\draw[IlliniBlue,thick] (-3,2.5) -- (4,2.5);",
    rf"\fill[IlliniOrange!35] (-3,2.25) rectangle ({-zero:.6f},2.75);",
    rf"\fill[IlliniOrange!35] ({zero:.6f},2.25) rectangle (4,2.75);",
    rf"\draw[IlliniOrange,very thick] ({-zero:.6f},2.2) -- ({-zero:.6f},2.8);",
    rf"\draw[IlliniOrange,very thick] ({zero:.6f},2.2) -- ({zero:.6f},2.8);",
    rf"\node[below,font=\footnotesize] at ({-zero:.6f},2.15) {{$-2.075$}};",
    rf"\node[below,font=\footnotesize] at ({zero:.6f},2.15) {{$2.075$}};",
    r"\node[font=\footnotesize] at (-.2,2.72) {Two-sided 5\% test};",
    r"\node[anchor=west,font=\bfseries] at (-3,1.15) {Exclude an Increase of at Least \$2/MWh};",
    r"\draw[IlliniBlue,thick] (-3,.15) -- (4,.15);",
    rf"\fill[IlliniOrange!35] (-3,-.1) rectangle ({small:.6f},.4);",
    rf"\draw[IlliniOrange,very thick] ({small:.6f},-.15) -- ({small:.6f},.45);",
    rf"\node[above,font=\footnotesize] at ({small:.6f},.45) {{$0.258$}};",
    r"\node[font=\footnotesize] at (-1.5,.15) {One-sided 5\% test};",
    rf"\draw[dashed,IlliniBlue] ({b:.6f},-.15) -- ({b:.6f},2.8);",
    rf"\fill[IlliniBlue] ({b:.6f},2.5) circle (2.6pt);",
    rf"\fill[IlliniBlue] ({b:.6f},.15) circle (2.6pt);",
    rf"\node[anchor=west,font=\footnotesize,align=left] at ({b+.18:.6f},1.4) {{Observed estimate\\\$1.749/MWh}};",
    r"\foreach \x in {-3,-2,-1,0,1,2,3,4}{\draw[IlliniBlue] (\x,-.45)--(\x,-.55);\node[below,font=\footnotesize] at (\x,-.55){\x};}",
    r"\node at (.5,-1.3) {Possible Estimate (\$/MWh)};",
    r"\node[align=center,text width=12cm,font=\footnotesize] at (.5,-2.1) {Shading marks rejection regions; the observed estimate is outside both.\\Table 2, column 4, at the reference exposure. Fixed Gaussian SE: \$1.059/MWh.\\The \$2 margin is illustrative. The reported SE already clusters by utility.};",
    r"\end{tikzpicture}",
]
path = root / "06_Lecture_Notes/figures/M06_null_and_harm_regions.tex"
path.write_text("\n".join(lines) + "\n")
print("Built", path.name, "from the verified estimate, SE, and illustrative margin.")
