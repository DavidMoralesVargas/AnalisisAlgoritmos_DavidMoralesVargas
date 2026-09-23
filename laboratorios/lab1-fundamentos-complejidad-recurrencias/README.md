# Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias

**Nombre completo:** DAVID MORALES VARGAS

## Instrucciones para reproducir el experimento

1. Crear el entorno virtual dentro de la raíz del proyecto
    ```bash
    python -m venv venv
    ```

    ó

    ```bash
    py -m venv venv
    ```
2. Ubicados ya en la raíz del repositorio se activa el entorno virtual:
   - `source venv/bin/activate`(Linux/macOS)
   - `venv\Scripts\activate` (Windows)
3. Instalar las dependencias:
   ```
   pip install -r requirements.txt
   ```
4. Ingresar a la carpeta del laboratorio evaluativo:
   ```
   cd laboratorios/lab1-fundamentos-complejidad-recurrencias
   ```
5. Ejecutar cada ejercicio desde este laboratorio (parte3_casos.py y parte4_complejidad.py):
   - **Parte 3** (genera `graficas/parte3_comparaciones.png` y `graficas/parte3_tiempo.png`):
     ```
     py parte3_casos.py
     ```
   - **Parte 4** (genera `graficas/parte4_tiempo.png`):
     ```
     py parte4_complejidad.py
     ```

    También se puede desactivar el entorno virtual (en caso de ser necesario)

    ```bash
    deactivate
    ```
    ---

## Parte 1 — Analizar el algoritmo antes de comprar hardware

Concluir instantáneamente que el problema se resuelve duplicando la velocidad de servidor es lo equivalente a elegir un lenguaje de programación o framework solo porque es lo más nuevo en el mercado. Para casos como este se debe analizar múltiples puntos de vista, incluyendo el algoritmo, ya que un algoritmo puede funcionar a la perfección y entregar el resultado que se desea, pero eso no significa que sea eficiente frente a la ventana de tiempo no negociable de 4 horas que se debe respetar. El algoritmo fue hecho para una cantidad de registros diferentes, siendo estos de mucha menor cantidad, y al haber un crecimiento tan alto entonces se llega a concluir que no es el adecuado para tal tarea y se deben evaluar otras opciones.

El algoritmo insertion soft por su naturaleza tiene una complejidad algorítmica, que, en el peor caso, llega a ser un cuadrado de n (n siendo la cantidad de registros que llegan) por lo que significa que mientras peor lleguen los registros, como si vinieran en el peor caso posible, entonces el tiempo que tarda dicho algoritmo en resolver su tarea puede llegar hasta cuadruplicarse, pues esa idea de que si duplicamos la velocidad entonces se reducirá el tiempo de ejecución solo es una idea pasajera por no ver las posibles entradas que los datos pueden entregar. Esa es la principal razón por la que el sistema colapsa, ya que la idea de que mejora el tiempo de ejecución es algo pasajero, entonces indiferentemente de lo bueno que hayan comprado el hardware del servidor se llegará al mismo problema: tiempo insuficiente por tiempo de ejecución excesivamente alto.

Con un problema de este estilo, no se puede suponer fallos y soluciones sin verificar toda la trazabilidad de lo que está sucediendo. Si se fuera a tomar soluciones como las que la secretaria de Educación propone, de directamente concluir que es el servidor, entonces eso reflejará perdidas monetarias y de tiempo mayores a las que se sufrían antes, no por la cantidad que se le agrego al servidor, sino por no analizar donde estaba exactamente el problema.

Una vez, como programador, experimenté un problema similar al que sufre el software de Tamiza. Como practicante en un hospital tuve la oportunidad de apoyar en el proceso de pruebas de laboratorio, lo cual un bot de Python tenía un algoritmo para sacar las pruebas de laboratorio de todos los pacientes cada día a las 7 de la mañana. El problema es que, si bien el algoritmo sacaba todas las pruebas y las mandaba a la base de datos correctamente, lo hacía muy lento y se pasaba de la hora incluso a mostrar datos a partir de las 12 PM, entonces a los doctores se les entregaban pruebas con datos que al final no reflejaban una correcta trazabilidad del paciente en el día anterior. Se estaba viendo la posibilidad de cambiar el algoritmo para que entregará los datos en el tiempo estimado por el hospital.

---
