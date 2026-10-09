---
title: "10 S18 - Repaso activo y ejercicios resueltos"
created: 2026-10-09
fecha: 2026-10-07
capitulo: 18
sesion: 18
tags:
  - maestria/ia-generativa
  - agentes/llmops
  - estudio
  - arquitectura/repaso
---

# 10 S18 - Repaso activo y ejercicios resueltos

[[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/00 Índice - S18 Guardrails costo y latencia|Índice de S18]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

Las respuestas están plegadas para intentar resolver antes de comprobar. Los casos adicionales son elaboración propia; las cuentas principales reconstruyen la actividad del PDF.

## Controles y privacidad

> [!question]- 1. ¿Por qué «no reveles claves» en el prompt no es suficiente?
> Es una instrucción que puede incumplirse. El mecanismo debe impedir rutas concretas: no enviar secretos innecesarios, limitar herramientas y argumentos, validar la salida y sanitizar registros. El prompt ayuda, pero no sustituye esas decisiones ejecutables.

> [!question]- 2. Una inyección está dentro de un documento recuperado. ¿En qué borde se controla?
> En el contexto recuperado y en las acciones posteriores. Los permisos del documento se comprueban antes de exponerlo; se trata como evidencia, no como instrucción. Una solicitud de herramienta sigue necesitando validación de catálogo, argumentos y autorización. Es inyección indirecta.

> [!question]- 3. ¿Qué significan bloquear, corregir y dejar pasar?
> Bloquear detiene esa continuación. Corregir transforma el contenido y permite continuar con la nueva versión. Dejar pasar permite continuar sin cambios. En el contrato `(bool, texto)`, `True` puede corresponder a corregir o dejar pasar.

> [!question]- 4. `lower()` convirtió ACTUA en actua. ¿También convierte actúa en actua?
> No. Convierte mayúsculas a minúsculas, pero conserva la tilde. La comparación debe normalizar de forma compatible entrada y referencia; aun así, el detector sigue siendo una heurística.

> [!question]- 5. ¿Por qué la lista 101 102 103 coincide con la regex de teléfono?
> Tiene un dígito de inicio, un dígito final y nueve caracteres intermedios admitidos. La clase permite espacios y `{7,}` cuenta caracteres de esa clase, no únicamente dígitos. La redacción elimina una lista legítima de tiendas: es un falso positivo de PII.

> [!question]- 6. El bloqueo ocurre antes del LLM, pero la traza conserva la entrada original. ¿Se evitó todo el daño?
> No. Se evitó esa llamada, pero se creó una copia persistente del dato. Todas las ramas deben aplicar la política de escritura de registros, y se necesitan controles de acceso y retención.

> [!question]- 7. ¿Qué diferencia hay entre retención de 7 días y abrir traces.jsonl en append?
> Retención describe cuánto se conserva. `append` añade registros sin borrar los anteriores. Para hacer efectiva la retención hace falta eliminación o expiración que cubra los destinos y copias pertinentes.

## Métricas

> [!question]- 8. Hay 30 ataques y 70 solicitudes legítimas. Se bloquean 24 ataques y 7 legítimas. Calcula TP, FN, FP, TN, recall y FPR.
> TP=24, FN=30−24=6, FP=7, TN=70−7=63. Recall=24/30=80 %. FPR=7/70=10 %. Precisión de bloqueos=24/(24+7)=77,42 %. Tasa de bloqueo total=31/100=31 %; esa última no distingue daño de sobrebloqueo.

> [!question]- 9. Un control bloquea todos esos 100 casos. ¿Qué métricas obtiene?
> TP=30, FN=0, FP=70, TN=0. Recall=100 %, FPR=100 %. Detecta todos los ataques, pero también impide todas las tareas legítimas. Una cifra de daño nula no demuestra utilidad.

> [!question]- 10. Un banco tiene 50 consultas legítimas y ningún ataque. ¿Cuál es el recall?
> No está definido: el denominador `TP+FN` es cero. Se puede medir FPR sobre consultas legítimas, pero no capacidad de detectar ataques con ese banco.

> [!question]- 11. Una nueva regla pasó todos los 17 casos del banco del curso. ¿Qué falta para afirmar que está bien integrada?
> Forzar los controles dentro del agente y verificar sus spans, decisiones y efectos: qué se llamó, qué texto se usó y qué se guardó. La cobertura de 17 casos no prueba protección universal y debe incluir falsos positivos.

## Costo y latencia

> [!question]- 12. Con 2 100 tokens de entrada, 300 de salida y tarifas 5/25 por millón, ¿cuál es el costo?
> Entrada: 2 100×5/1 000 000=0,0105 USD. Salida: 300×25/1 000 000=0,0075 USD. Total: 0,018 USD. Para 30 000 llamadas: 540 USD. Son las tarifas históricas del ejercicio.

> [!question]- 13. El pequeño tiene tarifas 1/5. ¿El grande cuesta 25 veces más?
> No. Tanto la entrada como la salida del grande cuestan cinco veces más por token. Para los mismos conteos, el total también es cinco veces: 0,018/0,0036=5. El 25 es la tarifa de salida del grande, no una razón de costos.

> [!question]- 14. Si 60 % del tráfico cambia al pequeño, ¿cuál es el ahorro mensual?
> Grande: 12 000 llamadas×0,018=216 USD. Pequeño: 18 000×0,0036=64,80 USD. Total=280,80 USD. Ahorro=540−280,80=259,20 USD, equivalente a 48 %. Se supone mismo consumo de tokens, calidad y router sin costo adicional.

> [!question]- 15. El prefijo baja de 2 000 a 1 000 tokens. ¿El gasto baja a la mitad?
> No. La pregunta y la salida permanecen. La nueva entrada del grande es 1 100 tokens, con costo 0,0055 USD; salida 0,0075 USD; total 0,013 USD. Mes=390 USD. Ahorro=150/540=27,78 %.

> [!question]- 16. El prefijo representa 55,56 % del costo. ¿Eso es el ahorro garantizado de caché?
> No. Es la parte del costo ordinario atribuible al prefijo bajo el escenario. Faltan escritura, lectura, expiración, mínimo, aciertos y condiciones de facturación. Reutilizar cálculo no equivale necesariamente a entrada gratuita.

> [!question]- 17. Cada llamada cuesta 0,018 USD. Se permite un intento inicial y un reintento. ¿Cuál es el máximo por solicitud y el promedio si 20 % reintenta?
> Máximo del componente de llamadas=2×0,018=0,036 USD. Promedio=0,8×0,018+0,2×0,036=0,0216 USD. Es 20 % más que 0,018, bajo costo idéntico por intento. La segunda llamada podría tener diferente longitud en una aplicación real.

> [!question]- 18. El primer evento llega a 0,1 s y el primer texto útil a 1,4 s. ¿Qué tiempo describe la experiencia de empezar a leer?
> 1,4 s. El primer evento puede contener metadatos y no una respuesta visible. Se deben declarar las señales y puntos de medición; no mezclar primer evento, primer token y respuesta completa.

> [!question]- 19. Una respuesta de caché semántica no llamó al modelo. ¿Debe tener una traza?
> Sí. Debe registrar el acierto, la respuesta de origen o su referencia, las versiones y condiciones pertinentes. Sin ese evento, una respuesta reutilizada puede confundirse con generación nueva y ocultar antigüedad o errores de permisos.

## Versiones

> [!question]- 20. El registro conserva v1 y v2, pero `obtener()` devuelve la mayor. ¿Cómo volver a v1?
> Seleccionar explícitamente una versión activa y hacer que la aplicación la consulte. Guardar v1 no cambia lo que se sirve. Conviene registrar y verificar la activación; un rollback no debe borrar la historia de v2.

> [!question]- 21. ¿Por qué `version or ultima` es un error si la versión 0 es válida?
> Porque 0 es falso en una condición y la expresión elige `ultima`. `version is None` diferencia omisión de cero. También debe usarse un orden de versiones definido: cadenas como v9 y v10 no se ordenan como enteros.

> [!question]- 22. La v2 mejora JSON válido de 80 % a 98 %, pero correctitud baja de 92 % a 83 %. ¿Cumple el criterio de la página 28?
> No. El criterio requiere mejorar formato sin degradar correctitud. La tabla es un ejemplo didáctico propio; no un resultado medido del cuaderno del curso, cuya comparación está rotulada simulada.

## Aplicar los mecanismos a una tarea completa

> [!question]- 23. Quedan USD 0,015 y la siguiente llamada puede gastar USD 0,018. El gasto actual está por debajo del límite. ¿La autorizas?
> No. El saldo actual no cubre la próxima operación. Se rechaza o se elige una alternativa que respete presupuesto y calidad. Comprobar solo que el gasto acumulado está por debajo del máximo permitiría excederlo con esa llamada.

> [!question]- 24. Reservas USD 0,018 con límite de USD 0,05 y luego el consumo real es USD 0,016. ¿Qué saldo queda?
> Al reservar quedan USD 0,032 disponibles. Al conciliar se sustituye la reserva por el gasto real y quedan USD 0,034. La diferencia USD 0,002 se libera porque ya se conoce el consumo.

> [!question]- 25. En el router del 60 %, el 10 % de las llamadas pequeñas requiere después una grande. ¿Se conserva el ahorro de 48 %?
> No. Son 1 800 grandes adicionales×0,018=USD 32,40. Total USD 313,20; ahorro `(540−313,20)/540=42 %`. Se conserva el supuesto de iguales tokens por llamada y router sin costo adicional.

> [!question]- 26. Cambias «enero» por «febrero» al final de una pregunta. ¿Qué debería reutilizarse?
> La caché de prefijo puede reutilizar instrucciones idénticas y luego generar una respuesta nueva. Una caché semántica no debe reutilizar la cifra de enero para febrero, aunque las preguntas tengan alta similitud. Streaming solo cambia cuándo recibes la respuesta; no decide si esa cifra es válida.

> [!question]- 27. NFD descompuso `ú` en `u` y una marca de acento. ¿Ya se eliminó la tilde?
> No. La marca sigue en la cadena. La función del laboratorio la elimina después al descartar caracteres de categoría Mn. Esa decisión también afecta ñ, por lo que se usa como copia de comparación y no como transformación indiscriminada de todo dato.

## Contexto de la entrega mencionada por el PDF

La página 31 presenta el Taller 4 como 25 % de la asignatura y menciona 0.b=3 %, 2.c=10 % y Parte 3=15 % en sus referencias de evaluación. El PDF no permite reconstruir toda la rúbrica ni la base de cada porcentaje; no se suman como si fueran componentes completos del 25 % global. La fecha indicada es sábado 17 de octubre de 2026. Es contexto del material, no una tarea o recordatorio creado en estas notas.

El cierre anuncia ajuste fino para la sesión siguiente: allí sí se modifica θ. Lo aprendido aquí sigue siendo aplicable porque cambiar el modelo no elimina la necesidad de permisos, validación, presupuesto, trazas protegidas y evaluación.

Fuente: PDF 2–5, 8–17, 20, 23–31 · numeración visible = página PDF · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/S18 Guardrails costo y latencia.pdf#page=31|Sesión 18, p. 31]].

---

← [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/09 S18 - Laboratorio local de guardrails y versiones|Anterior]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/00 Índice - S18 Guardrails costo y latencia|Índice]] →
