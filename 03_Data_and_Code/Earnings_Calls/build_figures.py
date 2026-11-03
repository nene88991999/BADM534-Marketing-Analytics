"""Generate editable Illinois-color figures from the executed aggregate tables."""
from pathlib import Path
import json
import pandas as pd

HERE = Path(__file__).resolve().parent
FIGURES = HERE.parents[1] / '06_Lecture_Notes/figures'


def main():
    a = json.loads((HERE / 'results/assessment.json').read_text())
    text = r'''\begin{tikzpicture}
\begin{axis}[xbar,width=12cm,height=5.3cm,xmin=0,xmax=29,ymin=-.6,ymax=1.6,
 xlabel={Calls With a Core Match (Percent)},ytick={0,1},
 yticklabels={All Observed Calls,Calls With Any Match},xtick={0,5,10,15,20,25},xmajorgrids=true]
\addplot[fill=IlliniBlue,draw=IlliniBlue,bar width=15pt,bar shift=0pt] coordinates {(RATE,0)};
\addplot[fill=IlliniOrange,draw=IlliniOrange,bar width=15pt,bar shift=0pt] coordinates {(WRONG,1)};
\node[anchor=west] at (axis cs:5.2,0) {112 / 2,325};
\node[anchor=west] at (axis cs:12,1.42) {112 / 445};
\end{axis}\end{tikzpicture}
'''.replace('RATE', f'{100*a["observed_call_rate"]:.6f}').replace('WRONG', f'{100*a["wrong_positive_only_rate"]:.6f}')
    (FIGURES / 'M02_calls_denominator.tex').write_text(text)
    rates = pd.read_csv(HERE / 'results/role_rates.csv')
    r = rates[rates['sample'].eq('all_observed')].set_index('role')
    def panel(x, title, maximum, values, ticks):
        return r'''\begin{axis}[at={(Xcm,0)},anchor=south west,width=6.2cm,height=5.3cm,
 ybar,bar shift=0pt,bar width=19pt,xmin=-.6,xmax=1.6,ymin=0,ymax=MAX,
 xtick={0,1},xticklabels={Management,Analysts},ytick={TICKS},
 ylabel={TITLE},ymajorgrids=true,nodes near coords,
 tick label style={font=\fontsize{9}{11}\selectfont},
 label style={font=\fontsize{10}{12}\selectfont},
 yticklabel style={/pgf/number format/fixed,/pgf/number format/precision=3},
 every node near coord/.append style={font=\fontsize{10}{12}\selectfont},
 point meta=explicit symbolic]
\addplot[fill=IlliniBlue,draw=IlliniBlue] coordinates {(0,VM) [LM]};
\addplot[fill=IlliniOrange,draw=IlliniOrange] coordinates {(1,VA) [LA]};
\end{axis}
'''.replace('Xcm',str(x)+'cm').replace('MAX',str(maximum)).replace('TICKS',ticks).replace('TITLE',title).replace('VM',str(values[0])).replace('VA',str(values[1])).replace('LM',str(values[2])).replace('LA',str(values[3]))
    text = '\\begin{tikzpicture}\n' + panel(0,'Core Matches',150,[127,23,127,23],'0,50,100,150')
    vals = [r.loc[x, 'per_10000_words'] for x in ['management','analyst']]
    text += panel(7,'Matches per 10,000 Words',.105,[*vals,'0.076','0.083'],'0,.025,.05,.075,.1')
    text += '\\end{tikzpicture}\n'
    assert r.loc['management','core_matches'] == 127 and r.loc['analyst','core_matches'] == 23
    (FIGURES / 'M05_calls_exposure.tex').write_text(text)
    e = pd.read_csv(HERE / 'results/event_windows.csv')
    e = e[e.window_days.eq(90) & e['sample'].eq('firms_in_both_windows') & e.group.eq('comparison')].set_index('period')
    assert (e.calls == 27).all() and (e.positive_calls == 2).all()
    text = r'''\begin{tikzpicture}[node distance=1cm]
\node[box,text width=4.5cm] (before) at (0,0) {Before Clarification\\27 Calls From 27 Firms\\5 Core Matches\\2 Positive Calls};
\node[orangebox,text width=4.5cm] (after) at (7,0) {After Clarification\\Same 27 Firms, 27 Calls\\2 Core Matches\\2 Positive Calls};
\draw[edge] (before) -- node[above,align=center]{90-Day\\Windows} (after);
\node[box,text width=4.5cm] (left) at (0,-2.7) {2 / 27 = 7.41\%};
\node[orangebox,text width=4.5cm] (right) at (7,-2.7) {2 / 27 = 7.41\%};
\draw[edge] (before) -- (left);
\draw[accent] (after) -- (right);
\node[align=center,text width=12cm] at (3.5,-4) {Repeated mentions fall while the share of calls mentioning the topic stays constant.};
\end{tikzpicture}
'''
    (FIGURES / 'M06_calls_windows.tex').write_text(text)


if __name__ == '__main__':
    main()
