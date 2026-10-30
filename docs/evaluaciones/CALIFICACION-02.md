# Retroalimentación — Laboratorio evaluativo 02: Dividir y vencer

**Estudiante:** David Morales Vargas · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `2a6d651`

Excelente trabajo: un laboratorio completo, ordenado y bien sustentado con sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 18 / 20 |
| Calidad de la explicación teórica | 19 / 20 |
| Corrección de la implementación | 23 / 25 |
| Calidad del análisis de las gráficas | 22 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **92 / 100** |
| **Nota (0–5)** | **4.60** |

## 1. Corrección conceptual (18 / 20)
**Lo que hizo bien:**
- Identificó que divide y vencerás empieza a ganar entre n = 10 y n = 50, con los tiempos medidos, y explicó el costo extra de la recursión en tamaños pequeños.
- Comparó con el máximo de un arreglo, planteó `T(n) = 2T(n/2) + Θ(1)` y concluyó que dividir no mejora `Θ(n)`.
- Recomendó divide y vencerás y declaró la estimación a 1.000.000 de registros (unas 27 horas contra unos 6 segundos), con su razonamiento.

**Lo que puede mejorar:**
- Dice que dividir obliga a "copiar sublistas", pero su propio código no copia nada (trabaja con índices). Conviene describir el costo real: las llamadas recursivas y las tuplas que se devuelven.
- Al estimar, vale la pena decir que la constante del modelo viene de un solo tamaño medido y puede variar a escalas mayores.

## 2. Calidad de la explicación teórica (19 / 20)
**Lo que hizo bien:**
- Planteó `T(n) = 2T(n/2) + Θ(n)`, explicó de dónde sale cada término y verificó el caso 2 del método maestro.
- Justificó el `Θ(n²)` de la fuerza bruta con la suma `n(n+1)/2`.

**Lo que puede mejorar:**
- Podría explicar también por qué el caso cruzado cuesta `Θ(n)` mostrando que los dos barridos juntos recorren todo el rango.

## 3. Corrección de la implementación (23 /25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta en todos los casos pedidos y coinciden en listas aleatorias; no modifican la lista de entrada y `subarreglo_maximo` resuelve los tres casos sin usar la fuerza bruta.
- Tiene type hints y docstrings Google en cada función, y el código respeta PEP 8.

**Lo que puede mejorar:**
- Quedaron los comentarios `# TODO` de la plantilla dentro de `subarreglo.py`; hay que borrarlos al terminar cada función.
- En `pruebas.py`, `subarreglo_fuerza_bruta` y `suma_cruzada` no se prueban por separado en el caso cruzado; ayudaría una prueba directa de `suma_cruzada`.

## 4. Calidad del análisis de las gráficas (22 / 25)
**Lo que hizo bien:**
- La gráfica tiene título, ejes rotulados, leyenda y ambas curvas en los mismos ejes, con 8 tamaños (de 10 a 8000).
- Calculó el factor al duplicar n para ambos algoritmos y lo comparó con `Θ(n²)` y `Θ(n log n)`; sus cifras coinciden con la tabla y con la gráfica (fuerza bruta cerca de 6,1 s en n = 8000).
- Agregó una tabla con los valores, útil porque la curva de divide y vencerás queda pegada al eje.

**Lo que puede mejorar:**
- Al duplicar de 4000 a 8000 obtuvo un factor de 1,35 para divide y vencerás, lejos del 2,17 esperado, y lo atribuyó solo a ruido. Habría sido mejor repetir esa medición o usar más repeticiones para confirmarlo.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- Estructura correcta (`laboratorios/lab2-divide-y-vencer/`) con todos los archivos del entregable.
- El informe sigue el orden pedido, la gráfica se ve, cada parte enlaza su código y las instrucciones de reproducción son claras.
- Hay cuatro commits del laboratorio con mensajes descriptivos.

## ¿El código funciona?
Sí. Las pruebas pasan, ambas soluciones dan siempre la misma suma (también en listas aleatorias) y la medición corre y genera la gráfica sin errores.

## Para el próximo laboratorio
- Borre los comentarios `TODO` de la plantilla cuando termine cada función.
- Si un resultado medido se aleja mucho de la teoría, repita la medición o aumente las repeticiones antes de atribuirlo al ruido.
- Describa los costos de su propio código (lo que realmente hace) y no los de una versión distinta.
- Incluya una prueba directa para cada función auxiliar, como `suma_cruzada`.
