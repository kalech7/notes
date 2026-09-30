---
title: "Database Internals — Gossip y tablas de latidos"
created: 2026-09-30
libro: "Database Internals"
capitulo: 9
tags:
  - lecturas/database-internals
  - arquitectura/deteccion-de-fallas
---

# Gossip y tablas de latidos

[[Obsidian/lecturas/database internals/09 Detección de fallas/00 Índice|Índice del capítulo 9]]

## Compartir lo que se sabe de otros

**Gossip** es una difusión mediante intercambios sucesivos entre participantes. En vez de exigir que A consulte directamente a todos, A intercambia información con algunos vecinos y estos hacen lo mismo. Una noticia de C puede llegar a A a través de B. La propagación acumulada aporta perspectivas adicionales y puede sortear un enlace directo averiado.

El detector descrito mantiene una tabla de miembros con **contador de heartbeat** e información temporal sobre su avance. Cada participante incrementa periódicamente su contador y transmite su tabla a un vecino elegido aleatoriamente. El receptor combina las novedades con su tabla local. Después examina qué contadores llevan demasiado tiempo sin avanzar.

## Un contador debe representar novedad

**Ejemplo propio.** A conoce `C = 41`. B le transmite una tabla con `C = 42`, que representa evidencia nueva. A guarda 42 y registra en su reloj local cuándo lo aprendió. Si B vuelve a enviar 42, A no debe tratar esa copia como avance de C: puede ser la repetición de una noticia antigua mientras C ya está caído.

![[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 09/04-gossip-frescura.png]]

La caja verde de C contiene un contador que avanza a 42. B conoce esa novedad y la flecha azul permite que llegue a A. Las cajas inferiores comparan incorporar 42 por primera vez con recibirlo otra vez. La actualización temporal debe corresponder a avance nuevo, no a cualquier recepción. Así el tráfico de los demás miembros no rejuvenece indefinidamente a C.

Una regla pedagógica de mezcla, para una misma ejecución del emisor, es conservar el contador mayor. Un contador menor o igual no prueba progreso adicional. Registrar el **instante local de incorporación de evidencia nueva** permite evaluar recencia sin comparar directamente relojes de pared de máquinas distintas.

El capítulo no resuelve todos los detalles de una implementación productiva. Si C reinicia y empieza su contador otra vez desde cero, conservar siempre el máximo antiguo impediría reconocer su nueva ejecución. Hace falta distinguir la identidad de la ejecución —por ejemplo, una generación— o una regla equivalente. Este detalle es una ampliación propia para mostrar la condición bajo la cual funciona el ejemplo de máximos.

## Tres estados de la figura 9-4

En el primer panel los tres procesos se comunican y comparten evidencia. En el segundo falla la conexión directa entre P1 y P3, pero P2 conserva rutas hacia ambos y transmite la novedad de P3. P1 no necesita acusar inmediatamente a P3 por el fallo del enlace directo. En el tercero P3 cae y deja de generar nuevas señales. Cuando ya no aparece avance y vence el criterio local, los otros participantes pueden sospechar de él.

Estas tablas son **vistas locales que convergen mediante intercambio**, no una fotografía simultánea e infalible del sistema entero. Dos observadores pueden actualizar sus tablas en instantes distintos. El mecanismo mejora la oportunidad de reunir evidencia; no impide particiones ni garantiza que todos reciban una noticia en un plazo fijo bajo un modelo asíncrono.

## Qué significa que escale de forma lineal

El capítulo afirma que la comunicación puede crecer como máximo linealmente con el número de procesos. Esa afirmación necesita especificar qué se mide. Si cada uno de `n` miembros envía un mensaje a un vecino por ronda, hay del orden de `n` mensajes. Si **cada mensaje transporta una tabla completa de `n` entradas**, el volumen de entradas transmitidas por ronda es del orden de `n²`.

**Cálculo propio.** Con 100 miembros y una entrada de 24 bytes, una tabla ocupa aproximadamente `100 × 24 = 2 400 bytes`, sin cabeceras. Un envío por miembro implica `100 × 2 400 = 240 000 bytes` por ronda. Con 200 miembros, cada tabla ocupa 4 800 bytes y el total llega a 960 000 bytes. Duplicar los miembros cuadruplica ese volumen en el modelo de tabla completa, aunque solo duplique el número de mensajes.

Transmitir diferencias, limitar el contenido o elegir otro diseño puede cambiar el costo. No se deduce automáticamente del término gossip. También hay que contar la frecuencia, las cabeceras y la cantidad de vecinos por intercambio.

## Lo que gossip y phi resuelven de forma distinta

Gossip decide **cómo se difunde evidencia**. Phi decide **cómo interpretar el silencio con un historial temporal**. Son dimensiones distintas y pueden combinarse si la evidencia y la política de recencia están bien definidas. Recibir mediante gossip una tabla vieja no debe equivaler a recibir un nuevo heartbeat de su propietario.

Una falsa sospecha puede difundirse también. La mejora de cobertura de rutas no convierte un rumor en certeza. En sistemas reales suelen necesitarse reglas para novedades, identidad y corrección de sospechas; estas notas no atribuyen al esquema introductorio del libro un protocolo completo que no aparece en él.

> [!question]- ¿Qué sucede si A recibe continuamente tablas que incluyen un C caído?
> Si el contador de C no avanza, esas copias no deben renovar su instante de evidencia nueva. A seguirá acumulando silencio respecto del avance de C y podrá sospechar según su criterio, aunque A y B sigan intercambiando mensajes.

**Referencia:** PDF 6–7 · impresas 200–201 · figuras 9-4. [[Obsidian/lecturas/database internals/Materiales/09 a 11 Detección de fallas liderazgo y replicación.pdf#page=6|PDF de consulta]].

---

← [[Obsidian/lecturas/database internals/09 Detección de fallas/04 Phi-accrual adaptación y umbrales|Anterior]] · [[Obsidian/lecturas/database internals/09 Detección de fallas/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/09 Detección de fallas/06 FUSE y propagación del silencio|Siguiente]] →
