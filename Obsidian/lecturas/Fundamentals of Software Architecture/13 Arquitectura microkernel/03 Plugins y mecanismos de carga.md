---
title: "13 · Plugins y mecanismos de carga"
created: 2026-09-29
capitulo: 13
tags:
  - lecturas/software-architecture
  - arquitectura/microkernel
---

# Plugins y mecanismos de carga

[[Obsidian/lecturas/Fundamentals of Software Architecture/13 Arquitectura microkernel/00 Índice|← Índice del capítulo 13]]

**Plugin es un papel arquitectónico; biblioteca, paquete o servicio son maneras de implementarlo.** La forma de empaquetar decide qué puede cambiarse sin recompilar o reiniciar, pero no garantiza que el componente respete la frontera.

## Qué contiene una extensión

El libro atribuye al plugin procesamiento especializado, características adicionales o código de personalización. En Going Green, una extensión de teléfono contiene las reglas para evaluar ese modelo; el núcleo conoce la operación de evaluar y el resultado esperado. Idealmente, una extensión no invoca otras extensiones.

Un plugin demasiado pequeño puede fragmentar innecesariamente una regla coherente. Uno demasiado grande puede esconder muchas variantes que vuelven a cambiar juntas. La unidad útil es una capacidad con una razón reconocible para cambiar: «evaluar modelo A» o «aplicar reglas de jurisdicción B». Un archivo de utilidades no se vuelve plugin solo por ponerlo en una carpeta llamada `plugins`.

## Biblioteca separada frente a paquete del mismo proyecto

La figura 13-4 empaqueta plugins como bibliotecas: JAR en Java, DLL en entornos que utilizan ese formato, o paquetes equivalentes en otros lenguajes. Un **JAR** es un archivo de distribución que puede contener clases y recursos Java. El núcleo necesita localizar e instanciar un punto de entrada de la biblioteca; copiar un archivo al disco no basta para definir cómo integrarlo.

La figura 13-5 usa paquetes o espacios de nombres dentro del mismo proyecto. Un **paquete** agrupa código y nombres, pero no crea por sí mismo una entrega independiente. Es una solución más sencilla si la aplicación se publica completa y no necesita administrar extensiones en caliente.

El libro recomienda una estructura semántica como aplicación → plugins → dominio → contexto. En código propio se puede expresar como `app.plugins.assessment.iphone6s`: deja visible el papel de extensión, el dominio de evaluación y la variante. La grafía `plug-in` utilizada en la explicación del libro es una etiqueta conceptual; el guion no se debe copiar como identificador de paquete Java.

| Opción | Qué separa | Qué todavía hay que decidir |
|---|---|---|
| Paquete del proyecto | Organización y dependencias del código | Reglas de importación, selección y pruebas |
| Biblioteca empaquetada | Artefacto de extensión | Cargador, compatibilidad, actualización y recursos |
| Servicio remoto | Proceso y potencialmente entrega | Transporte, errores parciales y operación |

## Compilación y ejecución son decisiones distintas

En plugins **basados en compilación**, el conjunto se integra para construir la entrega. Agregar, modificar o retirar uno requiere publicar de nuevo la aplicación monolítica. La frontera sigue aportando pruebas y mantenimiento, aunque el despliegue sea conjunto.

En plugins **gestionados en ejecución**, existe un mecanismo para descubrir, activar y retirar capacidades mientras el núcleo continúa funcionando. El libro menciona OSGi y otras tecnologías como ejemplos de infraestructura. No es una propiedad gratuita: la plataforma necesita controlar dependencias, recursos y ciclo de vida.

Un ciclo didáctico completo sería: descubrir el artefacto → verificar contrato compatible → crear instancia → registrar capacidad → aceptar solicitudes → dejar de aceptar trabajo → terminar o trasladar lo pendiente → liberar recursos → retirar registro. Saltar el paso de drenaje puede dejar una evaluación en medio de una actualización. Dejar referencias a objetos retirados puede mantener código o recursos activos.

Como precisión verificada en fuente primaria, **Java `ServiceLoader` descubre y carga implementaciones de un servicio definido por una interfaz o clase**; no constituye por sí solo una plataforma completa de actualización en caliente. OSGi especifica operaciones de instalación, inicio, parada, actualización y desinstalación de bundles. Esta ampliación aclara el mecanismo sin sustituir el planteamiento del capítulo. [API oficial de ServiceLoader](https://docs.oracle.com/en/java/javase/26/docs/api/java.base/java/util/ServiceLoader.html), [ciclo de vida de OSGi Core 7](https://docs.osgi.org/specification/osgi.core/7.0.0/framework.lifecycle.html).

## Qué hace realmente el ejemplo de reflexión

El código del libro consulta el registro, obtiene un nombre de clase, la localiza mediante `Class.forName`, consigue un constructor y crea un objeto. **Reflexión** significa inspeccionar o utilizar tipos a partir de información disponible durante la ejecución, en lugar de fijar todas las clases concretas directamente en la llamada del código fuente. Finalmente convierte la instancia al contrato esperado y ejecuta la evaluación.

Eso explica la indirección, pero deja decisiones abiertas: qué hacer si no existe la clave, la clase no está disponible, el constructor falla o el tipo no cumple el contrato. Tampoco desarrolla inyección de configuración, duración de la instancia o seguridad de concurrencia. Son omisiones del ejemplo didáctico, no propiedades resueltas por usar reflexión.

Un diseño propio puede registrar directamente objetos ya construidos o fábricas. Una **fábrica** crea una implementación cuando se la necesita. Así el núcleo conserva una llamada uniforme sin tener que conocer nombres de clases. Se gana comprobación y claridad a cambio de decidir explícitamente cómo construir el catálogo.

> [!question]- ¿Biblioteca separada significa actualización sin reinicio?
> No. El artefacto separado ayuda a distribuir, pero la actualización depende de cargadores, referencias, trabajos activos y recursos. El capítulo diferencia precisamente el empaquetado y la gestión del ciclo de vida.

> [!question]- ¿Crear una instancia nueva por solicitud es obligatorio?
> No. El fragmento del libro lo hace para ilustrar la invocación. Un objeto compartido puede ahorrar creación, pero obliga a decidir si su estado mutable soporta solicitudes simultáneas. Esa decisión pertenece al diseño concreto.

## Fuente principal

[[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/10 Arquitectura microkernel.pdf#page=3|PDF 3 y 6–7 · impresas 195 y 198–199 · figuras 13-4 y 13-5]]. Ciclo de drenaje y alternativas con fábricas son elaboraciones propias. Las precisiones sobre APIs tienen fuentes primarias arriba.

---

[[Obsidian/lecturas/Fundamentals of Software Architecture/13 Arquitectura microkernel/02 Composición espectro e interfaz|← Anterior]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/13 Arquitectura microkernel/04 Registro contratos y adaptación|Siguiente →]]
