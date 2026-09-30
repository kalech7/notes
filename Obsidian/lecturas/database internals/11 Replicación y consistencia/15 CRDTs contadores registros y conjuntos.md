---
title: "Database Internals — Capítulo 11 · CRDTs contadores registros y conjuntos"
created: 2026-09-30
libro: "Database Internals"
capitulo: 11
tags:
  - lecturas/database-internals
  - arquitectura/sistemas-distribuidos
---

# CRDTs contadores registros y conjuntos

[[Obsidian/lecturas/database internals/11 Replicación y consistencia/00 Índice|Índice del capítulo]]

La **consistencia eventual fuerte**, SEC, añade una propiedad clave: réplicas que han incorporado el mismo conjunto de actualizaciones deben alcanzar el mismo estado equivalente, aunque las reciban en distinto orden permitido por el tipo. **CRDT** significa *Conflict-Free Replicated Data Type*: un tipo replicado cuyo diseño define cómo actualizar y fusionar para lograr esa convergencia.

Esto no lo convierte en un registro linealizable. Durante una partición cada réplica puede tener un conjunto diferente de actualizaciones y devolver valores distintos. La fuerza está en la convergencia determinista cuando comparten las actualizaciones, no en visibilidad inmediata ni en transacciones generales.

## Dos formas de replicar

| Familia | Qué se intercambia | Condiciones básicas |
|---|---|---|
| Por operaciones, CmRDT | Operaciones como «incrementa» | Entrega con las condiciones requeridas, control de duplicados, conmutatividad de concurrentes |
| Por estado, CvRDT | Estados del tipo | Actualizaciones inflacionarias y fusión asociativa, conmutativa e idempotente |

**Conmutativa** significa que intercambiar operandos no cambia el resultado. **Asociativa**, que agrupar fusiones de otra manera no lo cambia. **Idempotente**, que fusionar el mismo estado de nuevo no lo duplica. En una réplica por estado, estas propiedades permiten tolerar repetición y orden distinto de mensajes.

> [!warning] Precisión de la impresa 238
> La fuente describe las operaciones CmRDT como «side-effect free» y dice que aplicarlas no cambia el estado. Una operación de actualización sí cambia el estado replicado. La distinción útil es preparar la operación sin mutar y aplicarla con un efecto definido, además de controlar efectos externos. También hace falta tratar entrega y duplicados: sumar dos veces un mismo mensaje no es seguro sólo porque la suma sea conmutativa. El G-counter de la siguiente página se presenta aquí como **CRDT por estado**, porque intercambia vectores y los fusiona.

## G-counter: incrementar sin perder cambios

Un **G-counter** sólo crece. Con tres participantes, el estado empieza en `[0,0,0]`. Cada nodo aumenta únicamente su propia casilla. A incrementa y obtiene `[1,0,0]`; C incrementa y obtiene `[0,0,1]`. La fusión toma el máximo por componente.

![[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 11/08 G-counter.png]]

Las cajas azul y naranja representan estados locales tras incrementos independientes. Las dos flechas llevan los estados a una fusión por máximos que produce `[1,0,1]`. La caja verde calcula el valor visible mediante suma: 2. Es la reconstrucción del ejemplo numérico de la impresa 239, no un conteo observado en un sistema real.

La secuencia de la fuente se puede verificar:

```text
A fusiona C: max([1,0,0], [0,0,1]) = [1,0,1]
B fusiona A inicial: max([0,0,0], [1,0,0]) = [1,0,0]
B fusiona C: max([1,0,0], [0,0,1]) = [1,0,1]
C fusiona A inicial: max([0,0,1], [1,0,0]) = [1,0,1]
valor = sum([1,0,1]) = 2
```

Si llega otra vez `[1,0,0]`, los máximos siguen en `[1,0,1]`: el incremento no se cuenta dos veces. Sumar los dos valores locales y después sumar retransmisiones perdería esa protección. La propiedad depende de que cada participante sólo actualice su componente y no reutilice una identidad con un contador reiniciado que contradiga el estado anterior.

## PN-counter

Un **PN-counter** permite incrementos y decrementos con dos G-counters: P registra cantidades positivas y N registra cantidades negativas. Ambos se fusionan por máximos. El valor es `sum(P)−sum(N)`.

Ejemplo propio: P=`[4,2,0]` y N=`[1,0,2]` producen `6−3=3`. «Decrementar» no reduce una casilla existente: incrementa la casilla correspondiente de N. Esto conserva crecimiento monótono del estado interno aunque el número expuesto baje. El libro menciona superpares para organizar distribución y reducir intercambio directo; esa organización no reemplaza las reglas de fusión.

Un PN-counter no garantiza que un saldo permanezca no negativo cuando todos descuentan sin coordinación. El tipo converge aritméticamente; imponer cupos o invariantes globales puede necesitar otro diseño.

## Registros LWW y multivalor

Un **registro LWW** conserva el valor con mayor etiqueta en un orden total determinista. La etiqueta debe desempatar de forma inequívoca, por ejemplo `(contador, identidad)`. Fusionar por máximo converge, pero descarta los otros valores. Si la etiqueta contiene tiempo físico, desajustes pueden escoger un ganador distinto al último cambio real.

Un **registro multivalor** conserva versiones concurrentes que no se dominan causalmente, para que una actualización posterior o la aplicación las reconcilie. No conserva necesariamente todos los valores escritos para siempre: las versiones sustituidas causalmente pueden dejar de ser activas. Es una precisión de la simplificación de la impresa 239.

## G-set, 2P-set y JSON

Un **G-set** sólo permite añadir elementos. Fusiona mediante unión: `{a,b} ∪ {b,c} = {a,b,c}`. Añadir repetidamente b no crea duplicados.

El esquema con conjunto de altas A y de bajas R es un **2P-set**: el estado visible es `A−R` y ambos se fusionan por unión. Sólo se puede marcar para baja un elemento antes añadido. La baja queda como un **tombstone**, una marca persistente de eliminación. Una vez que un elemento está en R, añadirlo otra vez a A no lo devuelve al conjunto visible. La fuente menciona altas y bajas, pero no desarrolla esta limitación de reinserción.

Ejemplo propio: A=`{a,b}`, R=`{a}` expone `{b}`. Después otra réplica añade a y se fusiona; R aún contiene a, así que sigue sin verse. Para permitir quitar y volver a añadir hacen falta identidades de ocurrencias o un diseño distinto con reglas explícitas para concurrencia.

El capítulo también menciona un CRDT JSON con listas y mapas anidados para inserciones, borrados y asignaciones. Un JSON arbitrario no se vuelve un CRDT al unir sus textos: el diseño necesita identificadores, contexto y reglas para operaciones incompatibles. El algoritmo particular citado admite entrega sin un orden específico, pero eso no se generaliza a todos los CRDTs por operaciones.

> [!question]- ¿SEC evita perder cualquier cambio de negocio?
> No. Un LWW converge mientras descarta perdedores deliberadamente. La preservación de incrementos del G-counter depende de su tipo y sus condiciones. Convergencia y semántica de negocio deben evaluarse por separado.

**Referencia:** PDF 42–44 · impresas 238–240. [[Obsidian/lecturas/database internals/Materiales/09 a 11 Detección de fallas liderazgo y replicación.pdf#page=42|PDF de consulta]].

---

← [[Obsidian/lecturas/database internals/11 Replicación y consistencia/14 Réplicas testigo y reparación|Anterior]] · [[Obsidian/lecturas/database internals/11 Replicación y consistencia/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/11 Replicación y consistencia/16 Laboratorio y repaso resuelto|Siguiente]] →
