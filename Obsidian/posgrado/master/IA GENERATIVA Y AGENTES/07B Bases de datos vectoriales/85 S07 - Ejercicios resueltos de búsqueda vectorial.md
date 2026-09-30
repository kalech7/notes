---
title: "85 S07 - Ejercicios resueltos de búsqueda vectorial"
created: 2026-09-29
fecha: 2026-09-22
capitulo: 7
sesion: "07"
tags:
  - maestria/ia-generativa
  - recuperacion
  - bases-vectoriales
---

# 85 S07 - Ejercicios resueltos de búsqueda vectorial

[[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/07B Bases de datos vectoriales/79 S07 - Guía de búsqueda vectorial e índices|Guía de sesión 07]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

Estos ejercicios unen el costo del índice con la calidad de RAG. Todas las cifras propias son didácticas. No representan un benchmark ejecutado de IVF o HNSW.

## Cuentas y parámetros

> [!question]- 1. Hay 200000 vectores de 128 dimensiones. ¿Cuántas multiplicaciones pide comparar cada uno mediante producto punto?
> $200000\times128=25600000$. Faltan sumas, selección top-k y transferencia de memoria; no se convierte automáticamente a milisegundos.

> [!question]- 2. N=100000, nlist=64, nprobe=4. ¿Cuántas comparaciones aproxima la fórmula equilibrada?
> $64+(100000/64)\times4=6314$. Cuenta centroides y candidatos, no solo vecinos devueltos. Si las listas no tienen igual tamaño, se suman sus tamaños reales.

> [!question]- 3. ¿Abrir todas las listas vuelve exacto a cualquier IVF?
> Para IVFFlat sin compresión, mismo conjunto y sin otros cortes, recupera la búsqueda exhaustiva. En IVF-PQ puede persistir error de cuantización; abrir todas las celdas solo elimina la omisión de listas.

> [!question]- 4. ¿Qué diferencia hay entre nlist, nprobe y k?
> nlist define cuántas celdas tiene el índice; nprobe cuántas abre una consulta; k cuántos resultados solicita. No son intercambiables.

> [!question]- 5. ¿Por qué puede perderse el vecino si eliges el centroide correcto?
> El centroide más cercano a la consulta no necesariamente contiene su punto más cercano. En la frontera, un punto de otra celda puede estar más cerca que todos los examinados.

> [!question]- 6. ¿Qué puedes cambiar en HNSW sin rehacer el grafo existente?
> Normalmente ef_search controla exploración por consulta. M y la calidad de construcción afectan el grafo; cambiar su configuración no rehace las conexiones existentes y puede requerir reindexar.

## Métricas y memoria

> [!question]- 7. Exacto={1,2,3,4,5}; ANN={1,3,5,7,9}. ¿Recall del índice?
> Intersección={1,3,5}, así que $3/5=0,6$. La relevancia para el usuario requiere una referencia diferente.

> [!question]- 8. ¿Recall 0,99 y p99=800 ms significan lo mismo?
> No. Recall es coincidencia con vecinos exactos; p99 es un percentil de tiempos. Bajar ef_search puede probarse para reducir exploración, midiendo cuánto recall se pierde.

> [!question]- 9. ¿Cuánta memoria bruta ocupa un millón de vectores de d=384 con float32?
> $10^6\times384\times4=1536000000$ bytes, o 1,536 GB decimales. Faltan índice, metadatos y memoria de proceso. En GiB el valor numérico cambia.

> [!question]- 10. ¿Un índice con recall 1 puede tener recuperación mala?
> Sí. Puede reproducir exactamente un ranking que no contiene la evidencia de la pregunta. Por ejemplo, los embeddings podrían no representar el dato necesario o un filtro podría excluirlo.

> [!question]- 11. ¿Subir ef_search arregla Hit Rate 0,55 si recall promedio es 0,98?
> No se puede prometer. Se compara Hit Rate con búsqueda exacta bajo mismos datos y filtros. Si sigue en 0,55, se investiga antes o después del índice. El promedio puede ocultar fallas en consultas críticas.

> [!question]- 12. ¿La latencia del índice es la del chatbot entero?
> Solo si el alcance declarado las hace coincidir. Normalmente faltan embedding de consulta, red, contexto y generación. Tampoco es válido sumar percentiles de componentes como si fueran el percentil exacto del total.

## Base vectorial y operación

> [!question]- 13. ¿Para qué sirve el payload si ya hay un vector?
> Para vincular el resultado con texto, fuente y propiedades utilizables. El vector ayuda al ranking; no contiene un documento que el generador pueda leer literalmente. Alternativamente, el ID puede apuntar a otro almacén.

> [!question]- 14. ¿Una demo en memoria con una FAQ acertada valida el índice y encoder?
> No por sí sola. Hay que conocer generación de vectores, referencia exacta, preguntas de evaluación y mediciones. Demuestra una operación de la API, no una calidad general.

> [!question]- 15. ¿El contenedor conserva siempre los datos después de borrarlo y crearlo otra vez?
> No. Persistencia exige almacenamiento durable configurado y una política de recuperación. Correr un proceso en contenedor y preservar sus datos son responsabilidades distintas.

## Caso integrado: dónde intervenir

Tienes una colección de reglamentos, consulta sobre devolución de matrícula, recall del índice 0,98 y una respuesta errónea. El diagnóstico se puede organizar así:

1. Comprobar que el texto con el plazo se extrajo y que su versión es la que corresponde.
2. Verificar que el fragmento se representó de forma compatible con consulta y métrica.
3. Ejecutar exacto con el mismo filtro y comparar evidencia recuperada frente a ANN.
4. Comprobar si el fragmento pertinente entra al contexto final.
5. Comparar las afirmaciones de la respuesta con ese contexto.

Si el exacto tampoco recupera la evidencia, subir exploración no alcanza a resolver la causa. Si el exacto la recupera y ANN la omite, se mide una nueva configuración del índice. Si ambos la recuperan pero el contexto la elimina, se ajusta selección; si llega al prompt y la respuesta cambia el plazo, se revisa generación y verificación.

Esta ruta enlaza con [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/08 RAG fragmentación y recuperación/40 S08 - Diagnóstico de fallos y decisiones del taller|40 S08 - Diagnóstico de fallos y decisiones del taller]] y [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/09 Evaluación de RAG y patrones avanzados/48 S09 - Diagnóstico experimentos y Taller 2|48 S09 - Diagnóstico experimentos y Taller 2]]. Identificar la etapa permite justificar una mejora concreta, sin atribuir todo error a «la base vectorial».

Fuente: síntesis de [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/sesion-07.pdf|sesion-07.pdf]] y de las notas 79–84. Los ejercicios y soluciones son propios.

---

← [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/07B Bases de datos vectoriales/84 S07 - Colecciones payload filtros y operación|Anterior]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/08 RAG fragmentación y recuperación/34 S08 - Guía para entender fragmentación y recuperación|Siguiente]] →
