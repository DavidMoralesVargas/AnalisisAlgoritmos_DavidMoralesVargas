"""Generadores de lotes de registros para los escenarios de Tamiza."""

import random


def generar_aleatorio(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote de n registros en orden aleatorio (escenario A).

    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio, para que el
            experimento sea reproducible.

    Returns:
        Lista de n indices de riesgo enteros distintos, desordenada.
    """
    rng = random.Random(semilla)
    lote = list(range(n))
    rng.shuffle(lote)
    return lote


def generar_casi_ordenado(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote casi ordenado: 98% ordenado y 2% al final (escenario B).

    Tamiza ordena de mayor a menor, asi que "casi ordenado" aqui significa
    casi descendente: el primer 98% ya queda en orden descendente y el 2%
    restante llega desordenado al final.

    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio.

    Returns:
        Lista de n indices de riesgo enteros distintos, con el primer
        98% en el orden que el algoritmo produce (descendente) y el 2%
        restante desordenado al final.
    """
    rng = random.Random(semilla)
    corte = int(n * 0.98)

    ordenado = list(range(n, n - corte, -1))
    resto = list(range(n - corte, 0, -1))
    rng.shuffle(resto)

    return ordenado + resto


def generar_inverso(n: int) -> list[int]:
    """Genera un lote en el orden exactamente contrario (escenario C).

    Tamiza ordena de mayor a menor, asi que el peor caso (el orden
    exactamente contrario al resultado) es la lista en orden ASCENDENTE:
    cada elemento nuevo debe desplazarse contra todos los anteriores.

    Args:
        n: cantidad de registros del lote.

    Returns:
        Lista de n indices de riesgo enteros distintos, en el orden
        inverso al que el algoritmo debe producir (ascendente).
    """
    return list(range(1, n + 1))