"""Write editable Illinois-color TikZ from the saved aggregate tables."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FIGURES = ROOT.parents[1] / '06_Lecture_Notes/figures'


def load(name):
    with (ROOT / 'results' / name).open(newline='') as stream:
        return list(csv.DictReader(stream))


def points(rows, x, y, scale=1):
    return ' '.join(f'({float(r[x])*scale:.8f},{float(r[y]):.8f})' for r in rows)


def main():
    rows = [r for r in load('mixture_comparison.csv') if r['regime'] == 'reference']
    added = [r for r in rows if r['design'] == 'add_clean'
             and float(r['q']) == 1 and int(r['n_b']) > 0]
    unrelated = [r for r in rows if r['design'] == 'add_clean'
                 and float(r['q']) == 0 and int(r['n_b']) > 0]
    left = r'''% Synthetic score contributions; fixed sum loss and penalties a=50, c=1500.
\begin{tikzpicture}
\begin{axis}[at={(0,0)},anchor=south west,width=6.3cm,height=5.5cm,
 xmin=100,xmax=100000,xmode=log,ymin=0,ymax=1,
 xtick={100,1000,10000,100000},xticklabels={100,1k,10k,100k},
 ytick={0,.25,.5,.75,1},xlabel={Clean Examples $n_B$},
 ylabel={Score Contribution},title={Feature Attribution},
 legend style={at={(.5,-.43)},anchor=north,legend columns=1,font=\scriptsize,fill=none,draw=none}]
'''
    for style, values, y, label in [
        ('IlliniOrange,mark=*', added, 'tag_contribution', 'Tag, matched task'),
        ('IlliniBlue,mark=square*,dashed', added, 'task_contribution', 'Task, matched task'),
        ('Storm,mark=triangle*,dotted', unrelated, 'tag_contribution', 'Tag, unrelated task')]:
        left += f'\\addplot[{style}] coordinates {{{points(values,"n_b",y)}}};\n'
        left += f'\\addlegendentry{{{label}}}\n'
    left += r'''\end{axis}
\begin{axis}[at={(7.5cm,0)},anchor=south west,width=6.3cm,height=5.5cm,
 xmin=0,xmax=100,ymin=0,ymax=1,xtick={0,25,50,75,100},ytick={0,.25,.5,.75,1},
 xlabel={Source A Share (\%)},ylabel={Tag Contribution},title={Fixed Total = 30,000},
 legend style={at={(.5,-.43)},anchor=north,legend columns=1,font=\scriptsize,fill=none,draw=none}]
'''
    for q, style in [(1, 'IlliniOrange,mark=*'), (.1, 'IlliniBlue,mark=square*,dashed'),
                     (0, 'Storm,mark=triangle*,dotted')]:
        values = [r for r in rows if r['design'] == 'fixed_total' and float(r['q']) == q]
        left += f'\\addplot[{style}] coordinates {{{points(values,"n_a","tag_contribution",100/30000)}}};\n'
        left += f'\\addlegendentry{{$q={q:g}$}}\n'
    left += '\\end{axis}\n\\end{tikzpicture}\n'
    (FIGURES / 'M07_mixture_attribution.tex').write_text(left)
    rows = load('service_contexts.csv')
    labels = [('all', 'All'), ('product_support', 'Product'),
              ('refund', 'Refund'), ('cancellation', 'Cancellation')]
    chart = r'''% Entirely synthetic paired outcomes; all attempts in denominators.
\begin{tikzpicture}
\begin{axis}[width=13.5cm,height=6.4cm,ybar,bar width=13pt,
 symbolic x coords={All,Product,Refund,Cancellation},xtick=data,
 ymin=0,ymax=108,ytick={0,20,40,60,80,100},ylabel={Correct Resolutions (\%)},
 enlarge x limits=.18,legend style={at={(.5,1.02)},anchor=south,legend columns=2,column sep=6pt,fill=none,draw=none},
 nodes near coords,point meta=y,every node near coord/.append style={font=\footnotesize},
 xlabel={Attempts per Version: 1,000 Total; 900 Product, 80 Refund, 20 Cancellation},
 xlabel style={font=\footnotesize}]
'''
    for version, color, label in [('original', 'IlliniBlue', 'Original'),
                                   ('combined', 'IlliniOrange', 'Combined')]:
        coords = []
        for context, x in labels:
            r = next(r for r in rows if r['version'] == version and r['context'] == context)
            coords.append(f'({x},{100*float(r["rate_per_attempt"]):.8f})')
        chart += f'\\addplot[draw={color},fill={color}] coordinates {{{" ".join(coords)}}};\n'
        chart += f'\\addlegendentry{{{label}}}\n'
    chart += '\\end{axis}\n\\end{tikzpicture}\n'
    (FIGURES / 'M07_conditional_service.tex').write_text(chart)
    print('Wrote two TikZ figures from the saved results.')


if __name__ == '__main__':
    main()
