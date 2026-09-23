"""Parte 3: peor caso, mejor caso y caso promedio de insertion sort.

Ejecuta insertion_sort sobre tres escenarios de entrada (aleatorio, casi
ordenado y orden inverso), para varios tamanos de entrada, midiendo tiempo
de ejecucion y numero de comparaciones. Genera dos graficas en graficas/.
"""

import time
from pathlib import Path

import matplotlib.pyplot as plt

from algoritmos import insertion_sort
from datos import generar_aleatorio, generar_casi_ordenado, generar_inverso

# Al menos siete tamanos de entrada, como pide el enunciado.
TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]

# Un generador por escenario. Todos reciben n; los que usan aleatoriedad
# aceptan ademas una semilla, ya fijada por defecto en datos.py.
ESCENARIOS = {
    "A - Aleatorio": generar_aleatorio,
    "B - Casi ordenado": generar_casi_ordenado,
    "C - Orden inverso": generar_inverso,
}

CARPETA_GRAFICAS = Path("graficas")


def medir() -> dict[str, dict[str, list[float]]]:
    """Mide tiempo y comparaciones de insertion_sort en los tres escenarios.

    Para cada escenario y cada tamano de entrada, genera el lote (fuera del
    cronometro), y mide unicamente la llamada a insertion_sort.

    Returns:
        Un diccionario indexado por nombre de escenario, cada uno con las
        listas "tiempos" y "comparaciones", en el mismo orden que TAMANOS.
    """
    resultados = {
        nombre: {"tiempos": [], "comparaciones": []} for nombre in ESCENARIOS
    }

    for nombre, generador in ESCENARIOS.items():
        for n in TAMANOS:
            lote = generador(n)  # generacion de datos: fuera del cronometro

            inicio = time.perf_counter()
            _, comparaciones = insertion_sort(lote)
            duracion = time.perf_counter() - inicio

            resultados[nombre]["tiempos"].append(duracion)
            resultados[nombre]["comparaciones"].append(comparaciones)

            print(
                f"{nombre:<20} | n={n:>6} | "
                f"t={duracion:.6f}s | comparaciones={comparaciones}"
            )

    return resultados


def graficar_comparaciones(
    resultados: dict[str, dict[str, list[float]]], carpeta: Path
) -> None:
    """
    Genera parte3_comparaciones.png: comparaciones vs. tamano de entrada.

    Args:
        resultados: Un diccionario indexado por el nombre del escenario, 
            que contiene las listas de "comparaciones" medidas.
        carpeta: Objeto Path que representa el directorio donde se 
            guardará la gráfica.

    Returns:
        None. La función guarda el archivo en disco y no retorna valores.
    """
    plt.figure()
    for nombre, datos in resultados.items():
        plt.plot(TAMANOS, datos["comparaciones"], marker="o", label=nombre)

    plt.title("Insertion sort: comparaciones vs. tamano de entrada")
    plt.xlabel("Tamano de entrada (n)")
    plt.ylabel("Numero de comparaciones")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig(carpeta / "parte3_comparaciones.png", dpi=150, bbox_inches="tight")
    plt.close()


def graficar_tiempo(
    resultados: dict[str, dict[str, list[float]]], carpeta: Path
) -> None:
    """
    Genera parte3_tiempo.png: tiempo de ejecucion vs. tamano de entrada.

    Args:
        resultados: Un diccionario indexado por el nombre del escenario, 
            que contiene las listas de "tiempos" medidos.
        carpeta: Objeto Path que representa el directorio donde se 
            guardará la gráfica.

    Returns:
        None. La función guarda el archivo en disco y no retorna valores.
    """
    plt.figure()
    for nombre, datos in resultados.items():
        plt.plot(TAMANOS, datos["tiempos"], marker="o", label=nombre)

    plt.title("Insertion sort: tiempo de ejecucion vs. tamano de entrada")
    plt.xlabel("Tamano de entrada (n)")
    plt.ylabel("Tiempo (segundos)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig(carpeta / "parte3_tiempo.png", dpi=150, bbox_inches="tight")
    plt.close()


def main() -> None:
    CARPETA_GRAFICAS.mkdir(parents=True, exist_ok=True)

    resultados = medir()

    graficar_comparaciones(resultados, CARPETA_GRAFICAS)
    graficar_tiempo(resultados, CARPETA_GRAFICAS)

    print(f"\nGraficas guardadas en: {CARPETA_GRAFICAS.resolve()}")


if __name__ == "__main__":
    main()