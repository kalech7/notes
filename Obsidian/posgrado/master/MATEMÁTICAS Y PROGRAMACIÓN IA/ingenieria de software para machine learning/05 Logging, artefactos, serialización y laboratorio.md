---
title: Logging, artefactos, serialización y laboratorio
tags:
  - master/matematicas-programacion
  - experimentos
  - laboratorio
related:
  - "[[../laboratorios fundamentos ia/ingenieria_software_ml.py]]"
---

# Logging, artefactos, serialización y laboratorio

Archivo: [[../laboratorios fundamentos ia/ingenieria_software_ml.py]].

## Qué registrar

- identificador de corrida;
- hora y versión de código;
- configuración completa;
- versión/hash de datos;
- métricas por partición;
- advertencias y errores;
- rutas y hashes de artefactos.

No registres secretos, tokens ni datos personales innecesarios.

## Log frente a resultado

Un log describe eventos; una tabla de resultados permite análisis. No sustituyas una estructura tabular con miles de líneas de texto.

## Artefactos

```text
runs/2026-09-05T120000Z/
├── config.json
├── metrics.json
├── predictions.csv
├── model.bin
└── manifest.json
```

El manifiesto conserva hash y tamaño para detectar archivos alterados.

## Serialización

Guardar un objeto arbitrario con pickle puede ejecutar código al cargar. Solo carga artefactos confiables y registra versiones. Para intercambio simple prefiere JSON, CSV, Parquet o formatos específicos del modelo.

## Laboratorio

El script construye componentes inyectables:

- `Config` inmutable;
- `FeatureExtractor`;
- `Scorer`;
- `Evaluator`;
- `Experiment`;
- manifiesto con SHA-256.

Pruebas incluidas:

1. misma configuración produce el mismo identificador;
2. una entrada inválida lanza excepción;
3. un scorer falso permite probar evaluación;
4. el manifiesto detecta un cambio;
5. no se mezclan efectos de escritura con cálculo de métricas.

## Criterio de dominio

- [ ] Puedo reconstruir un entorno con lock.
- [ ] Puedo ejecutar tests desde una sesión limpia.
- [ ] Puedo distinguir configuración, estado aprendido y artefacto.
- [ ] Puedo reemplazar un componente mediante un contrato.
- [ ] Puedo auditar qué datos y versión produjeron una métrica.

## Preguntas finales

1. ¿Qué hace reproducible una corrida además de la semilla?
2. ¿Por qué no versionar `.venv`?
3. ¿Qué debe probar un test semántico que una prueba de shape no ve?
4. ¿Por qué guardar hashes?

---

Anterior: [[04 Pruebas unitarias, integración y pruebas semánticas]] · Volver al [[00 Índice y recordatorio - Ingeniería de software para ML]]

