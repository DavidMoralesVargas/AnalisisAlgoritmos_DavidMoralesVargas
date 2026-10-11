# Laboratorio evaluativo 02 — Dividir y vencer

**Nombre completo:** DAVID MORALES VARGAS

## Instrucciones para reproducir el experimento

1. Ubicarse en la raíz del repositorio del curso y crear el entorno virtual (solo la primera vez):
   ```bash
   python -m venv venv
   ```
   ó (en Windows, si `python` no está en el PATH)
   ```bash
   py -m venv venv
   ```
2. Activar el entorno virtual:
   - Linux/macOS: `source venv/bin/activate`
   - Windows: `venv\Scripts\activate`
3. Instalar las dependencias (cómo `matplotlib`):
   ```bash
   pip install -r requirements.txt
   ```
4. Entrar a la carpeta del laboratorio:
   ```bash
   cd laboratorios/lab2-divide-y-vencer
   ```
5. Ejecutar las pruebas (el scrip termina imprimiendo `Todas las pruebas pasaron.`):
   ```bash
   python pruebas.py  
   ```
   ó `py pruebas.py` (Para Windows)
6. Ejecutar la medición (imprime los tiempos y genera `graficas/tiempo_vs_n.png`):
   ```bash
   python medicion.py
   ```
   ó `py medicion.py` (Para Windows)

---

## Parte 1: Implementar y verificar las dos soluciones

Código de esta parte: [`subarreglo.py`](subarreglo.py) y [`pruebas.py`](pruebas.py)

Las tres funciones están en [`subarreglo.py`](subarreglo.py):

- [`subarreglo_fuerza_bruta`](subarreglo.py#L4-L29): prueba todos los pares de días `(i, j)` acumulando la suma dentro del ciclo.
- [`suma_cruzada`](subarreglo.py#L32-L67): barrido lineal desde el punto medio hacia cada lado, para el tramo que incluye al menos un día de cada mitad.
- [`subarreglo_maximo`](subarreglo.py#L70-L100): divide y vencerás; resuelve los casos izquierdo, derecho y cruzado y devuelve el mejor de los tres, sin llamar a la fuerza bruta.

**Cómo se verificó.** El script [`pruebas.py`](pruebas.py) usa `assert` (instrucción en Python que permite comprobar que una condición proporcionada sea verdadera. Se usa para hacer pruebas unitarias) y compara siempre la suma, no los índices. Casos cubiertos:

- La serie de ocho días de la situación problema (suma `17`, días 2 a 7).
- Una serie de un solo elemento (positivo y negativo).
- Una serie con todos los valores negativos (el mejor tramo es el elemento menos negativo).
- Una serie con todos los valores positivos (el mejor tramo es la serie completa).
- Un caso donde el mejor tramo cruza el punto medio (`[-5, 2, 3, 4, 5, -6]`, tramo de los índices 1 a 4).
- Que las funciones no modifican la lista recibida.
- 30 listas aleatorias (con semilla fija), en las que ambas funciones deben dar la misma suma.

---

## Parte 2: Medir y graficar

Código de esta parte: [`medicion.py`](medicion.py)

**Cómo se midió:**

- Tamaños de entrada ([`TAMANOS`](medicion.py#L12)): 10, 50, 100, 500, 1000, 2000, 4000 y 8000.
- Datos generados por [`generar_datos`](medicion.py#L18-L28) con semilla fija ([`SEMILLA = 42`](medicion.py#L13)), enteros entre -100 y 100. Para cada tamaño se usa la **misma lista** en ambos algoritmos.
- Solo se cronometra la llamada al algoritmo, con `time.perf_counter()`; la generación de datos queda fuera.
- Cada medición se repite 3 veces ([`REPETICIONES`](medicion.py#L14)) y se reporta la **mediana**.
- Dentro del propio experimento ([`medir`](medicion.py#L47-L80)) se verifica con `assert` que ambos algoritmos devuelven la misma suma en cada tamaño.

![Tiempo de ejecución vs. tamaño de entrada: fuerza bruta y divide y vencerás](graficas/tiempo_vs_n.png)

**Tiempos medidos (segundos, mediana de 3 repeticiones):**

| n | Fuerza bruta (s) | Divide y vencerás (s) |
|---:|---:|---:|
| 10 | 0.000023s | 0.000049s |
| 50 | 0.000122s | 0.000090s |
| 100 | 0.000459s | 0.000198s |
| 500 | 0.019468s | 0.001141s |
| 1000 | 0.126704s | 0.007267s |
| 2000 | 0.426440s | 0.010730s |
| 4000 | 1.662596s | 0.023872s |
| 8000 | 7.103474s | 0.047261s |

---

## Parte 3: Análisis

### 1. Recurrencia

Código relacionado: [`subarreglo_maximo`](subarreglo.py#L70-L100), [`suma_cruzada`](subarreglo.py#L32-L67) y [`subarreglo_fuerza_bruta`](subarreglo.py#L4-L29).

La función `subarreglo_maximo` realiza dos llamadas recursivas, una por cada mitad, cada una sobre n/2 elementos. La función `suma_cruzada` no es recursiva: los dos barridos que hace desde el punto medio recorren el rango una sola vez, entonces eso significa un Θ(n). Combinar es comparar las tres sumas, Θ(1), así que:

`T(n) = 2T(n/2) + Θ(n)`

Usando el método maestro: a = 2, b = 2, `n^(log_2 2) = n`. Como f(n) = Θ(n) = Θ(n^(log_b a)), se cumple el caso 2 y T(n) = Θ(n log n).

La fuerza bruta tiene un ciclo externo sobre i, que son los n valores, y uno interno sobre j desde el valor de la variable i hasta n-1, que acumula la suma en Θ(1) por paso. El total es Σ(n-i) = n(n+1)/2 = Θ(n²).


### 2. Lo medido contra lo esperado

Datos: [gráfica y tabla de la Parte 2](#parte-2-medir-y-graficar).

La curva de fuerza bruta crece de forma acelerada, siendo de 0,127 segundos con un n = 1000 y 7,10 segundos con un n = 8000. La de divide y vencerás, en cambio, apenas llega a 0,047 segundos con un n = 8000. Se puede visualizar como al duplicar n de 4000 a 8000, la fuerza bruta se multiplicó por 7,103/1,663 = 4,27 (Θ(n²) predicción 4) y divide y vencerás por 0,047/0,0239 = 1,98 (Θ(n log n) predicción 2,17). De 2000 a 4000 los factores fueron aproximadamente 3,9 y 2,23. Para ambos casos coinciden con los datos teóricos. El tramo de 1000 a 2000 dio 3,37 y 1,48, más lejos de lo esperado, se atribuye a ruido en mediciones de pocos milisegundos.

### 3. Tamaños pequeños

Datos: [gráfica y tabla de la Parte 2](#parte-2-medir-y-graficar).

Sí existe un tamaño en el que divide y vencerás empieza a ganar. En n = 10 divide y vencerás es más lento ya que tiene 49 microsegundos frente a 23 microsegundos. En n = 50 ya gana ya que tiene 90 microsegundos frente a 122 microsegundos y desde ahí en forma general empieza a ganar en todos los tamaños de las medidas, con una ventaja que crece alrededor de 2,3 veces con un n = 100, 17 veces con un n = 500 y 150 veces con un n = 8000. El cruce queda entre n = 10 y n = 50. Aparece tarde porque la recursión paga un costo constante que la fuerza bruta no tiene, por las llamadas a la función, las tuplas de retorno y un caso cruzado en cada nivel. Para el caso de la fuerza bruta solo hace dos ciclos simples. Entonces teniendo un n pequeño, la diferencia entre n² y n log n todavía es pequeña y esas constantes son las que dominan. Como en n = 10 los tiempos son de microsegundos, esa medición también tiene más ruido.

### 4. ¿Cuándo conviene dividir?

Para comparar: [`subarreglo_maximo`](subarreglo.py#L70-L100) (donde combinar cuesta un barrido lineal).

Para hallar el máximo de un arreglo, combinar cuesta una comparación: `T(n) = 2T(n/2) + Θ(1)`. Con n^(log_2 2) = n, f(n) = Θ(1) crece más lento (caso 1), y T(n) = Θ(n). Recorrer el arreglo una vez también es Θ(n), así que dividir no mejora la complejidad y lo único que hace realmente es agregar overhead de la pila de llamadas y de copiar sublistas. En el subarreglo máximo sí conviene: la alternativa es Θ(n²) y combinar cuesta Θ(n), mucho menos que lo que la fuerza bruta repite. Hay que tener en cuenta que dividir solo conviene cuando la recurrencia da una complejidad menor que la alternativa directa; si no, lo único que se logrará es un gasto innecesario de tiempo y memoria.

### 5. Concepto para la gerente

Datos: [gráfica y tabla de la Parte 2](#parte-2-medir-y-graficar).

Recomiendo usar divide y vencerás. Esto es una estimación, no una medición: se parte de n = 8000, el mayor tamaño medido, y se supone que el crecimiento observado se mantiene a mayor escala. El factor de escala es 10^6/8000 = 125.

- **Fuerza bruta** (complejidad Θ(n²)): el tiempo se multiplica por 125², que es igual a 15.625. Entonces 7,10 s × 15.625 ≈ 111.000 s, lo que equivale a unas 31 horas.
- **Divide y vencerás** (complejidad Θ(n log n)): el tiempo se multiplica por 125 × log₂(10^6) / log₂(8000) = 125 × 19,9/13, aproximadamente igual a 192. Entonces 0,0473 s × 192 ≈ 9 s, que es excesivamente menor al resultado estimado del algoritmo de fuerza bruta.

