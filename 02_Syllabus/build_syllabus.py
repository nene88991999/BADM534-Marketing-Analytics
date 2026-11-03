"""Render the Markdown syllabus to a two-page Illinois-color PDF.

Requires reportlab. Run from any folder with Python; no network access is used.
Markdown remains the source of prose and tables. Relative PDF links point to GitHub.
"""
from pathlib import Path
from html import escape
import re
import posixpath
import reportlab
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                               TableStyle, PageBreak)

HERE = Path(__file__).resolve().parent
BLUE = colors.HexColor('#13294B')
ORANGE = colors.HexColor('#FF5F05')
GRAY = colors.HexColor('#707372')
REPO = 'https://github.com/nene88991999/BADM534-Marketing-Analytics/blob/main/'


def inline(text):
    text = escape(text)
    def link(match):
        label, target = match.groups()
        if not target.startswith(('http:', 'https:', 'mailto:')):
            target = REPO + posixpath.normpath(posixpath.join('02_Syllabus', target))
        return f'<a href="{target}" color="#13294B"><u>{label}</u></a>'
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', link, text)
    return re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)


def main():
    fonts = Path(reportlab.__file__).parent / 'fonts'
    pdfmetrics.registerFont(TTFont('CourseSans', str(fonts / 'Vera.ttf')))
    pdfmetrics.registerFont(TTFont('CourseSans-Bold', str(fonts / 'VeraBd.ttf')))
    pdfmetrics.registerFontFamily('CourseSans', normal='CourseSans', bold='CourseSans-Bold')
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle('CourseTitle', fontName='CourseSans-Bold', fontSize=23,
                              leading=27, textColor=BLUE, spaceAfter=9))
    styles.add(ParagraphStyle('SectionTitle', fontName='CourseSans-Bold', fontSize=12,
                              leading=15, textColor=BLUE, spaceBefore=9, spaceAfter=5,
                              keepWithNext=True))
    styles.add(ParagraphStyle('Prose', fontName='CourseSans', fontSize=10,
                              leading=12.5, textColor=BLUE, spaceAfter=6))
    styles.add(ParagraphStyle('Point', parent=styles['Prose'], leftIndent=10,
                              firstLineIndent=-8, spaceAfter=3))
    styles.add(ParagraphStyle('Cell', parent=styles['Prose'], fontSize=9.3,
                              leading=12, spaceAfter=0))
    def para(text, style='Prose'):
        return Paragraph(inline(text), styles[style])
    lines=(HERE/'Marketing_Analytics_Syllabus.md').read_text().splitlines()
    story=[];i=0
    while i<len(lines):
        line=lines[i].strip()
        if not line:i+=1;continue
        if line=='---':story.append(PageBreak());i+=1;continue
        if line.startswith('# '):story.append(para(line[2:], 'CourseTitle'));i+=1;continue
        if line.startswith('## '):story.append(para(line[3:], 'SectionTitle'));i+=1;continue
        if line.startswith('- '):story.append(para('• '+line[2:], 'Point'));i+=1;continue
        if line.startswith('|'):
            rows=[]
            while i<len(lines) and lines[i].startswith('|'):
                cells=[c.strip() for c in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r':?-+:?',c) for c in cells):rows.append(cells)
                i+=1
            widths=[118,394] if len(rows[0])==2 else [60,78,374]
            table=Table([[para(c,'Cell') for c in row] for row in rows],colWidths=widths,
                        hAlign='LEFT',repeatRows=1)
            commands=[('BACKGROUND',(0,0),(-1,0),colors.HexColor('#EEF1F5')),
                      ('LINEBELOW',(0,0),(-1,0),1,ORANGE),
                      ('VALIGN',(0,0),(-1,-1),'TOP'),
                      ('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),
                      ('TOPPADDING',(0,0),(-1,-1),3 if len(rows[0])==2 else 5),('BOTTOMPADDING',(0,0),(-1,-1),3 if len(rows[0])==2 else 5),
                      ('LINEBELOW',(0,-1),(-1,-1),.35,GRAY)]
            for n,row in enumerate(rows):
                if row[0]=='No Class':commands.append(('BACKGROUND',(0,n),(-1,n),colors.HexColor('#FFF0E7')))
            table.setStyle(TableStyle(commands));story.extend([table,Spacer(1,4)]);continue
        paragraph=[line];i+=1
        while i<len(lines) and lines[i].strip() and not lines[i].startswith(('#','|','- ')):
            paragraph.append(lines[i].strip());i+=1
        story.append(para(' '.join(paragraph)))
    def decorate(canvas,doc):
        canvas.saveState();canvas.setStrokeColor(ORANGE);canvas.setLineWidth(2)
        canvas.line(50,755,562,755)
        canvas.setFont('CourseSans',8);canvas.setFillColor(GRAY)
        canvas.drawString(50,28,'Marketing Analytics | Spring 2027')
        canvas.drawRightString(562,28,str(doc.page));canvas.restoreState()
    pdf=HERE/'Marketing_Analytics_Syllabus.pdf'
    doc=SimpleDocTemplate(str(pdf),pagesize=letter,rightMargin=50,leftMargin=50,
                          topMargin=48,bottomMargin=43,title='Marketing Analytics: Spring 2027 Syllabus',
                          author='Nathan Yang')
    doc.build(story,onFirstPage=decorate,onLaterPages=decorate)
    print(pdf)


if __name__=='__main__':
    main()
