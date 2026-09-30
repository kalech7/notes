---
title: "13 · Casos del libro y variaciones"
created: 2026-09-29
capitulo: 13
tags:
  - lecturas/software-architecture
  - arquitectura/microkernel
---

# Casos del libro y variaciones

[[Obsidian/lecturas/Fundamentals of Software Architecture/13 Arquitectura microkernel/00 Índice|← Índice del capítulo 13]]

**Los casos comparten una estructura: proceso común y variaciones encapsuladas.** El interés no es memorizar marcas, sino identificar qué pertenece al núcleo y qué cambia dentro de cada extensión.

## Going Green: evaluar dispositivos

El caso de reciclaje aparece a lo largo del capítulo. El problema inicial es valorar cada modelo con reglas diferentes. Una cadena central decide entre iPhone 6s, iPad y Galaxy 5 y llama a rutinas particulares. Cada modelo añadido modifica el mismo método.

En la versión microkernel, el núcleo recibe el identificador del dispositivo, consulta un registro y obtiene un evaluador que implementa el contrato. Cada evaluador contiene reglas y conocimiento de su modelo. La salida incluye informe, posibilidad de reventa, valor y precio recomendado. El núcleo puede guardar o presentar la salida sin conocer las reglas que produjeron la valoración.

| Parte estable | Parte variable | Por qué separarlas |
|---|---|---|
| Recibir y registrar un dispositivo | Pruebas concretas del modelo | Los modelos cambian más que el flujo de recepción |
| Seleccionar e invocar un evaluador | Algoritmo y reglas de evaluación | El núcleo necesita una operación común |
| Mostrar el resultado | Contenido del informe especializado | El plugin conoce sus razones y diagnóstico |

El libro muestra varias realizaciones del mismo caso: biblioteca, paquete, acceso remoto y datos propios. No son cuatro estilos de negocio diferentes. Conservan la relación núcleo–evaluador y cambian empaquetado, transporte o propiedad de datos.

Un fallo de diseño sería que el núcleo, después de recibir el informe, añadiera `si modelo=telefonoA, ajustar el precio`. La regla especializada habría regresado al centro. Si el ajuste es realmente común a todos los equipos, hay que nombrarlo como política transversal y aplicarlo con significado explícito.

## Pagos: variaciones dentro de un dominio

El capítulo considera el procesamiento de pagos como un servicio de dominio que actúa como núcleo. Tarjeta, PayPal, crédito de tienda, tarjeta regalo y orden de compra son posibles plugins. Todos participan en «procesar pago», pero las interacciones particulares varían.

Como ampliación propia, una capacidad común podría recibir identificador, importe, moneda y referencia de operación, y devolver estado y referencia del proveedor. Sin embargo, los medios no son idénticos: algunos pueden autorizar primero y capturar después; otros pueden requerir pasos humanos. Un contrato demasiado simplificado puede forzar al núcleo a conocer esas diferencias. La solución consiste en describir capacidades y estados, en lugar de fingir que todo es una llamada instantánea a `pagar`.

El ejemplo muestra una composición: un módulo o servicio del núcleo puede utilizar su propio microkernel interno. No obliga a que cada medio de pago sea un microservicio ni afirma que un proveedor externo sea un plugin cargado localmente.

## Preparación fiscal: resumen y formularios

El ejemplo del libro utiliza el formulario estadounidense 1040 como resumen central de información. Las cantidades que terminan en ese resumen pueden requerir otros formularios y hojas de trabajo. Cada formulario adicional puede implementarse como plugin que calcula una parte del resultado; el núcleo coordina y consolida.

La analogía muestra una separación por variación normativa. Una modificación de un formulario puede quedar contenida en su extensión si mantiene el contrato de resultado. Una nueva hoja puede añadirse sin mezclar todas sus reglas con las demás. El componente `AuditChecker`, citado en el registro, representa otra capacidad fiscal: señalar datos que el producto considera susceptibles de revisión.

Estas son descripciones del caso pedagógico del libro, **no instrucciones fiscales ni afirmaciones sobre formularios o normativa actuales**. Para comprender la arquitectura no hace falta conocer las reglas tributarias reales: basta reconocer una coordinación estable y cálculos especializados que evolucionan.

Un límite práctico aparece si las hojas dependen entre sí. Como elaboración propia, el núcleo puede coordinar resultados intermedios mediante contratos, pero una extensión que llama libremente a otras crea el riesgo de dependencias transitivas de la nota anterior. Las reglas compartidas necesitan dueño definido.

## Seguros: proceso común y reglas por jurisdicción

El libro plantea que presentar y tramitar un siniestro puede seguir un flujo relativamente estable mientras las reglas cambian según la jurisdicción. Cada conjunto de reglas puede vivir en un plugin, implementado en código o mediante una instancia particular de un motor de reglas.

Un **motor de reglas** permite expresar decisiones declarativamente: se especifican condiciones y acciones, en lugar de escribir todo el control como procedimientos. Puede usar herramientas visuales o un lenguaje de dominio. La forma declarativa no impide el acoplamiento: reglas que modifican datos compartidos o activan muchas otras reglas pueden formar un sistema difícil de comprender.

El capítulo relaciona ese problema con *Big Ball of Mud*, una estructura sin límites claros donde un cambio pequeño exige verificar muchas partes. Separar por jurisdicción permite cambiar un conjunto sin reconstruir todo el motor común. El núcleo mantiene recepción y coordinación; el plugin administra conocimiento local.

El ejemplo de reemplazo de parabrisas sirve al libro para ilustrar que las condiciones varían entre jurisdicciones. No se toma aquí como una afirmación legal vigente. Lo que interesa es que una regla local no debería obligar a editar todos los demás conjuntos de reglas.

## Herramientas y productos extensibles

Eclipse, PMD, Jira y Jenkins aparecen como ejemplos del libro de productos con extensiones. Eclipse agrega capacidades de desarrollo; PMD ilustra análisis de código mediante reglas; Jira y Jenkins ilustran ampliación de herramientas. Chrome y Firefox aparecen como navegadores con capacidades añadidas.

Esto se debe leer junto al espectro del capítulo: **admitir extensiones no prueba que el núcleo sea mínimo**. Un navegador puede ser útil sin ellas y situarse hacia el extremo de más funcionalidad autónoma. El listado identifica la idea general de ampliación; no documenta la arquitectura exacta de cada versión actual ni equipara sus garantías de seguridad y carga.

La empresa de transporte internacional y la aseguradora, mencionadas al inicio, amplían el mismo encaje a personalización por reglas locales, legales o logísticas. En todos estos casos la estructura funciona cuando el dominio permite identificar variaciones coherentes.

> [!question]- ¿Un motor de reglas elimina la necesidad de arquitectura?
> No. Permite expresar decisiones de otra manera, pero todavía hay que definir límites, propiedad de datos, coordinación y dependencias. Un único motor con reglas entrelazadas puede conservar el mismo problema que un gran método con condiciones.

> [!question]- ¿Cuál es la pregunta que permite reconocer el patrón en otro negocio?
> «¿Qué recorrido se conserva y qué conocimiento cambia por variante?» Si se puede dar una respuesta concreta y un contrato coherente, existe un candidato para núcleo y plugins. Después hay que comprobar despliegue, datos y riesgos.

## Fuente principal

[[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/10 Arquitectura microkernel.pdf#page=2|PDF 2–3 y 6–10 · impresas 194–195 y 198–202 · Going Green y pagos]]; [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/10 Arquitectura microkernel.pdf#page=15|PDF 15–16 · impresas 207–208 · productos, impuestos y seguros]]. Los límites de contratos y estados se desarrollan como ejemplos propios.

---

[[Obsidian/lecturas/Fundamentals of Software Architecture/13 Arquitectura microkernel/08 Equipos características y elección|← Anterior]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/13 Arquitectura microkernel/10 Laboratorio y repaso resuelto|Siguiente →]]
