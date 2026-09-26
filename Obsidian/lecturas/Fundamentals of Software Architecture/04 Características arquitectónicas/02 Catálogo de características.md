---
title: "Capítulo 4 · Características arquitectónicas · Catálogo de características"
created: 2026-09-25
tags:
  - lecturas/software-architecture
capitulo: 4
orden: 2
---

# Catálogo de características

[Inicio del libro](../00%20Empieza%20aqu%C3%AD.md) → [Capítulo 4 · Características arquitectónicas](00%20%C3%8Dndice.md) → Nota 2 de 7

**Objetivo:** Reconocer las cuatro familias del catálogo.

> [!info] Contexto del capítulo
> Segunda edición. PedidoClaro y sus cifras son ejemplos didácticos propios; Silicon Sandwiches es la kata del libro. El [índice del capítulo](00%20%C3%8Dndice.md) conserva el alcance y las referencias generales.

## 2. Catálogo completo de las cuatro tablas

Las tablas siguientes incluyen **todas las entradas de las tablas 4-1 a 4-4**. Las explicaciones desarrollan su significado y los ejemplos son propios. Las categorías ayudan a conversar; no son compartimentos exclusivos ni una lista de todo lo que existe.

### Operacionales: qué ocurre mientras funciona

**Fuente: tabla 4-1, PDF p. 5; impresa 59.**

| Entrada del libro | Significado y ejemplo en PedidoClaro |
|---|---|
| Disponibilidad (*availability*) | Estar operativo y accesible cuando se necesita. La compra debe funcionar durante el horario acordado; un proceso vivo que rechaza pedidos no basta. |
| Continuidad (*continuity*) | Capacidad frente a desastres. Si se pierde un centro de cómputo, existe una estrategia para sostener o restablecer la operación. |
| Rendimiento (*performance*) | Comportamiento temporal y bajo carga. Evaluar respuestas, picos y operaciones frecuentes; una prueba con un usuario no representa el almuerzo. |
| Recuperabilidad (*recoverability*) | Recuperar servicio y estado tras un fallo. Restaurar pedidos desde copias verificadas y medir cuánto demora. |
| Fiabilidad / seguridad frente a daños (*reliability/safety*) | El libro agrupa ambas y menciona criticidad, vidas y pérdidas. Aquí se distinguen: fiabilidad es funcionar correctamente durante un intervalo; *safety* trata de evitar daños inaceptables. Mostrar correctamente alérgenos ilustra esta última. |
| Robustez (*robustness*) | Manejar errores y condiciones límite sin comportamiento descontrolado. Una conexión interrumpida produce un resultado claro y permite reintentar sin duplicar compras. |
| Escalabilidad (*scalability*) | Sostener la operación al aumentar usuarios o solicitudes. Añadir capacidad debe permitir atender más pedidos dentro de objetivos acordados. |

Continuidad es la capacidad global de afrontar la interrupción; recuperabilidad se concentra en volver a un estado operativo. Robustez incluye entradas inválidas y condiciones extremas; no se limita a duplicar servidores. *Safety* tampoco equivale a *security*: prevenir daños y proteger frente a accesos o acciones indebidas son preocupaciones relacionadas, pero distintas.

### Estructurales: qué permite la organización interna

**Fuente: tabla 4-2, PDF p. 6; impresa 60.**

| Entrada del libro | Significado y ejemplo propio |
|---|---|
| Configurabilidad (*configurability*) | Facilitar que usuarios finales cambien opciones mediante interfaces: modificar horarios sin editar código. |
| Extensibilidad (*extensibility*) | Incorporar funcionalidad adicional: introducir nuevos tipos de promociones mediante límites preparados para esa variación. |
| Instalabilidad (*installability*) | Instalar en las plataformas necesarias con dificultad controlada: preparar una nueva caja sin pasos manuales ambiguos. |
| Aprovechamiento / reutilización (*leverageability/reuse*) | Usar componentes comunes en distintos productos: compartir un cálculo monetario entre tienda y administración. |
| Localización (*localization*) | Adaptar idiomas de pantallas y campos. En el ejemplo, mostrar etiquetas y formatos locales; traducir texto no resuelve por sí solo todos los formatos. |
| Mantenibilidad (*maintainability*) | Aplicar correcciones y mejoras con esfuerzo y riesgo razonables: ajustar impuestos sin romper pagos. |
| Portabilidad (*portability*) | Funcionar en distintas plataformas: cambiar de motor de datos sin rehacer toda la aplicación. |
| Actualizabilidad (*upgradeability*) | Pasar a nuevas versiones de servidores y clientes con facilidad: actualizar cajas y conservar compatibilidad durante la transición. |

Extender agrega posibilidades; mantener incluye corregir y adaptar. Instalar establece una versión en un entorno; actualizar transforma una instalación existente y puede requerir migraciones. Reutilizar tampoco es gratis: una biblioteca compartida exige coordinar contratos y versiones entre consumidores.

### Nube: capacidades ofrecidas por el proveedor

**Fuente: tabla 4-3, PDF p. 6; impresa 60.**

| Entrada del libro | Significado y ejemplo propio |
|---|---|
| Escalabilidad bajo demanda (*on-demand scalability*) | Obtener recursos dinámicamente al aumentar la demanda: ampliar instancias para más sucursales. |
| Elasticidad bajo demanda (*on-demand elasticity*) | Ajustarse a fluctuaciones: aumentar capacidad durante el almuerzo y reducirla después. |
| Disponibilidad por zonas (*zone-based availability*) | Separar recursos entre zonas para reducir el impacto de ciertos fallos: mantener instancias en dos zonas. |
| Privacidad y seguridad por regiones (*region-based privacy and security*) | Considerar dónde pueden residir los datos y qué restricciones regionales afectan al proveedor: elegir ubicación de datos y copias según obligaciones verificadas. |

La capacidad del proveedor no equivale a la propiedad del sistema. Dos zonas pueden depender de una base de datos sin recuperación. Una región tampoco demuestra cumplimiento: intervienen copias, registros, accesos y transferencias. Una obligación concreta exige comprobar jurisdicción, contratos y criterio profesional aplicable.

### Transversales: atraviesan componentes y responsabilidades

**Fuente: tabla 4-4, PDF p. 7; impresa 61.**

| Entrada del libro | Significado y ejemplo propio |
|---|---|
| Accesibilidad (*accessibility*) | Permitir el uso por personas con diversas capacidades: navegación por teclado y mensajes que no dependan solo del color. |
| Archivabilidad (*archivability*) | Archivar o eliminar datos tras períodos definidos: separar historial operativo y archivo según una política acordada. |
| Autenticación (*authentication*) | Comprobar identidad: verificar quién inicia sesión como encargado. |
| Autorización (*authorization*) | Limitar acciones y datos por permisos: un encargado solo modifica su sucursal. |
| Legal (*legal*) | Restricciones normativas y derechos relevantes para construcción, despliegue y datos. El libro menciona GDPR y Sarbanes-Oxley como ejemplos; no se presume su aplicabilidad a PedidoClaro. |
| Privacidad (*privacy*) | Restringir exposición de información; el libro destaca ocultarla incluso a personal interno privilegiado. Ejemplo: limitar el acceso a direcciones de clientes. |
| Seguridad (*security*) | Controles de protección, cifrado, comunicaciones y acceso. Ejemplo: proteger credenciales y verificar permisos en el servidor. |
| Soportabilidad (*supportability*) | Facilitar soporte y diagnóstico: correlacionar un pedido con sus errores sin revelar datos innecesarios. |
| Usabilidad / logro de objetivos (*usability/achievability*) | Permitir alcanzar objetivos con formación razonable: completar un pedido sin instrucciones externas. |

Autenticarse no concede todos los permisos. Cifrar no garantiza privacidad si demasiadas personas poseen acceso legítimo. Añadir registros mejora diagnóstico, pero registrar direcciones completas aumenta exposición: una decisión afecta varias características simultáneamente.

---

**Anterior:** [Comportamiento y capacidades](01%20Comportamiento%20y%20capacidades.md) · **Índice:** [Volver al capítulo](00%20%C3%8Dndice.md) · **Siguiente:** [Familias ISO y terminología](03%20Familias%20ISO%20y%20terminolog%C3%ADa.md)
