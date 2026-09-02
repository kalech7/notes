---
title: Cómo redactar una conclusión defendible
aliases:
  - Reportar comparación de modelos
tags:
  - posgrado
  - estadistica
  - comunicacion-cientifica
  - machine-learning
related: "[[00 Índice - Comparación estadística de modelos]]"
---

# Cómo redactar una conclusión defendible

Anterior: [[07 Implementación reproducible en Python]] · Volver al [[00 Índice - Comparación estadística de modelos|índice]] · Siguiente: [[09 Resumen, errores frecuentes y preguntas de repaso]]

Una buena conclusión no enumera números sin conexión. Integra diseño, efecto, incertidumbre y límites en un argumento único.

## 1. Las seis piezas

```mermaid
flowchart LR
    U[1. Unidades<br/>qué fue comparado] --> D[2. Dirección<br/>quién tuvo menor pérdida]
    D --> M[3. Magnitud<br/>diferencia media]
    M --> I[4. Intervalo<br/>precisión]
    I --> R[5. Referencia<br/>prueba y supuestos]
    R --> L[6. Límite<br/>alcance y relevancia]
```

### Cómo leer el diagrama

Cada pieza restringe la siguiente. No puede hablarse de «B es mejor» sin decir en qué unidades, métrica y dirección. El $p$-value aparece después del efecto y el intervalo porque mide extremidad bajo una referencia, no el tamaño del beneficio. El límite cierra el argumento para impedir una generalización mayor que el diseño.

## 2. Plantilla razonada

### Frase 1: diseño

> Se compararon **[número y tipo de unidades]** de forma **[pareada/independiente/estructurada]**, usando **[métrica]** y la diferencia **[A-B o B-A]**.

### Frase 2: efecto y precisión

> La diferencia media observada fue **[valor y unidad]**, favorable a **[modelo]**, con **[intervalo y nivel de confianza]**.

### Frase 3: referencia y límites

> Bajo **[prueba, alternativa y supuestos]**, se obtuvo **[estadístico y p-value]**. El resultado está limitado a **[población/proceso]** y no establece por sí solo **[relevancia práctica, causalidad o superioridad general]**.

## 3. Aplicación al caso conductor

> En diez casos de prueba pareados, evaluados por los mismos modelos ya entrenados, se calculó $d_i=\operatorname{loss}_A(i)-\operatorname{loss}_B(i)$. B redujo la *log-loss* en promedio $0.019$ puntos respecto de A, con $IC_{95\%}=[0.0004,0.0376]$. Bajo una prueba $t$ bilateral sobre las diferencias, $t(9)=2.310$ y $p=0.0463$; una referencia exacta por cambios de signo produjo $p=0.0664$. La fuerza de evidencia depende del contrato inferencial y de una muestra pequeña; el análisis no prueba superioridad general ni relevancia práctica fuera de casos futuros comparables con estos modelos fijos.

Esta redacción incluye los resultados de ambos procedimientos sin presentarlos como votos. También explica que responden a referencias distintas.

> [!note] Cómo incorporar Shapiro-Wilk sin exagerarlo
> En el caso didáctico, Shapiro-Wilk produce $W=0.9752$ y $p=0.9347$. Puede informarse como «no se detectó evidencia contra normalidad en diez diferencias», seguido de la limitación «un $p$ grande con $n=10$ no demuestra normalidad ni independencia». La explicación completa está en [[04A Diagnóstico de normalidad con Shapiro-Wilk]].

## 4. Del lenguaje excesivo al proporcional

| Evita | Problema | Prefiere |
| --- | --- | --- |
| «B es mejor.» | Omite métrica, unidad y alcance. | «B tuvo menor log-loss media en estos diez casos pareados.» |
| «B quedó demostrado como superior.» | Un umbral no demuestra superioridad general. | «El efecto observado favoreció a B bajo el diseño declarado.» |
| «Los modelos son iguales.» | No rechazar no demuestra igualdad. | «El análisis no aportó evidencia suficiente contra la nulidad bajo este procedimiento.» |
| «Hay 95.4 % de probabilidad de mejora.» | Invierte el condicional del $p$-value. | «Bajo $H_0$ y los supuestos, $p=0.0463$ mide extremidad.» |
| «El efecto es significativo, por tanto importa.» | Confunde evidencia con relevancia. | «La importancia debe compararse con costos y un umbral sustantivo.» |
| «Se validó en cinco estudios.» | Los folds del mismo dataset no son estudios independientes. | «Se usó validación cruzada de cinco folds con datos reutilizados.» |

## 5. Cómo hablar del $p$-value

Forma recomendada:

> Bajo $H_0$, el diseño y los supuestos de la prueba $t$, la probabilidad de obtener un estadístico al menos tan extremo como el observado es aproximadamente $0.046$.

Esta frase conserva el condicionamiento. Evita convertir la probabilidad de los datos bajo una hipótesis en probabilidad de la hipótesis dados los datos.

## 6. Cómo hablar del intervalo

Forma recomendada:

> El procedimiento $t$ produjo un intervalo del $95\%$ desde $0.0004$ hasta $0.0376$ puntos de *log-loss* para la diferencia media A-B. El rango incluye mejoras compatibles casi nulas y mejoras de varias centésimas a favor de B.

La segunda oración traduce la escala sin afirmar que todos los valores tengan igual probabilidad posterior.

![[assets/intervalo-efecto.png|900]]

### Qué aporta este gráfico a la redacción

El marcador de efecto muestra dirección y magnitud. La barra muestra precisión. La cercanía del extremo inferior a cero impide convertir un resultado limítrofe en una afirmación rotunda.

## 7. Cómo declarar el alcance

La unidad fija la forma de la generalización:

| Unidad | Redacción de alcance prudente |
| --- | --- |
| Casos | «casos futuros comparables evaluados por estos modelos fijos» |
| Corridas | «nuevas corridas del pipeline bajo el mismo protocolo» |
| Datasets | «nuevas tareas comparables con las estudiadas» |
| Folds | «particiones del mismo dataset»; no llamarlas estudios independientes |

Evita «en general» si no puedes nombrar la población generalizada.

## 8. Superioridad, no diferencia y equivalencia

### $p<0.05$

Clasifica el resultado como extremo bajo un contrato y umbral convencionales. Todavía deben revisarse magnitud, intervalo, supuestos, multiplicidad y alcance.

### $p>0.05$

No demuestra igualdad. Puede reflejar efecto pequeño, muestra pequeña, alta variabilidad o un método poco preciso.

### Equivalencia

Para sostener que A y B son suficientemente similares, primero se fija un margen $[-\delta,+\delta]$ que represente diferencias prácticamente irrelevantes. Después se usa un procedimiento formal de equivalencia y se exige precisión suficiente.

> [!important] Ausencia de evidencia no es evidencia de ausencia
> Una prueba de diferencia y una prueba de equivalencia formulan objetivos distintos.

## 9. Análisis primario y secundarios

Si la prueba $t$ fue primaria y los cambios de signo un análisis de sensibilidad, dilo. Si ambos se decidieron después de mirar los datos, también debe quedar registrado.

Ejemplo:

> La prueba $t$ bilateral se preespecificó como análisis primario. La enumeración de cambios de signo se realizó como análisis de sensibilidad para estudiar la dependencia de la conclusión respecto de la referencia nula.

No presentes un análisis secundario como si siempre hubiera sido el plan principal.

## 10. Lista final de revisión

Antes de cerrar un informe, confirma:

- [ ] Nombré la unidad y la población objetivo.
- [ ] Expliqué por qué los pares son reales.
- [ ] Declaré métrica, resta y dirección de mejora.
- [ ] Reporté diferencias o al menos su dispersión, no solo dos promedios.
- [ ] Informé magnitud en la escala original.
- [ ] Informé intervalo y supuestos.
- [ ] Si informé Shapiro-Wilk, aclaré que diagnostica forma de $d$ y no independencia ni superioridad.
- [ ] Interpreté el $p$-value como extremidad condicionada.
- [ ] No usé $p>0.05$ como prueba de igualdad.
- [ ] Separé relevancia estadística y práctica.
- [ ] Documenté dependencia, multiplicidad y decisiones post hoc.
- [ ] Limité la conclusión a lo que autoriza el diseño.

## 11. Regla para recordar

> [!success]
> **Unidad + dirección + magnitud + precisión + referencia + límite** producen una conclusión defendible. Quitar cualquiera de esas piezas abre un salto lógico.

Anterior: [[07 Implementación reproducible en Python]] · Siguiente: [[09 Resumen, errores frecuentes y preguntas de repaso]]
