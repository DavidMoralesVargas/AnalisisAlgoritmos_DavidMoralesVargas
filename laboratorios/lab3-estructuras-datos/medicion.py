"""Experimentos de medicion: lista enlazada frente a tabla hash."""

import os
import random
import time

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

from estructuras import ListaEnlazada, TablaHash  # noqa: E402

ESTADOS = ("en bodega", "en reparto", "entregado")
CARPETA_GRAFICAS = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "graficas"
)
BUSQUEDAS = 200
REPETICIONES_LISTA = 3
REPETICIONES_TABLA = 50
SEMILLA = 7


def generar_guias_inexistentes(
    existentes: set[int], cantidad: int, semilla: int = 7
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.

    Args:
        existentes: guias almacenadas en las estructuras.
        cantidad: cuantas guias inexistentes generar.
        semilla: semilla del generador, para reproducir la medicion.

    Returns:
        Una lista con `cantidad` guias que no pertenecen a `existentes`.
    """
    azar = random.Random(semilla)
    inexistentes: list[int] = []
    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)
    return inexistentes


def es_primo(numero: int) -> bool:
    """Indica si un entero es primo (division de prueba).

    Args:
        numero: entero a evaluar.

    Returns:
        True si el numero es primo, False en caso contrario.
    """
    if numero < 2:
        return False
    divisor = 2
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 1
    return True


def primo_cercano(objetivo: int) -> int:
    """Devuelve el primo mas cercano a un valor (el menor en caso de empate).

    Args:
        objetivo: valor alrededor del cual se busca el primo.

    Returns:
        El primo mas cercano a `objetivo`.
    """
    distancia = 0
    while True:
        if es_primo(objetivo - distancia):
            return objetivo - distancia
        if es_primo(objetivo + distancia):
            return objetivo + distancia
        distancia += 1


def generar_guias_existentes(n: int, semilla: int = SEMILLA) -> list[int]:
    """Genera n guias distintas de diez digitos con semilla fija.

    Args:
        n: cantidad de guias a generar.
        semilla: semilla del generador, para reproducir la medicion.

    Returns:
        Lista de n enteros distintos de diez digitos.
    """
    azar = random.Random(semilla + n)
    return azar.sample(range(10**9, 10**10), n)


def construir(
    guias: list[int], m: int, azar: random.Random
) -> tuple[ListaEnlazada, TablaHash]:
    """Construye una lista y una tabla con las mismas guias y estados.

    Args:
        guias: guias a insertar.
        m: numero de casillas de la tabla.
        azar: generador usado para asignar estados.

    Returns:
        La lista enlazada y la tabla hash ya pobladas.
    """
    lista = ListaEnlazada()
    tabla = TablaHash(m)
    for guia in guias:
        estado = azar.choice(ESTADOS)
        lista.insertar(guia, estado)
        tabla.insertar(guia, estado)
    return lista, tabla


def verificar(
    lista: ListaEnlazada, tabla: TablaHash, guias: list[int]
) -> None:
    """Verifica que lista y tabla coincidan para una muestra de guias.

    Args:
        lista: lista enlazada poblada.
        tabla: tabla hash poblada con las mismas guias.
        guias: guias existentes de las que se toma la muestra.

    Returns:
        None.
    """
    muestra = random.Random(SEMILLA).sample(guias, min(100, len(guias)))
    for guia in muestra:
        estado = lista.buscar(guia)
        assert estado is not None
        assert estado == tabla.buscar(guia)


def tiempo_medio(
    estructura: ListaEnlazada | TablaHash,
    consultas: list[int],
    repeticiones: int,
) -> float:
    """Mide el tiempo medio por busqueda (solo cronometra las busquedas).

    Se repite la medicion `repeticiones` veces y se conserva la menor,
    para reducir el ruido del sistema operativo.

    Args:
        estructura: lista o tabla donde se busca.
        consultas: guias a buscar.
        repeticiones: veces que se repite la tanda de busquedas.

    Returns:
        Tiempo medio por busqueda, en microsegundos.
    """
    mejor = float("inf")
    for _ in range(repeticiones):
        inicio = time.perf_counter()
        for guia in consultas:
            estructura.buscar(guia)
        total = time.perf_counter() - inicio
        mejor = min(mejor, total)
    return mejor / len(consultas) * 1e6


def experimento_a(valores_n: list[int]) -> list[tuple[int, int, float, float]]:
    """Mide lista frente a tabla variando n, con alfa cercano a 2.

    Args:
        valores_n: numeros de guias a probar.

    Returns:
        Filas (n, m, microsegundos lista, microsegundos tabla).
    """
    filas: list[tuple[int, int, float, float]] = []
    for n in valores_n:
        guias = generar_guias_existentes(n)
        m = primo_cercano(n // 2)
        lista, tabla = construir(guias, m, random.Random(SEMILLA))
        verificar(lista, tabla, guias)
        consultas = generar_guias_inexistentes(set(guias), BUSQUEDAS, SEMILLA)
        t_lista = tiempo_medio(lista, consultas, REPETICIONES_LISTA)
        t_tabla = tiempo_medio(tabla, consultas, REPETICIONES_TABLA)
        filas.append((n, m, t_lista, t_tabla))
        print(f"n={n:>7} m={m:>6} alfa={n / m:5.2f} "
              f"lista={t_lista:12.3f} us  tabla={t_tabla:8.3f} us")
    return filas


def experimento_b(
    n: int, alfas: list[float]
) -> list[tuple[float, int, float]]:
    """Mide la tabla con n fijo variando el factor de carga.

    Args:
        n: numero de guias fijo.
        alfas: factores de carga objetivo.

    Returns:
        Filas (alfa real, m, microsegundos por busqueda en la tabla).
    """
    guias = generar_guias_existentes(n)
    consultas = generar_guias_inexistentes(set(guias), BUSQUEDAS, SEMILLA)
    filas: list[tuple[float, int, float]] = []
    for alfa in alfas:
        m = primo_cercano(round(n / alfa))
        lista, tabla = construir(guias, m, random.Random(SEMILLA))
        verificar(lista, tabla, guias)
        t_tabla = tiempo_medio(tabla, consultas, REPETICIONES_TABLA)
        filas.append((tabla.factor_carga(), m, t_tabla))
        print(f"n={n} m={m:>6} alfa={tabla.factor_carga():6.2f} "
              f"tabla={t_tabla:8.3f} us")
    return filas


def graficar_a(filas: list[tuple[int, int, float, float]]) -> None:
    """Grafica lista frente a tabla y guarda lista_vs_tabla.png.

    Args:
        filas: resultados del experimento A.

    Returns:
        None.
    """
    ns = [f[0] for f in filas]
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(ns, [f[2] for f in filas], "o-", label="Lista enlazada")
    ax.plot(ns, [f[3] for f in filas], "s-", label="Tabla hash (alfa ~ 2)")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_title("Busqueda de guia inexistente: lista frente a tabla hash")
    ax.set_xlabel("Numero de guias n (escala log)")
    ax.set_ylabel("Tiempo medio por busqueda (microsegundos, escala log)")
    ax.grid(True, which="both", alpha=0.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig(os.path.join(CARPETA_GRAFICAS, "lista_vs_tabla.png"), dpi=150)
    plt.close(fig)


def graficar_b(n: int, filas: list[tuple[float, int, float]]) -> None:
    """Grafica tiempo frente a alfa y guarda tiempo_vs_alfa.png.

    Args:
        n: numero de guias usado en el experimento.
        filas: resultados del experimento B.

    Returns:
        None.
    """
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot([f[0] for f in filas], [f[2] for f in filas], "o-",
            label=f"Tabla hash, n = {n}")
    ax.set_title("Efecto del factor de carga en la busqueda (inexistentes)")
    ax.set_xlabel("Factor de carga alfa = n / m (adimensional)")
    ax.set_ylabel("Tiempo medio por busqueda (microsegundos)")
    ax.grid(True, alpha=0.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig(os.path.join(CARPETA_GRAFICAS, "tiempo_vs_alfa.png"), dpi=150)
    plt.close(fig)


def main() -> None:
    """Ejecuta los experimentos A y B y genera las dos graficas.

    Returns:
        None.
    """
    os.makedirs(CARPETA_GRAFICAS, exist_ok=True)
    print("Experimento A")
    filas_a = experimento_a([100, 500, 1000, 5000, 20000, 50000, 100000])
    graficar_a(filas_a)
    print("Experimento B")
    n_b = 20000
    filas_b = experimento_b(n_b, [0.25, 0.5, 1, 2, 4, 6, 8, 10])
    graficar_b(n_b, filas_b)
    print(f"Graficas guardadas en {CARPETA_GRAFICAS}")


if __name__ == "__main__":
    main()
