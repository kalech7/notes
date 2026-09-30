---
title: "14 · Topologías de datos y dependencias"
created: 2026-09-29
capitulo: 14
tags:
  - lecturas/software-architecture
  - arquitectura/service-based
---

# Topologías de datos y dependencias

[[Obsidian/lecturas/Fundamentals of Software Architecture/14 Arquitectura basada en servicios/00 Índice|← Índice del capítulo 14]]

**Separar los ejecutables sin pensar en sus datos deja una parte importante del acoplamiento intacta.** El capítulo permite una base compartida, bases por grupos de dominio y una base por servicio. Cada variante cambia quién puede consultar, quién puede escribir y qué coordinación exige un cambio.

## Base única compartida

Una base compartida puede conservar relaciones y consultas SQL directas. Si Pedidos necesita nombre del cliente y líneas del pedido, puede obtenerlos con consultas locales a tablas relacionadas, sin preguntar por red a tres servicios. Eso simplifica algunos reportes y hace más fácil una transacción local cuando sus cambios están dentro del mismo alcance.

El costo tiene tres dimensiones distintas. **Operación:** la caída o saturación del motor puede perjudicar a varios servicios. **Evolución:** cambiar una columna usada por varios obliga a preservar o coordinar contratos. **Autoridad:** si todos pueden escribir todas las tablas, una invariante puede quedar repartida entre lugares que no se conocen.

El estilo acepta compartir datos, pero no exige escritura irrestricta. Como elaboración propia, se puede definir que Facturación es responsable de las reglas de factura y que Informes tiene lectura limitada. Esto conserva la comodidad del motor común sin convertir toda tabla en propiedad informal de todos.

## Base por grupos

Algunos dominios pueden separarse y otros seguir juntos. En la variante intermedia de la figura 14-5 un servicio tiene su base y los otros comparten otra. La agrupación reduce parte del radio de impacto, a cambio de que las relaciones entre grupos necesiten una decisión explícita.

Ejemplo propio: Cotizaciones públicas utiliza una base propia y Operación interna comparte otra para recepción, evaluación y contabilidad. Las lecturas frecuentes del público ya no compiten directamente con cada consulta de la operación. Pero el estado interno que debe mostrarse al cliente necesita publicarse o sincronizarse; mover datos a otro motor no resuelve esa transferencia por sí solo.

## Base por servicio

Una base privada puede dar más autonomía de esquema y capacidad. También puede eliminar joins directos entre dominios y transacciones locales que antes cubrían todos sus cambios. El libro advierte que hay que comprobar si otros servicios requieren esos datos: si para cada operación terminan llamando a su propietario por red, la partición puede crear la comunicación que este estilo intenta limitar.

![Tres topologías de bases de datos](../Recursos%20visuales/Cap%C3%ADtulo%2014/c14-05-datos.png)

Las filas muestran tres decisiones de propiedad y acceso. En la primera todos dependen de la misma base; en la segunda hay dos grupos; en la tercera cada servicio tiene su almacenamiento. Las flechas identifican acceso directo, no un compromiso de atomicidad entre motores. La fila inferior dibuja menos datos compartidos, pero no muestra cómo se obtiene información ajena: esa pregunta sigue pendiente.

## Compartir dato o pedirlo por API

La preferencia del capítulo suele ser compartir datos antes que introducir muchas llamadas entre servicios. Es una orientación del estilo, no una ley de diseño universal. Una API puede proteger reglas y propiedad; una consulta compartida puede evitar una cadena remota y facilitar un reporte. La elección debe incluir compatibilidad, permisos, carga, actualidad y autoridad de escritura.

| Necesidad | Opción compatible con este estilo | Pregunta imprescindible |
|---|---|---|
| Leer referencias estables de clientes | Tablas comunes con contrato estable | ¿Qué servicios se rompen si cambia la estructura? |
| Consultar un estado para el público | Copia o proyección pública | ¿Cuánto retraso permite la experiencia? |
| Aplicar una regla exclusiva de Facturación | Operación de ese dominio | ¿Puede llamarse sin construir una cadena frágil? |
| Reporte de varios dominios | Consulta controlada a datos compartidos | ¿Interfiere con la carga de trabajo principal? |

Una **proyección** es una representación preparada para un uso de lectura particular, como una tabla pública con estado y fecha sin los detalles internos del diagnóstico. La copia reduce dependencias de lectura, pero obliga a especificar retraso, actualización y recuperación ante fallos. Esa ampliación es propia: el capítulo menciona sincronización y reflejo de tablas, sin desarrollar su implementación.

## Tres tipos de acoplamiento que conviene separar

**Acoplamiento de esquema**: Informes deja de funcionar si se elimina una columna. **Acoplamiento operacional**: un servicio pierde capacidad cuando se satura un motor común. **Acoplamiento de significado**: dos servicios interpretan «pedido aprobado» de manera distinta aunque la columna tenga el mismo nombre. Cambiar solo la topología física puede reducir el segundo sin arreglar los otros dos.

Tampoco «base por servicio» significa automáticamente un quantum por servicio. Una interfaz común, una dependencia síncrona obligatoria o un dato todavía compartido puede unir las capacidades en una misma unidad de dependencias arquitectónicas. El análisis de quanta se realiza con la topología completa, no contando cilindros.

> [!question]- ¿Separar bases aumenta siempre la consistencia?
> No. Puede mejorar propiedad y control de cambios, pero una operación que cruza motores suele requerir coordinación adicional. La consistencia local y la coherencia del flujo completo son propiedades diferentes.

> [!question]- ¿Una base compartida permite ahorrar todas las llamadas entre dominios?
> Puede evitar algunas lecturas remotas, pero una regla de negocio ajena no se obtiene simplemente leyendo una tabla. Antes de sustituir una API por SQL hay que comprobar qué validación, autorización y semántica se estaría omitiendo.

## Fuente principal

[[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/11 Arquitectura basada en servicios.pdf#page=7|PDF 7–8 · impresas 215–216 · figura 14-5]], y [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/11 Arquitectura basada en servicios.pdf#page=18|PDF 18 · impresa 226 · sincronización entre bases]].

---

[[Obsidian/lecturas/Fundamentals of Software Architecture/14 Arquitectura basada en servicios/04 Interfaces gateway y fronteras|← Anterior]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/14 Arquitectura basada en servicios/06 Esquemas bibliotecas y cambios|Siguiente →]]
