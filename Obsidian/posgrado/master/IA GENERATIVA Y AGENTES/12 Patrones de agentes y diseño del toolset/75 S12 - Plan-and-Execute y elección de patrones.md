---
title: "75 S12 - Plan-and-Execute y elección de patrones"
created: 2026-09-29
fecha: 2026-09-29
capitulo: 12
sesion: "12"
tags:
  - maestria/ia-generativa
  - agentes
  - estudio
---

# 75 S12 - Plan-and-Execute y elección de patrones

[[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/69 S12 - Guía para entender patrones y toolsets|Guía de la sesión 12]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

**Plan-and-Execute** separa crear un plan de ejecutarlo. El planificador produce pasos antes de actuar; el ejecutor lleva a cabo esos pasos y registra resultados. Puede añadirse una revisión del plan cuando las observaciones invalidan sus supuestos.

## 1. El plan de ventas y su dependencia

Un plan posible es: consultar marzo, consultar abril, calcular variación y redactar. Las dos consultas son independientes si la fuente y la definición ya están establecidas. El cálculo depende de ambas. Redactar depende del resultado y de su evidencia.

![[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Recursos visuales/55-s12-plan-y-cambio.png|55-s12-plan-y-cambio.png]]

La caja izquierda contiene un plan previo. El ejecutor realiza una parte y recibe una observación. La caja roja representa una condición que lo invalida: falta abril. La verde cambia la estrategia, por ejemplo para pedir otro período. El retorno explica por qué replanificar crea otro bucle y necesita límites.

Un ejecutor puede usar ReAct para resolver uno de los pasos. Separar fases no significa que toda ejecución esté prohibida de decidir detalles locales; significa que la estrategia global se hizo explícita antes.

## 2. Qué aporta un plan y dónde falla

Un plan hace visibles dependencias y supuestos. Permite revisar operaciones antes de ejecutarlas y comprobar si falta una etapa. En tareas largas puede evitar cambiar de objetivo después de cada resultado.

Pero el entorno puede desmentirlo. Si falta abril, insistir en la resta produce una respuesta sin base. **Replanning** significa actualizar el plan según lo observado, conservando lo que sigue válido. No significa ejecutar de nuevo todos los pasos por costumbre.

El máximo de replanes y el presupuesto de toda la corrida deben vivir fuera del modelo. Si el planificador puede producir subplanes ilimitados, un máximo de pasos dentro de cada subplan no acota el sistema completo.

## 3. No hay una garantía de menor costo

Un ejemplo simplificado con $n$ pasos puede necesitar una llamada para planificar, $n$ llamadas del ejecutor y otra para sintetizar: $n+2$. Si replanifica $r$ veces, añade esas llamadas y potenciales repeticiones. Si un paso necesita varias decisiones, $n$ ya no equivale al número de llamadas.

El ejecutor podría usar un modelo con menor costo, pero eso es una decisión que requiere medición de calidad y precio vigentes. La nota enseña el mecanismo sin asumir tarifas. «Una llamada por paso» de ReAct y «×2–4» de Reflexion son aproximaciones del curso, no leyes ni resultados universales de sus papers.

Para dos consultas independientes, paralelizar puede reducir una parte de latencia de $t_1+t_2$ a aproximadamente $\max(t_1,t_2)$ más coordinación. No reduce necesariamente la suma de consumo. El paso dependiente debe esperar ambos resultados.

## 4. Comparación práctica

| Situación | Organización razonable | Razón |
| --- | --- | --- |
| Secuencia estable, siempre la misma | Pipeline fijo | El programador ya conoce la ruta |
| Próximo paso depende de lo encontrado | ReAct | Permite adaptar consultas a observaciones |
| Muchas dependencias visibles y revisión previa útil | Plan-and-Execute | Hace explícita la estrategia |
| Una salida se puede evaluar y corregir | Reintentos con feedback; Reflexion cuando corresponde | Incorpora una lección comprobable |
| No hay criterio fiable para aceptar | Mejorar la evaluación antes de añadir autocorrección | Evita aceptar o romper respuestas por señales débiles |

No es una competencia de nombres: puedes combinar plan global, ejecución adaptativa y evaluación entre intentos. La complejidad solo se justifica si resuelve un problema observado.

## 5. Clasificar la lista de diez con criterio

La parte 5 del notebook mezcla niveles. Una clasificación útil para **esta actividad** es:

| Elemento | Nivel principal | Explicación |
| --- | --- | --- |
| ReAct | Control | Alterna decisiones, acciones y observaciones |
| Parallel Execution | Control y orquestación | Programa tareas independientes simultáneas |
| Agent Handoff | Control y orquestación | Transfiere responsabilidad y estado |
| LLM Workflow | Control, etiqueta amplia | Organiza un recorrido; puede ser fijo |
| Task Decomposition | Control cuando coordina subobjetivos | Divide, asigna y reúne resultados |
| Chain of Thought | Prompting o generación de razonamiento | No define por sí solo la ejecución externa |
| Self-Critique | Técnica o componente de evaluación | Critica un candidato; puede integrarse en un bucle |
| Self-Reflection | Técnica o componente de memoria y control | Extrae una lección; su implementación determina el nivel |
| Function Calling | Mecanismo | Estructura una solicitud de función |
| Episodic Memory | Memoria | Guarda experiencias de corridas anteriores |

El ejercicio pide una sola cubeta por elemento. Esa simplificación sirve para separar preocupaciones, pero algunos términos atraviesan niveles: descomposición puede ser solo una instrucción del prompt, y reflexión puede ser parte de un controlador completo.

**El supuesto «duplicado» requiere cautela.** Self-Critique y Self-Reflection se usan a veces como sinónimos en divulgación; no son universalmente el mismo método. Una crítica puede evaluar la salida actual, mientras una reflexión puede guardar una lección para intentos futuros. Sin el texto de la lista original, no es posible probar identidad exacta de implementaciones. No se confunden ambos automáticamente con el framework Reflexion del paper.

Que el autor venda memoria puede explicar su énfasis; no refuta ni valida su clasificación. Se puede contrastar definiciones, ejemplos ejecutables, evidencia y costos, y distinguir descripción de recomendación comercial.

## 6. Alcance de la evidencia

La página 18 avisa que sus fuentes de Plan-and-Execute son notas internas del curso y no los papers locales seleccionados. Esta ampliación explica el mecanismo; no presenta porcentajes de mejora para ese patrón. Las rutas internas citadas no se recibieron ni se consideran inspeccionadas.

> [!question]- ¿Cuál es la diferencia central con una cadena fija?
> En la cadena fija, la ruta la definió el programador. En Plan-and-Execute, el modelo propone el plan antes de recorrerlo. En ReAct, decide el próximo paso según el contexto de cada vuelta. Un sistema puede combinar estos niveles.

Fuentes: [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/sesion-12.pdf#page=18|PDF 18–19]], notebook del martes celdas 17–19. Comparaciones de llamadas, dependencias y clasificación matizada son elaboraciones pedagógicas.

---

← [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/74 S12 - Verificadores fiables y errores del notebook|Anterior]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/76 S12 - Toolsets validación errores y límites efectivos|Siguiente]] →

