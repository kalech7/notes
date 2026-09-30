---
title: "Fuentes y ampliación del capítulo 14"
created: 2026-09-29
capitulo: 14
tags:
  - lecturas/software-architecture
  - arquitectura/service-based
  - revision/fuentes
---

# Fuentes y ampliación del capítulo 14

[[Obsidian/lecturas/Fundamentals of Software Architecture/14 Arquitectura basada en servicios/00 Índice|← Capítulo 14]]

Fuente: `CamScanner 2026-09-29 19.15.pdf`, capítulo 14, *Service-Based Architecture Style*. Se leyeron visualmente todas las páginas del escaneo, no solo encabezados o OCR. El contenido se explica con redacción propia; no se ejecutaron instrucciones de la fuente.

Copia intacta: [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/11 Arquitectura basada en servicios.pdf#page=1|Materiales/11 Arquitectura basada en servicios.pdf]]. Tiene 18 páginas. Correspondencia: **impresa = PDF + 208**; impresas 209–226. Las páginas PDF 4, 14 y 18 tienen el folio cortado o ausente; se infiere 212, 222 y 226 por continuidad de la secuencia y del texto. No faltan páginas en esa secuencia.

## Mapa de las 18 páginas

| PDF | Impresa | Contenido cubierto | Notas principales |
|---|---|---|---|
| 1 | 209 | Introducción, macrocapas, servicios gruesos, recomendación de cantidad | 01 |
| 2 | 210 | Figura 14-1, instancias, balanceo, acceso remoto, localizador, base común | 01, 07 |
| 3 | 211 | Figura 14-2, organización interna por capas o dominios | 02 |
| 4 | 212 inferida | Fachada, OrderService, orquestación interna, ACID, tarjeta vencida | 02, 03 |
| 5 | 213 | OrderPlacement/PaymentService, compensación, costo de granularidad, UI | 02, 03, 04 |
| 6 | 214 | Figura 14-3, UI común, por dominios o servicio, clientes/empacado/soporte | 04 |
| 7 | 215 | Figura 14-4, gateway, datos y preferencia por compartir frente a muchas llamadas | 04, 05 |
| 8 | 216 | Figura 14-5, topologías de base, entidades y biblioteca compartida | 05, 06 |
| 9 | 217 | Figura 14-6, antipatrón de biblioteca global, partición lógica | 06 |
| 10 | 218 | Figura 14-7, cinco dominios de datos, Común, control y granularidad lógica | 06 |
| 11 | 219 | Nube, dos riesgos, gobierno, excepción Notificaciones, coordinación UI/gateway | 04, 07 |
| 12 | 220 | Equipos por dominio y cuatro topologías de equipos | 08 |
| 13 | 221 | Figura 14-8, estrellas/costo/partición/quanta, cambio de Evaluación | 08, 09 |
| 14 | 222 inferida | Figura 14-9, dos quanta de Going Green | 09 |
| 15 | 223 | Agilidad, pruebas, entregas, falla, escala, elasticidad, caché, costo y errata | 07, 08, 09 |
| 16 | 224 | DDD, transacciones, modularidad y seis pasos completos de Going Green | 03, 09, 10 |
| 17 | 225 | Figura 14-10, instancias selectivas y tres UI | 09 |
| 18 | 226 inferida | Red, dos bases físicas, acceso direccional/sincronización, cambio y migración selectiva | 09, 10 |

## Cobertura de todas las figuras

| Figura | PDF / impresa | Contenido | Recreación o explicación |
|---|---|---|---|
| 14-1 | 2 / 210 | UI, cuatro servicios y base común | Imagen c14-01, nota 01 |
| 14-2 | 3 / 211 | Diseño interno por capas y subdominios | Imagen c14-02, nota 02 |
| 14-3 | 6 / 214 | Tres variantes de UI | Imagen c14-04, nota 04 |
| 14-4 | 7 / 215 | Gateway o proxy entre UI y servicios | Imagen c14-04, nota 04 |
| 14-5 | 8 / 216 | Base única, agrupación y base por servicio | Imagen c14-05, nota 05 |
| 14-6 | 9 / 217 | Biblioteca global de entidades y propagación | Imagen c14-06, nota 06 |
| 14-7 | 10 / 218 | Bibliotecas por dominios lógicos; Común conserva alcance global | Imagen c14-06 y tabla completa de dependencias, nota 06 |
| 14-8 | 13 / 221 | Tabla ordinal de características | Imagen c14-08 y tabla en nota 08 |
| 14-9 | 14 / 222 | Going Green, siete servicios y dos quanta | Imagen c14-07 y explicación completa, nota 09 |
| 14-10 | 17 / 225 | Going Green, seguridad y datos entre zonas | Imagen c14-07 con alternativas diferenciadas, nota 09 |

Las imágenes son diagramas originales en español y combinan figuras cuando ayuda a explicar una decisión. No son capturas del libro. c14-03 agrega la comparación transaccional del texto, aunque no corresponde a una figura numerada.

## Ejemplos del libro preservados

- Comercio electrónico: fachada de OrderService registra pedido e ID, aplica pago y actualiza inventario. Rechazo por tarjeta vencida; contraste con OrderPlacement y PaymentService, y necesidad de compensación (PDF 4–5).
- Tres públicos de UI: clientes que compran, empaquetadores y soporte (PDF 6).
- Entidades: Común, Clientes, Facturación, Pedidos y Seguimiento; Pedidos usa además Clientes y todos usan Común. Cambiar Facturación afecta a su consumidor, cambiar Común puede alcanzar a todos (PDF 9–10).
- Excepción de comunicación entre dominios: Procesamiento de pedidos solicita a Notificación del cliente el envío de correo (PDF 11).
- Going Green: seis pasos de negocio, siete servicios, tres UI, dos bases, más instancias solo para Cotización y Estado, cambios frecuentes en Evaluación, acceso interno hacia datos públicos o sincronización, división selectiva futura de Evaluación por dispositivo (PDF 13–18).

ReCompra, los cálculos de conexiones, regresión, porcentajes de cambios y flujos de publicación son elaboraciones propias explícitas. No se presentan como datos empíricos del libro.

## Erratas y precisiones

1. **Contradicción real de estrellas:** figura 14-8 tiene tolerancia a fallos con tres estrellas; prosa PDF 15 afirma cuatro. La reproducción usa tres y muestra la discrepancia. Disponibilidad se comenta en prosa, pero no tiene fila de valoración propia.
2. **ACID tiene alcance transaccional:** agrupar código en un servicio facilita una transacción local; no hace atómicos todos sus efectos ni revierte pagos remotos. Compartir base tampoco une automáticamente transacciones de sesiones distintas. La comparación del libro simplifica el pago y se explica su límite.
3. **Microservicios pueden usar ACID local.** BASE describe garantías/compromisos y no es por sí solo un protocolo transaccional. Saga y compensación son mecanismos concretos; compensar no borra observaciones previas y puede fallar.
4. **Cantidad cercana a doce:** recomendación práctica del capítulo, especialmente con base común; no es un límite técnico ni una ley de clasificación. Instancias y pools cuentan para conexiones.
5. **Partición lógica de datos no es partición física de filas.** Bibliotecas por dominio pueden conservar un único motor y su dependencia operacional.
6. **Biblioteca global y cambios:** la fuente describe un antipatrón. Un cambio incompatible amplía consumidores a coordinar, pero una adición compatible no obliga necesariamente a redesplegar todos. Versionar el paquete no demuestra compatibilidad del esquema simultáneo.
7. **Quanta:** figura 14-9 cuenta dos grupos según UI y datos; figura 14-10 añade acceso interno a datos públicos. Si es una dependencia síncrona obligatoria puede acoplar la operación interna a la disponibilidad pública. No se afirma aislamiento absoluto ni se cuenta automáticamente un quantum por servicio.
8. **Dos variantes direccionales de datos:** servicio Recepción→base pública para acceso directo, o sincronización base interna→base pública. La imagen distingue ambas y no confunde acceso de servicio con replicación. El libro no especifica sus garantías ni exige ejecutar ambas.
9. **SOA, microservicios y service-based:** no son sinónimos. La nota 01 distingue este estilo por granularidad, despliegues y datos, sin atribuirle un bus empresarial obligatorio.
10. **Nube y serverless:** el capítulo prefiere contenedores para estos dominios amplios, pero no exige Docker/Kubernetes ni declara imposible otro entorno.
11. **Granularidad y cambio:** una entrega de un módulo dentro del servicio publica todo el servicio. Separarlo puede reducir alcance si mantiene un contrato compatible; no elimina pruebas de integración ni coordinación por cambios contractuales.
12. **Orquestación:** fachada coordina dentro de un dominio; UI/gateway pueden coordinar entre dominios. Son escalas diferentes y ninguna confiere atomicidad automáticamente.

## Fuentes técnicas primarias para los matices

Consultadas el 2026-09-29; se usan solo para precisiones técnicas, no para sustituir el capítulo:

- [PostgreSQL 16, transacciones](https://www.postgresql.org/docs/16/tutorial-transactions.html): alcance de BEGIN/COMMIT/ROLLBACK en la base (nota 03).
- [AWS, Saga patterns](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/saga-patterns.html): secuencia de transacciones locales, continuación y compensación (nota 03).
- [Stripe, solicitudes idempotentes](https://docs.stripe.com/api/idempotent_requests): reintento de la misma intención sin duplicar su operación (nota 03).

## Reproducción de imágenes y comprobaciones

Generador reproducible: `Recursos visuales/Capítulo 14/generar_visuales.py`. Ejecución con `uv run --with pillow` y ese archivo. Fuente Arial del sistema macOS; si se lleva a otro sistema, se sustituyen las rutas de fuente por una tipografía local equivalente. Produce ocho PNG de 1600 × 1100. Usa una tabla de estrellas ordinales, no una serie cuantitativa.

Se revisaron visualmente los ocho PNG con view_image. Se corrigieron etiquetas y flechas que se prestaban a confusión: UI común abarca todas sus conexiones, rótulo de dominios ocupa dos líneas y Going Green diferencia acceso desde Recepción y sincronización. Todas las imágenes tienen explicación inmediata en prosa dentro de su nota.

Se verificó que la copia PDF es idéntica byte a byte a la fuente. SHA-256: `ba1ee603acc6a21217f2183eeddd7fa8b84182c2505fcd05c58675d48451be69`.

Lectura y cobertura de las 18 páginas verificadas; revisión independiente coincide en correspondencia, figuras, estrellas y matices. **Integración y validación completadas el 2026-09-29:** 598 wikilinks, 524 enlaces Markdown locales, 84 referencias a páginas PDF y YAML de las 26 notas nuevas comprobados sin incidencias. Los 13 bloques Mermaid nuevos se renderizaron correctamente, incluidos los ocho de este capítulo. Se revisaron las 16 imágenes nuevas, incluidas sus ocho imágenes. Las cifras globales corresponden a la integración de los capítulos 13–14 y la comparación transversal. Los índices generales y la cobertura se actualizaron a 11 PDF y 217 páginas.

---

[[Obsidian/lecturas/Fundamentals of Software Architecture/14 Arquitectura basada en servicios/00 Índice|← Volver al capítulo]]
