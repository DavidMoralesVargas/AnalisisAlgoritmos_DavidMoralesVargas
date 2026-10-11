"""Pruebas de subarreglo.py: casos conocidos y listas aleatorias."""

import random

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


def suma_dd(serie: list[float]) -> float:
    """Devuelve la suma del mejor tramo hallado por divide y venceras.

    Args:
        serie: variacion diaria de caja. Tiene al menos un elemento.

    Returns:
        La suma maxima de un tramo contiguo de la serie completa,
        calculada con subarreglo_maximo.
    """
    return subarreglo_maximo(serie, 0, len(serie) - 1)[2]


# 1. Serie de ocho dias de la situacion problema (suma 17, dias 2 a 7).
serie = [-3, 5, -2, 8, -6, 3, 9, -4]
assert subarreglo_fuerza_bruta(serie)[2] == 17
assert suma_dd(serie) == 17

# 2. Un solo elemento.
assert subarreglo_fuerza_bruta([7])[2] == 7
assert suma_dd([7]) == 7
assert suma_dd([-7]) == -7

# 3. Todos negativos: el mejor tramo es el elemento menos negativo.
negativos = [-8, -3, -5, -1, -9]
assert subarreglo_fuerza_bruta(negativos)[2] == -1
assert suma_dd(negativos) == -1

# 4. Todos positivos: el mejor tramo es la serie completa.
positivos = [2, 4, 1, 6, 3]
assert subarreglo_fuerza_bruta(positivos)[2] == 16
assert suma_dd(positivos) == 16

# 5. Caso donde el mejor tramo cruza el punto medio (medio = 2).
cruzado = [-5, 2, 3, 4, 5, -6]
assert subarreglo_fuerza_bruta(cruzado)[2] == 14
assert suma_dd(cruzado) == 14
assert subarreglo_maximo(cruzado, 0, len(cruzado) - 1)[:2] == (1, 4)

# 6. Las funciones no modifican la lista recibida.
copia = serie.copy()
subarreglo_fuerza_bruta(serie)
subarreglo_maximo(serie, 0, len(serie) - 1)
assert serie == copia

# 7. Treinta listas aleatorias
rng = random.Random(123)
for _ in range(30):
    n = rng.randint(1, 200)
    lista = [rng.randint(-100, 100) for _ in range(n)]
    assert subarreglo_fuerza_bruta(lista)[2] == suma_dd(lista)

print("Todas las pruebas pasaron.")
