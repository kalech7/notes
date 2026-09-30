---
title: "Database Internals — Cobertura y validación de capítulos 9–11"
created: 2026-09-30
capitulo: 9
capitulos:
  - 9
  - 10
  - 11
tags:
  - lecturas/database-internals
  - arquitectura/sistemas-distribuidos
  - fuentes
---

# Detección de fallas, liderazgo y replicación

[[Obsidian/lecturas/database internals/00 Empieza aquí|Inicio del libro]] → [[Obsidian/lecturas/database internals/90 Fuentes y revisión/00 Índice|Fuentes y revisión]]

La fuente es el PDF «CamScanner 2026-09-30 16.59.pdf», de 45 páginas escaneadas, correspondiente a *Database Internals* de Alex Petrov. Tres subagentes leyeron visualmente los tres capítulos completos y elaboraron notas y gráficos; la integración revisó las explicaciones, los enlaces y las comprobaciones. El OCR sirvió de apoyo, especialmente para localizar secciones. Las páginas giradas se leyeron mediante imágenes orientadas, sin modificar el PDF conservado.

**Fuente conservada:** [[Obsidian/lecturas/database internals/Materiales/09 a 11 Detección de fallas liderazgo y replicación.pdf|Escaneo completo de capítulos 9–11]].

## Correspondencia de páginas

| Capítulo | Páginas PDF | Páginas impresas | Correspondencia | Ruta |
|---|---:|---:|---|---|
| 9 · Failure Detection | 1–9 | 195–203 | impresa = PDF + 194 | [[Obsidian/lecturas/database internals/09 Detección de fallas/00 Índice\|Detección de fallas]] |
| 10 · Leader Election | 10–18 | 205–213 | impresa = PDF + 195 | [[Obsidian/lecturas/database internals/10 Elección de líder/00 Índice\|Elección de líder]] |
| 11 · Replication and Consistency | 19–45 | 215–241 | impresa = PDF + 196 | [[Obsidian/lecturas/database internals/11 Replicación y consistencia/00 Índice\|Replicación y consistencia]] |

Las impresas 204 y 214 no están en el archivo. No se presume su contenido. Los capítulos 9 y 10 incluyen resumen y referencias; el 11 llega a su resumen en la impresa 241, sin bibliografía posterior. Las referencias a capítulos posteriores presentes en el libro no convierten esos capítulos en material leído.

## Mapa de temas y figuras

| PDF · impresas | Desarrollo presente | Figuras |
|---|---|---|
| 1–3 · 195–197 | Seguridad, vivacidad, calidad del detector, pings, heartbeats y detección sin timeout | 9-1 y 9-2 en PDF 3 |
| 4–5 · 198–199 | Continuación de contadores sin timeout y caminos justos, sondeos con intermediarios y detector phi-accrual | 9-3 en PDF 5 |
| 6–7 · 200–201 | Interpretación de phi, gossip y contadores de heartbeats | 9-4 en PDF 7 |
| 7–9 · 201–203 | Propagación por silencio, resumen y referencias | 9-5 en PDF 8 |
| 10–11 · 205–206 | Función del líder, estabilidad y relación con locks | — |
| 12–15 · 207–210 | Bully modificado, alternativas y división candidatos/ordinarios | 10-1 en PDF 13, 10-2 en PDF 14, 10-3 en PDF 15 |
| 15–17 · 210–212 | Invitación, anillo y acumulación de identidades | 10-4 en PDF 15, 10-5 en PDF 17 |
| 17–18 · 212–213 | Elección frente a consenso, resumen y bibliografía | — |
| 19–23 · 215–219 | Replicación, disponibilidad, CAP, harvest/yield y memoria compartida | — |
| 24–27 · 220–223 | Operaciones concurrentes, orden y modelos de consistencia | 11-1 en PDF 24 |
| 27–31 · 223–227 | Linealizabilidad, puntos de linealización, costos y registros atómicos | 11-2 en PDF 28, 11-3 en PDF 29, 11-4 en PDF 30 |
| 31–33 · 227–229 | Consistencia secuencial y relación con serializabilidad | 11-5 en PDF 33 |
| 33–37 · 229–233 | Causalidad, dependencias, historias divergentes y seguimiento de contexto | 11-6 y 11-7 en PDF 34, 11-8 en PDF 35, 11-9 en PDF 36 |
| 37–38 · 233–234 | Garantías de sesión y consistencia eventual | — |
| 39–41 · 235–237 | Consistencia ajustable, quórums, escrituras incompletas y réplicas testigo | — |
| 42–44 · 238–240 | Consistencia eventual fuerte, CRDTs y modelos por estado/operaciones | — |
| 44–45 · 240–241 | Repaso de modelos y resumen | — |

Las figuras se explican conceptualmente dentro de las notas. Los PNG son recreaciones didácticas y diagramas propios: no se distribuyen fotografías recortadas de las figuras del libro. Un recurso puede reunir varias figuras relacionadas.

## Precisiones técnicas

Estas aclaraciones separan lo que afirma el escaneo de la explicación técnica necesaria para interpretar sus ejemplos:

- **Sospecha y evidencia.** Un timeout o un phi alto no demuestra que el proceso haya muerto. También puede reflejar una demora, una pausa o una partición. La vivacidad necesita condiciones de progreso; una sospecha no autoriza a abandonar las reglas de seguridad del protocolo.
- **Phi.** La transformación `−log10(1 − F(t))` cuantifica cuán inusual es el tiempo de silencio bajo el modelo de intervalos observado. No es una probabilidad posterior de caída. Un umbral requiere calibración y no proporciona garantías absolutas.
- **Gossip.** Con frecuencia y fanout constantes, el número agregado de mensajes por ronda puede crecer linealmente. Si cada mensaje incluye una tabla de tamaño proporcional al número de nodos, sus bytes no tienen por qué crecer linealmente.
- **Figura 9-5.** En PDF 8, el inciso d) menciona la ausencia de P1 y P2. La figura y los pasos previos corresponden a la ausencia de P4 y P2. Las notas explican esa errata y la propagación de indisponibilidad del grupo mediante silencio inducido de nodos aún vivos.
- **Bully.** El pie de PDF 12 identifica una variante modificada. Las notas describen esa variante, sin atribuir sus pasos literalmente a todas las versiones de Bully. En la optimización por candidatos, el máximo se elige entre candidatos elegibles, no entre todos los nodos ordinarios.
- **Elección y consenso.** La mayoría necesita reglas sobre rondas, votos y legitimidad de las acciones. Elegir un nombre no replica un log ni impide por sí solo que un líder antiguo siga intentando escribir.
- **CAP.** Su C es linealizabilidad; su A exige respuesta eventual a las peticiones dirigidas a procesos no fallidos bajo el modelo. La caja de PDF 22 mezcla esa C con expresiones de atomicidad e invariantes transaccionales; las notas distinguen ambos significados. CAP trata el conflicto durante una partición y no una elección permanente de «dos de tres».
- **Historias concurrentes.** En la figura 11-2 las escrituras se solapan. Una ilustración que escoge W1 antes que W2 no significa que el tiempo real obligue a ese orden. Una operación cuya respuesta se pierde puede haber surtido efecto; una historia con operaciones pendientes debe tratarse con esa posibilidad.
- **Quórums.** `R + W > N` garantiza intersección dentro de un conjunto fijo de réplicas, pero necesita reglas de versiones, concurrencia y reparación para ofrecer garantías adicionales. El contraejemplo de escritura incompleta muestra una lectura nueva seguida de una antigua. La intersección no basta para inferir linealizabilidad.
- **Testigos.** Un testigo con metadatos no sirve un payload que nunca almacenó. El ejemplo del libro permite almacenamiento provisional del valor y recuperación antes de retirar esas copias; las garantías dependen del protocolo completo.
- **CRDTs.** La preparación de una operación puede carecer de efectos; su aplicación modifica el estado. La expresión de PDF 42 sobre efectos secundarios necesita esa distinción. El G-counter descrito mediante vectores y máximo por componente es un ejemplo por estado; un contador por operaciones necesita las garantías de entrega correspondientes.

Los ejemplos, los ejercicios y los programas son elaboración propia. Comprueban modelos acotados y no implementan un protocolo de consenso para producción, fallas físicas ni un motor de almacenamiento real.

## Recursos y comprobaciones

Se crearon **33 notas**: ocho para el capítulo 9, ocho para el 10 y diecisiete para el 11, incluyendo sus índices y laboratorios. Los **18 PNG** (5 + 5 + 8) fueron inspeccionados visualmente; se corrigieron textos y un destino de imagen. Cada recurso está integrado con una explicación en prosa. La revisión cruzada entre subagentes contrastó las notas de liderazgo y replicación con el escaneo.

| Capítulo | Recursos regenerables | Ejercicios y comprobaciones |
|---|---|---|
| 9 | [[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 09/generar_graficos.py\|Cinco diagramas con Pillow]] | [[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 09/laboratorio.py\|Laboratorio ejecutado]]: phi, frescura de contadores gossip y silencio FUSE |
| 10 | [[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 10/generar_liderazgo.py\|Cinco diagramas con Pillow]] | Conteos de mensajes, rangos, candidatos, fusiones, anillo y mayoría explicados en el repaso |
| 11 | [[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 11/generar_graficos.py\|Ocho diagramas con Pillow]] | [[Obsidian/lecturas/database internals/Materiales/Laboratorios/11 consistencia_modelo.py\|Laboratorio ejecutado]]: nueve intersecciones, regresión 1→0, reparación 1→1 y G-counter convergente bajo seis permutaciones y duplicados |

Los tres bloques Mermaid de esta ampliación —dos en liderazgo y uno en la ruta general— renderizaron correctamente con mermaid-cli y Chrome. Las 45 páginas conservadas coinciden byte a byte con el archivo original: SHA-256 `daf4710af23f66c69a515008418c5b983c93b51a6db285182b8a3e33722e1d95`.

La validación estructural comprobó propiedades YAML, wikilinks, imágenes, navegación, enlaces locales y páginas de las anclas del PDF, sin errores. El alcance son las notas nuevas, la cobertura y los índices modificados. El [[Obsidian/lecturas/database internals/90 Fuentes y revisión/validacion_capitulos_09_11.json|informe de validación]] registra los conteos finales. Puede regenerarse con [[Obsidian/lecturas/database internals/90 Fuentes y revisión/validar_capitulos_09_11.py|el validador]] usando `uv run --with pyyaml --with pymupdf`; la inspección visual y la ejecución de Mermaid se registran aquí por separado.

---

← [[Obsidian/lecturas/database internals/90 Fuentes y revisión/07 Cobertura y validación de sistemas distribuidos|Anterior: capítulo 8]] · [[Obsidian/lecturas/database internals/90 Fuentes y revisión/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/09 Detección de fallas/00 Índice|Siguiente: comenzar capítulo 9]] →
