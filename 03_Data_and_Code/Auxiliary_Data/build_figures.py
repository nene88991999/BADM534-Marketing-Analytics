"""Write editable Illinois-color figures from the saved analytic tables."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FIGURES = ROOT.parents[1] / "06_Lecture_Notes/figures"


def read(name):
    with (ROOT / "results" / name).open() as stream:
        return list(csv.DictReader(stream))


def coordinates(rows, x, y, scale=1):
    return " ".join(f"({float(r[x]):.9f},{scale * float(r[y]):.9f})" for r in rows)


def main():
    rows = read("profile_means.csv")
    figure = "% Generated from invented analytic means by Auxiliary_Data/build_figures.py.\n\\begin{tikzpicture}\n"
    panels = [([r for r in rows if r["price"] == "-1"], "feature", "Standard,Premium", "Feature at Low Price", "Product Feature"),
              ([r for r in rows if r["feature"] == "-1"], "price", "Low,High", "Price with Standard Feature", "Price")]
    for i, (chosen, x, labels, title, xlabel) in enumerate(panels):
        figure += rf"""\begin{{axis}}[at={{({7.1*i}cm,0)}},anchor=south west,
width=6.1cm,height=5.7cm,xmin=-1.3,xmax=1.3,xtick={{-1,1}},xticklabels={{{labels}}},
ymin=1.8,ymax=4.6,ytick={{2,3,4}},xlabel={{{xlabel}}},ylabel={{Mean Rating}},title={{{title}}},
legend style={{at={{(.5,-.30)}},anchor=north,legend columns=2,column sep=8pt,font=\scriptsize,fill=none,draw=none}}]
"""
        for source, style, label in [("primary_mean", "IlliniBlue,mark=*", "Primary"),
                                      ("auxiliary_mean", "IlliniOrange,mark=square*,dashed", "Auxiliary")]:
            figure += f"\\addplot[{style}] coordinates {{{coordinates(chosen, x, source)}}};\n"
            if i == 0:
                figure += f"\\addlegendentry{{{label}}}\n"
        figure += "\\end{axis}\n"
    (FIGURES / "M04_auxiliary_contrasts.tex").write_text(figure + "\\end{tikzpicture}\n")

    curve = read("value_curve.csv")
    figure = r"""% Synthetic four-profile model; cost ratios vary; source variances and bias features fixed.
\begin{tikzpicture}
\begin{axis}[width=13.5cm,height=6.6cm,xmin=0,xmax=.4,ymin=-1,ymax=37,
xtick={0,.1,.2,.333333333,.4},xticklabels={0,0.1,0.2,$1/3$,0.4},
ytick={0,10,20,30},xlabel={Information-Cost Ratio $\lambda$},
ylabel={Asymptotic Cost Saving (\%)},
legend style={at={(.5,-.25)},anchor=north,legend columns=1,fill=none,draw=none}]
"""
    figure += f"\\addplot[IlliniOrange] coordinates {{{coordinates(curve[1:], 'information_cost_ratio', 'saving_fraction', 100)}}};\n"
    figure += "\\addlegendentry{Bias in Intercept and Price}\n"
    figure += "\\addplot[IlliniBlue,dashed] coordinates {(0,0) (.4,0)};\n\\addlegendentry{Bias in Every Response Feature}\n"
    figure += "\\addplot[only marks,mark=o,IlliniOrange,forget plot] coordinates {(0,33.333333333)};\n"
    figure += "\\node[anchor=west,font=\\small] at (axis cs:.01,34) {Limit: 33.33\\%};\n"
    figure += "\\addplot[Storm,dotted,forget plot] coordinates {(.333333333,0) (.333333333,32)};\n"
    figure += "\\end{axis}\n\\end{tikzpicture}\n"
    (FIGURES / "M04_auxiliary_value.tex").write_text(figure)

    sensitivity = read("bias_sensitivity.csv")
    figure = r"""% Analytic MSE; both source counts grow proportionally; omitted feature bias is fixed.
\begin{tikzpicture}
\begin{axis}[width=13.5cm,height=6.6cm,xmode=log,log basis x=2,xmin=.9,xmax=36,
xtick={1,2,4,8,16,32},xticklabels={1,2,4,8,16,32},ymin=0,ymax=.085,
ytick={0,.02,.04,.06,.08},yticklabels={0,0.02,0.04,0.06,0.08},scaled y ticks=false,
xlabel={Multiplier of Both Source Sample Sizes},ylabel={Total Coefficient MSE},
legend style={at={(.5,-.25)},anchor=north,legend columns=2,font=\small,fill=none,draw=none}]
"""
    for name, style, label in [
        ("correct_model_mse", "IlliniBlue,mark=*", "Correct Bias Model"),
        ("omitted_bias_mse", "IlliniOrange,mark=square*", "Omitted Feature Bias"),
        ("squared_bias", "Storm,dashed", "Squared Bias"),
        ("original_mse_target", "Patina,dotted", "Original MSE Target"),
    ]:
        figure += f"\\addplot[{style}] coordinates {{{coordinates(sensitivity, 'sample_multiplier', name)}}};\n\\addlegendentry{{{label}}}\n"
    figure += "\\end{axis}\n\\end{tikzpicture}\n"
    (FIGURES / "M07_auxiliary_bias.tex").write_text(figure)
    print("Wrote three TikZ figures from saved analytic tables.")


if __name__ == "__main__":
    main()
