---
title: "74 S12 - Verificadores fiables y errores del notebook"
created: 2026-09-29
fecha: 2026-09-29
capitulo: 12
sesion: "12"
tags:
  - maestria/ia-generativa
  - agentes
  - estudio
---

# 74 S12 - Verificadores fiables y errores del notebook

[[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/69 S12 - Guía para entender patrones y toolsets|Guía de la sesión 12]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

Un **verificador** es un procedimiento que comprueba un criterio explícito. Su utilidad depende de que ese criterio corresponda al objetivo y de que su implementación no acepte errores ni rechace soluciones válidas. Un verificador de formato no es un verificador de verdad.

## 1. El contrato del martes

La celda 12 exige una salida que sea JSON, con exactamente las claves `categoria` y `urgencia`; categoría `tecnico` o `ventas`; urgencia entera. No define un intervalo para la urgencia. Por tanto, añadir «entre 1 y 5» cambiaría la tarea y tendría que declararse como ampliación.

```json
{"categoria": "tecnico", "urgencia": 4}
```

Las categorías funcionan como valores enumerados de un contrato. `"técnico"` puede ser español correcto, pero es distinto de `"tecnico"` para este campo. Un contrato puede escoger valores sin tilde para facilitar interoperabilidad; eso no corrige ni evalúa la ortografía del texto general.

## 2. Sintaxis, estructura, dominio y significado

| Nivel | Pregunta | Ejemplo de fallo |
| --- | --- | --- |
| Sintaxis | ¿Se puede parsear como JSON? | Texto extra antes del objeto |
| Estructura | ¿Es un objeto y tiene las claves exactas? | `[]` o un campo extra |
| Tipo y dominio | ¿Los valores tienen tipos y categorías permitidos? | Categoría con tilde o urgencia decimal |
| Semántica | ¿La categoría y urgencia corresponden al caso? | Ticket de ventas etiquetado como técnico |

El verificador del notebook cubre parte de los tres primeros niveles; no recibe el ticket ni una referencia para evaluar el cuarto. Un objeto puede pasar y estar mal clasificado. También puede haber duplicados de claves que un parser común resuelva quedándose con el último valor; la versión didáctica no añade un detector de claves duplicadas.

## 3. Errores reproducidos del verificador original

| Entrada | Conducta original | Conducta de la variante didáctica |
| --- | --- | --- |
| `[]` | `AttributeError` al llamar `.keys()` | Rechazo: la raíz debe ser objeto |
| `null` | `AttributeError` | Rechazo: la raíz debe ser objeto |
| `{"categoria": [], "urgencia": 4}` | `TypeError` al buscar una lista en un conjunto | Rechazo: categoría debe ser cadena permitida |
| `{"categoria": "tecnico", "urgencia": true}` | Acepta | Rechazo: booleano no es entero del contrato |
| `{"categoria": "tecnico", "urgencia": 4.0}` | Rechaza | Rechaza: aquí se exige entero, no decimal |

En Python, `bool` es subclase de `int`, así que `isinstance(True, int)` da `True`. La corrección explícita para este contrato es `type(valor) is int`. Antes de llamar `.keys()` se comprueba que el parseo devuelva un diccionario; antes de pertenencia a un conjunto se comprueba que la categoría sea cadena.

```python
if not isinstance(datos, dict):
    return False, "La raíz debe ser un objeto JSON"
if set(datos) != {"categoria", "urgencia"}:
    return False, "Usa exactamente las claves categoria y urgencia"
if not isinstance(datos["categoria"], str):
    return False, "categoria debe ser una cadena"
if datos["categoria"] not in {"tecnico", "ventas"}:
    return False, "categoria debe ser tecnico o ventas, sin tilde"
if type(datos["urgencia"]) is not int:
    return False, "urgencia debe ser un entero, no un booleano"
```

Parsear no transforma cualquier JSON válido en un objeto. JSON admite arrays, números, booleanos y `null`. La sintaxis correcta no implica que la forma corresponda al contrato.

## 4. Qué información devuelve una crítica útil

«Está mal» expresa rechazo, pero no localiza el cambio necesario. «Entrega solo el objeto JSON, sin texto previo» permite eliminar el prefijo del intento 1. «La categoría debe ser tecnico, sin tilde» permite corregir el intento 2. El intento 3 cumple el contrato.

La crítica debe relacionar regla, fallo y corrección. Puede añadir el valor observado sin exponer datos innecesarios. No conviene inventar campos o restricciones que no forman parte de la tarea.

## 5. Por qué autocorregirse puede empeorar

![[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Recursos visuales/54-s12-reflexion-ablacion.png|54-s12-reflexion-ablacion.png]]

Las barras reproducen la tabla 3 de la copia local de Reflexion: GPT-4, los 50 problemas más difíciles de HumanEval Rust. La auto-reflexión sin tests baja de 60 a 52 %. Tests y reflexión juntos alcanzan 68 %. La barra roja muestra una pérdida de ocho puntos porcentuales frente a la base; demuestra que este procedimiento puede producir ediciones dañinas en ese protocolo, no que toda revisión sea perjudicial.

Una **ablación** cambia o elimina un componente para estudiar su aporte. La interpretación propuesta por los autores es que, sin una señal que permita reconocer una solución ya correcta, el proceso sigue editando y puede romperla. De ahí la importancia de aceptación temprana y evaluador fiable.

En programación, `pass@1` se refiere a la solución final evaluada del procedimiento. Si ese procedimiento permite intentos internos y tests, el costo no equivale a una única generación de la base. No se debe anunciar que 91 % significa que cada primera generación bruta ya es correcta.

## 6. Falsos positivos, falsos negativos y denominadores

Un falso positivo del verificador acepta una implementación incorrecta. Un falso negativo rechaza una implementación correcta. Ambos importan: uno entrega errores; el otro puede provocar cambios innecesarios.

El paper informa 16,3 % para MBPP Python y 1,4 % para HumanEval Python como probabilidad de solución incorrecta **entre las que pasaron sus tests**:

$$P(\text{solución incorrecta}\mid\text{tests pasan})$$

No es automáticamente la tasa clásica $P(\text{tests pasan}\mid\text{solución incorrecta})$. Cambiar el denominador cambia la pregunta. Esta precisión evita confundir aceptación engañosa con frecuencia de todos los errores.

Para evaluar un agente de ventas, una validación estructural se puede complementar con comparación contra totales obtenidos de una fuente de referencia, trazabilidad del período, denominador correcto y ausencia de causas inventadas. Aceptar JSON no basta.

> [!question]- ¿Un segundo LLM que diga «correcto» vuelve confiable al verificador?
> No por sí solo. Necesita criterios, calibración y comparación con casos conocidos; puede compartir errores con el actor. Una señal ejecutable útil reduce parte de la incertidumbre, pero también hay que comprobar su cobertura.

Fuentes: notebook del martes, celda 12; [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/sesion-12.pdf#page=15|PDF 15–16]]; [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/fuentes/papers/s3-agentes/shinn-2023-reflexion.pdf#page=8|artículo, tablas 2–3, PDF 8]]. Los errores Python se reprodujeron en [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/Practica/s12_laboratorio_local.py|s12_laboratorio_local.py]].

---

← [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/73 S12 - Reflexion entre intentos memoria y aprendizaje|Anterior]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/75 S12 - Plan-and-Execute y elección de patrones|Siguiente]] →

