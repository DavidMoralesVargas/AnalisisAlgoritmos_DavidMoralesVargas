# Retroalimentación — Laboratorio 01: Fundamentos, complejidad y recurrencias

**Estudiante:** David Morales Vargas · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-06 23:59 · **Versión revisada:** commit `d7452eb`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 17 / 25 |
| Calidad de la explicación teórica | 18 / 25 |
| Corrección de la implementación | 17 / 20 |
| Calidad del análisis de las gráficas | 13 / 20 |
| Documentación y organización del informe | 9 / 10 |
| **Total** | **74 / 100** |
| **Nota (0–5)** | **3.70** |

## 1. Corrección conceptual (17 / 25)
**Lo que hizo bien:**
- Distingue que un algoritmo puede dar el resultado correcto y aun así no caber en la ventana de 4 horas, y nombra esa ventana como la restricción que se incumple.
- Da un segundo ejemplo propio (el bot de pruebas de laboratorio del hospital que terminaba pasadas las 12 del día).
- En la Parte 2 relaciona el tiempo con el consumo de energía repetido día tras día, y señala al paciente y al operador del centro de contacto como afectados, diciendo quién asume el costo.

**Lo que puede mejorar:**
- En el ejemplo del hospital faltan datos: cuántas pruebas se procesaban y cuánto tardaba el proceso.
- La explicación de por qué duplicar el servidor no sirve es confusa. Dice que el tiempo "se cuadruplica" y, en la Parte 2, que duplicar la velocidad haría que el ordenamiento tarde más; ninguna de las dos cosas es correcta. Lo que ocurre es que el tiempo baja a la mitad, pero con más registros vuelve a crecer al cuadrado.
- Se menciona a la "Secretaría de Educación" en lugar de la de Salud.
- La tensión de que el orden decide a quién se llama primero se menciona, pero no se explica qué obligación extra impone sobre que el orden sea correcto.

## 2. Calidad de la explicación teórica (18 / 25)
**Lo que hizo bien:**
- Escribe la predicción antes de medir y justifica con claridad por qué usaría el orden inverso para decidir si entra a producción.
- Plantea la recurrencia de merge sort y explica cada término (2 subproblemas, mitad de tamaño, costo lineal de mezclar).
- Resuelve por sustitución con pasos intermedios y llega a `O(n log n)`. Incluye la tabla de complejidades.

**Lo que puede mejorar:**
- Las definiciones de los tres casos no dicen sobre qué conjunto de entradas se toma el máximo, el mínimo o el promedio, ni que el tamaño n se mantiene fijo.
- En la sustitución faltan el caso base y la constante que hace que la hipótesis se cumpla.
- En el análisis línea a línea de insertion sort se listan los conteos, pero la frase "el tiempo total es:" queda sin resultado. Falta sumar y concluir `n²` y `n`.

## 3. Corrección de la implementación (17 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien de mayor a menor, no cambian la lista recibida, cuentan comparaciones entre elementos y no usan `sorted()` ni `sort()`. La mezcla de merge sort es propia y recursiva.
- Los tres generadores dan listas con valores distintos, del tamaño pedido, y los aleatorios usan semilla.
- Hay *type hints* y *docstrings* en casi todas las funciones.

**Lo que puede mejorar:**
- Las funciones `main` no tienen *docstring*.
- Hay detalles de PEP 8: espacios sobrantes al final de línea y falta de línea final en los archivos.

## 4. Calidad del análisis de las gráficas (13 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen y tienen título, ejes rotulados, leyenda y las curvas en los mismos ejes.
- En la Parte 4.2 concluye bien que merge sort conviene, describe cómo crece cada curva y lo conecta con `O(n²)` y `O(n log n)`.
- El concepto técnico recomienda merge sort, responde al servidor con un dato medido (2.8 s con n = 6400), extrapola a 1.200.000 registros (unas 27 horas para insertion sort) y habla de la memoria extra.

**Lo que puede mejorar:**
- En la Parte 3.2 se confunden los escenarios: dice que el caso A es el mejor y el B el promedio, pero la gráfica muestra lo contrario (B casi ordenado es el mejor y A aleatorio es el promedio). Las cifras citadas tampoco corresponden al escenario que nombra.
- La extrapolación debe decir claramente que es una estimación y con qué supuestos. Para merge sort solo dice "segundos", sin razonar con su crecimiento `n log n`.
- Al explicar los tamaños pequeños habla de memoria; la razón principal es el costo de crear listas y hacer llamadas recursivas.

## 5. Documentación y organización del informe (9 / 10)
**Lo que hizo bien:**
- La carpeta del laboratorio está en una ubicación válida y tiene todos los archivos y gráficas pedidos.
- El informe sigue el orden pedido, las imágenes se ven con ruta relativa y cada parte enlaza su código. Hay instrucciones de reproducción y 11 commits descriptivos.

**Lo que puede mejorar:**
- Las instrucciones usan el comando `py`, que solo existe en Windows; conviene indicar también `python`.

## ¿El código funciona?
Sí. Ambos scripts corren sin errores y generan las gráficas, y los dos algoritmos ordenan correctamente en las pruebas hechas.

## Para el próximo laboratorio
- Revise que lo que escribe coincida con lo que muestran sus gráficas (qué escenario es el mejor y cuál el promedio).
- Termine los cálculos escritos: sume los costos línea a línea y cierre la sustitución con caso base y constantes.
- Dé números concretos en los ejemplos propios (cuántos datos, cuánto tarda, qué límite se incumple).
- Declare las extrapolaciones como estimaciones y explique con qué fórmula las calculó.
- Antes de entregar, corra una revisión de estilo (PEP 8) y agregue *docstring* a todas las funciones.
