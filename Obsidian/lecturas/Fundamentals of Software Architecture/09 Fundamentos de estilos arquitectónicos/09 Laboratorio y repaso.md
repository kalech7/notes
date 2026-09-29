---
title: "Laboratorio y repaso"
created: 2026-09-28
capitulo: 9
tags:
  - lecturas/software-architecture
  - arquitectura/estilos
---

[[Obsidian/lecturas/Fundamentals of Software Architecture/09 Fundamentos de estilos arquitectónicos/00 Índice|← Índice del capítulo 9]]

# Laboratorio y repaso de fundamentos

Este laboratorio es una **elaboración propia** para conectar los conceptos del capítulo 9. PedidoClaro es un caso didáctico distinto de la kata Silicon Sandwiches. Todas sus cifras y decisiones de escenario son supuestos, no mediciones del libro.

## 1. El problema completo

PedidoClaro gestiona compra, promociones, existencias y entrega. Un equipo pequeño mantiene un único despliegue con base de datos compartida. El volumen de consultas de catálogo es muy superior al de pedidos. Las modificaciones de promociones locales son frecuentes. El negocio quiere que un pedido confirmado no se duplique y que el 95 % de respuestas de creación llegue antes de 600 ms bajo una carga acordada.

Un integrante propone convertir cada responsabilidad en un servicio. Otro propone conservar el sistema actual. Antes de elegir, hay que separar cuatro decisiones: partición lógica, despliegue, datos y organización del equipo.

## 2. Paso 1: dibujar una partición razonada

**Respuesta explicada.** Agrupar inicialmente por dominios Compra, Promociones, Inventario y Entrega tiene sentido si los cambios frecuentes se expresan en esas capacidades. Cada módulo puede conservar capas internas. Las promociones locales no obligan a mover toda lógica local a una caja global `Local`; primero se comprueba si comparte reglas con otros dominios.

El despliegue puede seguir siendo uno. Se gana una frontera conceptual sin introducir todavía comunicación remota interna. El costo es que los módulos comparten entrega y parte del alcance de fallo; se necesitan reglas para evitar accesos indiscriminados a datos ajenos.

**Qué haría revisar la respuesta:** evidencia de un problema operacional que no se resuelve razonablemente dentro del despliegue actual, cambios muy distintos en frecuencia o requisitos de aislamiento y capacidad operativa para una separación.

## 3. Paso 2: evaluar la propuesta distribuida

La propuesta genera seis llamadas remotas secuenciales por pedido, de 80 ms cada una en promedio, además de 70 ms de trabajo no incluido en esas llamadas.

$$
T_{medio\ estimado}=6\times80+70=550\text{ ms}
$$

**¿Cumple el objetivo?** No se puede afirmar. El objetivo es p95 ≤ 600 ms; el cálculo es una estimación de media. Además hay que medir fallos, timeouts, carga y entorno. Un promedio cercano al umbral no sustituye una distribución del recorrido completo.

**Siguiente investigación:** capturar tiempos por tramo, medir p95 total, identificar llamadas necesarias y evaluar si la separación ofrece un beneficio que justifique la coordinación. La respuesta no es reducir todos los servicios a una cifra arbitraria: es comprobar la ruta crítica.

## 4. Paso 3: revisar un contrato demasiado amplio

Cada pedido consulta un perfil de 300 kB para usar 150 B. Hay 400 consultas por segundo.

| Variante | Cuenta decimal | Resultado |
|---|---|---|
| Perfil completo | 300.000 B × 400/s | 120.000.000 B/s = 120 MB/s = 960 Mbit/s |
| Datos necesarios | 150 B × 400/s | 60.000 B/s = 60 kB/s = 480 kbit/s |

La carga útil disminuye 2.000 veces. La siguiente pregunta es si un contrato estrecho puede mantenerse y autorizarse claramente. No se debe prometer el mismo factor de mejora en latencia: el cálculo solo describe transferencia.

## 5. Paso 4: diseñar el resultado incierto

El servicio de pago registra un cobro, pero Compra no recibe la respuesta. Un desarrollador quiere generar un nuevo identificador y repetir.

**Respuesta explicada.** Generar una nueva intención podría provocar un segundo efecto. Se debe conservar la identidad de la operación original y usar un mecanismo que permita conocer su resultado o repetirla con garantías adecuadas. El flujo necesita distinguir aceptado, rechazado y pendiente/desconocido.

Un timeout limita espera; no demuestra rechazo. Un circuit breaker protege frente a fallos repetidos; no resuelve qué pasó con ese cobro. Una consulta de estado o un reintento con identidad estable necesita soporte coherente del receptor.

## 6. Paso 5: poner a prueba la compensación

Después del pago, la confirmación de entrega falla. El diseño decide cancelar el cobro mediante una operación compensatoria. Esa operación también falla.

**Respuesta explicada.** No se puede declarar que el sistema volvió al estado previo. Debe persistirse qué efecto ocurrió, qué compensación se intentó y cuál es el estado pendiente. Hace falta recuperación con límites y responsables. Dependiendo del negocio, una devolución puede ser diferente de anular un cargo; las reglas financieras no se inventan en el diseño técnico.

El equipo debe mostrar tanto el recorrido exitoso como el fallo original y el fallo de recuperación. Un diagrama que termina siempre en «revertido» oculta el problema principal.

## 7. Paso 6: explicar un incidente sin cambio de código

El lunes aumentan los timeouts. No hay nueva versión. Se descubre una ruta de red diferente después de mantenimiento.

**Respuesta explicada.** La falacia de topología fija explica por qué «mismo código» no implica «mismo entorno». Hay que correlacionar cambios de infraestructura con medidas y coordinar responsables de red, plataforma y aplicación. Aumentar el timeout podría ser parte de una decisión posterior, pero no sustituye el diagnóstico.

## 8. Paso 7: asignar responsabilidades humanas

Un equipo alineado con Compra conserva el flujo de negocio. Una plataforma ofrece despliegue y observabilidad. Si falta capacidad de investigar trazas, apoyo habilitador ayuda a adquirirla. Un subsistema de optimización de rutas puede requerir especialización separada si su complejidad lo justifica.

Se evalúa si estas relaciones reducen esperas y carga cognitiva. Dibujar cuatro nombres sin cambiar acceso, decisiones o contratos no modifica la colaboración real.

## 9. Las once falacias, con la pregunta que las detecta

| N.º | Supuesto falso | Pregunta de revisión |
|---|---|---|
| 1 | La red es fiable | ¿Qué sabemos si la respuesta no llega? |
| 2 | La latencia es cero | ¿Cuánto tarda el recorrido completo, incluida su cola lenta? |
| 3 | El ancho de banda es infinito | ¿Qué volumen transmitimos por segundo y cuánto se usa? |
| 4 | La red es segura | ¿Quién puede invocar cada operación y sobre qué recurso? |
| 5 | La topología no cambia | ¿Qué cambios externos invalidan nuestros supuestos? |
| 6 | Hay un administrador | ¿Quién responde por cada dependencia operacional? |
| 7 | El transporte no cuesta | ¿Cuál es el costo incremental de infraestructura y operación? |
| 8 | La red es homogénea | ¿Qué diferencias de infraestructura y configuración importan? |
| 9 | Versionar es fácil | ¿Cuántos contratos mantenemos, quién los usa y cuándo se retiran? |
| 10 | Compensar siempre funciona | ¿Qué ocurre si también falla la recuperación? |
| 11 | Observar es opcional | ¿Podemos reconstruir el estado y recorrido de una operación? |

Las ocho primeras son la lista clásica presentada en el capítulo; las tres últimas son su ampliación por los autores. Las preguntas son reformulaciones didácticas propias.

## 10. Prueba de comprensión

> [!question]- ¿Cómo puede ser modular un monolito?
> Puede agrupar responsabilidades por dominio, encapsular detalles y controlar dependencias dentro de una sola unidad de despliegue. Modularidad lógica y distribución física son dimensiones distintas.

> [!question]- ¿Por qué un módulo por dominio puede tener capas?
> Porque el primer nivel define el criterio principal y los niveles internos pueden usar otro. Un módulo Compra puede separar entrada, reglas y persistencia sin convertir todo el sistema en partición técnica superior.

> [!question]- ¿Qué dato falta si solo se conoce el p95 de cada servicio?
> Falta la distribución del recorrido completo y las relaciones entre tiempos. No es válido obtener siempre su p95 sumando percentiles individuales.

> [!question]- ¿Cuál es la diferencia entre ancho de banda y costo de transporte?
> El primero expresa capacidad o tasa de datos. La séptima falacia trata del costo económico de infraestructura y operación; no es otro nombre para latencia.

> [!question]- ¿Por qué la organización del equipo forma parte del análisis?
> Porque las fronteras técnicas requieren colaboración para cambiar y operar. Una supuesta unidad autónoma que necesita negociar cada modificación con numerosos equipos no dispone de autonomía efectiva.

## Referencias de este laboratorio

- PDF pp. 8–13, impresas 137–142: partición y kata.
- PDF pp. 14–21, impresas 143–150: clasificación y once falacias.
- PDF p. 22, impresa 151: tipos de equipos.
- PDF p. 23, impresa 152: comparar estilos según sus características y compensaciones, sin buscar un ganador universal.

## Fuente principal

- [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/06 Fundamentos de estilos arquitectónicos.pdf#page=8|Fundamentals of Software Architecture, 2.ª ed., capítulo 9, PDF pp. 8–23; impresas 137–152]].

Las explicaciones, diagramas y ejemplos identificados como propios son elaboraciones didácticas; las páginas indicadas permiten contrastar los conceptos con el escaneo.

---

[[Obsidian/lecturas/Fundamentals of Software Architecture/09 Fundamentos de estilos arquitectónicos/08 Conway y topologías de equipos|← Anterior]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/10 Arquitectura por capas/00 Índice|Capítulo 10 →]]
