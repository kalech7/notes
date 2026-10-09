## Diagrama 1: Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/17 Observabilidad y versionado de prompts/01 S17 - Por qué una respuesta exitosa puede ser un fallo.md

```mermaid
flowchart LR
    Q[Consulta del usuario] --> E[Ejecución del agente]
    E --> R[Respuesta con HTTP 200]
    E --> T[Traza de los pasos]
    R --> V[Evaluación de la respuesta]
    T --> D[Diagnóstico de tiempo costo y errores]
    V --> M[Decisión de mejora]
    D --> M

```

## Diagrama 2: Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/17 Observabilidad y versionado de prompts/03 S17 - Tokens costos y atribución del gasto.md

```mermaid
flowchart TD
    A[Corrida cara] --> B[Localizar spans con llamadas al modelo]
    B --> C[Leer modelo tokens y tarifa]
    C --> D[Calcular costo de cada llamada]
    D --> E[Ordenar contribuciones]
    E --> F[Examinar entrada y repeticiones del mayor aporte]
    F --> G[Probar una mejora y reevaluar calidad]

```

## Diagrama 3: Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/17 Observabilidad y versionado de prompts/04 S17 - Latencia percentiles y diagnóstico de anomalías.md

```mermaid
flowchart TD
    A[Panel de corridas] --> B[Costo por corrida]
    A --> C[Latencia p50 p95 y máximo]
    A --> D[Calidad y errores]
    B --> E[Corrida 7 para investigar gasto]
    C --> F[Corrida 4 para investigar tiempo]
    E --> G[Spans y contexto de cada caso]
    F --> G
    D --> G

```

## Diagrama 4: Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/17 Observabilidad y versionado de prompts/05 S17 - Instrumentar el bucle y conservar los errores.md

```mermaid
flowchart TD
    A[Abrir span y tomar tiempo] --> B[Ejecutar operación]
    B --> C{Terminó bien}
    C -->|Sí| D[Guardar resultado permitido]
    C -->|No| E[Registrar error saneado]
    E --> F[Propagar excepción]
    D --> G[Finally cerrar duración y guardar span]
    F --> G

```

## Diagrama 5: Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/17 Observabilidad y versionado de prompts/07 S17 - Configuración privacidad y exportación de trazas.md

```mermaid
flowchart LR
    U[Usuario] --> A[Aplicación del agente]
    A --> M[Servidor del modelo]
    A --> X[Datos de observabilidad saneados]
    X --> L[Servidor Langfuse]
    L --> I[Interfaz y exportación]

```

## Diagrama 6: Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/17 Observabilidad y versionado de prompts/08 S17 - Versiones etiquetas evaluación y rollback de prompts.md

```mermaid
flowchart TD
    A[Registrar v2 y changelog] --> B[Ejecutar v1 y v2 sobre pruebas comparables]
    B --> C[Relacionar cada generation con su versión]
    C --> D[Comparar calidad costo latencia y errores]
    D --> E{Cumple los criterios}
    E -->|Sí| F[Mover production a v2]
    E -->|No| G[Conservar v1 y corregir candidata]
    F --> H[Monitorear comportamiento real]
    H --> I{Aparece una regresión}
    I -->|Sí| J[Rollback a versión conocida]
    I -->|No| K[Mantener y ampliar evidencia]

```

## Diagrama 7: Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/17 Observabilidad y versionado de prompts/09 S17 - Laboratorio resuelto sin API ni servicios externos.md

```mermaid
flowchart TD
    A[Abrir traza y span agente] --> B[Guardrail de entrada]
    B --> C{Caso bloqueado}
    C -->|Sí| D[Registrar bloqueo]
    C -->|No| E[Generation decidir con tokens ficticios]
    E --> F[Tool calendario]
    F --> G{Caso de error}
    G -->|Sí| H[Registrar error y propagar]
    G -->|No| I[Generation redactar con tokens ficticios]
    I --> J[Registrar salida saneada]
    D --> K[Cerrar span padre y traza]
    H --> K
    J --> K
    K --> L[Exportar JSONL saneado]

```

## Diagrama 8: Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/01 S18 - Guardrails y bordes de confianza.md

```mermaid
flowchart LR
    U["Pregunta"] --> E["Entrada: alcance y datos"]
    E --> R["Recuperar documentos permitidos"]
    R --> C["Contexto: permisos y evidencia"]
    C --> D{"¿Evidencia suficiente?"}
    D -->|Sí| M["Generar respuesta"]
    D -->|No| A["Abstención controlada"]
    M --> S["Salida: formato, citas y secretos"]
    S --> F["Respuesta permitida"]

```

## Diagrama 9: Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/02 S18 - Reglas patrones y normalización.md

```mermaid
flowchart LR
    A["Texto recibido"] --> N["Normalización para comparar"]
    P["Frases de referencia"] --> NP["La misma normalización"]
    N --> C["Comparación"]
    NP --> C
    C --> D{"¿Coincide una señal?"}
    D -->|Sí| B["Bloquear según política"]
    D -->|No| E["Continuar con otros controles"]

```

## Diagrama 10: Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/03 S18 - Datos personales y errores de redacción.md

```mermaid
flowchart LR
    Q["Ventas de tiendas 101 102 103"] --> P["Regex confunde lista y teléfono"]
    P --> T["Lista sustituida por marcador"]
    T --> L["El modelo recibe menos información"]
    L --> R["La respuesta puede perder utilidad"]

```

## Diagrama 11: Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/04 S18 - Trazas secretos y retención.md

```mermaid
flowchart TD
    A["Entrada original"] --> G{"¿Se permite continuar?"}
    G -->|Sí| C["Usar entrada redactada"]
    G -->|No| B["Construir respuesta bloqueada"]
    C --> E["Sanitizar registro en el punto de escritura"]
    B --> E
    E --> T["Guardar solo campos permitidos"]

```

## Diagrama 12: Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/05 S18 - Medir guardrails y equilibrar seguridad y utilidad.md

```mermaid
flowchart LR
    P["Política explícita"] --> B["Casos y etiquetas"]
    B --> R["Ejecutar regla"]
    R --> M["TP, FP, FN y TN"]
    M --> D["Revisar fallos por familia"]
    D --> V["Nueva versión"]
    V --> H["Probar también casos reservados"]

```

## Diagrama 13: Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/07 S18 - Cachés streaming batching y latencia.md

```mermaid
flowchart LR
    Q["Consulta y permisos"] --> S["Buscar respuesta similar"]
    S --> D{"¿Coinciden condiciones de reutilización?"}
    D -->|Sí| C["Devolver respuesta de caché"]
    D -->|No| M["Llamar al modelo"]
    C --> T["Traza del acierto y origen"]
    M --> T

```

## Diagrama 14: Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/08 S18 - Prompts versionados evaluación y rollback.md

```mermaid
flowchart LR
    R["Registro: v1 y v2 conservadas"] --> E["Evaluación y decisión"]
    E --> A["Configuración activa: v2"]
    A --> S["Aplicación sirve v2"]
    D["Se detecta regresión"] --> B["Cambiar activa a v1"]
    B --> T["Aplicación sirve v1"]
    R --> B

```

## Diagrama 15: Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/09 S18 - Laboratorio local de guardrails y versiones.md

```mermaid
flowchart TD
    I["Entrada"] --> G{"¿Bloqueada?"}
    G -->|Sí| B["Respuesta controlada, cero llamadas"]
    G -->|No| R["Redactar y ejecutar simulador"]
    R --> V{"¿Salida permitida?"}
    V -->|Sí| O["Devolver respuesta"]
    V -->|No| L{"¿Queda intento?"}
    L -->|Sí| R
    L -->|No| F["Fallo controlado"]

```

## Diagrama 16: Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/01 Guía - Entender las sesiones 17 y 18.md

```mermaid
flowchart TD
  A[Pregunta del usuario] --> B[Control de entrada]
  B -->|Permitida o corregida| C[Buscar datos autorizados]
  B -->|Bloqueada| X[Respuesta controlada]
  C --> D[Modelo propone una respuesta]
  D --> E[Control de salida]
  E --> F[Respuesta final]
  B -. Resultado protegido .-> T[Traza de la ejecución]
  C -. Paso y duración .-> T
  D -. Modelo tokens y prompt .-> T
  E -. Resultado protegido .-> T
  X -. Bloqueo registrado .-> T
  F --> V[Evaluar calidad y utilidad]

```

## Diagrama 17: Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/02 Caso resuelto - Diagnosticar y mejorar un asistente de ventas.md

```mermaid
flowchart TD
    A[Consulta y tiendas identificadas] --> B[Validar estructura y permisos]
    B -->|Permitida| C[Recuperar las tres filas]
    B -->|No permitida| X[Respuesta controlada]
    C --> D[Calcular el total de referencia]
    C --> E[Generar con prompt v2]
    E --> F[Validar formato contenido y datos]
    F --> G[Comparar total con referencia]
    D --> G
    G --> H[Registrar calidad costo y duración]

```