---
title: "13 · Equipos, características y elección"
created: 2026-09-29
capitulo: 13
tags:
  - lecturas/software-architecture
  - arquitectura/microkernel
---

# Equipos, características y elección

[[Obsidian/lecturas/Fundamentals of Software Architecture/13 Arquitectura microkernel/00 Índice|← Índice del capítulo 13]]

**Microkernel favorece personalización y ampliación con una operación relativamente sencilla, pero la forma monolítica habitual limita escala y tolerancia a fallos.** Las estrellas del libro expresan apoyo relativo del estilo, no mediciones ni garantías para un producto concreto.

## La tabla del libro, contrastada con el escaneo

| Característica | Valor de figura 13-9 | Por qué importa |
|---|---|---|
| Coste total | $ | La forma habitual requiere poca infraestructura distribuida |
| Tipo de partición | Dominio y técnica | El núcleo admite capas o módulos y los plugins representan variaciones |
| Número de quanta | 1 | El núcleo es el paso obligado en la topología descrita |
| Simplicidad | ★★★★☆ | Dos papeles principales y despliegue habitual conjunto |
| Modularidad | ★★★☆☆ | Las extensiones contienen capacidades, sujetas a buen contrato |
| Mantenibilidad | ★★★☆☆ | Las reglas particulares pueden cambiar de forma contenida |
| Testabilidad | ★★★☆☆ | Un plugin puede probarse con entradas y resultados delimitados |
| Desplegabilidad | ★★★☆☆ | La gestión en ejecución mejora cambios, pero no siempre existe |
| Evolucionabilidad | ★★★☆☆ | Se añaden o retiran variantes sin rehacer el flujo común |
| Capacidad de respuesta | ★★★☆☆ | Llamadas locales y selección de capacidades pueden reducir trabajo |
| Escalabilidad | ★☆☆☆☆ | La entrega monolítica obliga a escalar el conjunto |
| Elasticidad | ★☆☆☆☆ | Cambiar automáticamente capacidad granular resulta difícil |
| Tolerancia a fallos | ★☆☆☆☆ | Un proceso central puede concentrar el impacto de fallos |

Las puntuaciones son ordinales: cuatro estrellas no significan el doble de capacidad que dos. No se han convertido a un gráfico numérico. El coste `$` tampoco es un presupuesto en dólares: es una categoría relativa del libro.

**Hay una inconsistencia en el texto bajo la figura.** Menciona *reliability* con tres estrellas junto a testabilidad y desplegabilidad, pero la tabla no contiene una fila de fiabilidad. La tabla sí contiene mantenibilidad. Estas notas preservan la tabla y señalan la diferencia, sin inventar una puntuación adicional.

## Qué fortalezas tienen causa estructural

La mantenibilidad y la evolución mejoran si una modificación de reglas queda dentro de un plugin. El ejemplo fiscal del libro permite incorporar un formulario como una extensión y retirar otro que deja de ser necesario. La ganancia depende de conservar contrato y comportamiento del núcleo: si cada formulario obliga a modificar la coordinación, la ventaja disminuye.

La testabilidad mejora porque se puede dar una entrada a un evaluador y verificar su resultado sin recorrer todas las variantes. Eso reduce el alcance de pruebas específicas. Aun así se necesitan pruebas de selección, compatibilidad e integración. La desplegabilidad de tres estrellas refleja variantes: un plugin integrado por compilación exige publicar el monolito; uno gestionado en ejecución puede cambiar con menos alcance, si su ciclo de vida está resuelto.

La capacidad de respuesta recibe tres estrellas. El libro atribuye parte de esa ventaja a aplicaciones relativamente pequeñas, menos trabajo innecesario y menor presencia del antipatrón *Architecture Sinkhole*, donde capas reenvían solicitudes sin aportar trabajo. Son explicaciones generales de la valoración, no leyes: un núcleo que invoca cien plugins o un evaluador pesado puede responder lentamente.

WildFly aparece como ejemplo del libro de retirar capacidades innecesarias, como clustering, caché o mensajería, para evitar su coste. **Clustering** reúne varias instancias coordinadas; **caché** conserva resultados para reutilizarlos. La idea es ejecutar solo lo que el producto necesita. No se presenta aquí como una guía de configuración vigente de WildFly ni como una promesa de una mejora medida.

## Qué debilidades requieren otra decisión

**Escalabilidad** es poder atender más carga agregando capacidad; **elasticidad** es adaptar esa capacidad de manera dinámica a la demanda. Un plugin modular local no puede escalarse como una unidad de despliegue independiente si todo comparte el mismo proceso y entrega. Se puede ajustar concurrencia u optimizar el uso de recursos dentro del proceso, pero eso no crea una entrega separada por plugin. Replicar toda la aplicación puede ser posible, pero también replica capacidades poco utilizadas y exige revisar estado y coordinación.

La tolerancia a fallos es la capacidad de seguir prestando servicio cuando una parte falla. La separación de código ayuda a localizar errores, pero el núcleo sigue siendo un punto central. Plugins remotos pueden aislar procesos y permitir escalado específico, a costa de red y operación. Por eso no se debe aplicar la tabla sin cambios a esa variante distribuida.

## Equipos según el capítulo

| Tipo de equipo | Papel que describe el libro | Ejemplo propio |
|---|---|---|
| Alineado a un flujo de valor | Construye el núcleo y, según el producto, plugins | Equipo del proceso de reciclaje y sus capacidades comunes |
| Habilitador | Apoya experimentos y aprendizaje mediante comportamiento aislado | Probar una regla nueva de valoración en un plugin experimental |
| Subsistema complicado | Desarrolla capacidades especializadas | Evaluación de batería o analítica que requiere conocimiento experto |
| Plataforma | Atiende principalmente detalles operacionales | Empaquetado, instalación, observación y actualizaciones |

La frontera permite a un especialista trabajar en su capacidad sin asumir el flujo completo. El equipo del núcleo necesita ofrecer contratos comprensibles y soporte de integración. Si cada plugin requiere negociar cambios centrales, la estructura del software se convierte en una dependencia continua entre equipos.

El libro vincula equipos habilitadores con pruebas A/B y experimentos. Una **prueba A/B** compara variantes sobre grupos definidos. No basta con instalar dos plugins: se necesita una regla de asignación y una forma de evaluar resultados. Esas decisiones pertenecen al experimento y no quedan resueltas por la arquitectura.

## Cuándo elegirlo

El encaje es fuerte cuando el proceso general se mantiene y las variaciones son numerosas y frecuentes: dispositivos, métodos de pago, formularios o jurisdicciones. Conviene confirmar que cada variante puede expresarse mediante un contrato coherente y que la simplicidad de operar una entrega conjunta es valiosa.

Si las capacidades necesitan escala, disponibilidad y operación independientes como requisito principal, una variante local puede ser insuficiente. Si todas comparten reglas cambiantes de forma inseparable, una interfaz de plugins puede ocultar un dominio mal dividido. La decisión se toma sobre estas necesidades, no por la cantidad de herramientas conocidas que utilizan extensiones.

> [!question]- ¿Tres estrellas en testabilidad significa que solo se prueba tres quintas partes?
> No. Es una valoración relativa del apoyo del estilo a esa característica. La cobertura y eficacia de las pruebas dependen del producto y sus riesgos.

> [!question]- ¿Puede ser particionado por dominio y por técnica?
> Sí: el núcleo puede tener capas técnicas y las extensiones agrupar variaciones del negocio, o el núcleo puede organizarse por dominios. La figura 13-9 reconoce esa combinación para este estilo.

## Fuente principal

[[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/10 Arquitectura microkernel.pdf#page=12|PDF 12–15 · impresas 204–207 · equipos y figura 13-9]]. Ejemplos de equipos y criterios de elección desarrollan las causas del capítulo.

---

[[Obsidian/lecturas/Fundamentals of Software Architecture/13 Arquitectura microkernel/07 Riesgos dependencias y gobierno|← Anterior]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/13 Arquitectura microkernel/09 Casos del libro y variaciones|Siguiente →]]
