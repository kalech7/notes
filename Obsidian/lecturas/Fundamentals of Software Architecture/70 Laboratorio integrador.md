---
title: "Laboratorio integrador · PedidoClaro"
created: 2026-09-25
tags:
  - lecturas/software-architecture
  - practica
---

# Laboratorio integrador: de una necesidad a una arquitectura razonada

[[Obsidian/lecturas/Fundamentals of Software Architecture/00 Empieza aquí|← Índice]]

Este ejercicio es **elaboración propia**, no una kata adicional del libro. Integra lo estudiado en los cinco capítulos. Puedes hacerlo en papel o duplicar esta nota y responder antes de desplegar las soluciones.

## Situación y supuestos

PedidoClaro tiene 12 locales, un equipo de cuatro desarrolladores y un único equipo de operación compartido. Ofrece pedidos por web, promociones nacionales y descuentos locales. Durante una campaña espera 100 solicitudes/s durante quince minutos. La operación que confirma pedidos debe cumplir un p95 inferior a dos segundos bajo esa carga. Cada local dispone de un límite físico de preparación que debe respetarse al ofrecer horarios.

El proveedor de mapas puede fallar sin que desaparezcan las direcciones de los locales. Los pagos se realizan mediante un proveedor externo. Las promociones cambian semanalmente; los nuevos descuentos no deben alterar los pedidos ya aceptados. Todo esto es inventado para practicar. Los otros capítulos usan cifras distintas en ejemplos independientes; no son una especificación única de esta empresa.

## 1. Separar comportamiento, capacidad y restricción

Clasifica cada enunciado y explica por qué:

| Enunciado | Tu clasificación |
|---|---|
| El usuario elige un local y una franja de recogida | |
| p95 de confirmación inferior a dos segundos con 100 solicitudes/s | |
| Equipo de cuatro desarrolladores | |
| Los pedidos aceptados conservan el precio acordado | |
| Mapas falla sin interrumpir aceptación de pedidos | |
| Las promociones cambian semanalmente | |

> [!success]- Una respuesta razonada
> Elegir local y franja es comportamiento. El umbral de respuesta bajo carga es una capacidad medible. El tamaño del equipo es una restricción organizativa. Conservar precio es una regla de dominio y de integridad cuyo cumplimiento puede requerir decisiones estructurales. Tolerar el fallo de mapas describe aislamiento y continuidad. Cambiar promociones semanalmente es una necesidad comercial que conviene traducir a modificabilidad, pruebas y despliegue; no impone automáticamente microservicios.

## 2. Elegir límites antes de elegir despliegues

Propón responsabilidades para Catálogo, Promociones, Pedidos, Pagos y Preparación. Indica qué módulo puede modificar el estado de un pedido, quién aplica una promoción y quién registra que se recibió una confirmación de pago.

> [!success]- Solución posible
> Pedidos puede poseer el ciclo de vida del pedido y guardar el precio aceptado. Promociones calcula una propuesta según reglas y versión; Pedidos conserva el resultado necesario para honrar el acuerdo. Pagos integra el proveedor y comunica estados verificados; no debe permitir que cualquier respuesta del navegador se trate como prueba de cobro. Preparación controla la capacidad y avance en cocina. Son límites lógicos: podrían vivir dentro de un mismo despliegue. El contrato entre ellos debe aclarar quién decide y qué datos se conservan, no solamente qué endpoint existe.

## 3. Comparar dos estructuras

Compara una aplicación modular con cinco servicios separados. Utiliza necesidades concretas, no una puntuación universal.

| Dimensión | Aplicación modular | Servicios separados |
|---|---|---|
| Publicación | Una unidad principal; simplifica coordinación inicial | Puede ser independiente si contratos y datos lo permiten |
| Operación | Menos unidades que mantener | Más comunicación, observación y recuperación entre unidades |
| Escalado | Puede replicarse completa; gasto en partes no saturadas | Permite escalado selectivo si las dependencias lo permiten |
| Cambio de promociones | Frontera interna comprobable | Frontera de contrato remoto y compatibilidad |
| Consistencia | Transacciones locales donde el modelo lo permite | Requiere definir coordinación y estados intermedios |

> [!success]- Decisión provisional defendible
> Con el equipo supuesto, exploraría primero una aplicación modular y comprobaría su capacidad bajo carga. La razón es reducir operación inicial mientras se protegen límites que podrían permitir separar una responsabilidad más adelante. Cambiaría esta decisión si las mediciones mostraran un cuello de botella separable o si equipos y frecuencias de despliegue justificaran independencia. Tampoco descartaría la distribución solo por tamaño de equipo: habría que considerar capacidades gestionadas, experiencia y restricciones concretas.

## 4. Calcular y cuestionar una métrica

El módulo Pedidos tiene 2 tipos abstractos, 8 concretos, 3 módulos que dependen de él y 2 dependencias hacia otros módulos. Calcula A, I y D. Luego explica qué no sabes todavía.

> [!success]- Cálculo
> `A = 2 / 10 = 0,20`; `I = 2 / (3 + 2) = 0,40`; `D = |0,20 + 0,40 − 1| = 0,40`. Falta saber si esas abstracciones representan buenas responsabilidades, si hay ciclos, qué contratos cambian, qué dependencias dinámicas no se midieron y cómo afecta un cambio al negocio. D no es un porcentaje de mala arquitectura.

## 5. Proteger un pedido ante un fallo

Un cliente pulsa confirmar, el servidor guarda el pedido y la respuesta se pierde. El cliente reintenta. ¿Qué impide crear dos pedidos? ¿Qué ocurre si el pago queda en estado desconocido?

> [!success]- Ampliación técnica para integrar las ideas
> Una clave idempotente ligada a la operación y registrada con su resultado puede permitir reconocer el reintento. La comprobación y el registro deben evitar una carrera entre peticiones; consultar primero y escribir después sin control no basta. Un estado de pago desconocido requiere consulta o conciliación con el proveedor, no asumir automáticamente éxito o fallo. Esta ampliación explica por qué los contratos y los estados importan al evaluar acoplamiento dinámico; no desarrolla todas las garantías de un sistema de pagos.

## 6. Convertir la decisión en evidencia

Diseña pruebas para confirmar o refutar las siguientes hipótesis:

| Hipótesis | Evidencia relevante |
|---|---|
| Soportamos la campaña | Carga definida, datos representativos, p95 y errores por operación durante quince minutos |
| Mapas no derriba pedidos | Fallos y lentitud del proveedor; comportamiento y mensajes visibles al usuario |
| No duplicamos pedidos al reintentar | Pérdida de respuesta y peticiones concurrentes con la misma clave |
| Podemos restaurar | Recuperación real desde copia y registros; tiempo, integridad y punto de datos recuperado |
| Promociones conserva su frontera | Pruebas de reglas y comprobación de dependencias entre módulos |

El volumen de solicitudes no equivale automáticamente a pedidos ni a usuarios simultáneos. Antes de la prueba, define qué fracción consulta, confirma o reintenta, y durante cuánto tiempo permanece cada sesión.

## 7. Registrar un ADR breve

Un **Architecture Decision Record** conserva una decisión y su razón. Esta plantilla es una ampliación didáctica; el capítulo del libro dedicado a ADR no está incluido en tus escaneos.

| Campo | Ejemplo de contenido |
|---|---|
| Título | Separar responsabilidad de mapas del éxito de la compra |
| Estado | Propuesta para validar |
| Contexto | Mapas puede fallar; el pedido y la dirección siguen siendo útiles |
| Decisión | La navegación detallada se obtiene de forma separada y con espera limitada |
| Alternativa | Bloquear la compra hasta recibir mapas |
| Consecuencia favorable | El proveedor auxiliar no impide aceptar pedidos |
| Costo aceptado | Puede ofrecerse información de navegación menos completa |
| Verificación | Inyectar errores y lentitud; observar compras y mensajes al usuario |
| Revisión | Si el negocio exige estimaciones de entrega cuyo cálculo depende de mapas |

Evalúa tu trabajo preguntando: ¿cada prioridad tiene una razón de negocio?, ¿cada decisión reconoce un costo?, ¿cada promesa tiene evidencia?, ¿separaste hechos, supuestos y dudas? La calidad está en esa cadena de razonamiento, no en que tu dibujo coincida con una solución única.
