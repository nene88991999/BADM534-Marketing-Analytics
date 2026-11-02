"""Build Beamer decks and complete Markdown companions from source/sessions.json."""
from pathlib import Path
import argparse
import concurrent.futures
import json
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parent

def esc(s):
    parts = re.split(r'(\$[^$]*\$)', str(s))
    table = {'&': r'\&', '%': r'\%', '#': r'\#', '_': r'\_', '{': r'\{', '}': r'\}', '~': r'\textasciitilde{}'}
    return ''.join(p if p.startswith('$') and p.endswith('$') else ''.join(table.get(c,c) for c in p) for p in parts)

def frame_tex(s):
    kind=s['kind']
    if kind=='art':
        body = '\\begin{frame}[plain]\n\\begin{tikzpicture}[remember picture,overlay]\n\\node[inner sep=0pt] at (current page.center) {\\includegraphics[width=\\paperwidth,height=\\paperheight,keepaspectratio]{assets/'+s['image']+'.png}};\n\\end{tikzpicture}\n'
    else:
        body='\\begin{frame}'+('[fragile]' if kind=='code' else '')+'{'+esc(s['title'])+'}\n\\usebeamercolor[fg]{normal text}\n'
        if kind=='bullets':
            body+='\\vfill\n\\begin{slidebullets}\n'+'\n'.join('\\item '+esc(x) for x in s['bullets'])+'\n\\end{slidebullets}\n\\vfill\n'
        elif kind=='equation':
            body+='\\noindent '+esc(s['intro'])+'\n\\medskip\n\\[\n'+s['equation']+'\n\\]\n\\medskip\n\\noindent '+esc(s['interpretation'])+'\n'
        elif kind=='figure':
            # Fixed-coordinate diagrams retain the note sources' font geometry.
            diagram = r'\begin{axis}' not in (ROOT/s['figure']).read_text()
            body+='\\centering\n\\begingroup\n'
            if diagram:
                body+='\\fontsize{11}{13.2}\\selectfont\n\\def\\small{\\fontsize{10}{12}\\selectfont}\n\\def\\footnotesize{\\fontsize{9}{11}\\selectfont}\n\\def\\scriptsize{\\fontsize{8}{9.5}\\selectfont}\n\\hyphenpenalty=10000\n'
            body+='\\begin{adjustbox}{max width=0.98\\textwidth,max totalheight=0.65\\textheight}\n\\input{'+s['figure']+'}\n\\end{adjustbox}\n\\endgroup\n\\par\\medskip\n{\\small '+esc(s['caption'])+'\\par}\n'
        elif kind=='code':
            body+='\\noindent '+esc(s['intro'])+'\n\\begin{lstlisting}\n'+s['code'].rstrip()+'\n\\end{lstlisting}\n{\\small '+esc(s['check'])+'\\par}\n'
        elif kind=='table':
            align='l'+'r'*(len(s['headers'])-1)
            body+='\\vfill\n\\centering\n{\\small\\begin{tabular}{'+align+'}\n\\toprule\n'+' & '.join(esc(x) for x in s['headers'])+r' \\'+'\n\\midrule\n'
            body+='\n'.join(' & '.join(esc(x) for x in row)+r' \\' for row in s['rows'])+'\n\\bottomrule\n\\end{tabular}}\n\\par\\medskip\n'+esc(s['caption'])+'\n\\vfill\n'
        else: raise ValueError(kind)
    note = esc(s.get('notes',''))
    if s.get('source'):
        source = re.split(r'((?:https?://|\.\./)[^\s]+)', s['source'])
        source = ''.join(r'\url{'+x+'}' if x.startswith(('http','../')) else esc(x) for x in source)
        note += '\n\n'+source
    if note: body+='\\note{'+note+'}\n'
    return body+'\\end{frame}\n'

def companion(session):
    lines=['# '+session['title'],'','By Nathan Yang','',f"Session {session['number']:02d}. {session['module']}. 170 minutes.",'',f"[PDF]({session['stem']}.pdf) | [LaTeX]({session['stem']}.tex) | [Session Plan](SESSION_PLAN.md)",'','## Learning Objectives','']
    lines += ['- '+x for x in session['objectives']]
    lines += ['','## Related Materials','']+['- '+x for x in session['links']]
    lines+=['','## Slide 1: '+session['title'],'','Marketing Analytics. By Nathan Yang.']
    for n,s in enumerate(session['slides'],2):
        lines+=['',f"## Slide {n}: {s['title']}",'']
        k=s['kind']
        if k=='bullets': lines+=['- '+x for x in s['bullets']]
        elif k=='equation': lines += [s['intro'],'','$$',s['equation'],'$$','',s['interpretation']]
        elif k=='figure': lines += [s['caption'],'','**Figure description:** '+s['description'],'',f"[Editable TikZ]({s['figure']})"]
        elif k=='art': lines += [f"![{s['description']}](assets/{s['image']}.png)",'',s['description']]
        elif k=='code': lines += [s['intro'],'','```python',s['code'].rstrip(),'```','',s['check']]
        elif k=='table':
            lines += ['| '+' | '.join(s['headers'])+' |','| '+' | '.join(['---']*len(s['headers']))+' |']
            lines += ['| '+' | '.join(row)+' |' for row in s['rows']]
            lines += ['',s['caption']]
        if s.get('notes'): lines+=['',s['notes']]
        if s.get('source'): lines+=['','Source: '+s['source']]
    lines+=['']
    return '\n'.join(lines)

def write_sources(sessions):
    for s in sessions:
        title='\\title{Marketing Analytics}\n\\subtitle{'+esc(s['title'])+'}\n\\author{By Nathan Yang}\n\\date{Session '+f"{s['number']:02d}"+'}\n'
        tex='\\input{theme.tex}\n'+title+'\\begin{document}\n\\begin{frame}\n\\titlepage\n\\end{frame}\n'+''.join(frame_tex(x) for x in s['slides'])+'\\end{document}\n'
        (ROOT/(s['stem']+'.tex')).write_text(tex)
        (ROOT/(s['stem']+'.md')).write_text(companion(s))

def compile_one(s, engine, presenter=False):
    build=ROOT/'build'/s['stem']; build.mkdir(parents=True,exist_ok=True)
    source=ROOT/(s['stem']+'.tex')
    if presenter:
        wrapper=ROOT/'presenter_tmp.tex'
        wrapper.write_text('\\def\\PresenterVersion{1}\n\\input{'+s['stem']+'.tex}\n')
        source=wrapper
    run=subprocess.run([engine,'--keep-logs','--outdir',str(build),str(source)],cwd=ROOT,text=True,capture_output=True)
    (build/'compile.txt').write_text(run.stdout+'\n'+run.stderr)
    if presenter: source.unlink()
    if run.returncode: raise RuntimeError(f"{s['stem']}: {run.stderr[-1800:]}")
    pdf=build/(source.stem+'.pdf')
    if not presenter: shutil.copyfile(pdf,ROOT/(s['stem']+'.pdf'))
    return s['stem']

def main():
    p=argparse.ArgumentParser();p.add_argument('--tectonic',default=shutil.which('tectonic'));p.add_argument('--only',type=int);p.add_argument('--sources-only',action='store_true');p.add_argument('--presenter',action='store_true');p.add_argument('--jobs',type=int,default=3);a=p.parse_args()
    sessions=json.loads((ROOT/'source/sessions.json').read_text())
    if a.only: sessions=[s for s in sessions if s['number']==a.only]
    write_sources(sessions)
    if a.sources_only:return
    if not a.tectonic:p.error('Provide --tectonic /path/to/tectonic')
    if a.presenter and len(sessions)!=1:p.error('--presenter requires --only SESSION')
    with concurrent.futures.ThreadPoolExecutor(max_workers=a.jobs) as pool:
        for stem in pool.map(lambda s:compile_one(s,str(Path(a.tectonic).resolve()),a.presenter),sessions): print('Built',stem,flush=True)
    if not a.only:
        from pypdf import PdfReader,PdfWriter
        out=PdfWriter()
        for s in sessions:
            r=PdfReader(ROOT/(s['stem']+'.pdf'))
            if len(r.pages)!=len(s['slides'])+1: raise ValueError('Unexpected slide count: '+s['stem'])
            offset=len(out.pages);out.append(r);out.add_outline_item(f"{s['number']:02d}. {s['title']}",offset)
        out.add_metadata({'/Title':'Marketing Analytics: Lectures','/Author':'Nathan Yang'})
        with (ROOT/'Marketing_Analytics_Lectures.pdf').open('wb') as f:out.write(f)
        print('Combined',len(out.pages),'slides',flush=True)

if __name__=='__main__':main()
