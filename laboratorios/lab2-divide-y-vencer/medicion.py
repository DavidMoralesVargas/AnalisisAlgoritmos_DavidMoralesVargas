"""Medicion del tiempo de fuerza bruta vs. divide y venceras."""
 
import random
import statistics
import time
from collections.abc import Callable
from pathlib import Path
from typing import Any
 
import matplotlib.pyplot as plt
 
from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo
 
TAMANOS = [10, 50, 100, 500, 1000, 2000, 4000, 8000]
SEMILLA = 42
REPETICIONES = 3
CARPETA_GRAFICAS = Path("graficas")
 
 
def generar_datos(n: int) -> list[int]:
    """Genera n variaciones enteras entre -100 y 100 con semilla fija.
 
    Args:
        n: cantidad de valores a generar.
 
    Returns:
        Lista de n enteros reproducible gracias a la semilla fija.
    """
    rng = random.Random(SEMILLA)
    return [rng.randint(-100, 100) for _ in range(n)]
 
 
def cronometrar(
    funcion: Callable[..., tuple[int, int, float]], *argumentos: Any
) -> tuple[float, tuple[int, int, float]]:
    """Mide una llamada con time.perf_counter().
 
    Args:
        funcion: algoritmo a medir.
        *argumentos: argumentos que recibe el algoritmo.
 
    Returns:
        Una tupla (segundos, resultado) con la duracion de la llamada y
        lo que devolvio el algoritmo.
    """
    inicio = time.perf_counter()
    resultado = funcion(*argumentos)
    return time.perf_counter() - inicio, resultado
 
 
def medir() -> dict[str, list[float]]:
    """Mide ambos algoritmos para cada tamano de entrada.
 
    Para cada n se genera una unica lista (fuera del cronometro) y se
    usa la misma para ambos algoritmos. Cada medicion se repite y se
    guarda la mediana. Verifica que ambos den la misma suma.
 
    Returns:
        Un diccionario con la lista de tiempos (segundos) de cada
        algoritmo, en el mismo orden que TAMANOS.
    """
    tiempos = {"Fuerza bruta": [], "Divide y venceras": []}
 
    for n in TAMANOS:
        datos = generar_datos(n)
        muestras_fb = []
        muestras_dd = []
 
        for _ in range(REPETICIONES):
            t_fb, res_fb = cronometrar(subarreglo_fuerza_bruta, datos)
            t_dd, res_dd = cronometrar(subarreglo_maximo, datos, 0, n - 1)
            assert res_fb[2] == res_dd[2], f"Sumas distintas con n={n}"
            muestras_fb.append(t_fb)
            muestras_dd.append(t_dd)
 
        tiempos["Fuerza bruta"].append(statistics.median(muestras_fb))
        tiempos["Divide y venceras"].append(statistics.median(muestras_dd))
 
        print(
            f"n={n:>6} | fuerza bruta={tiempos['Fuerza bruta'][-1]:.6f}s | "
            f"divide y venceras={tiempos['Divide y venceras'][-1]:.6f}s"
        )
 
    return tiempos
 
 
def graficar(tiempos: dict[str, list[float]], carpeta: Path) -> None:
    """Genera tiempo_vs_n.png con ambas curvas en los mismos ejes.
 
    Args:
        tiempos: tiempos medidos de cada algoritmo, indexados por nombre.
        carpeta: directorio donde se guarda la grafica.
 
    Returns:
        None. La grafica se guarda en disco.
    """
    plt.figure()
    for nombre, valores in tiempos.items():
        plt.plot(TAMANOS, valores, marker="o", label=nombre)
 
    plt.title("Subarreglo maximo: tiempo de ejecucion vs. tamano de entrada")
    plt.xlabel("Tamano de entrada n (numero de dias)")
    plt.ylabel("Tiempo de ejecucion (segundos)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig(carpeta / "tiempo_vs_n.png", dpi=150, bbox_inches="tight")
    plt.close()
 
 
def main() -> None:
    """Ejecuta el experimento completo y guarda la grafica.
 
    Returns:
        None. Imprime los tiempos por consola y guarda la grafica.
    """
    CARPETA_GRAFICAS.mkdir(parents=True, exist_ok=True)
    tiempos = medir()
    graficar(tiempos, CARPETA_GRAFICAS)
    print(f"\nGrafica guardada en: {CARPETA_GRAFICAS.resolve()}")
 
 
if __name__ == "__main__":
    main()