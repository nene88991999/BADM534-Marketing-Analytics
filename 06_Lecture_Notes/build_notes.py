#!/usr/bin/env python3
"""Build the lecture PDF from Markdown and TikZ; optionally refresh figure PNGs.

Requires Pandoc, Tectonic, and TeX packages (downloaded by Tectonic as needed).
--figures additionally requires Poppler's pdftoppm and Pillow.
No downloaded course-resource code is executed.
"""
import argparse
import json
import re
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def run(args):
    subprocess.run([str(a) for a in args], cwd=ROOT, check=True)

def heading_targets(source, pandoc):
    """Match GitHub heading links to the labels supplied by figure_filter.lua."""
    document = json.loads(subprocess.check_output(
        [pandoc, str(source), '--from=markdown+tex_math_dollars', '--to=json'],
        cwd=ROOT, text=True))
    targets = {}

    def inline_text(node):
        if isinstance(node, list):
            return ''.join(inline_text(child) for child in node)
        if not isinstance(node, dict):
            return ''
        if node.get('t') == 'Str':
            return node['c']
        if node.get('t') in ('Space', 'SoftBreak', 'LineBreak'):
            return ' '
        if node.get('t') in ('Code', 'Math'):
            return node['c'][-1]
        return inline_text(node.get('c', []))

    def visit(node):
        if isinstance(node, list):
            for child in node:
                visit(child)
        elif isinstance(node, dict):
            if node.get('t') == 'Header':
                _, attributes, content = node['c']
                anchor = re.sub(r'[^\w\s-]', '', inline_text(content)).lower().replace(' ', '-')
                targets[f'modules/{source.name}#{anchor}'] = (
                    source.stem.split('_')[0] + '-' + attributes[0])
            visit(node.get('c', []))

    visit(document['blocks'])
    return targets

def glossary_latex(pandoc, targets, standalone=False):
    source = re.sub(r'(?m)^(#{1,2} .+)$', r'\1 {.unnumbered}',
        (ROOT/'Glossary.md').read_text())
    fragment = subprocess.check_output([pandoc,
        '--from=markdown+tex_math_dollars', '--to=latex',
        '--top-level-division=chapter', '--no-highlight',
        '--lua-filter='+str(ROOT/'figure_filter.lua')], cwd=ROOT, input=source, text=True)

    def link(match):
        target, label = match.groups()
        target = target.replace(r'\#', '#')
        destination = targets[target]
        if standalone and not destination.startswith('M09-'):
            return r'\href{Marketing_Analytics_Lecture_Notes.pdf\#' + destination + '}{' + label + '}'
        return r'\hyperref[' + destination + ']{' + label + '}'

    fragment = re.sub(r'\\href\{(modules/[^}]+)\}\{([^{}]+)\}', link, fragment)
    fragment = re.sub(r'\\noindent\s*\n+', lambda m: r'\noindent ', fragment)
    fragment = re.sub(r'(?:\\noindent\s*)?\\hypertarget\{module-([a-z])\}',
        lambda m: '\\par\\Needspace{10\\baselineskip}\n\\hypertarget{module-' + m[1] + '}', fragment)
    fragment = re.sub(r'(?m)^(?:\\noindent )?\\textbf\{',
        lambda m: '\\Needspace{4\\baselineskip}\n\\noindent\\textbf{', fragment)
    return '\\clearpage\n\\begingroup\n\\setlength{\\parindent}{0pt}\n' + fragment + '\n\\endgroup\n'

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--pandoc', default='pandoc')
    ap.add_argument('--tectonic', default='tectonic')
    ap.add_argument('--pdftoppm', default='pdftoppm')
    ap.add_argument('--figures', action='store_true')
    ap.add_argument('--figure-name', action='append', help='Render only this figure name with --figures; repeat for multiple figures')
    args=ap.parse_args()
    if args.figure_name and not args.figures:
        ap.error('--figure-name requires --figures')
    modules=sorted((ROOT/'modules').glob('M*.md'))
    if [p.stem.split('_')[0] for p in modules] != [f'M{i:02d}' for i in range(1,10)]:
        raise ValueError('Expected M01–M09, including Marketing Dialectics')
    build=ROOT/'build'
    build.mkdir(exist_ok=True)
    preface_source=build/'Preface.md'
    preface_source.write_text((ROOT/'Preface.md').read_text().replace(
        '# Preface\n', '# Preface {.unnumbered}\n', 1))
    preface=subprocess.check_output([args.pandoc,str(preface_source),
        '--from=markdown+tex_math_dollars','--to=latex','--top-level-division=chapter',
        '--no-highlight','--id-prefix=frontmatter-',
        '--lua-filter='+str(ROOT/'figure_filter.lua')],cwd=ROOT,text=True)
    preface=re.sub(r'\\noindent\s*\n+', lambda m: r'\noindent ', preface)
    names=[]
    fragments=[]
    targets={}
    for module in modules:
        targets.update(heading_targets(module, args.pandoc))
        names += re.findall(r'\.\./figures/(M\d+_[a-z_]+)\.png',module.read_text())
        fragments.append(subprocess.check_output([args.pandoc,str(module),
            '--from=markdown+tex_math_dollars','--to=latex','--top-level-division=chapter',
            '--no-highlight','--id-prefix='+module.stem.split('_')[0]+'-','--lua-filter='+str(ROOT/'figure_filter.lua')],cwd=ROOT,text=True))
    for name in names:
        if not (ROOT/'figures'/f'{name}.tex').is_file():
            raise FileNotFoundError(name)
    intro=r'''% Generated by build_notes.py from Preface.md, Glossary.md, and modules/*.md.
\input{preamble.tex}
\begin{document}
\hypersetup{pageanchor=false}
\begin{titlepage}
\color{IlliniBlue}
\vspace*{1.2cm}
{\Huge\bfseries Marketing Analytics\par}
\vspace{.8cm}
{\LARGE Lecture Notes\par}
\vspace{.5cm}
{\large Marketing Decisions and AI-Assisted Coding\par}
\vspace{1.1cm}
\noindent{\color{IlliniOrange}\rule{\textwidth}{2pt}}\par
\vspace{.7cm}
{\large By Nathan Yang\par}
{\large November 27, 2026\par}
\end{titlepage}
\pagenumbering{roman}
\hypersetup{pageanchor=true}
\renewcommand{\contentsname}{Table of Contents}
\pdfbookmark[0]{Table of Contents}{table-of-contents}
\tableofcontents
\clearpage
'''+preface+r'''
\clearpage
\pagenumbering{arabic}
'''
    master=ROOT/'Marketing_Analytics_Lecture_Notes.tex'
    fragments = [re.sub(r'\\noindent\s*\n+', lambda m: r'\noindent ', fragment) for fragment in fragments]
    fragments = [fragment.replace('Python source:',
        '\\FloatBarrier\n\\Needspace{8\\baselineskip}\nPython source:') for fragment in fragments]
    # Keep short teaching tables intact; let complete Python programs span pages.
    fragments = [fragment.replace(r'\begin{longtable}[]',
        '\\begin{table}[H]\n\\centering\\small\n\\begin{tabular}')
        .replace(r'\endhead', '')
        .replace(r'\end{longtable}', '\\end{tabular}\n\\end{table}')
        .replace(r'\begin{verbatim}', '\\begin{Verbatim}[breaklines,breakanywhere,fontsize=\\small]')
        .replace(r'\end{verbatim}', '\\end{Verbatim}')
        for fragment in fragments]
    master.write_text(intro+'\n'.join(fragments)+glossary_latex(args.pandoc, targets)+'\n\\end{document}\n')
    run([args.tectonic,'--keep-logs','--outdir',build,master])
    shutil.copy2(build/'Marketing_Analytics_Lecture_Notes.pdf',ROOT/'Marketing_Analytics_Lecture_Notes.pdf')
    chapter = fragments[-1].replace(r'\label{M09-marketing-dialectics}}',
        '\\label{M09-marketing-dialectics}}\n\\noindent{\\large By Nathan Yang}\\par\\medskip', 1)
    standalone = ROOT/'Marketing_Dialectics.tex'
    standalone_intro = r'''\input{preamble.tex}
\begin{document}
\hypersetup{pdftitle={Marketing Dialectics},pageanchor=false}
\begin{titlepage}
\color{IlliniBlue}
\vspace*{1.2cm}
{\Huge\bfseries Marketing Analytics\par}
\vspace{.8cm}
{\LARGE Marketing Dialectics\par}
\vspace{1.1cm}
\noindent{\color{IlliniOrange}\rule{\textwidth}{2pt}}\par
\vspace{.7cm}
{\large By Nathan Yang\par}
{\large November 27, 2026\par}
\end{titlepage}
\pagenumbering{roman}
\hypersetup{pageanchor=true}
\renewcommand{\contentsname}{Table of Contents}
\pdfbookmark[0]{Table of Contents}{table-of-contents}
\begingroup
\setlength{\parskip}{2pt}
\tableofcontents
\endgroup
\clearpage
\pagenumbering{arabic}
\setcounter{chapter}{8}
'''
    standalone.write_text(standalone_intro + chapter +
        glossary_latex(args.pandoc, targets, standalone=True) + '\n\\end{document}\n')
    run([args.tectonic,'--keep-logs','--outdir',build,standalone])
    shutil.copy2(build/'Marketing_Dialectics.pdf',ROOT/'Marketing_Dialectics.pdf')
    if args.figures:
        render_names = args.figure_name or names
        missing = set(render_names) - set(names)
        if missing:
            raise ValueError('Figures absent from modules: ' + ', '.join(sorted(missing)))
        from PIL import Image, ImageChops
        atlas=ROOT/'figure_atlas.tex'
        atlas.write_text('\\input{preamble.tex}\n\\begin{document}\n\\pagestyle{empty}\n'+
            '\n'.join('\\noindent\\input{figures/'+n+'.tex}\\clearpage' for n in render_names)+
            '\n\\end{document}\n')
        try:
            run([args.tectonic,'--keep-logs','--outdir',build,atlas])
            for page in build.glob('atlas-*.png'):
                page.unlink()
            run([args.pdftoppm,'-r','150','-png',build/'figure_atlas.pdf',build/'atlas'])
            pages=sorted(build.glob('atlas-*.png'))
            if len(pages)!=len(render_names):
                raise ValueError(f'Expected {len(render_names)} figure pages; got {len(pages)}')
            for name,page in zip(render_names,pages):
                im=Image.open(page).convert('RGB')
                bbox=ImageChops.difference(im,Image.new('RGB',im.size,'white')).getbbox()
                if not bbox: raise ValueError(f'Empty figure: {name}')
                l,t,r,b=bbox
                im.crop((max(0,l-25),max(0,t-25),min(im.width,r+25),min(im.height,b+25))).save(ROOT/'figures'/f'{name}.png')
        finally:
            atlas.unlink(missing_ok=True)
    print(f'Built {len(modules)} modules and {len(names)} figures: {ROOT / "Marketing_Analytics_Lecture_Notes.pdf"}')

if __name__=='__main__':
    main()
