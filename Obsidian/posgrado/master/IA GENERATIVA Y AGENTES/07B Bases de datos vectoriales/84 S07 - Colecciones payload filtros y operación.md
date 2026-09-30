---
title: "84 S07 - Colecciones payload filtros y operación"
created: 2026-09-29
fecha: 2026-09-22
capitulo: 7
sesion: "07"
tags:
  - maestria/ia-generativa
  - recuperacion
  - bases-vectoriales
---

# 84 S07 - Colecciones payload filtros y operación

[[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/07B Bases de datos vectoriales/79 S07 - Guía de búsqueda vectorial e índices|Guía de sesión 07]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

Una base de datos vectorial organiza consultas sobre vectores y los vincula con información utilizable. El índice es una parte del sistema. El resto permite identificar resultados, recuperar contenido, filtrar, actualizar y operar el servicio según sus capacidades.

## 1. Colección y punto

Una **colección** reúne puntos con una configuración compatible de dimensión y medida, entre otras opciones del motor. Un **punto** tiene un identificador, uno o más vectores según el diseño, y metadatos opcionales. **Payload** es el contenido o propiedades asociados al punto: por ejemplo texto, fuente, idioma y tema.

![[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Recursos visuales/62-s07-vector-payload-filtro.png|62-s07-vector-payload-filtro.png]]

La primera caja vincula un vector con `faq-17` y sus datos. La consulta aporta otro vector y un filtro por tema. La selección se restringe a candidatos elegibles y los ordena por similitud. El resultado permite volver al contenido que se usará en el contexto del LLM. El vector ayuda a buscar; no reemplaza el texto que explica la respuesta.

No es obligatorio guardar todo el documento como payload: un ID puede apuntar a texto en otro almacén. Sin payload, pueden devolverse IDs, puntajes y otros campos configurados; lo importante es conservar una correspondencia fiable con el contenido autorizado.

## 2. El filtro no sustituye el significado

Un filtro `tema = pagos` decide qué puntos cumplen una condición de metadatos. La similitud decide cuáles están cerca de la consulta dentro del conjunto permitido. Un filtro correcto puede mejorar pertinencia; uno mal etiquetado puede excluir justamente la evidencia necesaria.

Aplicar un filtro después de buscar un top-k global puede dejar muy pocos resultados: si solo uno de los diez candidatos pertenece a pagos, no significa que exista un solo punto pertinente entre todos los pagos. La consulta filtrada debe compararse con un exacto que tenga el mismo filtro. La implementación del motor determina cómo combina filtrado e índice.

Filtros tampoco son automáticamente un sistema de autorización: la aplicación debe construir y hacer cumplir las restricciones de acceso. No debería depender de que el modelo elija voluntariamente un filtro correcto.

## 3. Crear, insertar, consultar, actualizar

El fragmento de la presentación describe cuatro ideas:

1. Crear colección y declarar dimensión y métrica.
2. Insertar o actualizar puntos mediante `upsert`.
3. Consultar con vector, filtros y cantidad de resultados.
4. Usar IDs y payload para construir el contexto.

`Upsert` combina insertar un ID nuevo y actualizar uno existente según el contrato del servicio. Si se cambia de encoder, conservar dimensión no garantiza compatibilidad del espacio: puede requerirse recalcular vectores e indexar una versión nueva. Si se elimina un punto, deben considerarse también referencias, duplicados y la consistencia de metadatos.

La [documentación oficial de Qdrant sobre índices](https://qdrant.tech/documentation/manage-data/indexing/) distingue estructuras vectoriales y de payload. Esto refuerza la separación entre buscar por cercanía y facilitar condiciones sobre propiedades. El ejemplo docente no mide por sí solo toda esa operación.

## 4. Modo en memoria y servicio persistente

`QdrantClient(":memory:")` del PDF representa un modo local efímero. Sirve para estudiar la API sin un servidor aparte. Al terminar ese proceso se pierde ese almacenamiento en memoria.

Un cliente por URL habla con un servicio separado. Aparecen red, configuración, versiones, permisos, disponibilidad y almacenamiento. Un contenedor **no garantiza persistencia por existir**: para conservar datos después de reemplazarlo hace falta configurar almacenamiento durable apropiado. No se ejecutaron los comandos del PDF durante esta revisión.

El Taller 2 descrito exige el servicio en contenedor; se conserva como requisito académico de esa fuente. Las notas explican qué cambia operativamente, sin afirmar que el servidor de tu proyecto ya esté configurado así.

## 5. Qué demuestra la demo de vectores

El PDF dice que la actividad usa vectores de 64 dimensiones y remite a su función `embed_demo`, pero el código completo de `s2-mar` no está disponible. No conocemos por inspección directa cómo genera esos vectores.

Que una base devuelva una FAQ plausible no mide recall ANN sin referencia exacta; que responda rápido una vez no mide p50/p99; y multiplicar dimensión por cuatro solo estima almacenamiento bruto si realmente usa float32, no RAM total. La demo enseña el contrato colección–punto–consulta. No se debe convertir en evidencia de calidad de un encoder semántico ni benchmark del índice.

La respuesta rigurosa a la pregunta del PDF 22 es **ninguno de los tres está demostrado como medición completa por el fragmento mostrado**. Para confirmar la explicación docente basada en `embed_demo` haría falta el notebook. Estas notas no inventan su implementación.

## 6. Cómo decidir qué operar

Un motor se evalúa también por quién lo mantiene, filtros, actualizaciones, persistencia y recuperación. Una biblioteca ANN puede encajar en una aplicación; un servicio añade capacidades y costos operativos; una extensión puede aprovechar infraestructura existente.

Por ejemplo, el [README oficial de pgvector](https://github.com/pgvector/pgvector) describe una extensión de PostgreSQL con búsqueda exacta y opciones HNSW/IVFFlat. Esto no establece un umbral universal de millones ni demuestra que sea mejor para cualquier carga. Las frases «decenas de miles» y «millones» del material orientan órdenes de magnitud; se decide con necesidades y mediciones concretas.

Un archivo que solo fija versiones mínimas con `>=` permite instalaciones distintas. Reproducir una línea base exige registrar versiones realmente usadas, configuración, datos y consultas; un lockfile o entorno fijado ayuda, pero tampoco sustituye datos y semilla.

> [!question]- ¿Cambiar la dimensión sin reconstruir vectores conserva el sistema?
> No. La forma debe ser compatible con la colección y el espacio aprendido debe ser coherente entre documentos y consulta. Cambiar el encoder puede invalidar la comparabilidad incluso con dimensión idéntica.

Fuente: [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/sesion-07.pdf#page=19|PDF 19, 21–24]]. Documentación primaria enlazada consultada el 29 de septiembre de 2026. Se distingue contenido del PDF de verificación directa; no se instalaron motores.

---

← [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/07B Bases de datos vectoriales/83 S07 - Recall del índice latencia y memoria|Anterior]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/07B Bases de datos vectoriales/85 S07 - Ejercicios resueltos de búsqueda vectorial|Siguiente]] →
