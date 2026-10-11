# Retroalimentación — Laboratorio 01: Fundamentos, complejidad y recurrencias

**Estudiante:** David Morales Vargas · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-07 23:59 · **Versión revisada:** commit `32fcad5`

Muy buen trabajo de corrección: arregló casi todo lo que se le señaló en la primera revisión y su informe quedó mucho más claro y consistente con sus gráficas.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 21 / 25 |
| Calidad de la explicación teórica | 22 / 25 |
| Corrección de la implementación | 19 / 20 |
| Calidad del análisis de las gráficas | 16 / 20 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **88 / 100** |
| **Nota (0–5)** | **4.40** |

## 1. Corrección conceptual (21 / 25)
**Lo que hizo bien:**
- Distingue que un algoritmo puede dar el resultado correcto y aun así no caber en la ventana de 4 horas, y nombra esa ventana como la restricción que se incumple.
- Ahora explica bien por qué duplicar el servidor no resuelve el problema de fondo: el tiempo baja a la mitad, pero si los registros se duplican el trabajo se cuadruplica y el problema vuelve.
- Su ejemplo propio del hospital ya trae datos (más de 50.000 pruebas diarias y una hora límite) y la restricción que se incumple.
- En la Parte 2 relaciona el tiempo con el consumo de energía repetido día tras día, y señala al paciente y al operador del centro de contacto como afectados, diciendo quién asume el costo.

**Lo que puede mejorar:**
- Falta explicar la obligación extra que impone que el orden decida a quién se llama primero: por eso el orden tiene que ser siempre correcto y completo, no solo rápido.
- En el ejemplo del hospital, las horas (7 a. m., 9 a. m. y 12 m.) se mezclan un poco; conviene decir con claridad a qué hora debía estar listo el resultado y a qué hora llegaba.

## 2. Calidad de la explicación teórica (22 / 25)
**Lo que hizo bien:**
- Escribe la predicción antes de medir y justifica con claridad por qué usaría el orden inverso para decidir si entra a producción.
- Ahora define los tres casos diciendo sobre qué entradas se toma el máximo, el mínimo o el promedio, con n fijo.
- Plantea la recurrencia de merge sort, explica cada término y resuelve por sustitución, ya con el caso base y la constante que sostiene la hipótesis.
- Completa el análisis línea a línea de insertion sort: suma los costos y concluye Θ(n) en el mejor caso y Θ(n²) en el peor.

**Lo que puede mejorar:**
- El caso promedio de insertion sort solo se justifica con palabras; falta calcular la suma con el promedio de desplazamientos (cerca de la mitad en cada paso) para llegar a n².
- El caso base de la sustitución podría escribirse con más cuidado (por ejemplo, con la constante y el valor de n elegidos de forma explícita).

## 3. Corrección de la implementación (19 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien de mayor a menor, no cambian la lista recibida, cuentan comparaciones entre elementos y no usan `sorted()` ni `sort()`. La mezcla de merge sort es propia y recursiva.
- Los tres generadores dan listas con valores distintos, del tamaño pedido, y los aleatorios usan semilla.
- Ahora todas las funciones, incluidas las `main`, tienen *docstring*, y hay *type hints*.

**Lo que puede mejorar:**
- Quedaron avisos de estilo (PEP 8): espacios sobrantes al final de algunas líneas y falta del salto de línea al final de varios archivos.

## 4. Calidad del análisis de las gráficas (16 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen y tienen título, ejes rotulados, leyenda y las curvas en los mismos ejes.
- En la Parte 3.2 ya identifica bien los escenarios: C es el peor, B el mejor y A el más cercano al promedio. Las cifras que cita (más de 20 millones de comparaciones y casi 6 segundos para C; poco más de 10 mil comparaciones para B) coinciden con sus resultados y su gráfica.
- En la Parte 4.2 concluye que merge sort conviene, describe cómo crece cada curva y lo conecta con O(n²) y O(n log n).
- Ahora explica bien los tamaños pequeños: el costo de crear listas nuevas y de las llamadas recursivas pesa más que el ahorro cuando hay pocos datos.
- El concepto técnico recomienda merge sort, responde al servidor con un dato medido (2,8 s con n = 6400), calcula una extrapolación a 1.200.000 registros (unas 27 horas para insertion sort, cuenta correcta) y habla de la memoria extra.

**Lo que puede mejorar:**
- La extrapolación debe decir claramente que es una estimación, no una medición, y con qué supuestos se calculó. Para merge sort solo dice "segundos"; falta razonar con su crecimiento n log n para dar un valor aproximado.
- Algunas cifras no coinciden del todo con las gráficas: dice que merge sort tardó unos 0,02 s con n = 6400 y su gráfica muestra cerca de 0,05 s; para el escenario A dice "casi 3 segundos" y la gráfica marca cerca de 2,25 s.
- Al responder al servidor, dice "como se ve en la línea naranja", pero en esa gráfica la línea naranja es merge sort y la frase habla de insertion sort (la azul).

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- La carpeta del laboratorio está en una ubicación válida y tiene todos los archivos y gráficas pedidos.
- El informe sigue el orden pedido, las imágenes se ven con ruta relativa y cada parte enlaza su código.
- Las instrucciones de reproducción ya incluyen `python` además de `py`, y hay commits descriptivos que muestran el avance.

## ¿El código funciona?
Sí. Ambos scripts corren sin errores y generan las gráficas, y los dos algoritmos ordenan correctamente en las pruebas hechas.

## Para el próximo laboratorio
- Declare las extrapolaciones como estimaciones y explique con qué fórmula las calculó, también para el algoritmo rápido.
- Revise que cada cifra del texto coincida con la gráfica de donde la sacó y que el color o la curva que menciona sea la correcta.
- Cuando el orden afecta a personas, diga qué obligación extra eso impone sobre el resultado.
- Antes de entregar, corra una revisión de estilo (PEP 8) para quitar espacios sobrantes.
