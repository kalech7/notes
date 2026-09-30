---
title: "DDIA — Sync engines y software local-first: cada dispositivo es un líder"
created: 2026-09-29
capitulo: 6
tags:
  - lecturas/ddia
  - arquitectura/replicacion
cobertura: "Impresas 220–222"
---

# DDIA — Sync engines y software local-first: cada dispositivo es un líder

[[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/00 Empieza aquí|Inicio del libro]] → [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/00 Índice|Índice de Replicación]]

La replicación multilíder entre regiones ya parecía extrema: varios centros de datos aceptan escrituras y se sincronizan después. El libro lleva la idea a su límite: **cada teléfono, portátil o pestaña del navegador puede ser un líder**. La red entre ellos ya no es un enlace dedicado entre regiones, sino una conexión que puede desaparecer durante horas o días.

> [!info] Recuerda antes
> - Un **líder** es una réplica que acepta escrituras de clientes y las propaga a otras réplicas.
> - En replicación **multilíder asíncrona**, cada líder confirma localmente sin esperar a los demás; la propagación ocurre después.
> - El **retraso de replicación** (*replication lag*) es el tiempo entre que una escritura ocurre en una réplica y se refleja en otra.

## Del calendario al técnico sin cobertura

Piensa en una empresa de mantenimiento eléctrico. Sus técnicos rellenan formularios de inspección en una tableta dentro de subestaciones donde no hay señal. Si la app necesitara al servidor para guardar cada campo, sería inútil allí. Por eso la tableta tiene su propia base de datos local: **acepta escrituras aunque no haya red**, igual que un líder. Cuando el técnico vuelve a tener conexión, un proceso de fondo sincroniza lo que cambió con el servidor y con los demás dispositivos del equipo.

El libro usa el calendario del móvil y del portátil: puedes consultar reuniones (lecturas) y crear nuevas (escrituras) en cualquier momento, con o sin internet. Arquitectónicamente es replicación multilíder entre regiones llevada al extremo: **cada dispositivo es una «región»** y el enlace entre regiones es extremadamente poco fiable. El retraso de replicación deja de medirse en milisegundos y pasa a medirse en horas o días.

Esta diferencia tiene una consecuencia directa. En un sistema de servidores, a veces puedes **evitar conflictos** enviando todas las escrituras de un registro al mismo líder. Un dispositivo desconectado no puede pedir permiso a nadie antes de escribir, así que esa estrategia no está disponible. La resolución de conflictos deja de ser opcional; se estudia en [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/09 Conflictos LWW siblings y reglas del dominio|conflictos y reglas del dominio]] y en [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/10 CRDT y transformación operacional|CRDT y OT]].

## La colaboración en tiempo real también es multilíder

Google Docs y Sheets, Figma o Linear se sienten instantáneos porque tu tecleo aparece en pantalla **sin esperar la ida y vuelta al servidor**, y las ediciones de tus colaboradores llegan con poca latencia. Imagina a tres personas editando el guion de un podcast: cada pestaña abierta es una réplica que aplica cambios locales primero y los envía después.

En el sentido amplio que usa el libro para la edición colaborativa, aunque la app no permita trabajar sin conexión, aplicar ediciones en varias copias antes de recibir respuesta ya plantea un problema multilíder: dos personas pueden modificar lo mismo sin haber visto el cambio de la otra. Eso describe las réplicas de la experiencia de edición; una interfaz optimista por sí sola no demuestra que el almacenamiento autoritativo del servidor tenga varios líderes. Edición offline y colaboración en tiempo real necesitan, por tanto, la misma infraestructura:

1. Capturar cada cambio que hace el usuario.
2. Enviarlo enseguida si hay red, o guardarlo en una cola local para después.
3. Recibir cambios de los colaboradores.
4. Fusionarlos con la copia local, resolviendo conflictos si hubo ediciones concurrentes.
5. Actualizar la interfaz con el resultado.

## Tres términos que se suelen mezclar

| Término | Qué es | Ejemplo |
|---|---|---|
| **Sync engine** (motor de sincronización) | La biblioteca o infraestructura que hace los cinco pasos anteriores | Automerge, Yjs, Firestore |
| **Offline-first** | Una app que sigue permitiendo editar sin conexión; puede usar un sync engine | La app de inspecciones del ejemplo |
| **Local-first** | Una app colaborativa offline-first que además **sigue funcionando si su fabricante apaga todos sus servicios en línea** | Git |

Local-first es la exigencia más fuerte. Se consigue con un sync engine que hable un **protocolo de sincronización abierto** con varios proveedores disponibles: si uno desaparece, cambias de servidor sin perder tus datos ni tu app. Git es el ejemplo del libro: puedes sincronizar con GitHub, GitLab o cualquier otro alojamiento, aunque Git no ofrece colaboración en tiempo real. El término *sync engine* es antiguo como idea, pero ha ganado atención recientemente.

## Guardado localmente no significa sincronizado

Esta distinción no aparece desarrollada en el libro, pero es la fuente de muchos errores de diseño. Cuando el técnico pulsa «Guardar», pueden haber ocurrido cosas muy distintas:

| Estado | Qué garantiza | Qué **no** garantiza |
|---|---|---|
| Aplicado en la interfaz | El usuario ve su cambio | Que sobreviva a cerrar la app |
| Persistido localmente según el contrato duradero de la base del dispositivo | Sobrevive a un reinicio dentro de ese contrato | Que exista fuera de ella |
| Enviado | Salió por la red | Que el servidor lo haya aceptado |
| Aceptado por el servidor | Una copia vive fuera del dispositivo | Que los colaboradores ya lo vean, ni que la fusión lo conserve intacto |

La consecuencia práctica: la interfaz debería distinguir «guardado en este dispositivo» de «sincronizado». Y si el servidor puede **rechazar** un cambio (por permisos o validación), la app necesita una forma de deshacerlo o marcarlo, porque el usuario ya lo vio aplicado.

## Por qué un sync engine resulta atractivo

La forma dominante de construir apps web guarda muy poco estado en el cliente y pide cada dato al servidor cuando lo necesita. Con un sync engine el cliente conserva estado persistente y **la comunicación con el servidor pasa a un proceso de fondo**. El libro enumera cuatro ventajas:

- **Respuesta inmediata.** Leer datos locales evita esperar a la red. Algunas apps aspiran a responder en el siguiente fotograma: a 60 Hz eso deja 1000 / 60 ≈ 16,7 ms. Una sola ida y vuelta de 80 ms equivale a casi cinco fotogramas perdidos.
- **Trabajo sin conexión sin «modo offline».** Estar desconectado se trata igual que tener una red muy lenta. No hay que escribir ni probar una segunda ruta de código.
- **Modelo de programación más simple.** Cada llamada a un servicio exige manejar errores: *timeouts*, respuestas perdidas, reintentos (ver [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/05 Codificación y evolución/05 Bases de datos APIs y RPC|RPC y timeouts]]). Leer y escribir en la base local casi nunca falla, así que el código de la interfaz se vuelve más declarativo: describe qué mostrar, no cómo recuperarse de cada fallo.
- **Actualizaciones en vivo.** Para mostrar ediciones ajenas en tiempo real hay que recibir notificaciones y refrescar la interfaz eficientemente. Un sync engine combinado con **programación reactiva** (la interfaz se suscribe a los datos locales y se vuelve a dibujar cuando cambian) resuelve esto de forma natural.

## Cuándo no encaja

Un sync engine funciona mejor si **todos los datos que el usuario podría necesitar se descargan por adelantado**. Eso está bien para los documentos que una persona ha creado, porque una persona no genera tantos datos. No tiene sentido para el catálogo completo de una tienda en línea. En el ejemplo de inspecciones, la tableta descargaría solo las subestaciones asignadas al técnico esa semana, no el historial de toda la empresa.

Hay otros límites que el libro deja para capítulos posteriores y conviene tener presentes (elaboración propia): reglas que necesitan una autoridad única, como no vender más stock del que existe, no se pueden decidir libremente en varias copias desconectadas sin coordinación o derechos reservados de antemano; los datos locales deben protegerse si el dispositivo se pierde; y el esquema de la base local evoluciona con versiones viejas de la app todavía instaladas, lo que reabre los problemas de compatibilidad del capítulo 5.

## Historia y ecosistema

Lotus Notes fue pionero en los años ochenta, sin usar el término; la sincronización específica de calendarios también existe desde hace mucho. La edición describe sync engines de propósito general. Sus ejemplos corresponden al libro: algunos dependen de un **backend propietario** (Google Firestore, Realm, Ditto); otros tienen **backend de código abierto** y por eso sirven para software local-first (PouchDB/CouchDB, Automerge, Yjs). Los videojuegos multijugador tienen un problema parecido (responder al jugador local ya y reconciliar después con los demás) y lo llaman *netcode*, pero sus técnicas son muy específicas de los juegos y el libro no las trata.

> [!question]- Una app de chat solo deja escribir con conexión, pero muestra tu mensaje antes de que el servidor lo acepte. ¿Es multilíder?
> Plantea el problema de réplicas de edición que el libro trata como multilíder: tu pestaña muestra un cambio local antes de conocer cambios ajenos. Eso no basta para concluir que la base del servidor acepte escrituras mediante varios líderes. El protocolo todavía debe decidir si conserva, fusiona o rechaza el cambio provisional.

> [!question]- ¿Por qué la estrategia de «enviar siempre al mismo líder» no sirve para un sync engine?
> Porque evitar conflictos así exige que el dispositivo contacte a ese líder antes de escribir. Un dispositivo desconectado acepta la escritura igualmente, así que los conflictos pueden aparecer y hay que resolverlos al sincronizar.

> [!question]- ¿Qué diferencia a local-first de offline-first?
> Offline-first solo exige seguir editando sin conexión. Local-first añade que la app siga funcionando aunque su fabricante apague sus servidores, lo que requiere un protocolo de sincronización abierto con varios proveedores posibles.

> [!question]- ¿Sería razonable un sync engine para el inventario de un almacén con 2 millones de productos consultado desde móviles?
> Para el catálogo completo, no: el enfoque presupone descargar por adelantado todo lo que el usuario pueda necesitar. Podría usarse para el subconjunto que un operario gestiona, y aun así decisiones como reservar la última unidad necesitan coordinación o una asignación previa de derechos que impida venderla dos veces.

## Referencias

PDF 24–26 · impresas 220–222 · sin figuras propias de la sección. Enlaces: [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/06 Replicación.pdf#page=24|PDF 24 · impresa 220]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/06 Replicación.pdf#page=25|PDF 25 · impresa 221]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/06 Replicación.pdf#page=26|PDF 26 · impresa 222]]. La tabla de estados de guardado, el ejemplo de inspecciones y los límites de autoridad y seguridad son elaboración propia.

---

**Anterior:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/07 Multilíder regiones topologías y orden causal|Multilíder, regiones, topologías y orden causal]] · **Índice:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/00 Índice|Replicación]] · **Siguiente:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/09 Conflictos LWW siblings y reglas del dominio|Conflictos, LWW, siblings y reglas del dominio]]
