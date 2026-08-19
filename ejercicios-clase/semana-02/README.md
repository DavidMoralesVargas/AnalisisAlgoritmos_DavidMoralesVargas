# Explicación del laboratorio 2

Ejecución del entorno virtual para trabajos en conjunto usando Python.

## Asegurar que estamos en la raíz del proyecto
No movernos a alguna parte del proyecto con el comando 'cd'. Nos debemos mantener en la raíz del proyecto (curso-analisis-algoritmo)

## Crear el entorno virtual dentro de la raíz del proyecto

```bash
python -m venv venv
ó 
py -m venv venv
```

## Activar el entorno virtual 

```bash
venv\Scripts\activate (Para Windows)
source venv/bin/activate (Para Linux y MAC)
```

## Instalar las dependencias

```bash
pip install -r requirements.txt
```

## También se puede desactivar el entorno virtual (en caso de ser necesario)

```bash
deactivate
```

## TENER EN CUENTA

El flujo de trabajo será:

1. Clonar el repositorio.
2. Asegurar que estemos en la ráiz del proyecto.
3. Crear el entorno virtual.
4. Activar el entorno virtual.
5. Instalar las dependencias.

## Ejecutar los scripts de los ejercicios

```bash
py ejercicios-clase/semana-02/clasificador_anios.py
py ejercicios-clase/semana-02/refactor_pep8.py   
```
o usar el comando:
```bash
cd ejercicios-clase/semana-02
```
Y luego ejecutar los comandos:
```bash
py clasificador_anios.py
py refactor_pep8.py   
```