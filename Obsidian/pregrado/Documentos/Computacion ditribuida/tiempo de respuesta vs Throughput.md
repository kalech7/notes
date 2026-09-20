## Tiempo de Respuesta (Response Time / Latency)
Se refiere al tiempo total que tarda un sistema en responder a una solicitud específica, desde el momento en que el usuario o cliente envía dicha solicitud hasta el momento en que recibe la respuesta completa.

- **Medida en:** Generalmente se expresa en milisegundos (ms) o segundos (s).
- **Importancia:** Es un factor crucial para la experiencia del usuario. Un tiempo de respuesta bajo es fundamental para mantener aplicaciones en tiempo real y sistemas interactivos fluidos, como videojuegos en línea, aplicaciones web y servicios financieros de alta frecuencia.

## Throughput (Tasa de Rendimiento)
Se refiere a la cantidad total de trabajo que un sistema puede procesar y completar en un período de tiempo determinado.

- **Medida en:** Generalmente se expresa en unidades por segundo, como transacciones por segundo (TPS), solicitudes por segundo (RPS) o megabits por segundo (Mbps).
- **Importancia:** Es una medida de la capacidad global del sistema. Un throughput alto significa que el sistema puede manejar simultáneamente una gran cantidad de trabajo o solicitudes. Esto es esencial para sistemas sometidos a alta carga, como servidores web concurridos, bases de datos masivas y redes de comunicación troncales.

> [!info] Explicación: Analogía del Tráfico Vehicular
> - **Tiempo de Respuesta:** Es la velocidad a la que un auto individual viaja del punto A al punto B. (Qué tan rápido vas).
> - **Throughput:** Es la cantidad total de autos que pueden pasar por la autopista en una hora. (Qué tan ancha es la carretera).

## Diferencias Clave

- **Enfoque Principal:**
    - **Tiempo de Respuesta:** Se centra en la velocidad individual con la que se completa una sola solicitud de principio a fin.
    - **Throughput:** Se enfoca en el volumen y la capacidad agregada, es decir, cuánto trabajo total el sistema puede procesar a la vez.

- **Relación y Compromisos (Trade-offs):**
    - **Tiempo de respuesta bajo NO siempre implica un throughput alto:** Un sistema puede ser muy rápido para responder a un usuario aislado, pero si se conectan varios usuarios al mismo tiempo, el sistema podría colapsar si carece de capacidad.
    - **Throughput alto NO siempre implica un tiempo de respuesta bajo:** Un sistema puede procesar 10,000 solicitudes a la vez empleando técnicas por lotes (batching), pero cada una de esas solicitudes podría tardar varios segundos o minutos en completarse para el usuario individual.

- **Aplicación Ideal:**
    - **Optimizar Tiempo de Respuesta:** Importante para la usabilidad interactiva y sistemas críticos donde el retraso es inaceptable (ej. un freno ABS o una videollamada).
    - **Optimizar Throughput:** Importante para la escalabilidad, eficiencia del servidor y procesamiento de datos en segundo plano (ej. un proceso nocturno que analiza millones de transacciones de un banco).

## Notas relacionadas
- [[rendimineto de htpp]]
- [[SLA]]
- [[servidores]]
- [[computacion distribuida]]
