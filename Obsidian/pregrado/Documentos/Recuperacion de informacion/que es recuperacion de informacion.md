La **Recuperación de Información** (Information Retrieval o IR) es la disciplina y el proceso de buscar, organizar y extraer información relevante (especialmente texto no estructurado o semi-estructurado) de grandes colecciones de documentos almacenados computacionalmente, con el objetivo de satisfacer la necesidad de información (query) de un usuario.

```mermaid
flowchart TD
    subgraph Creación del Índice (Offline)
        D[Colección de Documentos] --> C[Rastreo / Recolección]
        C --> P[Procesamiento de Texto y NLP]
        P --> I[(Índice Invertido)]
    end
    
    subgraph Fase de Búsqueda (Online)
        U[Usuario] -->|Consulta / Query| Q[Procesamiento de Consulta]
        Q --> M[Motor de Búsqueda\nConsulta el Índice]
        I -.-> M
        M --> R[Algoritmo de Ranking\nOrdenamiento por relevancia]
        R -->|Top Resultados| U
    end
```

> [!info] Explicación
> **Ejemplo clásico:** El buscador de Google. Entras buscando "receta pastel de chocolate" (la query). Google no lee toda la internet en ese milisegundo; ya tiene un "Índice" preconstruido. Usa tu query para buscar en el índice y extrae los documentos (páginas web) más relevantes ordenados mediante un algoritmo de ranking.

## La Tarea Principal
La tarea de los sistemas de recuperación es lograr que un usuario emita una consulta (una pregunta o un conjunto de palabras clave) hacia un gran corpus (biblioteca de documentos de texto), y el sistema le devuelva de inmediato el conjunto exacto de resultados relevantes, ordenados del mejor al peor, con tiempos de respuesta muy rápidos.

La recuperación de información va mucho más allá de una simple búsqueda de base de datos como "SELECT * FROM tabla WHERE palabra='pastel'". El IR moderno entiende contexto, sinónimos, faltas de ortografía e importancia del término.

## Relevancia vs Información Recuperada
La clave del éxito en un sistema de IR se mide evaluando la proporción entre lo que el sistema devuelve y lo que realmente le importaba al usuario.

Existen dos métricas fundamentales para medir la eficacia:
- **Precisión (Precision):** De todos los documentos que el sistema le devolvió al usuario, ¿cuántos eran verdaderamente relevantes? (Un sistema preciso no te muestra "basura").
- **Exhaustividad (Recall):** De todos los documentos relevantes que existían ocultos en toda la base de datos, ¿cuántos logró encontrar y devolver el sistema? (Un sistema exhaustivo no se deja ningún documento útil atrás).

> [!info] Explicación
> **El equilibrio Precisión-Recall:** Suele haber un "tira y afloja". Si un motor de búsqueda es muy estricto, tendrá alta precisión (0% basura), pero bajo recall (dejó documentos útiles atrás). Si es muy permisivo, tendrá alto recall (trajo todo lo útil), pero baja precisión (se coló mucha basura en los resultados).

## Notas relacionadas
- [[Índice invertido]]
- [[matriz termino frecuencia]]
- [[Modelos de recuperación]]
- [[ranking]]
