"""Write editable Illinois-color TikZ from the checked geographic results."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent
FIGURES = ROOT.parents[1] / '06_Lecture_Notes/figures'


def save(name, text):
    (FIGURES / (name + '.tex')).write_text(text + '\n')


def main():
    save('M02_digital_measurement', r'''\begin{tikzpicture}[x=1cm,y=1cm]
\node[box,text width=3.5cm] (a) at (0,0) {Consenting consumer\\Windows devices};
\node[box,text width=3.5cm] (b) at (5.2,0) {Application minutes\\and category weights};
\node[box,text width=3.5cm] (c) at (10.4,0) {Private aggregation\\and geographic indices};
\draw[edge] (a) -- (b); \draw[edge] (b) -- (c);
\node[orangebox,text width=5.5cm] (need) at (8.1,-2.6) {Customer service decision\\Offer digital and assisted channels};
\draw[accent] (c.south) -- node[right,align=left,font=\footnotesize] {Area-level\\context} (need.north east);
\node[box,text width=4.2cm] (test) at (0.2,-2.6) {Observe requested channel,\\task completion, time, and cost};
\draw[edge] (test) -- node[above,font=\footnotesize] {Task evidence} (need);
\node[align=center,text width=13cm,font=\footnotesize] at (5.2,-4.1) {Application categories aggregate different tasks. An area's usage score does not identify\\an individual customer's ability, preferences, or authorization.};
\end{tikzpicture}''')
    data = pd.read_csv(ROOT / 'results/illinois_map.csv')
    pieces = [r'\begin{tikzpicture}']
    for i, name in enumerate(['mci', 'cci']):
        pieces.append(r'\begin{axis}[at={(' + str(i * 6.5) + r'cm,0)},anchor=south west,width=6.4cm,height=8cm,'
            r'xmin=-91.6,xmax=-87.3,ymin=36.8,ymax=42.6,xlabel={Longitude},ylabel={Latitude},'
            r'title={' + name.upper() + r': Within-Illinois Score},grid=major,clip=true,'
            r'xtick={-91,-89,-87},ytick={37,39,41},title style={font=\small}]')
        masks = [data[name+'_z'] < -1, data[name+'_z'].between(-1,1), data[name+'_z'] > 1]
        for mask, color, marker in zip(masks, ['IlliniBlue','Storm','IlliniOrange'], ['o','+','triangle*']):
            coords = ' '.join(f'({r.longitude:.5f},{r.latitude:.5f})' for r in data[mask].itertuples())
            pieces.append(r'\addplot[only marks,mark=' + marker + r',mark size=1pt,color=' + color + '] coordinates {' + coords + '};')
        pieces.append(r'\end{axis}')
    pieces.extend([r'\node[anchor=north,align=center,font=\footnotesize] at (6.3,-1.6) {Blue circles: $z<-1$; gray crosses: $-1\leq z\leq1$; orange triangles: $z>1$.\\'
        r'1,253 released Illinois areas; equal area weights; Census internal points.\\Each index uses its own Illinois mean and population standard deviation.};',r'\end{tikzpicture}'])
    save('M02_digital_geography', '\n'.join(pieces))
    estimates = pd.read_csv(ROOT / 'results/regressions.csv')
    parts = [r'\begin{tikzpicture}\begin{axis}[width=11.5cm,height=7cm,scaled x ticks=false,xtick={-.02,0,.02,.04,.06},xticklabel style={/pgf/number format/fixed,/pgf/number format/precision=2},xmin=-.03,xmax=.065,ymin=.5,ymax=3.5,'
        r'xlabel={Index units per \$10,000 of median household income},ytick={1,2,3},'
        r'yticklabels={State + controls,Education + broadband,Income alone},'
        r'grid=major,legend style={at={(.98,.57)},anchor=north east},clip=true]']
    for name, color, mark, offset in [('mci','IlliniBlue','*',.09),('cci','IlliniOrange','square*',-.09)]:
        values = estimates.loc[estimates['index'].eq(name)]
        coordinates = ' '.join(f'({r.income_slope_per_10000_dollars:.7f},{3-j+offset})' for j,r in enumerate(values.itertuples()))
        parts.append(r'\addplot[only marks,mark=' + mark + ',mark size=3pt,color='+color+'] coordinates {'+coordinates+'};')
        parts.append(r'\addlegendentry{'+name.upper()+'}')
    parts += [r'\draw[dashed,Storm] (axis cs:0,.5) -- (axis cs:0,3.5);',r'\end{axis}',
        r'\node[anchor=north,yshift=-.3cm,align=center,text width=13cm,font=\footnotesize] at (current bounding box.south) {28,511 common areas; equal ZIP weights; 2017--2021 ACS.\\50 open-ended income codes excluded; descriptive coefficients.};',r'\end{tikzpicture}']
    save('M03_digital_controls','\n'.join(parts))
    data = pd.read_csv(ROOT / 'results/illinois_clusters.csv')
    summary = pd.read_csv(ROOT / 'results/cluster_summary.csv')
    parts = [r'\begin{tikzpicture}\begin{axis}[width=12cm,height=7cm,xlabel={MCI (index units)},'
             r'ylabel={CCI (index units)},grid=major,clip=true,'
             r'legend style={at={(1.02,.98)},anchor=north west},xmin=0,xmax=4.6,ymin=0,ymax=4.8]']
    for group, color, mark in [(1,'IlliniBlue','o'),(2,'Storm','+'),(3,'IlliniOrange','triangle*')]:
        coords=' '.join(f'({r.mci:.5f},{r.cci:.5f})' for r in data[data.cluster.eq(group)].itertuples())
        n=int(summary.loc[summary.cluster.eq(group),'areas'].iloc[0])
        parts += [r'\addplot[only marks,mark='+mark+',mark size=1.2pt,color='+color+'] coordinates {'+coords+'};',
                  r'\addlegendentry{Group '+str(group)+': '+str(n)+' areas}']
    parts += [r'\end{axis}',r'\node[anchor=north,yshift=-.3cm,align=center,text width=13cm,font=\footnotesize] at (current bounding box.south) {1,253 Illinois areas; $k=3$ on standardized scores, shown in original units.\\Raw versus standardized partitions: adjusted Rand index $0.805$.};',r'\end{tikzpicture}']
    save('M04_digital_clusters','\n'.join(parts))


if __name__ == '__main__':
    main()
