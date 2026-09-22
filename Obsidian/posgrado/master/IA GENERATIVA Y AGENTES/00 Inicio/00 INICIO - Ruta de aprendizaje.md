---
title: "IA generativa y agentes - Ruta de aprendizaje"
tags:
  - maestria/ia-generativa
aliases:
  - IA generativa y agentes
---

# IA generativa y agentes: empieza aquí

Este conjunto cubre las sesiones 00 a 06. Las notas avanzan desde qué es un modelo hasta transformer, preentrenamiento, alineamiento, inferencia, prompting, evaluación experimental y embeddings para recuperación semántica.

> [!tip] Cómo estudiar
> Lee primero la situación concreta, sigue el gráfico y después relaciona cada símbolo con el ejemplo. Al final de cada nota responde las preguntas sin abrir las soluciones. Usa [[27 PRÁCTICA - Sesiones 02 a 05]] para comprobar la segunda mitad del recorrido.

## Mapa visual

Abre [[Mapa de IA generativa y agentes.canvas|Mapa de IA generativa y agentes]] para recorrer las conexiones entre temas.

## 1. Fundamentos de IA

1. [[01 S00 - Qué es la IA y cómo evaluar inteligencia|Qué es la IA y cómo comprobar una capacidad]].
2. [[02 S00 - Reglas modelos y aprendizaje desde datos|Qué es un modelo y cómo aprende de ejemplos]].
3. [[03 S00 - Perceptrón redes neuronales y XOR|Cómo una neurona artificial toma una decisión]].
4. [[04 S00 - Correlación causalidad y límites de las predicciones|Por qué predecir no demuestra causalidad]].

## 2. Probabilidad y modelos generativos

1. [[05 S01 - Probabilidad y teorema de Bayes paso a paso|Bayes paso a paso]].
2. [[06 S01 - Modelos discriminativos y generativos|Discriminativo frente a generativo]].
3. [[07 S01 - Naive Bayes con un ejemplo de spam|Naive Bayes]].
4. [[08 S01 - GMM variables latentes y algoritmo EM|GMM y EM]].
5. [[09 S01 - Markov HMM y generación con bigramas|Markov, HMM y bigramas]].
6. [[10 S01 - VAE espacio latente y ELBO|VAE, latente continuo y ELBO]].
7. [[11 S01 - Del bigrama al LLM y primeros conceptos de agentes|Puente hacia LLM y agentes]].

Ampliaciones: [[15 AMPLIACIÓN - Bayes incertidumbre y suavizado con números|incertidumbre bayesiana]] y [[17 PRÁCTICA - Modelos generativos Naive Bayes GMM y bigramas|práctica con el notebook de modelos generativos]].

## 3. Transformers

1. [[18 S02 - Transformer de extremo a extremo|Pipeline completo del transformer]].
2. [[19 S02 - Atención Q K V paso a paso|Atención Q, K y V con números]].
3. [[20 S02 - Posición familias y decoder-only|Posición, encoder, decoder y decoder-only]].

## 4. Entrenamiento y alineamiento

1. [[16 AMPLIACIÓN - Cómo aprende un LLM desde el texto|Ejemplo pequeño: del texto a la pérdida]].
2. [[21 S03 - Preentrenamiento autosupervisado y MLE|Preentrenamiento, MLE, gradientes y perplejidad]].
3. [[22 S03 - SFT RLHF DPO y Constitutional AI|SFT y ajuste por preferencias]].

## 5. Inferencia y prompting

1. [[23 S04 - Greedy temperatura top-k y top-p|Decodificación: greedy, temperatura, top-k y top-p]].
2. [[24 S04 - Zero-shot few-shot y razonamiento|Zero-shot, few-shot y razonamiento]].
3. [[25 S04 - Salidas estructuradas costo y razonamiento interno|JSON, esquemas, costo y test-time compute]].

## 6. Talleres y práctica

- [[13 PRÁCTICA - Repaso integrado y ejercicios resueltos|Repaso de sesiones 00 y 01]].
- [[17 PRÁCTICA - Modelos generativos Naive Bayes GMM y bigramas|Notebook de Naive Bayes, GMM y bigramas]].
- [[26 S05 - Diseñar una comparación de modelos|Cómo comparar modelos con un experimento controlado]].
- [[27 PRÁCTICA - Sesiones 02 a 05|Ejercicios resueltos de transformer, alineamiento, inferencia y evaluación]].

## 7. Embeddings y recuperación semántica

1. [[28 S06 - Qué es un embedding y qué significa cercanía|Qué representa un embedding y qué quiere decir cercanía]].
2. [[29 S06 - De tokens a un vector de texto|Token, salida contextual y pooling]].
3. [[30 S06 - Cómo se entrena SBERT y por qué permite buscar|SBERT, aprendizaje entre textos y bi-encoder]].
4. [[31 S06 - Coseno producto punto y normalización|Coseno, producto punto, distancia y normalización con números]].
5. [[32 S06 - Elegir modelo y reconocer límites|Cómo elegir un modelo y detectar límites de recuperación]].
6. [[33 PRÁCTICA - Embeddings y similitud semántica|Ejercicios resueltos de la sesión 06]].

## 8. Referencias

- [[12 GLOSARIO - Diccionario explicado para estas sesiones|Glosario explicado]].
- [[14 FUENTES - Materiales y mapa de cobertura|Fuentes y cobertura por sesión]].

## Estructura de carpetas

```text
00 Inicio/
01 Fundamentos de IA/
02 Modelos probabilísticos y generativos/
03 Transformers/
04 Entrenamiento y alineamiento/
05 Inferencia y prompting/
06 Talleres y práctica/
07 Embeddings y recuperación/
90 Referencias/
Materiales/
Recursos visuales/
talleres/
```

Los PDF originales se conservan en `Materiales`. Los gráficos propios están en `Recursos visuales` en PNG y SVG. Los requisitos de evaluación encontrados en las sesiones se explican como contenido del curso; no se trataron como instrucciones para modificar estas notas.
