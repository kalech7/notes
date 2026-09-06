---
title: Incertidumbre, ablaciones y análisis de errores
tags:
  - master/matematicas-programacion
  - evaluacion
  - ablation
---

# Incertidumbre, ablaciones y análisis de errores

## Una métrica es una estimación

El F1 observado depende de la muestra de sesiones, usuarios y ataques simulados. Reporta incertidumbre respetando grupos.

## Bootstrap agrupado

Remuestrea unidades independientes completas, por ejemplo usuarios. No remuestrees ventanas individualmente si comparten sesión.

Procedimiento:

1. muestrear usuarios con reemplazo;
2. incluir todas sus predicciones;
3. recalcular métrica;
4. repetir;
5. resumir percentiles.

## Ablation study

Una ablación elimina una familia de información manteniendo el protocolo:

| Variante | Pregunta |
|---|---|
| solo tiempo | ¿basta ritmo? |
| solo geometría | ¿basta trayectoria? |
| sin clics | ¿aportan interacción discreta? |
| sin aceleración | ¿las diferencias de segundo orden ayudan? |
| baseline vs Isolation Forest | ¿aporta el algoritmo? |

No cambies simultáneamente features, split y modelo; perderías atribución.

## Análisis de errores

Para falsos rechazos:

- sesión muy corta;
- dispositivo distinto;
- cambio de velocidad;
- pausas atípicas;
- calidad de datos.

Para falsas aceptaciones:

- impostor con estilo similar;
- características demasiado agregadas;
- umbral permisivo;
- perfil legítimo demasiado amplio.

## Estratificación

Compara por usuario, duración, número de eventos y periodo. Hazlo como diagnóstico; muchas comparaciones exploratorias no deben convertirse en conclusiones confirmatorias sin corrección o estudio nuevo.

## Amenazas a la validez

- ataques simulados no equivalen a adversarios reales;
- dataset antiguo o dispositivo específico;
- pocas sesiones de enrolamiento;
- reutilización de impostores;
- selección de características guiada por test;
- drift de comportamiento.

## Privacidad

La dinámica de interacción puede funcionar como dato biométrico conductual. Minimiza almacenamiento, evita publicar trayectorias identificables y documenta consentimiento, finalidad y retención.

## Autoevaluación

1. ¿Qué unidad remuestrearías y por qué?
2. ¿Qué hace interpretable una ablación?
3. ¿Qué diferencia hay entre análisis exploratorio y confirmatorio?
4. Da tres amenazas a la validez externa.

---

Anterior: [[04 Umbrales biométricos - FAR, FRR y EER]] · Siguiente: [[06 Laboratorio del proyecto - dinámica de mouse]]

