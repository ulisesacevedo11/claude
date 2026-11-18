# -*- coding: utf-8 -*-
"""Renderiza los archivos de contenido (.txt con marcas) a un .docx."""
import glob, os, re
from PIL import Image
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

INK   = RGBColor(0x11, 0x1A, 0x21)
ACC   = RGBColor(0x0D, 0x5C, 0x8A)
CU    = RGBColor(0xA9, 0x54, 0x1C)
MUT   = RGBColor(0x5B, 0x6A, 0x76)

doc = Document()

# --- estilos base ---
st = doc.styles['Normal']
st.font.name = 'Calibri'; st.font.size = Pt(10.5); st.font.color.rgb = INK
st.paragraph_format.space_after = Pt(5)
st.paragraph_format.line_spacing = 1.12
st.element.rPr.rFonts.set(qn('w:eastAsia'), 'Calibri')

for nm, sz, col, bef, aft in [('Heading 1',20,ACC,20,8),('Heading 2',13.5,INK,14,4),('Heading 3',11.5,CU,10,3)]:
    s = doc.styles[nm]
    s.font.name='Calibri'; s.font.size=Pt(sz); s.font.color.rgb=col; s.font.bold=True
    s.paragraph_format.space_before=Pt(bef); s.paragraph_format.space_after=Pt(aft)
    s.font.italic=False

for sec in doc.sections:
    sec.top_margin=Cm(2.2); sec.bottom_margin=Cm(2.0)
    sec.left_margin=Cm(2.3); sec.right_margin=Cm(2.3)

def shade(cell, hexc):
    el = OxmlElement('w:shd'); el.set(qn('w:val'),'clear'); el.set(qn('w:fill'),hexc)
    cell._tc.get_or_add_tcPr().append(el)

def para(text='', size=10.5, color=INK, bold=False, italic=False, align=None,
         before=0, after=5, mono=False, left=0):
    p = doc.add_paragraph()
    r = p.add_run(text); r.bold=bold; r.italic=italic
    r.font.size=Pt(size); r.font.color.rgb=color
    if mono: r.font.name='Consolas'; r._element.rPr.rFonts.set(qn('w:eastAsia'),'Consolas')
    if align: p.alignment=align
    p.paragraph_format.space_before=Pt(before); p.paragraph_format.space_after=Pt(after)
    if left: p.paragraph_format.left_indent=Cm(left)
    return p

def rich(p, text, size=10.5, base=INK):
    """**negrita** dentro de un parrafo."""
    for i, chunk in enumerate(re.split(r'\*\*(.+?)\*\*', text)):
        if not chunk: continue
        r = p.add_run(chunk); r.bold = (i % 2 == 1)
        r.font.size=Pt(size); r.font.color.rgb=base
    return p

def body(text, left=0, after=5):
    p = doc.add_paragraph()
    p.paragraph_format.space_after=Pt(after)
    if left: p.paragraph_format.left_indent=Cm(left)
    rich(p, text); return p

def bullet(text):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_after=Pt(3)
    p.paragraph_format.left_indent=Cm(0.75); p.paragraph_format.first_line_indent=Cm(-0.35)
    rich(p, text, size=10.5); return p

def formula(text):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent=Cm(0.6)
    p.paragraph_format.space_before=Pt(4); p.paragraph_format.space_after=Pt(6)
    r = p.add_run(text); r.font.name='Consolas'
    r._element.rPr.rFonts.set(qn('w:eastAsia'),'Consolas')
    r.font.size=Pt(10); r.font.color.rgb=ACC; r.bold=True
    return p

def note(text):
    t = doc.add_table(rows=1, cols=1); t.style='Table Grid'; t.alignment=WD_TABLE_ALIGNMENT.LEFT
    c = t.rows[0].cells[0]; shade(c,'FDF3EC')
    c.paragraphs[0].paragraph_format.space_after=Pt(0)
    rich(c.paragraphs[0], text, size=10)
    doc.add_paragraph().paragraph_format.space_after=Pt(2)
    return t

def table(rows):
    t = doc.add_table(rows=len(rows), cols=len(rows[0])); t.style='Table Grid'
    for i,row in enumerate(rows):
        for j,txt in enumerate(row):
            c = t.cell(i,j); c.paragraphs[0].paragraph_format.space_after=Pt(1)
            rich(c.paragraphs[0], txt, size=9)
            if i==0:
                shade(c,'E8EEF2')
                for r in c.paragraphs[0].runs: r.bold=True
    doc.add_paragraph().paragraph_format.space_after=Pt(2)
    return t

def qheader(qid, prio, titulo, examenes, ref):
    h = doc.add_heading(level=2)
    r = h.add_run('%s  %s' % (qid, titulo))
    r.font.size=Pt(13.5); r.font.color.rgb=INK; r.bold=True
    p = doc.add_paragraph(); p.paragraph_format.space_after=Pt(6)
    r = p.add_run(prio + '   '); r.font.size=Pt(10); r.font.color.rgb=CU; r.bold=True
    r = p.add_run(examenes); r.font.size=Pt(8.5); r.font.color.rgb=MUT; r.italic=True
    if ref:
        r = p.add_run('   ·   ' + ref); r.font.size=Pt(8.5); r.font.color.rgb=MUT; r.italic=True

def enunciado(text):
    t = doc.add_table(rows=1, cols=1); t.style='Table Grid'
    c = t.rows[0].cells[0]; shade(c,'EDF2F5')
    c.paragraphs[0].paragraph_format.space_after=Pt(0)
    r = c.paragraphs[0].add_run('Enunciado tipo. '); r.bold=True; r.font.size=Pt(9.5); r.font.color.rgb=ACC
    rich(c.paragraphs[0], text, size=9.5)
    doc.add_paragraph().paragraph_format.space_after=Pt(2)

FIGN = [0]

def figura(path, caption):
    """Inserta una imagen centrada con su epigrafe numerado."""
    if not os.path.exists(path):
        raise SystemExit('FALTA LA FIGURA: ' + path)
    iw, ih = Image.open(path).size
    ratio = float(ih) / iw
    ancho = 15.8 if ratio < 0.58 else (14.8 if ratio < 1.0 else 11.0)
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(8); p.paragraph_format.space_after = Pt(2)
    p.add_run().add_picture(path, width=Cm(ancho))
    FIGN[0] += 1
    c = doc.add_paragraph(); c.alignment = WD_ALIGN_PARAGRAPH.CENTER
    c.paragraph_format.space_after = Pt(10)
    r = c.add_run('Figura %d.  ' % FIGN[0]); r.bold=True; r.font.size=Pt(8.5); r.font.color.rgb=ACC
    r = c.add_run(caption); r.italic=True; r.font.size=Pt(8.5); r.font.color.rgb=MUT
    return p

# ---------- parser ----------
def render(path):
    buf_tbl = []
    for raw in open(path, encoding='utf-8').read().split('\n'):
        line = raw.rstrip()
        if buf_tbl and not line.startswith(('#TH','#TR')):
            table(buf_tbl); buf_tbl = []
        if not line.strip():
            continue
        if   line.startswith('#U '):  doc.add_page_break(); doc.add_heading(line[3:], level=1)
        elif line.startswith('#Q '):  qheader(*[x.strip() for x in line[3:].split('|')])
        elif line.startswith('#E '):  enunciado(line[3:])
        elif line.startswith('#H '):  doc.add_heading(line[3:], level=3)
        elif line.startswith('#F '):  formula(line[3:])
        elif line.startswith('#L '):  bullet(line[3:])
        elif line.startswith('#N '):  note(line[3:])
        elif line.startswith('#G '):
            ruta, cap = [x.strip() for x in line[3:].split('|', 1)]
            figura(ruta, cap)
        elif line.startswith('#TH '): buf_tbl.append([x.strip() for x in line[4:].split('|')])
        elif line.startswith('#TR '): buf_tbl.append([x.strip() for x in line[4:].split('|')])
        else: body(line)
    if buf_tbl: table(buf_tbl)
