---
title: "Laboratorio de componentes, quanta y gobierno"
created: 2026-09-28
tags:
  - lecturas/software-architecture
  - ejercicios
capitulos:
  - 6
  - 7
  - 8
---

# Laboratorio de componentes, quanta y gobierno

[[Obsidian/lecturas/Fundamentals of Software Architecture/00 Empieza aquí|← Inicio del libro]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Apoyo y repaso/00 Índice|Apoyo y repaso]]

**Objetivo:** conectar las responsabilidades del capítulo 8, los límites operacionales del 7 y las comprobaciones del 6. Conocer tres definiciones no basta: debes poder explicar cómo una decisión en un nivel cambia lo que puedes medir y garantizar en otro.

> [!info] Procedencia
> Este caso y todas sus cifras son una elaboración didáctica propia. No es una kata transcrita del libro. Las ideas de base se desarrollan en [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/00 Índice|capítulo 6]], [[Obsidian/lecturas/Fundamentals of Software Architecture/07 Alcance y quanta/00 Índice|capítulo 7]] y [[Obsidian/lecturas/Fundamentals of Software Architecture/08 Pensamiento basado en componentes/00 Índice|capítulo 8]].

## 1. Leer el mapa sin confundir sus niveles

![De componentes lógicos a un quantum y a sus comprobaciones](../Recursos%20visuales/Cap%C3%ADtulos%206%20a%208/c678-integracion.png)

A la izquierda, los rectángulos son responsabilidades lógicas de PedidoClaro: capturar un pedido, reservar existencias y comunicar el estado. Las flechas expresan colaboración, sin fijar todavía un protocolo ni una ubicación. En el centro, el rectángulo grande reúne un desplegable y la base de datos necesaria para funcionar. El cilindro representa persistencia. A la derecha aparecen dos comprobaciones diferentes y la decisión que sigue a sus resultados.

Cada componente tiene una capacidad propia y, en esta alternativa, los tres se implementan dentro del mismo desplegable. Como dependen de la misma base de datos, no basta con entregar el ejecutable para tener una unidad operativa: también necesita esos datos y su disponibilidad. La evaluación final comprueba dos promesas: que las dependencias respetan una regla estructural y que el recorrido observado cumple el umbral de latencia bajo una carga declarada.

Las flechas grandes indican el avance del razonamiento desde el modelo lógico al límite operacional y su evidencia. No son mensajes de red. Las flechas verticales de la derecha ordenan la lectura de la evaluación; no dicen que una prueba estructural cause una latencia determinada.

**Conclusión.** Tres componentes no implican tres microservicios ni tres quanta. Una buena separación lógica permite razonar sobre responsabilidades; el despliegue, los datos y las dependencias determinan qué partes pueden operar de forma independiente.

El dibujo oculta infraestructura, autenticación, fallos y detalles transaccionales para centrarse en esos tres niveles. La alternativa monolítica es un supuesto del ejercicio, no la respuesta universal. «Notificar» aquí significa producir una confirmación dentro de la aplicación; si se añade un proveedor de correo externo, hay que dibujar y analizar esa dependencia.

## 2. Partir de un escenario verificable

El negocio solicita: «Durante el almuerzo, el cliente debe saber pronto si su pedido quedó aceptado».

Hay varias interpretaciones posibles de «aceptado»: haber recibido la solicitud, persistirla, reservar existencias o confirmar un pago. Acordamos para este ejercicio que significa **pedido persistido con reserva confirmada**, y que la respuesta informa ese estado. Quedan fuera el tiempo de entrega física y cualquier proceso posterior no declarado.

| Elemento | Supuesto del ejercicio | Por qué hace falta |
|---|---|---|
| Operación | Crear un pedido y confirmar su reserva | Fija dónde empieza y termina la medición |
| Carga | 40 solicitudes por segundo durante 15 minutos, después de 2 minutos de calentamiento | Una cifra sin carga comparable no explica capacidad |
| Entorno | Configuración y tamaño de datos documentados junto al ensayo | Permite repetir y comparar |
| Latencia | p95 de respuestas exitosas ≤ 300 ms | Explicita el percentil y su población |
| Fallos | Menos de 1 % de solicitudes fallidas sobre todos los intentos | Evita aparentar rapidez descartando errores |
| Invariante | No confirmar una reserva sin existencias disponibles | La rapidez no debe destruir la corrección |

Medir las respuestas exitosas y la tasa de fallos por separado evita esconder un problema: si solo 10 de 100 solicitudes terminan bien y son rápidas, su p95 no representa un sistema sano. Deben documentarse también timeouts, solicitudes canceladas y reintentos para no alterar silenciosamente el denominador.

## 3. Usar responsabilidades para crear componentes

Una primera implementación coloca toda la lógica en `ProcesarPedido`. Escribe lo que hace: valida campos, interpreta reglas de existencias, persiste datos y construye mensajes. Esa enumeración sugiere fronteras que hay que investigar.

La separación candidata es:

1. **Captura de pedidos:** recibe la intención del cliente, valida su estructura y conserva el estado del pedido.
2. **Reserva de existencias:** decide si se puede reservar y mantiene la regla de disponibilidad.
3. **Notificación de estado:** presenta el resultado acordado sin decidir reglas de inventario.

No se separa porque haya tres verbos: una responsabilidad coherente puede necesitar varios pasos. La pregunta es si cada conjunto tiene un propósito claro, reglas propias y razones de cambio que justifiquen su límite. Se asignan historias a los componentes y se revisan sus roles; si una historia no encaja, se investiga el modelo en lugar de forzarla dentro de una caja.

## 4. Elegir un límite operacional y declarar el costo

Supongamos que un equipo pequeño puede satisfacer los requisitos con un monolito modular y una base de datos compartida. La reserva y la creación del pedido pueden coordinarse dentro de una transacción local, siempre que la implementación y el motor elegidos permitan la garantía necesaria.

Se gana una forma sencilla de desplegar y coordinar esos cambios. Se conserva, a cambio, un alcance común para varios fallos y para el despliegue de código. Escalar el ejecutable tampoco elimina un cuello de botella de la base de datos.

Más adelante, el negocio exige que la consulta pública del catálogo soporte una carga muy superior y tenga un ritmo de cambios diferente. Esto abre una **pregunta arquitectónica**, no una orden automática de crear otro servicio. Hay que comparar separar ese recorrido, usar caché, replicar lecturas u optimizar consultas, según las garantías de consistencia que se necesiten. Solo una alternativa que resuelva el problema bajo sus restricciones justifica el costo nuevo.

## 5. Convertir promesas en funciones de aptitud

Una función de aptitud evalúa una característica relevante mediante un criterio objetivo. Una prueba funcional puede comprobar que un pedido se crea; otra comprobación, con intención arquitectónica, puede detectar si un cambio introduce ciclos o viola un presupuesto de latencia.

| Propiedad protegida | Comprobación | Momento | Respuesta ante incumplimiento |
|---|---|---|---|
| Modularidad | Inspeccionar dependencias entre módulos y buscar ciclos dirigidos | Integración de cambios | Identificar la nueva dependencia y revisar su necesidad |
| Rendimiento | Ensayo con la operación, carga, población y entorno declarados | Entorno de prueba controlado | Localizar el tramo que aumentó latencia |
| Corrección de reserva | Solicitudes concurrentes compiten por una existencia; se verifica que no se acepten ambas | Prueba de integración | Revisar coordinación y atomicidad |
| Operación del sistema | Observar latencia, errores y saturación sobre tráfico real | Ejecución en producción | Investigar la desviación con contexto |

Estas comprobaciones aportan evidencias distintas. Un grafo sin ciclos no demuestra buen rendimiento. Una prueba de carga aprobada no demuestra corrección ante todas las intercalaciones concurrentes. Un umbral necesita una razón y un responsable; cambiarlo solo para que la prueba pase destruye su valor como mecanismo de gobierno.

## 6. Interpretar un resultado y elegir el siguiente paso

En el ensayo hipotético se obtienen p95 = 470 ms y errores = 0,2 %. El objetivo de fallos se cumple y el de latencia no. Una traza muestra que las solicitudes lentas pasan gran parte de su tiempo esperando la consulta de existencias.

La inferencia defendible es que hay que investigar ese tramo: plan de consulta, volumen de datos, bloqueos, concurrencia y recursos. **El resultado todavía no demuestra que hagan falta microservicios.** Distribuir los componentes manteniendo la dependencia problemática puede añadir red sin resolver la espera.

Después de un cambio controlado, se repite el mismo ensayo. Si el nuevo resultado es p95 = 240 ms y errores = 0,2 %, se ha conseguido evidencia favorable **para ese escenario y entorno**. Conviene conservar la configuración y la serie temporal, porque una media de toda la prueba puede esconder una degradación al final.

## 7. Preguntas de transferencia

> [!question] Hay tres carpetas, tres componentes y una base de datos compartida. ¿Cuántos quanta hay?
> No se deduce contando carpetas. En la alternativa de este ejercicio, un desplegable y su base necesaria forman un quantum. Si la topología cambia, hay que volver a examinar las dependencias y el alcance.

> [!question] Una prueba funcional pasa y la comprobación de ciclos falla. ¿Existe contradicción?
> No. El comportamiento observado puede seguir siendo correcto mientras la estructura viola una regla que protege su evolución futura. Las pruebas responden preguntas distintas.

> [!question] Se sustituye una llamada síncrona por una cola. ¿Desaparecen las dependencias?
> No. Cambian el momento de coordinación y las consecuencias de esperar. Persisten contrato, broker, capacidad del consumidor, acumulación y tratamiento de fallos. Hay que medir también tiempo hasta el resultado final; aceptar un mensaje rápido no equivale a terminar el pedido rápido.

> [!question] ¿Qué cambia si notificar una reserva debe completarse antes de responder al cliente?
> La notificación pasa a formar parte del recorrido crítico medido. Su latencia y sus fallos afectan el resultado del escenario. Si depende de un proveedor, se debe incluir ese tramo y aclarar cómo se tratan sus timeouts.

> [!question] ¿Cuál es la evidencia mínima para proponer separar un componente?
> Un problema concreto, el mecanismo por el que la separación lo mejora, sus dependencias reales, los costos añadidos y una forma de comprobar el resultado. «Es más moderno» no permite predecir ni verificar la mejora.

## Fuentes para volver al mecanismo

- [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/04 Medición y gobierno.pdf#page=6|Capítulo 6, PDF pp. 6–13; impresas 86–93]]: gobierno y funciones de aptitud.
- [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/05 Alcance y componentes.pdf#page=2|Capítulo 7, PDF pp. 2–6; impresas 96–100]]: quanta, dependencias y comunicación.
- [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/05 Alcance y componentes.pdf#page=18|Capítulo 8, PDF pp. 18–27; impresas 112–121]]: identificación iterativa, responsabilidades y refinamiento.

---

[[Obsidian/lecturas/Fundamentals of Software Architecture/06 Apoyo y repaso/00 Índice|← Apoyo y repaso]]
