---
title: "78 S12 - Ejercicios resueltos y repaso activo"
created: 2026-09-29
fecha: 2026-09-29
capitulo: 12
sesion: "12"
tags:
  - maestria/ia-generativa
  - agentes
  - estudio
---

# 78 S12 - Ejercicios resueltos y repaso activo

[[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/69 S12 - Guía para entender patrones y toolsets|Guía de la sesión 12]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

Estas preguntas comprueban si puedes explicar causas y consecuencias. Las respuestas son elaboración propia basada en las fuentes de la sesión. Trata de resolverlas antes de desplegar cada solución.

## Mecanismo y evidencia

> [!question]- 1. El Thought dice «las ventas fueron 5000», pero no existe consulta previa. ¿Qué sabes?
> Sabes que el modelo produjo esa afirmación; no que obtuvo una medición. Hace falta una observación o una fuente autorizada que respalde la cifra. Un texto plausible no es evidencia externa.

> [!question]- 2. Una consulta devuelve total 2695. ¿Qué permite concluir y qué no?
> Permite usar el total para el período y la definición cubiertos por la consulta, si la herramienta es fiable. No explica por sí solo la causa del resultado ni certifica que la base represente todas las ventas posibles.

> [!question]- 3. ¿Cuántos pasos necesita el lunes para una herramienta y texto final?
> Dos decisiones del modelo y una llamada de herramienta. Puede haber más eventos de traza si se registran solicitud y observación por separado. Hay que declarar la unidad de «paso».

> [!question]- 4. ¿Por qué el simulador del lunes repite con un historial de dos mensajes por llamada?
> Busca un rol `tool_result_meta` que no aparece en el par natural `assistant_tool_use` y `tool_result`. No reconoce que recibió datos. La solución es hacer compatibles la detección y el historial; el presupuesto solo contiene la repetición.

> [!question]- 5. Una corrida usa cero herramientas y responde. ¿Eso define toda su arquitectura?
> No. Esa tarea pudo estar resuelta con el contexto disponible, o el modelo pudo contestar fuera de alcance. Para clasificar el sistema hay que inspeccionar quién decide, qué puede ejecutar y si hay realimentación.

## Bucles y presupuestos

> [!question]- 6. El detector encuentra acciones iguales. ¿Está probada una falla?
> Está probada la repetición bajo su equivalencia. Puede ser un reintento legítimo o una lectura tras cambio de estado. Hace falta relacionarla con progreso, resultados y contrato.

> [!question]- 7. ¿Por qué ordenar palabras falla con «Ana paga a Luis»?
> La misma bolsa de palabras aparece en «Luis paga a Ana», pero cambian pagador y receptor. La normalización borra el orden que expresa esa relación; puede producir un falso positivo.

> [!question]- 8. Se dispone de siete unidades y cada acción cuesta dos. ¿Cuántas caben?
> Tres, por costo 6. La cuarta exigiría 8 y se rechaza antes de ejecutarla. Las unidades son didácticas; no hay conversión implícita a dinero o tokens.

> [!question]- 9. Un agente tiene máximo de cinco pasos, pero la primera consulta no responde. ¿El máximo basta?
> No. El contador no avanza mientras la operación está bloqueada. Hace falta timeout de operación y una política de cancelación o aislamiento según el entorno.

> [!question]- 10. Tres intentos de cinco decisiones cada uno, con evaluación LLM y reflexión LLM después de cada uno de los dos fallos, ¿qué máximo hay bajo esos supuestos?
> Quince llamadas del actor, tres de evaluación y dos de reflexión: veinte. Suponemos que cada decisión, evaluación y reflexión usa una única llamada, y que no hay otras operaciones del modelo. El presupuesto global debe incluirlas.

## Reflexion y verificación

> [!question]- 11. ¿Qué cambia Reflexion si los pesos quedan fijos?
> Cambia el contexto: la trayectoria, señal de evaluación y reflexión se transforman en lecciones que recibe el próximo intento. No es ajuste fino ni RLHF por el solo hecho de llamarse aprendizaje verbal.

> [!question]- 12. ¿ReAct y Reflexion compiten por el mismo lugar?
> No necesariamente. ReAct puede organizar las acciones de un intento; Reflexion puede evaluar ese intento y preparar el siguiente. Pueden componerse.

> [!question]- 13. ¿Qué problema tiene `while not aprobado or intentos < máximo`?
> Sigue mientras cualquiera de las dos condiciones sea verdadera. Puede continuar después de aprobar si quedan intentos, y después del máximo si no aprobó. Para exigir a la vez fallo y saldo de intentos se usa `and`.

> [!question]- 14. ¿Por qué `true` pasa como `int` en el verificador original?
> JSON `true` se convierte en Python `True`, y `bool` hereda de `int`. `isinstance(True, int)` es verdadero. Para el contrato de entero sin booleanos se usa `type(valor) is int`.

> [!question]- 15. ¿`[]` es JSON válido? ¿Debe aceptarse en el ejercicio?
> Sí es JSON válido, pero no un objeto con categoria y urgencia. Debe rechazarse por estructura sin lanzar un error al intentar llamar `.keys()`.

> [!question]- 16. ¿La variante debe rechazar urgencia 100 por estar fuera de 1–5?
> No con el contrato recibido: no especifica ese rango. Se puede añadir en un nuevo diseño, documentándolo como requisito propio. Inventarlo alteraría el ejercicio.

> [!question]- 17. Un objeto pasa el verificador, pero clasifica una venta como problema técnico. ¿Qué falló?
> La evaluación de formato no contempla la correspondencia con el ticket. Hace falta un criterio semántico y una referencia o evidencia del caso. No se resuelve añadiendo más parseo JSON.

> [!question]- 18. La ablación cae de 60 a 52 %. ¿Es una caída de ocho por ciento?
> Son ocho puntos porcentuales. La caída relativa es $8/60\times100\approx13{,}33\%$. Hay que declarar cuál medida se informa.

## Planificación, herramientas y resultados

> [!question]- 19. El plan necesita abril, pero la herramienta devuelve sin datos. ¿Se debe reemplazar por cero?
> No automáticamente. Ausencia de datos no equivale a cero ventas. Se debe aclarar el significado, obtener otra fuente o terminar con el alcance limitado y, si corresponde, revisar el plan.

> [!question]- 20. ¿Por qué describir el esquema de la base reduce adivinaciones sin garantizar seguridad?
> Informa qué tablas y columnas existen. Los permisos, la validación y los límites de consulta siguen siendo controles separados. Conocer un nombre no autoriza a leerlo ni asegura una consulta barata.

> [!question]- 21. El modelo pide `row_limit=100000`, pero el máximo interno es 100. ¿Qué hace el programa?
> Valida la entrada y aplica como máximo 100, o rechaza el exceso según la política declarada. El esquema público puede incluir una preferencia; la restricción efectiva no debe ser superable por el modelo.

> [!question]- 22. Una herramienta «solo lectura» genera un PNG. ¿Hay un efecto secundario?
> Sí: escribe un archivo. Puede ser solo lectura respecto de la base, pero debe declarar y limitar el destino de salida. Los efectos se describen por recurso.

> [!question]- 23. ¿Qué prueba que ReAct mejora siempre frente a CoT?
> Nada en los resultados estudiados. En HotpotQA es 27,4 frente a 29,4; en FEVER, 60,9 frente a 56,3. La tarea, comparador, modelo y régimen deben acompañar cualquier afirmación de ganancia.

> [!question]- 24. ¿El 0 % de alucinación en fallas ReAct prueba que nunca inventa?
> No. Es una categoría de un subconjunto de fallas analizadas. El artículo también encuentra razonamiento o hechos inventados en parte de trayectorias con respuesta correcta. Ni la muestra ni el denominador permiten una afirmación universal.

## Caso integrado resuelto

Tarea: «Compara abril respecto de marzo y explica por qué bajó». El agente tiene las herramientas del lunes y los datos originales.

Primero obtiene marzo = 2695 y abril = 1670, conserva las llamadas y resultados, valida que ambos totales correspondan a la misma definición y calcula:

$$\Delta=1670-2695=-1025$$
$$\Delta\%=\frac{-1025}{2695}\times100\approx-38{,}03\%$$

La respuesta puede explicar la caída de 1025 y el porcentaje. **No puede probar una causa** solo con esos datos. Puede descomponer la diferencia por producto como análisis descriptivo, si obtiene el detalle, pero una contribución contable no demuestra causalidad.

La descomposición por producto, calculada de las siete filas, permite explicar **de qué partes consta** el cambio:

| Producto | Marzo | Abril | Diferencia abril − marzo |
| --- | ---: | ---: | ---: |
| laptop | 2350 | 1300 | -1050 |
| monitor | 300 | 320 | +20 |
| teclado | 45 | 50 | +5 |
| Total | 2695 | 1670 | -1025 |

La contribución negativa de laptops se compensa parcialmente con +25 de los otros productos: $-1050+20+5=-1025$. Marzo registra dos ventas de laptop y abril una. Eso explica la composición de **estas filas**, pero no prueba si faltaron registros, cambió demanda o existió una promoción. Incluso una descomposición exacta de un total sigue siendo descriptiva.

Si un intento usa abril de denominador, una evaluación fiable lo rechaza y proporciona la base correcta. Si un intento inventa «menor demanda», el evaluador de JSON no lo detectará; hace falta evaluar respaldo de afirmaciones. Si insiste en consultar lo mismo sin cambio de estado, detector y presupuesto contienen la falla. Si abril no está disponible, el plan debe revisarse y el resultado expresar incertidumbre.

## Glosario de bolsillo

| Término | Significado en estas notas |
| --- | --- |
| Trayectoria | Secuencia de decisiones y observaciones de un intento |
| Thought | Texto que organiza contexto, no evidencia externa por sí solo |
| Action | Solicitud de una operación o decisión operativa |
| Observation | Resultado que devuelve el entorno o herramienta |
| Verificador | Procedimiento que comprueba un criterio explícito |
| Reflexión | Texto que transforma feedback en una lección |
| Ablación | Experimento que modifica componentes para estudiar su aporte |
| Replanning | Revisión del plan ante nueva información |
| Idempotencia | Repetir no añade un efecto distinto después de la primera operación |
| Harness | Programa que valida, ejecuta, registra y controla el bucle |

Fuentes de repaso: [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/sesion-12.pdf|sesion-12.pdf]], ambos notebooks y las notas 68–77. Las cuentas y escenarios son didácticos; los resultados de laboratorio se conservan en [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/Practica/s12_resultados_verificados.json|s12_resultados_verificados.json]].

---

← [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/77 S12 - Laboratorio local y soluciones del martes|Anterior]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/13 MCP descubrimiento y casos de uso/00 Índice - S13 MCP y casos de uso|Siguiente: sesión 13]] →

