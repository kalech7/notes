---
title: RAG - chunking, embeddings, recuperación y reranking
tags:
  - master/matematicas-programacion
  - llm
  - rag
  - retrieval
---

# RAG: chunking, embeddings, recuperación y reranking

![[../assets/ruta maestra ia/10-rag-pipeline.gif|900]]

## Idea

Retrieval-Augmented Generation separa dos tareas:

1. recuperar evidencia relevante;
2. generar una respuesta condicionada por esa evidencia.

```mermaid
flowchart LR
    A[Documentos] --> B[Segmentar]
    B --> C[Embeddings e índice]
    Q[Pregunta] --> D[Recuperar candidatos]
    C --> D
    D --> E[Reranking]
    E --> F[Contexto con fuentes]
    F --> G[LLM]
    G --> H[Respuesta y citas]
```

## Ingesta

- extraer texto preservando títulos y páginas;
- limpiar ruido sin borrar significado;
- conservar metadatos y permisos;
- asignar identificadores estables;
- registrar versión del documento.

## Chunking

Un chunk debe ser recuperable y contener suficiente contexto. Opciones:

- longitud fija con solapamiento;
- por párrafo/sección;
- estructura semántica;
- jerárquico: sección grande y fragmento pequeño.

Chunks demasiado pequeños pierden contexto; demasiado grandes reducen precisión y consumen ventana.

## Embeddings

Cada chunk se representa como vector $v_i$. Para consulta $q$:

$$\cos(q,v_i)=\frac{q^Tv_i}{\|q\|\|v_i\|}.$$

Si vectores están normalizados, maximizar coseno equivale a maximizar producto interno.

## Recuperación léxica y densa

- léxica: coincide términos exactos, útil para nombres/códigos;
- densa: aproxima similitud semántica;
- híbrida: combina ambas.

## Reranking

La primera etapa recupera muchos candidatos con bajo coste. Un reranker más caro compara consulta-documento y reordena los mejores.

## Context construction

Incluye:

- texto del chunk;
- título/documento/página;
- separación clara entre instrucciones y evidencia;
- límite de tokens;
- orden por relevancia o estructura.

No permitas que texto recuperado actúe como instrucción privilegiada.

## Evaluación por capas

Recuperación:

- Recall@k;
- precision@k;
- MRR o nDCG cuando importa ranking.

Generación:

- corrección;
- fidelidad a evidencia;
- cobertura;
- calidad de citas;
- abstención cuando falta soporte.

> [!important] Diagnóstico en dos etapas
> Si la evidencia correcta no fue recuperada, no es un fallo primario del generador. Si fue recuperada y la respuesta la contradice, el problema está en construcción de contexto, instrucciones o generación.

## Seguridad y permisos

El índice debe filtrar por permisos antes de entregar chunks. RAG no debe convertir acceso parcial en búsqueda global.

## Autoevaluación

1. ¿Qué compromiso controla chunking?
2. ¿Cuándo ayuda recuperación híbrida?
3. ¿Qué aporta reranking?
4. ¿Cómo separas error de retrieval y de generation?

---

Anterior: [[17 Fine-tuning eficiente - LoRA, QLoRA y PEFT]] · Siguiente: [[19 Evaluación, alucinaciones, seguridad y prompt injection]]
