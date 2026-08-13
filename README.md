# Curso de Análisis de Algoritmos

- **Estudiante:** David Morales Vargas
- **Curso:** Análisis de Algoritmos - Virtual
- **Grupo:** 190304006-1
- **Profesor:** Santiago Suarez Cortes

Repositorio del curso para almacenar laboratorios, ejercicios de clase y scripts de benchmarks utilizados durante el semestre.

## Estructura

- `laboratorios/` — Contendrá los cinco informes evaluativos del curso.
- `ejercicios-clase/` — Código desarrollado durante las sesiones prácticas.
- `benchmarks/` — Scripts de  medición de tiempos de tiempos.

## Bloque de código

Ejemplo de un programa básico en Python:

```python
def mostrar_mensaje(opcion):
    if opcion == 1:
        print("Bienvenidos a Análisis de Algoritmos")
    elif opcion == 2:
        print("Hola, mundo")
    elif opcion == 3:
        print("Ups, creo que me equivoqué")
    else:
        print("Opción no válida")


def main():
    opcion = int(input("Ingrese un número (1-3): "))
    mostrar_mensaje(opcion)


if __name__ == "__main__":
    main()
```
