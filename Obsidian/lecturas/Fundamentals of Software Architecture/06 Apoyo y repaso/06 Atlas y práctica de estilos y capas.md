---
title: "Atlas y práctica · estilos y arquitectura por capas"
created: 2026-09-28
tags:
  - lecturas/software-architecture
  - repaso
---

# Atlas y práctica de estilos y capas

[[Obsidian/lecturas/Fundamentals of Software Architecture/00 Empieza aquí|← Inicio]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/09 Fundamentos de estilos arquitectónicos/00 Índice|Capítulo 9]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/10 Arquitectura por capas/00 Índice|Capítulo 10]]

La pregunta central de estos capítulos es **qué consecuencias trae elegir una estructura para el sistema**. Un nombre como «capas» o «microservicios» solo ayuda cuando puedes explicar cómo organiza responsabilidades, cambios, despliegues, datos y comunicación.

Este atlas conecta ocho imágenes con un caso resuelto. Las imágenes son elaboración propia; las referencias apuntan a los conceptos de los escaneos. Para los detalles temáticos sigue los índices de los capítulos.

## 1. Separar tres decisiones que suelen confundirse

**Partición:** cómo agrupas el código al nivel superior. **Despliegue:** qué partes puedes publicar y ejecutar separadamente. **Comunicación:** cómo colaboran esas partes durante un flujo.

Una aplicación puede estar organizada por dominios y seguir desplegándose como un único monolito. También puede separar técnicamente sus capas y colocarlas en máquinas distintas. Por eso «tiene módulos» no demuestra que tenga servicios independientes, y «usa la red» no demuestra que tenga buenos límites de negocio.

![Partición técnica y por dominio](../Recursos%20visuales/Cap%C3%ADtulos%209%20y%2010/c09-01-particion.png)

En la izquierda, el cambio de un pedido aparece en tres categorías técnicas. En la derecha, el módulo Pedidos reúne sus capas internas. El beneficio esperado del segundo diseño es concentrar cambios propios del dominio. Si el cambio afecta a contratos entre Pedidos e Inventario, habrá coordinación de todos modos. Las cajas describen organización: ninguna flecha significa una llamada HTTP por sí sola.

Fuente: PDF 06, pp. 8–13; impresas 137–142, figuras 9-2 a 9-6.

## 2. Entender por qué distribuir cambia el significado de fallar

![Respuesta perdida e idempotencia](../Recursos%20visuales/Cap%C3%ADtulos%209%20y%2010/c09-02-respuesta-perdida.png)

Sigue las flechas de arriba abajo. El servicio de pagos cobra y guarda su resultado; la respuesta se pierde. Pedidos observa un timeout, pero no conoce el resultado del cobro. Si interpreta «no recibí respuesta» como «no ocurrió nada», puede cobrar dos veces al reintentar.

La clave estable `pedido-42` permite reconocer un reintento de la misma operación, **si el receptor implementa esa garantía**. Debe definir cómo registra el resultado, resuelve dos solicitudes concurrentes y trata la reutilización de una clave con otros datos. El dibujo explica el propósito de la idempotencia; no demuestra que cualquier implementación sea correcta.

Fuente del problema: PDF 06, p. 15; impresa 144, figura 9-7. El cobro y su mitigación son ampliación didáctica.

## 3. Poner números antes de separar servicios

![Latencia y tráfico calculados](../Recursos%20visuales/Cap%C3%ADtulos%209%20y%2010/c09-03-latencia-datos.png)

La fila superior representa diez llamadas secuenciales. Con 100 ms de comunicación por llamada, añaden 1.000 ms al recorrido. Es un modelo aditivo sencillo; no incluye trabajo de negocio ni espera en colas. Si hay paralelismo, el camino crítico cambia y debe analizarse de nuevo.

Las cajas inferiores comparan dos cargas útiles a la misma frecuencia. El ahorro procede de enviar menos información por respuesta, no de asumir una red más rápida. Pasar de 500.000 bytes a 200 bytes reduce ese tráfico por un factor de 2.500. No implica que el tiempo total de la operación mejore 2.500 veces: pueden dominar otros costes.

Fuente: PDF 06, pp. 15–17; impresas 144–146. El gráfico corrige las unidades del ejemplo de la impresa 146.

## 4. Relacionar equipos con el trabajo que entregan

![Cuatro tipos de equipo](../Recursos%20visuales/Cap%C3%ADtulos%209%20y%2010/c09-04-equipos.png)

El centro representa un equipo responsable de una capacidad de negocio de extremo a extremo. Los otros equipos reducen obstáculos: aprender una técnica, utilizar un subsistema especializado o consumir servicios internos de plataforma. Las flechas representan apoyo organizativo, no protocolos de comunicación.

Un equipo pequeño no necesita crear cuatro departamentos. La distinción sirve para reconocer qué tipo de ayuda falta y evitar que un equipo de soporte termine convirtiéndose en una aprobación obligatoria para cada cambio. La topología de equipos influye en la arquitectura, pero no determina mecánicamente una única estructura.

Fuente: PDF 06, pp. 10 y 22; impresas 139 y 151.

## 5. Leer una arquitectura por capas sin imaginar servidores inexistentes

![Capas lógicas y despliegue](../Recursos%20visuales/Cap%C3%ADtulos%209%20y%2010/c10-01-capas-despliegue.png)

Presentación adapta la interacción, Negocio decide reglas, Persistencia organiza el acceso y la base de datos ejecuta almacenamiento y consultas. En el ejemplo físico, las primeras tres responsabilidades viven dentro del mismo despliegue de aplicación. La base de datos es un proceso separado.

La separación lógica permite cambiar implementación conservando contratos. El despliegue conjunto sigue haciendo que las partes se publiquen juntas. Trasladar una capa a otra máquina conserva sus responsabilidades, pero añade latencia, fallos de comunicación y operación.

Fuente: PDF 07, pp. 1–3; impresas 153–155, figuras 10-1 y 10-2.

## 6. Interpretar correctamente «abierta» y «cerrada»

![Reglas de capas abiertas y cerradas](../Recursos%20visuales/Cap%C3%ADtulos%209%20y%2010/c10-02-abiertas-cerradas.png)

Negocio puede utilizar Servicios compartidos o saltarlo para llegar a Persistencia. Presentación no puede saltarse Negocio para llegar a Servicios: **la apertura de Servicios no anula el cierre de Negocio**. Esta es la diferencia entre una excepción delimitada y una aplicación donde cualquier parte conoce cualquier detalle.

Para que la regla tenga efecto, documenta sus razones y comprueba las dependencias. Un dibujo no impide que alguien importe una clase de una capa no autorizada.

Fuente: PDF 07, pp. 3–6; impresas 155–158, figuras 10-3 a 10-5.

## 7. Investigar el sumidero antes de cambiar reglas

![Sumidero y recorrido con responsabilidades](../Recursos%20visuales/Cap%C3%ADtulos%209%20y%2010/c10-03-sumidero.png)

En la consulta de nombre, dos capas solo reenvían. En la confirmación de pedido, esos pasos comprueban disponibilidad y calculan un descuento. El mecanismo importa: atravesar una capa es útil si protege una responsabilidad o contrato, aunque su implementación sea corta.

Cuenta cuántas solicitudes y cuánto tiempo corresponden a pasos sin transformación, reglas ni otra responsabilidad relevante. El 80/20 que propone el libro orienta la discusión; no sustituye medidas ni autoriza automáticamente a eliminar todas las capas.

Fuente: PDF 07, pp. 6–7; impresas 158–159.

## 8. Distinguir aislamiento interno y redundancia

![Réplicas y base de datos compartida](../Recursos%20visuales/Cap%C3%ADtulos%209%20y%2010/c10-04-fallos-escala.png)

Agotar la memoria de una réplica derriba las capas que viven en ese proceso. Si existen réplicas intercambiables y un balanceador que evita la instancia caída, otras pueden atender. Son dos escalas de análisis diferentes: aislamiento entre funciones dentro del proceso y tolerancia a la pérdida de una instancia.

Todas las réplicas siguen utilizando la misma capacidad de almacenamiento. Más procesos pueden aumentar conexiones y presión sobre la base. Además, un defecto común puede derribarlos a todos. Por eso replicar exige diseñar estado, salud, recuperación y dependencias.

Fuente del riesgo: PDF 07, pp. 7 y 10; impresas 159 y 162. Las réplicas son una ampliación para evitar interpretar las limitaciones del estilo como imposibilidades absolutas.

## Laboratorio resuelto: PedidoClaro abre una segunda ciudad

> [!info] Caso inventado
> PedidoClaro no es Silicon Sandwiches. Los números y condiciones siguientes son supuestos didácticos, no requisitos del libro ni medidas de un producto real.

PedidoClaro tiene un equipo de seis personas, un único despliegue, una base de datos y tres capas de código: Presentación, Negocio y Persistencia. Las promociones cambian semanalmente; la mayor parte de esas modificaciones no afecta a entregas. El sistema debe confirmar pedidos en menos de 800 ms en el percentil 95 bajo la carga acordada. Un proveedor externo procesa los pagos. Se proponen dos cambios: dividir la aplicación en diez servicios y permitir a Presentación consultar cualquier tabla directamente.

### Paso 1: identificar qué problema pretende resolver cada cambio

Separar diez servicios solo tiene sentido si resuelve una necesidad concreta: publicación independiente, crecimiento desigual, propiedad del equipo o aislamiento. «Vamos a crecer» no especifica cuál. El acceso directo a tablas pretende reducir pasos, pero mezcla la interfaz con el esquema de almacenamiento y podría omitir reglas de acceso o negocio.

Antes de elegir, mediríamos cambios que se coordinan, tiempos de despliegue, saturación, latencia por tramo y coste de las capas. La arquitectura debe responder al problema observado.

### Paso 2: comparar alternativas sin confundir ejes

| Alternativa | Ventaja esperada | Coste o riesgo | Evidencia necesaria |
|---|---|---|---|
| Mantener capas bien gobernadas | Simplicidad y cambio técnico localizado | Un cambio de dominio cruza capas; despliegue conjunto | Historial de cambios y coste de regresión |
| Agrupar por dominio dentro del monolito | Concentrar Promociones, Pedidos y Entregas | Deben definirse contratos y propiedad de datos | Cambios que realmente quedan dentro de cada módulo |
| Separar servicios seleccionados | Publicación y capacidad independientes donde hagan falta | Red, contratos, observabilidad y coordinación de datos | Necesidad operacional específica y coste asumible |

La segunda alternativa se apoya en la partición del capítulo 9; esta sección no pretende explicar íntegramente el estilo del capítulo 11, que no está en los nuevos escaneos.

### Paso 3: construir un presupuesto de latencia

Supongamos que las diez llamadas propuestas son secuenciales y cada una añade exactamente 70 ms en un escenario simplificado. La comunicación consume 700 ms; si el procesamiento añade otros 180 ms, el recorrido tarda 880 ms. Ya falla el objetivo de 800 ms en ese escenario.

Este cálculo descarta una expectativa ingenua, pero **no calcula el p95 real**. Para validarlo necesitamos trazas del recorrido completo bajo carga. No basta sumar diez p95 de servicios: sus distribuciones y correlaciones determinan el percentil del total. Paralelizar solo es posible cuando no hay dependencias que exijan secuencia.

### Paso 4: tratar el pago como una operación con resultado incierto

Una respuesta perdida del proveedor no autoriza a marcar el cobro como fallido ni a emitir otro cobro sin control. Registraríamos un identificador estable de operación, un estado pendiente y una vía de consulta o conciliación. Si el proveedor soporta idempotencia, seguiríamos su contrato y su plazo de retención. Si no, el diseño debe contemplar esa limitación.

Si ya reservamos inventario y el pago falla de verdad, liberar esa reserva es una compensación. Puede fallar también: hacen falta estados observables, reintentos controlados y un procedimiento de conciliación. Compensar no equivale a retroceder el tiempo ni a una transacción local atómica.

### Paso 5: escoger una decisión revisable

Con estos supuestos, conservar un despliegue y mejorar límites de dominio es una propuesta razonable para experimentar. Mantendríamos las reglas de acceso entre capas dentro de cada módulo y el adaptador al proveedor de pagos. No aprobaríamos acceso libre desde Presentación a tablas sin identificar una consulta concreta, su contrato y sus controles.

El resultado se documentaría con consecuencias: simplifica la operación inicial, pero mantiene despliegue y recursos compartidos. Se revisaría si una parte necesita escala diferente, si los cambios de módulos se bloquean entre sí o si los objetivos dejan de cumplirse. No se obtiene esa decisión sumando estrellas; se justifica mediante restricciones y evidencia.

## Comprobación de comprensión

1. **¿Un monolito por dominios deja de ser monolito?** No: cambia la organización superior, no necesariamente la unidad de despliegue.
2. **¿Una capa abierta permite que todas las capas superiores accedan a cualquiera inferior?** No: siguen vigentes los cierres intermedios y las rutas autorizadas.
3. **¿Timeout significa operación no realizada?** No: puede haberse perdido la respuesta de una operación completada.
4. **¿Menos bytes garantizan una operación proporcionalmente más rápida?** No: reducen carga útil; el coste dominante puede estar en otra parte.
5. **¿Tres réplicas permiten escalar solo Promociones?** No: cada réplica sigue conteniendo el monolito entero; la capacidad compartida también limita.
6. **¿Un equipo de plataforma es simplemente quien aprueba despliegues?** No: su contribución es ofrecer capacidades internas que reduzcan fricción y faciliten autonomía con el gobierno necesario.
7. **¿Qué evidencia haría revisar la decisión del laboratorio?** Por ejemplo, trazas que revelen saturación específica, publicaciones de un dominio bloqueadas por otros o incumplimiento sostenido de los objetivos acordados.

## Referencias y siguiente lectura

- [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/06 Fundamentos de estilos arquitectónicos.pdf#page=8|PDF 06 desde la partición arquitectónica]]: capítulos y páginas detallados en cada sección.
- [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/07 Arquitectura por capas.pdf#page=1|PDF 07: arquitectura por capas]].
- [[Obsidian/lecturas/Fundamentals of Software Architecture/90 Fuentes y revisión/05 Ampliación capítulos 9 y 10|Mapa de cobertura y precisiones técnicas]].
- [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Apoyo y repaso/04 Método completo para tomar decisiones|Método de decisión]]: conecta el análisis con las características arquitectónicas ya estudiadas.
