La conducta racional se refiere al proceso mediante el cual un sistema de Inteligencia Artificial toma decisiones óptimas y maximiza los resultados esperados según su criterio de desempeño.
![[Pasted image 20231115142718.png]]

> [!info] Explicación
> **¿Qué es la Conducta Racional?** En Inteligencia Artificial, ser "racional" no significa ser inteligente al nivel humano, sino hacer lo correcto matemáticamente hablando. Un agente es racional si elige la acción que maximiza su medida de rendimiento esperada, basándose en la información que percibe del entorno y su propio conocimiento interno.

## Principios fundamentales 
- **Adquisición de información:** El sistema debe ser capaz de obtener y procesar datos relevantes para su entorno y sus tareas específicas.
- **Razonamiento y procesamiento de información:** El sistema debe analizar, interpretar y evaluar la información adquirida para identificar patrones, relaciones y posibles acciones a tomar.
- **Selección de acciones:** La IA debe elegir las acciones más apropiadas para alcanzar sus objetivos, teniendo en cuenta siempre las restricciones y los recursos que tiene disponibles.
- **Aprendizaje y adaptabilidad:** El sistema debe aprender de sus experiencias pasadas y adaptarse a nuevas situaciones o a cambios imprevistos en el entorno, mejorando continuamente su desempeño.

> [!info] Explicación
> Estos cuatro pilares permiten pasar de un sistema reactivo y ciego (que solo reacciona por reflejos) a un sistema verdaderamente autónomo, capaz de planear a futuro, comprender contextos cambiantes y ajustar sus estrategias.

## Aplicaciones de la conducta racional 
- **Sistemas expertos:** Proporcionan soluciones o diagnósticos basados en conocimiento que fue previamente adquirido de expertos humanos (ej. sistemas de diagnóstico médico).
- **Planificación y optimización:** Identifican y seleccionan una secuencia de acciones para lograr metas de la manera más eficiente posible, ahorrando tiempo o recursos.
- **Aprendizaje automático:** Permite que el sistema mejore su rendimiento a través de la experiencia continua y la adaptación a nuevos datos.
- **Resolución de problemas:** Permite al sistema identificar y superar obstáculos para alcanzar los objetivos definidos.

## Agente
Un agente es un ente o entidad que percibe su entorno mediante el uso de sensores y actúa sobre ese mismo entorno mediante el uso de actuadores.

|          | Sensores                            | Actuadores                                 |
| -------- | ----------------------------------- | ------------------------------------------ |
| Humanos  | Ojos, oídos, nariz, tacto           | Manos, pies, cuerdas vocales               |
| Robots   | Cámaras, sensores infrarrojos, láseres| Motores, ruedas, brazos mecánicos          |
| Software | Pulsaciones de teclado, datos de red| Pantallas, archivos de salida, envíos de red|

### Agentes genéricos
Son agentes que perciben el ambiente por medio de sensores clásicos como teclados, micrófonos o cámaras de video. Como respuesta, sus efectores o actuadores modifican el ambiente, utilizando elementos como monitores o impresoras. 
Ejemplo clásico: Un termostato (su sensor es el termómetro, su actuador es el calentador).
![[Pasted image 20231115145138.png]]

### Agentes inteligentes
Son entidades computacionales que perciben su entorno de forma compleja y actúan según su información y sus objetivos predefinidos, con aplicaciones avanzadas en robótica, sistemas de recomendación y asistentes virtuales.

```mermaid
flowchart LR
    subgraph Entorno [Entorno (Medio Ambiente)]
        E_State[Estado del Mundo]
    end

    subgraph Agente [Agente Inteligente]
        S[Sensores]
        P[Procesamiento / Toma de decisiones]
        A[Actuadores]
        
        S --> P
        P --> A
    end

    E_State -- "Percepciones" --> S
    A -- "Acciones" --> E_State
```

Sus componentes principales son:
- **Sensores:** Perciben el entorno constantemente y recolectan información.
- **Procesadores:** Realizan el razonamiento lógico y la toma de decisiones, basándose en la información recolectada y en el modelo interno.
- **Actuadores:** Ejecutan acciones físicas o lógicas en el entorno para alterarlo.

## Tipos de agentes
- **Agentes reactivos simples:** Actúan únicamente según reglas predefinidas de tipo "condición-acción", basándose exclusivamente en la percepción actual del entorno, sin memoria del pasado.
- **Agentes basados en modelos:** Utilizan un modelo interno del entorno (memoria de estado) que les permite saber cómo funciona el mundo y qué pasó antes para tomar decisiones.
- **Agentes basados en objetivos:** Además de conocer el estado actual, actúan en función de alcanzar metas específicas, evaluando posibles futuros para decidir qué hacer.
- **Agentes basados en utilidad:** Toman decisiones complejas basadas en la maximización de la utilidad esperada, considerando que algunas metas pueden ser más deseables, seguras o eficientes que otras.
- **Agentes de aprendizaje:** Son capaces de aprender y mejorar su desempeño de forma autónoma a lo largo del tiempo, generando nuevas reglas y ajustando su comportamiento ante la retroalimentación.

> [!info] Explicación
> **Evolución de los agentes:** Esta clasificación va desde lo más básico (reaccionar sin pensar) hasta lo más avanzado (aprender de los errores). Un agente de utilidad buscará siempre el camino más "feliz" (óptimo), mientras que el agente de aprendizaje será capaz de descubrir por sí mismo cuál es ese camino sin que un programador se lo dicte.

## Notas relacionadas
- [[problemas en IA]]
- [[machine learning]]
- [[web semantica]]
