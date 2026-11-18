# -*- coding: utf-8 -*-
"""Inserta las lineas #G (figura + epigrafe) al final de cada pregunta que le corresponde.

Los epigrafes de f00..f24 se toman de los <figcaption> de la pagina web;
los de f25..f28 estan escritos aca.
Es idempotente: primero borra las #G que hubiera.
"""
import glob, html, os, re

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PNG = os.path.join(RAIZ, 'figuras', 'png')

# figura -> pregunta
MAPA = {
    'f26': '7.1',  'f27': '7.2',  'f28': '7.3',  'f02': '7.4',  'f03': '7.5',
    'f00': '7.7',  'f01': '7.8',  'f25': '7.9',  'f05': '7.11', 'f06': '7.11',
    'f07': '7.12', 'f08': '8.1',  'f09': '8.3',  'f10': '8.5',
    'f11': '9.2',  'f12': '9.2',  'f13': '9.4',
    'f17': '10.4', 'f14': '10.6', 'f16': '10.6', 'f15': '10.9',
    'f18': '11.4', 'f19': '11.5', 'f20': '11.5', 'f21': '11.7',
    'f22': '12.1', 'f23': '12.2', 'f24': '12.3',
}
# f04 queda afuera: es otro diagrama circular, con los ejes al reves que f25.

PROPIOS = {
    'f25': 'Diagrama circular completo. Todo radio O-P es I1, la cuerda P0-P es I2 referida y el diametro '
           'vale V1/Xcc. Equivalencia con la nomenclatura del apunte: P0 = A (vacio), Pcc = S (arranque), '
           'P-infinito = E, Pn = C (punto de trabajo); la recta de la potencia mecanica es la A-S y la recta '
           'del par es la A-E.',
    'f26': 'Tres bobinas fijas desfasadas 120 grados en el espacio, recorridas por corrientes desfasadas '
           '120 grados en el tiempo, dan una resultante de modulo constante que avanza 120 grados por cada '
           '120 grados de la red: el campo gira a ns = 60 f1 / p.',
    'f27': 'Los dos extremos son los dos ensayos del transformador. Con s = 1 la resistencia ficticia se '
           'anula y la rama rotorica queda en cortocircuito; con s = 0 tiende a infinito y queda abierta.',
    'f28': 'La forma de la ranura decide el arranque. En la jaula, el efecto pelicular sube la resistencia '
           'aparente a 50 Hz y la baja en marcha, cuando f2 = s f1 cae a 1 o 2 Hz; en el rotor bobinado la '
           'resistencia se agrega desde afuera.',
}


def epigrafes_de_la_web():
    h = open(os.path.join(RAIZ, 'parcial-maquinas.html'), encoding='utf-8').read()
    figs = re.findall(r'<figure.*?</figure>', h, re.S)
    out = {}
    for i, f in enumerate(figs):
        m = re.search(r'<figcaption[^>]*>(.*?)</figcaption>', f, re.S)
        if not m:
            continue
        t = html.unescape(re.sub(r'<[^>]+>', '', m.group(1)))
        out['f%02d' % i] = re.sub(r'\s+', ' ', t).strip()
    return out


def main():
    caps = epigrafes_de_la_web()
    caps.update(PROPIOS)

    por_pregunta = {}
    for fig in sorted(MAPA):
        por_pregunta.setdefault(MAPA[fig], []).append(fig)

    usadas = set()
    for ruta in sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'c*.txt'))):
        lineas = [l for l in open(ruta, encoding='utf-8').read().split('\n')
                  if not l.startswith('#G ')]
        salida, actual = [], None

        def cerrar():
            if actual and actual in por_pregunta:
                salida.append('')
                for fig in por_pregunta[actual]:
                    salida.append('#G %s | %s' % (os.path.join(PNG, fig + '.png'), caps[fig]))
                    usadas.add(fig)

        for l in lineas:
            if l.startswith('#Q ') or l.startswith('#U '):
                cerrar()
                actual = l[3:].split('|')[0].strip() if l.startswith('#Q ') else None
            salida.append(l)
        cerrar()
        open(ruta, 'w', encoding='utf-8').write('\n'.join(salida))

    faltan = set(MAPA) - usadas
    print('figuras insertadas: %d' % len(usadas))
    if faltan:
        print('NO UBICADAS (la pregunta no existe): %s' % sorted(faltan))


main()
