# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '/root/.claude/skills/synced/27eb8805-2d9b-4f7d-ae7e-2347c7285d46_b1d2deb2-ac11-42db-8149-17a1fe837101/docx-revision-anotada/scripts')
from annotate import Doc, block

d = Doc('unpacked/word/document.xml')
print('fuente:', d.body_font, '| jc:', d.jc)

# ───────────────────────── 0 · OBSERVACIÓN: el listado que falta y las marcas ⚠ vencidas
p = d.find_para('ver el listado al final')
d.check_anchor(p)
d.after(p, block(d, 'OBSERVACIÓN', 0, [
  ('b', 'El listado de ⚠ que anuncia este párrafo no existe: el documento termina en E.12.'),
  ('p', 'Y hay algo más de fondo: las seis marcas ⚠ del cuerpo están desactualizadas. '
        'Los seis temas señalados como «no está en el apunte» sí están en el Apunte del '
        '2.º Cuatrimestre V5, y con bastante desarrollo:'),
  ('p', '1.8 Arranque en vacío contra plena carga → apunte p. 17, punto 12.8, con el gráfico '
        'cualitativo de las dos corrientes.'),
  ('p', '2.1 Qué pasa si queda conectado el bobinado de arranque → p. 25, «Falla del '
        'interruptor centrífugo», con los dos modos de falla.'),
  ('p', '3.1 Devanados de compensación → p. 39, al pie de la sección de reacción de armadura.'),
  ('p', '3.2 Rotor bloqueado → p. 41, dentro de las ecuaciones del motor.'),
  ('p', '3.3 Posición de las escobillas en carga → p. 40, con el esquema de generador y motor.'),
  ('p', '4.2 Bancos de capacitores → p. 64, con la resonancia y los filtros desintonizados.'),
  ('p', 'No se tocó la introducción porque hay dos caminos posibles y la elección es del autor: '
        'armar el listado prometido, o quitar las seis marcas y la referencia. Si se opta por lo '
        'segundo hay que editar seis puntos del cuerpo además de este párrafo.'),
]))

# ───────────────────────── 1 · MODIFICACIÓN: el título con la «x»
p = d.find_para('x1.1 Principio', occurrence=1)
d.check_anchor(p)
d.after(p, block(d, 'MODIFICACIÓN', 1, [
  ('p', '1.1 Principio de funcionamiento, resbalamiento, curva cupla-resbalamiento y tipos de rotor'),
]))

# ───────────────────────── 2 · MODIFICACIÓN: la tabla de secuencias de armónicos
t = d.find_tbl('Positiva (directa)')
d.after(t, block(d, 'MODIFICACIÓN', 2, [
  ('b', 'Columna «Armónicos» de la tabla, corregida:'),
  ('p', 'Positiva (directa): 1, 7, 13, 19…   ·   Negativa (inversa): 5, 11, 17, 23…   ·   '
        'Homopolar (cero): 3, 9, 15, 21…'),
  ('p', 'Y agregar a continuación de la tabla: «Los órdenes de arriba son los impares, que son '
        'los que realmente aparecen. La regla general es que el armónico de orden h es de '
        'secuencia directa si h = 3k+1, inversa si h = 3k+2 y homopolar si h = 3k, lo que '
        'incluiría también a los pares; pero en una red simétrica los armónicos pares no '
        'existen, porque la simetría de media onda los anula. Su presencia indica una asimetría '
        'o una componente de continua —rectificación de media onda, conducción desigual de un '
        'semiconductor— que satura los núcleos de transformadores y motores.»'),
]))

# ───────────────────────── 3 · OBSERVACIÓN: el bloque duplicado de E.10
p = d.find_para('par neto promedio igual a cero')
d.check_anchor(p)
d.after(p, block(d, 'OBSERVACIÓN', 3, [
  ('b', 'Las dos secciones anteriores están duplicadas con el resto de la respuesta E.10.'),
  ('p', '«Principio de Funcionamiento como Motor» y «El Problema del Arranque en el Motor '
        'Sincrónico» repiten contenido que la respuesta ya da en otro lado, con otras palabras:'),
  ('p', 'El párrafo de apertura de E.10 ya dice que con el rotor parado los polos reciben '
        'atracciones y repulsiones alternadas muy rápidas y que por eso no tiene par de arranque. '
        'Es lo mismo que dice después «Par de arranque nulo».'),
  ('p', 'La sección «Ángulo de carga», en la página siguiente, ya explica que el rotor se atrasa '
        'un ángulo δ que crece con la carga, que el par es máximo en δ = 90° y que superarlo hace '
        'perder el sincronismo. Es lo mismo que dice «Ángulo de Carga (δ)» en el bloque de arriba.'),
  ('p', 'Se nota además que es material pegado de otra fuente, porque cambia el estilo: estos dos '
        'títulos van en Mayúsculas Iniciales y el resto del documento usa minúscula.'),
  ('p', 'No se eliminó nada, porque la regla de esta revisión es no borrar texto del original. '
        'Para aplicarlo: borrar desde «Principio de Funcionamiento como Motor» hasta «…par neto '
        'promedio igual a cero.» inclusive. El resto de E.10 —intro, métodos de arranque, ángulo '
        'de carga y devanado amortiguador— queda completo y sin huecos.'),
]))

# ───────────────────────── 4 · OBSERVACIÓN: PCu1 con I'2
p = d.find_para('Pérdidas en el cobre del estator', occurrence=0)
d.check_anchor(p)
d.after(p, block(d, 'OBSERVACIÓN', 4, [
  ('b', 'PCu1 = m1 · I′2² · R1 vale sólo dentro del circuito aproximado.'),
  ('p', 'En el circuito aproximado la rama de magnetización se pasa a los bornes de entrada, '
        'así que I0 se deriva antes de R1 y por R1 circula I′2: la expresión es correcta y es '
        'la que usa toda esta respuesta.'),
  ('p', 'Pero el devanado real del estator lleva I1, no I′2. En el circuito exacto, y en '
        'cualquier problema numérico donde den la corriente de estator medida o la de placa, '
        'las pérdidas del estator son m1 · I1² · R1. Conviene tenerlo presente para no aplicar '
        'la fórmula fuera de contexto.'),
  ('p', 'No se modificó porque dentro del circuito aproximado la expresión es coherente y el '
        'apunte la escribe igual (p. 7).'),
]))

d.save()
print('bloques insertados: 5')
