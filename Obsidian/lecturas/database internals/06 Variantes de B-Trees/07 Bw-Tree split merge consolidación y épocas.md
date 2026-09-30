---
title: "Database Internals — Bw-Tree: split, merge, consolidación y épocas"
created: 2026-09-30
libro: "Database Internals"
capitulo: 6
tags:
  - lecturas/database-internals
  - arquitectura/b-trees
  - arquitectura/bw-tree
  - arquitectura/memoria
---

# Bw-Tree: split, merge, consolidación y épocas

[[Obsidian/lecturas/database internals/00 Empieza aquí|Inicio del libro]] → [[Obsidian/lecturas/database internals/06 Variantes de B-Trees/00 Índice|Capítulo 6]]

Una cadena de deltas no elimina el balance del árbol. Un nodo lógico puede crecer demasiado, quedar casi vacío o acumular demasiadas piezas para leerse eficientemente. El Bw-Tree distingue **modificar la estructura**, **consolidar su representación** y **reclamar piezas antiguas**. Son tareas relacionadas, pero no equivalentes.

Una **SMO**, *structural modification operation*, cambia relaciones entre nodos: por ejemplo, un split o un merge. La corrección debe mantenerse entre sus etapas, porque otro hilo puede encontrar el árbol a medio reorganizar.

## Split: publicar primero un camino de redirección

Supongamos un nodo N que se divide por el separador 50:

1. Consolidar su contenido lógico y preparar el nuevo hermano derecho R con las claves `>=50`.
2. Publicar en N un **split delta** que registra el separador y el enlace lógico a R. Las claves derechas dejan de pertenecer al rango vigente de N.
3. Añadir R y su separador al padre, para que futuras búsquedas lleguen directamente.

Entre 2 y 3 el padre todavía puede mandar una búsqueda de 70 a N. El split delta de N la redirige a R. El dato ya es alcanzable aunque aún no esté publicado el camino corto en el padre.

![[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 06/09-bw-split-merge.png]]

La fila superior muestra el split: preparar R, anunciar la redirección y terminar el padre. La inferior muestra el merge: marcar la derecha, incorporarla lógicamente en la izquierda y retirar el enlace redundante del padre. Las cajas finales de cada fila optimizan el recorrido sin dejar un intervalo en el que desaparezca el acceso a las claves.

La actualización del padre es importante para el costo de navegación. El capítulo resalta que el enlace de redirección conserva accesibilidad aun antes de esa actualización. No implica que sea conveniente acumular operaciones estructurales incompletas indefinidamente.

## Merge: unir contenidos antes de quitar la ruta redundante

Para fusionar derecha R con izquierda L, el texto describe:

1. Un **remove delta** en R marca el comienzo de su retirada estructural.
2. Un **merge delta** en L enlaza el contenido de R y lo hace parte lógica de L.
3. El padre elimina su enlace directo a R.

Durante una SMO, otros hilos pueden colaborar para completarla. El **helping**, o ayuda, evita que todo dependa de que el hilo que empezó vuelva inmediatamente a ejecutar. El capítulo también introduce **abort deltas** en el padre para evitar SMO concurrentes que entren en conflicto; actúan como marcas de coordinación de acceso a esa operación. Que su efecto se parezca a un lock no cambia la necesidad de razonar sobre el progreso y la ayuda del algoritmo completo.

Cuando se divide la raíz, aparece una raíz nueva con el nodo anterior y el hermano nuevo como hijos. La altura crece por la misma necesidad lógica que en un B-Tree convencional, aunque la representación y la publicación sean distintas.

**Referencia:** PDF 12–13 · impresas 122–123. [[Obsidian/lecturas/database internals/Materiales/06 Variantes de B-Trees.pdf#page=12|Fuente del capítulo]].

## Consolidar una cadena larga

Supongamos 40 deltas encima de una base. Reconstruir el nodo puede costar más que con dos deltas. La **consolidación** aplica los cambios pertinentes y crea una base nueva que representa el mismo estado lógico con menos piezas.

En el ejemplo de la nota anterior:

```text
PUT(C,7) → DELETE(B) → PUT(A,12) → base(A=10,B=20)
                     ↓ consolidación
                  nueva base(A=12,C=7)
```

La tabla de mapeo se actualiza para apuntar a esa nueva base mediante el protocolo correspondiente. Si se publican deltas mientras alguien prepara la consolidación, la instalación debe detectar el cambio y evitar perderlos. “Copiar y luego guardar el puntero” sin comprobación sería insuficiente.

Consolidar cambia la representación de un nodo; no cambia necesariamente cuántos hijos tiene ni su rango. Por eso **consolidación no es merge estructural**. Tampoco es exactamente la fusión de runs de un FD-Tree: allí se combinan niveles, mientras aquí se compacta la representación de un nodo lógico.

## Por qué no se puede liberar la cadena vieja al cambiar el puntero

Un lector pudo obtener la cabeza vieja antes de la consolidación y seguir recorriéndola. Aunque la tabla ya señale la nueva base, ese lector aún tiene referencias a la representación anterior. Liberarla inmediatamente permitiría leer memoria reutilizada para otro propósito.

![[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 06/10-reclamacion-epocas.png]]

El lector naranja alcanzó la cadena en la época 7 y sigue activo después de su retirada. La publicación verde dirige a los lectores posteriores hacia la nueva base; la violeta representa a uno de ellos. La representación vieja deja de ser accesible desde la tabla, pero su vida física debe prolongarse hasta que quienes podían usarla terminen.

La **reclamación por épocas**, *epoch-based reclamation*, agrupa participantes por períodos lógicos. Una pieza retirada se conserva mientras haya participantes de aquella época o de épocas anteriores que puedan haberla alcanzado. Después de su salida segura, puede reclamarse.

El número de época es un marcador del protocolo, no una fecha de reloj. El lector debe anunciar o registrar su participación de una manera que haga segura la relación entre “entré” y “obtuve el puntero”. Es incorrecto interpretar “sin latches” como “sin ningún seguimiento de lectores”.

Un lector que tarda mucho puede retrasar la reclamación y retener memoria. Esa consecuencia se parece a la retención de páginas por snapshots en CoW, aunque el mecanismo y la unidad retenida sean distintos.

> [!question]- ¿Cuándo cambia el valor visible durante una consolidación?
> No debería cambiar por la consolidación misma: la base nueva representa el mismo estado lógico. Lo que cambia es cuántas piezas se necesitan para reconstruirlo.

> [!question]- ¿“No está en la tabla” prueba que una pieza ya no tiene usuarios?
> No. Un lector anterior pudo guardar su dirección antes de que se retirara. La tabla determina nuevos accesos; la reclamación determina cuándo dejaron de existir accesos anteriores.

**Referencia:** PDF 13–14 · impresas 123–124. [[Obsidian/lecturas/database internals/Materiales/06 Variantes de B-Trees.pdf#page=13|Fuente del capítulo]].

---

← [[Obsidian/lecturas/database internals/06 Variantes de B-Trees/06 Bw-Tree cadenas de deltas y CAS|Anterior]] · [[Obsidian/lecturas/database internals/06 Variantes de B-Trees/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/06 Variantes de B-Trees/08 Cache-oblivious layout vEB y packed arrays|Siguiente]] →
