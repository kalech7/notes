---
title: "Database Internals — Capítulo 11 · Laboratorio y repaso resuelto"
created: 2026-09-30
libro: "Database Internals"
capitulo: 11
tags:
  - lecturas/database-internals
  - arquitectura/sistemas-distribuidos
---

# Laboratorio y repaso resuelto

[[Obsidian/lecturas/database internals/11 Replicación y consistencia/00 Índice|Índice del capítulo]]

Este laboratorio propio reproduce tres diferencias importantes sin depender de servidores ni paquetes externos: la intersección de quórums, una regresión causada por escritura incompleta y la convergencia de un G-counter. Es un modelo pequeño de estados, **no una implementación de base distribuida** ni una prueba de un producto.

El archivo runnable está en [[Obsidian/lecturas/database internals/Materiales/Laboratorios/11 consistencia_modelo.py|11 consistencia_modelo.py]]. Desde la raíz del vault:

```bash
python3 "Obsidian/lecturas/database internals/Materiales/Laboratorios/11 consistencia_modelo.py"
```

## 1. Enumerar quórums

Se forman todas las parejas de `{A,B,C}`. Se verifica que cada grupo de lectura de tamaño dos se cruza con cada grupo de escritura de tamaño dos. La salida indica **9 cruces**: tres opciones de escritura por tres de lectura.

El hecho comprobado es una propiedad de conjuntos. No incluye por sí solo selección de versiones, tiempos reales ni reparación. Probar que la intersección no está vacía no prueba linealizabilidad.

## 2. Leer una escritura incompleta

Se asignan versiones `A=1,B=0,C=0`. La escritura no obtuvo W=2. La lectura {A,B} selecciona la versión 1 y la siguiente {B,C} la versión 0. Ambas respetan R=2 y aparece la salida **regresión: 1 → 0**.

El modelo después propaga 1 a B antes de permitir la segunda lectura. {B,C} devuelve 1 y la salida indica **con reparación previa: 1 → 1**. Es una ilustración del efecto de reparar de forma bloqueante; no desarrolla todos los casos concurrentes o fallas de un protocolo real.

## 3. Fusionar un contador

A tiene `[1,0,0]`, B `[0,0,0]` y C `[0,0,1]`. Se fusionan todos en cada orden y con duplicados. El resultado debe ser `[1,0,1]`, suma 2. El script verifica conmutatividad, asociatividad e idempotencia sobre estos estados y comprueba que repetir mensajes no añade incrementos.

La verificación es significativa para este ejemplo y las reglas implementadas. La explicación general se deriva de que el máximo por componente tiene esas tres propiedades y cada componente sólo aumenta. No es una prueba automática de todos los CRDTs.

## Repaso resuelto

> [!question]- 1. A confirma x=1 y después otro cliente lee x=0 en B. ¿Qué modelo fuerte se viola?
> Se viola linealizabilidad si la escritura precede a la lectura, x no fue reemplazado por otra escritura y las respuestas pertenecen al mismo registro. La consistencia secuencial puede permitir un orden que coloque esa lectura antes de la escritura de otro cliente, si toda la historia lo admite.

> [!question]- 2. ¿Por qué no alcanza conservar copias para tolerar cualquier falla?
> Necesitamos conocer su estado, controlar autoridad, conservar suficientes versiones y reparar. Copias en el mismo dominio de falla pueden perderse juntas. Replicación añade redundancia; el protocolo y la colocación determinan qué falla cubre.

> [!question]- 3. Con N=5,W=3,R=2, ¿la lectura debe intersectar la escritura?
> No: R+W=5. Por ejemplo, escritura {A,B,C} y lectura {D,E} son disjuntas. Subir R a 3 obliga a por lo menos una intersección; aún hacen falta condiciones de versiones y protocolo.

> [!question]- 4. Con siete réplicas y mayoría, ¿cuántas hacen falta y cuántas pueden faltar?
> La mayoría es floor(7/2)+1=4. Pueden faltar tres y quedar cuatro. Es el caso N=2f+1 con f=3. Se presupone que las cuatro pueden comunicarse y satisfacer los demás requisitos.

> [!question]- 5. ¿Una lectura posterior con un saldo menor viola lecturas monótonas?
> No necesariamente. Una nueva compra puede producir un saldo menor en una versión más reciente. Monotonicidad significa no retroceder en la historia observada.

> [!question]- 6. Compara [2,1,0] y [1,2,0].
> Son incomparables: el primero tiene una componente mayor y otra menor. Indican concurrencia en el esquema vectorial; no hay que sumarlos ni elegir el mayor lexicográfico para inferir causalidad.

> [!question]- 7. Una respuesta llega antes que la publicación que motivó esa respuesta. ¿Qué hace una réplica causal?
> Retiene el dependiente hasta cumplir su contexto. La llegada al servidor no obliga a exposición inmediata. Si ignora o pierde el contexto causal, la garantía deja de cumplirse.

> [!question]- 8. ¿Por qué es peligroso borrar el objeto de finalización antes de expirar la lease?
> Puede llegar un reintento todavía válido y tratarse como operación nueva. La deduplicación necesita permanecer mientras el protocolo permita esa identidad y ese número de operación.

> [!question]- 9. El único nodo que conserva el valor nuevo está inaccesible, pero dos testigos tienen su versión. ¿Se puede responder el contenido?
> Los metadatos no reconstruyen un contenido arbitrario. Hace falta una copia accesible o que un testigo conserve el dato temporal según el protocolo. Un voto no sustituye el payload.

> [!question]- 10. Fusiona [3,0,1] y [2,4,0] en un G-counter.
> Los máximos por casilla producen [3,4,1]. El valor es 3+4+1=8. Repetir cualquiera de los dos estados deja [3,4,1].

> [!question]- 11. En un 2P-set, A={a,b,c}, R={b}; otra réplica vuelve a añadir b. ¿Cuál es el conjunto visible?
> {a,c}. La marca b sigue en R y la unión de altas no la elimina. El 2P-set no permite reinsertar el mismo elemento tras su eliminación.

> [!question]- 12. ¿Dos cuentas con lecturas y escrituras linealizables hacen atómica una transferencia entre ellas?
> No. Una secuencia que descuenta una cuenta y suma otra necesita un contrato de transacción. Linealizabilidad por objeto compone operaciones individuales, no agrupa llamadas en una transacción nueva.

## Tabla para elegir el contrato de una operación

| Necesidad propia de ejemplo | Propiedad a comprobar | Duda que queda |
|---|---|---|
| Recargar mi perfil recién guardado | Leer propias escrituras | ¿Qué ocurre al perder la sesión? |
| No volver de «enviado» a una versión antigua | Lecturas monótonas | ¿Cómo se conserva el contexto al cambiar de réplica? |
| No ver respuesta sin publicación | Causalidad | ¿Cómo se manejan las ramas concurrentes? |
| Mantener un contador durante partición | CRDT adecuado | ¿Hay un invariante adicional de cupos? |
| Reclamar una autoridad exclusiva | Operación y orden linealizables adecuados | ¿Cómo se rechaza una autoridad vencida? |
| Transferir entre cuentas | Transacciones con aislamiento y atomicidad adecuados | ¿Debe respetarse también precedencia real? |

El resumen del libro advierte que añadir una capa con garantías débiles sobre un sistema fuerte puede romper la experiencia: por ejemplo, una caché que responde un valor viejo puede hacer no linealizable el camino observable aunque el almacenamiento lo sea. Los contratos se evalúan a través de toda la ruta de la operación.

**Referencia:** PDF 44–45 · impresas 240–241. [[Obsidian/lecturas/database internals/Materiales/09 a 11 Detección de fallas liderazgo y replicación.pdf#page=44|PDF de consulta]].

---

← [[Obsidian/lecturas/database internals/11 Replicación y consistencia/15 CRDTs contadores registros y conjuntos|Anterior]] · [[Obsidian/lecturas/database internals/11 Replicación y consistencia/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/11 Replicación y consistencia/00 Índice|Volver al índice]] →
