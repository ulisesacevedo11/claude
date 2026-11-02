# Máquinas e Instalaciones Eléctricas — Respuestas al 2do parcial

Consolidado de **8 modelos** (parcial y recuperatorios: 12-11-25, 10-12-25, 11-12-24, 13-12-23, 06-03-24, 13-12-22, 07-12-22) de la carpeta `2do cuatrimestre/modelos`.

Las preguntas están **agrupadas por tema** siguiendo las unidades de la carpeta `2do cuatrimestre`:

| Unidad | Tema | ¿Aparece en los modelos? |
|---|---|---|
| 7 | Máquina asincrónica (trifásica) | Sí — tema dominante |
| 8 | Motor asincrónico monofásico | Sí — en 5 de 8 modelos |
| 9 | Motor paso a paso | No apareció nunca |
| 10 | Máquina de corriente continua | Sí — en 4 de 8 modelos |
| 11 | Máquina sincrónica | No apareció nunca |
| 12 | Calidad de energía | Sí — en 2 de 8 modelos |

**Descartado:** todas las preguntas de **transformadores** (ensayos de vacío y cortocircuito, cálculo de rendimiento, rendimiento máximo, diagrama fasorial en vacío, pérdidas vs. vida útil). Corresponden a la **Unidad 5 — Transformadores**, que está en la carpeta de **1er cuatrimestre**. Eran 7 preguntas, prácticamente una por modelo (ojo: el profesor las sigue incluyendo en los recuperatorios del 2do parcial, aunque el tema sea del 1er cuatrimestre).

---

## TEMA A — Máquina asincrónica trifásica (Unidad 7)

### A.1 — Circuito equivalente aproximado referido al primario, potencias y el término R'₂(1−s)/s
*(Parcial 12-11-25, pregunta 1)*

**Esquema (parte estatórica al comienzo):**

```
   I1 →  R1    jX1                      I'2 →   R'2      jX'2
 o──────[R1]──[jX1]──────┬──────────────────[R'2]──[jX'2]──┐
                         │                                 │
 V1                   Io │                            R'2(1-s)/s
                         ├──[Rm]──[jXm]                     │
                         │   ↓Ip    ↓Iμ                     │
 o───────────────────────┴─────────────────────────────────-┘
```

En el equivalente **aproximado**, la rama de magnetización (R_m // jX_m) se corre a bornes de entrada, de modo que I₁ = I_o + I'₂ con I_o constante. Todo lo rotórico se refiere al primario con la relación de transformación: R'₂ = a²R₂, X'₂ = a²X₂.

**Potencias, en orden de flujo:**

| Potencia | Expresión | Dónde se ve en el esquema |
|---|---|---|
| Absorbida de la red | P₁ = 3·V₁·I₁·cos φ₁ | bornes de entrada |
| Pérdidas en el cobre del estator | P_cu1 = 3·I₁²·R₁ | en R₁ |
| Pérdidas en el hierro | P_fe = 3·V₁²/R_m | en R_m |
| **Potencia transferida al rotor** (electromagnética, cruza el entrehierro) | **P_em = 3·I'₂²·(R'₂/s)** | toda la rama rotórica |
| Pérdidas en el cobre del rotor | P_cu2 = 3·I'₂²·R'₂ = **s·P_em** | en R'₂ |
| **Potencia mecánica interna** | **P_mi = 3·I'₂²·R'₂(1−s)/s = (1−s)·P_em** | en R'₂(1−s)/s |
| Pérdidas mecánicas (roce, ventilación) + adicionales | P_mec | no está en el circuito |
| **Potencia útil en el eje** | **P_u = P_mi − P_mec** | — |

Relación clave: **P_cu2 : P_mi : P_em = s : (1−s) : 1**.
Cupla electromagnética: T = P_em/ω_s = P_mi/ω, con ω_s = 2πn_s/60.

**Concepto del término R'₂(1−s)/s:**
No es una resistencia física: es una **resistencia ficticia de carga** que representa la **conversión electromecánica de energía**. La potencia que "se disipa" en ella no se transforma en calor, sino en potencia mecánica en el eje. Es el artificio que permite modelar una máquina rotante con un circuito eléctrico estático: separa, dentro de la rama rotórica R'₂/s, la parte que realmente se pierde como calor (R'₂) de la parte que se convierte en trabajo (R'₂(1−s)/s).

**Con s = 1 (rotor bloqueado / arranque):**
- R'₂(1−s)/s = 0 → el término desaparece y la rama rotórica queda **cortocircuitada** sobre R'₂ + jX'₂.
- No hay conversión electromecánica: P_mi = 0, n = 0. Sí hay cupla (cupla de arranque), pero potencia mecánica nula.
- Toda la potencia que cruza el entrehierro se disipa en el cobre del rotor: P_cu2 = P_em.
- La impedancia vista es mínima → **corriente de arranque máxima**, típicamente 5 a 8 veces la nominal. De ahí la necesidad de arranques a tensión reducida (ver A.6 y A.7).
- Es la condición del **ensayo de cortocircuito** del motor.

**Con s = 0 (velocidad de sincronismo):**
- R'₂(1−s)/s → ∞ → la rama rotórica **se abre**: I'₂ = 0.
- Sin corriente rotórica no hay cupla: T = 0. El motor sólo absorbe I_o (corriente de vacío, magnetizante + pérdidas en el hierro).
- Es físicamente **inalcanzable como motor**: para generar cualquier cupla, aunque sea sólo la que vence el roce, hace falta movimiento relativo entre el campo giratorio y el rotor. En vacío el motor queda en s ≈ 0,002…0,01, nunca en 0. Sólo se llega a s = 0 arrastrando el eje con una máquina externa.

---

### A.2 — Principio de funcionamiento, resbalamiento, tipos de rotor
*(Recuperatorio 11-12-24 preg. 2; 06-03-24 preg. 2; recurrente en casi todos los modelos)*

**Principio de funcionamiento:**
1. El estator tiene tres devanados desfasados 120° geométricos, alimentados con un sistema trifásico equilibrado. Por el **teorema de Ferraris**, producen un **campo magnético giratorio** de amplitud constante que gira a la velocidad de sincronismo:

   **n_s = 120·f / p** [rpm], con p = número de polos (n_s = 1500 rpm para 4 polos a 50 Hz).

2. Ese campo barre los conductores del rotor, que está en cortocircuito. Por **Faraday** induce en ellos una fem; como el circuito rotórico está cerrado, circula corriente I₂.
3. Por **Laplace** (F = B·I·L), la interacción de esa corriente con el campo giratorio produce una **fuerza y por lo tanto una cupla** sobre el rotor, en el sentido del campo (Lenz: el rotor trata de seguir al campo para anular la variación de flujo que lo genera).
4. El rotor acelera, pero **nunca alcanza al campo**: si lo alcanzara, cesaría el movimiento relativo, la fem inducida sería nula y desaparecería la cupla. De ahí el nombre **asincrónico** o **de inducción**.

**Resbalamiento (deslizamiento):**

   **s = (n_s − n) / n_s**,  o en %: s% = 100·(n_s − n)/n_s

Es la medida del movimiento relativo entre campo e rotor, y la variable que gobierna todo el comportamiento de la máquina. Consecuencias directas:
- Frecuencia rotórica: **f₂ = s·f₁** (frecuencia de resbalamiento).
- fem rotórica: E₂ = s·E₂₀.
- Reactancia rotórica: X₂ = s·X₂₀.
- Valores nominales típicos: s = 2 % a 6 % (menor en máquinas grandes).

**s = 1** → rotor detenido (arranque o rotor bloqueado): f₂ = f₁ = 50 Hz, corriente rotórica máxima, P_mi = 0, toda la potencia del entrehierro se disipa en el rotor. Cupla de arranque presente pero rendimiento nulo. Corriente de línea 5–8·I_n.

**s = 0** → rotor a velocidad de sincronismo: f₂ = 0, no hay fem inducida, I₂ = 0, cupla nula. Punto ideal inalcanzable como motor; sólo accionando el eje desde fuera. Si se lo fuerza por encima de n_s (s < 0) la máquina pasa a **generador asincrónico** y entrega energía a la red.

**Tipos de rotor y comportamiento electromecánico:**

| Tipo | Construcción | Comportamiento |
|---|---|---|
| **Jaula de ardilla simple** | Barras de Al o Cu en las ranuras, cortocircuitadas por anillos en ambos extremos | Robusto, sin escobillas, barato, sin mantenimiento. R₂ fija y baja: **buen rendimiento y bajo resbalamiento nominal**, pero **cupla de arranque modesta (1,5–2·T_n) con corriente de arranque alta (6–8·I_n)**. No permite regular velocidad por el rotor. |
| **Jaula profunda** | Barras de sección alta y angosta (ver A.3) | R₂ **variable automáticamente** con el resbalamiento: alta en el arranque, baja en marcha. Mejor cupla de arranque con menor corriente, conservando buen rendimiento. |
| **Doble jaula** | Dos jaulas concéntricas: la externa de alta R y baja X, la interna de baja R y alta X | Misma idea, más marcada: en el arranque trabaja la jaula externa (alta cupla), en marcha la interna (buen rendimiento). Mayor costo. |
| **Rotor bobinado (de anillos rozantes)** | Devanado trifásico en el rotor, llevado al exterior por tres anillos y escobillas | Permite **insertar resistencias externas**: desplaza la cupla máxima hacia s = 1, dando **cupla de arranque máxima con corriente reducida**, y permite regular velocidad. Contra: más caro, requiere mantenimiento de escobillas/anillos, peor rendimiento si se deja resistencia en marcha. Usado en arranques pesados y de gran inercia. |

---

### A.3 — Motor asincrónico con rotor de jaula profunda
*(Recuperatorios 10-12-25 preg. 2; 13-12-23 preg. 3; 07-12-22 preg. 3)*

Es la pregunta más repetida de los modelos.

**Construcción:** las barras del rotor no son de sección cuadrada o circular, sino **rectangulares altas y angostas** (relación altura/ancho típicamente 5:1 a 10:1), alojadas en ranuras profundas y radiales, cortocircuitadas en los extremos por los anillos.

**Característica más importante — aprovechamiento del efecto pelicular (skin):**

El flujo de dispersión que enlaza a la barra es mayor en el fondo de la ranura (más hierro alrededor) que cerca del entrehierro. Por lo tanto la parte baja de la barra tiene **mayor reactancia de dispersión** que la parte alta. La barra se comporta como muchos conductores elementales en paralelo, de impedancia creciente con la profundidad. El reparto de corriente entre ellos depende de la frecuencia rotórica **f₂ = s·f₁**:

- **En el arranque (s = 1, f₂ = 50 Hz):** las reactancias dominan. La corriente se concentra en la **parte superior** de la barra → la sección útil se reduce drásticamente → **R₂ aumenta** (2 a 4 veces) y X₂ disminuye. Esto da **mayor cupla de arranque** (la cupla de arranque crece con R₂ hasta cierto punto) con **menor corriente de arranque** (mayor impedancia y mejor factor de potencia rotórico).
- **En marcha normal (s ≈ 0,03, f₂ ≈ 1,5 Hz):** las reactancias son despreciables frente a las resistencias. La corriente se **distribuye uniformemente** en toda la sección → **R₂ vuelve a su valor bajo** → bajas pérdidas en el cobre del rotor, **buen rendimiento y bajo resbalamiento nominal**.

**La ventaja de fondo:** la jaula profunda se comporta como un **reóstato rotórico automático**, que se inserta en el arranque y se elimina solo al acelerar — logrando buena parte del beneficio del rotor bobinado **sin anillos, sin escobillas y sin mantenimiento**. Es la razón por la que domina el mercado industrial (categorías de diseño NEMA B y C).

**Limitaciones:** mayor reactancia de dispersión total → **factor de potencia algo peor** y cupla máxima algo menor que una jaula simple equivalente; rotor de diámetro mayor para alojar las ranuras profundas, lo que aumenta la inercia.

**Resbalamiento, s = 1 y s = 0:** idem A.2 (es la segunda parte literal de la pregunta en los tres modelos).

---

### A.4 — Curva par-resbalamiento y condición de equilibrio
*(Recuperatorio 06-03-24 preg. 2)*

```
  T
  │          ┌── T_max
  │         ╱ ╲
  │       ╱    ╲
  │     ╱       ╲
T_n├---╱---------●  ← punto de equilibrio (T_motor = T_carga)
  │  ╱           ╲___  T_carga
T_a├─╱                ╲
  │╱                    ╲
  └──┬──────────┬────────┬──→ s
    s=1       s_max     s=0
    (n=0)            (n=n_s)
         ← zona inestable │ zona estable →
```

Expresión de la cupla (circuito aproximado):

   **T = (3/ω_s) · V₁² · (R'₂/s) / [ (R₁ + R'₂/s)² + (X₁ + X'₂)² ]**

Cupla máxima y resbalamiento al que ocurre:

   **s_max = R'₂ / √(R₁² + (X₁+X'₂)²) ≈ R'₂ / X_cc**
   **T_max = (3/ω_s) · V₁² / [ 2·(R₁ + √(R₁²+(X₁+X'₂)²)) ]**

Dos conclusiones que la cátedra pide: **T_max no depende de R₂** (sólo su ubicación s_max), y **T ∝ V₁²** (una caída del 10 % de tensión cuesta ~19 % de cupla).

**Condición de equilibrio de funcionamiento:** el motor se estabiliza donde la curva del motor corta la curva de la carga, **T_motor = T_carga**. Pero sólo es un equilibrio **estable** en la rama entre s = 0 y s = s_max (donde dT/ds > 0, o lo que es lo mismo dT/dn < 0): ahí, si la carga aumenta, el motor baja de velocidad, sube el resbalamiento y por lo tanto **sube la cupla** hasta reencontrar el equilibrio. En la rama s_max < s < 1 el equilibrio es **inestable**: un aumento de carga frena el motor y la cupla *disminuye*, lo que lo frena más, hasta el vuelco (calado). Por eso el punto nominal se elige en la zona estable, con T_max/T_n ≈ 2–2,5 como margen de sobrecarga.

---

### A.5 — Diagrama circular del motor trifásico
*(Recuperatorio 13-12-22 preg. 3)*

El **diagrama circular** (o de Heyland/Ossanna) es el **lugar geométrico del extremo del fasor de corriente del estator I₁ cuando varía el resbalamiento de −∞ a +∞**. Con el circuito equivalente aproximado (V₁ y f constantes), ese lugar geométrico es una **circunferencia**.

```
            │ (reactivo)
            │
      P_u ─ │ ─ ─ ─ ─ ─ ─ ─ ─
       ╱    │ ·  ·  ·
      ╱ P_em│   ·      ·          recta de P_em (potencia al rotor)
     ╱      │ ·          ·
    ╱   s=1 ●   zona      ·  ← circunferencia (lugar de I1)
   ╱   (arranque)  de      ·
  ╱      ╲      arranque  ·
 ╱        ╲              ·
●──────────╲────────────·
Io (s=0)    ╲  I_arr    ·      ← I_arr = segmento 0 → punto s=1
vacío        ╲         ·
──────────────●───────●──────── (activo)
              Pn    s=1
```

**Cómo se construye:**
- **Punto de vacío (s = 0):** se obtiene del **ensayo en vacío**. El fasor desde el origen a ese punto es I_o (muy inductivo, cos φ ≈ 0,1–0,2). Es el extremo de un diámetro.
- **Punto de cortocircuito (s = 1, rotor bloqueado):** se obtiene del **ensayo de cortocircuito** a tensión reducida y se extrapola a tensión nominal. El fasor desde el origen a este punto es la **corriente de arranque I_arr** — y el diagrama muestra gráficamente por qué es 5 a 8 veces la nominal.
- La **circunferencia** pasa por ambos puntos, con el centro sobre la perpendicular trazada desde el punto medio de la cuerda que los une.

**Rectas del diagrama (todo leído como segmentos verticales, proporcionales a potencia):**
- **Recta de potencia absorbida:** el eje horizontal (eje de las potencias activas).
- **Recta de potencia transferida al rotor (P_em):** une el punto de vacío con el punto s = 1.
- **Recta de potencia mecánica (P_u):** une el punto de vacío con el punto de **sincronismo ideal** (s = 0 teórico, sin pérdidas).
- Entre la recta de P_em y la de P_u se lee la **pérdida en el cobre del rotor**; debajo de la de P_em, las pérdidas del estator y del hierro. El resbalamiento se lee como la relación entre esos dos segmentos: **s = P_cu2 / P_em**.

**Identificación que piden:**
- **Zona de arranque:** el arco cercano al punto s = 1 (parte derecha-inferior de la circunferencia), donde la corriente es máxima y la potencia útil nula. Es la zona por la que el motor "pasa" en el transitorio de aceleración.
- **Potencia nominal:** el punto de la circunferencia cuyo **segmento vertical hasta la recta de potencia mecánica equivale a P_n**. En ese punto se leen directamente I_n, cos φ_n, s_n, rendimiento (relación entre el segmento de P_u y el de P₁) y la cupla. Suele quedar en el primer tercio del arco desde vacío.
- **Corriente de arranque:** el módulo del vector desde el origen al punto s = 1.

---

### A.6 — Arranque estrella-triángulo: circuito de potencia y de mando
*(Parcial 12-11-25 preg. 4)*

**Por qué:** en arranque directo I_arr = 5…8·I_n, con caídas de tensión en la red y esfuerzos mecánicos. En estrella, cada bobinado recibe **V_línea/√3**, con lo que:
- corriente de línea de arranque → **1/3** de la del arranque directo,
- **cupla de arranque también → 1/3**.

Condición indispensable: el motor debe estar **previsto para funcionar en triángulo a la tensión de red** (p. ej. motor 380/660 V en red de 380 V) y tener los **6 bornes accesibles** (U1-V1-W1 / U2-V2-W2), con los puentes de la placa retirados.

**Circuito de potencia:**

```
  L1 L2 L3
   │  │  │
  ─┴──┴──┴─  Q1  (seccionador / interruptor + fusibles)
   │  │  │
   ├──┼──┼───────────────┐
   │  │  │               │
  ─┴──┴──┴─ KM1        ─┴──┴──┴─ KM2   (TRIÁNGULO)
   │  │  │  (línea)      │  │  │
  ─┴──┴──┴─ F1 (relé térmico)  │
   │  │  │               │  │  │
   U1 V1 W1 ─────────────┘  │  │  → KM2 puentea U1-W2, V1-U2, W1-V2
   │  │  │                  │  │
   U2 V2 W2 ───┬──┬──┬──────┘  │
               │  │  │
              ─┴──┴──┴─ KM3  (ESTRELLA: cortocircuita U2-V2-W2)
```

- **KM1** — contactor de línea, alimenta U1-V1-W1. Permanece cerrado todo el tiempo.
- **KM3** — contactor de estrella, **cortocircuita** los bornes U2-V2-W2 formando el punto neutro.
- **KM2** — contactor de triángulo, **une** U1-W2, V1-U2, W1-V2.
- **F1** — relé térmico, en serie con el motor; se ajusta a **I_n/√3 ≈ 0,58·I_n** si se monta dentro del triángulo, o a I_n si se monta en la línea.
- Calibre: KM1 y KM2 para ~0,58·I_n; KM3 para ~0,33·I_n (circula la menor corriente).

**Circuito de mando:**

```
  L1 ──┬── F1 (contacto NC del térmico) ──┬─────────────────────────┐
       │                                   │                        │
      S0 (parada, NC)                      │                        │
       │                                   │                        │
       ├──S1 (marcha, NA)──┬───────────────┤                        │
       │                   │               │                        │
       └──[KM1 aux NA]─────┘  (retención)  │                        │
       │                                   │                        │
       ├─── KM1 (bobina) ──── KT (bobina temporizada) ──────────────┤
       │                                                            │
       ├─── [KT NC, t] ─── [KM2 aux NC] ─── KM3 (bobina) ──────────┤  ESTRELLA
       │                                                            │
       └─── [KT NA, t] ─── [KM3 aux NC] ─── KM2 (bobina) ──────────┘  TRIÁNGULO
  N ─────────────────────────────────────────────────────────────────┘
```

**Secuencia de funcionamiento:**
1. Se pulsa **S1** → se energizan **KM1** (línea), **KM3** (estrella) y **KT** (temporizador al trabajo). KM1 se auto-retiene por su contacto auxiliar NA, en paralelo con S1.
2. El motor **arranca en estrella** con V_fase = 220 V y acelera hasta ~75–85 % de n_s (duración típica 3–10 s, según inercia).
3. Al cumplirse el tiempo de **KT**: su contacto NC **abre y desenergiza KM3** (se deshace la estrella), y su contacto NA **cierra y energiza KM2** (se forma el triángulo).
4. El motor queda en **marcha permanente en triángulo**, a tensión plena.
5. **S0** o el disparo del térmico **F1** cortan todo el mando.

**Enclavamiento (indispensable):** contacto auxiliar **NC de KM2 en serie con la bobina de KM3**, y **NC de KM3 en serie con la bobina de KM2**. Si KM2 y KM3 cerraran simultáneamente se produciría un **cortocircuito franco entre fases**. Se complementa con enclavamiento mecánico entre ambos contactores y, en la práctica, con un pequeño retardo de transición (KT con dos tiempos) para que se extinga el arco de KM3 antes de cerrar KM2.

**Desventajas a mencionar:** la cupla de arranque cae a 1/3, por lo que **sólo sirve para arranques en vacío o con carga de cupla creciente** (bombas, ventiladores), nunca con carga resistente constante en el arranque. Además en la conmutación Y→Δ hay un **corte momentáneo de alimentación** con un pico transitorio de corriente.

---

### A.7 — Arranque por autotransformador
*(Recuperatorio 10-12-25 preg. 5)*

**Principio:** alimentar el motor en el arranque a una tensión reducida **k·V** tomada de un autotransformador con tomas. Entonces:
- corriente en el motor: k·I_arr,
- corriente **tomada de la red**: **k²·I_arr** (el autotrafo también reduce la corriente del lado línea, a diferencia del arranque por resistencias),
- cupla de arranque: **k²·T_arr**.

Con tomas típicas de 50 / 65 / 80 %, se obtiene 25 / 42 / 64 % de la corriente y cupla del arranque directo. La **relación cupla/corriente de red es la mejor** de todos los arranques a tensión reducida — misma relación que Y-Δ pero con el factor **elegible** mediante la toma.

**Esquema de potencia (arranque Korndörfer, de 3 contactores):**

```
  L1 L2 L3
   │  │  │
  ─┴──┴──┴─ Q1 (seccionador + fusibles)
   │  │  │
   ├──┼──┼──────────────────────────┐
   │  │  │                          │
  ─┴──┴──┴─ KM1 (línea al autotrafo)│
   │  │  │                         ─┴──┴──┴─ KM3 (marcha directa)
   ╔══╪══╪════╗  AUTOTRANSFORMADOR  │  │  │
   ║ ⌇  ⌇   ⌇ ║  (3 bobinas con     │  │  │
   ║ │  │   │ ║   tomas 50/65/80%)  │  │  │
   ║ ├──┼───┼─╢── tomas ──┬──┬──┬───┤  │  │
   ║ │  │   │ ║           │  │  │   │  │  │
   ╚═╪══╪═══╪═╝          ─┴──┴──┴─ KM2 (al motor, por tomas)
     │  │   │                │  │  │
    ─┴──┴───┴─ KM0           └──┴──┴───────┴──┴──┴──→ M 3~
    (estrella del             (ambos caminos llegan a U V W)
     autotrafo)        F1 (relé térmico) en serie con el motor
```

**Secuencia (transición sin corte, que es la ventaja del Korndörfer):**
1. **Cierra KM0** (forma la estrella del autotransformador) y **KM1** (lo conecta a la red). **Cierra KM2**: el motor queda alimentado por las tomas, a k·V. Arranca y acelera.
2. **Abre KM0** → se deshace la estrella. Las bobinas del autotrafo quedan como **reactancias en serie** con el motor: el motor **nunca se desconecta**, sigue alimentado aunque a tensión algo menor. Esta es la etapa que evita el corte y el pico transitorio del Y-Δ.
3. **Cierra KM3** (marcha directa a plena tensión) y a continuación **abren KM1 y KM2**, dejando el autotransformador fuera de servicio.
4. Marcha permanente con el motor directamente a la red por KM3, protegido por F1.

El mando se arma con un temporizador KT que define el instante del paso 2–3, con **enclavamiento entre KM3 y el conjunto KM1/KM2** (no pueden coexistir la toma reducida y la plena tensión).

**Ventajas frente a Y-Δ:** factor k ajustable (adaptable a la carga), **transición sin interrupción**, no requiere los 6 bornes del motor ni que el motor sea de doble tensión. **Desventajas:** autotransformador voluminoso y caro, **dimensionado para servicio intermitente** (no soporta arranques muy frecuentes porque se calienta), mando más complejo (4 contactores). Se usa en motores de gran potencia con cargas de alta inercia.

---

## TEMA B — Motor asincrónico monofásico (Unidad 8)

### B.1 — Funcionamiento, partes constitutivas, variantes de arranque e inversión de giro
*(Recuperatorios 10-12-25 preg. 4; 11-12-24 preg. 4; 13-12-23 preg. 4; 06-03-24 preg. 3 — es la segunda pregunta más repetida)*

**Partes constitutivas:**
- **Estator:** chapas de acero al silicio ranuradas, con **dos devanados** desfasados 90° eléctricos en el espacio:
  - **devanado principal (de marcha o de trabajo):** muchas espiras de alambre grueso, baja resistencia, ocupa ~2/3 de las ranuras;
  - **devanado auxiliar (de arranque):** menos espiras, alambre más fino, mayor resistencia, ocupa ~1/3.
- **Rotor:** **jaula de ardilla** idéntica a la del trifásico (barras + anillos de cortocircuito). No tiene ninguna conexión eléctrica con el exterior.
- **Elementos de arranque según el tipo:** capacitor(es), **interruptor centrífugo** (montado en el eje) o relé de corriente/tensión, y la caja de bornes.
- Carcasa, tapas, rodamientos, ventilador.

**Problema de fondo — por qué no arranca solo:**
Un **único** devanado alimentado en monofásico no produce un campo giratorio, sino un **campo alternativo pulsante**, fijo en el espacio y variable en el tiempo. Por la **teoría del doble campo giratorio**, ese campo pulsante se descompone en **dos campos giratorios de igual amplitud (B_max/2) que giran en sentidos opuestos** a la velocidad de sincronismo.

- Con el **rotor detenido**, cada campo induce corrientes y produce su propia cupla, pero son **iguales y opuestas**: **cupla resultante nula → el motor no arranca por sí mismo**.
- Si se lo lleva a girar en un sentido cualquiera, el campo que gira en ese sentido ve un resbalamiento pequeño (s) y el contrario un resbalamiento grande (2−s). La cupla del directo crece y la del inverso cae: **la resultante es neta en el sentido en que se lo impulsó**, y el motor sigue girando solo.

Consecuencia: todo motor monofásico de inducción necesita un **artificio de arranque**, cuyo objetivo es crear un segundo campo desfasado en el tiempo y en el espacio (un campo **elíptico** o aproximadamente giratorio) para generar cupla a rotor parado. Y el campo inverso remanente, que nunca desaparece del todo, es la causa de las **cuplas pulsantes al doble de la frecuencia (100 Hz)**, el ruido y la vibración característicos, y del menor rendimiento y factor de potencia frente a un trifásico equivalente.

**Variantes de arranque:**

| Tipo | Cómo logra el desfasaje | T_arr/T_n | Aplicación |
|---|---|---|---|
| **Fase partida / split-phase** (RSIR) | El devanado auxiliar, de **alta R/X**, da un desfasaje natural de 25–30° respecto al principal. Sin capacitor. Un **interruptor centrífugo** lo desconecta al 75–80 % de n_s. | 1,5–2 | Potencias chicas (< 0,5 CV): ventiladores, bombas livianas, electrodomésticos |
| **Capacitor de arranque** (CSIR) | **Capacitor electrolítico** (alta capacidad, 50–400 µF) en **serie con el auxiliar** → desfasaje cercano a 90° → campo casi circular. El interruptor centrífugo desconecta **capacitor + auxiliar** al 75–80 % de n_s. | **3–4,5** (la más alta) | Arranques con carga: compresores de heladera, bombas de pozo, elevadores, hormigoneras |
| **Capacitor permanente** (PSC) | Capacitor de **papel/película** (pequeño, 2–20 µF) **permanentemente** en serie con el auxiliar; ambos devanados trabajan siempre. Sin partes móviles. | 0,5–1 (baja) | Donde se arranca en vacío y se exige silencio y buen FP: ventiladores de techo, extractores, aire acondicionado |
| **Dos capacitores** (CSCR) | Uno **electrolítico de arranque** + uno **permanente de marcha** en paralelo; el centrífugo desconecta sólo el de arranque. | 3–4,5 | Lo mejor de ambos: alta cupla de arranque **y** buen rendimiento y FP en marcha. Compresores grandes, 1–10 CV |
| **Polos sombra / shaded pole** | No tiene devanado auxiliar: una **espira de cobre en cortocircuito** abrazando parte de cada polo retrasa el flujo en esa región, generando un campo que "barre" hacia la zona sombreada. | < 0,5 | Muy baratos, rendimiento pobre (< 30 %). Potencias muy chicas: ventiladores de microondas, relojes, bombas de desagote de lavarropas |
| **Motor universal / de repulsión** (variantes con colector) | Rotor bobinado con colector; no es de inducción pura. | muy alta | Herramientas eléctricas, aspiradoras |

**El interruptor centrífugo:** contactos **normalmente cerrados** en reposo, montados sobre el eje, con masas y un resorte. Al alcanzar ~**75–80 % de la velocidad de sincronismo**, la fuerza centrífuga vence el resorte y **abre** el circuito del devanado auxiliar (y del capacitor de arranque, si lo hay). Al detenerse el motor, el resorte los vuelve a cerrar, dejándolo listo para el próximo arranque. Es necesario porque: (a) el electrolítico de arranque **no está diseñado para servicio continuo** (se destruiría en segundos), y (b) el auxiliar, de alambre fino y alta resistencia, **se quemaría** si quedara permanentemente energizado. Su falla (contactos pegados o que no cierran) es la causa más frecuente de que un motor monofásico "zumbe y no arranque" o se queme el bobinado auxiliar. En reemplazo se usan también **relés de corriente** (en serie, cierra el auxiliar por el pico de corriente de arranque) o **relés de tensión** (en paralelo, abre cuando la fem del auxiliar sube al acelerar) y, en equipos modernos, **PTC**.

**Curvas de cupla** *(pedido explícito en 11-12-24 preg. 4)*:

```
  T                          ← auxiliar conectado (campo casi circular)
  │   ╱‾‾‾╲
T_arr  ╱     ╲ ╲
  │ ╱         ╲ ╲  ← punto de conmutación del interruptor centrífugo
  │╱            ╲ ╲    (75–80 % de n_s)
T_n├ ─ ─ ─ ─ ─ ─ ╲ ●───╲
  │                ╲    ╲  ← sólo devanado principal (campo pulsante)
  │                  ╲   ╲
  0───────────────────────┴──→ n
  0            0,75·n_s    n_s
```
La curva real es la **envolvente superior**: se arranca sobre la curva de "ambos devanados", de alta cupla, y en el punto de conmutación se salta a la curva del devanado principal solo, que a esa velocidad ya está por encima de la cupla de la carga. Nótese que la curva del principal solo **nace en T = 0 para n = 0** — la demostración gráfica de que no arranca solo.

**Inversión de giro:**
El sentido de rotación lo determina **el orden del desfasaje entre el campo del devanado principal y el del auxiliar**. Por lo tanto se invierte **permutando las dos conexiones de uno de los dos devanados** (por convención, el **auxiliar**) **respecto del otro**:

```
   GIRO HORARIO                      GIRO ANTIHORARIO
   L ──┬── U1 [PRINCIPAL] U2 ──┬── N   L ──┬── U1 [PRINCIPAL] U2 ──┬── N
       │                       │           │                       │
       └── Z1 [AUX]+C     Z2 ──┘           └── Z2 ──[AUX]+C   Z1 ──┘
                                                  (auxiliar permutado)
```

**Lo que NO funciona:** invertir las dos fases de la **línea** (L y N), porque eso invierte *ambos* campos a la vez y el desfasaje relativo no cambia — el motor sigue girando igual. Tampoco sirve invertir los dos devanados simultáneamente.

Observaciones prácticas:
- Sólo es posible si los **cuatro extremos** (U1-U2 del principal y Z1-Z2 del auxiliar) están accesibles en la caja de bornes. Muchos motores de electrodoméstico traen el auxiliar interconectado internamente y **no son reversibles**.
- La inversión sólo debe hacerse **con el motor detenido**, porque una vez desconectado el auxiliar por el centrífugo, cambiar sus conexiones no tiene efecto; y un cambio de sentido en marcha implica un frenado con corrientes muy elevadas.
- Para inversión remota se usan **dos contactores con enclavamiento mutuo** que conmutan los extremos del auxiliar, más la logica de parada previa (temporizador de 1–2 s) antes de admitir el sentido opuesto.
- En los **PSC** (capacitor permanente), si ambos devanados son idénticos, la inversión puede hacerse en marcha simplemente conmutando a cuál de los dos devanados se le pone el capacitor en serie — es el caso de los ventiladores reversibles de techo.

---

## TEMA C — Máquina de corriente continua (Unidad 10)

### C.1 — Esquema mecánico-eléctrico de la máquina CC trabajando como motor; rotor bloqueado; dónde se representan las pérdidas
*(Parcial 12-11-25 preg. 3; recuperatorio 11-12-24 preg. 3)*

**Esquema eléctrico:**

```
      ┌──── CIRCUITO DE CAMPO ────┐        ┌──── CIRCUITO DE ARMADURA ────┐
                                               I_a →
  o───[R_f]──(L_f)──o                    o────[R_a]───(L_a)───( E )────o
  V_f    excitación                      V_a     ↑         ↑       ↑
         I_f → Φ                                 │         │       │
                                           pérdidas    inductancia  fem
                                           Joule en    de armadura  inducida
                                           el cobre                 (fcem)
```

**Ecuaciones fundamentales (régimen permanente):**
- Eléctrica de armadura: **V_a = E + I_a·R_a + 2·ΔV_esc**
- fem inducida (fuerza contraelectromotriz): **E = k·Φ·ω = (p·N/60a)·Φ·n**
- Cupla electromagnética: **T = k·Φ·I_a**
- Potencia electromagnética: **P_em = E·I_a = T·ω**
- Velocidad: **ω = (V_a − I_a·R_a) / (k·Φ)**

**Esquema mecánico / partes en juego:**
- **Estator (inductor):** carcasa de hierro (que cierra el circuito magnético), **polos principales** con el devanado de excitación que produce Φ, polos auxiliares o de conmutación, devanado compensador.
- **Rotor (armadura o inducido):** núcleo de chapas ranuradas con el devanado de armadura, **colector o conmutador** (delgas de cobre aisladas con mica) y **escobillas de carbón** con portaescobillas y resortes. Eje, rodamientos, ventilador.

**Funcionamiento como motor:** la corriente I_a entra desde la fuente por las escobillas. El **colector** actúa como un **inversor mecánico**: conmuta el sentido de la corriente en cada bobina en el instante en que pasa por la línea neutra, de modo que **la corriente bajo cada polo mantiene siempre el mismo sentido**. Así la fuerza F = B·I·L sobre todos los conductores tiene **sentido coherente** y la cupla resultante es unidireccional y continua. Al girar, el devanado de armadura corta el flujo polar y genera E, que se **opone** a V_a (fcem) y es lo que autorregula I_a: si el motor se carga, baja la velocidad, baja E, sube I_a y por lo tanto sube la cupla.

**Nota sobre "excitada por armadura":** en esta configuración la variable de control es **V_a** (control por armadura, a flujo constante), dando una característica velocidad-cupla **lineal y de caída suave** (shunt-like), con regulación de velocidad proporcional a V_a y cupla disponible constante — es la base del accionamiento con chopper o rectificador controlado. Se distingue del **control por campo** (flujo variable, potencia constante, zona de debilitamiento de campo por encima de la velocidad base).

**¿Qué ocurre si el rotor está bloqueado?** *(pedido en 12-11-25)*
- ω = 0 → **E = k·Φ·ω = 0**: desaparece la fuerza contraelectromotriz, que es la única que limita la corriente en régimen.
- La corriente queda limitada **sólo por la resistencia de armadura**, que es muy pequeña (décimas de ohm):
  **I_a = V_a / R_a**, típicamente **10 a 20 veces I_n** (la "corriente de cortocircuito" de la máquina).
- **Cupla máxima** (T = k·Φ·I_a, con I_a máxima) pero **potencia mecánica nula** (P = T·ω = 0): ni una fracción de la energía absorbida se convierte en trabajo.
- **Toda la potencia absorbida se disipa como calor en R_a y en las escobillas** → riesgo inmediato de quemar el bobinado de armadura, desprender las soldaduras de las delgas por dilatación y de chispazos destructivos / "flameo" en el colector. Además el par de choque castiga la transmisión.
- Es precisamente la razón por la que una máquina CC **no se arranca nunca a tensión plena** sin precauciones: se usa **resistencia de arranque en serie** con la armadura (escalonada y eliminada progresivamente a medida que crece E), **arranque a tensión reducida** (chopper, Ward-Leonard, rectificador controlado) y **protección de sobrecorriente / detección de rotor bloqueado**. Nótese que este estado es el mismo que el **ensayo de rotor bloqueado**, que por eso se hace a **tensión muy reducida**.

**¿Dónde se representan las pérdidas?** *(pedido en ambos modelos)*
Hay que distinguir las que **sí** aparecen como elementos del circuito equivalente y las que **no**:

| Pérdida | ¿Se representa en el circuito? | Dónde |
|---|---|---|
| Joule en el cobre de **armadura** | **Sí** | en **R_a**: P = I_a²·R_a |
| Joule en el cobre de **excitación** | **Sí** | en **R_f**: P = I_f²·R_f (= V_f·I_f en derivación) |
| Caída en las **escobillas** | Sí, como fuente de tensión constante | **2·ΔV_esc ≈ 2 V** por par de escobillas: P = 2·ΔV·I_a |
| Pérdidas en el **hierro** (histéresis + Foucault en el rotor) | **No** como elemento | se descuentan de P_em |
| Pérdidas **mecánicas** (roce de rodamientos, roce de escobillas, ventilación) | **No** | se descuentan de P_em |
| Pérdidas **adicionales / adicionales por carga** (~1 % de P_n) | **No** | se descuentan de P_em |

Las cuatro últimas **no tienen un elemento circuital** porque no son de naturaleza eléctrica resistiva: se representan en el **balance de potencias (diagrama de Sankey)**, como la diferencia entre la potencia electromagnética y la potencia en el eje. Para el motor:

```
P_1 = V_a·I_a + V_f·I_f  (absorbida de la red)
  │
  ├─→ P_cu campo (R_f)      ─┐
  ├─→ P_cu armadura (R_a)    │ pérdidas eléctricas → SÍ en el circuito
  ├─→ P_escobillas           ─┘
  ▼
P_em = E·I_a = T·ω          (potencia electromagnética, convertida)
  │
  ├─→ P_fe (hierro)         ─┐
  ├─→ P_mec (roce+vent.)     │ pérdidas "mecánicas y en el hierro" → NO en el circuito
  ├─→ P_adic                ─┘
  ▼
P_u = T_eje·ω               (potencia útil en el eje)      η = P_u / P_1
```
(En el **generador** el diagrama es el mismo recorrido al revés: se entra por el eje y se sale por los bornes.)

**¿Qué significa que la máquina sea reversible?** *(pedido en 11-12-24 preg. 3)*
Que **la misma máquina, sin ninguna modificación constructiva**, puede funcionar como **motor** (convierte energía eléctrica en mecánica) o como **generador/dinamo** (convierte mecánica en eléctrica). Es la reversibilidad electromecánica, y en la máquina CC es particularmente directa porque **el mismo colector** que rectifica para generar, conmuta para motorizar.

Lo que define el modo es la relación entre **E** y **V_a**:
- **E < V_a** → I_a = (V_a − E)/R_a es **positiva**, entra corriente a la armadura: **modo motor**, cupla y velocidad en el mismo sentido, la máquina consume de la red.
- **E > V_a** (porque la carga arrastra el eje, o porque se baja V_a, o porque se aumenta el flujo) → **I_a se invierte**, la cupla se invierte y pasa a ser **frenante** mientras el sentido de giro se mantiene: **modo generador**, la máquina **devuelve energía a la red**. Es el **frenado regenerativo**, de uso corriente en tracción eléctrica, ascensores y grúas (bajar una carga recuperando energía).
- Si además se invierte V_a o Φ, se obtienen los otros dos cuadrantes (frenado a contracorriente y marcha inversa): la máquina CC excitada independientemente es por eso una máquina de **cuatro cuadrantes** natural.

---

### C.2 — Partes constitutivas y reacción de armadura
*(Recuperatorios 10-12-25 preg. 3; 07-12-22 preg. 4)*

**Partes constitutivas:**

**Estator (inductor / circuito de excitación):**
- **Carcasa o yugo:** de acero fundido o laminado; sostiene mecánicamente la máquina y **cierra el circuito magnético**.
- **Polos principales:** núcleo de chapas con **expansión o zapata polar** (para distribuir el flujo en el entrehierro) y el **devanado de excitación** que crea Φ. En excitación derivación: muchas espiras finas; en serie: pocas espiras gruesas.
- **Polos auxiliares o de conmutación (interpolos):** más pequeños, ubicados en el eje neutro geométrico, con devanado de pocas espiras gruesas **en serie con la armadura**. Mejoran la conmutación.
- **Devanado de compensación:** alojado en ranuras de las **caras polares**, también en serie con la armadura.
- **Portaescobillas y escobillas** de grafito/electrografito, con resortes de presión regulable, montados en un anillo portaescobillas orientable.

**Rotor (armadura o inducido):**
- **Núcleo de chapas** de acero al silicio aisladas y ranuradas (laminado para limitar las corrientes de Foucault).
- **Devanado de armadura:** bobinas alojadas en las ranuras y conectadas al colector en configuración **imbricada (lap)** — para alta corriente, 2p caminos en paralelo — u **ondulada (wave)** — para alta tensión, 2 caminos.
- **Colector o conmutador:** cilindro de **delgas de cobre** aisladas entre sí con **mica**, montado sobre el eje y aislado de él. Es la pieza característica y el punto débil de la máquina.
- **Eje, rodamientos, ventilador y bandas de sujeción.**

**Entrehierro:** el espacio entre la zapata polar y la armadura; su longitud define en gran medida la reluctancia y la sensibilidad a la reacción de armadura.

**Reacción de armadura — el efecto de debilitamiento de los polos magnéticos:**

**Qué es:** la corriente I_a que circula por el devanado de armadura **crea su propio campo magnético** (fmm de armadura), transversal al de los polos principales (su eje coincide con la línea neutra geométrica, es decir, está en **cuadratura** con el eje polar). Ese campo **se superpone** al campo principal y lo distorsiona. El fenómeno existe sólo bajo carga: en vacío (I_a ≈ 0) no se manifiesta.

```
  En vacío (sólo Φ polar)        Bajo carga (Φ polar + Φ armadura)
     N                                 N
  ┌──────┐                         ┌──────┐
  │ →→→→ │  flujo uniforme         │ →→→  │  cuerno de "entrada": debilitado
  │ →→→→ │                         │ ↘→→→→│  cuerno de "salida": reforzado
  └──────┘                         └──────┘   (y saturado)
   n.g. = n.m.                      n.m. desplazada en el sentido de giro
```

**Dos efectos distintos:**
1. **Distorsión del flujo y desplazamiento de la línea neutra:** en una mitad de cada polo (el "cuerno de entrada") los dos campos se oponen y el flujo se **debilita**; en la otra ("cuerno de salida") se suman y el flujo se **refuerza**. La **línea neutra magnética** se corre respecto de la geométrica: **en el sentido de giro en el generador** y **en sentido contrario al giro en el motor**. El corrimiento crece con la carga.
2. **Debilitamiento neto del flujo total (el "efecto de debilitamiento de los polos" que pregunta el examen):** si el hierro fuera lineal, lo que se pierde en un cuerno se ganaría en el otro y el flujo total no cambiaría. Pero el cuerno reforzado **entra en saturación**, de modo que no gana todo lo que el otro pierde: el resultado es una **reducción neta del flujo por polo Φ**. Este es un efecto **desmagnetizante** de segundo orden pero perfectamente medible.

**Problemas que trae:**
- **Caída de la fem:** como E = k·Φ·ω, el debilitamiento de Φ **reduce E** bajo carga. En el **generador** esto empeora la regulación de tensión (la tensión de salida cae más de lo que explica I_a·R_a).
- **En el motor, inestabilidad de velocidad:** ω = (V_a − I_a·R_a)/(k·Φ). Al aumentar la carga, I_a crece, Φ disminuye y la velocidad **tiende a aumentar**, contrarrestando (o incluso invirtiendo) la caída normal por I_a·R_a. Un motor derivación puede presentar una característica **ascendente** y volverse **inestable**, con riesgo de embalamiento.
- **Pérdida de cupla:** T = k·Φ·I_a cae al caer Φ, por lo que la máquina entrega menos cupla de la esperada para una misma corriente.
- **Mala conmutación y chisporroteo (el problema más grave):** las escobillas están fijas en la línea neutra **geométrica**. Al correrse la línea neutra magnética, las escobillas cortocircuitan bobinas que **ya no están en una zona de flujo nulo**, de modo que esas bobinas tienen fem inducida y por ellas circulan corrientes de cortocircuito elevadas. El resultado es **chisporroteo y arco en el colector**, que produce: quemado y acanalado de las delgas, desgaste acelerado y rápido de escobillas, "flameo" (arco circular entre escobillas de distinta polaridad, que puede destruir el colector en segundos), interferencia electromagnética, y en atmósferas peligrosas, riesgo de ignición.
- A esto se suma la **fem de autoinducción** de la bobina en conmutación (L·di/dt, "conmutación retardada"), que agrava el chisporroteo.

**Cómo se soluciona:**

| Solución | Cómo actúa | Observaciones |
|---|---|---|
| **Polos auxiliares o de conmutación (interpolos)** | Devanado de pocas espiras gruesas, **en serie con la armadura**, ubicado sobre la línea neutra geométrica. Genera un flujo local que **anula la fem de reacción y la de autoinducción en la bobina que está conmutando**. Al estar en serie, **se autorregula**: su acción crece proporcionalmente a I_a. | **La solución estándar**: la lleva prácticamente toda máquina CC de más de 1 kW. Corrige la conmutación, pero **no el debilitamiento del flujo** (actúa sólo en la zona interpolar). |
| **Devanado de compensación (o compensador)** | Conductores alojados en ranuras de las **caras polares**, **en serie con la armadura** y recorridos en **sentido opuesto** a los conductores de armadura que tienen debajo. Cancela la fmm de armadura **punto a punto, a lo largo de toda la cara polar**. | La solución **más efectiva y completa**: elimina la distorsión y el debilitamiento. Es **caro y complejo** de construir, por lo que se reserva para máquinas grandes o de carga muy variable y choques de corriente (laminadores, tracción, Ward-Leonard). Se usa **junto con** los interpolos. |
| **Desplazar las escobillas** a la nueva línea neutra magnética | Girar el anillo portaescobillas en el sentido de giro (generador) o en contra (motor) hasta la posición de mínimo chisporroteo. | Solución **histórica y pobre**: sólo es correcta para **un** punto de carga, y al correrlas se introduce además una componente **directamente desmagnetizante** de la fmm de armadura, que **empeora** el debilitamiento del flujo. No sirve en máquinas de carga variable ni reversibles. |
| **Medidas de diseño magnético** | Aumentar el **entrehierro en los cuernos polares** (zapatas con entrehierro no uniforme o achaflanadas), hacer ranuras en las zapatas, o dimensionar el circuito magnético con menor densidad de flujo para alejarse de la saturación. | Reducen la sensibilidad a la reacción de armadura, a costa de más fmm de excitación (inductor más grande). |
| **Devanado serie de compensación / estabilizador** | En motores derivación, agregar unas pocas espiras **en serie** que refuercen el flujo al crecer la carga. | Compensa el debilitamiento y **estabiliza la característica de velocidad** (evita la pendiente ascendente). |

---

## TEMA D — Calidad de energía (Unidad 12)

### D.1 — Factor de forma, factor de cresta y corriente de neutro
*(Parcial 12-11-25 preg. 5)*

**Factor de forma:**

   **F_f = Valor eficaz / Valor medio rectificado = X_rms / X_med**

Para una **senoide pura**: X_rms = X_p/√2 = 0,707·X_p y X_med = 2·X_p/π = 0,637·X_p, de donde **F_f = π/(2√2) = 1,11**.

**Factor de cresta (o factor de pico):**

   **F_c = Valor de pico / Valor eficaz = X_p / X_rms**

Para una **senoide pura**: **F_c = √2 = 1,414**. Para otras formas: onda cuadrada 1,00; triangular 1,73; corriente de un rectificador monofásico con filtro capacitivo **2,5 a 3,5 o más**.

**Cómo se interpretan en el análisis de calidad de energía:**

Ambos son **indicadores de distorsión sin necesidad de un análisis armónico completo**: su **apartamiento de los valores de la senoide pura (1,11 y 1,414)** mide cuánto se deformó la onda. Lo que cada uno dice:

- **F_c > 1,414 → onda "picuda":** la energía está concentrada en picos breves y altos. Es la **firma típica de la corriente demandada por cargas no lineales con rectificador y capacitor de filtro**: fuentes conmutadas de PC y servidores, cargadores, LED, balastos electrónicos, variadores de velocidad. Consecuencias prácticas:
  - Las **protecciones térmicas y los interruptores**, calibrados en valor eficaz, no "ven" los picos; en cambio los **componentes semiconductores y los contactos** sí los sufren → necesidad de **sobredimensionar** protecciones y, a veces, de usar curvas de disparo distintas.
  - **Saturación de transformadores y UPS** por los picos de corriente, con distorsión de la tensión aguas abajo (el pico de corriente sobre la impedancia de la fuente **achata la cresta de la tensión**: "flat-topping").
  - Mayores **pérdidas en los conductores** que las que predice la corriente eficaz, por efecto pelicular en las componentes de alta frecuencia.
  - Instrumentos de medición **no TRMS** cometen errores groseros (de 10 a 40 %): un multímetro de valor medio calibrado en eficaz asume F_f = 1,11 y falla ante una onda distorsionada. **Exige instrumentos True RMS.**
- **F_c ≈ 1 → onda achatada o cuadrada:** típico de la **tensión** en redes muy cargadas con electrónica (flat-topping) o de la salida de inversores de onda cuadrada/modificada. Problema para equipos que dependen del pico de tensión para cargar sus capacitores de entrada (fuentes conmutadas, que responden tomando pulsos más altos aún, realimentando el problema).
- **F_f** es más sensible a la **asimetría y a la componente de continua**: un F_f muy alejado de 1,11 revela presencia de armónicas pares o de una componente de CC (rectificación de media onda, cargas asimétricas), que es especialmente dañina porque **satura los núcleos** de transformadores y motores.

Relación con el THD: para una onda sin continua, **X_rms = X_1·√(1+THD²)**, de modo que crecimientos de F_c y apartamientos de F_f son manifestaciones del mismo contenido armónico. En la práctica el F_c es el indicador que se usa para **dimensionar** (conductores, neutro, transformadores factor K, UPS) y el THD el que se usa para **evaluar el cumplimiento normativo** (IEEE 519, IEC 61000, en Argentina la Resolución ENRE 184/2000 y la norma AEA).

**Justificación de la corriente de neutro importante con cargas no lineales balanceadas:**

La pregunta es un clásico y encierra una paradoja aparente: *si el sistema está balanceado, ¿no debería ser I_N = 0?*

La respuesta: **en un sistema balanceado con cargas LINEALES, sí** — las tres corrientes fundamentales están desfasadas 120° y su suma vectorial es nula: I_N = I_R + I_S + I_T = 0. **Pero con cargas NO LINEALES la cancelación falla para una familia de armónicas.**

Analicemos el desfasaje de cada armónica de orden h entre fases. Si la fase R tiene su armónica h en fase 0, la fase S la tiene en **h·120°** y la T en **h·240°**:

| Orden h | Desfasaje entre fases | Secuencia | ¿Se cancela en el neutro? |
|---|---|---|---|
| 1, 7, 13, 19… (h = 3k+1) | 120° | **Directa** | **Sí** — suma vectorial nula |
| 5, 11, 17, 23… (h = 3k+2) | 240° (= −120°) | **Inversa** | **Sí** — suma vectorial nula |
| **3, 9, 15, 21… (h = 3k, múltiplos impares de 3)** | **h·120° = 360°·k ≡ 0°** | **Homopolar (cero)** | **NO — están EN FASE y se SUMAN aritméticamente** |

Las armónicas de orden **múltiplo impar de 3** ("triplens" o de secuencia homopolar) **tienen exactamente la misma fase en las tres fases del sistema**. Por lo tanto, al llegar al nudo del neutro **no se cancelan: se suman algebraicamente**:

   **I_N3 = I_R3 + I_S3 + I_T3 = 3·I_3**

Y la corriente de neutro total resulta:

   **I_N = 3·√(I_3² + I_9² + I_15² + …)**

**Magnitud del fenómeno:** en cargas electrónicas monofásicas (fuentes conmutadas), la 3ª armónica alcanza típicamente el **50 a 80 % de la fundamental**. Con I_3 = 0,6·I_1 por fase:

   I_N ≈ 3 × 0,6·I_1 = **1,8·I_1**

Es decir, **la corriente del neutro puede ser cerca del doble de la de cada fase**, aun con el sistema perfectamente balanceado. En casos extremos (grandes salas de servidores, iluminación LED masiva, bancos de cargadores) se han medido **I_N de 1,7 a 2,1 veces** la corriente de fase.

**Consecuencias y medidas:**
- **Sobrecalentamiento del conductor de neutro**, que tradicionalmente se dimensionaba **con sección reducida** (la mitad de las fases) precisamente porque "no lleva corriente". Es una causa frecuente de incendios en tableros y de fusión de barras de neutro.
- El neutro **no tiene protección de sobrecorriente** (no se lo puede seccionar), por lo que la sobrecarga pasa inadvertida hasta la falla.
- **Saturación y sobrecalentamiento de transformadores:** en un transformador **Dyn11**, las corrientes homopolares del secundario no pueden transferirse al primario y quedan **circulando por el devanado en triángulo**, calentándolo sin que se vea en la corriente de línea. Exige **factor de desclasificación** o transformadores **factor K**.
- **Elevación del potencial de neutro** respecto de tierra, con tensiones de modo común que afectan equipos sensibles e interfieren en redes de datos.
- **Interferencia telefónica y en señales** (las triplens son el componente de peor acoplamiento inductivo).

**Soluciones:**
1. **Dimensionar el neutro igual o mayor que las fases** — la AEA 90364 y la IEC 60364 exigen neutro de **sección plena** y hasta **1,45 a 2 veces** cuando el contenido de 3ª armónica supera el 33 %; o directamente **neutro doble** / una fase dedicada por circuito.
2. **Transformadores de aislación con conexión zig-zag o Δ-Y** cerca de la carga, que **atrapan** las homopolares y evitan que se propaguen aguas arriba.
3. **Filtros de 3ª armónica** (pasivos sintonizados a 150 Hz) o **filtros activos** en el neutro.
4. **Distribuir las cargas electrónicas** y preferir equipos con **corrección activa del factor de potencia (PFC)**, que toman corriente casi senoidal (THD < 10 %).
5. Usar **rectificadores trifásicos de 6, 12 o 18 pulsos** en lugar de muchas fuentes monofásicas, que no generan triplens.

---

### D.2 — Análisis de las componentes armónicas en una distribución de 50 Hz y sus efectos
*(Recuperatorio 13-12-22 preg. 4)*

**Marco conceptual:** una onda periódica distorsionada se descompone por **serie de Fourier** en la fundamental de 50 Hz más una suma de senoides de frecuencia múltiplo entero **h·50 Hz**. El indicador global es:

   **THD = √(Σ_{h≥2} I_h²) / I_1 × 100 %**

El origen son las **cargas no lineales**: rectificadores y fuentes conmutadas, variadores de velocidad y arrancadores electrónicos, hornos de arco y soldadoras, balastos electrónicos y LED, UPS, transformadores y motores saturados.

**Análisis orden por orden, con la frecuencia correspondiente a una red de 50 Hz:**

| Orden | Frecuencia | Secuencia | Origen típico | Efectos específicos |
|---|---|---|---|---|
| **2ª, 4ª, 6ª… (pares)** | 100, 200, 300 Hz | — | Rectificación de **media onda**, cargas asimétricas, conducción desigual de semiconductores, hornos de arco en el cebado | Normalmente **ausentes o muy chicas** en redes simétricas (la simetría de media onda las anula). Su presencia **indica una falla o asimetría** y suele venir con **componente de continua**, que **satura los núcleos** de transformadores y motores, desplaza el ciclo de histéresis, aumenta la corriente de magnetización y produce ruido audible. También **falsea la medición** de instrumentos de valor medio. |
| **3ª (y 9ª, 15ª, 21ª)** | **150** (450, 750, 1050) Hz | **Homopolar (cero)** | La **dominante** en instalaciones de alumbrado y electrónica: fuentes conmutadas monofásicas, LED, balastos, cargadores | **El problema más grave en baja tensión.** Se **suman en el neutro** (I_N = 3·I_3, ver D.1) → sobrecarga y quemado del neutro y de las barras del tablero. En transformadores **Dyn** quedan **circulando en el triángulo**, calentándolo sin manifestarse en la línea → necesidad de desclasificar el transformador o usar **factor K**. Peor **acoplamiento inductivo con líneas telefónicas y de datos** (interferencia). Elevan el potencial neutro-tierra. En motores **no producen cupla** (al ser homopolares no crean campo giratorio): sólo calor. |
| **5ª (y 11ª, 17ª, 23ª)** | **250** (550, 850, 1150) Hz | **Inversa** | Rectificadores trifásicos de 6 pulsos, variadores de velocidad: son sus armónicas características (h = 6k ± 1) | Crean un **campo giratorio en sentido CONTRARIO** al de la fundamental. En **motores de inducción**: cupla de frenado (reduce la cupla útil), **cuplas pulsantes y vibración mecánica**, pérdidas adicionales en el rotor y **sobrecalentamiento** → reducción de la vida útil del aislamiento (la regla de Montsinger: +10 °C ≈ mitad de vida útil). En **generadores**, calentamiento del rotor y de las piezas de sujeción. Es la armónica que los **filtros pasivos** de planta atacan primero. |
| **7ª (y 13ª, 19ª, 25ª)** | **350** (650, 950, 1250) Hz | **Directa** | Idem anteriores (h = 6k + 1) | Campo giratorio en el **mismo sentido** pero a 7 veces la velocidad: produce **cuplas pulsantes de alta frecuencia** (al batir con la fundamental), ruido audible, vibración y **calentamiento** por pérdidas en el hierro y por efecto pelicular en el cobre. Contribuye al desgaste de rodamientos por corrientes parásitas de eje. |
| **Altas (> 25ª) e interarmónicas** | > 1,25 kHz | varias | Conmutación de IGBT en variadores (kHz), hornos de arco, cicloconvertidores | **Flicker** y fluctuaciones de tensión (interarmónicas), interferencia electromagnética radiada y conducida, falla de equipos de control y comunicación por líneas (PLC), ruido en señales analógicas. Las pérdidas en el hierro crecen como f² para Foucault y f^1,6 para histéresis. |

**Efectos generales (válidos para todas las armónicas):**

1. **Pérdidas adicionales y calentamiento:**
   - En **conductores**: las pérdidas Joule crecen con el valor eficaz total, y además la resistencia efectiva aumenta con la frecuencia por **efecto pelicular y de proximidad** (R_h ≈ R_dc·√h): el cobre se calienta más de lo que predice la corriente de la fundamental → desclasificación de cables.
   - En **transformadores**: pérdidas en el hierro (histéresis ∝ f·B^1,6, Foucault ∝ f²·B²) y pérdidas adicionales en el cobre y en las piezas estructurales. Se cuantifica con el **factor K** o el factor de pérdidas por corrientes de Foucault F_HL; obliga a **desclasificar** el transformador (un transformador estándar alimentando 100 % de cargas electrónicas debe desclasificarse al 50–70 %).
   - En **motores**: calentamiento adicional, cuplas parásitas y vibración. El indicador normalizado es el **HVF (Harmonic Voltage Factor)** de la NEMA MG-1.

2. **Resonancia con los bancos de capacitores de corrección del factor de potencia** — el efecto más destructivo y menos intuitivo. El banco de capacitores (X_C) y la inductancia de cortocircuito de la red (X_L, esencialmente el transformador) forman un **circuito resonante** a:

   **f_r ≈ f₁·√(S_cc / Q_c)**

   Si f_r coincide con una armónica presente (muy frecuente que caiga cerca de la 5ª o 7ª), se produce **amplificación de la corriente y de la tensión armónica** de 5 a 20 veces. Consecuencias: **falla y explosión de capacitores**, actuación de sus fusibles, sobretensiones en toda la instalación, disparo de protecciones. Solución: **reactancias antiarmónicas (filtros desintonizados)** en serie con el banco, sintonizadas típicamente al 4,2ª o 4,7ª orden (p = 5,67 % o 7 %), que llevan la resonancia por **debajo** de la armónica más baja presente.

3. **Degradación del factor de potencia real.** Con distorsión, el factor de potencia **ya no es cos φ**:

   **FP = P / S = cos φ₁ / √(1 + THD_I²) = FP_desplazamiento × FP_distorsión**

   Aparece una **potencia de distorsión D**, con S = √(P² + Q² + D²). Un banco de capacitores **no corrige la componente de distorsión** (sólo el desplazamiento), por lo que puede ocurrir que se penalice el FP aunque el cos φ sea excelente.

4. **Mal funcionamiento de protecciones y aparatos de maniobra:**
   - **Disparos espurios de interruptores diferenciales** (las corrientes de fuga de alta frecuencia de los filtros EMI de las fuentes conmutadas se suman) y de **termomagnéticos** (los picos de corriente actúan sobre el elemento magnético).
   - Pérdida de selectividad; relés de protección y de medida con errores de lectura.
   - Mayor desgaste de contactos por los picos de corriente en la maniobra.
   - **Fusibles** que se degradan por ciclado térmico a 100/150 Hz.

5. **Errores de medición y facturación:** medidores de inducción (de disco) y multímetros de valor medio dan errores del 10 al 40 % frente a ondas distorsionadas. Obligatorio el uso de instrumentos **True RMS** y analizadores de calidad clase A (IEC 61000-4-30).

6. **Reducción de la vida útil de las aislaciones** por el ciclado térmico y el mayor dv/dt; **ruido audible** en transformadores y reactores por fuerzas magnetostrictivas a 100, 150, 250 Hz; **vibración** en máquinas rotantes.

7. **Deformación de la tensión de la red:** la corriente armónica, al circular por la impedancia de la fuente, produce caídas armónicas de tensión (V_h = I_h·Z_h) que **distorsionan la tensión para todos los usuarios** conectados al mismo punto. Así un usuario contamina a otro; de ahí la necesidad de límites normativos de **emisión de corriente** por usuario (IEEE 519: THD_I ≤ 5 % en el punto de acople común para I_cc/I_L < 20; IEC 61000-3-2 para equipos; ENRE 184/2000 en Argentina).

**Medidas de mitigación, en orden de intervención:**
- **En la carga:** equipos con **PFC activo** (THD_I < 10 %), rectificadores de **12 o 18 pulsos**, variadores con rectificador activo (AFE).
- **Filtros pasivos sintonizados** (L-C serie a 250, 350 Hz), para derivar la armónica a tierra; baratos y robustos, pero fijos y con riesgo de resonar con la red.
- **Filtros activos** (inyectan la corriente armónica en contrafase); caros pero adaptativos y sin riesgo de resonancia.
- **Reactancias antiarmónicas** en todo banco de capacitores de una instalación con electrónica (prácticamente obligatorio hoy).
- **Transformadores de aislación zig-zag o Δ-Y** y **transformadores factor K** cerca de las cargas, para bloquear las homopolares.
- **Dimensionamiento preventivo:** neutro de sección plena o doble, desclasificación de transformadores y cables, instrumentos TRMS.
- **Desplazamiento de fase:** alimentar grupos de rectificadores con transformadores de distinta conexión (Δ-Y y Δ-Δ) para que sus armónicas de 5ª y 7ª se cancelen mutuamente.

---

## Apéndice — Preguntas descartadas (Unidad 5, Transformadores — 1er cuatrimestre)

Se dejaron afuera por no corresponder al 2do cuatrimestre, pero conviene saber que **el profesor las sigue incluyendo** en los recuperatorios del 2do parcial (en 6 de los 8 modelos). Son:

| Modelo | Pregunta descartada |
|---|---|
| 12-11-25 (#2) | Ensayo de transformador monofásico: procedimiento, set-up, conexionado y mediciones para extraer las **pérdidas en el cobre** (ensayo de cortocircuito), e información operativa que aporta |
| 10-12-25 (#1) | Ensayo de transformador: parámetros, circuitos característicos, significado de cada pérdida, pérdidas en función del tiempo y vida útil |
| 11-12-24 (#1) | Cálculo: trafo 315 kVA 13200/380-220 V, P_fe = 1,5 kW, P_cu_n = 2,5 kW → rendimiento a 1/8 de carga con FP = 1, y rendimiento máximo y estado de carga al que ocurre |
| 13-12-23 (#1 y #2) | Cálculo: trafo 500 kVA, P_fe = 1 kW, P_cu_n = 1,5 kW → relación de transformación, corrientes nominales, η a ½ carga, η máximo. Más ensayos y pérdidas en el diagrama fasorial en vacío |
| 06-03-24 (#1) | Cálculo: trafo 500 kVA 13200/400 V, P_fe = 1 kW, P_cu_n = 4 kW → relación de transformación, corrientes, η al 100 % con FP 0,75 inductivo, η máximo |
| 13-12-22 (#1 y #2) | Cálculo (500 kVA, 1 kW / 1,5 kW) y ensayos + pérdidas en el diagrama fasorial en vacío |
| 07-12-22 (#1 y #2) | Cálculo (500 kVA, 1 kW / 6,5 kW: η a ½ carga FP 1, η al 100 % FP 0,75 ind., η máximo) y ensayos + vida útil |

**Dos temas del programa del 2do cuatrimestre que NO aparecieron en ningún modelo:** **Unidad 9 — Motor paso a paso** y **Unidad 11 — Máquina sincrónica**. Dado que el 2do parcial del 12-11-25 ya incluyó Calidad de Energía (Unidad 12), conviene no descartarlos de la preparación.
