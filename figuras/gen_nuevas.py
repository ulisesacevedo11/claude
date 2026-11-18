# -*- coding: utf-8 -*-
"""Genera las tres figuras que faltaban para las preguntas 7.1, 7.2 y 7.3."""
import math, os

OUT = os.path.dirname(os.path.abspath(__file__))
INK, ACC, CU, GR, MUT = '#111a21', '#0d5c8a', '#a9541c', '#0f7a52', '#64748b'
FNT = 'system-ui,Segoe UI,Helvetica,Arial,sans-serif'

def head(w, h):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" '
            'font-family="%s"><rect width="%d" height="%d" fill="#ffffff"/>' % (w, h, w, h, FNT, w, h))

def txt(x, y, s, size=12, fill=INK, bold=False, anchor='start', italic=False):
    return ('<text x="%g" y="%g" font-size="%g" fill="%s" text-anchor="%s"%s%s>%s</text>'
            % (x, y, size, fill, anchor,
               ' font-weight="700"' if bold else '',
               ' font-style="italic"' if italic else '', s))

ARROW = ('<defs>'
         '<marker id="a" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="9" refX="10" refY="4.5" orient="auto">'
         '<polygon points="0,0 11,4.5 0,9" fill="%s"/></marker>'
         '<marker id="ac" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="9" refX="10" refY="4.5" orient="auto">'
         '<polygon points="0,0 11,4.5 0,9" fill="%s"/></marker></defs>' % (CU, ACC))


# ---------------------------------------------------------------- A: campo giratorio
def campo_giratorio():
    W, H = 780, 452
    s = [head(W, H), ARROW]
    s.append(txt(W/2, 26, 'Campo giratorio: tres bobinas fijas, un campo que gira', 15, INK, True, 'middle'))

    # tres cortes del estator
    fases = [('U', 90, ACC), ('V', 210, GR), ('W', 330, CU)]
    for k, (inst, ang) in enumerate([(0, 90), (120, 210), (240, 330)]):
        cx, cy, r = 150 + k*245, 135, 70
        s.append('<circle cx="%g" cy="%g" r="%g" fill="#f4f7f9" stroke="%s" stroke-width="2"/>' % (cx, cy, r, MUT))
        s.append('<circle cx="%g" cy="%g" r="%g" fill="#ffffff" stroke="%s" stroke-width="1.2"/>' % (cx, cy, r*0.46, MUT))
        # polos de cada fase
        for nm, a, col in fases:
            ax, ay = cx + (r-9)*math.cos(math.radians(a)), cy - (r-9)*math.sin(math.radians(a))
            s.append('<circle cx="%g" cy="%g" r="9" fill="%s" opacity="0.22"/>' % (ax, ay, col))
            s.append(txt(ax, ay+4, nm, 11, col, True, 'middle'))
        # vector campo resultante
        bx, by = cx + (r*0.58)*math.cos(math.radians(ang)), cy - (r*0.80)*math.sin(math.radians(ang))
        s.append('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="2.8" marker-end="url(#a)"/>'
                 % (cx, cy, bx, by, CU))
        s.append(txt(cx, cy+r+22, 'ωt = %d°' % inst, 12, INK, True, 'middle'))
        s.append(txt(cx, cy+r+38, 'B hacia %s' % fases[k][0], 11, MUT, False, 'middle'))

    # el campo avanza 120 grados entre instante e instante
    for xa, xb in ((238, 307), (483, 552)):
        s.append('<line x1="%g" y1="140" x2="%g" y2="140" stroke="%s" stroke-width="2" '
                 'marker-end="url(#a)" stroke-dasharray="5 4"/>' % (xa, xb, CU))
        s.append(txt((xa+xb)/2.0, 130, '+120\u00b0', 11, CU, True, 'middle'))

    # senoides
    x0, x1, yb, amp = 95, 690, 318, 42
    s.append('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="1.4"/>' % (x0-20, yb, x1+18, yb, INK))
    for nm, ph, col in [('i_U', 0, ACC), ('i_V', 120, GR), ('i_W', 240, CU)]:
        pts = []
        for i in range(0, 241):
            deg = i*1.5
            x = x0 + (x1-x0)*deg/360.0
            y = yb - amp*math.cos(math.radians(deg - ph))
            pts.append('%s%g %g' % ('M' if i == 0 else 'L', x, y))
        s.append('<path d="%s" stroke="%s" stroke-width="2.4" fill="none"/>' % (' '.join(pts), col))
        xp = x0 + (x1-x0)*ph/360.0
        s.append(txt(xp + (6 if ph == 0 else 0), yb - amp - 10, nm, 11, col, True,
                     'start' if ph == 0 else 'middle'))
    for deg, lab in [(0, 'ωt=0°'), (120, '120°'), (240, '240°')]:
        x = x0 + (x1-x0)*deg/360.0
        s.append('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="1.2" stroke-dasharray="4 4"/>'
                 % (x, yb-amp-14, x, yb+amp+10, MUT))
        s.append(txt(x, yb+amp+26, lab, 10.5, MUT, False, 'middle'))

    s.append(txt(x0-20, 414, 'Tres corrientes desfasadas 120° en el tiempo, en tres bobinas desfasadas 120° en el espacio:', 11.5, MUT))
    s.append(txt(x0-20, 432, 'la resultante tiene módulo constante y gira a la velocidad sincrónica ns = 60·f1/p.', 11.5, MUT))
    s.append('</svg>')
    open(os.path.join(OUT, 'n1-campo-giratorio.svg'), 'w', encoding='utf-8').write(''.join(s))


# ---------------------------------------------------------------- B: s = 1 / s = 0
def extremos_s():
    W, H = 800, 352
    s = [head(W, H), ARROW]
    s.append(txt(W/2, 26, 'Los dos extremos del resbalamiento en la rama rotórica', 15, INK, True, 'middle'))

    def zig(x, y, w, col, lab, sub=''):
        """resistencia"""
        n, dx = 6, w/6.0
        p = ['M%g %g' % (x, y)]
        for i in range(n):
            p.append('L%g %g' % (x + dx*(i+0.5), y + (-9 if i % 2 == 0 else 9)))
        p.append('L%g %g' % (x + w, y))
        out = ['<path d="%s" stroke="%s" stroke-width="2.4" fill="none"/>' % (' '.join(p), col),
               txt(x + w/2, y - 16, lab, 11.5, col, True, 'middle')]
        if sub:
            out.append(txt(x + w/2, y + 26, sub, 10, MUT, False, 'middle'))
        return ''.join(out)

    def coil(x, y, w, col, lab):
        n, dx = 4, w/4.0
        p = ['M%g %g' % (x, y)]
        for i in range(n):
            p.append('A %g %g 0 0 1 %g %g' % (dx/2, dx/2, x + dx*(i+1), y))
        return ('<path d="%s" stroke="%s" stroke-width="2.4" fill="none"/>' % (' '.join(p), col)
                + txt(x + w/2, y - 14, lab, 11.5, col, True, 'middle'))

    for k, (tit, sub, estado, col) in enumerate([
            ('s = 1 · rotor bloqueado', 'R′₂(1−s)/s = 0', 'corto', CU),
            ('s = 0 · sincronismo', 'R′₂(1−s)/s → ∞', 'abierto', ACC)]):
        ox, y = 25 + k*390, 150
        s.append('<rect x="%g" y="60" width="350" height="240" rx="10" fill="#fbfcfd" stroke="%s" stroke-width="1.4"/>'
                 % (ox, MUT))
        s.append(txt(ox + 175, 86, tit, 13, col, True, 'middle'))
        # linea superior
        s.append('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="2"/>' % (ox+22, y, ox+60, y, INK))
        s.append(zig(ox+60, y, 60, INK, "R′₂"))
        s.append('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="2"/>' % (ox+120, y, ox+140, y, INK))
        s.append(coil(ox+140, y, 60, INK, "X′₂"))
        s.append('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="2"/>' % (ox+200, y, ox+228, y, INK))
        if estado == 'corto':
            s.append('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="4.5"/>' % (ox+228, y, ox+300, y, col))
            s.append(txt(ox+264, y-16, 'EN CORTO', 11, col, True, 'middle'))
        else:
            s.append('<circle cx="%g" cy="%g" r="4.5" fill="none" stroke="%s" stroke-width="2.4"/>' % (ox+232, y, col))
            s.append('<circle cx="%g" cy="%g" r="4.5" fill="none" stroke="%s" stroke-width="2.4"/>' % (ox+296, y, col))
            s.append(txt(ox+264, y-16, 'ABIERTO', 11, col, True, 'middle'))
        s.append(txt(ox+264, y+26, sub, 10.5, MUT, False, 'middle'))
        # retorno
        s.append('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="2"/>' % (ox+300, y, ox+322, y, INK))
        s.append('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="2"/>' % (ox+322, y, ox+322, y+52, INK))
        s.append('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="2"/>' % (ox+322, y+52, ox+22, y+52, INK))
        s.append('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="2"/>' % (ox+22, y+52, ox+22, y, INK))
        s.append(txt(ox+6, y+30, "E′₂", 12, INK, True, 'middle'))
        # conclusiones
        if estado == 'corto':
            filas = ['f₂ = f₁ = 50 Hz  ·  E₂ máxima',
                     'I₂ máxima (4 a 7 Iₙ)  ·  cos φ₂ ≈ 0,2',
                     'Pₘ = 0  ·  todo se va en P_Cu2',
                     '→ TRANSFORMADOR EN CORTOCIRCUITO']
        else:
            filas = ['f₂ = 0  ·  E₂ = 0',
                     "I′₂ = 0  ·  sólo circula I₀",
                     'par nulo  ·  Pₘ = 0',
                     '→ TRANSFORMADOR EN VACÍO']
        for i, f in enumerate(filas):
            s.append(txt(ox + 175, 236 + i*16, f, 10.5, col if i == 3 else MUT, i == 3, 'middle'))
    s.append(txt(40, 332, 'R′₂ no depende de s; E₂ y X₂ sí. De esa asimetría sale todo el comportamiento de la máquina.', 11.5, MUT))
    s.append('</svg>')
    open(os.path.join(OUT, 'n2-extremos-s.svg'), 'w', encoding='utf-8').write(''.join(s))


# ---------------------------------------------------------------- C: tipos de rotor
def tipos_rotor():
    W, H = 780, 390
    s = [head(W, H), ARROW]
    s.append(txt(W/2, 26, 'Tipos de rotor: la forma de la ranura decide el arranque', 15, INK, True, 'middle'))

    paneles = [
        ('Jaula normal', 'barra redonda', ['sin efecto pelicular', 'R₂ fija y baja', 'M_arr 0,8–1,2 Mₙ', 'I_arr 4–7 Iₙ']),
        ('Ranura profunda', 'barra alta y angosta', ['efecto pelicular fuerte', 'R₂ alta en el arranque', 'M_arr 1,2–1,5 Mₙ', 'I_arr 4–4,8 Iₙ']),
        ('Doble jaula', 'externa + interna', ['externa: R alta, X baja', 'interna: R baja, X alta', 'M_arr 1–2 Mₙ', 'I_arr 3,3–5,5 Iₙ']),
    ]
    for k, (tit, sub, filas) in enumerate(paneles):
        ox = 26 + k*192
        s.append('<rect x="%g" y="48" width="176" height="300" rx="9" fill="#fbfcfd" stroke="%s" stroke-width="1.3"/>' % (ox, MUT))
        s.append(txt(ox+88, 70, tit, 12.5, INK, True, 'middle'))
        s.append(txt(ox+88, 85, sub, 10, MUT, False, 'middle'))
        # entrehierro
        s.append('<line x1="%g" y1="100" x2="%g" y2="100" stroke="%s" stroke-width="2.2"/>' % (ox+22, ox+154, ACC))
        s.append(txt(ox+88, 96, 'entrehierro', 9, ACC, False, 'middle'))
        # hierro
        s.append('<rect x="%g" y="104" width="132" height="110" fill="#e9eef2" stroke="%s" stroke-width="1.2"/>' % (ox+22, MUT))
        cxx = ox + 88
        if k == 0:
            s.append('<circle cx="%g" cy="150" r="21" fill="%s" opacity="0.85"/>' % (cxx, CU))
            s.append(txt(cxx, 196, 'sección uniforme', 9.5, MUT, False, 'middle'))
        elif k == 1:
            s.append('<rect x="%g" y="112" width="22" height="94" rx="7" fill="%s" opacity="0.85"/>' % (cxx-11, CU))
            s.append('<rect x="%g" y="112" width="22" height="28" rx="7" fill="%s"/>' % (cxx-11, '#d98b50'))
            s.append('<line x1="%g" y1="126" x2="%g" y2="126" stroke="%s" stroke-width="1.8" marker-end="url(#a)"/>' % (cxx+44, cxx+15, CU))
            s.append(txt(cxx+42, 146, 'I en el', 8.5, CU, True, 'middle'))
            s.append(txt(cxx+42, 158, 'arranque', 8.5, CU, True, 'middle'))
        else:
            s.append('<rect x="%g" y="112" width="26" height="24" rx="6" fill="%s"/>' % (cxx-13, '#d98b50'))
            s.append('<rect x="%g" y="148" width="42" height="56" rx="9" fill="%s" opacity="0.85"/>' % (cxx-21, CU))
            s.append('<line x1="%g" y1="136" x2="%g" y2="148" stroke="%s" stroke-width="1.6" stroke-dasharray="3 3"/>' % (cxx, cxx, MUT))
            s.append(txt(cxx+42, 124, 'externa', 9, CU, True, 'middle'))
            s.append(txt(cxx+42, 180, 'interna', 9, CU, True, 'middle'))
        for i, f in enumerate(filas):
            s.append(txt(ox+16, 240 + i*19, '· ' + f, 10, MUT))

    # panel rotor bobinado
    ox = 602
    s.append('<rect x="%g" y="48" width="152" height="300" rx="9" fill="#f4f9f6" stroke="%s" stroke-width="1.6"/>' % (ox, GR))
    s.append(txt(ox+76, 70, 'Rotor bobinado', 12.5, GR, True, 'middle'))
    s.append(txt(ox+76, 85, 'de anillos rozantes', 10, MUT, False, 'middle'))
    s.append('<circle cx="%g" cy="150" r="40" fill="#ffffff" stroke="%s" stroke-width="1.8"/>' % (ox+56, MUT))
    for a in (90, 210, 330):
        ax, ay = ox+56 + 26*math.cos(math.radians(a)), 150 - 26*math.sin(math.radians(a))
        s.append('<circle cx="%g" cy="%g" r="9" fill="%s" opacity="0.3"/>' % (ax, ay, GR))
    for i, yy in enumerate((132, 150, 168)):
        s.append('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="1.6"/>' % (ox+96, yy, ox+114, yy, INK))
        s.append('<circle cx="%g" cy="%g" r="3.4" fill="%s"/>' % (ox+96, yy, INK))
    s.append('<path d="M %g 126 L %g 174 L %g 174 L %g 126 Z" fill="none" stroke="%s" stroke-width="1.8"/>'
             % (ox+114, ox+114, ox+132, ox+132, GR))
    s.append(txt(ox+76, 206, 'anillos + reóstato', 9.5, MUT, False, 'middle'))
    for i, f in enumerate(['R₂ **ajustable** desde afuera',
                           'corre s_Ck hacia s = 1',
                           'M_máx no cambia de valor',
                           'par máximo en el arranque',
                           'escobillas: mantenimiento']):
        s.append(txt(ox+14, 240 + i*19, '· ' + f.replace('**', ''), 10, MUT))
    s.append(txt(26, 372, 'En la jaula R₂ la fija el fabricante y el efecto pelicular la hace variar sola con la frecuencia f₂ = s·f₁; '
                 'en el rotor bobinado la elige el usuario.', 11.5, MUT))
    s.append('</svg>')
    open(os.path.join(OUT, 'n3-tipos-rotor.svg'), 'w', encoding='utf-8').write(''.join(s))


campo_giratorio()
extremos_s()
tipos_rotor()
print('generadas')
