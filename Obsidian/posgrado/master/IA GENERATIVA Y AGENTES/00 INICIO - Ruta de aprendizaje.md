---
title: "IA generativa y agentes - Ruta de aprendizaje"
tags:
  - maestria/ia-generativa
---

# IA generativa y agentes

Apuntes para aprender las **sesiones 00 y 01**, con explicaciones progresivas, ejemplos resueltos y preguntas desplegables. Se omitieron de los apuntes la portada y la presentación personal del profesor de la sesión 00, incluidos sus datos de contacto. Los PDF originales se conservan íntegros como material de consulta.

## Cómo estudiar

1. Lee una nota y explica su idea principal sin mirar.
2. Resuelve las preguntas del final antes de abrir las respuestas.
3. **Haz clic en el título o en la flecha de cada pregunta** para desplegar la respuesta en Obsidian, en vista de lectura o vista previa en vivo. En modo fuente verás el código Markdown.
4. Repite al día siguiente las preguntas que fallaste. Avanza cuando puedas explicar el mecanismo, no solo recordar el nombre.

Los ejemplos numéricos y aclaraciones son elaboración didáctica. Las referencias al pie de cada introducción indican qué páginas del material sustentan el tema. Los números corresponden a las páginas del PDF.

## Sesión 00: entender de dónde viene la IA

- [[01 S00 - Qué es la IA y cómo evaluar inteligencia]]
- [[02 S00 - Reglas modelos y aprendizaje desde datos]]
- [[03 S00 - Perceptrón redes neuronales y XOR]]
- [[04 S00 - Correlación causalidad y límites de las predicciones]]

**Al terminar:** deberías distinguir automatización, aprendizaje, evaluación de comportamiento y causalidad.

## Sesión 01: entender qué hace generativo a un modelo

Conviene empezar por Bayes, aunque la presentación introduzca primero la clasificación de modelos.

- [[05 S01 - Probabilidad y teorema de Bayes paso a paso]]
- [[06 S01 - Modelos discriminativos y generativos]]
- [[07 S01 - Naive Bayes con un ejemplo de spam]]
- [[08 S01 - GMM variables latentes y algoritmo EM]]
- [[09 S01 - Markov HMM y generación con bigramas]]
- [[10 S01 - VAE espacio latente y ELBO]]
- [[11 S01 - Del bigrama al LLM y primeros conceptos de agentes]]

**Al terminar:** deberías explicar qué distribución modela cada familia, cómo genera y qué información pierde con sus supuestos.

## Complementos de los libros, explicados dentro de tus notas

Las notas 01–11 incorporan ahora explicaciones de secciones consultadas directamente en los cuatro libros. Incluyen ejemplos de evaluación, sobreajuste, convergencia, incertidumbre, decisiones, EM y modelos de lenguaje. Las referencias son opcionales para consultar: la explicación está desarrollada aquí.

Los dos desarrollos más largos están separados para leerlos paso a paso:

- [[15 AMPLIACIÓN - Bayes incertidumbre y suavizado con números]]: después de la nota 05.
- [[16 AMPLIACIÓN - Cómo aprende un LLM desde el texto]]: después de la nota 11.

## Apoyo y práctica

- [[12 GLOSARIO - Diccionario explicado para estas sesiones]]
- [[13 PRÁCTICA - Repaso integrado y ejercicios resueltos]]
- [[14 FUENTES - Materiales y mapa de cobertura]]

## Ruta en bloques pequeños

| Bloque | Notas | Resultado que debes poder explicar |
| --- | --- | --- |
| 1 | 01–02 | Qué se evalúa y de dónde viene el conocimiento |
| 2 | 03–04 | Cómo decide una neurona y por qué predecir no prueba causas |
| 3 | 05–06 | Cómo usar Bayes y distinguir los enfoques |
| 4 | 07–08 | Cómo generar con Naive Bayes y GMM |
| 5 | 09–10 | Qué aportan las secuencias y los latentes continuos |
| 6 | 11–13 | Cómo conectar estas ideas con LLM y resolver ejercicios |

No necesitas leer los libros completos para seguir estos apuntes. La nota de fuentes distingue los materiales base de las lecturas de ampliación. El tema de agentes aparece aquí como orientación inicial; no se presenta como una sesión desarrollada que no está entre los PDF aportados.
