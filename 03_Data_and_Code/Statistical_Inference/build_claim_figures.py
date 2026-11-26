"""Editable figures for repeated experiments, campaign profit, and burden claims."""
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent
FIGURES = ROOT.parents[1] / "06_Lecture_Notes/figures"


def main():
    data = pd.read_csv(ROOT / "results/pvalue_bins.csv")
    parts = [r"\begin{tikzpicture}"]
    for i, stores in enumerate([40, 160]):
        parts.append(r"\begin{axis}[width=6.4cm,height=6cm,at={(" + str(i * 8.0) +
            r"cm,0)},anchor=south west,xmin=0,xmax=1,ymin=0,ymax=90,"
            r"xtick={0,.25,.5,.75,1},ytick={0,30,60,90},grid=major,"
            r"xlabel={$p$-Value},ylabel={Experiments in Bin (\%)},"
            r"title={" + str(stores) + r" Stores},"
            r"legend style={at={(.5,-.27)},anchor=north,legend columns=1}]")
        for effect, color, marker in [(0, "IlliniBlue", "*"), (8, "IlliniOrange", "square*")]:
            rows = data.loc[data.stores.eq(stores) & data.true_effect_dollars.eq(effect)]
            coords = " ".join(f"({(r.bin_left+r.bin_right)/2:.4f},{100*r.fraction:.4f})"
                              for r in rows.itertuples())
            parts += [r"\addplot[color=" + color + ",mark=" + marker +
                      r",mark size=1.8pt] coordinates {" + coords + "};",
                      r"\addlegendentry{True Effect: \$" + str(effect) + "}"]
        parts.append(r"\end{axis}")
    parts += [r"\node[anchor=north,yshift=-.3cm,text width=14cm,align=center,font=\footnotesize] at (current bounding box.south) {20,000 synthetic experiments per scenario; equal 0.05-wide bins.\\Independent Gaussian store means; balanced assignment; pooled $t$ tests.};",
              r"\end{tikzpicture}"]
    (FIGURES / "M03_pvalue_distributions.tex").write_text("\n".join(parts) + "\n")

    row = pd.read_csv(ROOT / "results/campaign_decision.csv").iloc[0]
    lo, hi, mid, threshold = [100 * row[k] for k in
                            ["ci95_low", "ci95_high", "lift", "break_even_lift"]]
    campaign = r'''\begin{tikzpicture}
\begin{axis}[width=13cm,height=5.2cm,xmin=-.025,xmax=.30,ymin=0,ymax=2,
    xtick={0,.05,.10,.15,.20,.25,.30},ytick=\empty,
    xlabel={Incremental Purchase Probability (Percentage Points)},axis y line=none]
\draw[dotted,Storm,thick] (axis cs:0,0) -- (axis cs:0,1.7);
\draw[dashed,IlliniOrange,very thick] (axis cs:THRESHOLD,0) -- (axis cs:THRESHOLD,1.7);
\node[align=center,font=\small] at (axis cs:.25,1.9) {Break-Even Lift};
\addplot[IlliniBlue,very thick,mark=|,mark size=5pt] coordinates {(LOW,1) (HIGH,1)};
\addplot[IlliniBlue,only marks,mark=*,mark size=3pt] coordinates {(MID,1)};
\node[align=center,font=\small] at (axis cs:.10,1.5) {Estimated Lift and 95\% Interval};
\node[align=center,font=\small] at (axis cs:.12,.35) {Estimated Net Contribution: $-\$0.06$\\per Treated Customer};
\end{axis}
\node[anchor=north,yshift=-.4cm,text width=13cm,align=center,font=\footnotesize] at (current bounding box.south) {Hypothetical randomized campaign: one million customers per arm.\\\$40 margin per incremental purchase; \$0.10 contact cost per treated customer.};
\end{tikzpicture}
'''
    for key, value in [("LOW", lo), ("HIGH", hi), ("MID", mid), ("THRESHOLD", threshold)]:
        campaign = campaign.replace(key, f"{value:.8f}")
    (FIGURES / "M06_significance_and_profit.tex").write_text(campaign)

    rows = pd.read_csv(ROOT / "results/equivalence_claims.csv")
    parts = [r'''\begin{tikzpicture}\begin{axis}[width=13.8cm,height=7cm,
        xmin=-9,xmax=12,ymin=.5,ymax=4.5,xtick={-5,0,5,10},ytick={1,2,3,4},
        yticklabels={Faster,Detectable Small,Precise Small,Imprecise},
        xlabel={Mean Additional Task Time (Seconds)},grid=major]
\fill[IlliniBlue,opacity=.06] (axis cs:-5,.5) rectangle (axis cs:5,4.5);
\draw[dashed,IlliniOrange,very thick] (axis cs:-5,.5) -- (axis cs:-5,4.5);
\draw[dashed,IlliniOrange,very thick] (axis cs:5,.5) -- (axis cs:5,4.5);
\draw[dotted,Storm,thick] (axis cs:0,.5) -- (axis cs:0,4.5);''']
    for i, r in enumerate(rows.itertuples()):
        y = 4 - i
        parts.append(r"\addplot[IlliniBlue,very thick,mark=|,mark size=4pt] coordinates {"+
                     f"({r.ci90_low:.8f},{y}) ({r.ci90_high:.8f},{y})"+"};")
        parts.append(r"\addplot[IlliniBlue,only marks,mark=*,mark size=3pt] coordinates {"+
                     f"({r.estimate_seconds},{y})"+"};")
    parts += [r"\end{axis}",
              r"\node[anchor=north,yshift=-.3cm,text width=14cm,align=center,font=\footnotesize] at (current bounding box.south) {Hypothetical independent groups: 50 per arm in the first case, 800 otherwise.\\Points: estimated differences. Bars: 90\% $t$ intervals. Dashed bounds: $\pm5$ seconds.\\Two-sided equivalence requires the full interval inside both bounds.};",
              r"\end{tikzpicture}"]
    (FIGURES / "M09_equivalence_and_burden.tex").write_text("\n".join(parts) + "\n")

    curve = pd.read_csv(ROOT / "results/data_center_power_curve.csv")
    coords = " ".join(f"({r.target_usd_per_mwh:.4f},{100*r.power:.6f})" for r in curve.itertuples())
    parts = [r'''\begin{tikzpicture}
\begin{axis}[width=12.8cm,height=6.4cm,xmin=0,xmax=5,ymin=0,ymax=100,
 xlabel={Specified True Price Increase (\$/MWh)},ylabel={Rejection Probability (\%)},
 xtick={0,1,2,3,4,5},ytick={0,20,40,60,80,100},grid=major]
\draw[dashed,Storm,thick] (axis cs:0,80) -- (axis cs:5,80);
\addplot[IlliniBlue,very thick] coordinates {''' + coords + "};"]
    targets = pd.read_csv(ROOT / "results/data_center_power.csv")
    for r in targets.iloc[:2].itertuples():
        parts.append(r"\addplot[IlliniOrange,only marks,mark=square*,mark size=3pt] coordinates {"+
                     f"({r.target_usd_per_mwh},{100*r.power})"+"};")
        parts.append(r"\node[anchor=south east,font=\small] at (axis cs:"+
                     f"{r.target_usd_per_mwh},{100*r.power+3}"+
                     r") {\$"+str(int(r.target_usd_per_mwh))+f": {100*r.power:.1f}"+r"\%};")
    parts += [r"\end{axis}",
              r"\node[anchor=north,yshift=-.3cm,text width=13cm,align=center,font=\footnotesize] at (current bounding box.south) {Table 2, column 4: reported cluster SE scaled by $100(456/6804)$.\\Two-sided 5\% normal test; fixed SE of \$1.059/MWh.\\80\% power requires about \$2.97/MWh. Power depends on the specified effect.};",
              r"\end{tikzpicture}"]
    (FIGURES / "M06_data_center_power.tex").write_text("\n".join(parts) + "\n")

    (FIGURES / "M09_household_incidence_and_agency.tex").write_text(r'''\begin{tikzpicture}[
 box/.style={draw=IlliniBlue,rounded corners,align=center,text width=4.2cm,minimum height=1.5cm},
 arr/.style={-{Latex[length=2mm]},thick,IlliniBlue}]
\node[box] (aggregate) at (0,0) {Average Revenue Increase\\\$2 per MWh};
\node[box] (uniform) at (7,1.65) {1,000 Households\\Each Pays \$2 More};
\node[box] (concentrated) at (7,-1.65) {100 Households Pay \$20 More\\900 Pay No More};
\draw[arr] (aggregate.east) -- (uniform.west);
\draw[arr] (aggregate.east) -- (concentrated.west);
\node[align=center,text width=11cm,font=\small] at (3.5,-3.5) {Both allocations collect \$2,000 from 1,000 households using 1 MWh each.\\The same average leaves incidence unresolved.};
\node[draw=IlliniOrange,very thick,rounded corners,align=center,text width=11cm,minimum height=1.4cm]
 at (3.5,-5.2) {Who Can Examine the Reasons, Challenge the Allocation,\\and Obtain Review or Remedy?};
\node[align=center,text width=11cm,font=\footnotesize] at (3.5,-6.4) {Synthetic one-month example. Agency requires evidence about authority and process.};
\end{tikzpicture}
''')


if __name__ == "__main__":
    main()
