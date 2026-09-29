---
title: "66 S11 - Límites trazas y laboratorio del bucle"
sesion: "11"
fecha: 2026-09-28
tags:
  - maestria/ia-generativa
  - agentes
  - herramientas
fuente: "[[sesion-11.pdf]]"
---

# 66 S11 - Límites trazas y laboratorio del bucle

[[59 S11 - Guía para entender agentes y herramientas|Guía de la sesión 11]] · [[00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

Anterior: [[65 S11 - Toolformer aprendizaje resultados y límites]]

Siguiente: [[67 S11 - Ejercicios resueltos y repaso activo]]

## 1. Por qué un objetivo no garantiza una salida

El modelo puede insistir en una búsqueda que no devuelve nada, repetir una llamada inválida o no reconocer que ya obtuvo la respuesta. Un ciclo sin límite puede seguir consumiendo recursos. La condición de parada debe formar parte del programa.

![[48-s11-parada.png]]

**Cómo leerlo:** antes de pedir otra decisión se comprueba el contador. Una respuesta final cierra la ejecución. Una llamada sigue por validación, ejecución y observación. Si no quedan pasos, la salida informa que la tarea quedó incompleta.

## 2. Define primero qué estás contando

`max_steps` no tiene un significado universal. Puede contar decisiones del modelo, llamadas a herramientas o vueltas de un planificador. Un turno puede contener varias llamadas en algunas implementaciones.

En el laboratorio incluido, **un paso = una decisión del simulador**. La respuesta final también consume un paso. Por tanto, el caso exitoso usa cuatro decisiones y tres llamadas de herramientas.

La p. 23 menciona valores 5, 6, 8 y 10 en distintos materiales. No establece un número obligatorio. La decisión debe relacionarse con la tarea y con cómo se define la unidad contada.

## 3. Un límite no reemplaza los demás

| Límite | Problema que acota | Lo que no garantiza |
| --- | --- | --- |
| Número de decisiones | Repetición indefinida entre pasos | Que una herramienta no se bloquee dentro de un paso. |
| Tiempo máximo por operación | Operaciones que no regresan | Que no haya muchas operaciones rápidas inútiles. |
| Volumen de contexto | Entradas demasiado largas | Que el contenido sea pertinente o verdadero. |
| Llamadas o gasto | Consumo acumulado | Que la respuesta sea correcta. |
| Reintentos | Insistencia ante errores repetidos | Que volver a ejecutar una escritura sea inocuo. |

El simulador solo aplica límite de decisiones, validación y un catálogo cerrado. Como sus herramientas son operaciones locales breves, no implementa una infraestructura de timeouts de servicios externos. Es un ejemplo del mecanismo, no un sistema listo para producción.

## 4. Qué debe explicar la salida por límite

Un cierre útil indica lo conseguido, lo pendiente y por qué paró. Por ejemplo: «Obtuve febrero y marzo, pero se agotó el máximo de decisiones antes de producir la respuesta final». No debería transformar ausencia de resultado en un dato inventado.

Un sistema puede generar un resumen adicional al detenerse, pero esa llamada también requiere presupuesto. En nuestro ejemplo el cierre por límite lo compone el programa, sin volver a llamar a un modelo.

## 5. Qué es una traza y para qué sirve

Una traza registra lo que sucedió. No es solo la respuesta final ni una narración convincente del modelo.

| Campo | Por qué ayuda |
| --- | --- |
| Inicio y pregunta | Reconstruye el objetivo de la ejecución. |
| Paso y evento | Ordenan las transiciones. |
| ID de llamada y herramienta | Vinculan solicitud y resultado. |
| Argumentos | Permiten detectar período, tipo o dominio incorrecto. |
| Resultado y error | Distinguen evidencia, ausencia y fallo. |
| Duración | Ayuda a localizar lentitud. |
| Estado de cierre | Distingue final, límite y fallo del protocolo. |

Para depurar selección también se necesita saber qué catálogo e instrucciones estaban disponibles, usando una versión o una instantánea apropiada. En sistemas reales se deben evitar secretos en la traza y controlar qué datos se conservan. No todo el contenido de una base tiene que copiarse para que el registro sea útil.

El taller, según p. 24, usa vocabulario *Thought, Action, Observation*. Para estudiar, puedes registrar una **justificación breve de la acción** junto a su ejecución y observación. Esa explicación no es una lectura verificable del razonamiento interno del modelo. Los eventos ejecutados y sus resultados son evidencia distinta de la explicación textual.

## 6. Laboratorio incluido: observar el protocolo sin una API

Archivo: [[s11_laboratorio_bucle.py]]. Resultados de la verificación: [[s11_resultados_verificados.json]]. Ambos están en `11 Agentes y uso de herramientas/Practica`.

Desde esa carpeta:

```bash
python3 s11_laboratorio_bucle.py
```

Solo utiliza la biblioteca estándar de Python. Imprime JSON; no llama a un proveedor, no requiere credenciales, no se conecta a una base real y no modifica datos empresariales.

> [!important] Qué demuestra y qué no
> `modelo_simulado` es una función con reglas, no un LLM. Responde a observaciones para enseñar el intercambio de mensajes. Que los casos pasen verifica el harness del ejemplo y las cuentas; no mide la capacidad de decisión de un modelo real ni reproduce el notebook docente.

### Cómo leer el código

1. `total_ventas` y `variacion_porcentual` son las herramientas reales del ejemplo.
2. `ejecutar` mantiene una lista cerrada, valida entradas y devuelve éxito o error.
3. `modelo_simulado` inspecciona resultados previos y propone el siguiente mensaje.
4. `correr` mantiene historial, IDs, contador y traza.
5. `verificar` recorre casos de éxito, límite y fallo y comprueba los resultados esperados.

### Casos que puedes observar

| Caso | Lo que deberías ver |
| --- | --- |
| Éxito con límite 4 | Dos consultas, un cálculo y respuesta de 25 %. |
| Mismo caso con límite 3 | Las herramientas terminan, pero no queda decisión para responder; cierre por límite. |
| Repetición con límite 3 | Tres llamadas y cierre incompleto; nunca una repetición ilimitada. |
| Herramienta desconocida | Resultado de error asociado al ID; después cierre explicando el fallo. |
| Mes inválido | Rechazo antes de consultar. |
| Mes válido sin datos | Error de disponibilidad, distinto del de formato. |
| Base cero | Error: porcentaje indefinido. |
| ID repetido | Fallo de protocolo; no se ejecuta la segunda propuesta ambigua. |
| Mensaje mal formado | Cierre de protocolo, sin intentar ejecutar. |

El archivo de resultados incluye las trazas reales de esta simulación; sus milisegundos dependen del equipo. No son benchmarks de un LLM.

## 7. Diagnosticar antes de cambiar el modelo

| Síntoma | Hipótesis inicial | Evidencia a inspeccionar |
| --- | --- | --- |
| No propone ninguna herramienta | No recibió catálogo o entendió que bastaba responder | Entrada real, catálogo y objetivo. |
| Propone una herramienta que no existe | Catálogo inconsistente o nombre inventado | Nombre propuesto y registro. |
| Repite la misma búsqueda | Resultado insuficiente, historial omitido o mala estrategia | Argumentos y observaciones de cada vuelta. |
| Calcula con meses invertidos | Confunde base y actual | Parámetros del cálculo, no solo texto final. |
| Dice que la consulta funcionó pero no hay dato | Resultado ambiguo o error oculto | Estado `ok`, dato, error y referencia. |
| Acaba correctamente el protocolo con respuesta falsa | Falta evaluación de éxito | Comparación con valores y criterios esperados. |

Una intervención útil modifica una causa plausible: una descripción, un resultado ambiguo o la conservación del historial. Después se compara en los mismos casos, como en [[57 S10 - Reproducibilidad entregables y reflexión]].

## 8. Qué anuncia la sesión sobre el Taller 3

El PDF sitúa el Taller 3 el sábado 3 de octubre de 2026, con 25 % según la p. 26, y anuncia patrones de razonamiento, MCP y sistemas multiagente para las siguientes sesiones. Aquí se registra como información del material, no como verificación independiente del calendario vigente.

La actividad de p. 24 propone declarar herramientas, ejecutar llamadas, construir el bucle y conservar una traza. La presentación indica que dispone de un simulador sin credenciales. No se inspeccionó ese notebook; el programa de estas notas es independiente.

**Fuente:** [[sesion-11.pdf#page=23|pp. 23–26]]. La clasificación de fallos, el laboratorio y la separación de presupuestos son ampliaciones explicativas.
