---
title: "73 S12 - Reflexion entre intentos memoria y aprendizaje"
created: 2026-09-29
fecha: 2026-09-29
capitulo: 12
sesion: "12"
tags:
  - maestria/ia-generativa
  - agentes
  - estudio
---

# 73 S12 - Reflexion entre intentos memoria y aprendizaje

[[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/69 S12 - Guía para entender patrones y toolsets|Guía de la sesión 12]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

**Reflexion** organiza un ciclo de producir, evaluar, extraer una lección y volver a intentar. Su rasgo distintivo es que el siguiente intento recibe texto sobre el fallo anterior. La memoria modifica la información disponible; no exige actualizar los pesos. Esta idea se contrasta con [el registro del artículo de Shinn y colaboradores](https://arxiv.org/abs/2303.11366).

## 1. Una crítica concreta tiene información que «intenta otra vez» no tiene

Supón que el agente calcula la variación de ventas usando abril como denominador:

$$\frac{1670-2695}{1670}\times100\approx-61{,}38\%$$

La división existe, pero responde a una referencia diferente. Un verificador que conoce la tarea puede señalar: «la base de comparación es marzo: usa 2695 como denominador». El siguiente intento dispone de una corrección concreta y puede producir -38,03 %.

Volver a muestrear una respuesta sin esa crítica puede acertar por casualidad o repetir el error. No incorpora explícitamente una lección. Una crítica también puede ser falsa: si recomienda un denominador incorrecto, puede empeorar la salida.

## 2. Tres funciones y dos memorias

El paper distingue actor $M_a$, evaluador $M_e$ y auto-reflexión $M_{sr}$. Son **funciones o componentes conceptuales**: no exige tres proveedores ni tres juegos de pesos diferentes en toda implementación.

| Componente | Entrada | Salida |
| --- | --- | --- |
| Actor | Tarea, observaciones y lecciones disponibles | Texto o trayectoria de acciones |
| Evaluador | Candidato o trayectoria | Señal de aceptación, puntuación o fallo |
| Reflexión | Trayectoria, señal y memoria previa | Texto que identifica una lección útil |

El evaluador puede ser código determinista, señal del entorno, heurística o un modelo, según la tarea. Si usa el mismo modelo que el actor, la separación de roles no garantiza independencia de errores.

La **memoria corta** contiene la trayectoria del intento. La **memoria de experiencias** conserva las reflexiones para los intentos siguientes. «Larga» es relativo al alcance de esos intentos; no significa que se almacene dentro de los pesos ni que sobreviva por siempre.

![[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Recursos visuales/53-s12-reflexion-anidada.png|53-s12-reflexion-anidada.png]]

El marco naranja es el ciclo entre intentos. El actor produce la trayectoria; el evaluador decide si se acepta; si falla, la reflexión devuelve una lección al actor. El retorno incorpora información al contexto. La salida superior representa aceptación. El código debe añadir además el máximo de intentos y los presupuestos, aunque no aparezcan como cajas en este esquema.

## 3. ReAct puede vivir dentro de Reflexion

ReAct decide cómo actuar **durante** una corrida. Reflexion decide cómo usar lo ocurrido para el **próximo intento**. Se pueden componer, como en ALFWorld en el paper. Un actor que solo produce una salida JSON también puede participar en un ciclo de evaluación y reintento; no necesita hacer búsquedas para cada ejemplo.

El mini-ejercicio del martes utiliza un verificador de JSON y salidas simuladas. Demuestra la estructura de reintentos, pero no reproduce toda la reflexión generada por LLM y memoria episódica del artículo. Si una función devuelve siempre el siguiente elemento de una lista, la mejoría está programada; no demuestra aprendizaje del modelo.

## 4. Memoria acotada: qué ganas y qué pierdes

Guardar todas las experiencias mantiene más detalle, pero aumenta contexto y puede acumular errores. Mantener las últimas $k$ conserva un costo acotado, pero olvida lecciones antiguas. Resumir comprime la historia, pero puede omitir una condición decisiva.

El artículo declara una cota de experiencias $\Omega$ usualmente entre 1 y 3; en ALFWorld conserva las últimas tres, y en la configuración de programación descrita usa una experiencia. No hay un único `k=3` universal para Reflexion.

Una memoria útil podría guardar: «fallo: denominador equivocado; criterio: base temporal solicitada; corrección: comparar con marzo». Guardar «la respuesta estuvo mal» no indica qué cambiar. Guardar una conjetura como hecho puede contaminar los intentos siguientes.

## 5. La condición de parada exige precisión lógica

La intención es terminar cuando el evaluador aprueba **o** se agotan los intentos. Por tanto, la condición para continuar debe ser:

```python
while not aprobado and intentos < max_intentos:
    # generar, evaluar y, si falla, incorporar una lección
    ...
```

En la copia local del paper, Algoritmo 1, PDF 4, aparece **`not pass or t < max trials`**. Se confirmó también visualmente. Esa condición no implementa la terminación descrita: puede continuar después de aprobar si quedan intentos, y puede continuar después del máximo si nunca aprueba. Las notas corrigen esa discrepancia y la práctica usa un `for` acotado con retorno temprano.

El PDF de la clase presenta la intención correcta, pero no corresponde atribuir al pseudocódigo impreso una garantía que su operador lógico no cumple. El límite debe comprobarse en la implementación.

Un reintento también requiere definir **desde qué estado comienza**. En ALFWorld, el paper reinicia el entorno después de cada fallo y conserva las lecciones. En una aplicación que envió un pedido o escribió en una base, comenzar otro intento no revierte automáticamente el efecto anterior. La memoria puede impedir repetirlo, pero los permisos e idempotencia del ejecutor siguen haciendo falta.

En ese experimento, la heurística propone reflexionar al repetir la misma acción y recibir la misma respuesta durante más de tres ciclos, o al superar 30 acciones. Es un criterio sobre trayectoria y falta de progreso, más preciso que comparar solo palabras. Esos umbrales pertenecen a ese entorno y no son máximos universales. La mejora de 130/134 es acumulada a lo largo de hasta 12 ensayos, con memoria y reinicio, no una medición equivalente a una generación única.

## 6. Evidencia histórica y alcance

El paper informa 130 de 134 tareas ALFWorld resueltas por ReAct + Reflexion durante varios intentos: $130/134\approx97{,}01\%$. No es el éxito del primer intento ni es comparable directamente con el 71 % de otra configuración de ReAct. En HumanEval Python presenta 91,0 frente a 80,1 del modelo base; en Rust, 68,0 frente a 60,0. La mejora no es universal: MBPP Python muestra 77,1 frente a 80,1.

La sección de HotpotQA usa 100 preguntas y reporta que, en ese protocolo, repetir con temperatura 0,7 no corrigió tareas falladas del primer intento en las líneas base. No prueba que cualquier reintento sin memoria sea inútil en cualquier aplicación. La expresión «20 % de mejora» del material no debe convertirse en «20 puntos porcentuales» sin una cuenta y denominadores compatibles.

El nombre *verbal reinforcement learning* describe el aprendizaje mediante experiencias textuales del método. En la ejecución estudiada, no es el ajuste de parámetros con una recompensa que vimos en RLHF. La conexión con [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/04 Entrenamiento y alineamiento/22 S03 - SFT RLHF DPO y Constitutional AI|22 S03 - SFT RLHF DPO y Constitutional AI]] ayuda a distinguir contexto de entrenamiento.

> [!question]- ¿Una reflexión convincente demuestra que identificó la causa real del error?
> No. Es otra salida generada. Debe contrastarse con la señal verificable y el resultado del siguiente intento; una explicación plausible puede atribuir una causa equivocada.

Fuentes: [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/sesion-12.pdf#page=12|PDF 12–16]], [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/fuentes/papers/s3-agentes/shinn-2023-reflexion.pdf#page=3|artículo §3–4, PDF 3–8]]; Algoritmo 1 en PDF 4 y límites en PDF 9. Lectura seleccionada de la copia local; no se afirma lectura completa de todos sus apéndices.

---

← [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/72 S12 - Pasos presupuestos timeouts y condiciones de parada|Anterior]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/74 S12 - Verificadores fiables y errores del notebook|Siguiente]] →

