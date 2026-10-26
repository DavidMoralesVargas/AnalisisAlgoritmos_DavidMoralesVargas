"""Pruebas con assert de ListaEnlazada y TablaHash."""

import random

from estructuras import ListaEnlazada, TablaHash

ESTADOS = ("en bodega", "en reparto", "entregado")

# --- Busqueda exitosa e infructuosa en la lista ---
lista = ListaEnlazada()
lista.insertar(1000000010, "en bodega")
lista.insertar(1000000024, "en reparto")
lista.insertar(1000000017, "en bodega")
lista.insertar(1000000005, "entregado")
assert lista.buscar(1000000024) == "en reparto"
assert lista.buscar(1000000005) == "entregado"
assert lista.buscar(1000000099) is None
assert lista.tamano == 4
assert ListaEnlazada().buscar(1) is None  # lista vacia

# --- Busqueda exitosa e infructuosa en la tabla ---
tabla_ej = TablaHash(7)
for g, e in ((1000000010, "en bodega"), (1000000024, "en reparto"),
             (1000000017, "en bodega"), (1000000005, "entregado")):
    tabla_ej.insertar(g, e)
assert tabla_ej.buscar(1000000024) == "en reparto"
assert tabla_ej.buscar(1000000005) == "entregado"
assert tabla_ej.buscar(1000000099) is None

# --- Colision forzada con m = 7: 10, 24 y 17 caen en la casilla 3 ---
tabla = TablaHash(7)
for guia in (10, 24, 17):
    assert tabla.hash(guia) == 3
    tabla.insertar(guia, "en bodega")

assert tabla.buscar(10) == "en bodega"
assert tabla.buscar(24) == "en bodega"
assert tabla.buscar(17) == "en bodega"
assert tabla.buscar(99) is None
assert tabla.casillas[3].tamano == 3
longitud = 0
nodo = tabla.casillas[3].cabeza
while nodo is not None:
    longitud += 1
    nodo = nodo.siguiente
assert longitud == 3

# --- Factor de carga ---
assert tabla.factor_carga() == 3 / 7

# --- Veinte colecciones aleatorias: lista y tabla coinciden ---
azar = random.Random(2026)
for _ in range(20):
    n = azar.randint(1, 300)
    guias = azar.sample(range(10**9, 10**10), n)
    m = azar.choice((1, 7, 31, 101, 211))
    lista_a = ListaEnlazada()
    tabla_a = TablaHash(m)
    for guia in guias:
        estado = azar.choice(ESTADOS)
        lista_a.insertar(guia, estado)
        tabla_a.insertar(guia, estado)
    assert tabla_a.factor_carga() == n / m

    for guia in guias:  # existentes
        assert lista_a.buscar(guia) is not None
        assert lista_a.buscar(guia) == tabla_a.buscar(guia)

    existentes = set(guias)
    inexistentes = 0
    while inexistentes < 50:  # inexistentes
        guia = azar.randint(10**9, 10**10 - 1)
        if guia in existentes:
            continue
        assert lista_a.buscar(guia) is None
        assert tabla_a.buscar(guia) is None
        inexistentes += 1

print("Todas las pruebas pasaron.")
