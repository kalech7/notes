---
title: "Capítulo 1 · Introducción · Responsabilidades del arquitecto"
created: 2026-09-25
tags:
  - lecturas/software-architecture
capitulo: 1
orden: 4
---

# Responsabilidades del arquitecto

[Inicio del libro](../00%20Empieza%20aqu%C3%AD.md) → [Capítulo 1 · Introducción](00%20%C3%8Dndice.md) → Nota 4 de 6

**Objetivo:** Reconocer las ocho expectativas del rol.

> [!info] Contexto del capítulo
> Segunda edición. PedidoClaro y sus cifras son ejemplos didácticos propios; Silicon Sandwiches es la kata del libro. El [índice del capítulo](00%20%C3%8Dndice.md) conserva el alcance y las referencias generales.

> [!info] Recuerda antes
> Una decisión arquitectónica siempre sacrifica algo y solo tiene sentido dentro de su contexto. El trabajo del arquitecto no termina al elegir: debe comunicar, comprobar consecuencias y revisar la elección cuando cambian los hechos.

## 4. Ocho expectativas del arquitecto

El libro enumera ocho expectativas, independientemente del cargo o nivel de responsabilidad. Conviene estudiarlas como actividades conectadas: decidir sin comunicar, verificar o comprender el negocio deja incompleta la función. **Lista original: PDF 8, impresa 8.**

### 1. Tomar decisiones que guíen

El arquitecto define decisiones y principios para orientar elecciones tecnológicas. El énfasis del libro está en **guiar**: establece criterios que permiten al equipo elegir. También reconoce situaciones en las que seleccionar una tecnología concreta es necesario para preservar rendimiento, disponibilidad u otra característica. **Fuente: PDF 8–9, impresas 8–9.**

En PedidoClaro, «los clientes de la interfaz no accederán directamente a la base de datos» comunica una restricción arquitectónica. Elegir una biblioteca visual normalmente requiere otro nivel de detalle. La frontera depende del contexto: una biblioteca puede adquirir importancia arquitectónica si determina una capacidad crítica. El error es clasificar por el nombre de la tecnología en lugar de por su efecto.

### 2. Analizar continuamente la arquitectura

La vitalidad arquitectónica consiste en revisar si la solución sigue siendo viable ante cambios técnicos y del negocio. El libro advierte sobre la degradación estructural cuando modificaciones locales deterioran características necesarias. Incluye pruebas y liberaciones dentro de esa evaluación. **Fuente: PDF 9, impresa 9.**

Si PedidoClaro programa una promoción en dos horas, pero necesita diez días para validarla y desplegarla, la rapidez de programación no representa la agilidad del sistema completo. Medir solo el tramo más cómodo esconde el cuello de botella que impide responder al negocio.

### 3. Mantenerse al día

Conocer tendencias ayuda porque las decisiones arquitectónicas suelen durar y resultar costosas de cambiar. El libro menciona almacenamiento y despliegue en la nube e IA generativa como ejemplos de cambios relevantes en su contexto. **Fuente: PDF 9, impresa 9.**

Estar informado no significa adoptar cada novedad. Como práctica propia para PedidoClaro, una evaluación breve puede preguntar qué problema resuelve una herramienta, cuánto cuesta introducirla y qué evidencia justificaría cambiar. Aprender aumenta las opciones; adoptar añade obligaciones.

### 4. Verificar el cumplimiento de decisiones

Aquí **compliance** significa comprobar que los equipos siguen las decisiones y principios documentados y comunicados. No equivale automáticamente a cumplimiento legal o regulatorio. El ejemplo del libro muestra cómo el acceso directo desde presentación puede frustrar el aislamiento de cambios de base de datos. También anticipa verificaciones automatizadas mediante funciones de aptitud arquitectónica. **Fuente: PDF 11, impresa 10.**

**Ampliación propia:** una comprobación de dependencias podría detectar importaciones del acceso a datos desde la interfaz. Esa prueba observaría una regla específica, no certificaría toda la arquitectura. Si la regla empieza a causar problemas reales, corresponde revisar su justificación, además de detectar incumplimientos.

### 5. Comprender tecnologías diversas

El libro favorece amplitud técnica: conocer opciones y sus ventajas e inconvenientes, sin exigir ser especialista en todas. La diversidad de entornos también obliga a entender cómo integrar sistemas construidos con tecnologías distintas. **Fuente: PDF 11, impresa 10.**

Conocer una sola herramienta de mensajería puede llevar a proponerla para cualquier comunicación. Reconocer varias alternativas permite preguntar si PedidoClaro necesita procesamiento inmediato, entrega posterior, confirmaciones o recuperación. La amplitud resulta útil cuando mejora esas preguntas; memorizar nombres comerciales no basta.

### 6. Conocer el dominio del negocio

Comprender problemas, objetivos y requisitos permite diseñar soluciones pertinentes y comunicarse con quienes operan el negocio. **Fuente: PDF 10, impresa 11.**

En nuestro ejemplo, «pedido recibido», «pagado» y «listo para preparar» podrían ser estados diferentes. Si se confunden, cocina puede preparar compras cuyo cobro falló. Conocer esas distinciones es tan necesario como dominar la base de datos: determinan qué transiciones y garantías necesita el sistema.

### 7. Liderar y desarrollar habilidades interpersonales

Trabajo en equipo, facilitación, liderazgo y comunicación forman parte del papel del arquitecto. El libro subraya que una orientación técnica valiosa necesita acompañamiento para convertirse en implementación. **Fuente: PDF 10, impresa 11.**

En PedidoClaro, facilitar una conversación entre caja, cocina y desarrollo permite descubrir significados contradictorios de «confirmado». Liderar no consiste únicamente en comunicar la respuesta final; también implica hacer visibles desacuerdos y ayudar a construir criterios compartidos.

### 8. Comprender y navegar la política organizativa

Las decisiones amplias redistribuyen costos y autonomía. El libro ilustra el problema restringiendo el acceso a una base de datos de CRM: mejora el control para su propietario, pero obliga a otros equipos a cambiar integraciones y asumir esfuerzo. Eso exige negociación. **Fuente: PDF 12, impresa 12.**

En PedidoClaro, limitar consultas directas puede beneficiar al equipo de Pedidos y complicar los informes de Finanzas. La objeción no demuestra ignorancia técnica: quizá identifica un costo real. Negociar una interfaz de consulta y una transición financiada hace viable la decisión. La política trata también de prioridades, recursos y responsabilidad, no solo de conflictos personales.

---

**Anterior:** [Leyes y compensaciones](03%20Leyes%20y%20compensaciones.md) · **Índice:** [Volver al capítulo](00%20%C3%8Dndice.md) · **Siguiente:** [Principios decisiones y ADR](05%20Principios%20decisiones%20y%20ADR.md)
