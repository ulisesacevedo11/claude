# -*- coding: utf-8 -*-
import sys, glob, re
sys.path.insert(0,'.')
import render as R
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

doc, para, note, table = R.doc, R.para, R.note, R.table
INK, ACC, CU, MUT = R.INK, R.ACC, R.CU, R.MUT
FILES = sorted(glob.glob('c*.txt'))

# ---------------- portada ----------------
para(after=60)
para('BANCO DE PREGUNTAS', 11, CU, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, after=4)
para('2.º Parcial de Máquinas', 34, ACC, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, after=2)
para('Unidades VII a XII', 20, INK, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, after=18)
para('Máquinas e Instalaciones Eléctricas · UTN FRH', 11, MUT, align=WD_ALIGN_PARAGRAPH.CENTER, after=4)
para('Todas las preguntas posibles del segundo cuatrimestre, resueltas,', 11, MUT, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, after=0)
para('con diagramas y ordenadas por probabilidad de que las tomen.', 11, MUT, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, after=70)

# recuento automatico
qs = []
for f in FILES:
    for line in open(f, encoding='utf-8'):
        if line.startswith('#Q '):
            qid, prio, tit, exa, ref = [x.strip() for x in line[3:].split('|')]
            qs.append((qid, prio, tit, exa, ref))
tot = len(qs)
n3 = sum(1 for q in qs if q[1]=='★★★'); n2 = sum(1 for q in qs if q[1]=='★★')
n1 = sum(1 for q in qs if q[1]=='★');   n0 = sum(1 for q in qs if q[1]=='○')

nfig = sum(1 for f in FILES for l in open(f, encoding='utf-8') if l.startswith('#G '))
t = doc.add_table(rows=1, cols=5); t.style='Table Grid'
for i,(num,lab) in enumerate([(str(tot),'preguntas'),(str(nfig),'diagramas'),(str(n3+n2+n1),'ya tomadas'),(str(n0),'todavía no'),('6','unidades')]):
    c = t.cell(0,i); R.shade(c,'EDF2F5')
    p1 = c.paragraphs[0]; p1.alignment=WD_ALIGN_PARAGRAPH.CENTER; p1.paragraph_format.space_after=Pt(0)
    r = p1.add_run(num); r.bold=True; r.font.size=Pt(22); r.font.color.rgb=ACC
    p2 = c.add_paragraph(); p2.alignment=WD_ALIGN_PARAGRAPH.CENTER; p2.paragraph_format.space_after=Pt(2)
    r = p2.add_run(lab); r.font.size=Pt(8.5); r.font.color.rgb=MUT
doc.add_page_break()

# ---------------- como usarlo ----------------
doc.add_heading('Cómo usar este documento', level=1)
R.body('Cada pregunta trae el **enunciado tipo** —redactado como lo redacta la cátedra—, la **respuesta desarrollada**, en qué exámenes apareció y la página del **Apunte del 2.º Cuatrimestre** donde está el tema.')
R.body('Las preguntas que se contestan con un dibujo traen la **figura ya hecha**, numerada y con epígrafe. Son las que conviene reproducir en la hoja del parcial: varias consignas piden explícitamente «esquematice», «grafique» o «dibuje».')
R.body('Las preguntas están **ordenadas por unidad**, no por prioridad. La prioridad la da la marca de estrellas, y el mapa de la página siguiente las ordena de más a menos probable.')
doc.add_heading('Las marcas de prioridad', level=3)
table([['Marca','Significado','Qué hacer'],
       ['★★★','Tomada **3 o más veces**','Saberla de memoria. Es casi seguro que vuelve.'],
       ['★★','Tomada **2 veces**','Saberla bien.'],
       ['★','Tomada **1 vez**','Leerla y entenderla.'],
       ['○','**Nunca tomada**','Está en el programa. Leerla al menos una vez: el parcial del 12-11-25 incorporó Calidad de Energía, que tampoco tenía antecedente.']])
doc.add_heading('De dónde sale', level=3)
for s in ['**Apunte del 2.º Cuatrimestre (V5)**, 68 páginas, Unidades VII a XII — es la fuente principal y la referencia de páginas.',
          '**Siete modelos de parcial y recuperatorio** (12-11-25, 10-12-25, 11-12-24, 13-12-23, 06-03-24, 13-12-22 y 07-12-22), más las preguntas de los parciales **13-11-24** y **25-11-20** y de los "modelos p2" citadas en el documento de respuestas de la carpeta.',
          'Material de cátedra de cada unidad: presentación de **Motor Paso a Paso**, presentación de **Máquina Sincrónica** y apuntes de **Motor Sincrónico** del Ing. José Luis González, presentaciones de **Máquina de CC**, **Brushless y servomotores** y **Calidad de la energía**.',
          'El **problema resuelto de motores asíncronos** de la carpeta Unidad VII / Problemas, del que sale el ejercicio N.2.']:
    R.bullet(s)
doc.add_heading('Lo que este documento NO cubre', level=3)
note('**Transformadores.** Son Unidad 5, del primer cuatrimestre, y por eso quedan fuera del alcance de este banco. Pero **hay una pregunta de transformadores en los siete modelos, sin excepción**, casi siempre como pregunta 1 y con un cálculo numérico de rendimiento. Preparalos aparte.')
note('**Las figuras.** Las respuestas remiten a la página del apunte donde está cada esquema: circuito equivalente, diagrama circular, esquemas de mando y potencia, curvas de cupla, diagrama de Blondel y curvas en V. Para los esquemas eléctricos conviene dibujarlos a mano mientras se estudia, que es como hay que resolverlos en el parcial.')

# ---------------- mapa de prioridades ----------------
doc.add_page_break()
doc.add_heading('Mapa de prioridades', level=1)
R.body('Las mismas preguntas, ordenadas de más a menos probable. Si tenés poco tiempo, estudiá de arriba hacia abajo.')
orden = {'★★★':0, '★★':1, '★':2, '○':3}
rows = [['','Pregunta','Apareció en']]
for qid, prio, tit, exa, ref in sorted(qs, key=lambda q: (orden[q[1]], q[0])):
    rows.append([prio, '**%s**  %s' % (qid, tit), exa if prio != '○' else '—'])
tmap = table(rows)
from docx.shared import Cm as _Cm
def fijar_anchos(t, cms):
    t.autofit = False
    tblPr = t._tbl.tblPr
    lay = OxmlElement('w:tblLayout'); lay.set(qn('w:type'), 'fixed'); tblPr.append(lay)
    grid = t._tbl.find(qn('w:tblGrid'))
    if grid is not None:
        for gc, cm in zip(grid.findall(qn('w:gridCol')), cms):
            gc.set(qn('w:w'), str(int(cm * 567)))
    for row in t.rows:
        for cell, cm in zip(row.cells, cms):
            cell.width = _Cm(cm)
fijar_anchos(tmap, [1.6, 8.4, 6.4])

# ---------------- contenido ----------------
for f in FILES:
    R.render(f)

# ---------------- cierre ----------------
doc.add_page_break()
doc.add_heading('Antes de entrar al parcial', level=1)
R.body('Los **cinco temas que más se repiten**, por si querés hacer un último repaso:')
for s in ['**Jaula profunda** y, pegado, resbalamiento con s = 1 y s = 0 (7.4 y 7.2). Salió tres veces.',
          '**Motor monofásico**: doble campo giratorio, arranques e inversión de giro (8.1, 8.2, 8.5). Salió cuatro veces.',
          '**Máquina de CC**: partes, reacción de armadura y rotor bloqueado (10.1, 10.4, 10.6). Salió cuatro veces entre sus dos variantes.',
          '**Circuito equivalente y potencias**, con el término R\'2(1−s)/s (7.7 y 7.8).',
          '**Factor de forma, factor de cresta y corriente de neutro** (12.1 y 12.2).']:
    R.bullet(s)
R.body('')
note('**Tres cosas que se cobran caro en la corrección.** Primero: **par y potencia no son lo mismo** — con el rotor bloqueado hay par máximo y potencia nula. Segundo: en la inversión del monofásico se permutan los terminales **de un solo** devanado, no de los dos ni de la línea. Tercero: en los métodos de arranque, la corriente baja con **k** pero el par baja con **k²**, así que siempre se pierde más par del que se gana en corriente.')
R.body('')
para('Armado a partir del material de la carpeta «Máquinas e Instalaciones Eléctricas», Unidades VII a XII. Los resultados numéricos de la sección de ejercicios están verificados; las referencias de página corresponden al Apunte del 2.º Cuatrimestre V5.', 8.5, MUT, italic=True)

out = '/home/user/claude/2do Parcial Maquinas - Todo Resuelto con Diagramas.docx'
doc.save(out)
print('guardado:', out)
print('figuras:', nfig)
print('preguntas:', tot, '| ★★★:', n3, '★★:', n2, '★:', n1, '○:', n0)
