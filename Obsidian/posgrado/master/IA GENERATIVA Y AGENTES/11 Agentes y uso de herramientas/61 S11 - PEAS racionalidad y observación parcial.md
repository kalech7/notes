---
title: "61 S11 - PEAS racionalidad y observación parcial"
created: 2026-09-28
capitulo: 11
sesion: "11"
fecha: 2026-09-28
tags:
  - maestria/ia-generativa
  - agentes
  - herramientas
fuente: "[[sesion-11.pdf]]"
---

# 61 S11 - PEAS racionalidad y observación parcial

[[59 S11 - Guía para entender agentes y herramientas|Guía de la sesión 11]] · [[00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

Anterior: [[60 S11 - Chatbot pipeline RAG y agente quién decide]]

Siguiente: [[62 S11 - Function calling y bucle del agente paso a paso]]

## 1. Qué significa PEAS

PEAS es una forma de especificar el problema antes de construir el agente. Sus letras son *Performance measure*, *Environment*, *Actuators* y *Sensors*: medida de desempeño, entorno, actuadores y sensores.

![[42-s11-peas.png]]

El entorno produce información que llega mediante sensores; el agente elige acciones que se realizan mediante actuadores. La barra superior define cómo juzgamos el resultado. La métrica no se deduce de que el agente «parezca inteligente».

| Letra | Pregunta de diseño | Ejemplo del asistente |
| --- | --- | --- |
| P | ¿Qué cuenta como hacerlo bien? | Calcular el crecimiento correcto, citar cifras y terminar dentro del presupuesto. |
| E | ¿Qué parte del mundo interviene? | Base de ventas, documentos del negocio y conversación con el usuario. |
| A | ¿Qué puede hacer el sistema? | Ejecutar una consulta permitida, calcular y presentar una respuesta. |
| S | ¿Qué puede percibir? | Pregunta, resultados, errores, metadatos y tiempos de ejecución. |

Una herramienta de lectura funciona como canal de percepción; la ejecución de la consulta es también una operación del programa. Una herramienta de escritura puede modificar el entorno y devolver una observación. No es necesario clasificar cada función en una sola caja de forma rígida.

## 2. Objetivo y desempeño no son idénticos

El objetivo del usuario puede ser «explica cuánto crecieron las ventas». Una medida de desempeño especifica cómo verificarlo: cantidades del mes correcto, misma moneda, fórmula adecuada y respuesta sustentada.

Si solo premiamos «terminó rápido», podría inventar una cifra. Si solo premiamos «usó herramientas», podría consultar cien veces. Si solo premiamos «texto convincente», podríamos aceptar un cálculo incorrecto. Una mala medida induce una mala noción de éxito.

Un ejemplo propio de rúbrica es aprobar únicamente si se cumplen cuatro condiciones: cifras correctas, cálculo correcto, procedencia verificable y finalización válida. Después comparamos latencia o número de llamadas entre las ejecuciones aprobadas. Así evitamos compensar un resultado falso con una respuesta rápida.

## 3. Racional no significa infalible

En el marco clásico, un agente racional selecciona lo que se espera que mejore su desempeño según lo que sabe y ha percibido. «Se espera» importa: no conoce necesariamente el futuro ni el estado completo del mundo.

Imagina dos fuentes: una consulta reciente y un archivo de hace un año. Consultar la reciente puede ser razonable, aunque el servicio falle después. Juzgar una decisión requiere distinguir la información disponible al decidir del desenlace observado posteriormente.

La función abstracta de agente puede expresarse como:

$$a_t=f(o_1,o_2,\ldots,o_t).$$

Aquí $o_t$ es una observación, $a_t$ una acción y $f$ la regla que transforma la historia de observaciones en una acción. En una aplicación con LLM, esa regla se implementa mediante pesos, instrucciones, contexto, decodificación y restricciones del programa. No vive únicamente en los pesos.

## 4. Los cuatro tipos, con el mismo problema

| Tipo | Qué usa para decidir | Ejemplo didáctico | Límite |
| --- | --- | --- | --- |
| Reactivo simple | Observación actual y reglas | Si aparece «total marzo», llama a la consulta de marzo. | No considera qué se consultó antes. |
| Basado en modelo del mundo | Estado interno actualizado | Conserva que febrero ya fue consultado y está pendiente marzo. | Mantener estado no define por sí solo qué se busca lograr. |
| Basado en objetivos | Estado y meta | Elige las consultas necesarias para comparar dos meses. | Cumplir la meta no establece cómo intercambiar costo y rapidez. |
| Basado en utilidad | Una evaluación de alternativas | Compara una respuesta suficiente ahora con una consulta adicional costosa. | Necesita una función o criterio de preferencias bien definido. |

**«Basado en modelos» aquí no significa simplemente «usa un modelo de lenguaje».** Significa que mantiene una representación de cómo está o cómo evoluciona el entorno. Confundir ambas acepciones impide entender la clasificación.

El PDF ubica al agente LLM del curso en la categoría basada en objetivos. Es una simplificación útil del diseño mostrado, no una imposibilidad de que un sistema con LLM maneje restricciones, preferencias o funciones de utilidad explícitas. Tampoco todo agente reactivo requiere observabilidad total para hacer algo útil; esa limitación afecta qué desempeño puede alcanzar en una tarea determinada.

Una utilidad permite distinguir **dos resultados que cumplen la misma meta**. Supón, como ejemplo propio, que una respuesta correcta obtenida en 2 segundos y otra obtenida en 30 segundos reciben distinta preferencia por la latencia. Se podría definir $U=100\,\mathbf{1}_{\text{correcto}}-\lambda C-\mu T$, donde $C$ es costo, $T$ tiempo y los coeficientes representan cuánto pesan. Esa fórmula no es una política recomendada: una mala elección de pesos puede hacer rentable equivocarse. Sirve para mostrar por qué «cumplió el objetivo» y «escogió la alternativa preferida» son preguntas diferentes.

Los cuatro tipos no describen cuatro niveles obligatorios de una misma aplicación. Sus mecanismos pueden coexistir, y **aprender** es otra dimensión: un agente reactivo o uno basado en utilidad puede ajustar su comportamiento con experiencia. En el sistema del curso, actualizar historial cambia el estado y el contexto; no es por sí solo entrenamiento de sus parámetros.

## 5. Observación parcial: lo que existe y lo que llega al contexto

La base completa puede contener miles de transacciones. El modelo recibe una respuesta resumida: «total marzo = 15 000». Esa observación no le informa automáticamente sobre devoluciones, impuestos o moneda. El mundo contiene más que el mensaje disponible.

Por eso el resultado debería conservar información pertinente:

```json
{
  "mes": "2026-03",
  "total": 15000,
  "moneda": "USD",
  "definicion": "ventas netas sin impuestos",
  "fuente": "consulta_demo_marzo"
}
```

Esto reduce ambigüedad, pero no convierte la observación en una fotografía completa del mundo. La consulta podría estar desactualizada o haber seleccionado el conjunto equivocado. Es necesario verificar el dato, no solo su formato.

En notación de estado:

$$s_{t+1}=U(s_t,a_t,o_{t+1}).$$

$s_t$ es el estado que mantiene el programa; $U$ la operación de actualización. Tras consultar marzo, el estado añade su total, procedencia y posibles errores. El estado almacenado no es idéntico al estado verdadero del entorno: puede ser incompleto.

## 6. Clasificar el entorno ayuda a prever problemas

Como ampliación, el asistente puede trabajar en un entorno parcialmente observable, secuencial y cambiante: lo que consulta primero condiciona lo que hace después, y otra persona puede modificar la base entre consultas. Una calculadora puede ser determinista, aunque el sistema completo no tenga resultados totalmente predecibles.

Por ejemplo, si febrero y marzo se consultan en momentos con versiones distintas de los datos, una diferencia podría reflejar una actualización. Para una comparación fiable conviene declarar período, moneda, criterio de inclusión y, cuando sea pertinente, versión o instante de corte.

> [!tip] Recordatorio
> PEAS describe la tarea; el bucle implementa una estrategia para resolverla; la evaluación comprueba si lo consiguió.

**Fuente:** [[sesion-11.pdf#page=8|pp. 8–11]], que atribuye el marco a Russell y Norvig, cap. 2. Las fórmulas y el caso son ampliaciones. No se da por consultada la edición de AIMA citada en el pie del PDF; se conserva esa atribución como fuente de la presentación.
