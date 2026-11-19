# -*- coding: utf-8 -*-
"""Curvas de arranque estrella-triangulo: corriente y par contra velocidad.

Motor de ejemplo: 380/660 V en red de 380 V, jaula normal.
  par     -> formula de Kloss con s_Ck = 0,20  =>  M_max = 2,6 Mn y M_arr = 1,0 Mn
  corr.   -> I(s) = V / raiz((R1 + R2/s)^2 + Xcc^2), con R1 0,6  R2 0,5  Xcc 3,2
  carga   -> bomba centrifuga, par resistente cuadratico
"""
import math, os

OUT = os.path.dirname(os.path.abspath(__file__))
INK, ACC, CU, GR, MUT = '#111a21', '#0d5c8a', '#a9541c', '#0f7a52', '#64748b'
W, H = 830, 700
CONM = 0.85                      # velocidad de conmutacion Y -> triangulo

SCK, MMAX = 0.20, 2.6
V, R1, R2, XCC = 219.4, 0.6, 0.5, 3.2
I0 = 0.35                        # corriente de vacio, en por unidad de la de carga nominal


def _i2(n):
    """componente de carga, normalizada a su valor nominal (s = 0,04)"""
    s = max(1e-4, 1.0 - n)
    ref = V / math.sqrt((R1 + R2/0.04)**2 + XCC**2)
    return (V / math.sqrt((R1 + R2/s)**2 + XCC**2)) / ref


def _bruta(n):
    return math.sqrt(I0**2 + _i2(n)**2)


_REF = _bruta(0.96)


def par(n):
    s = max(1e-4, 1.0 - n)
    return 2*MMAX / (s/SCK + SCK/s)


def corriente(n):
    """I1 = I0 + I'2, suma vectorial: por eso no se anula en sincronismo."""
    return _bruta(n) / _REF


def carga(n):
    return 0.10 + 0.90*n*n


def txt(x, y, t, size=12, fill=INK, bold=False, anchor='start', italic=False):
    return ('<text x="%g" y="%g" font-size="%g" fill="%s" text-anchor="%s"%s%s>%s</text>'
            % (x, y, size, fill, anchor, ' font-weight="700"' if bold else '',
               ' font-style="italic"' if italic else '', t))


class Plot(object):
    def __init__(self, x0, x1, ytop, ybot, ymax, titulo, unidad):
        self.x0, self.x1, self.yt, self.yb, self.ymax = x0, x1, ytop, ybot, ymax
        self.s = []
        self.s.append(txt((x0+x1)/2.0, ytop-16, titulo, 13, INK, True, 'middle'))
        # ejes
        self.s.append('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="1.5"/>'
                      % (x0, ytop-6, x0, ybot, INK))
        self.s.append('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="1.5"/>'
                      % (x0, ybot, x1+14, ybot, INK))
        self.s.append(txt(x0-8, ytop-12, unidad, 11, MUT, True, 'end'))
        # grilla horizontal
        paso = 1 if ymax <= 3.2 else 2
        v = paso
        while v <= ymax:
            y = self.py(v)
            self.s.append('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="#dde4e9" stroke-width="1"/>'
                          % (x0, y, x1, y))
            self.s.append(txt(x0-7, y+4, str(v), 10, MUT, False, 'end'))
            v += paso
        # eje de velocidad
        for frac in (0, 0.25, 0.5, 0.75, 1.0):
            x = self.px(frac)
            self.s.append('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="1.2"/>'
                          % (x, ybot, x, ybot+5, MUT))
            self.s.append(txt(x, ybot+19, '%g' % frac, 10, MUT, False, 'middle'))

    def px(self, n):
        return self.x0 + (self.x1 - self.x0)*n

    def py(self, v):
        return self.yb - (self.yb - self.yt)*min(v, self.ymax)/self.ymax

    def curva(self, f, col, ancho=2.6, dash=None, desde=0.0, hasta=1.0, escala=1.0):
        pts = []
        k = 0
        while k <= 200:
            n = desde + (hasta-desde)*k/200.0
            pts.append('%s%g %g' % ('M' if k == 0 else 'L', self.px(n), self.py(f(n)*escala)))
            k += 1
        self.s.append('<path d="%s" stroke="%s" stroke-width="%g" fill="none"%s stroke-linecap="round"/>'
                      % (' '.join(pts), col, ancho, ' stroke-dasharray="7 4"' if dash else ''))

    def vertical(self, n, col, rotulo=None):
        x = self.px(n)
        self.s.append('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="1.6" '
                      'stroke-dasharray="5 4"/>' % (x, self.yt-6, x, self.yb, col))
        if rotulo:
            self.s.append(txt(x, self.yt-12, rotulo, 10.5, col, True, 'middle'))

    def salto(self, n, v1, v2, col, rotulo):
        x = self.px(n)
        self.s.append('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="3" '
                      'marker-end="url(#fl)"/>' % (x, self.py(v1), x, self.py(v2)+6, col))
        self.s.append(txt(x-10, (self.py(v1)+self.py(v2))/2.0 + 4, rotulo, 10.5, col, True, 'end'))

    def punto(self, n, v, col):
        self.s.append('<circle cx="%g" cy="%g" r="5" fill="%s"/>' % (self.px(n), self.py(v), col))

    def dump(self):
        return ''.join(self.s)


s = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" '
     'font-family="system-ui,Segoe UI,Helvetica,Arial,sans-serif">'
     '<rect width="%d" height="%d" fill="#ffffff"/>' % (W, H, W, H, W, H),
     '<defs><marker id="fl" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="9" '
     'refX="10" refY="4.5" orient="auto"><polygon points="0,0 11,4.5 0,9" fill="%s"/></marker></defs>' % CU]

s.append(txt(W/2.0, 30, 'Arranque estrella-triángulo: corriente y par contra velocidad', 16, INK, True, 'middle'))

# ---------------- corriente ----------------
p1 = Plot(95, 690, 82, 272, 6, 'Corriente de línea', 'I / Iₙ')
p1.curva(corriente, CU, 2.8)
p1.curva(corriente, ACC, 2.8, escala=1/3.0, hasta=CONM)
p1.vertical(CONM, MUT, 'conmutación Y → Δ')
p1.salto(CONM, corriente(CONM)/3.0, corriente(CONM), CU, 'pico de conmutación')
p1.punto(0, corriente(0), CU)
p1.punto(0, corriente(0)/3.0, ACC)
s.append(p1.dump())
s.append(txt(p1.px(0.06), p1.py(corriente(0))-10, 'directo:  %.1f Iₙ' % corriente(0), 11.5, CU, True))
s.append(txt(p1.px(0.06), p1.py(corriente(0)/3.0)-10, 'en estrella:  %.1f Iₙ' % (corriente(0)/3.0), 11.5, ACC, True))

# ---------------- par ----------------
p2 = Plot(95, 690, 392, 582, 3, 'Par', 'M / Mₙ')
p2.curva(carga, GR, 2.4, dash=True)
p2.curva(par, CU, 2.8)
p2.curva(par, ACC, 2.8, escala=1/3.0, hasta=CONM)
p2.vertical(CONM, MUT)
p2.salto(CONM, par(CONM)/3.0, par(CONM), CU, 'el par vuelve al valor pleno')
p2.punto(0, par(0), CU)
p2.punto(0, par(0)/3.0, ACC)
s.append(p2.dump())
s.append(txt(p2.px(0.05), p2.py(par(0))+17, 'directo:  %.1f Mₙ de arranque' % par(0), 11.5, CU, True))
s.append(txt(p2.px(0.20), p2.py(par(0.20)/3.0)-14, 'en estrella:  %.2f Mₙ' % (par(0)/3.0), 11.5, ACC, True))
s.append(txt(p2.px(0.52), p2.py(carga(0.52))+20, 'par resistente de la carga', 11, GR, True, 'middle'))
s.append(txt(p2.px(0.30), p2.py(2.35), 'Mₘáx = %.1f Mₙ' % MMAX, 11, CU, True, 'middle'))

# leyenda y notas
s.append('<line x1="110" y1="634" x2="146" y2="634" stroke="%s" stroke-width="3"/>' % CU)
s.append(txt(152, 638, 'arranque directo (conexión triángulo)', 11, MUT))
s.append('<line x1="400" y1="634" x2="436" y2="634" stroke="%s" stroke-width="3"/>' % ACC)
s.append(txt(442, 638, 'arranque en estrella: todo a 1/3', 11, MUT))
s.append(txt(95, 668, 'En estrella cada bobinado recibe V/√3, así que la corriente de línea y el par caen los dos a 1/3. '
             'La conmutación debe hacerse antes de que', 11, MUT))
s.append(txt(95, 686, 'la curva azul corte a la de la carga: si no, el motor se cala. Velocidad de paso típica: 80 a 85 % de la sincrónica.', 11, MUT))
s.append(txt(p1.x1+50, p1.yb+5, 'n / nₛ', 11, MUT, True))
s.append(txt(p2.x1+50, p2.yb+5, 'n / nₛ', 11, MUT, True))
s.append('</svg>')

open(os.path.join(OUT, 'n4-estrella-triangulo.svg'), 'w', encoding='utf-8').write(''.join(s))
print('I arranque directo = %.2f In   en estrella = %.2f In' % (corriente(0), corriente(0)/3.0))
print('M arranque directo = %.2f Mn   en estrella = %.2f Mn' % (par(0), par(0)/3.0))
print('en la conmutacion (n = %.2f ns): I_Y = %.2f In  ->  I_D = %.2f In'
      % (CONM, corriente(CONM)/3.0, corriente(CONM)))
print('par en estrella al conmutar = %.2f Mn   carga = %.2f Mn' % (par(CONM)/3.0, carga(CONM)))
