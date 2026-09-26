---
title: "Capítulo 4 · Características arquitectónicas · Preguntas y ejercicio resuelto"
created: 2026-09-25
tags:
  - lecturas/software-architecture
capitulo: 4
orden: 7
---

# Preguntas y ejercicio resuelto

[Inicio del libro](../00%20Empieza%20aqu%C3%AD.md) → [Capítulo 4 · Características arquitectónicas](00%20%C3%8Dndice.md) → Nota 7 de 7

**Objetivo:** Justificar una decisión ante demanda y fallos.

> [!info] Contexto del capítulo
> Segunda edición. PedidoClaro y sus cifras son ejemplos didácticos propios; Silicon Sandwiches es la kata del libro. El [índice del capítulo](00%20%C3%8Dndice.md) conserva el alcance y las referencias generales.

## 7. Preguntas de comprobación

### 1. ¿Toda exigencia importante es una característica arquitectónica?

> [!success]- Solución
> No. Debe reunir los tres criterios del libro. Calcular correctamente un precio es importante, pero describe funcionalidad del dominio; un objetivo temporal que obliga a reorganizar el procesamiento puede constituir una característica arquitectónica.

### 2. ¿Un promedio de 195 ms garantiza p95 inferior a 300 ms?

> [!success]- Solución
> No: el promedio no determina la distribución. En el ejemplo concreto sí se calcula p95 = 100 ms por rango más próximo, pero ese resultado proviene de las observaciones, no del promedio.

### 3. ¿Cuatro instancias prueban elasticidad?

> [!success]- Solución
> No. Podrían permanecer siempre encendidas. Hay que observar el ajuste ante demanda cambiante, incluida la reducción y el tiempo necesario para disponer de capacidad útil.

### 4. ¿Una restauración en ocho minutos cumple RPO de dos minutos?

> [!success]- Solución
> No puede deducirse. Ocho minutos describe recuperación efectiva y se compara con RTO. Para RPO necesitamos la antigüedad del estado recuperado respecto del incidente.

### 5. ¿Autenticar al encargado permite que consulte cualquier sucursal?

> [!success]- Solución
> No. La identidad comprobada es entrada para decidir permisos. La autorización debe delimitar acciones y datos, y verificarse en el servidor.

### 6. ¿Por qué los autores excluyen adecuación funcional de su catálogo?

> [!success]- Solución
> Porque la consideran parte de las funciones y motivaciones del dominio. Discrepan de la clasificación presentada; no niegan la importancia de completitud, corrección y pertinencia funcional.

### 7. ¿Dos zonas y un proveedor de pagos garantizan una tienda segura y disponible?

> [!success]- Solución
> No. Hay que analizar dependencias comunes, persistencia, recuperación y permisos. Esas capacidades externas ayudan, pero la arquitectura debe utilizarlas de modo coherente con amenazas y fallos concretos.

## 8. Ejercicio aplicado: justificar una decisión

**Supuestos inventados:** PedidoClaro recibe 40 solicitudes/s normalmente y 140 durante quince minutos. Una instancia soporta 50 con p95 ≤ 300 ms; cuatro soportan 160. Arrancar capacidad adicional tarda tres minutos. Se exige RTO ≤ 10 min, RPO ≤ 2 min y disponibilidad temporal de 99,9 % sobre treinta días completos.

Propón una estructura inicial, identifica tres riesgos y explica cómo verificarías los objetivos. Calcula el margen de capacidad del pico y el presupuesto temporal de indisponibilidad. No presupongas que un estilo garantiza propiedades.

> [!success]- Solución orientativa
> Un monolito replicado, balanceador y persistencia con recuperación probada es una hipótesis inicial posible. Cuatro instancias dejan 160 − 140 = 20 solicitudes/s de margen: 12,5 % de la capacidad medida. No demuestra tolerancia al fallo de una instancia: falta medir la capacidad con tres.
>
> Tres riesgos son la demora de arranque, la dependencia compartida de datos y la pérdida o duplicación de pedidos durante recuperación. Un pico previsible permite preparar capacidad con antelación; uno inesperado requiere reserva u otra estrategia que se pruebe bajo carga.
>
> Verificaríamos latencias y errores con la mezcla realista de operaciones, retiraríamos una instancia durante la prueba y ensayaríamos restauración y reconciliación de pedidos. El presupuesto temporal es 43,2 minutos; cumplir RTO por incidente no garantiza cumplir disponibilidad mensual si los incidentes se repiten. La propuesta se acepta solo si la evidencia satisface los objetivos y su coste resulta justificable.

---

**Anterior:** [Lenguaje común y compromisos](06%20Lenguaje%20com%C3%BAn%20y%20compromisos.md) · **Índice:** [Volver al capítulo](00%20%C3%8Dndice.md) · **Siguiente:** [De necesidades a decisiones](../05%20Identificar%20y%20priorizar%20caracter%C3%ADsticas/01%20De%20necesidades%20a%20decisiones.md)
