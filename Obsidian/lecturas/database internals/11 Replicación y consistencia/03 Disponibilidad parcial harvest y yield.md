---
title: "Database Internals — Capítulo 11 · Disponibilidad parcial harvest y yield"
created: 2026-09-30
libro: "Database Internals"
capitulo: 11
tags:
  - lecturas/database-internals
  - arquitectura/sistemas-distribuidos
---

# Disponibilidad parcial harvest y yield

[[Obsidian/lecturas/database internals/11 Replicación y consistencia/00 Índice|Índice del capítulo]]

El capítulo introduce **harvest** y **yield** para medir servicio degradado de forma más útil que un «funciona/no funciona». No sustituyen el teorema CAP: describen objetivos de una aplicación que acepta respuestas incompletas bajo condiciones definidas.

**Harvest** mide la completitud de una respuesta frente a los datos que deberían participar en ella. **Yield** mide la proporción de solicitudes completadas con éxito respecto a las intentadas. Un servidor encendido puede estar saturado y reducir yield aunque su uptime sea excelente.

## Dos denominadores diferentes

Ejemplo propio: un buscador debería consultar 100 documentos, pero un shard inaccesible contiene 8. Contestar usando los otros 92 produce un harvest de `92/100=0,92`. Si durante un período llegaron 1 000 consultas y 970 terminaron correctamente, el yield es `970/1 000=0,97`. Son medidas independientes: se puede responder casi siempre con contenido incompleto o fallar muchas solicitudes mientras las exitosas son completas.

| Política ilustrativa | Solicitudes exitosas | Datos recuperados por respuesta | Efecto |
|---|---:|---:|---|
| Fallar cuando falta cualquier shard | Puede disminuir | Completos en los éxitos | Conserva completitud |
| Consultar sólo shards disponibles | Puede aumentar | Parciales | Sacrifica harvest |
| Separar consultas críticas de otras | Según tipo de operación | Según contrato | Degradación consciente |

Estos números son ejemplos de cálculo, no mediciones del libro. En una consulta cuyo conjunto verdadero sea desconocido, medir harvest exacto puede ser difícil. El sistema necesita un denominador significativo: shards previstos, documentos conocidos u otro indicador ligado a su contrato.

## La corrección sigue siendo una condición

Una tienda podría mostrar un catálogo parcial si informa que ciertas categorías no están disponibles. Para determinar si un pago ya fue cobrado, omitir el shard que contiene pagos y responder «no existe» puede causar un segundo cobro. La tolerancia a información parcial depende de la semántica, no del hecho de que el resultado tenga aspecto normal.

El libro propone continuar atendiendo usuarios cuyas particiones de datos siguen disponibles y exigir completitud para datos críticos. Eso obliga a distinguir una **partición de datos** —repartición del contenido entre shards— de una **partición de red** —interrupción de mensajes—. La primera organiza almacenamiento; la segunda es una falla de comunicación.

Ejemplo propio: si 10 de 100 tiendas no responden, un panel de ventas puede mostrar «90 tiendas informaron». El total parcial es correcto como total recibido y es incorrecto si se presenta como total final. El diseño conserva valor al usuario definiendo exactamente qué significa la respuesta degradada.

> [!question]- ¿Un yield de 99 % implica que el 99 % de los datos se devolvió?
> No. Yield cuenta solicitudes; harvest cuenta completitud dentro de una respuesta. Una solicitud exitosa podría tener información parcial si el contrato lo permite.

**Referencia:** PDF 22–23 · impresas 218–219. [[Obsidian/lecturas/database internals/Materiales/09 a 11 Detección de fallas liderazgo y replicación.pdf#page=22|PDF de consulta]].

---

← [[Obsidian/lecturas/database internals/11 Replicación y consistencia/02 CAP PACELC y sus límites|Anterior]] · [[Obsidian/lecturas/database internals/11 Replicación y consistencia/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/11 Replicación y consistencia/04 Registros e intervalos concurrentes|Siguiente]] →
