"""Parte 4.2: validacion experimental de insertion sort vs. merge sort.

Mide el tiempo de ejecucion de ambos algoritmos sobre el escenario A
(aleatorio) de Tamiza, para los mismos tamanos de entrada de la Parte 3,
y genera la grafica comparativa parte4_tiempo.png.
"""

import time
from pathlib import Path

import matplotlib.pyplot as plt

from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio

# Mismos tamanos que en la Parte 3, para que las mediciones sean comparables.
TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]

CARPETA_GRAFICAS = Path("graficas")


def medir() -> dict[str, list[float]]:
    """Mide el tiempo de insertion_sort y merge_sort sobre el escenario A.

    Para cada tamano, genera un unico lote aleatorio (fuera del cronometro)
    y mide, por separado, la llamada a cada algoritmo sobre ese mismo lote.

    Returns:
        Un diccionario con las listas de tiempos de cada algoritmo, en el
        mismo orden que TAMANOS.
    """
    tiempos = {"Insertion sort": [], "Merge sort": []}

    for n in TAMANOS:
        lote = generar_aleatorio(n)  # generacion de datos: fuera del cronometro

        inicio = time.perf_counter()
        insertion_sort(lote)
        t_insertion = time.perf_counter() - inicio

        inicio = time.perf_counter()
        merge_sort(lote)
        t_merge = time.perf_counter() - inicio

        tiempos["Insertion sort"].append(t_insertion)
        tiempos["Merge sort"].append(t_merge)

        print(
            f"n={n:>6} | insertion_sort={t_insertion:.6f}s | "
            f"merge_sort={t_merge:.6f}s"
        )

    return tiempos


def graficar(tiempos: dict[str, list[float]], carpeta: Path) -> None:
    """Genera parte4_tiempo.png: tiempo de ejecucion vs. tamano de entrada.

    Args:
        tiempos: Diccionario con los nombres de los algoritmos como claves 
            y las listas de tiempos de ejecución medidos como valores.
        carpeta: Objeto Path que indica el directorio donde se guardará 
            la gráfica generada.

    Returns:
        None. La función guarda la imagen en disco y no retorna valores.
    """
    plt.figure()
    for nombre, valores in tiempos.items():
        plt.plot(TAMANOS, valores, marker="o", label=nombre)

    plt.title("Insertion sort vs. merge sort: tiempo de ejecucion (escenario A)")
    plt.xlabel("Tamano de entrada (n)")
    plt.ylabel("Tiempo de ejecucion (segundos)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig(carpeta / "parte4_tiempo.png", dpi=150, bbox_inches="tight")
    plt.close()


def main() -> None:
    CARPETA_GRAFICAS.mkdir(parents=True, exist_ok=True)

    tiempos = medir()
    graficar(tiempos, CARPETA_GRAFICAS)

    print(f"\nGrafica guardada en: {CARPETA_GRAFICAS.resolve()}")


if __name__ == "__main__":
    main()