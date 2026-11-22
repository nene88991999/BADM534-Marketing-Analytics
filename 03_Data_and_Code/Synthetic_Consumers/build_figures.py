"""Build two editable Illinois-color figures from the saved aggregate results."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FIGURES = ROOT.parents[1] / "06_Lecture_Notes/figures"


def points(values):
    return " ".join(f"({i},{value:.8f})" for i, value in enumerate(values, 1))


def main():
    responses = json.loads((ROOT / "results/response_ratings.json").read_text())
    chosen = {r["anchor_set"]:r for r in responses
              if (r["concept"], r["persona"], r["repeat"]) == ("refill", "p01", 1)}
    figure = r"""% Same instructor-authored answer; imposed similarities; no model call.
\begin{tikzpicture}
\begin{axis}[width=13.5cm,height=6.3cm,ybar,bar width=15pt,
 xmin=.5,xmax=5.5,xtick={1,2,3,4,5},ymin=0,ymax=60,
 ytick={0,10,20,30,40,50,60},xlabel={Purchase-Intent Category},
 ylabel={Assigned Weight (\%)},
 legend style={at={(.5,1.02)},anchor=south,legend columns=2,column sep=8pt,fill=none,draw=none}]
"""
    for name, color in [("set_1", "IlliniBlue"), ("set_2", "IlliniOrange")]:
        row = chosen[name]
        figure += f"\\addplot[draw={color},fill={color}] coordinates {{{points([100*x for x in row['distribution']])}}};\n"
        figure += f"\\addlegendentry{{Set {name[-1]}, Mean {row['mean_rating']:.2f}}}\n"
    figure += "\\end{axis}\n\\end{tikzpicture}\n"
    (FIGURES / "M05_anchor_ratings.tex").write_text(figure)

    details = json.loads((ROOT / "results/screening_details.json").read_text())
    pooled = [r for r in details if r["candidate"] == "pooled"]
    overall = [sum(r["reference_distribution"][k] for r in pooled)/6 for k in range(5)]
    figure = r"""% Six synthetic concepts, 100 invented ratings each; all candidate patterns imposed.
\begin{tikzpicture}
\begin{axis}[at={(0,0)},anchor=south west,width=6.1cm,height=5.5cm,ybar,bar width=13pt,
 xmin=.5,xmax=5.5,xtick={1,2,3,4,5},ymin=0,ymax=60,ytick={0,20,40,60},
 xlabel={Rating Category},ylabel={Overall Share (\%)},title={Identical Overall Distributions}]
"""
    figure += f"\\addplot[draw=IlliniBlue,fill=IlliniBlue] coordinates {{{points([100*x for x in overall])}}};\n"
    figure += r"""\end{axis}
\begin{axis}[at={(7.1cm,0)},anchor=south west,width=6.1cm,height=5.5cm,
 xmin=.8,xmax=6.2,xtick={1,2,3,4,5,6},xticklabels={A,B,C,D,E,F},
 ymin=3.9,ymax=4.6,ytick={4,4.2,4.4,4.6},
 xlabel={Concept},ylabel={Mean Rating},title={Different Concept Rankings},
 legend style={at={(.5,-.32)},anchor=north,legend columns=2,font=\scriptsize,fill=none,draw=none}]
"""
    series = [("Reference", "IlliniBlue,mark=*", [r["reference_mean"] for r in pooled])]
    for name, style in [("pooled", "Storm,mark=triangle*,dotted"),
                        ("reversed", "IlliniOrange,mark=square*,dashed"),
                        ("compressed", "Patina,mark=diamond*,dashdotted")]:
        series.append((name.title(), style, [r["predicted_mean"] for r in details if r["candidate"] == name]))
    for name, style, values in series:
        figure += f"\\addplot[{style}] coordinates {{{points(values)}}};\n\\addlegendentry{{{name}}}\n"
    figure += "\\end{axis}\n\\end{tikzpicture}\n"
    (FIGURES / "M04_concept_screening.tex").write_text(figure)
    print("Wrote two TikZ figures from saved synthetic results.")


if __name__ == "__main__":
    main()
