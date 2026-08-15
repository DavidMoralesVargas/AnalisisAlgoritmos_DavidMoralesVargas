# ANTES
# def CalcularPromedio(Lista):
#     s=0
#     for x in Lista:
#      s=s+x
#     return s/len(Lista)
 
# l=[1,2,3,4,5]
# print(CalcularPromedio(l))

#DESPUÉS
def calcular_promedio(numeros: list[int]) -> float:
    """
    Función que calcula el promedio de una lista de números.

    Args:
        numeros (list[int]): La lista de números enteros.

    Returns:
        float: El promedio de los elementos que se calculan de la lista.
    """
    suma = 0
    for numero in numeros:
        suma += numero
        
    return suma / len(numeros)


def main() -> None:
    """
    Función main que ejecuta el método para calcular el promedio.

    Args:
        None: No recibe atributos.

    Returns:
        None: No devuelve una variable
    """
    numeros_prueba = [213, 123, 41, 41, 52]
    print(calcular_promedio(numeros_prueba))


if __name__ == "__main__":
    main()



