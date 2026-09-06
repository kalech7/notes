---
title: Laboratorio del proyecto - dinámica de mouse
tags:
  - master/matematicas-programacion
  - proyecto
  - laboratorio
related:
  - "[[../proyecto/README - Proyecto de dinámica de mouse]]"
---

# Laboratorio del proyecto: dinámica de mouse

## Objetivo

Ejecutar una línea base completa sobre Balabit sin usar etiquetas de test para entrenar ni calibrar.

Entrada:

```text
training_files/user*/session_*
test_files/user*/session_*
public_labels.csv
```

Salida:

```text
features.csv
predictions.csv
metrics.json
```

## Protocolo por usuario

1. Ordenar sesiones legítimas de training por nombre estable.
2. Separar enrolamiento y validation.
3. Extraer características por sesión.
4. Ajustar scaler y perfil/Isolation Forest en enrolamiento.
5. Calibrar umbral con scores legítimos de validation.
6. Evaluar test con etiquetas solo al final.

## Convención

```text
score alto = más anómalo
label 1 = impostor
predicción 1 = alarma
```

## Pruebas antes de evaluar

- ninguna sesión de enrolamiento aparece en validation/test;
- todas las características son finitas;
- cada fila de features representa una sesión;
- umbral no depende de `public_labels.csv`;
- las etiquetas se unen por nombre de archivo, no por orden de filas.

## Resultados mínimos

Reporta por usuario y global:

- número de sesiones;
- precision y recall de impostor;
- F1;
- FAR y FRR;
- EER exploratorio;
- matriz de confusión;
- distribución de scores.

## Explicación que debes poder dar

> “El perfil aprende exclusivamente sesiones legítimas de enrolamiento. Validation legítimo fija cuánto comportamiento natural estamos dispuestos a rechazar. Las etiquetas del test solo se abren después para medir seguridad y usabilidad. El resultado vale para ataques simulados del dataset, no demuestra detección universal de suplantación.”

## Checklist

- [ ] Ejecuté tests sintéticos.
- [ ] Ejecuté el baseline real.
- [ ] Guardé configuración y versiones.
- [ ] Revisé al menos cinco errores.
- [ ] Comparé baseline e Isolation Forest.
- [ ] Escribí limitaciones y privacidad.

---

Anterior: [[05 Incertidumbre, ablaciones y análisis de errores]] · Volver al [[00 Índice y recordatorio - Anomalías y secuencias]] · Proyecto: [[../proyecto/README - Proyecto de dinámica de mouse]]

