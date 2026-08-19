"""Clasificador de años bisiestos.
 
Complete las funciones siguiendo la especificación de cada docstring.
"""
 
 
def es_bisiesto(anio: int) -> bool:
    """Determina si un año es bisiesto.
 
    Un año es bisiesto si es divisible por 4, excepto los años
    divisibles por 100 que no lo sean también por 400.
 
    Args:
        anio: año a evaluar (número entero).
 
    Returns:
        True si el año es bisiesto, False en caso contrario.
    """
    # TODO: implemente la lógica usando if / elif / else.
    if anio % 400 == 0:
        return True
    elif anio % 100 == 0:
        return False
    elif anio % 4 == 0:
        return True
    else:
        return False
 
 
def leer_anios() -> list[int]:
    """Solicita al usuario una lista de años separados por comas.
 
    Debe reintentar mientras la entrada no se pueda convertir a enteros
    (use try / except para capturar entradas inválidas).
 
    Returns:
        Lista de años como enteros.
    """
    # TODO: implemente la lectura y validación.
    while True:
        try:
            entrada = input("Ingrese una lista de años separados por comas: ")

            anios = [int(a.strip()) for a in entrada.split(",") if a.strip()]
            
            if not anios:
                print("Lista vacía. Debe ingresar al menos un año")
                continue
                
            return anios
        except ValueError:
            print("Error. Debe ingresar una lista de número separados por coma")
 
 
def main() -> None:
    """Punto de entrada del script."""
    # TODO: use leer_anios(), filtre los años bisiestos con una
    # comprensión de listas, e imprima un resumen que incluya al menos
    # la lista de años bisiestos y cuántos hay.
    print("--- AÑOS BISIESTOS ---")
    anios = leer_anios()
    
    bisiestos_encontrados = [anio for anio in anios if es_bisiesto(anio)]
    
    print("\n--- RESUMEN ---")
    
    print(f"Años ingresados: {anios}")

    if bisiestos_encontrados:
        print(f"Los años bisiestos encontrados son: {bisiestos_encontrados}")
        print(f"La cantidad de años bisiesto: {len(bisiestos_encontrados)}")
    else:
        print("No se encontró ningún año bisiesto en la lista.")
 
 
if __name__ == "__main__":
    main()