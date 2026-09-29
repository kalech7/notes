---
title: "06 · Gobierno en operación, ingeniería del caos y práctica integradora"
created: 2026-09-28
tags:
  - lecturas/software-architecture
  - arquitectura/medicion
---

# Gobierno en operación, ingeniería del caos y práctica integradora

[[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/00 Índice|← Índice del capítulo]]

> [!info] Fuente y alcance
> *Fundamentals of Software Architecture*, capítulo 6. **PDF 12–13 · impresas 92–93; síntesis del capítulo** del [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/04 Medición y gobierno.pdf|PDF conservado]]. «Libro» identifica sus planteamientos; las ampliaciones, plantillas y datos supuestos se señalan como elaboración didáctica.

No todas las propiedades relevantes se comprueban analizando código. Un servicio puede tener dependencias impecables y aun así colapsar cuando una dependencia responde lentamente. El capítulo amplía las funciones de aptitud a operación y presenta los ejemplos históricos de Netflix para mostrar que **se puede evaluar cómo conserva el sistema una propiedad bajo condiciones adversas**.

## El cambio de perspectiva del caos

El razonamiento del libro parte de asumir que los fallos ocurrirán. Al trasladarse a la nube, no se controla directamente cada detalle de la infraestructura; diseñar como si toda dependencia respondiera siempre bien sería frágil. Introducir perturbaciones permite buscar evidencia sobre tolerancia a fallos y recuperación.

Los nombres siguientes se conservan como **ejemplos históricos descritos por el texto**, no como catálogo de herramientas actuales o recomendaciones de instalación:

| Mecanismo mencionado | Qué representa en la explicación |
|---|---|
| Chaos Monkey y familia | Introducir fallos operativos para evaluar resistencia |
| Latency Monkey | Simular latencia elevada de dependencias |
| Chaos Kong | Probar una interrupción de gran alcance en infraestructura |
| Conformity Monkey | Verificar reglas de conformidad operativa |
| Security Monkey | Buscar configuraciones y problemas de seguridad conocidos |
| Janitor Monkey | Identificar recursos huérfanos que siguen consumiendo dinero |

El capítulo describe la interrupción de Chaos Kong como fallo de un centro de datos de Amazon. Aquí se conserva el sentido del ejemplo —ensayar una pérdida importante de infraestructura— sin convertir la terminología del texto en una descripción actual y exhaustiva del alcance de esa herramienta.

Los últimos mecanismos muestran que gobierno no se limita a «romper cosas». También puede comprobar configuraciones o detectar recursos sin consumidores. Una instancia sin uso sigue generando costo; identificarla conecta evidencia operativa con una decisión de mantenimiento.

## Diagrama: comprobaciones antes y después de desplegar

![Ciclo de comprobación arquitectónica durante desarrollo y operación](../Recursos%20visuales/Cap%C3%ADtulos%206%20a%208/c06-08-gobierno.png)

**Procedencia:** ampliación propia que conecta ejemplos de las pp. 89–93.

En la parte superior, el recorrido va de cambio de código → verificación → resultado. Abajo se observa operación, se formula un experimento de fallo y se aprende. Las flechas organizan un recorrido conceptual, no un pipeline que obligue a ejecutar caos después de cada despliegue. La flecha azul lleva el aprendizaje de vuelta a cambios de código o de reglas.

**Secuencia causal:** una comprobación de capas puede prevenir una importación indeseada, pero no revelar qué ocurre cuando la red tarda cinco segundos. Un experimento operativo puede mostrar acumulación de peticiones y agotar un recurso. Con esa evidencia se modifica el diseño —por ejemplo, sus límites de espera— y se añade una verificación que evite la regresión.

**Conclusión:** preservar arquitectura requiere observar tanto estructura como comportamiento. **Límites:** un experimento solo da evidencia sobre el escenario, entorno y duración ensayados. Superarlo no demuestra tolerancia a todos los fallos posibles.

## Ejemplo de experimento explicado

Este protocolo y sus cifras son **supuestos didácticos**, no instrucciones copiadas del libro ni un experimento realizado.

**Hipótesis:** si el servicio externo de recomendaciones responde lentamente, la compra seguirá funcionando sin recomendaciones.

**Escenario:** ambiente de prueba representativo, carga de 100 peticiones por segundo; agregar dos segundos de latencia al servicio de recomendaciones durante cinco minutos.

**Qué observar:** tasa de compras exitosas, latencia de compra, peticiones pendientes y tiempo de recuperación al retirar la perturbación. El servicio de recomendaciones y la compra deben observarse por separado para no diluir el efecto.

**Criterio supuesto:** éxito de compra al menos 99 %, p95 de compra no superior a 500 ms y recuperación en menos de un minuto. Estos objetivos requieren un diseño que no espere indefinidamente la respuesta opcional.

**Resultado hipotético:** el éxito se mantiene, pero p95 sube a 2 300 ms. La hipótesis compuesta falla: continuidad funcional no equivale a mantener rendimiento. Investigaríamos dónde se espera al proveedor y cómo se aplican los tiempos límite. Reducir un timeout sin comprender el comportamiento de reintentos podría generar más carga; cada corrección necesita evidencia.

**Control del experimento:** definir alcance, condiciones de parada y reversión permite distinguir ensayo controlado de interrupción arbitraria. La nota enseña el mecanismo; no autoriza ejecutar perturbaciones en ningún entorno real.

## Práctica integradora: PedidoClaro

PedidoClaro es el caso inventado usado en las notas anteriores del libro: una tienda de sándwiches. Estos datos también son supuestos. Una promoción aumenta la demanda y el equipo quiere conservar rapidez de compra, independencia de módulos y facilidad de despliegue.

| Necesidad | Evidencia propuesta | Regla supuesta | Momento |
|---|---|---|---|
| Compra rápida | Distribución de latencia por operación | Al menos 99 % bajo 500 ms con carga definida | Prueba de carga y operación |
| Modularidad | Grafo de paquetes de negocio | Sin ciclos intermodulares | Cada integración |
| Respeto de capas | Dependencias controlador/servicio/persistencia | Sin acceso directo controlador → persistencia | Cada integración |
| Cambio comprensible | CC por método y revisión de contexto | Revisar métodos por encima del umbral acordado | Desarrollo |
| Despliegue fiable | Resultado y duración de cada despliegue | Evaluar tasa de éxito y casos extremos | Por despliegue y tendencia |
| Resistencia a lentitud externa | Experimento con dependencia opcional | Compra mantiene el presupuesto establecido | Ensayo controlado |

### Resolución razonada

1. **Precisar el objetivo operativo.** «Rápido durante la promoción» exige carga, entorno, ventana y operaciones concretas. No se mide la media global mezclando compra con páginas estáticas.
2. **Definir módulos y capas.** Antes de buscar ciclos, acordar qué elementos son nodos y qué dependencia se analiza. Una regla vaga produce resultados difíciles de interpretar.
3. **Probar que la verificación detecta una infracción conocida.** Como ampliación de calidad del verificador, introducir en una rama de prueba una dependencia deliberadamente prohibida permite comprobar que la configuración no está vacía o mirando otro directorio.
4. **Explicar cada fallo.** La salida debe incluir ruta del ciclo, dependencia o escenario que incumple, para facilitar una corrección concreta.
5. **Revisar los resultados conjuntamente.** Pasar todas las pruebas de código no sustituye el ensayo operativo; cumplir rendimiento no justifica ocultar una dependencia problemática.

## Preguntas de repaso con respuesta

**¿Puede un sistema pasar todas sus funciones de aptitud y tener mala arquitectura?** Sí. Las funciones pueden cubrir pocas propiedades, usar escenarios irreales o tener criterios equivocados.

**¿Se debe eliminar una regla cuando bloquea una entrega?** El bloqueo por sí solo no demuestra que la regla sea errónea. Hay que examinar el principio, la infracción y el costo de la excepción; una excepción razonada necesita alcance y revisión, no una desactivación silenciosa.

**¿Una métrica objetiva elimina el juicio humano?** No. El dato puede ser reproducible mientras su interpretación, su umbral y su relevancia siguen dependiendo del contexto.

**¿Qué une las cuatro figuras originales del capítulo?** La primera representa una propiedad del flujo de código; la segunda muestra mecanismos para evaluar propiedades; la tercera revela una degradación de modularidad; la cuarta muestra una estructura cuya intención puede gobernarse. El recorrido completo va de **describir y medir** a **verificar y conservar**.

---

[[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/07 Capas y reglas de dependencia|← Anterior]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/00 Índice|Índice]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/00 Índice|Siguiente →]]
