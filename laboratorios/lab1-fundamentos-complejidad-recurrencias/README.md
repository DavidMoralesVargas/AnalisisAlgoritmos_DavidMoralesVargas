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

## Parte 2 — Responsabilidad ambiental y ética de la implementación

Ya se vio en el punto anterior como una mala decisión, por no mirar todo el punto de vista del programa, puede tener consecuencias desagradables. Al tomar una conclusión tan precipitada y duplicar la velocidad del servidor hará que tarde mucho más tiempo el ordenamiento (que conlleve a que el servidor colapse) de la lista para priorizar a los pacientes, o simplemente el hecho de usar un algoritmo que tarde más que otro, lo que se traduce directamente a muchos más recursos que se le deben exigir al servidor para que procese eso día tras día, semana tras semana, mes tras mes, años tras año. Como el algoritmo es ineficiente para este proceso por el tiempo tan exagerado que toma completar su tarea entonces eso afecta directamente al consumo energético, lo que es directamente proporcional a una huella de carbono injustificada y que tenga un mayor impacto negativo ambientalmente hablando. No solo las personas y el servidor sufren, también los recursos naturales que se usan para poder operar esos procedimientos computacionales.

Ya tomamos en cuenta un impacto ambiental que puede sufrir por la mala implementación del algoritmo en la situación actual de la plataforma Tamiza. Ahora, diariamente se puede sufrir dentro de la organización de Salud por esa demora, ya que el algoritmo también puede llegar a fallar y dar datos incompletos que no se debería dejar pasar por alto. Existen varias personas afectadas por este error, pero se puede destacar principalmente a dos actores: el operador de centro de contacto y al paciente. Al necesitar de una lista incompleta y sin un orden hace que el personal de ese servicio trabaje de una forma muy desorganizada, con mala priorización y se seguro realizando trabajo no correspondiente a sus labores, esto sin contar probablemente quejas por partes de los pacientes y problemas internos por errores que se pueden cometer. Por otro lado, el paciente sufre excesivamente también por este error, y que si no se tiene una priorización correcta y por orden de quien debe ser atendido primero causa directamente que una persona no sea contactada a tiempo para su cita, y eso es un riesgo médico y grave que debe asumir el mismo paciente, ya que, de todas formas, no podrá ser atendido. Los tiempos de espera van a aumentar para las personas que realmente necesitan una atención más inmediata. Por algo más secundario, está la secretaria de Salud que tiene que realizar pagos excesivos y demás por la mala implementación de un algoritmo, y el equipo de desarrollo que debe trabajar tiempos extras resolviendo problemas relacionados también a dicho tema.

Por todo lo anterior, y más allá del tiempo que el servidor va a gastar en la ejecución del algoritmo y el tiempo de más que la personas que trabajen en esa organización deben usar, se está hablando de un software médico, que son aplicativos más delicados con el funcionamiento que deben implementar. Al momento de que un algoritmo se demore más de lo que debería no solo es pérdida de dinero por parte de la empresa, por parte de los trabajadores con cosas extras que deben hacer, sino que directamente se está manejando un tema con la priorización de los pacientes. Hay pacientes que deben ser atendidos urgentemente, y tienen más problemas que otros, de ahí la priorización que se hace, entonces un error con la ejecución puede ser vital para una persona que debe ser atendida, eso es un fallo critico en el sistema de salud, y reglas de calidad que no se están cumpliendo.

---

