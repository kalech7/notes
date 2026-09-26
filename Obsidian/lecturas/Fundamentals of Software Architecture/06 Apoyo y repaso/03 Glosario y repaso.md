---
title: "Glosario y repaso · Fundamentals of Software Architecture 2.ª edición"
created: 2026-09-25
tags:
  - lecturas/software-architecture
  - repaso
---

# Glosario y repaso

[Inicio del libro](../00%20Empieza%20aqu%C3%AD.md) → [Apoyo y repaso](00%20%C3%8Dndice.md)

Las definiciones son breves recordatorios de las explicaciones desarrolladas en los capítulos. Algunos términos —como RTO, RPO e idempotencia— aparecen aquí como ampliaciones didácticas.

| Término | Significado y diferencia importante | Capítulo |
|---|---|---|
| Arquitectura | Organización y decisiones que relacionan comportamiento, capacidades y restricciones | 1 |
| Componente lógico | Responsabilidad agrupada; no implica servidor propio | 1, 3 |
| Estilo arquitectónico | Organización de partida con propiedades y costos característicos | 1 |
| Decisión arquitectónica | Elección contextual que impone o guía restricciones relevantes | 1 |
| Principio | Orientación general que ayuda a tomar decisiones | 1 |
| Trade-off | Compensación: lo que ganas y lo que pagas al elegir | 1, 2 |
| ADR | Registro de contexto, elección, alternativas y consecuencias | 1, laboratorio |
| Vitalidad arquitectónica | Adecuación continua de la arquitectura al contexto que cambia | 1 |
| Amplitud técnica | Conocer opciones, usos y límites suficientes para compararlas | 2 |
| Profundidad técnica | Capacidad detallada para implementar y diagnosticar un área | 2 |
| Frozen Caveman | Convertir una experiencia pasada en preocupación rígida para todo contexto | 2 |
| Radar tecnológico | Registro de categorías y posturas de evaluación; no ranking universal | 2 |
| POC | Experimento para resolver una incertidumbre; no garantía de preparación para producción | 2 |
| Bottleneck Trap | El arquitecto monopoliza una pieza crítica que no puede atender a tiempo | 2 |
| Cola de trabajo | Entregas repartidas entre consumidores que comparten una tarea | 2 |
| Publicación/suscripción | Comunicación de un evento a intereses suscritos independientes | 2 |
| Contrato | Acuerdo sobre forma, significado y comportamiento observable | 2, 3 |
| Modularidad | Agrupar y encapsular responsabilidades con relaciones controladas | 3 |
| Granularidad | Tamaño o alcance de las unidades resultantes | 3 |
| Cohesión | Qué tan relacionadas están las partes que permanecen juntas | 3 |
| Acoplamiento | Dependencia que vincula elementos y puede propagar cambios | 3 |
| LCOM | Familia de métricas de falta de cohesión; especifica siempre la variante | 3 |
| Ca | Acoplamiento entrante: elementos externos que dependen de la unidad | 3 |
| Ce | Acoplamiento saliente: elementos externos de los que depende la unidad | 3 |
| A | Proporción de tipos abstractos dentro del conjunto contado | 3 |
| I | Ce / (Ca + Ce); no es probabilidad de fallo | 3 |
| D | Distancia normalizada a A + I = 1; requiere interpretar contexto | 3 |
| Connascencia | Acuerdo entre partes que deben cambiar coordinadamente para conservar corrección | 3 |
| Fuerza | Dificultad relativa de detectar y transformar un tipo de connascencia | 3 |
| Localidad | Proximidad de los participantes; determina dónde se concentra el acuerdo | 3 |
| Grado | Número de participantes afectados por el acuerdo | 3 |
| Característica arquitectónica | Capacidad importante para el éxito con influencia en la estructura | 4 |
| Implícita / explícita | Inferida del contexto / expresada en requisitos; ambas deben concretarse | 4, 5 |
| Latencia | Tiempo de una operación definido entre dos puntos de observación | 4 |
| Throughput | Trabajo completado por unidad de tiempo | 4 |
| p95 | Valor bajo el que queda aproximadamente el 95 % de observaciones según la convención usada | 4 |
| Escalabilidad | Capacidad de sostener objetivos al aumentar carga y recursos | 4, 5 |
| Elasticidad | Adaptación de recursos a la demanda, incluyendo reducción | 4, 5 |
| Disponibilidad | Accesibilidad operativa según criterio, período y alcance acordados | 4 |
| Fiabilidad | Funcionamiento correcto bajo condiciones y período definidos | 4 |
| Tolerancia a fallos | Continuidad de funciones acordadas pese a ciertos fallos | 4 |
| Recuperabilidad | Capacidad de restaurar servicio y datos después de un fallo | 4 |
| RTO | Objetivo de tiempo para recuperar el servicio | 4 |
| RPO | Objetivo que limita la pérdida temporal de datos | 4 |
| Autenticación | Comprobar identidad declarada | 4 |
| Autorización | Decidir qué puede hacer una identidad en un contexto | 4 |
| Lenguaje ubicuo | Significados compartidos entre negocio y equipo técnico | 4 |
| Característica compuesta | Capacidad que depende de varias capacidades más específicas | 5 |
| Kata | Ejercicio acotado para practicar decisiones y discutir compensaciones | 5 |
| Característica conductora | Prioridad que orienta decisiones estructurales | 5 |
| Idempotencia | Repetir la misma operación lógica no multiplica su efecto esperado | Laboratorio |

## Conexión con tu lectura de datos

En [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/00 Empieza aquí|DDIA: almacenamiento y evolución]] estudias cómo se guardan y representan datos. Aquí estudias por qué escoger una estructura que utilice esos mecanismos. La conexión no es «una arquitectura exige una base concreta»: una necesidad de búsqueda puede motivar índices; una necesidad de evolución independiente exige compatibilidad de contratos; una decisión de separar datos obliga a pensar cómo se coordinan estados.

## Repaso por recuperación activa

Antes de consultar definiciones, intenta explicar estas cinco situaciones:

1. Un servicio cambia y obliga a desplegar otros siete. ¿Qué dependencias investigarías? ¿Por qué ocho despliegues no demuestran modularidad?
2. El promedio de respuesta mejora pero aumentan reclamaciones. ¿Qué distribución, operación y población de usuarios revisarías?
3. Un equipo pide que toda característica tenga prioridad máxima. ¿Cómo convertirías la conversación en escenarios y tres prioridades compartidas?
4. Una métrica mejora después de añadir interfaces que nadie utiliza. ¿Qué evidencia mostraría que el cambio añadió valor?
5. Un proveedor auxiliar deja de responder. ¿Cuál es el comportamiento degradado aceptable y cómo lo comprobarías?

Una respuesta completa identifica mecanismo, costo, supuesto y evidencia. Las preguntas resueltas al final de cada capítulo permiten comprobar los fundamentos antes de intentar el laboratorio.

---

[← Índice de este bloque](00%20%C3%8Dndice.md)
