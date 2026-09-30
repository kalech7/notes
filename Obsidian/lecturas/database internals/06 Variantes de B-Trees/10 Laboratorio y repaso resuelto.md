---
title: "Database Internals — Laboratorio y repaso resuelto"
created: 2026-09-30
libro: "Database Internals"
capitulo: 6
tags:
  - lecturas/database-internals
  - arquitectura/b-trees
  - arquitectura/laboratorio
  - arquitectura/repaso
---

# Laboratorio y repaso resuelto

[[Obsidian/lecturas/database internals/00 Empieza aquí|Inicio del libro]] → [[Obsidian/lecturas/database internals/06 Variantes de B-Trees/00 Índice|Capítulo 6]]

Este laboratorio usa ejemplos propios para comprobar las reglas del capítulo. El objetivo es predecir estados y costos, no medir el rendimiento de una base de datos real.

## Simulación ejecutable

El archivo [[Obsidian/lecturas/database internals/Materiales/Laboratorios/06 variantes_btree.py|06 variantes_btree.py]] usa únicamente la biblioteca estándar de Python. Puede ejecutarse desde la raíz del vault:

```bash
python3 "Obsidian/lecturas/database internals/Materiales/Laboratorios/06 variantes_btree.py"
```

Comprueba snapshots CoW con ramas compartidas, combinación base+buffer, un tombstone sobre versiones inferiores, una carrera CAS simulada, consolidación y el orden vEB del gráfico. La secuencia CAS está modelada sin hilos reales; el script no implementa un motor, reclamación concurrente ni persistencia durable.

| Experimento | Resultado esperado |
|---|---|
| Cambiar 70 bajo raíz CoW nueva | Raíz anterior: 10; nueva: 12; rama intacta compartida |
| Aplicar buffer de la nota 03 | `10:A, 20:B2, 40:D` |
| Borrar 70 con valor viejo en un run inferior | 70 ausente; quitar la marca antes de limpiar permite que reaparezca |
| Dos escritores parten de H | T1 publica; primer intento de T2 falla; el reintento conserva ambos cambios |
| Consolidar base y deltas | `A:12, C:7` antes y después |
| Ordenar cuatro niveles con vEB | `1,2,3,4,8,9,5,10,11,6,12,13,7,14,15` |

## 1. Calcular escritura de páginas

Una página tiene 8 KiB y recibe 32 cambios de 32 bytes cada uno. El modelo A reescribe la página después de cada cambio; el modelo B escribe una sola página al finalizar. Ignoramos logs, metadatos y caché.

> [!question]- ¿Cuántos bytes escribe cada modelo y cuál es su amplificación?
> `8 KiB = 8192 bytes`. Los cambios lógicos suman `32 × 32 = 1024 bytes`. A escribe `32 × 8192 = 262144 bytes`, por lo que amplifica `262144/1024 = 256`. B escribe `8192 bytes`, amplificación `8192/1024 = 8`. La reducción es `262144/8192 = 32 veces` para este componente y estas condiciones.

## 2. Contar copias en CoW

Un árbol tiene raíz, dos niveles internos y hojas. Modificamos una hoja sin dividirla, y cada nivel ocupa una página de 4 KiB en la ruta.

> [!question]- ¿Cuántas páginas nuevas hacen falta y qué permanece compartido?
> La ruta tiene cuatro páginas: hoja, dos internos y raíz. Se copian esas cuatro, `4 × 4096 = 16384 bytes`. Los subárboles ajenos a la ruta permanecen compartidos. No se puede liberar una página compartida solo porque dejó de ser parte del camino modificado.

## 3. Reconstruir una lectura con cambios pendientes

La base contiene `10:A,20:B,30:C`. Los cambios visibles son `PUT(20,B2),DELETE(30),PUT(40,D),PUT(20,B3)` en ese orden.

> [!question]- ¿Qué devuelve el rango de 10 a 40 inclusive?
> `10:A,20:B3,40:D`. El último cambio visible de 20 reemplaza a B2; el borrado suprime 30; 40 se intercala al final. El resultado debe coincidir antes y después de reconciliar esos cambios.

## 4. Distribuir un lote LA-Tree

El árbol separa rangos con 50. El buffer superior recibe `PUT(12,a),PUT(80,c),DELETE(70),PUT(18,b)`.

> [!question]- ¿Qué recibe cada subárbol y dónde debe consultar una lectura de 80 antes de aplicar el lote?
> El izquierdo recibe las operaciones de 12 y 18. El derecho recibe las de 80 y 70, respetando la semántica de orden que corresponda. Leer 80 exige consultar su cambio pendiente en los buffers pertinentes además de la hoja base; si solo se busca la hoja antigua, se pierde una inserción ya visible.

## 5. Prevenir la resurrección de un borrado

La cabeza contiene `DELETE(70)`, L1 no contiene 70 y L2 guarda `70:viejo`. Se vacía la cabeza hacia L1 y se decide quitar el tombstone para ahorrar espacio.

> [!question]- ¿Qué falla y cuándo puede retirarse esa marca?
> Una lectura posterior puede devolver el registro viejo de L2. El tombstone debe acompañar la propagación hasta eliminar u ocultar todas las versiones inferiores pertinentes. Retirarlo solo porque L1 no tenía la clave confunde un nivel con el conjunto de niveles.

## 6. Distinguir muestra y registro en fractional cascading

Se consulta el primer elemento `>=27` en las listas A1, A2 y A3 de la nota 05. C1 contiene un 30 auxiliar.

> [!question]- ¿Debemos devolver 30 como resultado de A1?
> No. A1 contiene `12,24,32,34,39`: su resultado es 32. El 30 de C1 sirve para navegar al nivel inferior. En A2 el resultado es 28 y en A3 es 30. Confundir catálogo auxiliar con registros originales modifica la respuesta de la consulta.

## 7. Detectar una escritura perdida sin CAS

T1 y T2 leen la cabeza H. T1 prepara `D1→H`; T2 prepara `D2→H`. T1 publica D1; después T2 guarda D2 con una asignación incondicional.

> [!question]- ¿Qué actualización queda fuera de la cadena y cómo se evita?
> D1 queda fuera de la cadena alcanzable desde la cabeza D2. T2 debe usar CAS esperando H; como la cabeza es D1, su intento falla. Relee, revisa la operación y prepara una publicación que mantenga D1, por ejemplo `D2'→D1→H` en este caso.

## 8. Resolver un split incompleto

El padre aún manda la clave 70 a N. N ya tiene un split delta con separador 50 y hermano R.

> [!question]- ¿Debe abortarse la lectura porque el padre todavía no conoce R?
> El protocolo permite redirigir desde N hacia R para claves del rango derecho. Así 70 sigue alcanzable durante el half-split lógico. Los hilos pueden ayudar a completar la actualización del padre para recuperar el camino directo.

## 9. Decidir cuándo reclamar una cadena

Un lector de época 7 tomó una cabeza vieja. El sistema la retira durante aquella época y publica una base nueva. En época 8 comienzan lectores que solo alcanzan la base nueva.

> [!question]- ¿Es suficiente que todos los lectores de época 8 terminen?
> No. El lector de época 7 todavía puede usar la cadena vieja. Hay que esperar la salida segura de los participantes de la época de retirada y anteriores que podían haberla obtenido. Los lectores posteriores no sustituyen esa condición.

## 10. Verificar localidad y densidad

Se usa el layout vEB de la nota 08. La ruta es `1→3→7→15`, los bloques contienen cuatro nodos y el primer nodo está alineado. Un packed array separado tiene capacidad ocho y contiene seis elementos.

> [!question]- ¿Cuántos bloques toca la ruta vEB y qué densidad tiene el array?
> Los nodos están en posiciones desde cero `0,2,12,14`, bloques `0,0,3,3`: dos bloques distintos. El array tiene densidad `6/8=75 %`. La densidad global no permite concluir que todos sus segmentos tengan huecos: una ventana local puede estar al 100 %.

## Términos para explicar sin memorizar

| Término | Explicación breve |
|---|---|
| CoW | Construir una versión nueva sin alterar páginas que usan lectores anteriores |
| Reconciliación | Construir una imagen física a partir de base y cambios aplicables |
| Run | Secuencia ordenada cuyo contenido publicado no se modifica en el sitio |
| Fence | Referencia que orienta una búsqueda entre niveles o páginas |
| Tombstone | Marca que impide devolver una versión anterior borrada |
| Delta | Pieza que describe un cambio separado de la base |
| ID lógico | Identidad estable que una tabla traduce a la ubicación actual |
| CAS | Publicar solo si el valor actual coincide con el esperado |
| SMO | Operación que modifica relaciones estructurales entre nodos |
| Consolidación | Reemplazar base y deltas por una representación más corta del mismo estado |
| Época | Período lógico que ayuda a saber cuándo nadie usa piezas retiradas |
| vEB layout | Orden físico que conserva contigüidad de subárboles a varias escalas |
| Packed array | Array ordenado con huecos distribuidos y reglas de densidad |

El repaso está resuelto para permitir comprobar el razonamiento. Las preguntas y el programa son elaboración propia a partir de los mecanismos del capítulo.

**Referencia:** PDF 1–18 · impresas 111–128. [[Obsidian/lecturas/database internals/Materiales/06 Variantes de B-Trees.pdf#page=1|Fuente del capítulo]].

---

← [[Obsidian/lecturas/database internals/06 Variantes de B-Trees/09 Comparar variantes y conectar los mecanismos|Anterior]] · [[Obsidian/lecturas/database internals/06 Variantes de B-Trees/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/00 Índice|Siguiente]] →
